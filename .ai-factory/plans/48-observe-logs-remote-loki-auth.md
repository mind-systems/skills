# Plan: observe-logs: remote Loki auth

## Context
Add optional `Authorization`-header support to `query-loki.sh` so the same skill hits a local unauthenticated Loki (default) or a remote Grafana Service Account proxy, driven entirely by two env vars with nothing credential-specific hardcoded.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Known risk (out of scope, note only)
`check_backend` probes `${LOKI_URL}/ready` and treats any non-`2xx` as "backend down → exit 1". In remote mode `LOKI_URL` is a Grafana datasource-proxy base (`/api/datasources/proxy/uid/<uid>`), and `/ready` is a Loki *root* endpoint (not under `/loki/api/v1/`). The spec's verification assumes the proxy forwards `/ready` (bad token → 401), but a valid-token 2xx for the proxied `/ready` is not confirmed here. If a given Grafana returns 404/403 for the proxied `/ready` while `query_range` works, the skill would wrongly report the backend down and block all queries. With `Testing: no` this cannot be exercised in this change; it is a documented Grafana-config dependency, not a code fix in this milestone. Flagged for the implementer — do not silently widen `check_backend`'s success condition without evidence.

## Tasks

### Phase 1: Script auth support

- [x] **Task 1: Add auth config + header-args to the three curl call-sites**
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  In the Configuration section (after the `LOKI_URL="${OBS_LOKI_URL:-http://localhost:3100}"` line at line 10) add `LOKI_AUTH="${OBS_LOKI_AUTH:-}"`.
  Add a helper that builds the curl auth arguments into a bash array **and use array expansion at the call-sites** — do NOT use an unquoted `$(...)` command substitution: the header value `Bearer <token>` contains a space and word-splitting would shatter it into separate argv elements, corrupting the header. Concretely, populate a global once near the config:
  ```bash
  AUTH_ARGS=()
  [[ -n "$LOKI_AUTH" ]] && AUTH_ARGS=(-H "Authorization: ${LOKI_AUTH}")
  ```
  Insert the auth args into each `curl` invocation using the **bash-3.2-safe guarded expansion** — the script is `#!/usr/bin/env bash` and targets macOS (see the BSD-awk fallback comments), where `/bin/bash` is **3.2.57**. Under `set -u`, a bare `"${AUTH_ARGS[@]}"` on an empty array aborts with `AUTH_ARGS[@]: unbound variable` on bash < 4.4 — which would break the default no-auth path on stock macOS. Use instead at every call-site:
  ```bash
  curl ... ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} ...
  ```
  This expands to nothing when the array is empty and preserves the embedded space in `Authorization: Bearer <token>` when set (verified on bash 3.2.57). This matches the existing script's discipline of never value-expanding a possibly-empty array unguarded (cf. `cmd_window`'s `${#parts[@]} -gt 0` guard, lines 404-410). The two sites:
  1. `check_backend` — the `/ready` probe curl (lines 20-22).
  2. `query_range` — the `query_range` GET curl (lines 103-110).
  These are the **only two** `curl` invocations in `query-loki.sh`. The spec's "three sites: `check_backend`, `query_range`, `/ready` check" miscounts: `check_backend` **is** the sole `/ready` caller, so the `/ready` check and site 1 are the same curl — there is no third distinct site. Patch both; if any other `curl` targeting `${LOKI_URL}` is found during implementation, patch it the same way.
  When both env vars are unset, `AUTH_ARGS` is empty and no `-H` is added — byte-identical behavior to today (the required no-op default).
  Do NOT log or echo the header value anywhere (no credential leakage to stdout/stderr).

- [x] **Task 2: Document `OBS_LOKI_AUTH` in the script usage heredoc**
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  In the `usage()` heredoc `Environment:` block (lines 437-438) add a line for `OBS_LOKI_AUTH` under the existing `OBS_LOKI_URL` line — e.g. `OBS_LOKI_AUTH  Full Authorization header value (default: unset — no auth)`. Keep the existing `OBS_LOKI_URL` line unchanged.

### Phase 2: Skill documentation

- [x] **Task 3: Replace the SKILL.md Endpoint section**
  Files: `src/skills/observe-logs/SKILL.md`
  Replace the current `## Endpoint` section (SKILL.md lines 44-54: the single-var prose + the one `export OBS_LOKI_URL` example) with the two-row variable table and the local/remote examples from the spec (`.ai-factory/notes/26-observe-logs-remote-auth.md`, lines 51-72). Content to render:
  - Intro sentence: two env vars control the connection; no hardcoded fallback beyond the local default; the skill never stores or assumes a credential.
  - Two-row table: `OBS_LOKI_URL` → `http://localhost:3100` → Loki base URL; `OBS_LOKI_AUTH` → _(unset)_ → Full `Authorization` header value.
  - **Local backend (no auth):** leave both unset.
  - **Remote via Grafana Service Account:** set both, datasource UID embedded in the URL — include the `export OBS_LOKI_URL=https://grafana.example.com/api/datasources/proxy/uid/<uid>` and `export OBS_LOKI_AUTH="Bearer <service-account-token>"` example block.
  - Closing note: set these in the shell environment or a secrets manager — never in committed files.
  Preserve the existing "backend is down → one clear line + recovery hint" paragraph (lines 53-54) below the new content, and keep the trailing `---` separator before `## Running the script`.

- [x] **Task 4: Keep the Raw LogQL templates section consistent with remote auth**
  Files: `src/skills/observe-logs/SKILL.md`
  The `## Raw LogQL templates` block (lines 170-197) shows hand-run `curl -sG "${OBS_LOKI_URL}/..."` / `curl -s "${OBS_LOKI_URL}/..."` examples with no `Authorization` header — against a remote authenticated backend these return 401, contradicting the "same skill hits local or remote" goal. Add a **one-line caveat** immediately under the "For ad-hoc queries..." intro (line 172), e.g.: "For a remote authenticated backend, add `-H \"Authorization: ${OBS_LOKI_AUTH}\"` to each `curl` below (omit it when running against local Loki)." Do NOT rewrite every example — the caveat keeps the block readable while closing the gap. This is documentation only; no script change.

## Code Review Summary

**Files Reviewed:** 1 plan (`48-observe-logs-remote-loki-auth.md`) against 2 target files (`query-loki.sh`, `SKILL.md`) + spec note `26-observe-logs-remote-auth.md`
**Risk Level:** 🔴 High — one confirmed, reproducible bug in the plan's core instruction that breaks the default (no-auth) path on macOS system bash.

### Context Gates

- **Roadmap** (`ROADMAP.md:107`): ✅ Milestone "observe-logs: remote Loki auth" is present and unchecked; plan heading matches the milestone title; `Spec:` points to `.ai-factory/notes/26-observe-logs-remote-auth.md`, which exists and matches the plan's scope. Linkage intact.
- **Architecture** (`ARCHITECTURE.md`): ✅ No boundary/dependency concern — the change is an env-var + curl-header addition inside a single leaf skill script; no cross-skill contract touched.
- **Rules** (`RULES.md`): ⚠️ WARN — file absent (optional). No convention gate to apply.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): ⚠️ WARN — absent (optional). No project overrides to apply.

### Critical Issues

**C1 — `"${AUTH_ARGS[@]}"` is NOT safe-when-empty under `set -u` on bash < 4.4; this breaks the default local path on macOS.**
Location: Task 1, the bolded claim *"Because the script runs under `set -u`, always expand as `"${AUTH_ARGS[@]}"` (safe when empty)."*

This claim is false on bash 3.2–4.3. macOS ships **bash 3.2.57** as `/bin/bash`, and `#!/usr/bin/env bash` will resolve to it on any machine without a newer bash first in `PATH`. The script clearly targets macOS — see the BSD-awk fallback comments (`format_response`, lines 71–72). Reproduced on the review machine (bash 3.2.57):

```
$ bash -c 'set -euo pipefail; a=(); printf "%s\n" "${a[@]}"'
bash: a[@]: unbound variable   # exit 1
```

So when both env vars are unset — the **required no-op default** the plan promises to keep "byte-identical" — the very first `curl ... "${AUTH_ARGS[@]}" ...` would abort the script with `AUTH_ARGS[@]: unbound variable`. The default path (local, no auth) would stop working entirely on stock macOS.

Note this is exactly why the *existing* script never expands an empty array by value: `cmd_window` guards with `if [[ ${#parts[@]} -gt 0 ]]` before touching `${parts[*]}` (lines 404–410). The plan would introduce the first unconditional empty-array value-expansion in the file, defeating that discipline.

**Fix:** use the bash-3.2-safe guarded expansion at each call-site:
```bash
curl ... ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} ...
```
Verified on bash 3.2.57 — expands to nothing when empty, and preserves the embedded space in `Authorization: Bearer <token>` when set. The plan's array-vs-word-splitting reasoning is otherwise correct; only the empty-case expansion syntax must change. Update the bolded instruction accordingly so the implementer doesn't copy the unsafe form verbatim.

### Non-Blocking Issues

**W1 — Raw LogQL templates in SKILL.md stay unauthenticated (documentation gap).**
The plan patches only the script's three (really two — see below) curl sites and the Endpoint prose. It does not touch the `## Raw LogQL templates` block (SKILL.md lines 170–197), whose `curl -sG "${OBS_LOKI_URL}/..."` examples carry no `Authorization` header. Against a remote authenticated backend those hand-run examples return 401, contradicting the skill's stated goal ("same skill hits local or remote"). Recommend the plan either add `-H "Authorization: ${OBS_LOKI_AUTH}"` (or a one-line caveat) to that block, or explicitly scope it out with a rationale. Currently it is silently out of scope.

**W2 — `/ready` health check through the Grafana datasource proxy is unverified.**
`check_backend` probes `${LOKI_URL}/ready` and treats any non-`2xx` as "backend down → exit 1" (script lines 24–28). For the remote mode, `LOKI_URL` is a Grafana datasource-proxy base (`/api/datasources/proxy/uid/<uid>`); `/ready` is a Loki *root* endpoint, not under `/loki/api/v1/`. The spec's own verification note assumes the proxy forwards `/ready` (bad token → 401), but a valid-token 2xx for `/ready` through the proxy is not confirmed. If a given Grafana returns 404/403 for the proxied `/ready` while `query_range` works, the skill would wrongly report the backend down and block all queries. With `Testing: no`, this can't be exercised here — worth a note in the plan (or a fallback that treats a reachable-but-non-ready proxy gracefully). Low likelihood, real blast radius.

### Positive Notes

- **Good correction of the spec's buggy approach.** The spec note (lines 42–47) prescribes `auth_header() { ... echo "-H" "Authorization: ..."; }` invoked as unquoted `$(auth_header)` — which word-splits `Bearer <token>` on the space and corrupts the header. The plan correctly rejects this in favor of a bash array, and explains exactly why. That is the right call; the spec note is research-genre, not contract text, so the deviation is justified and well-documented.
- **Accurate line references and honest handling of the spec's miscount.** The spec claims "three curl sites: `check_backend`, `query_range`, `/ready` check", but `check_backend` *is* the sole `/ready` caller — there are only **two** distinct curl invocations in the script (lines 20–22 and 103–110). Task 1 catches this, reconciles it explicitly, and instructs patching both plus any other `${LOKI_URL}` curl "if present." Confirmed: those are the only two `curl` calls in `query-loki.sh`.
- **Security discipline is right:** no logging/echoing of the header value (Task 1), credentials only via env/secrets manager, never committed (Task 3). Matches the read-only, no-hardcoded-vendor posture of the skill.
- **Endpoint/usage edits** (Tasks 2 & 3) reference correct line ranges (usage heredoc `Environment:` at 437–438; Endpoint section 44–54) and correctly preserve the backend-down paragraph and trailing `---`. The usage heredoc is `<<'EOF'` (quoted), so the added plain line needs no escaping — fine.

---

**Verdict:** Not a pass. Fix **C1** (the empty-array expansion syntax) before implementation — as written, Task 1 breaks the default no-auth path on the repo's own target platform. Address W1/W2 or scope them out explicitly.

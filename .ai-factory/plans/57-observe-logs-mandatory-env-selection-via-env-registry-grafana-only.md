# Plan: observe-logs: mandatory env selection via `.env` registry (Grafana-only)

## Context
Move `observe-logs` from a single hardcoded Loki endpoint to mandatory environment selection: a pipe-delimited `.env` registry next to the skill, a required top-level `--env <name>` flag that resolves the Grafana proxy URL + Bearer token, and no localhost/no-auth fallback.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Registry file and gitignore

- [x] **Task 1: Add committed `.env.example` registry template**
  Files: `src/skills/observe-logs/.env.example`
  Create a committed example registry. Short header comment: copy to `.env`, run `chmod 600 .env`, one environment per line in the format `<env-name>|<grafana-proxy-url-with-uid>|<authorization-header-value>`; `#` comments and blank lines are ignored; the file is parsed, never sourced. Provide three commented sample lines keyed `stage` / `dev` / `prod`, each using the observed Grafana datasource-proxy shape `https://<grafana-host>/api/datasources/proxy/uid/<uid>` and auth `Bearer glsa_<token>` with `<uid>` / `<token>` placeholders. Keep it terse — it documents format, not usage.

- [x] **Task 2: Gitignore the real `.env`, keep `.env.example` tracked**
  Files: `.gitignore`
  Add `/src/skills/observe-logs/.env` to the repo-root `.gitignore` so the user-filled registry with tokens is never committed. Do NOT add a pattern that would also ignore `.env.example` (use the exact path, not `.env*`). `.env.example` must stay tracked.

### Phase 2: Script — env resolution

- [x] **Task 3: Rewrite `query-loki.sh` config + main dispatch for mandatory `--env`** (depends on Task 1)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Remove the `http://localhost:3100` default and the implicit no-auth path. Concretely:
  - Delete the `LOKI_URL="${OBS_LOKI_URL:-http://localhost:3100}"` / `LOKI_AUTH="${OBS_LOKI_AUTH:-}"` defaults; `LOKI_URL` and `LOKI_AUTH` are now populated only by env resolution.
  - Resolve the registry path from the script's own location via `${BASH_SOURCE[0]}` — compute `<script-dir>` (e.g. `dirname "${BASH_SOURCE[0]}"`) and read `<script-dir>/../.env`. Never use `$PWD`; this is what makes it work through the `~/.claude/skills` symlink.
  - Add a top-level `--env <name>` parse at the very start of main dispatch, **before** `check_backend` runs (check_backend needs the resolved URL). Accept `--env` as the leading flag (spec example: `query-loki.sh --env stage window 30m --project mind`), capture its value, and strip both tokens from the argument list so the remaining args (`since-restart` / `trace` / `window` + their existing flags) reach the unchanged per-subcommand parsers untouched.
  - Resolve the entry by parsing (never sourcing) `.env` with `while IFS='|' read -r name url auth`, skipping blank lines and lines beginning with `#`; on the line whose first field equals the requested name, set `LOKI_URL="$url"` and `LOKI_AUTH="$auth"`. The space inside `Bearer glsa_…` stays intact because auth is the trailing field.
  - Build `AUTH_ARGS` from `LOKI_AUTH` after resolution (keep the existing bash-3.2-safe `${AUTH_ARGS[@]+...}` guard pattern); the three curl sites (`check_backend`, `query_range`, `/ready`) stay otherwise unchanged.
  - Hard-error paths (no fallback, no network call): (a) no `--env` given → error and list the available environment names read from `.env`; (b) unknown `--env` name → error and list available names; (c) `.env` file absent → error instructing to copy `.env.example` to `.env`. Derive the "available names" list from the first pipe field of each non-comment, non-blank line.
  - Keep bash 3.2 (macOS) compatibility and all subcommand semantics, pagination, and `--project` / `--service` / `--level` / `--limit` filters untouched.

- [x] **Task 4: Update `usage()` environment block in the script** (depends on Task 3)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Rewrite the `Environment:` section of `usage()` to describe the new model: a required top-level `--env <name>` resolved from the `.env` registry next to the script (copied from `.env.example`); remove the `OBS_LOKI_URL` default / `OBS_LOKI_AUTH` unset rows. Add `--env <name>` to the top-line usage syntax. Keep the Notes (label schema, read-only) unchanged.

### Phase 3: SKILL.md rewrite

- [x] **Task 5: Lean, agent-facing Endpoint rewrite in SKILL.md** (depends on Task 3)
  Files: `src/skills/observe-logs/SKILL.md`
  Rewrite the `## Endpoint` section for the agent (the sole reader), keeping it lean — not a user manual:
  - Environments live in `.env` next to the skill (user copies `.env.example`, fills `stage`/`dev`/`prod`, `chmod 600`).
  - `--env <name>` is **required** on every invocation; there is no default endpoint and no direct-Loki path.
  - Infer `--project` from the current project/repo (mind → `--project mind`, tradeoxy → `--project tradeoxy`); the user names only the environment, overridable if they name a project.
  - `/observe-logs <env>` ⇒ a recent `window` slice for the current project unless the user asks for `since-restart` / `trace`; no environment given ⇒ do not guess, ask or let the script error.
  - Drop the two-variable table, the "export before each call" guidance, and the local/remote split. Update the `argument-hint` frontmatter and the `bash scripts/query-loki.sh …` invocation examples throughout so they include `--env <name>`.
  - In the `## Raw LogQL templates` section, drop the local-vs-remote auth phrasing and reflect that `OBS_LOKI_URL` / `OBS_LOKI_AUTH` are no longer user-exported (either update the templates to note they come from the registry via `--env`, or trim the auth caveat) — keep it lean.
  - Preserve the `## Label schema`, subcommand descriptions, and `## Read-only discipline` sections; only the endpoint/auth-facing guidance changes.

## Commit Plan
- **Commit 1** (after tasks 1-2): "Add observe-logs env registry template and gitignore the real .env"
- **Commit 2** (after tasks 3-5): "Require --env selection resolved from the .env registry in observe-logs"

# observe-logs: mandatory environment selection via `.env` registry (Grafana-only)

**Date:** 2026-07-07
**Source:** conversation context

## Summary

`observe-logs` moves from a single hardcoded endpoint to **mandatory environment
selection**. Environments (`stage` / `dev` / `prod`) live in a pipe-delimited registry
**next to the skill** — `.env.example` committed, real `.env` gitignored and
user-filled. The agent invokes `/observe-logs <env>` and gets logs for the **current
project** on that environment. There is **no default endpoint**: the old direct-Loki
`http://localhost:3100` path is removed — everything now goes through Grafana's
datasource proxy. No environment named ⇒ hard error.

## Current state

- Skill at `src/skills/observe-logs/`, symlinked into `~/.claude/skills/observe-logs`.
  Both paths expose the same inode — a file dropped in the skill root is visible
  identically through the symlink and the real repo path.
- `scripts/query-loki.sh` today is **single-endpoint**: `OBS_LOKI_URL`
  (default `http://localhost:3100`) / `OBS_LOKI_AUTH` (default unset → no auth).
  Subcommands `since-restart <svc>` / `trace <id>` / `window <range>` with `--level` /
  `--project` / `--service` / `--limit`. Auth wired at three `curl` sites
  (`check_backend`, `query_range`, `/ready`) from note `26-observe-logs-remote-auth.md`.
- **The stack has moved to Grafana. Direct Loki access is gone.** All reads go through
  Grafana's datasource proxy:
  `https://<grafana-host>/api/datasources/proxy/uid/<datasource-uid>`, auth
  `Bearer <grafana-service-account-token>` (`glsa_…`). The registry keys are
  **`stage` / `dev` / `prod`** — each mapped by the user to its Grafana endpoint in
  `.env`. Observed endpoints so far: `http://localhost:3000/…` and
  `https://grafana-staging.mind-awake.life/…`, same datasource UID
  `P8E80F9AEF21F6940`, differing only in host/token.
- Reaching a given environment today means hand-exporting the two env vars before each
  call. That is the pain being removed. The primary consumer is the **agent**, not a
  human reading SKILL.md.

## Target / chosen design

Settled by the user — state it, do not re-open.

**No default. Environment is mandatory.** Remove the `http://localhost:3100` default
and the unauthenticated direct-Loki path entirely. Every invocation resolves an
endpoint+token from the registry. No environment selected, or an unknown name ⇒ **hard
error** that lists the available environment names from `.env`. The agent never guesses
an endpoint and never falls back to raw Loki.

**Storage.** A registry file in the skill root: `.env.example` (committed, documents
the format) plus `.env` (gitignored, `chmod 600`, user-filled). Tokens are read-only
Grafana service-account tokens on a personal FileVault laptop → plaintext in a
gitignored `.env` is the accepted store. Keychain / 1Password / MCP / global
`settings.json` `env` all rejected as overkill for on-demand, rarely-used reads — no
daemon, no deploy, no per-project install.

**Format.** One environment per line, pipe-delimited:

```
<env-name>|<grafana-proxy-url-with-uid>|<authorization-header-value>
```

`#` comments and blank lines ignored. **Parsed with `while IFS='|' read` — never
sourced** (sourcing would execute arbitrary shell; parsing also treats the space in
`Bearer glsa…` as the trailing field). Each line bundles the non-secret parts (name,
Grafana URL incl. UID) and the secret token together, for simplicity.

**Selection.** A top-level `--env <name>` flag, **required**, parsed in the main
dispatch before the subcommand runs and stripped from the argument list so the existing
per-subcommand parsers never see it. On match, set `OBS_LOKI_URL` + `OBS_LOKI_AUTH`
from the entry, then dispatch as today. Example:
`query-loki.sh --env staging window 30m --project mind`.

**Resolution.** Locate `.env` relative to the **script's own location** via
`${BASH_SOURCE[0]}` (`<script-dir>/../.env`), never `$PWD` — this is what makes it work
through the `~/.claude/skills` symlink (proven by inode equality).

**Projects vs environments.** `project` (mind, tradeoxy, …) stays a Loki
**index-label filter** (`--project`), not part of the registry — adding a project is
zero new config. Only the **environment** axis maps to a distinct endpoint+token.

## Agent-facing behavior (`/observe-logs <env>`)

This is the whole point — designed for the agent, which is the sole reader of SKILL.md.

- **Argument = environment**, required (`stage` / `dev` / `prod`).
  `/observe-logs stage` ⇒ fetch logs on the `stage` environment.
- **Project is inferred from the current working project** (the repo the session is in:
  `mind` → `--project mind`, `tradeoxy` → `--project tradeoxy`). The user says only the
  environment; the agent supplies the project from context. Overridable if the user
  names one.
- **Default slice:** a recent `window` (e.g. `window 30m`) for the current project,
  unless the user asks for `since-restart` / `trace`. The agent picks the subcommand.
- **No environment given ⇒ do not guess.** The agent asks which environment (or the
  script errors) — there is no endpoint without one.

## Files to change (skills repo)

- **NEW** `src/skills/observe-logs/.env.example` — committed. Short header: copy to
  `.env`, `chmod 600`, the pipe format. Three commented sample lines
  (`stage` / `dev` / `prod`) with placeholder `<uid>` / `<token>`.
- `src/skills/observe-logs/scripts/query-loki.sh` — **remove** the `localhost:3100`
  default and the no-auth path. Resolve script dir via `BASH_SOURCE`; require and parse
  a top-level `--env <name>`; look it up in `.env` (skip `#`/blank, `IFS='|' read`,
  match name) and set `OBS_LOKI_URL` / `OBS_LOKI_AUTH`. Errors: no `--env` given
  (list available envs); unknown name (list available envs); `.env` absent ("copy
  `.env.example` to `.env`").
- `.gitignore` (repo root) — add `/src/skills/observe-logs/.env` (must **not** ignore
  `.env.example`).
- `src/skills/observe-logs/SKILL.md` — **lean** rewrite of the Endpoint section for the
  agent: environments come from `.env` next to the skill, `--env <name>` is required,
  no default / no direct Loki, infer `--project` from the current project. Do **not**
  expand it into a user manual — only what the agent needs to invoke correctly. Keep
  the label schema, subcommand list, and read-only discipline; drop the "manually
  export before each call" guidance.

## Guards

- Read-only `GET` only — unchanged.
- **No default endpoint** — no `--env` ⇒ error, never a fallback to `localhost:3100`
  or any raw-Loki path (removed).
- **Do not source** `.env` — parse it.
- Resolve `.env` via `BASH_SOURCE`, never `$PWD` (symlink correctness).
- `.env.example` stays committed; only `.env` is gitignored.
- Do not touch subcommand semantics, pagination, or the
  `--project` / `--service` / `--level` / `--limit` filters.
- Keep SKILL.md lean — agent-facing, not a manual.
- bash 3.2 compatible (macOS) — same constraint the script already honors.

## Verify

- `query-loki.sh --env staging window 5m --project mind` returns staging mind logs;
  `--env local …` returns local.
- `query-loki.sh window 5m` (no `--env`) → error listing available env names, no
  network call to any default.
- Unknown `--env foo` → error listing available names; `--env staging` with no `.env`
  → error pointing at `.env.example`.
- Invoked via the symlinked path it still finds `.env` in the skill root.
- `git status` shows `.env.example` tracked and `.env` ignored.
- `/observe-logs stage` while working in the mind repo fetches recent staging logs for
  `--project mind` without the user naming the project.

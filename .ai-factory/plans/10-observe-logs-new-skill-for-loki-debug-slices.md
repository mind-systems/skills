# Plan: observe-logs — new skill for Loki debug slices

## Context
Add a personal-scope skill `observe-logs` that teaches Claude the local Loki log
backend's label schema and canned query slices, backed by a thin read-only bash
script — so any project can pull common log slices without re-deriving the schema
each session.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Query script

- [x] **Task 1: Scaffold package and script plumbing**
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Create the directory `src/skills/observe-logs/scripts/` and the executable
  `query-loki.sh` (`chmod +x`, `#!/usr/bin/env bash`, `set -euo pipefail`).
  Implement the shared plumbing only:
  - Resolve endpoint from env `OBS_LOKI_URL`, default `http://localhost:3100`.
  - **Backend-down guard:** probe `GET $OBS_LOKI_URL/ready` first (short
    `curl --max-time`); on failure or non-2xx, print one clear line — backend
    unreachable + how to start it (`make backend-up` in the observability repo) —
    and exit non-zero. Never hang.
  - A shared helper that issues read-only `GET /loki/api/v1/query_range` with a
    LogQL `query`, `start`, `end`, `limit`, `direction` and prints the matched
    log lines plus key labels (`project`/`service_name`/`level`) in a compact,
    Claude-readable form. Use `jq` if available; degrade gracefully (raw JSON or
    minimal parse) if not.
  - Top-level arg dispatch: `since-restart` | `trace` | `window`, plus a usage
    message for unknown/missing subcommands.
  Keep everything strictly read-only (only `GET` to `/ready`, `/query_range`,
  optionally `/labels`, `/series`). No writes, ever.

- [x] **Task 2: Implement the three slice subcommands** (depends on Task 1)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Implement each subcommand on top of the Task 1 helper:
  - `since-restart <service> [--project P]` — **two requests:** first query the
    latest `service.start` marker for the service
    (`{service_name="<svc>"[,project="P"]} | event_name="service.start"` — match
    the actual structured-metadata key for `event.name`; backward `direction`,
    `limit=1`), extract its `timeUnixNano`, then fetch all records for that
    service with `start` set to that timestamp. Error clearly if no marker found.
  - `trace <trace_id>` — `{<base labels>} | trace_id="<id>"` over a sensible
    default window; `trace_id` is **structured metadata**, filtered with
    `| trace_id="…"`, never a label.
  - `window <range> [--level L] [--project P] [--service S]` — parse `<range>`
    (e.g. `15m`, `2h`) into `start`/`end`, build the label selector from the
    optional filters (`level`, `project`, `service_name`), and query that window.
  Map `service.name`→`service_name` everywhere; never query high-cardinality
  fields (`trace_id`, ids) as labels.

### Phase 2: Skill instructions

- [x] **Task 3: Write SKILL.md** (depends on Task 2)
  Files: `src/skills/observe-logs/SKILL.md`
  Frontmatter: `name: observe-logs`; `description` covering what it does + when
  to use, with trigger phrases ("logs", "loki", "since restart", "by trace",
  "лог", "логи"); `argument-hint: "[since-restart <svc> | trace <id> | window <range>]"`
  (quoted — brackets in YAML); `allowed-tools: Bash Read`. `name` must match the
  directory name exactly. Body (≤ 500 lines):
  - **Label schema** — only `project`/`service_name`/`level` are index labels;
    note `service.name`→`service_name` (the single most common mistake);
    high-cardinality fields (`trace_id`, ids) live in structured metadata,
    filtered with `| key="…"`.
  - **Endpoint** — read from env `OBS_LOKI_URL`, default `http://localhost:3100`;
    never assume cloud / never hard-code a vendor.
  - **When to use** each slice and how to invoke `scripts/query-loki.sh` (relative
    path) for `since-restart` / `trace` / `window`.
  - **Since-last-restart recipe** spelled out as the two-step process (latest
    `event.name="service.start"` timestamp → query after it).
  - **Raw LogQL templates** for ad-hoc queries beyond the three slices.
  - **Read-only discipline** — only `GET /loki/api/v1/query_range`, `/labels`,
    `/series`; never writes.
  If the body nears the 500-line limit, move the LogQL cheat-sheet / label-schema
  reference into `src/skills/observe-logs/references/`.

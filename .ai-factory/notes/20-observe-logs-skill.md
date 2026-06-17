# Task — observe-logs: new skill for querying the local Loki/Grafana log backend

**Date:** 2026-06-17
**Source:** conversation context — observability project, Phase 3 "Query/MCP wrapper" decision

## Problem

The `observability` stack (separate repo under `~/projects/observability`) centralizes structured logs from every project into a local, native (no-Docker) **Loki** backend, queried via **LogQL over the Loki HTTP API**; the design explicitly has *Claude pull the needed slice itself* while the developer browses in Grafana.

Today there is no ergonomic way to do that. Each time, Claude must hand-write a LogQL expression and `curl` the API, re-deriving from memory:
- the **label schema** — only `project`, `service_name`, `level` are index labels (note: the OTLP attribute `service.name` materializes as the Loki label **`service_name`** due to dot-sanitization);
- that high-cardinality fields (`trace_id`, ids) live in **structured metadata**, filtered with `| trace_id="…"`, not as labels;
- the **"since last restart"** recipe — find the latest `service.start` marker (the load-bearing `event.name="service.start"` attribute, per the frozen contract `observe-contract@v0.1.2`), take its timestamp, then query everything after it.

This is error-prone and repeated across every debugging session, from any consuming project (tradeoxy, mind).

This task was decided **as a skill, not an MCP server** (see Rationale): the only consumer is Claude Code, so MCP's cross-client value is unrealized, and the hard part is *knowledge + canned slices*, which a skill encodes with zero running infrastructure.

## Desired behavior

A personal-scope skill **`observe-logs`** that teaches Claude how to query the local Loki backend and bundles a thin script for the deterministic slices. Because it lives in the global skills repo, it is available from **any** project — you debug `mind`/`tradeoxy` and pull log slices from wherever you are, against the shared local backend.

Invoked when the user asks for logs ("show me logs since the broker restarted", "everything for trace X", "errors in core in the last 15m"). The skill drives a bundled script for the three canonical slices and falls back to documented raw LogQL for ad-hoc queries.

## The skill package (`src/skills/observe-logs/`)

**`SKILL.md`** — frontmatter (`name: observe-logs`; `description` covering what it does + when to use, with trigger phrases like "logs", "loki", "since restart", "by trace", "лог", "логи"; `argument-hint: "[since-restart <svc> | trace <id> | window <range>]"`; `allowed-tools: Bash Read`). Body:
- the **label schema** (`project`/`service_name`/`level` only; `service.name`→`service_name`); high-cardinality fields in structured metadata, filtered with `| key="…"`;
- the **endpoint**: read from env `OBS_LOKI_URL`, default `http://localhost:3100`; the skill never assumes cloud;
- **when to use** each slice and how to invoke the script;
- the **since-last-restart recipe** spelled out (two-step: latest `event.name="service.start"` timestamp → query after it);
- raw LogQL templates for ad-hoc queries beyond the three slices;
- **read-only** discipline (only `GET /loki/api/v1/query_range`, `/labels`, `/series`); never writes.

**`scripts/query-loki.sh`** — the thin tool (bash + `curl`, optional `jq`):
- `since-restart <service> [--project P]` — query the latest `service.start` marker for the service, extract its `timeUnixNano`, then fetch all records for that service after it.
- `trace <trace_id>` — `{<labels>} | trace_id="<id>"` across the relevant window (structured-metadata filter).
- `window <range> [--level L] [--project P] [--service S]` — time-window slice (e.g. `15m`, `2h`) with optional filters.
- endpoint from `OBS_LOKI_URL` (default `http://localhost:3100`); output the matched lines + key labels in a compact, Claude-readable form.
- **backend-down guard:** probe `/ready` first; if Loki is unreachable, print a clear one-line message (and how to start it: `make backend-up` in the observability repo) instead of hanging.

**`references/`** (optional, only if SKILL.md nears the 500-line limit) — a LogQL cheat-sheet / label-schema reference.

## Watch-points

- `service.name` → `service_name` in every query (the single most common mistake).
- `since-restart` is **two requests**, not one — the marker query then the windowed query; the script hides that behind one subcommand.
- `trace_id` is structured metadata (`| trace_id="…"`), never a label — querying it as a label returns nothing.
- Keep it read-only and endpoint-configurable; default local, never hard-code anything cloud- or vendor-specific.

## Rationale (skill, not MCP)

- **Only consumer is Claude Code** — MCP's cross-client portability buys nothing here; the project's own model is "Claude pulls the slice itself via LogQL."
- **Zero running infrastructure** — no extra process / `.mcp.json` server to keep alive; Claude already reaches the HTTP API.
- **The value is knowledge** (label schema, since-restart recipe) + a few canned slices — exactly what a skill encodes.
- **Reversible** — the query logic lives in a standalone script, so wrapping it in an MCP tool later (if a non-Claude-Code client ever needs it) is additive, no rework.

## Done when

The `observe-logs` skill exists at `src/skills/observe-logs/` with a working `SKILL.md` + `scripts/query-loki.sh`; the three slices return correct results against a running local Loki (`make backend-up` in the observability repo); queries use `service_name` and structured-metadata filters correctly; the script is read-only, endpoint-configurable via `OBS_LOKI_URL`, and degrades cleanly when the backend is down.

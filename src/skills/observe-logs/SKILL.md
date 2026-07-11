---
name: observe-logs
description: >-
  Pull structured log slices from a local Loki backend without re-deriving the
  label schema each session. Covers three canned queries: logs since the last
  service restart, all lines for a trace ID, and an arbitrary time window with
  optional level/project/service filters. Use when debugging services ("logs",
  "loki", "since restart", "by trace", "лог", "логи", "логи сервиса",
  "покажи логи") or when you need a quick structured view of recent activity.
argument-hint: "--env <name> [since-restart <svc> | trace <id> | window <range>]"
allowed-tools: Bash Read
---

# observe-logs

A skill for pulling read-only log slices from the local Loki backend.
It knows the label schema, the three most common slice patterns, and how
to invoke `scripts/query-loki.sh` for each.

---

## Label schema

Only three fields are index labels — always filter with them inside `{}`:

| Label | Maps from | Notes |
|---|---|---|
| `project` | `project` | Top-level project/tenant identifier |
| `service_name` | `service.name` (OTLP) | **Use `service_name`, never `service.name`** |
| `level` | `level` / `severity` | `debug`, `info`, `warn`, `error` |

> **The single most common mistake:** writing `{service.name="…"}` — dots are
> not valid in Loki label names. The correct label is `service_name`.

---

## Endpoint

Environments live in a `.env` registry next to this skill — the user copies
`.env.example` to `.env`, fills in one pipe-delimited line per environment
(`stage` / `dev` / `prod`, each with its Grafana datasource-proxy URL and
`Authorization` header value), and runs `chmod 600 .env`. The skill never
stores or assumes a credential itself.

`--env <name>` is **required** on every invocation — there is no default
endpoint and no direct-Loki / no-auth path. It must lead the argument list:

```bash
bash scripts/query-loki.sh --env stage window 30m --project mind
```

Infer `--project` from the current project/repo when the user doesn't name
one (e.g. working in `mind` → `--project mind`, in `tradeoxy` → `--project
tradeoxy`); the user only needs to name the environment. If the user names a
project explicitly, that overrides the inferred one.

When invoked as `/observe-logs <env>` with nothing else specified, run a
recent `window` slice for the current project — unless the user's phrasing
asks for `since-restart` or `trace`. If no environment is given at all, don't
guess one: ask the user, or invoke the script without `--env` and let it
error with the list of available environment names.

If the backend is unreachable the script prints one clear line pointing at the
`.env` URL/token for that environment and network/VPN connectivity, then
exits non-zero immediately.

---

## Running the script

All three slice subcommands are wrappers around a single `GET /loki/api/v1/query_range`
helper in `scripts/query-loki.sh`. Invoke it with a relative path from the
skill root, or from any project directory via its absolute path.

```bash
# From the skill root
bash scripts/query-loki.sh --env <name> <subcommand> [args]

# Or via Claude's Bash tool:
bash /path/to/observe-logs/scripts/query-loki.sh --env <name> <subcommand> [args]
```

Output format: `[timestamp] [level] [project/service] message` — one line per
log entry. Uses `jq` when available; degrades to minimal parsing otherwise.

---

## Subcommand: `since-restart`

Fetch the **full log feed** for a service since its most recent restart — no
line cap. Uses client-side pagination past Loki's per-call limit.

```bash
bash scripts/query-loki.sh --env <name> since-restart <service_name> [--project P]
```

Error if no marker is found (service may not emit this event, or hasn't
restarted in the 7-day lookback window).

**Example:**
```bash
bash scripts/query-loki.sh --env stage since-restart api-gateway
bash scripts/query-loki.sh --env prod since-restart worker --project payments
```

---

## Subcommand: `trace`

Fetch all log lines associated with a trace ID. Looks back 24 hours.

```bash
bash scripts/query-loki.sh --env <name> trace <trace_id> [--limit N]
```

Use `--limit N` (default 200) to raise the cap for high-volume traces.

**Example:**
```bash
bash scripts/query-loki.sh --env stage trace 4bf92f3577b34da6a3ce929d0e0e4736
bash scripts/query-loki.sh --env stage trace 4bf92f3577b34da6a3ce929d0e0e4736 --limit 1000
```

---

## Subcommand: `window`

Fetch logs in a relative time window with optional filters.

```bash
bash scripts/query-loki.sh --env <name> window <range> [--level L] [--project P] [--service S] [--limit N]
```

`<range>` formats: `15m`, `2h`, `1d` (minutes / hours / days).
All filters are optional.

`--limit N` sets the maximum number of log lines returned (default 200). Bump it
when 200 lines aren't enough — e.g. `--limit 2000` for a busier window.

**Two calling modes:**

- **Single service** — use `--service <svc>` (and optionally `--project`).
  Returns only that service's logs.
- **Cross-service** — use `--project <p>` with `--service` omitted.
  Returns logs from all services in the project. Output is globally time-ordered
  by timestamp (entries from different services are interleaved chronologically,
  not grouped by service).

**Examples:**
```bash
bash scripts/query-loki.sh --env stage window 30m
bash scripts/query-loki.sh --env stage window 2h --service payment-processor
bash scripts/query-loki.sh --env prod window 1h --level error --project platform
bash scripts/query-loki.sh --env dev window 15m --project api --service gateway --level warn
bash scripts/query-loki.sh --env prod window 1h --project platform --limit 1000
```

---

Ad-hoc / hand-written queries and the deep label schema → read
`references/logql.md`.

---

## Read-only discipline

This skill and script only issue GET requests:

- `GET /ready` — liveness probe
- `GET /loki/api/v1/query_range` — log queries
- `GET /loki/api/v1/labels` — label discovery (optional)
- `GET /loki/api/v1/series` — series discovery (optional)

No push, no delete, no write of any kind — ever.

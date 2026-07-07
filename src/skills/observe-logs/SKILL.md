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

All other fields are **structured metadata** — not indexed, filtered with a
pipeline expression (`| key="value"`) after the label selector:

- `trace_id` — never a label; always `| trace_id="…"`
- `span_id`, request IDs, user IDs — same rule
- `event.name` (OTLP) → queried as `| event_name="…"` in LogQL

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

**Two-step process** (spelled out below):

1. Query the latest `event.name="service.start"` marker for the service:
   ```
   {service_name="<svc>"} | event_name="service.start"
   ```
   Direction: `backward`, `limit=1`. Extracts the timestamp of the last restart.

2. Fetch **all** log records for the service starting at that timestamp using
   client-side pagination (PAGE_SIZE=5000 per call, looping until Loki returns
   a short page):
   ```
   {service_name="<svc>"}
   ```
   Direction: `forward`, `start=<restart_timestamp>`. Returns every line
   regardless of how many there are — output grows as long as logs exist.

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

`trace_id` is structured metadata — the script filters with `| trace_id="…"`.
Loki requires at least one non-empty label matcher, so the script uses
`{service_name=~".+"}` as the base selector; this spans all services.
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
All filters are optional; omitting them defaults to `{service_name=~".+"}` (Loki
requires at least one non-empty matcher — bare `{}` is rejected).

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

## Raw LogQL templates

For ad-hoc queries beyond the three slices, use `curl` directly. Pull the URL
and `Authorization` value for the target environment from `.env` (the same
registry `--env` resolves) and export them first:

```bash
export LOKI_URL="<url from the .env line for your environment>"
export LOKI_AUTH="<auth from the .env line for your environment>"
```

```bash
# All error logs in the last hour
curl -sG -H "Authorization: ${LOKI_AUTH}" "${LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={level="error"}' \
  --data-urlencode "start=$(python3 -c 'import time; print(int((time.time()-3600)*1e9))')" \
  --data-urlencode "end=$(python3 -c 'import time; print(int(time.time()*1e9))')" \
  --data-urlencode 'limit=100' | jq -r '.data.result[].values[][1]'

# Specific service, specific level
curl -sG -H "Authorization: ${LOKI_AUTH}" "${LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={service_name="api-gateway",level="error"}' \
  ...

# Filter by trace (structured metadata)
curl -sG -H "Authorization: ${LOKI_AUTH}" "${LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={service_name="api-gateway"} | trace_id="abc123"' \
  ...

# List all known labels
curl -s -H "Authorization: ${LOKI_AUTH}" "${LOKI_URL}/loki/api/v1/labels" | jq '.data[]'

# List values for a label
curl -s -H "Authorization: ${LOKI_AUTH}" "${LOKI_URL}/loki/api/v1/label/service_name/values" | jq '.data[]'
```

---

## Read-only discipline

This skill and script only issue GET requests:

- `GET /ready` — liveness probe
- `GET /loki/api/v1/query_range` — log queries
- `GET /loki/api/v1/labels` — label discovery (optional)
- `GET /loki/api/v1/series` — series discovery (optional)

No push, no delete, no write of any kind — ever.

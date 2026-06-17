---
name: observe-logs
description: >-
  Pull structured log slices from a local Loki backend without re-deriving the
  label schema each session. Covers three canned queries: logs since the last
  service restart, all lines for a trace ID, and an arbitrary time window with
  optional level/project/service filters. Use when debugging services ("logs",
  "loki", "since restart", "by trace", "лог", "логи", "логи сервиса",
  "покажи логи") or when you need a quick structured view of recent activity.
argument-hint: "[since-restart <svc> | trace <id> | window <range>]"
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

Read from environment variable `OBS_LOKI_URL`; defaults to
`http://localhost:3100`. Never assume a cloud vendor; never hard-code a URL.

```bash
export OBS_LOKI_URL=http://localhost:3100   # already the default
```

If the backend is down the script prints one clear line with a recovery hint
(`make backend-up` in the observability repo) and exits non-zero immediately.

---

## Running the script

All three slice subcommands are wrappers around a single `GET /loki/api/v1/query_range`
helper in `scripts/query-loki.sh`. Invoke it with a relative path from the
skill root, or from any project directory via its absolute path.

```bash
# From the skill root
bash scripts/query-loki.sh <subcommand> [args]

# Or via Claude's Bash tool:
bash /path/to/observe-logs/scripts/query-loki.sh <subcommand> [args]
```

Output format: `[timestamp] [level] [project/service] message` — one line per
log entry. Uses `jq` when available; degrades to minimal parsing otherwise.

---

## Subcommand: `since-restart`

Fetch all logs for a service since its most recent restart.

```bash
bash scripts/query-loki.sh since-restart <service_name> [--project P]
```

**Two-step process** (spelled out below):

1. Query the latest `event.name="service.start"` marker for the service:
   ```
   {service_name="<svc>"} | event_name="service.start"
   ```
   Direction: `backward`, `limit=1`. Extracts the timestamp of the last restart.

2. Fetch all log records for the service starting at that timestamp:
   ```
   {service_name="<svc>"}
   ```
   Direction: `forward`, `start=<restart_timestamp>`.

Error if no marker is found (service may not emit this event, or hasn't
restarted in the 7-day lookback window).

**Example:**
```bash
bash scripts/query-loki.sh since-restart api-gateway
bash scripts/query-loki.sh since-restart worker --project payments
```

---

## Subcommand: `trace`

Fetch all log lines associated with a trace ID. Looks back 24 hours.

```bash
bash scripts/query-loki.sh trace <trace_id>
```

`trace_id` is structured metadata — the script filters with `| trace_id="…"`.
Loki requires at least one non-empty label matcher, so the script uses
`{service_name=~".+"}` as the base selector; this spans all services.

**Example:**
```bash
bash scripts/query-loki.sh trace 4bf92f3577b34da6a3ce929d0e0e4736
```

---

## Subcommand: `window`

Fetch logs in a relative time window with optional filters.

```bash
bash scripts/query-loki.sh window <range> [--level L] [--project P] [--service S]
```

`<range>` formats: `15m`, `2h`, `1d` (minutes / hours / days).
All filters are optional; omitting them defaults to `{service_name=~".+"}` (Loki
requires at least one non-empty matcher — bare `{}` is rejected).

**Examples:**
```bash
bash scripts/query-loki.sh window 30m
bash scripts/query-loki.sh window 2h --service payment-processor
bash scripts/query-loki.sh window 1h --level error --project platform
bash scripts/query-loki.sh window 15m --project api --service gateway --level warn
```

---

## Raw LogQL templates

For ad-hoc queries beyond the three slices, use `curl` directly:

```bash
# All error logs in the last hour
curl -sG "${OBS_LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={level="error"}' \
  --data-urlencode "start=$(python3 -c 'import time; print(int((time.time()-3600)*1e9))')" \
  --data-urlencode "end=$(python3 -c 'import time; print(int(time.time()*1e9))')" \
  --data-urlencode 'limit=100' | jq -r '.data.result[].values[][1]'

# Specific service, specific level
curl -sG "${OBS_LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={service_name="api-gateway",level="error"}' \
  ...

# Filter by trace (structured metadata)
curl -sG "${OBS_LOKI_URL}/loki/api/v1/query_range" \
  --data-urlencode 'query={service_name="api-gateway"} | trace_id="abc123"' \
  ...

# List all known labels
curl -s "${OBS_LOKI_URL}/loki/api/v1/labels" | jq '.data[]'

# List values for a label
curl -s "${OBS_LOKI_URL}/loki/api/v1/label/service_name/values" | jq '.data[]'
```

---

## Read-only discipline

This skill and script only issue GET requests:

- `GET /ready` — liveness probe
- `GET /loki/api/v1/query_range` — log queries
- `GET /loki/api/v1/labels` — label discovery (optional)
- `GET /loki/api/v1/series` — series discovery (optional)

No push, no delete, no write of any kind — ever.

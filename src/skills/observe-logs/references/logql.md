# LogQL reference

Ad-hoc and hand-written query detail for `observe-logs` — read only when the
three canned subcommands (`since-restart`, `trace`, `window`) don't fit and a
hand-written LogQL query is required.

---

## Structured metadata

All other fields are **structured metadata** — not indexed, filtered with a
pipeline expression (`| key="value"`) after the label selector:

- `trace_id` — never a label; always `| trace_id="…"`
- `span_id`, request IDs, user IDs — same rule
- `event.name` (OTLP) → queried as `| event_name="…"` in LogQL

---

## `since-restart` internals

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

---

## `trace` base selector

`trace_id` is structured metadata — the script filters with `| trace_id="…"`.
Loki requires at least one non-empty label matcher, so the script uses
`{service_name=~".+"}` as the base selector; this spans all services.

---

## `window` default selector

omitting them defaults to `{service_name=~".+"}` (Loki requires at least
one non-empty matcher — bare `{}` is rejected).

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

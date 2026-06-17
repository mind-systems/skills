# Code Review (round 2): observe-logs — Loki debug slices

Scope: `src/skills/observe-logs/scripts/query-loki.sh` and
`src/skills/observe-logs/SKILL.md`. All checks re-run empirically against the
live local Loki (`/ready` = 200), including real log data
(`project=observe-js-smoke`, `service_name=smoke-service`, with `service.start`
markers).

## Round-1 findings — all resolved and verified

- **B1 (trace sent invalid `{}` selector)** — fixed. `cmd_trace` now uses
  `{service_name=~".+"} | trace_id="…"` (`query-loki.sh:251`). Verified:
  `trace abc123` → `status:success`, prints `No log lines matched.`
- **B2 (window with no filters sent `{}`)** — fixed. Empty-filter case now
  defaults to `{service_name=~".+"}` (`:307-310`). Verified: `window 15m` →
  success; `window 15m --level error` → success.
- **L1 (jq <1.7 strftime)** — fixed. `tonumber/1e9 | gmtime | strftime(...)`
  (`:54`). Verified formatter output on jq 1.7 with real data:
  `[2026-06-17T09:12:05Z] [info] [observe-js-smoke/smoke-service] service.start`.
- **L2 (gawk-only strftime in no-jq fallback)** — fixed. Fallback now prints raw
  epoch seconds `[%d]` and avoids `strftime` (`:62-66`).
- **L3 (leaked `jq: parse error` on non-JSON error body)** — fixed. Error branch
  now `2>/dev/null`s the jq attempt and falls back to `head -5` (`:108-109`).
- **L4 (trailing valueless flag crashed under `set -u`)** — fixed. Each flag
  guards `[[ $# -ge 2 ]]` before shifting (`:165, :272-280`). Verified:
  `window 15m --level` → `ERROR: --level requires a value`, clean exit.
- **L5 (empty result printed nothing)** — fixed. `format_response` counts values
  and prints `No log lines matched.` on zero (`:38-43`).

## Full-path verification (this round)

- `since-restart smoke-service` exercises the complete two-step flow against real
  markers: marker query with `| event_name="service.start"` returns the latest
  marker, timestamp extracted (`2026-06-17T09:12:05Z`), step-2 windowed fetch
  returns the post-restart lines. The `event_name` structured-metadata key
  matches the real data. Works end-to-end.
- `since-restart nonexistent-svc` → clear "No service.start marker found" error,
  non-zero exit.
- Bad/missing subcommand → usage text, exit 1.
- Backend-down guard, read-only discipline (only `GET /ready` + `/query_range`),
  and nanosecond arithmetic all unchanged and correct.
- SKILL.md trace (`:118-120`) and window (`:138-139`) prose updated to document
  the `{service_name=~".+"}` base selector and that bare `{}` is rejected —
  docs now match the code.

No outstanding or new findings. All three slices work correctly against the live
backend.

REVIEW_PASS

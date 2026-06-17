# Code Review: observe-logs — Loki debug slices

Scope reviewed: `src/skills/observe-logs/scripts/query-loki.sh` and
`src/skills/observe-logs/SKILL.md` (the only code/behavioral changes; the
roadmap/notes/plan/sidecar files are process artifacts and out of scope).

All findings below were verified empirically against the live local Loki
(`/ready` returned 200) by issuing the exact LogQL the script generates.

---

## Blocking

### B1 — `trace` subcommand always sends an invalid stream selector (`{}`), fails 100% of the time
`query-loki.sh:234`

```bash
local logql="{} | trace_id=\"${trace_id}\""
```

Loki LogQL rejects an empty stream selector. The query_range API returns
**HTTP 400**:

```
parse error : queries require at least one regexp or equality matcher that
does not have an empty-compatible value. For instance, app=~".*" does not
meet this requirement, but app=~".+" will
```

Verified end-to-end — `query-loki.sh trace abc123` prints
`ERROR: Loki query failed (status=unknown)` and exits non-zero. A structured-
metadata pipeline filter (`| trace_id=...`) does **not** satisfy the
"at least one matcher" requirement; the `{}` selector itself must be non-empty.

This means the `trace` slice — one of the three core deliverables — never works.

**Fix:** use a non-empty matcher that spans all streams, e.g.
`{service_name=~".+"} | trace_id="${trace_id}"` (verified: returns
`status:"success"`). Update the comment at `:232-233` and the SKILL.md claim at
`SKILL.md:118-119` ("not a label selector … spans services and projects" — the
*intent* is right, but it still needs a non-empty `{}` matcher).

### B2 — `window <range>` with no filters sends `{}`, fails
`query-loki.sh:280-285`

When none of `--level/--project/--service` are passed, `parts` is empty and the
selector becomes the literal `{}`:

```bash
local selector="{"
if [[ ${#parts[@]} -gt 0 ]]; then ... fi
selector="${selector}}"
```

Same Loki 400 parse error as B1. Verified: `query-loki.sh window 15m` →
`ERROR: Loki query failed`. The documented default invocation
`window 30m` (`SKILL.md:142`) and the claim "omitting them queries across all
streams (no label selector restrictions)" (`SKILL.md:137-138`) are both broken —
`{}` is not a valid "all streams" query in Loki.

**Fix:** when `parts` is empty, default the selector to a non-empty catch-all
such as `{service_name=~".+"}` (verified valid). `window <range> --level error`
(and any single filter) already works correctly.

---

## Low / Non-blocking

### L1 — formatter silently degrades to raw JSON on jq < 1.7
`query-loki.sh:47`

`.[0] | tonumber / 1e9 | strftime(...)` passes a number straight to `strftime`.
jq **1.7** (the version on this machine, `jq-1.7.1-apple`) accepts this and the
formatter works — verified. But jq **1.6** requires a broken-down time
(`... | gmtime | strftime(...)`) and errors otherwise; combined with the
`2>/dev/null || echo "$raw"` fallback at `:48`, the whole pretty-print silently
collapses to a raw-JSON dump with no indication why. Cheap hardening: insert
`| gmtime` before `strftime` so both jq versions format correctly.

### L2 — no-jq fallback formatter relies on gawk-only `strftime`
`query-loki.sh:56` (and `now_ns`/`restart_readable` lean on python3)

The non-jq branch calls `strftime()` in awk, which is a GNU awk extension absent
from the BSD `awk` shipped on macOS (this platform). On a box without jq, this
path hits the `2>/dev/null || echo "$raw"` fallback and dumps raw JSON. Minor,
since jq is the primary path and is present here — but the "degrades gracefully
without jq" guarantee is weaker than it reads.

### L3 — error path leaks a `jq: parse error` to stderr
`query-loki.sh:94`

On a Loki 400 the response body is plain text, not JSON, so
`echo "$response" | jq -r '.error // .message // ""' >&2` emits
`jq: parse error: Invalid numeric literal...` instead of the actual Loki
message. Observed in the B1/B2 repro. Add `2>/dev/null` and fall back to
printing the raw body so the user sees the real parse error.

### L4 — trailing flag with no value crashes under `set -u`
`query-loki.sh:149`, `:255-257`

`--project) shift; project="$1"` — if a flag is the last token (e.g.
`since-restart worker --project`), the `shift` leaves `$1` unset and, under
`set -u`, `project="$1"` aborts with `$1: unbound variable` instead of a
friendly usage error. Guard with `${2:-}` semantics or check `$# -ge 2` before
shifting.

### L5 — empty result set prints nothing
`query-loki.sh:212`, `:241`, `:292`

A successful query with zero matches prints only the `>&2` progress lines and an
empty stdout, indistinguishable at a glance from a silent failure. A
`No log lines matched.` notice on empty `.data.result` would read better.

---

## Verified working
- Backend-down guard (`check_backend`) correctly distinguishes 2xx vs `000`/non-2xx.
- `since-restart` builds a valid non-empty selector (`{service_name="<svc>"}`) — selector shape is correct (untested for marker presence; no `service.start` data locally).
- `window <range> --<filter>` with any filter present works (verified `--level error` → `status:success`).
- jq formatter output format `[ts] [level] [project/service] message` is correct on jq 1.7.
- Nanosecond arithmetic stays within bash 64-bit signed range; no overflow.
- Read-only discipline holds: only `GET /ready` and `GET /query_range` are issued.

The two blocking findings (B1, B2) break two of the three advertised slices in
their primary invocation and should be fixed before this skill is usable.

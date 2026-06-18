# Code Review: observe-logs full restart feed (review 2)

**Scope:** `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/SKILL.md`
**Follow-up to:** review 1.

## Status of review-1 findings

- **[Medium] Lossy cursor via `tonumber` → duplicate lines (review 1, finding 1):** **Resolved.** `query_range_all` now derives the cursor from a string max — `[.data.result[].values[][0]] | max` — with a comment explaining that lexicographic max over equal-length 19-digit ns strings equals the numeric max without IEEE-754 loss. Verified: max returns the full-precision `1718800000000000900` and bash `$((last_ns + 1))` yields `…901`. The cursor now advances strictly past the true last entry, so no boundary duplicates and no premature stall on jq 1.6 or 1.7.
- **[Low] `--limit` not validated (review 1, finding 2):** **Resolved.** Both `cmd_trace` and `cmd_window` now enforce `[[ "$limit" =~ ^[0-9]+$ ]]` with a clear error message.

The cross-service merge, multi-page accumulation, termination guards, and read-only discipline remain correct (re-verified). SKILL.md accurately documents the new behavior.

## Remaining findings

### 1. [Low] `format_response` sort key still uses `tonumber` — inconsistent with the cursor fix

The merge sort key was *not* given the same treatment as the cursor:
```
ns: (.[0] | tonumber),
...
sort_by(.ns)
```
On jq < 1.7 this collapses ns values that differ only below ~2^53 precision to one key, so two sub-microsecond-apart entries from different streams may sort in input (per-stream concatenation) order rather than true time order. Impact is **cosmetic**: the displayed timestamp is second-resolution (`%Y-%m-%dT%H:%M:%SZ`), so reordering within the same second is invisible, and on the installed jq 1.7.1 the values are exact anyway. For parity with the cursor fix and version-independent correctness, sort by the raw string instead — e.g. carry `ns: .[0]` (a 19-digit string) and `sort_by(.ns)` (lexicographic = numeric for equal length), computing the display time as `(.ns | tonumber) / 1e9 | gmtime | strftime(...)` only at print time. Optional; near-zero real impact.

### 2. [Nit] `--limit` regex accepts `0` (and leading zeros) despite "positive integer" message

`^[0-9]+$` passes `--limit 0` (message claims "positive integer") and `--limit 05` (forwarded verbatim to Loki). `limit=0` is sent to Loki, whose behavior for a zero limit is backend-defined (may error or apply a default). Negligible — tighten to `^[1-9][0-9]*$` if you want the message and the check to agree. Not worth a round-trip on its own.

### 3. [Note] Unchanged from review 1 — acceptable trade-offs

- The accumulator is re-parsed every page (`jq -s` over the full accumulated payload), i.e. O(n²) in page count. Fine for typical "since restart" feeds; only matters for very large unbounded feeds.
- `next_cursor = last_ns + 1` skips any entries sharing the exact final nanosecond of a *full* (5000-entry) page. Inherent to ns-cursor pagination and astronomically unlikely at real log rates.

No action required on these.

## Summary

Both actionable findings from review 1 are fixed correctly. What remains is one low-severity consistency item (sort key still uses lossy `tonumber`, cosmetic at second-resolution display) and a one-character nit on the limit regex. Nothing blocking.

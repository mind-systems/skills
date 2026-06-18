# Code Review: observe-logs full restart feed (review 3)

**Scope:** `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/SKILL.md`
**Follow-up to:** review 1 and review 2.

## Status of prior findings

**Review 1**
- [Medium] Lossy `tonumber` cursor → boundary duplicates: **resolved** in review 2 (string max for the cursor).
- [Low] `--limit` not validated: **resolved** in review 2.

**Review 2**
- [Low] `format_response` sort key still used `tonumber` (lossy on jq < 1.7): **resolved.** The flattened entries now carry the raw string (`ns: .[0]`) and sort with `sort_by(.ns)`. Lexicographic order over equal-length 19-digit ns strings equals numeric order, so interleaving is correct on every jq version; `tonumber` is now applied only at display time (`\(.ns | tonumber / 1e9 | gmtime | strftime(...))`), where second-resolution rounding is harmless. Verified: a three-entry, two-stream payload prints in true chronological order (early → mid → late).
- [Nit] `--limit` regex accepted `0`/`05`: **resolved.** Both `cmd_trace` and `cmd_window` now use `^[1-9][0-9]*$`. Verified: `0`, `05`, `abc` rejected; `200` accepted.

## Full-change assessment

All six plan tasks are implemented and now internally consistent:

- `query_range_all` paginates `forward` at `PAGE_SIZE=5000`, accumulates pages into one Loki-shaped payload, and terminates on empty page / short page / non-advancing cursor. The cursor uses full-precision string max, so it advances strictly past the true last entry — no duplicates, no spin.
- `since-restart` Step 2 uses the unbounded paginator; Step 1 marker lookup and `event_name="service.start"` / `trace_id` semantics are unchanged.
- `--limit` (validated, default 200) is wired into `window` and `trace`; `since-restart` no longer reads `DEFAULT_LIMIT`.
- `format_response` flattens all streams and globally sorts by timestamp; single-stream output is a no-op sort (ordering preserved). Empty-result short-circuit and `|| echo "$raw"` fallback intact; non-`jq` branch unchanged.
- Read-only discipline holds — only `GET /loki/api/v1/query_range` is issued; no new endpoints, no writes.
- SKILL.md accurately documents the full feed, `--limit`, and single-vs-cross-service modes.

Previously noted inherent trade-offs remain and are acceptable by design: the accumulator is re-parsed per page (O(n²) in page count, fine for realistic feeds), and a full page whose final nanosecond is shared by entries beyond the 5000th would skip the surplus (astronomically unlikely at real log rates). Neither is a defect.

No outstanding correctness, security, or runtime concerns.

REVIEW_PASS

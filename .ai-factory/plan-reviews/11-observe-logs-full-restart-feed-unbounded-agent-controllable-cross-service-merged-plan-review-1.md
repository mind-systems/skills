# Plan Review: observe-logs full restart feed

**Plan:** `11-observe-logs-full-restart-feed-unbounded-agent-controllable-cross-service-merged.md`
**Target:** `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/SKILL.md`
**Risk Level:** 🟢 Low

## Verification of Plan Claims

All cited line references are accurate against the current files:

| Claim | Verified |
|---|---|
| `DEFAULT_LIMIT` at `:11` | ✓ (line 11) |
| `query_range` ends after `:117` | ✓ |
| `cmd_since_restart` `:158–230`, Step 2 call `:227` | ✓ |
| Marker lookup `backward limit=1` `:196` | ✓ |
| `cmd_window` `:264–318`, call `:315` | ✓ |
| `cmd_trace` `:236–259`, call `:256` | ✓ |
| `format_response` jq program `:45–55`, empty short-circuit `:39–42`, else branch `:56–72` | ✓ |
| SKILL.md `since-restart` `:77–106`, `window` `:129–147` | ✓ |

`PAGE_SIZE=5000` matches Loki's actual `max_entries_limit_per_query` default. No DB / migration surface (bash script). Read-only GET discipline is preserved by reusing `query_range`.

## Architectural Assessment

The task decomposition is coherent and the dependency graph is correct:

- **Pagination model is sound.** Loki `query_range` with `direction=forward` returns the globally-earliest N entries in `[start, end)` (start inclusive, end exclusive). Advancing `cursor = max_ns + 1` is the correct standard cursor approach and avoids duplicating the boundary entry. The mandatory termination guards (short/empty page + stalled-cursor break) are correctly specified and prevent infinite loops.
- **Task 1 ↔ Task 4 interplay is correct.** `query_range_all` concatenates per-page `.data.result[]` arrays (producing repeated stream entries across pages); Task 4's global `sort_by(ns)` flatten is what makes the merged multi-page / multi-stream payload come out chronological. The two tasks are interdependent and the plan sequences them so the final state (Commit 2) is correct.
- **No broken intermediate state that regresses behavior.** After Commit 1 (tasks 1–3, old `format_response` still in place), `since-restart` output is no *worse*-ordered than today — see note 3 below.

## Findings

### Should-fix (non-blocking)

1. **`--limit` needs integer validation, not just presence.** Task 3 says to follow "the same validation pattern as `--level`/`--project`, require a value." But those flags only check that a value *exists* (`[[ $# -ge 2 ]]`); they do no content validation. `--limit` is different: its value is interpolated into the Loki `limit=` query param and is conceptually numeric. A non-numeric or negative `--limit` would produce a malformed Loki request (and a confusing `status != success` exit). Recommend adding an explicit guard, e.g. `[[ "$1" =~ ^[0-9]+$ ]] || { echo "ERROR: --limit must be a positive integer" >&2; exit 1; }`. This is the one real robustness gap; everything else is informational.

### Notes (informational, no action required)

2. **Boundary-nanosecond truncation edge case.** With `cursor = max_ns + 1`, if a single page is truncated at exactly `PAGE_SIZE` *and* multiple entries share that page's maximum ns (sub-microsecond bursts), the entries at `max_ns` that didn't fit get skipped. This is the well-known Loki forward-pagination boundary case and is acceptable for a debugging tool; worth a one-line comment in the helper so a future reader doesn't mistake it for a bug. (Using `max_ns` rather than `max_ns + 1` would instead risk re-emitting the boundary entry — the plan's choice is the safer of the two.)

3. **`since-restart` is still not globally level-ordered until Task 4.** `{service_name="x"}` matches one stream *per level* (level is a label), so within a page the old `format_response` prints all-errors-then-all-infos, not chronological. This is **pre-existing** behavior, and Task 4 fixes it — Commit 1 neither improves nor regresses it. No change needed; just be aware Commit 1 alone does not yet deliver chronological single-service output for multi-level services.

4. **Task 4 is load-bearing for pagination ordering, not only cross-service merge.** The plan frames Task 4 as the "cross-service" task, but its global sort is also what orders multi-page `since-restart` output. The sequencing already accounts for this (both land before the work is considered done); only the framing is narrower than the actual effect.

## Positive Notes

- Excellent precision on line anchors — every reference verified correct against the live files.
- Explicit, mandatory termination guards called out up front (the highest-risk part of any pagination loop).
- `jq`-unavailable fallback is handled deliberately (single bounded call + documented limitation) rather than attempting a fragile JSON-less merge.
- Preserves byte-identical single-stream ordering and the empty-result short-circuit, minimizing behavioral blast radius.
- Commit plan cleanly splits the mechanical pagination/limit work from the formatter rewrite + docs.

PLAN_REVIEW_PASS

# observe-logs: full restart feed — unbounded, agent-controllable, cross-service merged

**Date:** 2026-06-18
**Source:** conversation context

## Key Findings

- The debug flow is fixed: start the app → reproduce the bug → read **all** logs since that start, ideally interleaved across services. `query-loki.sh` fails this on two fronts — it caps output at 200 lines and it prints per-service blocks instead of one time-ordered feed. Both live in one small script (`scripts/query-loki.sh`) plus a doc section in `SKILL.md`; this is one task, not several.
- **No 200-line limit on `since-restart`.** `DEFAULT_LIMIT=200` (`query-loki.sh:11`) is applied to all three subcommands today, including `since-restart`, where it silently truncates. `since-restart` must return **every** line from the `service.start` marker to now. Loki caps a single `query_range` call at the server's `max_entries_limit_per_query` (default 5000), so "unbounded" requires **client-side pagination**: page `forward`, advance the cursor past the last returned ns, repeat until a page comes back short.
- **`service.start` is the right checkpoint but suspected broken** — verifying the marker query + anchor actually returns logs against a real restart (mind_api server restart, or mind_mobile app start) is part of this task, and fixing it if broken.
- **Anchor is per-service** — pick one service, anchor to *its* last `service.start`. Server restart → from server start; mobile app launch → from app start. The existing `since-restart <service>` shape stays.
- **Agent-controllable `--limit` for checkpoint-less modes.** `window` and `trace` have no natural checkpoint, so they keep a bound — but expose `--limit N` (default 200, agent bumps when 200 isn't enough). The 200 default applies **only** here, never to `since-restart`.
- **Cross-service chronological merge.** A `{project="mind"}` query returns every line, but Loki groups results **by stream** and `direction` orders only *within* a stream — so multi-service output prints as per-service chunks. The global timeline is a client-side sort (as Grafana Explore does), and the gap is in `format_response()`. Single-stream queries sort to a no-op, so single-service output is unchanged.

## Details

### Current state

`src/skills/observe-logs/scripts/query-loki.sh`:
- `DEFAULT_LIMIT=200` (line 11) — feeds every subcommand's final fetch.
- `query_range(logql, start_ns, end_ns, limit, direction)` (79–117) — one `GET /loki/api/v1/query_range`, no pagination.
- `cmd_since_restart` (158–230) — Step 1 finds the latest `service.start` marker (`backward limit=1`); Step 2 fetches `forward` from that ts with `limit=$DEFAULT_LIMIT` (the harmful cap).
- `cmd_window` (264–318) / `cmd_trace` (236–259) — fetch with `limit=$DEFAULT_LIMIT`; no `--limit` flag.
- `format_response()` (34–73) — `jq` does `.data.result[] | … | $stream.values[] | "<line>"`, emitting each stream consecutively → never interleaved.

### The change (one script + one SKILL.md section)

1. **Pagination helper** (e.g. `query_range_all`): loop `query_range` `forward` from the anchor with a per-call page size of **5000** (a `PAGE_SIZE=5000` constant — Loki's common `max_entries_limit_per_query` default), after each page read the last entry's ns across all streams, set next `start = last_ns + 1`, repeat until a page returns fewer than `PAGE_SIZE` (or zero). Accumulate every page's `.data.result` into one combined Loki-shaped payload so `format_response` consumes it unchanged. Guard against an infinite loop if the cursor fails to advance.
2. **`since-restart` uses pagination, no limit** — Step 2 calls the paginating fetch from `restart_ts_ns` to now; drop the `$DEFAULT_LIMIT` argument. Marker lookup (Step 1) stays single `backward limit=1`.
3. **`--limit N` flag** parsed in `cmd_window` (and `cmd_trace`), defaulting to `DEFAULT_LIMIT` (200) when omitted. These stay single-call bounded — no pagination (no checkpoint to bound volume naturally).
4. **Verify `service.start` end-to-end** — run `since-restart` against a service that actually restarted; confirm the marker is found, the anchor ts is correct, and logs from the restart forward are returned. Fix the marker query (`| event_name="service.start"`) or anchor extraction if broken.
5. **Cross-service merge in `format_response()`** — rewrite the `jq` branch to collect every entry across all streams into one array carrying `project`/`service_name`/`level` alongside `[ns, msg]`, sort by the numeric ns, then format each as the existing `[timestamp] [level] [project/service] message` line. Preserve the empty-result short-circuit ("No log lines matched."). Non-`jq` fallback stays best-effort (document that the global sort needs `jq`).
6. **`SKILL.md`** — `window` section: document the two modes (single-service `--service` vs merged cross-service `--project`, `--service` omitted) and that multi-service output is globally time-ordered; document `--limit`. `since-restart` section: note it returns the full feed (no limit) from the marker.

### Guards

- Read-only discipline unchanged — `GET /loki/api/v1/query_range` only; no new endpoints.
- Single-service output stays byte-compatible in ordering (one stream → sort is a no-op); keep the existing line shape — `[project/service]` already names the emitter, no extra tag.
- `since-restart` / `trace` label & structured-metadata semantics unchanged beyond the limit/pagination change (marker via `| event_name="service.start"`, trace via `| trace_id="…"`).
- `DEFAULT_LIMIT` is repurposed as the checkpoint-less default only; `since-restart` no longer reads it.
- Pagination must terminate: stop on a short page or a stalled cursor; never spin.
- `--services a,b` subset selector is **out of scope** — separate task if wanted.
- `name` in frontmatter still equals the directory name; no frontmatter churn.

### Verify

- `since-restart mind_api` (after a real restart): full feed from the `service.start` marker, >200 lines if they exist, no truncation; crosses the per-call cap via multiple pages and still returns everything in order.
- `window 10m --service mind_api`: defaults to 200 and output is identical to before the change; `--limit 2000` returns up to 2000.
- `window 10m --project mind` against a session exercising both `mind_api` and `mind_mobile`: lines from both interleaved in strict timestamp order.
- `trace <id> --limit 1000`: honours the bump.
- Canonical install at `~/.claude/skills/observe-logs` picks up the edit via the `src/skills` symlink.

## Open Questions

- None. Per-call page size settled at 5000 (`PAGE_SIZE` constant). If the local Loki is configured below 5000, the loop still terminates correctly (a page shorter than `PAGE_SIZE` ends it) — it just paginates in smaller chunks than expected.

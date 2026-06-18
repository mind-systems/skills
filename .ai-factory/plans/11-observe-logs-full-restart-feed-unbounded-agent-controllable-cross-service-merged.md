# Plan: observe-logs: full restart feed — unbounded, agent-controllable, cross-service merged

## Context
Make `since-restart` return **every** log line from the `service.start` marker via client-side pagination (no 200-line cap), add an agent-bumpable `--limit` to the checkpoint-less `window`/`trace` modes, and rewrite `format_response()` so multi-service output is one globally time-ordered feed instead of per-stream blocks.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Script — pagination & limits

- [x] **Task 1: Add `PAGE_SIZE` constant and `query_range_all` pagination helper**
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Add `PAGE_SIZE=5000` near `DEFAULT_LIMIT` (`:11`, Loki's common `max_entries_limit_per_query` default). Add a new helper `query_range_all(logql, start_ns, end_ns)` placed after `query_range` (after `:117`). It loops: call `query_range "$logql" "$cursor" "$end_ns" "$PAGE_SIZE" "forward"`; from each response read the **maximum** `.data.result[].values[][0]` ns across all streams (use `jq` when available, fall back to the existing `grep -oE '"[0-9]{19}"'` style scan); accumulate each page's `.data.result` arrays into one combined Loki-shaped payload (`{"status":"success","data":{"result":[…]}}`) so `format_response` consumes it unchanged; set next `cursor = last_ns + 1`; stop when a page returns fewer than `PAGE_SIZE` entries **or** zero entries. **Termination guards (mandatory):** break if the page is short/empty, and break if the computed next cursor does not advance past the previous cursor (stalled cursor) — never spin. Merge pages with `jq` (e.g. reduce/`+` on `.data.result`); when `jq` is unavailable, fall back to a single `query_range` call at `PAGE_SIZE` (best-effort, document the limitation) rather than attempting a JSON-less merge.

- [x] **Task 2: Switch `since-restart` Step 2 to unbounded pagination** (depends on Task 1)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  In `cmd_since_restart` (`:158–230`) replace the Step 2 call `query_range "$log_query" "$restart_ts_ns" "$end_ns" "$DEFAULT_LIMIT" "forward"` (`:227`) with `query_range_all "$log_query" "$restart_ts_ns" "$end_ns"`. Drop the `$DEFAULT_LIMIT` argument entirely for this mode. Leave Step 1 (marker lookup, `backward limit=1`, `:196`) and all label/metadata semantics (`| event_name="service.start"`) unchanged.

- [x] **Task 3: Add `--limit N` flag to `window` and `trace`** (depends on Task 1)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  In `cmd_window` (`:264–318`): add a `--limit` case to the arg-parse loop (same validation pattern as `--level`/`--project`, require a value), defaulting the local to `DEFAULT_LIMIT` (200) when omitted; pass it to the single `query_range` call (`:315`). In `cmd_trace` (`:236–259`): parse args in a loop instead of `${1:-}` so a trailing `--limit N` is accepted (first positional = `trace_id`, `--limit` sets the bound), defaulting to `DEFAULT_LIMIT`; pass it to the `query_range` call (`:256`). These modes stay single-call bounded — no pagination. Update each subcommand's local `Usage:` line to show `[--limit N]`.

### Phase 2: Script — cross-service merge

- [x] **Task 4: Rewrite the `jq` branch of `format_response()` for global chronological order**
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Rewrite the `jq -r` program (`:45–55`) so it flattens **all** streams' `values[]` into one array where each element carries its stream's `project`/`service_name`/`level` alongside `[ns, msg]`, sorts the combined array by numeric ns (`sort_by(.[0] | tonumber)` or equivalent), then emits the existing line shape `[\(ts)] [\(level)] [\(project)/\(service)] \(msg)` per entry (keep the `gmtime`→`strftime` ts formatting for jq 1.6 compat). Preserve the empty-result short-circuit at `:39–42` ("No log lines matched.") and the `|| echo "$raw"` fallback. Single-stream input must remain byte-identical in ordering (a sort over one already-ordered stream is a no-op). Leave the non-`jq` `else` branch (`:56–72`) as-is (best-effort; global sort needs `jq`).

### Phase 3: Verification & docs

- [x] **Task 5: Verify `service.start` marker + anchor against a real restart** (depends on Task 2)
  Files: `src/skills/observe-logs/scripts/query-loki.sh`
  Against a real restart (`mind_api` server restart or `mind_mobile` app start), run `since-restart` and confirm: the marker query (`| event_name="service.start"`) finds the latest marker, the extracted anchor ts is correct, and logs from the restart forward are returned in order — including a feed exceeding the per-call `PAGE_SIZE` cap to confirm pagination crosses it and returns everything (>200 / >5000 lines when they exist). If the marker query or anchor extraction (`:194`, `:200–205`) is broken, fix it. If the local Loki has no qualifying restart to test against, document what was checked and leave the marker/anchor logic intact.

- [x] **Task 6: Update `SKILL.md` — `since-restart` and `window` sections** (depends on Tasks 2, 3, 4)
  Files: `src/skills/observe-logs/SKILL.md`
  `since-restart` section (`:77–106`): note it returns the **full feed** from the `service.start` marker with no line limit (client-side pagination past Loki's per-call cap). `window` section (`:129–147`): document `--limit N` (default 200, bump when 200 isn't enough), and document the two modes — clean single-service via `--service <svc>` vs merged cross-service via `--project <p>` with `--service` omitted — and that multi-service output is globally time-ordered by timestamp. Add `[--limit N]` to the usage line. Optionally mention `--limit` in the `trace` section. Keep frontmatter `name: observe-logs` unchanged.

## Commit Plan
- **Commit 1** (after tasks 1-3): "Add unbounded pagination and agent-controllable limit to query-loki"
- **Commit 2** (after tasks 4-6): "Merge cross-service logs chronologically and document new behavior"

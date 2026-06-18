# Code Review: observe-logs full restart feed (review 1)

**Scope:** `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/SKILL.md`
**Verified against:** plan tasks 1–6.

All six tasks are implemented as specified. The cross-service merge and the multi-page accumulator were tested with synthetic payloads and behave correctly (chronological interleave across services; page merge produces a valid Loki-shaped payload). Read-only discipline is preserved — `query_range_all` only calls the existing GET helper, no new endpoints. Termination guards are present and, for realistic data, the loop always advances. Findings below.

---

## Findings

### 1. [Medium] Cursor advance via `tonumber` is lossy on jq < 1.7 → duplicate lines across page boundaries

`query_range_all` computes the next cursor from
```
last_ns=$(echo "$page" | jq -r '[.data.result[].values[][0] | tonumber] | max // empty')
...
next_cursor=$((last_ns + 1))
```
`tonumber` converts the 19-digit nanosecond string to jq's internal number. On jq 1.7+ the literal precision is preserved (verified: `jq-1.7.1-apple` returns `1718800000000000456` intact), so on the current machine this works. But the formatter carries an explicit **"jq 1.6 compat"** comment (line 46) — i.e. the script intends to support jq 1.6, where numbers are IEEE-754 doubles and any value above 2^53 (~9e15) loses its low digits.

Under jq 1.6 the truncated `last_ns` (T) is ≤ the real max (R), so `next_cursor = T+1` is ≤ R. The next page starts at `T+1` and re-fetches every entry with ns in `(T, R]` — entries already returned in the previous page's tail. Since `format_response` does not de-duplicate, those lines appear **twice** in `since-restart` output at every full (5000-entry) page boundary. (In a pathological burst where 5000 entries fall within one precision quantum, `T+1` could even fall at/below the page start and trip the stall guard, causing premature termination / data loss — academic, but the same root cause.)

The same `tonumber` is used as the sort key in `format_response` (`ns: (.[0] | tonumber)` → `sort_by(.ns)`); on jq 1.6 two entries within the same precision quantum collapse to one key, so sub-microsecond interleave order is non-deterministic. Display is second-resolution, so this is cosmetic, but it shares the fix.

**Fix:** drop `tonumber` and take the max over the raw strings — all current ns values are exactly 19 digits, so lexicographic max equals numeric max, and bash `$((...))` handles the full-precision 19-digit int64 fine (verified):
```sh
last_ns=$(echo "$page" | jq -r '[.data.result[].values[][0]] | max // empty')
```
Optionally use the string for the sort key too (`sort_by(.ns)` over a zero-padded/equal-length string) to make ordering precision-independent. If jq 1.6 support is genuinely not a requirement, the alternative is to drop the "1.6 compat" comment and document jq ≥ 1.7 as required — but the string-max fix is cheaper and removes the dependency entirely.

---

### 2. [Low] `--limit` value is not validated as numeric

`cmd_window` / `cmd_trace` accept `--limit "$1"` and pass it straight into `query_range` → curl → Loki. A non-numeric value (`--limit abc`) is sent to Loki, which rejects it; `query_range` then exits 1 with `ERROR: Loki query failed (status=...)`. The failure is loud but the message doesn't point at the bad flag. A small guard (`[[ "$limit" =~ ^[0-9]+$ ]]` with a clear error) would localize the mistake. Low priority — degradation is safe, just less friendly.

---

### 3. [Note] Accumulator is re-parsed every page (O(n²))

Each loop iteration does `printf '%s\n%s' "$accumulated" "$page" | jq -s '...'`, re-serializing the entire accumulated result set per page. For typical "since restart" feeds (a few pages) this is fine. For a very large unbounded feed (tens of pages × 5000), wall-clock grows quadratically. Not a correctness issue and not worth fixing unless large feeds become common; flagging so it's a conscious trade-off. (A streaming approach — emit each page's formatted lines and sort once at the end, or append raw `.data.result` arrays without re-reading the accumulator — would avoid it, but both complicate the "one payload into `format_response`" contract.)

---

### 4. [Note] >PAGE_SIZE entries at an identical nanosecond would skip the remainder

If a single ns timestamp ever has more than 5000 entries, `next_cursor = last_ns + 1` skips past the surplus. This is inherent to nanosecond-cursor pagination and astronomically unlikely at real log rates; noted only for completeness. No action recommended.

---

## Summary

One Medium finding worth addressing before relying on `since-restart` in any jq-1.6 environment (finding 1 — duplicate lines); it is latent on the current jq 1.7.1 box but the code advertises 1.6 compat. The fix is a one-line change to string-max. Findings 2–4 are low/informational. Documentation (SKILL.md) accurately reflects the new behavior (full feed, `--limit`, single vs cross-service modes, global time ordering).

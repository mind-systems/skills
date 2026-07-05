# milestone-rescue: disposal-pinning — promote observations at the moment of routing

**Date:** 2026-07-05
**Source:** conversation context (live incident around milestone 52's deferred observations)

## Problem today

`orchestrator-artifacts/SKILL.md:63-64` closes the marker writer set with "All four
markers are written by `milestone-rescue-audit` only." That forces a ceremonial
`milestone-rescue-audit prune` run even when the observations were already surfaced
**and disposed of** in the same session: a rescue reads the review artifacts, the
observations get routed into roadmap tasks right there (live case: milestone 52's
three observations → specs 07/08 via `/roadmap-decompose` in the same chat), and the
only remaining work for an audit run would be stamping markers on decisions already
made. In the live case the entries were hand-pinned `[promoted → <spec>]` outside the
ratified writer set — the pattern works and must be legalized.

The correct invariant: **whoever disposes of an observation pins it, at the moment of
disposal.** As soon as the task lands in the roadmap, the entry it came from carries
its marker. `milestone-rescue-audit` prune mode remains the sweeper for *orphaned*
(undisposed) observations — it is not the monopolist over the grammar.

## The change (two files, one contract)

### 1. `src/skills/orchestrator-artifacts/SKILL.md` §6 (one sentence, `:63-64`)

Replace "All four markers are written by `milestone-rescue-audit` only." with a
writer-set statement: markers are written by downstream **disposal** tools, never by
the reviewer; `[promoted → <path>]` is written by whichever disposal skill routes the
observation into a roadmap task — at the moment of routing; the evaluative markers
`[audit-corroborated]` / `[audit-dismissed]` and the sweep marker
`[unrouted-reported]` remain `milestone-rescue-audit`'s. Everything else in §6 —
marker names, append-only accumulation, entry text / `Affects:` never rewritten, the
**pinned** definition, the sibling dedup rule — stays byte-identical.

### 2. `src/skills/milestone-rescue/SKILL.md` — new Step 5.6

Insert a lean step (~10 lines) between Step 5.5 (`:385-417`) and "What NOT to do"
(`:419`): **Step 5.6 — Pin disposed observations.** When deferred-observation entries
encountered in the artifacts read this session are routed into roadmap tasks — a new
task + spec written (e.g. via `/roadmap-decompose` in the same chat) or folded into a
spec repaired at Step 5 — append `` [promoted → <spec path>] `` to the entry, and to
**every sibling occurrence** across that milestone's review files, per the engine's
dedup rule (cite the engine; do not redefine grammar or pinned-ness). Pin at the
moment the task/spec lands, not at session end. Rescue writes **only** `[promoted →
<path>]`: it routes, it does not evaluate — dismissing, corroborating, and sweeping
unrouted entries stay `milestone-rescue-audit`'s. Entries not disposed in-session stay
unmarked, for audit prune mode.

One matching clause in "What NOT to do": do not write `[audit-corroborated]`,
`[audit-dismissed]`, or `[unrouted-reported]`, and do not dismiss an observation by
marker — rescue's only marker is `[promoted → <path>]`, only for observations actually
routed into a task or spec this session.

## Guards

- **Writer-set change only** — the marker grammar (names, append-only, pinned
  definition, dedup) is untouched in the engine; callers cite it, never redefine it.
- **`milestone-rescue-audit`'s body is untouched** — it never claims exclusivity in
  its own text (verified by grep this session); its prune mode already treats any
  marker as pinned, so rescue-promoted entries are skipped naturally; its rescue-mode
  corroboration pass is unaffected.
- **`roadmap-prune`'s gate is untouched** — the pinned check is writer-agnostic by
  construction.
- `milestone-rescue`'s `allowed-tools` already includes `Edit` (`:13`) — no
  frontmatter change.
- The engine is load-once with three loaders (`grep -l "orchestrator-artifacts"` →
  rescue, audit, prune) — re-run the grep at implementation time and keep all three
  coherent with the new sentence.
- ≤500 lines: rescue is 446 today — keep Step 5.6 lean; the engine is 70.

## How to verify

1. `grep -n "written by" src/skills/orchestrator-artifacts/SKILL.md` → the writer-set
   sentence names disposal tools and the per-marker split; no sole-writer claim
   remains.
2. `src/skills/milestone-rescue/SKILL.md` has Step 5.6 with `[promoted → <path>]`,
   the sibling-dedup citation, and the moment-of-routing rule; "What NOT to do" bans
   the other three markers.
3. `git diff src/skills/milestone-rescue-audit/SKILL.md` → empty.
4. Behavior baseline: milestone 52's hand-pinned entries (7 occurrences, 3 dedup
   groups, markers pointing at specs 07/08) are exactly the output Step 5.6 would have
   produced — the live pattern is now the documented behavior.

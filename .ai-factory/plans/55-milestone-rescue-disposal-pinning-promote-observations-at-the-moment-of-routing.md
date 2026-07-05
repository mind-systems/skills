# Plan: milestone-rescue: disposal-pinning — promote observations at the moment of routing

## Context
Legalize the real invariant that whoever disposes of a deferred observation pins it at the moment of routing: split the engine's marker writer-set so `[promoted → <path>]` belongs to the disposal skill, and give `milestone-rescue` a lean Step 5.6 that pins promoted entries when a task/spec lands. No behavior change to `milestone-rescue-audit` or `roadmap-prune`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Writer-set split in the engine

- [x] **Task 1: Replace the sole-writer sentence in §6 with a writer-set split**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In §6 "Status-marker grammar" (`:63-64`), replace the final sentence "All four markers are written by `milestone-rescue-audit` only." with a writer-set statement: markers are written by downstream **disposal** tools, never by the reviewer; `[promoted → <path>]` is written by whichever disposal skill routes the observation into a roadmap task, at the moment of routing; the evaluative markers `[audit-corroborated]` / `[audit-dismissed]` and the sweep marker `[unrouted-reported]` remain `milestone-rescue-audit`'s. Change **only** that closing sentence — leave everything else in §6 byte-identical: the marker names/list (`:58-60`), append-only accumulation, the "Entry text and `Affects:` are never rewritten" line, the **Pinned** definition, and the sibling dedup rule (`:61-63`). The Edit matches the sole-writer sentence by exact string, so the approximate line hints do not need to be exact. Do not touch §5's reviewer-never-writes-markers line — it already holds.

### Phase 2: Rescue pins what it routes

- [x] **Task 2: Add Step 5.6 and its What-NOT-to-do clause to milestone-rescue** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Insert a new lean step (~10 lines, no rationale prose) between the end of Step 5.5 (`:417`) and the `## What NOT to do` header (`:419`):
  - **`## Step 5.6 — Pin disposed observations.`** When deferred-observation entries encountered in the artifacts read this session are routed into roadmap tasks — a new task + spec written (e.g. via `/roadmap-decompose` in the same chat) or folded into a spec repaired at Step 5 — append `` [promoted → <spec path>] `` to the entry and to **every sibling occurrence** across that milestone's review files, **per the engine's dedup rule** (cite `orchestrator-artifacts` §6; do not redefine the grammar, the pinned definition, or the dedup rule). Scope the pin to review files **still present on disk** at pin time — Step 5 may already have deleted the rescued slug's review files (spec / spec+plan delete both genres; spec+plan+code and plan-ratified delete reviews, keep plan-reviews), and a deleted file has nothing to pin and nothing left for `roadmap-prune`'s gate to flag. Pin at the moment the task/spec lands, not at session end. Entries not disposed in-session stay unmarked, left for `milestone-rescue-audit` prune mode.
  - Follow the existing Step 5.5 heading style (`## Step 5.5 — …` with a trailing `---` separator before `## What NOT to do`).
  - Add one matching bullet to `## What NOT to do` (`:419-446`): do not write `[audit-corroborated]`, `[audit-dismissed]`, or `[unrouted-reported]`, and do not dismiss an observation by marker — rescue's only marker is `[promoted → <path>]`, written only for observations actually routed into a task or spec this session (evaluating/dismissing/sweeping stay `milestone-rescue-audit`'s).
  - Guards: no frontmatter change (`allowed-tools` already includes `Edit` at `:13`); keep the addition lean so the file stays ≤500 lines (446 today).

- [x] **Task 3: Verify guards** (depends on Task 2)
  Files: (verification only — no new edits unless a guard fails)
  Confirm the change is a writer-set split and nothing else drifted:
  - `grep -n "written by" src/skills/orchestrator-artifacts/SKILL.md` → the writer-set sentence names disposal tools and the per-marker split; no sole-writer claim remains.
  - `git diff src/skills/milestone-rescue-audit/SKILL.md` → empty (audit body untouched; it never claimed exclusivity in its own text).
  - `git diff src/skills/roadmap-prune/SKILL.md` → empty (prune gate is writer-agnostic).
  - `wc -l src/skills/milestone-rescue/SKILL.md` → ≤500.
  - Behavior baseline: milestone 52's hand-pinned entries (markers pointing at specs 07/08, every sibling occurrence marked) are exactly what Step 5.6 would now produce.

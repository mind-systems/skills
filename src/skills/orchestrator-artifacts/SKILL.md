---
name: orchestrator-artifacts
description: >-
  Shared description of the orchestrator's on-disk artifact protocol — directory
  layout, PASS signals, sidecar fields, the `## Deferred observations` section
  format, and the status-marker grammar. Pure protocol reference, no procedure.
  Loaded by milestone-rescue, milestone-rescue-audit, and roadmap-prune so each
  stops re-describing the layout inline. Use when reading or writing plans,
  plan-reviews, reviews, or sidecars under `.ai-factory/`.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---

# Orchestrator Artifacts — the File Protocol

This is a load-once engine: its callers depend on its exact behavior — edits here
must honor their expectations as part of its contract; the reverse graph resolves
via `` grep -l "orchestrator-artifacts" src/skills/*/SKILL.md src/commands/*.md ``.

## 1. Layout

Artifacts live under the target repo's `.ai-factory/`: `plans/` (`<seq>-<slug>.md`
plan + `<seq>-<slug>.json` sidecar), `plan-reviews/` (`<seq>-<slug>-plan-review-N.md`),
`reviews/` (`<seq>-<slug>-review-N.md`). Test mode adds `test-runs/` (`<seq>-<slug>-test-N.txt`)
and roots at `ROADMAP_TESTS.md`. This flat layout is for the default pair
(`ROADMAP.md`/`ROADMAP_TESTS.md`); a named roadmap's artifacts live under a
subdirectory keyed by its roadmap file stem — `roadmaps/kg-wmservice.md` →
`plans/kg-wmservice/…`, same stem segment under `plan-reviews/`, `reviews/`,
`test-runs/`. `<seq>` is assigned by the orchestrator at plan time and is not
recoverable from a roadmap line; `N` is the round number — files in round order are
the finding→fix history. Numbering is per-directory — each subdirectory carries its
own `<seq>` axis.

## 2. Signals

A review passes when its file ends with `PLAN_REVIEW_PASS` / `REVIEW_PASS`
(`TEST_PASS` for test runs) on its own last line; no signal on the last round means
the stage did not pass.

## 3. Sidecar fields

`planner`, `implementer` (resumable session ids), `step` (resume point — the closed
set and its artifact requirements live in `milestone-rescue`, its only writer),
`elapsed` (seconds, cumulative).

## 4. Committed ⇔ completed

The orchestrator commits a milestone's artifacts together with the milestone;
tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight
work.

## 5. `## Deferred observations` section

Present in both review genres. Entry: `- Affects: <phase / spec-note path /
"unknown"> — <observation>`. The section may be absent. Entries are non-findings —
a review with only them still passes. The reviewer never writes or imitates status
markers — the field after the observation text is reserved for downstream tools.

## 6. Status-marker grammar

Append-only space-separated bracketed suffix at the end of the entry line. Written by
the **resolution session** — the dedicated session the user opens from the parked
prune's handoff — at the moment it disposes of an observation:

- `[fixed]` — the gap is fixed directly in this session
- `[routed → <path>]` — routed into an **open** task's spec; `<path>` must resolve to
  an editable surface (an open task's spec note), never a completed or frozen one
- `[dismissed]` — evaluated and found moot, stale, or already handled

The reviewer never writes or imitates markers. Entry text and `Affects:` are never
rewritten — markers only accumulate. **Pinned** = the entry line carries ≥1 marker.
Dedup rule: whoever pins an entry pins every occurrence across that milestone's
review files (dedup by `Affects:` target + gist).

**Legacy markers** `[promoted → <path>]`, `[audit-corroborated]`, `[audit-dismissed]`,
`[unrouted-reported]` are retired from the active vocabulary; encountered in old
repos they still count as pinned (lazy migration — history is never rewritten).

## 7. Mirrors-the-orchestrator invariant

This file mirrors the orchestrator's file protocol (`orchestrator/main.py`,
`agents.py`, `prompts/reviewer.md`) — if the protocol changes there, update this
file; do not let them diverge.

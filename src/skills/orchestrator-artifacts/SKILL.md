---
name: orchestrator-artifacts
description: >-
  Shared description of the orchestrator's on-disk artifact protocol — directory
  layout, PASS signals, sidecar fields, the `## Deferred observations` section
  format, and the status-marker grammar. Pure protocol reference, no procedure.
  Loaded by milestone-rescue, milestone-rescue-audit, and roadmap-prune so each
  stops re-describing the layout inline. Use when reading or writing plans,
  plan-reviews, reviews, patches, or sidecars under `.ai-factory/`.
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
`reviews/` (`<seq>-<slug>-review-N.md`), `patches/` (test mode bridges reviewer output
here; empty in implement mode). Test mode adds `test-runs/` (`<seq>-<slug>-test-N.txt`)
and roots at `ROADMAP_TESTS.md`. `<seq>` is assigned by the orchestrator at plan time
and is not recoverable from a roadmap line; `N` is the round number — files in round
order are the finding→fix history.

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

Append-only space-separated bracketed suffix at the end of the entry line. Markers:
`[promoted → <path>]`, `[unrouted-reported]`, `[audit-corroborated]`,
`[audit-dismissed]`. Entry text and `Affects:` are never rewritten — markers only
accumulate. **Pinned** = the entry line carries ≥1 marker. Dedup rule: whoever pins
an entry pins every occurrence across that milestone's review files (dedup by
`Affects:` target + gist). Markers are written by downstream **disposal** tools,
never by the reviewer; `[promoted → <path>]` is written by whichever disposal skill
routes the observation into a roadmap task, at the moment of routing; the
evaluative markers `[audit-corroborated]` / `[audit-dismissed]` and the sweep
marker `[unrouted-reported]` remain `milestone-rescue-audit`'s.

## 7. Mirrors-the-orchestrator invariant

This file mirrors the orchestrator's file protocol (`orchestrator/main.py`,
`agents.py`, `prompts/reviewer.md`) — if the protocol changes there, update this
file; do not let them diverge.

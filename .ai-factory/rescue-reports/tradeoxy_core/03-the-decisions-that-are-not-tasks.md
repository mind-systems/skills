# The decisions that are not tasks

**Project:** tradeoxy_core
**Date:** 2026-09-08
**Written by:** the architect that decomposed Phase 46, from the same session's measurements

## What this file is

The third report of the same week, covering three events that changed the work materially and that no artifact genre holds. `01` asks what the week cost and why its record does not survive; `02` asks what a round is actually spent on. This one collects the decisions that are not tasks at all — a task closed by human judgment, a task deleted outright, and the model correction that ended the most expensive loop of the arc. It contradicts neither companion.

## One — a task closed by hand over a review that never passed

Exactly two slugs in the entire corpus have reviews on disk and no `REVIEW_PASS` token in any of them: slug 121 (task 38.1, the explicit-start correlation surface on `replay.proto`) and slug 137 (task 39.6.2.1.1, the order-axis scripted-double harness). Both roadmap lines carry `[x]`. All four review files are committed. Both sidecars stand at `review_failed:3` and will stand there permanently.

Neither is an accident. The operator's own account is that these were closed by hand, having read the review and judged the remaining findings acceptable. The surviving evidence agrees. Slug 121's round-3 verdict reads: "The rescoped change is correct, complete, and fully green (parse-check 8/8, `replay-rpc.spec.ts` 8/8, `tsc` clean); the review-2 blocker is resolved. The sole outstanding item is a minor documentation-convention nit — a plan-layer citation in the new proto comment — which does not affect behavior." Slug 137 closed after the review's own recommendation was carried out: the unrelated documentation edits sitting in the same working tree went out as `b9a7210` ("Docs update"), and the task's own files followed three minutes later as `b43e80f`.

Twice in the whole corpus makes this a rare and deliberate act, not a leak. What is missing is not the outcome — the roadmap has it right — but the reason. Nothing anywhere records what was judged acceptable, or why. A reader arriving at slug 137's sidecar a year from now finds `review_failed:3` and no way to learn that a person looked at it and decided.

This distortion runs **opposite** to the one `01` describes, and the pair is worth holding together. A rescue deletes the plan-reviews of the attempt it repairs, so a task that died three times and passed on the fourth is recorded permanently as having passed cleanly: the record is biased toward success. A hand-close freezes the sidecar at failure for a task that shipped: the record is biased toward failure. The two point in opposite directions and hide the same thing — the moment a human judged.

One thread runs out of this. The nit that cost slug 121 its formal pass was a plan-layer citation inside a proto comment, a violation of the project's own rule that a code comment never carries a spec path. The same class is live in the tree today: `src/replay/__tests__/replay-start.service.spec.ts:11` reads `// ReplayStartService — spec (see .ai-factory/specs/74-replay-layout-run-resolution.md)`, and it is the only such comment anywhere under `src/` or `proto/`. One instance of the class was weighed and accepted deliberately; the other has never been looked at by anyone.

## Two — a task deleted with no replacement

Commit `fa53204` removed task 39.7, "Empty-delta guard: a run-owned order-axis slot never leaks through a live candle event", as a single deletion line in the roadmap with nothing put in its place. It appears in no cost table, and whatever it cost to plan is not recoverable.

Two tasks were cancelled in this arc, for opposite reasons. 38.7 was cancelled because its requirement had already been discharged elsewhere — authorization happens where the subscription id enters core, and every later use inherits it. 39.7 was cancelled because a change of model removed the junction it existed to guard. `01` records the first and does not mention the second.

Neither cancellation is visible from the roadmap, because a removed line leaves nothing behind. 38.7 survives only as a passing mention inside 38.6's own completed line; 39.7 survives only inside a commit diff. A reader who wants to know which tasks were considered and dropped has no place to look.

## Three — the correction that ended the loop, and carries no task number

Commit `fa53204`, 20 August 2026, did five things at once: replaced task 39.6.2 with 39.6.2.1 and 39.6.2.2, deleted 39.7, added 39.8 and 39.9, and rewrote two governing documents.

In `docs/indicator-engine/spec-v2/11-consumers-and-sinks.md` the sentence "…the subscription id, not the slot's absence, is what separates it from live" is removed and "what separates a run from live is where its engines live, not a check performed at each junction" is added — verified as exactly one occurrence each, one on a removal line and one on an addition line. In `docs/backtest-replay/04-order-axis-participation.md` the same commit adds: "Core's own isolation is structural rather than checked: no engine a backtest run drives sits in the live runtime's pool."

Before that commit, isolation was a **checked** invariant inside a shared engine pool. Every task in the family therefore had to guard whichever junction the shared pool exposed next: 39.4 guarded slot selection and the live-dispatch exemption, 39.6.1 needed a narrower teardown because the shared one unconditionally released resources a run-owned instance did not own, and 39.7 was written because the candle-close handler iterated every slot including the run's own. Each split patched a junction. None removed the cause. The loop ended when the model was rewritten so that no engine a run drives enters the pool at all — after which there is nothing left to check, and the guards became dead code that tasks 39.8 and 39.9 are still open to delete.

The consequence for the record is the point of this section. The most consequential change of the entire arc is a documentation commit. It carries no task number, contributes to no elapsed total, produced no plan, no review and no rescue, and is invisible to anyone reading either the roadmap or the artifact tree. Recovering it here required diffing two governing documents against a commit found by searching the roadmap's history for a task number that no longer exists.

## What the three have in common

None of them is a task, a plan, a review or a rescue. Every artifact genre this pipeline produces is keyed to the execution of a task, so a decision that *removes* a task, *closes* one on judgment, or *changes the model the tasks were derived from* has no genre to land in. It lands in a commit diff, in a handoff written at the end of a session, or nowhere.

A note on method, because two of these three were nearly got wrong in the writing. The causal account of 38.7's cancellation exists in two places — a session handoff and report `01` — and in no artifact of the decision itself. Both are descriptions written after the fact by the people who acted. In this session that account was first repeated as established fact and had to be walked back to an attribution. A handoff is evidence of what someone concluded; it is not evidence of what happened, and where the two are treated as the same thing the record acquires confidence it has not earned.

## What would hold them

These are precisely the events a durable report exists to preserve, and not one of them would ever be produced by a rescue run — because not one of them is a rescue. A record keyed to failures of task execution cannot hold the decisions that delete a task, close it by hand, or move the ground it stood on. Those need a place of their own, or they keep surviving only in commit diffs and in the memory of the session that made them.

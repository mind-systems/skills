# Task Spec — milestone-rescue: sidecar lifecycle on full reset + detect non-convergence (done-but-unrecognized)

**Date:** 2026-06-01
**Roadmap:** ROADMAP.md Milestones
**Provenance:** bug found while running milestone-rescue on the `command-handoff` milestone.

## Current state

`milestone-rescue/SKILL.md` Step 5 ("Apply and clean up") deletes the slug's `plan-reviews/`, `reviews/`, `patches/`, and the plan `.md`, but has a hard rule: **never delete the `.json` sidecar — instead rewrite its `step` in place.** The sidecar `step` is set from a table keyed on what remains on disk after cleanup (e.g. plan-reviews deleted → `"planned"`).

This is wrong for a **full reset** (re-plan case), where the plan `.md` itself is deleted and the milestone will be re-planned from scratch:

- `step: "planned"` means "a plan exists / planning is done" — but the plan `.md` was just deleted. The orchestrator reads a state that contradicts the disk, and mis-steps (treats the milestone as ready for plan-review when there is no plan).
- `planner`, `implementer`, and `elapsed` in the sidecar describe a run that no longer exists. When the task is re-planned from scratch the old attempt is gone, so that data — including the elapsed time — is stale and misleading, not worth preserving.

The fixed-`step` table and the "do NOT delete the sidecar" rule were written assuming the sidecar should always survive cleanup. That holds for a re-implement, not for a full reset.

**Second gap — no path for "done, but the pipeline didn't recognize it."** Step 2 classifies any "no `REVIEW_PASS`" state as an implement-phase *failure* and Step 4 always proposes a milestone-description change (spec-gap / scope / mechanical). But a milestone can fail to converge while the implementation is actually complete and correct: every review round concludes non-blocking ("none block", "good shape") yet never emits the `REVIEW_PASS` token, each round surfaces fresh Low/Informational nits, the implementer fixes them, and the loop exhausts its iteration limit (`step: "review_failed:N"`). Here the milestone description is **not** the cause — the reviews confirm the implementation matches the spec — so proposing a description change is the wrong remedy.

## Target

Two changes to `milestone-rescue/SKILL.md`, both about classifying failure modes correctly.

### Change A — sidecar lifetime tracks the plan's

Make sidecar handling in Step 5 **conditional on what survives the cleanup**:

1. **Full reset (re-plan)** — the plan `.md` and plan-reviews are deleted, so nothing of the old plan remains. **Delete the `.json` sidecar too**, with the same git-native commands used for the other artifacts (`git rm -f` if staged/tracked, `git clean -f` if untracked). The orchestrator then sees no sidecar and treats the milestone as new, re-planning cleanly. Accept the loss of `elapsed`/`planner`/`implementer` — it describes a discarded attempt.

2. **Re-implement** — the plan `.md` and its passing plan-reviews are kept; only `reviews/`/`patches/` are deleted. **Keep the sidecar and update `step` in place** (`"plan_reviewed"`), exactly as today, preserving `planner`/`implementer`/`elapsed`. State tracking is still valid here because the plan survives.

3. Update the skill text so the two paths are explicit: the "do NOT delete the `.json` sidecar" hard rule gains a carve-out — *the sidecar is deleted iff the plan `.md` is deleted (full reset); otherwise it is updated in place.* Reconcile the sidecar `step` table accordingly (the "plan-reviews deleted → planned" row becomes "delete the sidecar" instead of writing `"planned"`).

Rule of thumb to encode: **the sidecar's lifetime tracks the plan's.** Plan gone → sidecar gone. Plan kept → sidecar updated.

### Change B — detect non-convergence (implementation done, pipeline didn't recognize it)

Add a classification branch so the skill stops treating a stuck-but-correct milestone as a defect:

1. **Detection (Step 2).** Before declaring a generic implement-phase defect, test for non-convergence: **no review contains `REVIEW_PASS`, every review verdict is non-blocking** (all findings Low/Informational — no Blocking/Critical), **and the plan's deliverables exist on disk** (the files the plan said to create/modify are present). When all three hold, classify as **non-convergence (done-but-unrecognized)**, not a defect.

2. **Action (Step 4).** For this classification, do **not** propose a milestone-description change — the description isn't the cause. Instead surface to the user: the implementation appears complete and correct (N non-blocking rounds, deliverables present); the pipeline failed only to emit `REVIEW_PASS` (reviewer kept generating cosmetic nits). Recommend **committing the deliverable** (after any remaining trivial nits) rather than re-running, which would likely loop again. Optionally fold genuinely **recurring, spec-traceable** nits back into the spec note before committing.

3. Keep the existing defect flow unchanged for real failures — if **any** review carries a Blocking/Critical finding, or the deliverables are absent, it is a normal implement-phase failure: use the standard Step 3/Step 4 propose-update path.

## Guards

- **Only delete the sidecar on a full reset** (plan `.md` deleted). In the re-implement path the sidecar must survive with `step: "plan_reviewed"` — deleting it there would lose valid in-flight state.
- **Non-convergence is a high-bar classification** — trigger it only when deliverables verifiably exist AND every round is non-blocking. A single Blocking/Critical finding, or missing deliverables, means a real defect → standard flow. Never use it to mask an unfinished implementation.
- Use **git-native deletion only** (`git rm -f` / `git clean -f`), consistent with the rest of Step 5; never plain `rm`.
- `elapsed`-time loss on full reset is **intended**, not a regression — the value is invalid once the task is re-planned from scratch.
- `milestone-rescue` is a custom / never-overwrite-from-upstream skill (CLAUDE.md line 95) — safe to edit directly, no divergence registration needed.

## Files

- `~/projects/skills/.claude/skills/milestone-rescue/SKILL.md` (modify) — Change A: Step 5 sidecar handling (conditional delete-vs-update, hard-rule carve-out, `step` table reconciliation). Change B: Step 2 non-convergence detection + Step 4 recommend-commit branch.

## Verify

- Running milestone-rescue on a **plan-phase / full-reset** failure deletes all four artifact types **and** the `.json` sidecar; no sidecar remains for the slug.
- Running it on an **implement-phase** failure keeps the plan + plan-reviews, deletes reviews/patches, and leaves the sidecar with `step: "plan_reviewed"` and `planner`/`implementer`/`elapsed` intact.
- After a full reset, the next orchestrator run re-plans the milestone from scratch (no contradictory `step`).
- On a milestone where all review rounds are non-blocking and the deliverables exist, the skill reports **non-convergence** and recommends committing — it does **not** propose a milestone-description change.
- On a milestone with a Blocking/Critical review finding or missing deliverables, the skill still runs the standard defect flow (propose update / decompose).

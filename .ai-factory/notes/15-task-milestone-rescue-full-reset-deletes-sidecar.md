# Task Spec — milestone-rescue: delete the sidecar on a full reset, not just rewrite its step

**Date:** 2026-06-01
**Roadmap:** ROADMAP.md Milestones
**Provenance:** bug found while running milestone-rescue on the `command-handoff` milestone.

## Current state

`milestone-rescue/SKILL.md` Step 5 ("Apply and clean up") deletes the slug's `plan-reviews/`, `reviews/`, `patches/`, and the plan `.md`, but has a hard rule: **never delete the `.json` sidecar — instead rewrite its `step` in place.** The sidecar `step` is set from a table keyed on what remains on disk after cleanup (e.g. plan-reviews deleted → `"planned"`).

This is wrong for a **full reset** (re-plan case), where the plan `.md` itself is deleted and the milestone will be re-planned from scratch:

- `step: "planned"` means "a plan exists / planning is done" — but the plan `.md` was just deleted. The orchestrator reads a state that contradicts the disk, and mis-steps (treats the milestone as ready for plan-review when there is no plan).
- `planner`, `implementer`, and `elapsed` in the sidecar describe a run that no longer exists. When the task is re-planned from scratch the old attempt is gone, so that data — including the elapsed time — is stale and misleading, not worth preserving.

The fixed-`step` table and the "do NOT delete the sidecar" rule were written assuming the sidecar should always survive cleanup. That holds for a re-implement, not for a full reset.

## Target

Make sidecar handling in Step 5 **conditional on what survives the cleanup**:

1. **Full reset (re-plan)** — the plan `.md` and plan-reviews are deleted, so nothing of the old plan remains. **Delete the `.json` sidecar too**, with the same git-native commands used for the other artifacts (`git rm -f` if staged/tracked, `git clean -f` if untracked). The orchestrator then sees no sidecar and treats the milestone as new, re-planning cleanly. Accept the loss of `elapsed`/`planner`/`implementer` — it describes a discarded attempt.

2. **Re-implement** — the plan `.md` and its passing plan-reviews are kept; only `reviews/`/`patches/` are deleted. **Keep the sidecar and update `step` in place** (`"plan_reviewed"`), exactly as today, preserving `planner`/`implementer`/`elapsed`. State tracking is still valid here because the plan survives.

3. Update the skill text so the two paths are explicit: the "do NOT delete the `.json` sidecar" hard rule gains a carve-out — *the sidecar is deleted iff the plan `.md` is deleted (full reset); otherwise it is updated in place.* Reconcile the sidecar `step` table accordingly (the "plan-reviews deleted → planned" row becomes "delete the sidecar" instead of writing `"planned"`).

Rule of thumb to encode: **the sidecar's lifetime tracks the plan's.** Plan gone → sidecar gone. Plan kept → sidecar updated.

## Guards

- **Only delete the sidecar on a full reset** (plan `.md` deleted). In the re-implement path the sidecar must survive with `step: "plan_reviewed"` — deleting it there would lose valid in-flight state.
- Use **git-native deletion only** (`git rm -f` / `git clean -f`), consistent with the rest of Step 5; never plain `rm`.
- `elapsed`-time loss on full reset is **intended**, not a regression — the value is invalid once the task is re-planned from scratch.
- `milestone-rescue` is a custom / never-overwrite-from-upstream skill (CLAUDE.md line 95) — safe to edit directly, no divergence registration needed.

## Files

- `~/projects/skills/.claude/skills/milestone-rescue/SKILL.md` (modify) — Step 5 sidecar handling: conditional delete-vs-update, the hard-rule carve-out, and the `step` table reconciliation.

## Verify

- Running milestone-rescue on a **plan-phase / full-reset** failure deletes all four artifact types **and** the `.json` sidecar; no sidecar remains for the slug.
- Running it on an **implement-phase** failure keeps the plan + plan-reviews, deletes reviews/patches, and leaves the sidecar with `step: "plan_reviewed"` and `planner`/`implementer`/`elapsed` intact.
- After a full reset, the next orchestrator run re-plans the milestone from scratch (no contradictory `step`).

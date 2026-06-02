# Plan: milestone-rescue: sidecar lifecycle + non-convergence detection

## Context
Fix two failure-mode classification bugs in `milestone-rescue/SKILL.md`: (A) the JSON sidecar must be deleted on a full reset instead of rewritten with a contradictory `step`, and (B) a done-but-unrecognized milestone (no `REVIEW_PASS`, all rounds non-blocking, deliverables present) must be classified as non-convergence and recommended for commit rather than a description change.

Target file: `.claude/skills/milestone-rescue/SKILL.md` (the top-level `milestone-rescue/` path is a symlink target; the real file lives under `.claude/skills/`).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Change A — sidecar lifetime tracks the plan's

- [x] **Task 1: Make the Step 5 cleanup deletion conditional on the Step 2 classification**
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  Prerequisite for the whole of Change A (see plan-review-1 Issue #1). The current cleanup block (lines ~185–195) deletes the plan `.md` **and** all plan-reviews unconditionally, so the "plan `.md` survives" discriminator the sidecar logic relies on never holds and the re-implement path would be dead code. Split the cleanup into two branches keyed on the failure mode from Step 2:
  - **Plan-phase failure / full reset** → delete plan `.md` + plan-reviews + reviews + patches (all four artifact types) for the slug. Nothing of the old plan remains.
  - **Implement-phase failure / re-implement** → **keep** the plan `.md` and its passing plan-reviews; delete only `reviews/` and `patches/` for the slug.
  Keep using git-native deletion only (`git clean -f -- <path>` for `??` untracked, `git rm -f -- <path>` for `A ` staged/added) — never plain `rm`. This realizes note Verify #60–61 (full-reset deletes all four; implement-phase keeps plan + plan-reviews, deletes reviews/patches).

- [x] **Task 2: Make sidecar handling conditional on plan `.md` survival** (depends on Task 1)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  In Step 5, after the conditional cleanup from Task 1, branch the sidecar handling per the spec note "Change A":
  - **Full reset (plan `.md` deleted)** — **delete the `.json` sidecar too**, using the same git-native commands (`git rm -f` if staged/tracked, `git clean -f` if untracked). Accept the loss of `planner`/`implementer`/`elapsed` — it describes a discarded attempt; note that this loss is intended, not a regression.
  - **Re-implement (plan `.md` kept)** — keep the sidecar and update `step` to `"plan_reviewed"` in place, preserving `planner`/`implementer`/`elapsed`, exactly as today.
  Encode the rule of thumb verbatim from the note: **the sidecar's lifetime tracks the plan's — plan gone → sidecar gone; plan kept → sidecar updated.**

- [x] **Task 3: Carve the exception into the "do NOT delete the sidecar" rule and reconcile the `step` table, emit text, and What-NOT-to-do** (depends on Task 2)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  - Rewrite the hard rule at lines ~193–195 ("Do NOT delete `.json` sidecar files...") to add the carve-out: *the sidecar is deleted iff the plan `.md` is deleted (full reset); otherwise it is updated in place.*
  - Reconcile the `step` table (lines ~208–217): the "Plan-reviews deleted (or none pass) → `"planned"`" row becomes **delete the sidecar** (full-reset path) instead of writing `"planned"`. Keep the `"plan_reviewed"` rows for the re-implement path. Reconcile the "sidecar doesn't exist" and the fall-through (both pass → orchestrator finished) rows so they stay consistent with the new branching.
  - Update the matching bullet in "What NOT to do" (lines ~280–281) so it no longer claims `step` is the only thing ever changed — reflect that the sidecar is deleted on full reset.
  - Adjust the "Sidecar updated: step set to..." emit (line ~227) so it fires only on the re-implement path; add an equivalent line reporting the sidecar deletion on the full-reset path.

### Phase 2: Change B — detect non-convergence (done-but-unrecognized)

- [x] **Task 4: Add non-convergence detection to Step 2** (depends on Task 3)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  In Step 2 ("Classify failure mode"), before declaring a generic implement-phase defect, add a **non-convergence (done-but-unrecognized)** branch that triggers only when all three high-bar conditions hold:
  1. No review file contains `REVIEW_PASS` on its own line.
  2. Every review verdict is non-blocking — all findings Low/Informational, no Blocking/Critical.
  3. The plan's deliverables show evidence of having been produced/modified on disk — not mere file presence (for `modify`-type deliverables, where the target file pre-existed, look for the patches/reviews confirming the change landed rather than treating "file exists" as sufficient; see plan-review-1 Issue #4).
  When all three hold, classify as non-convergence — not a defect. If **any** review carries a Blocking/Critical finding, or deliverables are absent/unproduced, keep the existing implement-phase failure classification (standard flow). State the classification explicitly, as the step already requires. Keep the severity inspection here lightweight — a non-blocking/blocking check, not a full Step 3 issue extraction (see plan-review-1 Issue #5).

- [x] **Task 5: Add the recommend-commit branch to Step 4** (depends on Task 4)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  In Step 4 ("Propose milestone update"), add a branch for the non-convergence classification that does **not** propose a milestone-description change. Instead, surface to the user (via `AskUserQuestion`, matching existing template style): the implementation appears complete and correct (N non-blocking rounds, deliverables present); the pipeline only failed to emit `REVIEW_PASS` (reviewer kept generating cosmetic nits). Recommend **committing the deliverable** (after any remaining trivial nits) rather than re-running, which would likely loop again. Optionally fold genuinely recurring, spec-traceable nits back into the spec note before committing. Leave the existing spec-gap / mechanical-error / scope-overload templates unchanged for real defects.

- [x] **Task 6: Make Step 5 and Step 5.5 no-op for the non-convergence branch** (depends on Task 5)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  Resolves plan-review-1 Issues #2 and #3 — without this, control would flow from the accepted commit recommendation into the normal Step 5, which would delete the very artifacts being committed and reset the sidecar to `"plan_reviewed"`, contradicting the recommendation.
  - In Step 5, add explicit handling: when the classification is non-convergence and the user accepted the commit recommendation, **skip the artifact cleanup and the sidecar update entirely** — leave plans/plan-reviews/reviews/patches and the sidecar in place pending the commit.
  - In Step 5.5, add one sentence stating that for a non-convergence classification there are no real defects to propagate (every round was non-blocking), so propagation no-ops — do not surface cosmetic nits to unrelated milestones.

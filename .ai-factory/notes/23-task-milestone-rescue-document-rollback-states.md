# Task Spec — milestone-rescue: document the closed set of valid sidecar `step` rollback states

**Date:** 2026-06-23
**Roadmap:** ROADMAP.md Milestones
**Provenance:** while rescuing a `mind` milestone, the operator had to roll the sidecar back to plan-review on a *corrected-in-place* plan and found no documented `step` value for it — `"planned"` had to be inferred from the orchestrator source and convention.

## Current state

`milestone-rescue/SKILL.md` Step 5 ("Apply and clean up") only documents **two** sidecar outcomes:

- **Full reset** (plan `.md` deleted) → delete the `.json` sidecar too.
- **Re-implement** (plan + passing plan-reviews kept, reviews/patches deleted) → keep the sidecar, write `step: "plan_reviewed"`.

The "Re-implement" sub-section's `step` table has exactly two rows and **both write `"plan_reviewed"`**. Nowhere does the skill enumerate the full set of `step` values the orchestrator actually accepts, nor what phase each one resumes from, nor which artifact each requires on disk to be trusted.

The orchestrator's resume detector (`orchestrator/main.py` — `_validate_sidecar_step()` and `_detect_milestone_step()`) recognizes a **closed set of five** `step` values (implement mode):

| `step` value | Resumes at | Required on disk to validate |
|---|---|---|
| `"planned"` | plan-review, attempt 1 | none — always valid |
| `"plan_review_failed:N"` | plan, attempt N+1 | `plan-reviews/{seq}-{slug}-plan-review-N.md` |
| `"plan_reviewed"` | implement, iter 1 | a plan-review file ending with `PLAN_REVIEW_PASS` |
| `"implemented"` | review, iter 1 | none — always valid |
| `"review_failed:N"` | implement, iter N+1 | `reviews/{seq}-{slug}-review-N.md` |

(Test mode swaps `review_failed:N` for `test_run_failed:N` → `test-runs/{seq}-{slug}-test-N.txt`.) An unrecognized or artifact-missing value is cleared and execution falls through to the disk heuristic — so a wrong `step` is not catastrophic, but it **silently loses the intended resume point** and can re-run the planner from scratch.

The gap that bit us: a rescue can legitimately **correct the plan `.md` in place** (fold reviewer findings into it) and want plan-review to re-run on the corrected plan **without re-planning from scratch**. The correct `step` for that is `"planned"` — but the skill has no row for it. The value had to be inferred from `_detect_milestone_step` (`main.py:197`) and the past-tense-phase-completion naming convention. That guess-from-convention is exactly what this task removes.

## Target

Doc-only change to `milestone-rescue/SKILL.md` Step 5 — no orchestrator code touched.

### Change A — add a "Valid sidecar `step` states" reference

Add a closed-set reference table to Step 5 mirroring the orchestrator's `_validate_sidecar_step()`: for each of the five `step` values, the phase it resumes from and the artifact that must exist on disk for it to validate. State explicitly that this is a **closed set** — Step 5 picks a value from it, never invents one — and that the orchestrator clears any value whose required artifact is missing (falling through to the heuristic), so writing the wrong value silently loses the intended resume.

### Change B — document the missing "plan corrected → re-plan-review" rollback

Add the third legitimate rescue outcome alongside full-reset and re-implement:

- **Re-plan-review (plan corrected in place)** — the plan `.md` is kept (edited), plan-reviews are deleted (they reviewed the old plan), any reviews/patches deleted. Keep the sidecar and write `step: "planned"`, preserving `planner`/`implementer`/`elapsed`. The orchestrator then re-runs plan-review against the corrected plan without re-planning.

Reconcile it with the existing two outcomes so the three are presented as the complete set of Step 5 sidecar dispositions.

## Guards

- **Source of truth is the orchestrator**, not the skill: the table must mirror `_validate_sidecar_step()` / `_detect_milestone_step()` in `orchestrator/main.py`. Note in the skill that if the orchestrator's accepted set changes, this table is the thing to update — do not let them silently diverge.
- **`"planned"` and `"implemented"` carry no artifact reference and always validate** — so they are only *safe* to write when the corresponding earlier-phase artifacts actually exist (plan `.md` present for `"planned"`; plan present + non-empty working diff for `"implemented"`). The skill must state this precondition, or an operator could write `"planned"` after deleting the plan — the exact contradiction note 15 fixed.
- Keep Step 5's existing flow intact — this **adds** a reference table and one outcome row; it does not rewrite the cleanup logic. The two documented outcomes stay.
- `milestone-rescue` is a custom / never-overwrite-from-upstream skill (CLAUDE.md "Custom skills") — safe to edit directly, no divergence registration needed.

## Files

- `src/skills/milestone-rescue/SKILL.md` (modify) — Step 5: add the valid-`step`-states reference table (Change A) and the "plan corrected → `step: planned`" rollback outcome (Change B).

## Verify

- Step 5 contains a reference listing all five `step` values, each with its resume phase and required-on-disk artifact, matching `orchestrator/main.py`.
- The skill documents the "plan corrected in place → keep plan + sidecar, delete plan-reviews, write `step: "planned"`" rollback as a first-class outcome.
- A rescue operator can pick the correct `step` for a corrected-plan re-plan-review from the skill alone, without reading orchestrator source.
- The `"planned"`/`"implemented"` always-valid caveat (precondition: earlier artifacts must exist) appears in the guards.

# Plan: milestone-rescue — document the closed set of valid sidecar `step` rollback states

## Context
Make `milestone-rescue/SKILL.md` Step 5 self-sufficient for choosing a sidecar `step` value: add a closed-set reference table mirroring the orchestrator and document the missing "plan corrected in place → re-run plan-review" rollback outcome, so a rescue operator never has to infer a `step` from orchestrator source.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Documentation update

- [x] **Task 1: Add the "Valid sidecar `step` states" reference table to Step 5 (Change A)**
  Files: `src/skills/milestone-rescue/SKILL.md`
  Insert a new reference subsection inside Step 5 ("Apply and clean up"), placed before the per-outcome cleanup detail (logical spot: right after the line `The set of files to delete depends on the failure mode from Step 2:` block, or as a dedicated subsection just before "Update or delete the sidecar"). Add a closed-set table enumerating all five `step` values the orchestrator's `_validate_sidecar_step()` / `_detect_milestone_step()` accept in implement mode, mirroring the spec note exactly:
  | `step` value | Resumes at | Required on disk to validate |
  |---|---|---|
  | `"planned"` | plan-review, attempt 1 | none — always valid |
  | `"plan_review_failed:N"` | plan, attempt N+1 | `plan-reviews/{seq}-{slug}-plan-review-N.md` |
  | `"plan_reviewed"` | implement, iter 1 | a plan-review file ending with `PLAN_REVIEW_PASS` |
  | `"implemented"` | review, iter 1 | none — always valid |
  | `"review_failed:N"` | implement, iter N+1 | `reviews/{seq}-{slug}-review-N.md` |
  State explicitly that: (1) this is a **closed set** — Step 5 picks a value from it, never invents one; (2) the orchestrator clears any value whose required artifact is missing and falls through to the disk heuristic, so writing a wrong value silently loses the intended resume point and can re-run the planner from scratch. Add the test-mode note: test mode swaps `review_failed:N` for `test_run_failed:N` (artifact `test-runs/{seq}-{slug}-test-N.txt`). Add a one-line source-of-truth caveat: this table mirrors `_validate_sidecar_step()` / `_detect_milestone_step()` in `orchestrator/main.py` — if the orchestrator's accepted set changes, update this table; do not let them diverge.

- [x] **Task 2: Document the "Re-plan-review (plan corrected in place)" outcome and reconcile the three outcomes (Change B)** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Add the third legitimate Step 5 sidecar disposition alongside the existing **Full reset** and **Re-implement** outcomes, presenting the three together as the complete set:
  - **Re-plan-review (plan corrected in place)** — the plan `.md` is kept (edited to fold in reviewer findings), plan-review files are deleted (they reviewed the old plan), any review/patch files deleted. Keep the `.json` sidecar and write `step: "planned"`, preserving `planner`/`implementer`/`elapsed`. The orchestrator then re-runs plan-review against the corrected plan without re-planning from scratch.
  Update the existing sidecar-`step` decision table (currently two rows both writing `"plan_reviewed"`) so it covers all three dispositions distinctly — add a row for the corrected-plan case writing `"planned"`. Update the artifact-cleanup narrative in Step 5 so it acknowledges the corrected-plan path deletes plan-reviews while keeping the plan `.md`. Generalize the trailing `Emit:` message so it reflects whichever `step` was written (not hardcoded `"plan_reviewed"`). Keep the existing two outcomes and the overall cleanup flow intact — this adds a row/outcome, it does not rewrite the logic.

- [x] **Task 3: Add the always-valid precondition guard for `"planned"` / `"implemented"`** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Add a guard (in or near the new reference table from Task 1, and reinforced in the "What NOT to do" section if appropriate) stating that `"planned"` and `"implemented"` carry no artifact reference and **always validate** — so they are only safe to write when the corresponding earlier-phase artifacts actually exist on disk: plan `.md` present for `"planned"`; plan present plus a non-empty working diff for `"implemented"`. Explicitly call out the failure mode this prevents: an operator must never write `"planned"` after deleting the plan `.md`. Ensure this is consistent with the existing "Do not overwrite `planner`/`implementer`/`elapsed`" guidance and the full-reset-deletes-sidecar rule.

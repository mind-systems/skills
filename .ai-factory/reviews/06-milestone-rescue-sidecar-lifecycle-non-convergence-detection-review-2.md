# Code Review (round 2): milestone-rescue sidecar lifecycle + non-convergence detection

**Plan:** `06-milestone-rescue-sidecar-lifecycle-non-convergence-detection.md`
**Changed file:** `.claude/skills/milestone-rescue/SKILL.md` (instruction text — "bugs" = logical contradictions / undefined control flow that would mislead an agent following the skill)
**Spec note:** `.ai-factory/notes/15-task-milestone-rescue-full-reset-deletes-sidecar.md`

## What was verified

- `git status` / `git diff HEAD` reviewed; only `SKILL.md` is a code change. Blob changed since review-1 (`2701d9a` → `54f4fed`), confirming the round-1 findings were addressed.
- Read `SKILL.md` in full and re-checked all three review-1 findings plus a fresh independent pass against the spec note's Verify/Guards.

## Round-1 findings — all resolved

1. **(was Medium) Non-convergence + "Re-run anyway" (option 2) had undefined Step 5 behavior** — now explicitly handled (lines 231–236): skip the `$TARGET_FILE` edit and follow the implement-phase (re-implement) cleanup path — keep plan `.md` + passing plan-reviews, delete reviews/patches, set sidecar `step` to `"plan_reviewed"`, then Step 5.5. The undefined fall-through is closed. ✓
2. **(was Low) Option 3 "milestone spec" wording** — disambiguated (lines 156–159) to the **spec note file** (`.ai-factory/notes/<NN>-….md`), explicitly *"not the ROADMAP milestone line,"* and now states the clause is applied to that file before proceeding as option 1. The self-contradiction with the branch's "do not propose a milestone-description change" premise is gone. ✓
3. **(was Informational) Unreachable `step` table row** — the "reviews exist but none pass" row was removed; the table (lines 290–293) keeps only the two reachable rows, both yielding `"plan_reviewed"`. ✓

## Fresh pass against spec note

- Full reset → delete all four artifact types **and** the sidecar via git-native commands (lines 256–258, 274–279); `planner`/`implementer`/`elapsed` loss called out as intentional — Verify #60 ✓
- Implement-phase → keep plan `.md` + `PLAN_REVIEW_PASS` plan-reviews, delete only reviews/patches, sidecar `step="plan_reviewed"` with other keys preserved (lines 260–262, 292, 298–300) — Verify #61 ✓
- Non-convergence is high-bar (all three conditions; any Blocking/Critical or absent deliverable → standard flow) and recommends commit with no description change — Guard line 49, Verify #63 ✓
- git-native deletion only; sidecar deleted iff plan `.md` deleted; rule-of-thumb encoded verbatim (line 269) — Guards honored ✓
- Step 5 control flow is total: both non-convergence sub-branches short-circuit to Step 5.5 before the defect-flow entry at line 238; defect flows reach apply-then-cleanup. No undefined path remains.

## Verdict

All round-1 findings are resolved and no new correctness, consistency, or control-flow problems were found. The implementation is faithful to the plan and the spec note across every branch.

REVIEW_PASS

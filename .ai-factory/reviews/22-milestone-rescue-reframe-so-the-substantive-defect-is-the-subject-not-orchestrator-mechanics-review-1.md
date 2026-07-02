# Code Review: milestone-rescue reframe (round 1)

## Scope
The only product/code change in this diff is `src/skills/milestone-rescue/SKILL.md`. The other modified/added files (`.ai-factory/ROADMAP.md`, the spec note, plan `.json`/`.md`, plan-review) are AI-factory bookkeeping artifacts, not runtime code, and are out of scope for a correctness review. Reviewed the full SKILL.md against the spec note (`.ai-factory/notes/33-…`) and the plan.

## What the change does
A framing/output reframe of the skill — six surgical edits — so the substantive spec/contract defect becomes the first-class subject and orchestrator mechanics become internal routing signals. No procedural logic was altered.

## Guard verification (all pass)
- **≤ 500 lines:** file is 354 lines. ✓
- **Frontmatter unchanged (lines 1–13):** no diff in that region. ✓
- **Sidecar `step` closed-set table + contract text (lines 273–292):** untouched. ✓
- **All `git` commands (`git clean -f`, `git rm -f`, `git status --short`):** untouched. ✓
- **Classification logic + PASS-marker detection (Step 2):** identical; only the framing sentence added and the "state the diagnosis" ordering changed. ✓

## Correctness checks
- **Step 2 relabel (lines 63–65):** additive framing only; the plan-phase / implement-phase / non-convergence conditions and their `PLAN_REVIEW_PASS` / `REVIEW_PASS` predicates are byte-for-byte preserved. Behavior-identical. ✓
- **Step 2 diagnosis reorder (lines 85–87):** reordering of a human-facing statement; no control-flow impact. ✓
- **Step 3 Diagnosis Report (lines 111–137):** conforms to the spec — chronological prose, no tables/fragment lists, domain-language only with zero orchestrator vocabulary, ends with a visually set-off standalone root-cause sentence, and keeps the root-cause categories attached as a classification rather than replacing the narrative. ✓
- **Step 4 non-convergence template (lines 152–166):** leads with substance, mentions the missing `REVIEW_PASS` in a single subordinate clause, and preserves the three options and Option-3 spec-note behavior unchanged. ✓
- **Step 5 restatement (lines 294–295):** placed immediately before the "Show the user the list of deleted files" closing line, after the sidecar table, so the substantive summary precedes file bookkeeping. It sits on the real-defect path; the non-convergence path branches to Step 5.5 at line 222 before reaching it, so there is no conflict with the "no rollback / no repair" semantics of non-convergence. ✓
- **"What NOT to do" ban (lines 351–354):** correctly scopes the constraint to output/reporting and explicitly preserves internal reading of pipeline signals for routing — consistent with the Step 2 relabel. ✓

## Observation (non-blocking, no change required)
The Diagnosis Report in Step 3 is described as "mandatory," and its trigger is "Before presenting the Step 4 depth menu." The depth menu is shown only on the real-defect branch (Step 4, lines 185–199); the non-convergence branch presents a different `AskUserQuestion` (lines 152–166), not a "depth menu." Read literally, the trigger phrasing therefore scopes the report to real-defect classifications — which is the correct behavior, since a non-convergence case has no defect chain to narrate and no root-cause category to attach. This reading is sound as written; a future edit could make the scoping explicit for extra clarity, but it is not a defect.

## Verdict
No correctness, security, or guard-violation issues. The reframe is faithful to the spec, all behavior-identical guarantees hold, and the file stays well within the line budget.

REVIEW_PASS

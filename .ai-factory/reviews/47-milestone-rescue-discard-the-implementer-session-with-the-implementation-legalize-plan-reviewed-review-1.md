# Review 1 — milestone-rescue: discard the implementer session; legalize `plan_reviewed`

**Scope:** `src/skills/milestone-rescue/SKILL.md` (the only code/instruction change in the diff). The three `.ai-factory/` files (plan `.md`, plan-review, sidecar `.json`) are this task's own pipeline artifacts, not the change under review.

This is an agent-instruction file, not executable code — there is no runtime, migration, type surface, or concurrency to break. Correctness here means: internal consistency of the instructions, faithfulness to the spec (`.ai-factory/specs/02-milestone-rescue-stale-implementer-session.md`), and no contradiction with the orchestrator contract the skill mirrors.

## Verification against spec

All four spec requirements are implemented correctly:

- **Edit 1 (spec+plan drops `implementer`):** Step 5 "Depth: spec + plan" now sets `step: "planned"` and deletes `implementer`, preserving `planner`/`elapsed` (lines 300–307). ✓
- **What-NOT-to-do carve-out:** the preserve bullet (lines 428–434) now states `planner`/`elapsed` persist everywhere, `implementer` is deleted whenever the repair discards the implementation, and explicitly rejects keeping it "for the elapsed stats." Matches spec's three "What NOT to do" points. ✓
- **Edit 2 (new `plan_reviewed` rollback):** added as menu option 4 (lines 242–250) and as a dedicated Step 5 depth block (lines 327–344) — keeps plan + plan-reviews, deletes reviews/patches, sets `step: "plan_reviewed"`, drops `implementer`, and restates the `PLAN_REVIEW_PASS`-on-disk validation contract inline. ✓
- **Diagnosis recognition:** the byte-identical-to-HEAD signal is added to Step 2 (lines 86–92), Step 3's category list (lines 126–128), the Diagnosis Report guidance (lines 157–160), and the classification attach line (lines 170–173). ✓
- **Table note amended:** the trailing note (lines 367–372) now says `"plan_reviewed"` **is** written by this skill in exactly this rollback, gated on a `PLAN_REVIEW_PASS` file; other reference-only values unchanged. ✓
- **Table values unchanged / no orchestrator changes:** the closed-set table (lines 355–361) and its "five values" framing are untouched; no `main.py` edits. ✓

## Consistency checks (no defect found)

- **Menu numbering collision:** the non-convergence menu (Step 4, options 1–3) and the real-defect menu (now options 1–4) are separate `AskUserQuestion` presentations, and Step 5's non-convergence block's "(options 1, 2, or 3)" refers only to the non-convergence menu. No cross-wiring. ✓
- **Classification overlap (stale-implementer vs. non-convergence):** mutually exclusive — non-convergence requires deliverables present on disk with only Low/Info findings; stale-implementer requires the product byte-identical to HEAD (blocking "implementation absent" findings). Step 2 lists stale-implementer before non-convergence, so the diff-empty case routes correctly. ✓
- **Every real-defect menu option maps to a Step 5 block:** options 1–4 → spec / spec+plan / spec+plan+code / plan-ratified. Complete. ✓
- **`plan_reviewed` resume point:** table says "implement, iter 1"; dropping `implementer` yields a fresh session — matches the spec's intent (orchestrator resumes at implement iteration 1). ✓

## Findings

### 1. (Low) Frontmatter `description` still lists only three repair depths

`description` (line 5) reads `repairs to that depth (spec / spec+plan / spec+plan+code)` and does not mention the new plan-ratified (`plan_reviewed`) rollback that this change adds. This is a summary-completeness nit, not a defect: the trigger phrases ("rescue", "milestone failed", "pipeline stopped") still route the stale-implementer case into the skill, so invocation is unaffected. The spec deliberately scoped the edits to the body, so leaving the description untouched is defensible — flagging only so the discrepancy is a conscious choice rather than an oversight. Non-blocking.

## Conclusion

The change is faithful to the spec, internally consistent, and introduces no correctness or contract-mismatch defect. The single finding is a cosmetic summary omission that does not affect behavior. No blocking issues.

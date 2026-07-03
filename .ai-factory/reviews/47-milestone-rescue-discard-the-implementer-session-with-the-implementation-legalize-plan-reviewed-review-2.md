# Review 2 — milestone-rescue: discard the implementer session; legalize `plan_reviewed`

**Scope:** `src/skills/milestone-rescue/SKILL.md` — the only code/instruction change. The four `.ai-factory/` files (plan `.md`, plan-review, sidecar `.json`, review-1) are this task's own pipeline artifacts, not the change under review.

This is an agent-instruction file, not executable code: no runtime, migration, type surface, or concurrency exists to break. Correctness here = internal consistency, faithfulness to the spec (`.ai-factory/specs/02-milestone-rescue-stale-implementer-session.md`), and no contradiction with the orchestrator contract the skill mirrors.

## Verification against spec

All requirements implemented correctly:

- **Edit 1 — spec+plan drops `implementer`:** Step 5 "Depth: spec + plan" sets `step: "planned"` and deletes `implementer`, preserving `planner`/`elapsed` (lines 301–306); emit line updated. ✓
- **What-NOT-to-do carve-out:** preserve bullet (lines 429–435) states `planner`/`elapsed` persist at every depth, `implementer` is the one exception (deleted at spec+plan and plan-ratified depths), and explicitly rejects keeping it "for the elapsed stats." Matches all three spec "What NOT to do" points. ✓
- **Edit 2 — new `plan_reviewed` rollback:** menu option 4 (lines 243–246) and dedicated Step 5 block (lines 328–345) — keeps plan + plan-reviews, deletes reviews/patches, sets `step: "plan_reviewed"`, drops `implementer`, restates the `PLAN_REVIEW_PASS`-on-disk validation contract inline. ✓
- **Diagnosis recognition:** byte-identical-to-HEAD signal added to Step 2 (lines 87–93), Step 3 category list (lines 127–129), Diagnosis Report guidance (lines 158–161), and the classification attach line (lines 171–172). ✓
- **Table note amended:** trailing note (lines 368–373) now states `"plan_reviewed"` **is** written in exactly this rollback, gated on a `PLAN_REVIEW_PASS` file; other reference-only values unchanged. ✓
- **Table values / orchestrator unchanged:** closed-set table (lines 356–362) and its "five values" framing untouched; no `main.py` change. ✓
- **Frontmatter description:** updated to list the fourth depth `plan-ratified-implementation-absent` (line 6) — valid folded-scalar YAML, under the 1024-char limit. ✓

## Consistency checks (no defect found)

- **Menu numbering:** the non-convergence menu (options 1–3) and the real-defect menu (options 1–4) are separate `AskUserQuestion` presentations; Step 5's non-convergence "(options 1, 2, or 3)" refers only to the non-convergence menu. No cross-wiring.
- **Classification overlap (stale-implementer vs. non-convergence):** mutually exclusive — a product byte-identical to HEAD implies deliverables absent and blocking "implementation absent" findings, whereas non-convergence requires deliverables present with only Low/Info findings. Step 2 lists stale-implementer first, so a diff-empty case routes deterministically to the plan-ratified rollback.
- **`plan_reviewed` resume/artifact contract:** table says "implement, iter 1" requiring a `PLAN_REVIEW_PASS` plan-review; the rollback keeps plan-reviews and restates the gate, so the always-valid/silent-failure guards are respected. Dropping `implementer` yields the fresh session the spec intends.
- **Every real-defect option maps to a Step 5 block:** options 1–4 → spec / spec+plan / spec+plan+code / plan-ratified. Complete.

## Conclusion

The change is faithful to the spec, internally consistent, and introduces no correctness, contract-mismatch, or security defect. The review-1 finding (frontmatter description omitted the fourth depth) is now resolved.

REVIEW_PASS

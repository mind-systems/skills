# Plan Review 2: milestone-rescue — repair by depth, roll back to the repaired state

**Plan:** `.ai-factory/plans/15-milestone-rescue-refactor-repair-by-depth-roll-back-to-the-repaired-state.md`
**Target:** `src/skills/milestone-rescue/SKILL.md` (single file, + one CLAUDE.md verification touch)
**Risk Level:** 🟢 Low

## Verification performed

- Re-read the plan, the current `SKILL.md` (400 lines on disk; plan says ~401 — within tolerance), and plan-review-1.
- **All three plan-review-1 findings are now resolved in the revised plan:**
  1. *`$TARGET_FILE` resolution risks deletion* → now a dedicated **Constraint** (line 26, "`$TARGET_FILE` resolution is load-bearing — preserve it") **and** an explicit preservation note inside Task 5 ("Preserve the `$TARGET_FILE` resolution (current lines ~130–135) — it is NOT part of the templates being removed"), feeding both Task 6's contract-line edit and Task 7's Step 5.5. ✅
  2. *Non-convergence commit has no apply home* → now a **Constraint** (line 27, "Non-convergence is a fourth, terminal outcome — commit-as-is, no rollback") and an explicit bullet in Task 6 stating no cleanup / no sidecar change. ✅
  3. *`"plan_reviewed"` write retired* → now a **Constraint** (line 28) spelling out that the new flow only writes `"planned"` / `"implemented"` / deletes the sidecar, and keeps the 5-row table only as the orchestrator-contract reference. ✅
- **Line references re-confirmed accurate** against the live file: intro 16–24, non-convergence 67–90, issue-extraction 95–125, Step 4 templates 128–219, `$TARGET_FILE` 130–135, non-convergence apply 225–229, sidecar prose 289–302.
- **Cross-references confirmed:** `roadmap-decompose` skill exists (`src/skills/roadmap-decompose`); `milestone-rescue-audit/SKILL.md` line 31 points at `milestone-rescue` "for the artifact layout and directory structure" (validates the Step‑1 precision-floor block); CLAUDE.md line 104 already lists `milestone-rescue` under "never overwrite from upstream" (Task 8's "confirm, add only if missing" is correct).
- **Depth → sidecar `step` mapping is consistent with the always-valid guard:** spec+plan+code repairs code by hand in the working tree, so a non-empty diff exists when `"implemented"` is written — satisfying the existing precondition ("write `\"implemented\"` only when plan `.md` is present and a non-empty working diff exists"). No contradiction introduced.

## Critical Issues

None. The plan is implementable as written.

## Findings (recommended)

### 1. Stale `docs/overview.md` will contradict the refactored SKILL.md — Medium (scope decision)
The skill package ships `src/skills/milestone-rescue/docs/overview.md` (167 lines). It documents the **old** model end to end and will be left wholly inconsistent after this refactor:
- "translates it into a concrete proposal: update the milestone description in ROADMAP.md … Or … decompose it" (lines 13–16) — the exact framing Task 1/2 retire.
- It reproduces the **three Step 4 templates** (update / decompose, lines 91–127) that Task 5 deletes.
- Its sidecar section (lines 149–154) points the reader to "the mapping table in SKILL.md Step 5" and the old `plan_reviewed` write path — which Task 6 reorganizes around the three depths.

The plan's `Settings: Docs: no` and the "One file only" constraint deliberately scope this out, so this is **not a blocking defect** — but it leaves a shipped doc that directly contradicts the new behavior, which conflicts with the repo's "describe current state only" doc principle and the meta-repo premise that skills are the product. Plan-review-1 did not flag this.

**Recommendation:** either (a) add a short task to update or delete `docs/overview.md` (it is a different file, but the omission is the kind of thing the "Final consistency pass" in Task 8 should at minimum *note*), or (b) explicitly record in the plan that `overview.md` is knowingly left stale and will be reconciled separately. Option (a) is cleaner given the refactor's whole purpose is removing the old propose/decompose model.

### 2. The second "Situation after cleanup → Write step" decision table is not called out by name — Low
Beyond the prose at lines 289–302 that Task 6 names, the current Step 5 contains a *second* decision table (lines 325–328) that maps "plan corrected in place" → `"planned"` and "plan-reviews exist and pass" → `"plan_reviewed"`. The latter row is exactly the retired write. Task 6's "merge into one apply section keyed by the three depths" subsumes it, and the line‑28 constraint makes the intent unambiguous, so the implementer will almost certainly replace it — but the plan never points at lines 325–328 explicitly the way it does for the 289–302 prose.

**Recommendation:** add half a sentence to Task 6 noting the old "Situation after cleanup" sub-table (lines ~325–328, including its `"plan_reviewed"` write) is replaced by the depth-keyed mapping. Low impact; prevents an orphaned table surviving the merge.

## Positive Notes

- The revision is a clean, surgical response to plan-review-1: each of the three findings became a named Constraint **and** an inline task note, rather than a vague acknowledgment — exactly the redundancy the precision-floor philosophy calls for.
- The four precision-floor blocks (per-variant deleted-file set with git-native commands, the 5-row `step` table mirroring `orchestrator/main.py`, the "only touch `step`" rule, the Step‑1 discovery block) are protected in both the Constraints header and Tasks 6/8.
- Depth ordering (spec → spec+plan → spec+plan+code) and the "spec tier may already be fine, only plan/code touched" clause correctly model cumulative-from-spec repair without inventing a spurious "plan-only" or "code-only" depth.
- Commit grouping is dependency-ordered and leaves each intermediate state coherent.

## Verdict

The plan resolves every plan-review-1 finding and is solid. The two findings here are non-blocking refinements: finding 1 (stale `docs/overview.md`) is a genuine completeness gap the prior review missed and is worth closing, but it is a deliberate scope decision the author may accept; finding 2 is a minor robustness note for the Step 4/5 merge. Neither prevents implementation.

PLAN_REVIEW_PASS

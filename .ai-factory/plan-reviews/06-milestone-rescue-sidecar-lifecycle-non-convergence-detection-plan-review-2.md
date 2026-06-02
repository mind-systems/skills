# Plan Review 2: milestone-rescue sidecar lifecycle + non-convergence detection

**Plan:** `06-milestone-rescue-sidecar-lifecycle-non-convergence-detection.md`
**Target file:** `.claude/skills/milestone-rescue/SKILL.md`
**Spec note:** `.ai-factory/notes/15-task-milestone-rescue-full-reset-deletes-sidecar.md`
**Prior review:** `...-plan-review-1.md` (5 issues: #1 Critical, #2/#3 Medium, #4/#5 Minor)
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): present — WARN/none. Single-skill text edit, no boundary or dependency-model impact. Aligned with the "skills are runtime instructions, not code" model.
- **Rules** (`.ai-factory/RULES.md`): not present — skipped (WARN, optional file absent).
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS. Milestone `06` is present and open, and its description maps cleanly onto the plan's two changes (A: sidecar lifecycle, B: non-convergence). Spec-note linkage present and correct.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project overrides to apply.

## Verification performed

- Confirmed the real target is `.claude/skills/milestone-rescue/SKILL.md` (the top-level `milestone-rescue/` path is the symlink source; the live file is under `.claude/skills/`). **Plan path correct.**
- Re-cross-checked every line reference against the live file: cleanup block `~185–195` ✓, do-NOT-delete-sidecar hard rule `~193–195` ✓, `step` table `~208–217` ✓, emit text at line `227` ✓, What-NOT-to-do bullet `~280–281` ✓, Step 2 / Step 4 / Step 5 / Step 5.5 locations ✓. **All line references still accurate.**
- Confirmed `allowed-tools` grants `AskUserQuestion` and `Bash(git *)` — every action the plan calls for is within the existing grant. ✓
- Re-read spec note 15 and reconciled the revised plan against its Target / Guards / Verify sections.

## Resolution of plan-review-1 issues

All five prior issues are addressed by this revision:

- **Issue #1 (Critical) — re-implement sidecar path was unreachable because Step 5 deleted the plan `.md` unconditionally.** ✅ Resolved. New **Task 1** splits the Step 5 cleanup into two failure-mode branches *before* sidecar handling: full reset deletes all four artifact types; implement-phase keeps the plan `.md` + passing plan-reviews and deletes only `reviews/`+`patches/`. The "plan `.md` survives" discriminator is now actually producible, so Task 2's re-implement branch is reachable. Matches note Verify #60–61.
- **Issue #2 (Medium) — non-convergence flow would hit Step 5 and delete the artifacts being committed.** ✅ Resolved. New **Task 6** makes Step 5 skip cleanup + sidecar update entirely for an accepted non-convergence commit.
- **Issue #3 (Medium) — Step 5.5 propagation not considered for non-convergence.** ✅ Resolved. **Task 6** adds an explicit no-op sentence for Step 5.5.
- **Issue #4 (Minor) — "file exists" is a weak signal for modify-type deliverables.** ✅ Resolved. **Task 4** condition 3 now requires evidence the deliverable was *produced/modified* (patches/reviews confirming the change landed), not mere presence.
- **Issue #5 (Minor) — Step 2 peeking into severities owned by Step 3.** ✅ Resolved. **Task 4** explicitly scopes the Step 2 check to a lightweight non-blocking/blocking inspection, not a full Step 3 extraction.

## Remaining observations (all non-blocking / advisory)

These are clarifications for the implementer, not gaps that would derail the work.

### A. Precedence of the three-way classification inside Step 5

Step 2 now yields **three** classifications (plan-phase, implement-phase defect, non-convergence), but Task 1 frames the Step 5 cleanup as a **two-way** split (plan-phase vs implement-phase), with the non-convergence no-op layered on later by Task 6. For this to behave correctly, the implementer must place the **non-convergence check first** in Step 5 — otherwise non-convergence falls through into Task 1's "implement-phase / re-implement" branch and deletes `reviews/`+`patches/` before Task 6's skip applies. Task 6's wording ("skip … entirely") implies this, but stating the ordering explicitly ("check non-convergence before the plan-phase/implement-phase branch") would remove the ambiguity.

### B. Full-reset must also suppress sidecar *creation*, not just deletion

The current `step` table (lines 213–217) has a "Sidecar doesn't exist → **create it**" fall-through. On a full reset the desired end state is **no sidecar at all** (so the orchestrator treats the milestone as new). Task 3 does instruct reconciling the "sidecar doesn't exist" row, but the implementer should ensure the reconciled logic does not re-create a sidecar on the full-reset path even when none existed before. This is the one place the old "always create/update a sidecar" assumption could silently survive the edit.

### C. Step 4 non-convergence branch: fallback if the user declines the commit recommendation

Task 5 specifies the recommend-commit `AskUserQuestion` but not what happens if the user rejects it. Task 6's skip is gated on "the user accepted the commit recommendation," which correctly implies a non-accept path exists — but that path is otherwise undefined (presumably: fall back to the standard propose-update flow, in which case Step 5 cleanup *should* run). One sentence naming the decline fallback would close the loop. Minor.

### D. Implement-phase branch: "passing plan-reviews" vs all plan-reviews

Task 1's re-implement branch says keep "the plan `.md` and its passing plan-reviews." Note Verify #61 says keep "the plan + plan-reviews" (unqualified). Either reading is defensible for orchestrator state, but the implementer should pick one consciously; if non-passing earlier-round plan-reviews are deleted while passing ones are kept, that is a reasonable tightening — just make it intentional, not accidental.

## Positive notes

- **All five review-1 issues are addressed with dedicated tasks** rather than hand-waved — the Critical #1 in particular is now a first-class prerequisite (Task 1) the rest of Change A depends on.
- **Dependency ordering is sound** (Task 1 → 2 → 3 → 4 → 5 → 6), mirroring the natural edit order and ensuring the cleanup split lands before the sidecar branching that relies on it.
- **Git-native deletion preserved** for the sidecar too (`git rm -f` / `git clean -f`), consistent with note Guard line 50; plain `rm` explicitly forbidden.
- **`elapsed`/`planner`/`implementer` loss-is-intended** carried verbatim, pre-empting a false-positive "regression" review.
- **Change B remains correctly high-bar** — all three conditions required; any Blocking/Critical or absent deliverable falls back to the standard defect flow (note Guard line 49).
- **Change A's full surface is enumerated** (hard rule + `step` table + emit text + What-NOT-to-do) so the reconciliation leaves no dangling contradictory instruction.

## Verdict

The revision resolves every issue from plan-review-1, including the Critical architectural gap (#1). The remaining observations (A–D) are non-blocking implementation clarifications, not specification gaps — the plan is faithful to the spec note, the target path and line references are accurate, and the task sequencing is correct. The plan is ready to implement.

PLAN_REVIEW_PASS

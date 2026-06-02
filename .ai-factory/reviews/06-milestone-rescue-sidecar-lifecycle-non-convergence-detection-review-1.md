# Code Review: milestone-rescue sidecar lifecycle + non-convergence detection

**Plan:** `06-milestone-rescue-sidecar-lifecycle-non-convergence-detection.md`
**Changed file:** `.claude/skills/milestone-rescue/SKILL.md` (instruction text — "bugs" here = logical contradictions / undefined control flow that would mislead an agent following the skill)
**Spec note:** `.ai-factory/notes/15-task-milestone-rescue-full-reset-deletes-sidecar.md`

## What was verified

- `git status` / `git diff HEAD` reviewed; only `SKILL.md` is a code change (the other staged files are plan/review artifacts).
- Read `SKILL.md` in full against the plan's 6 tasks and the spec note's Target/Guards/Verify.
- **Change A is correct and complete:** Step 5 cleanup is now split by failure mode (Task 1, lines 246–254), sidecar handling branches on plan-`.md` survival (Task 2, lines 261–296), the "do NOT delete the sidecar" hard rule gained the carve-out (lines 256–259), the `step` table dropped the `"planned"` row (lines 282–286), emit text is split into full-reset vs re-implement (lines 271, 296), and the What-NOT-to-do bullet was reconciled (lines 352–354). This realizes note Verify #60–61. The re-implement path is now reachable (the central gap from plan-review-1 Issue #1 is resolved).
- **Change B Step 2 detection** (lines 67–85) faithfully encodes the three high-bar conditions and the "any Blocking/Critical or missing deliverable → standard flow" fallback.
- **Non-convergence Step 5/5.5 skip** (lines 224–228, 304–306) resolves plan-review-1 Issues #2/#3 for the commit path.

## Findings

### 1. (Medium) Non-convergence + "Re-run the pipeline anyway" (option 2) has undefined Step 5 behavior

Step 4's non-convergence template offers three options (lines 150–153). The Step 5 skip block only covers **option 1 or 3** (line 224–225: *"the user accepted option 1 or 3 … skip the artifact cleanup and the sidecar update"*). **Option 2 (re-run) falls through into normal Step 5**, which then:

- begins with *"Apply the confirmed change to `$TARGET_FILE`"* (line 230) — but for non-convergence no description change was ever proposed, so there is nothing to apply; and
- reaches the cleanup block whose deletion set *"depends on the failure mode from Step 2"* (line 246) — yet only **Plan-phase** and **Implement-phase** branches are listed (lines 248–254). **Non-convergence is a third, distinct classification** (Step 2 says *"classify as non-convergence … instead"*), so neither branch matches and the agent has no instruction for which files to delete or how to handle the sidecar.

Result: the re-run path is undefined. The natural intent is that re-running should behave like the **re-implement** path (keep the good plan + passing plan-reviews, delete reviews/patches so the reviewer starts fresh, update sidecar `step` to `"plan_reviewed"`). The skill should say so explicitly — e.g. "for non-convergence + option 2, follow the implement-phase (re-implement) cleanup path."

### 2. (Low) Option 3 wording risks contradicting the branch's own premise and diverges from the spec note

The non-convergence branch opens with *"do not propose a milestone-description change"* (line 137). Option 3 (lines 153, 156–158) tells the agent to *"scan the review findings for nits that reference a gap in the milestone spec … propose the minimal clause addition."* "Milestone spec" is ambiguous: read as the **ROADMAP milestone line**, it directly contradicts line 137; the spec note (note line 42) actually says fold nits back into *"the spec note"* — i.e. the `.ai-factory/notes/<NN>-…md` file, not the roadmap description. Recommend disambiguating to "the spec **note** file" to match the note and avoid the self-contradiction.

Secondary ambiguity: option 3 says "propose the minimal clause addition, then proceed as option 1," but the Step 5 skip block (for options 1 **and** 3) skips straight to Step 5.5 — so where/when the clause edit is actually written is unspecified. Clarify that the option-3 edit is applied (to the spec note) before the commit, distinct from the skipped artifact cleanup.

### 3. (Informational) `step` table row 2 is unreachable after re-implement cleanup

The table (lines 282–286) keeps the row *"Plan-reviews pass, reviews exist but none pass → `plan_reviewed` (re-implement)."* But the re-implement cleanup deletes **all** review files for the slug (line 253: *"Delete only the review files and patch files"*), so "reviews exist" can never hold *after cleanup* (the table's stated frame: "Situation after cleanup"). Harmless since both reachable rows yield `"plan_reviewed"`, but the row description is now misleading — consider dropping it or rewording.

## Summary

Change A is fully and correctly implemented; the primary Change B happy path (detect → recommend commit → skip cleanup) is correct. The findings are confined to secondary branches: an undefined control-flow path for non-convergence + re-run (Medium), and two wording/consistency issues (Low/Informational). None affect the recommended commit path, but Finding #1 leaves a real gap an agent could stumble into.

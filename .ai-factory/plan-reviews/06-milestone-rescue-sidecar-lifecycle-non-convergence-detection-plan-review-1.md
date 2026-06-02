# Plan Review: milestone-rescue sidecar lifecycle + non-convergence detection

**Plan:** `06-milestone-rescue-sidecar-lifecycle-non-convergence-detection.md`
**Target file:** `.claude/skills/milestone-rescue/SKILL.md`
**Spec note:** `.ai-factory/notes/15-task-milestone-rescue-full-reset-deletes-sidecar.md`
**Risk Level:** 🟡 Medium

## Context Gates

- **Architecture** (`ARCHITECTURE.md`): WARN — none. The change edits a single existing skill body; no boundary or dependency-model impact. Aligned with the "skills are runtime text instructions, not code dependencies" model.
- **Rules** (`RULES.md`): not present — skipped (WARN, optional file absent).
- **Roadmap** (`ROADMAP.md`): PASS — milestone `06` is present and open (`- [ ] milestone-rescue: sidecar lifecycle + non-convergence detection`), and its description matches the plan's two changes (A: sidecar lifecycle, B: non-convergence). Spec-note linkage present. Good linkage.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project overrides to apply.

## Verification performed

- Confirmed the real target file is `.claude/skills/milestone-rescue/SKILL.md` (the top-level `milestone-rescue/` path does not exist in this repo). **Plan path is correct.**
- Cross-checked every line reference in the plan against the actual file: `~193–195` (do-NOT-delete sidecar rule) ✓, `~208–217` (step table) ✓, `~280–281` (What NOT to do bullet) ✓, emit text `Sidecar updated: step set to...` at line 227 ✓, Step 2 / Step 4 locations ✓. **All line references are accurate.**
- Confirmed `allowed-tools` already grants `AskUserQuestion` and `Bash(git *)` — Task 4's `AskUserQuestion` use and the git-native deletion are within the skill's existing tool grant. ✓
- Read the spec note (15) in full and reconciled the plan against its Target/Guards/Verify sections.

---

## Critical Issues

### 1. Missing prerequisite: Step 5 cleanup never *keeps* the plan `.md`, so the "re-implement" sidecar path is unreachable

This is the central gap. The plan's entire Change A keys the sidecar decision on **"did the plan `.md` survive cleanup"** (Task 1: full reset = "plan `.md` … is deleted in the cleanup step"; re-implement = "plan `.md` and its passing plan-reviews are kept"). But the **current Step 5 cleanup deletes the plan `.md` unconditionally**:

> lines 185–186: *"delete all uncommitted files from `plan-reviews/`, `reviews/`, and `patches/`, **and `.md` files from `plans/`**, that belong to this milestone's slug."*

There is no failure-mode branch anywhere in Step 5. The cleanup always deletes the plan `.md` **and** all plan-reviews. Consequences:

- The discriminator the plan relies on is constant: the plan `.md` is *always* deleted → the **full-reset path always fires** → the skill would **always delete the sidecar**. The "re-implement → keep sidecar, set `step:"plan_reviewed"`" path becomes dead code.
- That directly **violates the spec note's guard** (note line 48): *"In the re-implement path the sidecar must survive with `step: "plan_reviewed"` — deleting it there would lose valid in-flight state."* and Verify #61: an implement-phase failure must *keep the plan + plan-reviews, delete reviews/patches, leave the sidecar with `step:"plan_reviewed"`*.
- The reconciled `step` table from Task 2 stays internally inconsistent: a "plan-reviews exist and pass, reviews deleted → `plan_reviewed`" row is unreachable if cleanup just deleted all plan-reviews.

**Root cause:** the plan jumps to the *last* link of the chain (sidecar handling) and assumes the earlier link (conditional artifact deletion) already exists. It does not. To realize the note's two paths, the cleanup deletion of the **plan `.md` and the passing plan-reviews must itself be made conditional on the Step 2 classification**:

- **Plan-phase failure / full reset** → delete plan `.md` + plan-reviews + reviews + patches + sidecar.
- **Implement-phase failure / re-implement** → keep plan `.md` + passing plan-reviews; delete only `reviews/` + `patches/`; update the sidecar `step` to `"plan_reviewed"`.

**Recommended fix:** add a task (or expand Task 1) that splits the Step 5 **cleanup block (lines 185–195)** by failure mode *before* the sidecar sub-step, so that "the plan `.md` survives" is actually achievable on the re-implement path. As written, the plan implements only half the mechanism. This matches note Verify #60–61 exactly.

---

## Medium Issues

### 2. Non-convergence path does not specify Step 5 behaviour — Step 5 would delete the artifacts you just recommended committing

Change B touches only Step 2 (classify) and Step 4 (recommend commit). After the user accepts the "commit" recommendation in Task 4's `AskUserQuestion`, control still flows into **Step 5 ("Apply and clean up")**, which:

- deletes all `.ai-factory/` artifacts for the slug (plans `.md`, plan-reviews, reviews, patches), and
- updates/derives the sidecar `step` (for a `review_failed:N` state → "reviews exist, none pass" → `"plan_reviewed"`).

For a **non-convergence** classification this is wrong: the milestone is effectively *done*, you are recommending a **commit**, and the plan/reviews document a successful (if unrecognized) attempt. Deleting them and resetting the sidecar to `"plan_reviewed"` contradicts the recommendation. The code deliverable itself is safe (it lives outside `.ai-factory/`, so Step 5 doesn't touch it), but the supporting artifacts and sidecar state would be churned.

**Recommended fix:** add explicit Step 5 handling for the non-convergence classification — e.g. *skip the cleanup + sidecar reset entirely* (or keep the artifacts pending the commit). The plan currently leaves the Step 2 → Step 4 → Step 5 interaction undefined for this new branch.

### 3. Step 5.5 (propagate findings) not considered for the non-convergence branch

Step 5.5 propagates recurring/mechanical issues to other open milestones. In a non-convergence case there are no real defects to propagate (every round was non-blocking). The plan doesn't state that Step 5.5 should no-op here. Likely harmless (no qualifying issues), but worth one explicit sentence so the implementer doesn't surface cosmetic nits to unrelated milestones.

---

## Minor / Nitpick

### 4. "Deliverables exist on disk" is a weak signal for *modify*-type deliverables

Task 3 condition 3 (from note line 40) checks that "the files the plan said to create/modify are present." For `milestone-rescue`-style work the deliverable is almost always an **edit to a pre-existing file** (e.g. a `SKILL.md`), so "the file is present" is trivially true and proves nothing about whether the change landed. The non-blocking-rounds condition compensates in practice, and this is inherited from the spec note rather than introduced by the plan — but consider tightening the wording so the check looks for evidence the deliverable *was actually produced/modified*, not mere file presence. Non-blocking.

### 5. Step 2 vs Step 3 ordering for severity inspection

Task 3 asks Step 2 to test "every review verdict is non-blocking," which requires inspecting review-finding severity — work that Step 3 ("Extract issues") formally performs. This means Step 2 must peek into severities before Step 3 categorizes them. Acceptable (Step 1 already reads every artifact), but the implementer should ensure the wording doesn't imply a full Step-3 extraction inside Step 2.

---

## Positive Notes

- **Correct target path and accurate line references** throughout — rare and verified against the live file.
- **Tasks are well-sequenced** with explicit dependencies (Task 2 → 1, Task 3 → 2, Task 4 → 3) that mirror the natural edit order.
- **Git-native deletion preserved** — the plan explicitly forbids plain `rm` and reuses the existing `git rm -f` / `git clean -f` convention (note Guard line 50). Good fidelity.
- **`elapsed`-loss-is-intended** call-out is carried verbatim from the note, pre-empting a future false-positive "regression" review.
- **Both hard-rule + table + emit-text + What-NOT-to-do are all enumerated** for Change A, so the reconciliation won't leave a dangling contradictory instruction (modulo Issue #1).
- **Change B is correctly gated as high-bar** (all three conditions; any Blocking/Critical → standard flow), faithfully matching note Guard line 49.

---

## Verdict

The plan is well-researched and faithful to the spec note on the parts it covers, but **Issue #1 is a genuine architectural gap**: it specifies sidecar handling that branches on plan-`.md` survival without ever creating the path where the plan `.md` survives, so the re-implement branch is unreachable and the skill would violate the note's own guard. Issue #2 leaves the non-convergence flow's cleanup behaviour undefined. Both should be resolved before implementation.

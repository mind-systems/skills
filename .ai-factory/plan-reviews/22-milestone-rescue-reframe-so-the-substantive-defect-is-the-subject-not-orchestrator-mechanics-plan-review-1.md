## Plan Review Summary

**Plan:** milestone-rescue — reframe so the substantive defect is the subject, not orchestrator mechanics
**Files Reviewed:** 1 target file (`src/skills/milestone-rescue/SKILL.md`) + spec note + ROADMAP entry
**Risk Level:** 🟢 Low

This is a well-scoped, faithful plan. It is a framing/output reframe of a single SKILL.md file, explicitly behavior-identical for artifact discovery, depth routing, rollback, and sidecar logic. It maps 1:1 onto the six edits in the spec note (`.ai-factory/notes/33-milestone-rescue-reframe-substantive-defect.md`) and the ROADMAP contract line. No code, no migrations, no cross-skill contracts touched.

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): No boundary/dependency issue. This is a single-skill content edit with no composition or dependency change (no new skill extraction, no cross-skill invocation). PASS.
- **Rules** (`.ai-factory/RULES.md`): Not present — no rule gate to apply. (WARN: optional file absent, non-blocking.)
- **Roadmap** (`.ai-factory/ROADMAP.md` present): The milestone line at ROADMAP.md:55 matches the plan exactly — tripwire framing, Step 2 relabel, mandatory Diagnosis Report (prose, no tables, domain language, standalone root-cause sentence), non-convergence substance-first, Step 5 restatement, "What NOT to do" ban, and the ≤500-line / sidecar-table / frontmatter guards. Linkage is explicit and correct. PASS.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): Not present — no project-specific review overrides to apply.

### Verification of Codebase Assumptions

All line anchors in the plan were checked against the live file and are accurate:

- Task 1 — opening prose under `# Milestone Rescue`: heading at L15, prose L17–21. ✓
- Task 2 — Step 2 at L59; "State the diagnosis explicitly" at L82. ✓
- Task 3 — Step 3 (Extract root cause) L87–105. ✓
- Task 4 — non-convergence `AskUserQuestion` block L120–133. ✓
- Task 5 — "Show the user the list of deleted files" at L261. ✓
- Task 6 — "What NOT to do" section L299–314. ✓
- Frontmatter is exactly L1–13; the sidecar `step` closed-set table + contract text sit at L240–259, matching the guard. ✓

Current file length is **314 lines**, comfortably under the 500-line ceiling; the additions (mainly the Diagnosis Report spec in Task 3) will not approach it. Task 6 correctly ends with a re-verification of the line count. The "edit in file order to avoid anchor drift" instruction plus "locate by content" in the spec note correctly handles the fact that Task 3's insertion shifts every subsequent anchor.

### Critical Issues

None. Nothing blocks implementation.

### Minor / Non-blocking

- **Non-convergence path × mandatory Diagnosis Report is under-specified.** Task 3 makes the Diagnosis Report a *mandatory* first-class deliverable "printed before the Step 4 depth menu." But the non-convergence classification does **not** route through the depth menu — it goes through the separate `AskUserQuestion` block that Task 4 rewrites, and by definition has no defect chain (all findings Low/Informational, work is done). A "chronological narrative of what defect the review found / what the fix broke" has no subject matter on that path, and would clash with Task 4's "the deliverable is complete and correct" opener. Similarly, Task 5's "restate what was wrong / what was repaired / at which depth" is a no-op for non-convergence (no rollback, no repair). Recommend the implementer scope the mandatory Diagnosis Report (Task 3) and the Step 5 restatement (Task 5) to the **real-defect paths (plan-phase / implement-phase)** and state explicitly that on the non-convergence path the report is omitted (the Task 4 substance-first prose already carries the user-facing summary there). This is a clarity gap, not a logic error — an attentive implementer would likely infer it, but pinning it avoids a forced awkward narrative.

### Positive Notes

- Clean separation of concern: every task edits one file, in file order, with per-task hard guards restated (≤500 lines, frontmatter frozen, sidecar table + git commands untouched, classification/PASS-detection logic unchanged — only relabeled).
- The plan preserves the "behavior-identical" contract from the spec note precisely — it never proposes touching the logic that decides depth or the rollback commands, only the framing and user-facing output.
- Dependencies between tasks are explicitly declared and correctly ordered (each Phase-N task depends on the prior), which matches the anchor-drift concern.
- Root-cause categories are correctly kept and *attached to* the report rather than replaced, matching the spec note's explicit "do not remove the categories" constraint.
- Commit message is a single squashed commit with a descriptive noun phrase, no conventional-commit prefix — consistent with repo conventions.

PLAN_REVIEW_PASS

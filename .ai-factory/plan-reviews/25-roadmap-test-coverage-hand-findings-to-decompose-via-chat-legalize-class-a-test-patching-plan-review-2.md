# Plan Review 2: roadmap-test-coverage — hand findings to decompose; legalize Class-A test patching

**Plan:** `25-roadmap-test-coverage-hand-findings-to-decompose-via-chat-legalize-class-a-test-patching.md`
**Target:** `src/skills/roadmap-test-coverage/SKILL.md` (297 lines)
**Risk Level:** 🟢 Low

## Resolution of Review-1 Findings

Both findings from plan-review-1 are now closed in the plan text:

- **Finding #1 (Class B handoff items may have no note path).** Task 2 now explicitly captures the **source file** path (referencing the existing `Source file` column, line ~247) for each Class B item, and states the rationale — Class B failures can belong to areas dropped in Layer 2 (Full coverage) or Layer 3 (loud-failure) that never produced a Layer-4 note. Task 3 now defines the fallback precisely: attach the Layer-4 note path when the area was researched, otherwise print the captured source file path — "no blank note paths." Fully resolved.
- **Finding #2 (stale frontmatter description).** Task 4 now permits the single `description` tweak ("emits refactor tasks" → collection/handoff wording), scopes it as the only frontmatter edit, and instructs the implementer not to treat "frontmatter unchanged" as a prohibition against correcting the now-inaccurate phrase. Resolved.

## Verification of Assumptions

Re-checked every line reference against the current SKILL.md — all accurate:
- Layer 6 at lines 191–201 ✓ (step 1 writes `## Test Infra` task to `$ROADMAP_PATH` at 195–196; step 2 appends `## Refactor Required` to the Layer-4 note at 197–199)
- Layer 7 Class B write at lines 257–258 ✓ (`## Bugs` phase)
- Layer 7 classification table with `Source file` column at line 247 ✓; Class-A patch instruction ("Keep assertions intact — only update the call signature") at 254–255 ✓
- Layer 8 at lines 264–282 ✓; summary lines 275–277 ✓ ("Refactor tasks added to roadmap: M" / "Existing tests patched (API drift): K" / "Silent bugs escalated to roadmap: J")
- Critical Rule 1 at line 288 ✓
- Frontmatter `description` "emits refactor tasks" at line 7 ✓

Consistency checks:
- `allowed-tools` correctly stays unchanged — `Write` is still required (Layer 6 step 2 note-append and Layer 7 Class-A patches both write), so the tool grant remains valid after roadmap writes are removed.
- Critical Rule 2 ("Never write ROADMAP_TESTS.md") remains accurate and untouched; removing the `$ROADMAP_PATH` writes makes the skill write *neither* roadmap file, which is more consistent with the planning/implementation separation.
- The in-memory handoff list persists across Layers 6→7→8 within a single orchestrated run (these layers execute in the orchestrator itself, not isolated agents), so the collect-then-print flow is sound.
- Line-count constraint (≤ 500) is safe — current file is 297 lines; net change is roughly neutral.

## Context Gates

- **Architecture:** `.ai-factory/ARCHITECTURE.md` present; no rule governs this skill's roadmap-write behavior (only a passing mention of `command-handoff`). No boundary conflict. — PASS
- **Rules:** `.ai-factory/RULES.md` — not present. — WARN (optional file absent)
- **Roadmap:** meta-skill edit; no milestone-linkage expectation for this repo. — N/A
- **Skill-context:** `.ai-factory/skill-context/aif-review/SKILL.md` — not present. No project overrides to apply. — WARN (optional file absent)

## Minor Observations (non-blocking)

- **Durability of Class B items between Layer 7 and Layer 8.** Refactor findings still persist to the Layer-4 note (Task 1 keeps step 2), but Class B handoff items now live only in the in-memory list until Layer 8 prints them. If the run aborts before Layer 8, those items are lost. This is negligible for a single-session, user-present chat skill and does not warrant a design change — noted only for awareness.
- Task 1's "collect and continue" wording lightly rephrases the current "emit and continue" log line; harmless given the layer is being renamed to "Refactor Collect."

## Positive Notes

- The plan folds both prior-review findings directly into the task text rather than leaving them as loose caveats — Task 2/Task 3 now carry the exact fallback rule that closes the ambiguous-note-path gap.
- Task boundaries remain crisp: each task names the exact layer and lines, and enumerates what to leave intact (classification table, agent prompt, Class-A patch text, re-run/all-green requirement).
- Dependencies are correct: Task 3 depends on Task 1+2 (handoff list must exist before Layer 8 prints it); Task 4 depends on Task 2 (Rule 1's rewording must match the Class-A instruction it legalizes).
- Task 4 tightly scopes the legalized exception (existing test, API-drift only, assertions intact, call signature only) and asks to reverify no residual contradiction with Layer 7 and the ≤500-line bound.

## Verdict

The plan is well-structured, its codebase assumptions are accurate, and it fully resolves both findings from plan-review-1. No blocking issues remain.

PLAN_REVIEW_PASS

## Plan Review Summary

**Plan:** Remove stale `/aif-plan`, `/aif-implement`, `/decompose` references from `roadmap-outline` and `roadmap-decompose`
**Files Targeted:** 2 (`src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): No boundary or dependency concern. This is a docs-only reference cleanup inside two existing skills; no module boundaries touched. WARN: none.
- **Rules** (`.ai-factory/RULES.md`): absent — WARN (optional file missing, non-blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md` present): This is a `fix`/cleanup milestone. Linkage is implicit (milestone #26 plan). No blocking issue.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): absent — no project-specific review overrides to apply.

### Verification Performed
Every factual claim in the plan was checked against the actual files:

- **Line numbers — all accurate.**
  - `roadmap-outline` L79: `not a granular task (that's \`/aif-plan\`)` ✓
  - `roadmap-outline` L229: Critical Rule 5, `use \`/aif-plan\` … and \`/aif-implement\`` ✓
  - `roadmap-decompose` L291: Critical Rule 5, same wording ✓
  - `roadmap-decompose` L236: Mode 3 heading `(\`/decompose check\`)` ✓
  - `roadmap-decompose` L240: `tell the user to run \`/decompose\` first` ✓
- **Coverage is complete.** An independent grep for `aif-plan|aif-implement|/decompose` across both files returns exactly the five lines the plan enumerates — no missed occurrences. The plan's "then grep this file for any remaining occurrences" safety step is a correct belt-and-suspenders measure, and there is nothing extra for it to catch.
- **Replacement targets are valid.** `roadmap-decompose` and `roadmap-outline` are live symlinks in `active/skills/`; `aif-plan` and `aif-implement` are absent from the active set — confirming the plan's premise that the referenced pipeline no longer exists. Pointing granular-task references at `/roadmap-decompose` is the correct successor.
- **Rule 5 rephrase aligns with project doctrine.** "implementation is the orchestrator's job (a separate run)" matches the hard constraint in CLAUDE.md ("Planning and implementation are separate processes … the orchestrator implements them").
- **Scope discipline is correct.** Plan explicitly forbids touching `upstream/ai-factory/` and restricts edits to `src/skills/` — consistent with the three-way-split invariant.

### Critical Issues
None.

### Minor Observations (non-blocking)
- **Task 2 "(depends on Task 1)" is cosmetic.** The two tasks edit different files with no data dependency; the ordering note is harmless but not a real constraint. Either task could run first. No action needed.
- **Wording-only guarantee holds.** None of the five edits touches a mode, gate, atomicity rule, or artifact-format contract — they are all prose/parenthetical substitutions. This matches the plan's "no logic changes" claim.
- Single-commit-at-end decision is appropriate (<5 tasks, one concern).

### Positive Notes
- Line-anchored, quote-level precision in each task makes the change unambiguous for the implementer.
- Includes a grep sweep as a safety net beyond the enumerated lines — good defensive planning.
- Correctly distinguishes the two replacement semantics: granular-task pointer → `/roadmap-decompose`, and execution pointer → orchestrator prose (not another slash command).

PLAN_REVIEW_PASS

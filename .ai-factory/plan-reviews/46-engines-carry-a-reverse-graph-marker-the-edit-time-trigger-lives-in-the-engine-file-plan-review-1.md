## Code Review Summary

**Files Reviewed:** plan (4 tasks) against 4 target files + spec + roadmap
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): PASS. The plan operates entirely within the engine/philosophy composition model — it adds an engine-side genre marker completing the "coupling declaration at both ends" rule. No boundary or dependency-direction violation (no `loaded-by:` field, no central map introduced).
- **Rules** (`.ai-factory/RULES.md`): WARN — file absent. No explicit convention file to check against; not blocking.
- **Roadmap** (`.ai-factory/ROADMAP.md` present): PASS. Milestone found at line 103 with an exactly matching title and `Spec: .ai-factory/specs/01-engine-reverse-graph-marker.md`. Plan `# Plan:` heading matches the roadmap line.
- **Spec tree** (`.ai-factory/specs/01-engine-reverse-graph-marker.md`): PASS. All four tasks map directly onto the spec's Edit 1 (marker in three engines) and Edit 2 (CLAUDE.md convention line). Every spec constraint is carried into the plan: declarative-not-imperative, no caller names, no new section, no frontmatter field, `note`'s hooks section undisturbed.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): absent — no project-specific review overrides to apply.

### Critical Issues
None.

### Verified Assumptions (codebase checks)
- **"Three engines named in `loads:` fields today."** Confirmed: `grep "^loads:"` across `src/skills/*` and `src/commands/*` yields exactly three distinct loaded skills — `roadmap-engine`, `test-philosophy`, `note`. The plan's set is complete; no fourth engine is missed.
- **Anchor points exist as described.**
  - Task 1: `roadmap-engine/SKILL.md` — "**Load this skill once per chat**" sentence present at lines 19–21 under the `# Roadmap Engine …` intro. ✓
  - Task 2: `test-philosophy/SKILL.md` — "Load this skill once per chat." present at line 20. ✓
  - Task 3: `note/SKILL.md` — no explicit load-once statement in body; one-line intro at line 19, `## Workflow` at line 21, `### Hooks (caller inputs)` at line 23. The "place marker after intro, before `## Workflow`, do not disturb Hooks" instruction is accurate and the free gap (line 20) exists. ✓
  - Task 4: `CLAUDE.md` — "Dependencies and the skill graph" section present at line 76, with the coupling-declaration rule at line 85 that Task 4 correctly frames the new line as a companion to. ✓
- **Grep literals match the documented convention.** Each task's inline reverse-graph literal (`grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md`) is byte-identical to the reverse-graph form already documented in CLAUDE.md line 81, so the markers will not introduce a competing convention.

### Non-blocking Notes
- The reverse-graph grep for `note` (`grep -l "note" …`) is inherently noisy — "note" is a common substring, so it also matches files that merely mention the word (e.g. "spec note", "notes/") rather than only true `loads: note` callers. This is a property of the pre-existing documented convention, not something this plan introduces, and the spec explicitly requires the marker to reproduce that literal. Out of scope here; flagged only for awareness.
- Tasks are ordered Phase 1 (engine markers) then Phase 2 (convention). No inter-task dependency forces this order, but it is harmless and matches the spec's Edit 1 → Edit 2 sequence.

### Positive Notes
- The plan is a faithful, minimal decomposition of the spec — each task names one file, one anchor, one grep literal, and repeats the declarative-not-imperative guard the spec insists on (preventing a using-agent from eagerly loading callers).
- The declarative-phrasing constraint is correctly propagated to every engine task, honoring the spec's core design intent (the marker loads for every *user* of the engine, so it must contain nothing executable).
- Task 4's framing ("caller side declares whom it loads; engine side declares that it is loaded and how to find by whom") accurately completes the both-ends coupling rule already in CLAUDE.md.

PLAN_REVIEW_PASS

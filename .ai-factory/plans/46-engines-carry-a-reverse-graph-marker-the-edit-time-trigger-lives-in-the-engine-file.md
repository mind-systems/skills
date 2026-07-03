# Plan: Engines carry a reverse-graph marker — the edit-time trigger lives in the engine file

## Context
Each of the three engines named in `loads:` fields today gets a declarative genre marker in its body stating it is a load-once engine whose callers depend on its exact behavior, with the reverse-graph grep inline — so the "grep callers before editing" trigger is present in the engine file itself, the node the edit-time perception tree passes through. CLAUDE.md's convention is extended to make the marker part of the rule.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Engine markers

- [x] **Task 1: Add reverse-graph marker to `roadmap-engine`**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Anchor on the existing load-once statement in the body intro (the "**Load this skill once per chat**" sentence at the end of the paragraph under `# Roadmap Engine — Shared Two-Tier Artifact Format`, lines ~19–21). Add one declarative sentence adjacent to it stating this is a load-once engine whose callers depend on its exact behavior, that edits to this file must honor their expectations as part of its contract, and that the reverse graph is `` grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md ``. Keep it declarative — describe how the reverse graph is *computed*, never phrased as an instruction to run grep ("before editing do X"). No caller names, no new section, no frontmatter field.

- [x] **Task 2: Add reverse-graph marker to `test-philosophy`**
  Files: `src/skills/test-philosophy/SKILL.md`
  Anchor on the existing "Load this skill once per chat." sentence at the end of the intro paragraph under `# Test Philosophy — …` (line ~20). Add one declarative sentence adjacent to it, same shape as Task 1, with the grep literal `` grep -l "test-philosophy" src/skills/*/SKILL.md src/commands/*.md ``. Declarative only, no caller names, no new section, no frontmatter field.

- [x] **Task 3: Add reverse-graph marker to `note`**
  Files: `src/skills/note/SKILL.md`
  `note` has no explicit load-once statement in its body, so place the marker near the top — after the one-line intro under `# Note — Research Summary Extraction` (line ~19), before `## Workflow`. Same declarative sentence shape, with the grep literal `` grep -l "note" src/skills/*/SKILL.md src/commands/*.md ``. Constraint: do not disturb the `### Hooks (caller inputs)` section, the default template, or any default behavior — the marker is prose added ahead of the workflow, nothing else. Declarative only, no caller names, no new section, no frontmatter field.

### Phase 2: Convention

- [x] **Task 4: Record the marker convention in CLAUDE.md**
  Files: `CLAUDE.md`
  In the "Dependencies and the skill graph" section, add one line establishing the marker as part of the convention: every engine (any skill named in a `loads:` field) carries the reverse-graph marker in its body, and a new engine gets the marker when the first `loads:` edge to it appears. Frame it as a companion to the existing coupling-declaration rule (caller side declares *whom* it loads; engine side declares *that it is loaded* and how to find by whom). One line, no caller list.

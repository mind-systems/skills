# Plan: `loads:` convention — declared, colocated skill dependencies; graph derived by grep

## Context
Make skill-to-skill load edges syntactic and colocated via a frontmatter `loads:` field in each depending skill, declare the rescue↔audit shared-register invariant at both ends, and add a lean "Dependencies and the skill graph" subsection to CLAUDE.md — with no static map anywhere, so the whole-picture graph is always derived by grep.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter `loads:` declarations

- [x] **Task 1: Add colocated `loads:` frontmatter to every depending skill**
  Files: `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md`, `src/skills/roadmap-test-coverage/SKILL.md`, `src/skills/roadmap-engine/SKILL.md`
  Add a top-level `loads:` frontmatter field (space-separated skill names) to each depending skill, placed among the existing top-level frontmatter keys (unknown fields are ignored by the harness, so this is safe — do not touch `allowed-tools`, `name`, `description`, etc.):
  - `roadmap-outline` → `loads: roadmap-engine`
  - `roadmap-decompose` → `loads: roadmap-engine`
  - `roadmap-decompose-skeleton` → `loads: roadmap-engine test-philosophy`
  - `roadmap-test-coverage` → `loads: test-philosophy`
  - `roadmap-engine` → `loads: note` (the engine declaring its own forward dependency on `note` does not violate caller-agnosticism — note 38 only forbids naming one's callers)
  Direction is one-way only: NO `loaded-by:` / reverse-edge field anywhere. Engines never list their callers. Skills that load nothing get no `loads:` field. Do not touch `upstream/ai-factory/`.

- [x] **Task 2: Verify completeness of declared edges by grep** (depends on Task 1)
  Files: (verification only — `src/skills/*/SKILL.md`, `src/commands/*.md`)
  Grep `src/skills/*/SKILL.md` and `src/commands/*.md` for Skill-tool load instructions and `Skill` in `allowed-tools`; confirm every real load edge is declared and none are invented. `ui-ux-pro-max`'s only `Skill` hit is a body heading ("How to Use This Skill"), not a load — exclude it. Also confirm `roadmap-decompose-skeleton`'s existing body "Call graph" section matches its new `loads:` line (leave that section in place — it is colocated and correct). No file changes unless a missing or spurious edge is found.

### Phase 2: Both-ends invariant declaration

- [x] **Task 3: Declare the shared Diagnosis-Report register at the rescue end** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In the Diagnosis Report spec (around the "Form: a chronological narrative in plain prose" paragraph, ~line 115), add one sentence noting that this narrative register is shared with `milestone-rescue-audit`'s output and must be changed in both files or neither. The audit end is already declared (`milestone-rescue-audit/SKILL.md` ~line 145 already says "the same register as `milestone-rescue`'s Diagnosis Report") — do not modify the audit file. Behavior-identical change: no other edits to rescue's body, sidecar `step` table, git commands, or frontmatter.

### Phase 3: CLAUDE.md convention subsection

- [x] **Task 4: Add "Dependencies and the skill graph" subsection to CLAUDE.md** (depends on Task 3)
  Files: `CLAUDE.md`
  Under the `## Skill Authoring` section (after the "Composition — mechanism vs policy" subsection, alongside the other `###` subsections), add a compact `### Dependencies and the skill graph` subsection (~25 lines, lean — CLAUDE.md loads every session). Cover, as prose/bullets, with NO static dependency map:
  - Dependencies are declared in the depending skill's frontmatter `loads:` field; engines never list their callers.
  - Forward graph = read `loads:` fields. Reverse graph = `grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md`. The declarations are the map — there is no central map to maintain.
  - Cross-file invariants no grep can derive (shared output registers, mirrored tables) are declared at the coupling point in **both** files.
  - Editing rules: grep for an engine's callers before touching it (their expectations are part of its contract); never inline engine content into a philosophy; "behavior-identical" / "word-for-word" in spec notes are contract text (the only type system this code has); a skill's output register is behavior — never simplify a prose-narrative requirement into tables; a refactored skill is unverified until a live run compares its output.
  - Pointers: `docs/skill-composition-model.md` (semantics), `docs/workflow.md` (pipeline order).
  Do NOT write a static graph, generate-a-map script, or `loaded-by:` list into CLAUDE.md, AGENTS.md, or any doc — that is the rejected cache-without-invalidation design.

# Plan: roadmap-outline: slim to philosophy-only over the engine's flow

## Context
Rewrite `src/skills/roadmap-outline/SKILL.md` to hold only its strategic lens and delegate all create/update/check flow machinery to `roadmap-engine`, matching the sibling `roadmap-decompose` slim (note 44). Behavior for the user must stay identical in every mode.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Slim the skill body

- [x] **Task 1: Replace the duplicated flow machinery with an engine-delegation header**
  Files: `src/skills/roadmap-outline/SKILL.md`
  Delete Step 0 (Load Project Context), Step 1 (Determine Mode), and all Mode 1/2/3 machinery — gather-input dialogs, codebase explore, draft-in-memory → confirm → notes-after-confirmation, progress review, check-mode scan, and summary blocks — the whole span from the `## Workflow` heading through the end of Mode 3 (current lines ~14–221). All of it is now covered by the engine's "Roadmap maintenance flow".
  Replace with the decompose-style opener: a one-sentence intro describing the strategic tier, then "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded) and run its **Roadmap maintenance flow** with the hooks below." Mirror the phrasing in `src/skills/roadmap-decompose/SKILL.md` lines 15–22.
  Keep the frontmatter as-is (lines 1–8): `loads: roadmap-engine` is already present; do NOT reintroduce a `Questions` pseudo-tool (removed by note 41) or any `/aif-plan` reference (removed by note 36). `AskUserQuestion` stays in `allowed-tools` (the engine's flow uses it).

- [x] **Task 2: Write the four hook sections for the engine's flow** (depends on Task 1)
  Files: `src/skills/roadmap-outline/SKILL.md`
  Add a `## Hooks for `roadmap-engine`'s flow` section with the four hook subsections, following the decompose layout (lines 24–72) but carrying outline's strategic philosophy:
  - **(a) Granularity** — each entry is a **high-level goal**: a capability the system gains, not a task; 5–15 milestones is the sweet spot (fewer = too vague, more = too granular); milestones later serve as **phase names** for the decomposition pass; order by logical sequence, dependencies first. Include the two parity carry-overs the engine's create flow does not itself hold: on first run mark already-completed milestones `[x]`; supply the Create-mode gather-input question that fills the engine's `AskUserQuestion: <caller phrases this…>` placeholder — phrase it as *"What are the major goals for this project?"* (matching the original Mode 1.1 wording).
  - Add coarse two-tier rendering + optional-note rule here (or as a short note directly under Granularity): entries render per the engine's format at strategic granularity (contract line + spec note), vision line sourced from `DESCRIPTION.md` or user input. The spec note is **optional at this tier** — when the contract line alone fully carries the milestone-phase (often just a named capability), skip the note and end the entry with no `Spec:` tag rather than pointing at an invented one; write a note only when there is real strategic content the line can't hold (constraints, ordering rationale, scope boundaries); never pad a note to justify its existence — `roadmap-decompose` writes the real notes later.
  - **(b) Per-entry gate** — register **none**. State explicitly that outline supplies no per-entry gate hook: restraint at the strategic tier is the 5–15 rule, not a split gate, and the agent must not improvise an atomicity-style gate here (that is decompose's gate).
  - **(c) Target-file routing** — always `.ai-factory/ROADMAP.md` (trivial policy, no keyword/argument branching).
  - **(d) Extra update-mode actions** — none beyond the engine's built-in menu (review progress / add / reprioritize / rewrite). State that outline registers no added action.

- [x] **Task 3: Reduce Critical Rules to philosophy-tier only** (depends on Task 2)
  Files: `src/skills/roadmap-outline/SKILL.md`
  Replace the current `## Critical Rules` block (lines 223–229) with a philosophy-tier list matching decompose's closing style (lines 74–81). Keep only rules that are outline's philosophy and NOT already owned by the engine's mechanism rules (read-before-modify, never remove silently, `[x]` stays until prune all live in the engine now — do not restate them):
  - Milestones are high-level — granular tasks belong to `/roadmap-decompose`.
  - Every milestone renders two-tier per `roadmap-engine`'s format, but the spec note is optional at this tier (per hook a) — never invent note content to fill a `Spec:` tag.
  - NO implementation — this skill only plans; the orchestrator implements in a separate run (post-note-36 wording, no `/aif-plan`/`/aif-implement` refs).
  Target total body size ~40–70 lines. Do not restate engine flow or format content inline anywhere.

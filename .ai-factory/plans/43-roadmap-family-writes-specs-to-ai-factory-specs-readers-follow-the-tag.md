# Plan: Roadmap family writes specs to `.ai-factory/specs/`; readers follow the tag

## Context
Retarget the roadmap family's spec-note writes to a new `.ai-factory/specs/` directory and make every spec *reader* resolve the file through its `Spec:` tag instead of a hardcoded directory — so the notes→specs migration is lazy (no project touched, old tags keep working) and invisible to readers.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Global constraints (apply to every task)
- **Depends on note 53** — `note`'s destination hook is already implemented (roadmap task marked `[x]`); this task consumes it.
- **Lazy migration — touch no project data.** Never `git mv` an existing `notes/` directory, never rewrite an existing `Spec:` tag, never bulk-edit existing roadmaps or spec files. Only skill/command/doc *bodies* change.
- **Default stays `notes/`.** Do not change `note`'s default destination; only callers pass `.ai-factory/specs/`. Standalone `/note` must remain byte-identical.
- **Out of scope:** `command-handoff` (note 55), `note`'s own defaults (note 53), `roadmap-prune` (note 56). Do not edit them here.
- **Upstream mirror untouched** — never edit anything under `upstream/`.
- Readers must resolve specs **only** through the `Spec:` tag — no reader may keep a hardcoded spec directory.

## Tasks

### Phase 1: Writers — retarget new writes to `.ai-factory/specs/`

- [x] **Task 1: roadmap-engine — retarget spec-note path, numbering, and the destination hook**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In "The two-tier artifact" (≈ lines 25–28): change the spec-note path to `.ai-factory/specs/<NN>-<slug>.md`, the `<NN>` numbering scan to run **against `.ai-factory/specs/`**, and the exact `Spec:` tag example to `` Spec: `.ai-factory/specs/<NN>-<slug>.md`. ``. In the note-loading sentence (≈ lines 30–31): state that when invoking `note` the caller passes destination `.ai-factory/specs/` via note's destination hook (note 53), and per-directory numbering happens there. In the "Roadmap File Format" example block (≈ lines 49–51) and the Create-mode finalize step (≈ line 147, "replace `<note pending>` with the real tag"): change every `` .ai-factory/notes/<NN>-<slug>.md `` to `` .ai-factory/specs/<NN>-<slug>.md ``. Leave "Never write a full spec inline" and all philosophy-tier text unchanged.

- [x] **Task 2: roadmap-test-coverage — Layer 4/6/8 note paths to `specs/`**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Per note 54, the Layer 4 test-plan notes are roadmap-family specs and move to `specs/`. Layer 4 numbering scan (≈ lines 92–93): `mkdir -p .ai-factory/specs` and `find .ai-factory/specs -name "[0-9][0-9]-*.md"`. Layer 4 agent-prompt paths (≈ lines 110, 125, 149 — "Note to write:", "Write the following document to", "saved:") → `.ai-factory/specs/<NN>-<slug>.md`. Layer 6 note pointer (≈ line 196) and Layer 8 output/handoff pointers (≈ lines 277, 294, 298) → `.ai-factory/specs/<NN>-<slug>.md`. Do not alter the agent-prompt template structure, the test-philosophy logic, or the layer flow — path strings only.

- [x] **Task 3: roadmap-outline docs — example `Spec:` paths to `specs/`** (depends on Task 1)
  Files: `src/skills/roadmap-outline/docs/overview.md`
  Update the example roadmap lines and prose that hardcode `` .ai-factory/notes/<NN>-<slug>.md `` (≈ lines 14–15, 25–26) to `` .ai-factory/specs/... ``, matching the engine's new target so copy-paste examples point to the new directory. Note: the philosophy `SKILL.md` files (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) hold **no** literal `notes/` path (verified by grep — they defer to the engine and resolve via the `Spec:` tag); do not invent edits there.

### Phase 2: Readers — de-hardcode; resolve through the `Spec:` tag

- [x] **Task 4: milestone-rescue — resolve the spec via the tag; rephrase the artifact filter and the guard**
  Files: `src/skills/milestone-rescue/SKILL.md`, `src/skills/milestone-rescue/docs/overview.md`
  Replace every literal spec-directory reference with tag-resolution: line ≈26 ("alongside the spec note in `.ai-factory/notes/`") → "alongside the spec note the milestone's `Spec:` tag names"; line ≈187 and line ≈246 (`.ai-factory/notes/<NN>-…md`) → "the spec note the `Spec:` tag points at". Rephrase the **artifact-discovery filter** (line ≈45, "Ignore any uncommitted files outside these directories (e.g. `notes/`)") so the four artifact dirs (`plans/`, `plan-reviews/`, `reviews/`, `patches/`) stay the whitelist but the example no longer implies a fixed spec directory — spec files live wherever the tag points. Rephrase the **guard** (line ≈232, "Never touch `.ai-factory/notes/` except the deliberate spec-note repair") to "Never touch the spec file (wherever its `Spec:` tag points) except the deliberate spec-note repair". Apply the same de-hardcoding to `docs/overview.md` (≈ line 147, "belonging to other milestone slugs … `.ai-factory/notes/`"). Keep all repair-depth logic and rollback mechanics unchanged.

- [x] **Task 5: command-pin-gaps & temporal-tree — verify tag-resolution, de-hardcode any directory wording**
  Files: `src/commands/command-pin-gaps.md`, `src/skills/temporal-tree/SKILL.md`
  `command-pin-gaps` already resolves the spec through the `Spec:` tag ("its `Spec:` note file", line ≈13) with no hardcoded directory — confirm this and, only if it clarifies, phrase it as "the file its `Spec:` tag names"; introduce **no** directory literal. `temporal-tree` contains no spec-directory reference (grep-verified — it reads `ARCHITECTURE.md`'s `## Features` table and `plans/`); confirm and leave unchanged. This task is verification with at most a one-line wording tweak — do not manufacture edits.

### Phase 3: Docs — record the genre split once

- [x] **Task 6: genre-split note across CLAUDE.md, global CLAUDE.md, and workflow doc**
  Files: `CLAUDE.md`, `src/global/CLAUDE.md`, `docs/workflow.md`
  State the split once per file: `specs/` = roadmap-family task specs (new writes), `notes/` = legacy location still served via `Spec:` tags, `handoffs/` = session handoffs. In repo `CLAUDE.md`: extend the `.ai-factory/` line in the repository-structure tree (≈ line 56, "Roadmap, notes, architecture, plans") to name `specs`/`handoffs`, and add a one-line genre note near the planning-chain section (≈ line 146). In `src/global/CLAUDE.md`: the two guidance lines that literally direct where the two-tier spec note goes (≈ line 21 monorepo routing, ≈ line 46 planning chain — both say "spec note in `.ai-factory/notes/`") retarget to `.ai-factory/specs/` for new work, since the engine now writes there; keep the lazy-migration reality (old tags still valid). In `docs/workflow.md` (Russian — **match the doc's language**): where it lists `.ai-factory/` artifacts / "спек-ноты" (≈ line 9), add a brief note that new spec-notes live in `.ai-factory/specs/`, legacy ones stay in `notes/` and are followed via the `Spec:` tag, handoffs in `handoffs/`. `docs/skill-composition-model.md` names no directory ("спек-нота" only) → leave it. No README doc table (per convention).

## Commit Plan
- **Commit 1** (after tasks 1-3): "Retarget roadmap-family spec writes to .ai-factory/specs"
- **Commit 2** (after tasks 4-5): "Resolve spec files through the Spec tag in rescue and readers"
- **Commit 3** (after task 6): "Document the specs/notes/handoffs genre split"

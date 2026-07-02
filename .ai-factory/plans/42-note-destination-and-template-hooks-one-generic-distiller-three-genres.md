# Plan: note: destination and template hooks — one generic distiller, three genres

## Context
Turn `note`'s hardcoded destination (`.ai-factory/notes/`) and section template into caller-supplied hooks, with today's values as defaults so standalone `/note` stays byte-identical — letting callers (roadmap-engine, command-handoff) reuse the engine instead of hand-rolling file machinery.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Add the hooks to the note engine

- [x] **Task 1: Introduce the destination-directory and template hooks**
  Files: `src/skills/note/SKILL.md`
  Add a short "Hooks" (caller inputs) subsection near the top of the Workflow that names two optional caller-supplied inputs, each defaulting to today's behavior when unset:
  - **Destination directory** — target directory for the note. Unset → default `.ai-factory/notes/` exactly as now. When set, every directory-scoped step uses it: the `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path. Numbering stays **per-directory** (scan the chosen directory only).
  - **Template** — a section skeleton for the note body. Unset → the current default template (Key Findings / Details / Open Questions). When set, the note body follows the caller's skeleton verbatim; `note` supplies only the mechanism (mining, distillation, numbering, placement) and does not reshape the caller's structure.
  Keep the section terse and mechanism-only — do not introduce any genre-specific content (no spec rules, no handoff skeletons). This is the composition-model split: mechanism stays in `note`, policy (what/where) becomes the caller's.

- [x] **Task 2: Thread the destination hook through Steps 3–4 and Note File Handling**
  Files: `src/skills/note/SKILL.md`
  Rewrite the directory-bound instructions to reference the destination hook instead of the literal path, while keeping the unset default `.ai-factory/notes/` explicit:
  - Step 3 "Save Note to File": path becomes `<destination>/<NN>-<slug>.md` where `<destination>` defaults to `.ai-factory/notes/`; the `<NN>` scan and the `mkdir -p` both target `<destination>`.
  - Step 4 "Report": the printed path uses `<destination>` (default `.ai-factory/notes/`).
  - "Note File Handling" section: describe notes living at `<destination>/<NN>-<slug>.md`, `<NN>` scanned per-directory in `<destination>`.
  Preserve the exact wording of the numbering rule (highest existing `NN` prefix + 1, start at `01`), the slug rule, and the Important Rules — only the directory reference changes. Standalone no-argument invocation must remain byte-identical to today.

- [x] **Task 3: Thread the template hook through Step 3 and update the frontmatter description**
  Files: `src/skills/note/SKILL.md`
  - In Step 3, state that when the template hook is unset the note follows the default template block shown there (unchanged); when set, the body follows the caller's skeleton verbatim. Keep the default template block intact as the unset case. The Important Rules (concise, findings-focused, include file paths, English) apply to both cases.
  - Update the frontmatter `description` to name the genre space: generic distiller for research notes, task specs, and handoffs, where destination and template are caller-supplied with defaults unchanged. Keep `user-invocable: true` and `disable-model-invocation: false` — standalone `/note` stays valid and unchanged. Do not rename the skill (`name: note` unchanged).

## Notes for the implementer
- Do **not** touch any caller — `roadmap-engine` (spec note 54) and `command-handoff` (spec note 55) adopt these hooks in their own separate milestones.
- Do **not** change the default destination away from `.ai-factory/notes/` — lazy migration across existing projects depends on the default staying put.
- Load-once discipline unchanged; the skill is edited in `src/skills/note/`, which `active/skills/note` already symlinks to.
- Fewer than 5 tasks — single commit at the end: "Add caller-supplied destination and template hooks to the note engine".

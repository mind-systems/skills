# Plan: 1.3 — note: folder-style layer — read siblings before writing

## Context
Add an always-on mechanism to the `note` engine so that before composing a note it reads the 1–2 most recent numbered neighbors in the destination folder and matches the folder's house style — below caller hooks, above engine defaults — giving every writer in the family (roadmap-engine, command-handoff) folder-consistent output for free.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Folder-style layer in the note engine

- [x] **Task 1: Add the sibling-read rule to Step 3**
  Files: `src/skills/note/SKILL.md`
  In `### Step 3: Save Note to File` (around the numbering scan at lines 50–55, before the template/compose block), add a "Folder style" rule as a mechanism step that runs before composing the body:
  - After determining `<NN>`, read the 1–2 most recent `[0-9][0-9]-*.md` files in `<destination>` (the same directory scanned for numbering — reuse that scan; highest-numbered neighbors) to learn the folder's prevailing register, prose-vs-list density, and heading/formatting habits.
  - Hold to that style **only where the caller's hooks are silent** — style is *matched*, never content-copied.
  - Guards, stated inline: empty folder (or a hook that already fully determines the body) → skip silently, no ceremony; at most 2 sibling reads.
  - State the three-level precedence at the rule: (1) caller hooks (template/verbosity) always win, (2) neighbor style fills only what hooks leave unsaid, (3) engine defaults last.
  Keep the existing numbering/`mkdir`/path text and the default-template block byte-identical in behavior — the only new observable behavior is up to 2 extra sibling reads. Follow the existing Step 3 prose register (numbered/bulleted mechanism description, matching lines 48–98).

- [x] **Task 2: State the precedence order in the Hooks section**
  Files: `src/skills/note/SKILL.md` (depends on Task 1)
  In `### Hooks (caller inputs)` (lines 27–33), add one line pinning that the folder-style layer sits strictly *below* the three hooks: hooks (template/verbosity) define structure and depth and always win; folder style fills only what hooks leave unsaid; engine defaults apply last. Do not alter the three hooks' semantics — they stay byte-identical; the folder-style layer is mechanism, always-on, with no new hook or parameter. Ensure the wording is consistent with the precedence stated in Task 1 (single source of truth — the Hooks line points at the layer, the Step 3 rule holds the mechanism).

## Verification (from spec `.ai-factory/specs/21-note-folder-style-layer.md`)
- Step 3 contains the sibling-read rule with the three-level precedence and the empty-folder skip.
- **Live behavioral check** (behavior-first, per the phase's hard rule — ROADMAP.md lines 145/149; not discharged by `Settings → Testing: no`, which only means no automated test file): write a note into a folder whose existing files use a distinct register (e.g. `specs/` two-tier spec notes) with a minimal template hook — the new file matches the folder's register where the hook is silent, while the caller hook still shapes structure. This exercises the new mechanism, not just its presence.
- Callers `roadmap-engine` and `command-handoff` need no edits — confirm no caller-facing contract changed (`grep -l "note" src/skills/*/SKILL.md src/commands/*.md` to re-check the reverse graph; no edits expected there).
- Unset-hooks standalone output rules stay byte-identical; the only new behavior is ≤2 extra sibling reads.

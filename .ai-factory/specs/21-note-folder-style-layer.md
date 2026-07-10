# note: folder-style layer — read siblings before writing

## Current state

`src/skills/note/SKILL.md` writes `<destination>/<NN>-<slug>.md` knowing nothing about what already lives in `<destination>`: Step 3 scans siblings only for the `<NN>` numbering, never for their register. Every destination folder (`specs/`, `handoffs/`, `notes/`, any caller-supplied dir) accumulates a de-facto house style — section density, register, formatting — but each new note is written blind to it, so style consistency depends on the caller's template alone. The whole roadmap family funnels through `note` (outline/decompose/skeleton → roadmap-engine → note; command-handoff → note), so the engine is the single point where a folder-style rule covers every writer at once.

## Change

One addition to `note`'s mechanism (Step 3, before composing the body): **read the folder's style from its neighbors** — open the 1–2 most recent `[0-9][0-9]-*.md` files in `<destination>` and hold to the folder's prevailing style. Precedence pinned hard:

1. **Caller hooks win, always** — the template and verbosity directives define structure and depth; a sibling never overrides a hook.
2. **Neighbor style fills only what hooks leave unsaid** — register, prose-vs-list density, heading/formatting habits.
3. **Engine defaults** apply last, as today.

Guards inside the rule: empty or hook-covered-everything folder → skip silently, no ceremony; at most 2 sibling reads; style is *matched*, never copied content-wise.

## Files & types

- edit `src/skills/note/SKILL.md` — one rule in Step 3 (or an adjacent "Folder style" paragraph) + one line in the Hooks section stating the precedence order

## Guards

- **Engine edit** — `note` is a load-once engine with callers depending on exact behavior (`roadmap-engine`, `command-handoff`); grep callers first; the three hooks' semantics are byte-identical, the style layer sits strictly *below* them.
- Unset-hooks standalone behavior stays byte-identical in output rules — the only new observable behavior is up to 2 extra sibling reads.
- No new hook, no parameter — this is mechanism, always-on.

## Verification

- Step 3 contains the sibling-read rule with the three-level precedence and the empty-folder skip.
- Live check: write a note into a folder whose existing files use a distinct register (e.g. `specs/` two-tier spec notes) with a minimal template hook — the new file matches the folder's register where the hook is silent; caller hooks still shape structure.
- Callers unchanged: `roadmap-engine`, `command-handoff` require no edits.

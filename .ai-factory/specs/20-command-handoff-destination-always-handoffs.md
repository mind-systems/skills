# command-handoff: rewrite to a lens over `note` — destination invariant included

## Current state

`src/commands/command-handoff.md` is the package's flagship pyramid inversion: 140 lines sitting on top of the 114-line `note` engine it delegates to. The file carries genuine policy — the meaning-tree mandate and map scoping (Step 2), the grid skeleton and prose shape (the template payload), the tree-completeness gate, the three `note` hooks, the minimal paste-back pointer — wrapped in ceremony that restates what the engine and the shapes already carry. And one live regression: the destination hook is pinned as bare `.ai-factory/handoffs/` (`:117`), so when the user names a target project ("сложи в `~/projects/mind/mind_api`") the agent treats the path as replacing the whole destination and the handoff lands in that project's `notes/`.

## Change

Rewrite the whole file as a **lens**: route plus policy, nothing else.

- **Destination invariant (absorbs the former standalone fix):** a handoff always lives in a `handoffs/` directory — a user-named path names the **project root only**; destination = `<root>/.ai-factory/handoffs/` (current project's when no target is named). Stated as an invariant of the artifact, not a rule about arguments; no new parameters, no modes.
- **Keep as policy, compressed to intent:** the meaning-tree mandate, next-step-scoped map, both shapes (the grid skeleton stays inline — its placeholders are the mining lens, i.e. the template-hook payload; the prose directive likewise), the tree-completeness gate, the verbosity directive, the semantic-slug rule, the minimal paste-back pointer.
- **Cut:** everything `note` already does (mining choreography, numbering, `mkdir`/`Write` mechanics — none may be restated), transitional explanations, ceremony around the delegation.
- Two-reader register throughout: imperatives to the executor, declarations to the editor.

## Guards

- **Behavior byte-equivalent except the destination fix** — shapes, gate semantics, pointer content, hook payloads unchanged in meaning even where wording compresses; spec 15's one-path design stands.
- `loads: note` frontmatter and the three-hook delegation stay; no file mechanics re-enter the command.
- ~80 lines is the aspiration, never a clamp — the skeleton is legal mass (it is the payload, not ceremony).

## Verification

- Live baseline: run the command on a real session before and after the rewrite; the handoff files must carry the same tree at the same depth; the paste-back pointer identical in structure.
- Destination check: invoke with an explicit foreign project path → file lands in `<that root>/.ai-factory/handoffs/<NN>-<slug>.md`, never `notes/`.
- `grep -n "mkdir\|Write\|numbering" src/commands/command-handoff.md` → no re-stated engine mechanics.

# Plan: 77.9 — "Decompose existing" points at the engine's definition of a task spec

## Context
Replace the first sentence under hook (d) "Decompose existing" in `src/skills/roadmap-decompose/SKILL.md`. It now lists a task spec's contents in its own parenthesis ("what exists today, … guards"). The new sentence points at `roadmap-engine`'s paragraph "What a task spec holds" instead. The task spec (`.ai-factory/specs/trickster77777/0225-decompose-existing-points-at-the-engines-definition-of-a-task-spec.md`, § "What must be true after") pins the new sentence verbatim and is the authority. The phase's governing specs are `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`.

Ground truth at planning time:
- Under the heading `### (d) Extra update action — "Decompose existing"`, the sentence is hard-wrapped over two lines and matches the spec's § "What is true now" quote word for word:
  `Register an added update-menu action: expand a vague task into a full spec (what`
  `exists today, the exact change, files/types/methods to touch, guards).`
- The skill's frontmatter already has `loads: roadmap-engine`, so the frontmatter does not change.
- `roadmap-engine/SKILL.md` has a bold lead-in `**What a task spec holds:**`, so the reference resolves by name.
- No open task above 77.9 in the roadmap edits this file.
- `active/skills/roadmap-decompose` is a symlink into `src/skills/roadmap-decompose`, so only the `src/` file is edited.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Replace the sentence

- [x] **Rewrite hook (d)'s opening sentence to point at the engine**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Under `### (d) Extra update action — "Decompose existing"`, replace the two-line sentence above with exactly this text, wrapped the same way the spec wraps it:
  ```
  Register an added update-menu action: expand a vague task into a full task spec, as
  `roadmap-engine`'s "What a task spec holds" defines it.
  ```
  If this plan and the spec disagree, copy the text from the spec's § "What must be true after". Keep the backticks around `roadmap-engine` and the straight double quotes around the paragraph name. Delete the parenthesis entirely. The blank line after the sentence and the "Task-spec-handling rule:" list below it stay as they are. Change nothing else in the file, including the earlier paragraph about reading the phase preamble, which names hook (d)'s "Decompose existing".

### Blast radius

- [x] **Run the spec's sweep and confirm nothing else restates the parenthesis** (depends on Rewrite hook (d)'s opening sentence to point at the engine)
  Files: none edited
  Run `grep -rn "exists today\|expand a vague task\|Decompose existing" src docs CLAUDE.md --include="*.md"` from the repo root. Expected matches: the new sentence ("expand a vague task"), the hook (d) heading, and the preamble paragraph that names hook (d)'s "Decompose existing". "exists today" should no longer match anything. Any other match that lists a spec's contents or relies on the removed parenthesis is a finding: report it and do not edit it.

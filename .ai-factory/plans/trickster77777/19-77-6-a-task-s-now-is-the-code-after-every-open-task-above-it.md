# Plan: 77.6 — a task's now is the code after every open task above it

## Context
Add one new standing entry, "**Standing entry — a task's now.**", to `## Method` in `src/skills/agent-architect/templates/buffer-seed.md`. It goes directly after "**Standing entry — what a spec holds.**" and before "**Standing entry — state the behaviour and stop.**". The entry says a task's "what is true now" is the code as every open task above it leaves it, not the tree on the day of writing. The task spec (`.ai-factory/specs/trickster77777/0222-a-tasks-now-is-the-code-after-every-open-task-above-it.md`, § "What must be true after") pins the entry verbatim and is the authority. The phase's governing specs are `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`; the second already carries this meaning in § "What a spec holds" ("read from the code as every open task above it leaves it").

Ground truth at planning time:
- The seed matches the spec's § "What is true now": the counts entry already carries 77.5's work-order sentence, and the entry "**Standing entry — what a spec holds.**" ends "…scope is / what the task changes." It is followed by a blank line, then "**Standing entry — state the behaviour and stop.**".
- Standing entries are separate paragraphs, each with a bold lead-in and a blank line between them. The prose is hard-wrapped at roughly 76 columns.
- The seed's opening paragraph, and `agent-architect/SKILL.md` § "Spawn once, message thereafter", match an entry by its bold lead-in "Standing entry —" and add any seed entry a buffer lacks. So the new entry reaches existing buffers at their next rehydration, and neither text needs a change.
- `active/skills/agent-architect` is a symlink into `src/skills/agent-architect`, so only the `src/` file is edited.
- No open task above 77.6 in the roadmap edits this file.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Add the entry

- [x] **Insert "Standing entry — a task's now." after "what a spec holds"**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Under `## Method`, insert a new paragraph between the paragraph that opens `**Standing entry — what a spec holds.**` and the paragraph that opens `**Standing entry — state the behaviour and stop.**`. Put one blank line before it and one after it, like the entries around it. The paragraph is exactly:
  ```
  **Standing entry — a task's now.** The roadmap runs top to bottom, one task
  at a time, so a task's "what is true now" is the code as every open task
  above it leaves it, not the tree on the day of writing. It is built from
  their "after", under their names, and what one of them rewrites is never
  quoted into it.
  ```
  If this plan and the spec disagree, copy the text from the spec's § "What must be true after". Keep the words, the punctuation, the straight double quotes and the straight apostrophe in "task's" exactly as given. The em dash `—` stays literal. Change nothing else in the file.

### Blast radius

- [x] **Run the spec's sweep and confirm nothing else needs the change** (depends on Insert "Standing entry — a task's now." after "what a spec holds")
  Files: none edited
  Run the two searches from the spec's § "What breaks on contact":
  ```
  grep -rn "Standing entry" src docs CLAUDE.md --include="*.md"
  grep -rn "exact values\|read from the code" src docs --include="*.md"
  ```
  The spec's finding says what each search should reach. The first reaches the seed's own entries, including the new one. It also reaches the seed's opening paragraph, which picks the new entry up by its lead-in with no edit. The second reaches `src/skills/roadmap-engine/SKILL.md` § "What a task spec holds" and `docs/what-a-task-carries.md` § "What a spec holds". Both stay as they are: the doc already carries the meaning, and the engine is not in this task's scope. Existing buffers under `.ai-factory/architects/` take the entry at their next rehydration, so leave them alone. If any skill or doc under `src/` or `docs/` says a task's "what is true now" is the tree on the day of writing, or tells a spec to quote what an earlier open task rewrites, stop and report it. Do not edit it.

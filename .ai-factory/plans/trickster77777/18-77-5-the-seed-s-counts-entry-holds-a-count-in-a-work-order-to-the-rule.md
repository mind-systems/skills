# Plan: 77.5 — the seed's counts entry holds a count in a work-order to the rule

## Context
Add one sentence to the entry "**Standing entry — the counts rule.**" in `src/skills/agent-architect/templates/buffer-seed.md`. The entry currently says "in conversation a number or a position is fine", which puts a work-order on the permitted side. The new sentence says a count in a work-order is held to the same rule. The task spec (`.ai-factory/specs/trickster77777/0219-the-seeds-counts-entry-says-a-work-order-is-not-conversation.md`, § "What must be true after") pins the sentence verbatim and is the authority. The phase's governing specs are `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`.

Ground truth at planning time:
- The entry's first sentence matches the spec's § "What is true now" quote word for word.
- The seed is prose hard-wrapped at roughly 76 columns. Inside the entry the first sentence ends "…since a / wrong one costs one reply." and is followed on the same line by "A number someone decided is written:".
- `active/skills/agent-architect` is a symlink into `src/skills/agent-architect`, so only the `src/` file is edited.
- No open task above 77.5 in the roadmap edits this file. 77.6, the next task, is written against the entry as 77.5 leaves it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Extend the counts entry

- [x] **Insert the work-order sentence after the "in conversation" clause**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  In the paragraph that opens `**Standing entry — the counts rule.**`, insert this exact sentence immediately after "since a wrong one costs one reply." and before "A number someone decided is written:":
  `A count in a work-order is held to the same rule: the spec is composed from the order, and a count in it becomes a count in the spec.`
  If this plan and the spec disagree, copy the sentence from the spec's § "What must be true after". Re-wrap only this paragraph so it keeps the file's existing line width. Reflowing changes line breaks only: no word or punctuation mark changes, and the em dashes `—` stay literal. Every other word of the entry, from "A number someone decided is written:" to the end, stays as it is. Change nothing else in the file.

### Blast radius

- [x] **Run the spec's sweep and confirm nothing else restates the clause** (depends on Insert the work-order sentence after the "in conversation" clause)
  Files: none edited
  Run the two searches from the spec's § "What breaks on contact":
  ```
  grep -rn "in conversation a number" . --include="*.md" --exclude-dir=.git
  grep -rln "counts rule" src docs --include="*.md"
  ```
  The spec's finding says what each search should reach. The first reaches the seed, which is the edited target. It also reaches the existing heads' buffers under `.ai-factory/architects/`, which each head refreshes from the seed at its next rehydration. Leave those buffers alone. Finally it reaches the phase note and task specs under `.ai-factory/specs/trickster77777/` that quote the clause. Those are planning records, so leave them alone too. The second search reaches only the seed. If any skill or doc under `src/` or `docs/` restates the "in conversation" clause, or carries the counts rule as permitting a number in a work-order, stop and report it. Do not edit it.

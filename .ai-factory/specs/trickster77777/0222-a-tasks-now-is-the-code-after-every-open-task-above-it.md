# 77.6 — a task's now is the code after every open task above it

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, as 77.5 leaves it, holds under `## Method` the entry "**Standing entry — the counts rule.**", which reads: "It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply. A count in a work-order is held to the same rule: the spec is composed from the order, and a count in it becomes a count in the spec." The rest of that entry is unchanged by 77.5. The entry after it is "**Standing entry — what a spec holds.**": "A spec states what is true now, what must be true after and what breaks on contact, and nothing else. It carries no check that the instruction was carried out: the orchestrator plans, builds and reviews on its own, and a check written into a spec comes back as plan steps and review rounds. It names no position in a file, only what the artifact must hold. It puts no fence around a neighbour; scope is what the task changes." The entry after that is "**Standing entry — state the behaviour and stop.**".

None of them says whose "now" a spec's "what is true now" is. Read literally, "read from the code" is the tree on the day of writing, while the roadmap runs top to bottom, one task at a time, and each task finds the code as the tasks above it left it. `docs/what-a-task-carries.md` § "What a spec holds" says it: what is true now is "read from the code as every open task above it leaves it". The seed's own opening says the entries under `## Method` whose lead-in begins "Standing entry —" are brought to its text at every start that finds a buffer's folder.

## What must be true after

Directly after the entry "**Standing entry — what a spec holds.**", and before "**Standing entry — state the behaviour and stop.**", under `## Method`, a new entry reads:

```
**Standing entry — a task's now.** The roadmap runs top to bottom, one task
at a time, so a task's "what is true now" is the code as every open task
above it leaves it, not the tree on the day of writing. It is built from
their "after", under their names, and what one of them rewrites is never
quoted into it.
```

Nothing else in the seed changes.

## What breaks on contact

**Rule:** a text breaks on this change if it states a task's "what is true now" as the tree on the day of writing, or tells a spec to quote what an earlier open task rewrites.

**Sweep:**
```
grep -rn "Standing entry" src docs CLAUDE.md --include="*.md"
grep -rn "read from the code" src docs --include="*.md"
```

**Finding.** The first search reaches the seed's own entries, where the new entry lands, and its opening paragraph, which matches an entry by the lead-in "Standing entry —" and so takes the new one in without a change. The buffers of existing heads hold copies of the standing entries and take the seed's text at their next rehydration, adding an entry the seed has that the buffer lacks, as `agent-architect` § "Spawn once, message thereafter" has it. The second search reaches `roadmap-engine`'s "What a task spec holds", which 77.3 leaves saying "read from the code with exact values", and `docs/what-a-task-carries.md` § "What a spec holds", which already carries the meaning.

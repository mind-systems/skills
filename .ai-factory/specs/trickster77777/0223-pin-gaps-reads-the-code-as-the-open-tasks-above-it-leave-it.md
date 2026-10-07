# 77.7 — pin-gaps reads the code as the open tasks above it leave it

## What is true now

`src/commands/command-pin-gaps.md`, as 77.4 leaves it. In the paragraph "Blast-radius holes" the invariant reads, as 77.4 pins it: "the **invariant** — a recorded finding that the sweep reaches the task's own target, so a reader can tell a working pattern from a broken one — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found." The paragraph that opens "The walk answers it." is outside that edit and reads: "The command reads the task, its task spec, and the code the task lands in, following named references to the leaf — depth along named edges, never a sweep across unrelated branches — and it walks what the orchestrator will do with the task".

The walk sentence reads the tree as it stands. A task runs after every open task above it, so its "what is true now" is the code as they leave it, as `docs/what-a-task-carries.md` § "What a spec holds" says.

## What must be true after

In the paragraph that opens "The walk answers it.", the first sentence reads:

"The command reads the task, its task spec, and the code the task lands in as every open task above it leaves it, following named references to the leaf — depth along named edges, never a sweep across unrelated branches — and it walks what the orchestrator will do with the task: how the planner would build a plan for it against this code, and how the reviewer would judge the implementation that comes back."

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it tells a reader to take a task's "what is true now" from the tree as it stands, where an open task above the task changes it.

**Sweep:**
```
grep -rn "code the task lands in" src docs CLAUDE.md --include="*.md"
```

**Finding.** The search reaches the sentence above, the target, and no other file. The command's `description:` says "the code it lands in" and is a skill description at its own level, which this task leaves as it is.

# 77.9 — "Decompose existing" points at the engine's definition of a task spec

## What is true now

`src/skills/roadmap-decompose/SKILL.md`, hook (d) "Decompose existing", reads:

```
Register an added update-menu action: expand a vague task into a full spec (what
exists today, the exact change, files/types/methods to touch, guards).
```

The parenthesis lists what a spec holds a second time, in an older shape than `roadmap-engine`'s "What a task spec holds", which gives three parts and nothing else. "What exists today" reads as the tree on the day of writing, where the engine's "what is true now" is read from the code at the task's own turn. "Guards" fences a neighbour, where the engine says no clause fences off a neighbour by name. The skill loads `roadmap-engine`, so a reference to its paragraph resolves.

The task-spec-handling rule below the sentence names the tag, the legacy case, the split and the numbering, and refers to `roadmap-engine`'s format and sub-numbering rule; none of it leans on the parenthesis. No open task above this one edits the file.

## What must be true after

The sentence reads:

```
Register an added update-menu action: expand a vague task into a full task spec, as
`roadmap-engine`'s "What a task spec holds" defines it.
```

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it lists what a task spec holds in a shape other than the engine's, or leans on the removed parenthesis.

**Sweep:**
```
grep -rn "exists today\|expand a vague task\|Decompose existing" src docs CLAUDE.md --include="*.md"
```

**Finding.** The search reaches the parenthesis and the sentence it sits in, the target (the parenthesis breaks across a line between "what" and "exists today", so the search anchors on "exists today"), the title of hook (d) and the sentence in the same skill that names hook (d) in its update flow, which points at the action and lists nothing of a spec's contents. No document or skill restates the parenthesis.

# 77.8 — "Decompose existing" reads what exists after the open tasks above it

## What is true now

`src/skills/roadmap-decompose/SKILL.md`, hook (d) "Decompose existing", reads:

```
Register an added update-menu action: expand a vague task into a full spec (what
exists today, the exact change, files/types/methods to touch, guards).
```

"What exists today" is the tree as it stands. A task runs after every open task above it, so what exists for it is the code as they leave it, as `docs/what-a-task-carries.md` § "What a spec holds" says. No other open task edits this file.

## What must be true after

The sentence reads:

```
Register an added update-menu action: expand a vague task into a full spec (what
exists once every open task above it has run, the exact change, files/types/methods to
touch, guards).
```

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it tells a reader to take what exists for a task from the tree as it stands.

**Sweep:**
```
grep -rn "exists today\|Decompose existing" src docs CLAUDE.md --include="*.md"
```

**Finding.** The search reaches the sentence above, the target, and the sentence in the same skill that names hook (d) in its update flow, which points at the action and says nothing of when "now" is.

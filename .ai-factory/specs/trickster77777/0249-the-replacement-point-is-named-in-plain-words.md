# 78.5 — the replacement point is named in plain words

## What is true now

`docs/reserved-words.md` defines "seam" as the `[x]`/`[ ]` boundary of a roadmap, where the project lives now. `src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", names the point at which the head replaces its hand with that word: "between the two you pick the seam." A head in the field read it as any point in the window and replaced its hand in the middle of a unit of work. `docs/paired-loop.md`, § "How the memory begins, and how it survives", carries the same phrase: "Between the two the head picks the seam, asks the hand to write its snapshot".

## What must be true after

In `agent-architect`, § "Spawn once, message thereafter", the clause reads: "between the two you pick a break in the work, the end of a unit of work."

In `docs/paired-loop.md`, § "How the memory begins, and how it survives", the clause reads: "Between the two the head picks a break in the work, the end of a unit of work, asks the hand to write its snapshot".

Nothing else in either file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it names the point of the hand's replacement with a word the registry reserves for another concept.

**Sweep:**
```
grep -rn "seam" src/skills/agent-architect src/skills/architect-editor-engine src/agents docs/paired-loop.md
```

**Finding.** The search returns the one clause in `agent-architect` and the one in `docs/paired-loop.md`, each a target; the engine and the editor definition do not use the word.

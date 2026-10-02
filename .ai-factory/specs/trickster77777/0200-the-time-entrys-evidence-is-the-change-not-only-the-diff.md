# 72.1 — the time entry's evidence is the change, not only the diff

## What is true now

`src/skills/polymorphism-philosophy/SKILL.md` § "The two entries" reads: "One question, reached two ways. The **time** entry takes what a change just brought: does this change bring a second member to a kind, and was a seam cut at that arrival or not — its evidence is the diff. The **space** entry takes a named region with no change to trigger it — a module, a directory, a class — and inventories the kinds declared there (a union of two or more members, an enum, a boolean field naming a mode, a set of subclasses), asking the same question of each. A consumer skill reaches this unit through the time entry; a direct invocation, naming a region, reaches it through the space entry." The text wraps in the file at a fixed column. The word "diff" appears nowhere else in the unit.

The unit is read two ways. Invoked directly, on an area of code or logic or on closed tasks, for analysis, there is a diff: the change has landed. `roadmap-decompose-skeleton` Lens 1 loads the unit and applies its question to the target tasks, which are open `[ ]` tasks, so no diff exists; its evidence is the task text and the current code. The question's past tense, "was a seam cut at that arrival", is true only of a change that has landed; over an open task the skeleton decides whether the change will cut one. The user's own use confirms both readers: he called the skeleton on a code area and it worked.

## What must be true after

The time entry's sentence reads: "The **time** entry takes what a change just brought: does this change bring a second member to a kind, and does it cut a seam at that arrival or not — its evidence is the change, the diff where it has landed and the task that describes it where it has not."

## What breaks on contact

**Rule:** a text breaks on this change if it reads the time entry's evidence clause, or states what evidence the unit takes.

**Sweep:**
```
grep -rn "its evidence is the diff" src/ docs/ CLAUDE.md
grep -rn "time entry" src/ docs/ CLAUDE.md
grep -rn "polymorphism-philosophy" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the unit's own sentence, the task's target, and nothing else. The second reaches the unit alone: no other skill, command or doc names the time entry or its evidence. The third reaches the skeleton, `docs/sakshi-harness/skill-cycle.md` and the `CLAUDE.md` lists of skills. The skeleton's Lens 1 loads the unit once and applies its question to the target tasks, and states no evidence of its own, so it reads the new clause at run time and the open tasks it runs over are now the case the clause names. `skill-cycle.md` describes the axis by its event, "скелет вырезается в момент, когда вид обретает второго члена", and names the unit as the home of the question; it states no evidence and does not contradict the new sentence. The `CLAUDE.md` lists name the skill and nothing more. Within the unit, the sentence after the time entry's, "A consumer skill reaches this unit through the time entry; a direct invocation, naming a region, reaches it through the space entry", stays true: it names the usual route of each reader and does not speak of a direct invocation on closed tasks. The trigger paragraph speaks of the event and no evidence.

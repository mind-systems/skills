# 77.4 — the blast-radius invariant records that the sweep reaches the task's own target and no list

## What is true now

`src/commands/command-pin-gaps.md`, the bold lead-in "Blast-radius holes", gives the repair as the rule, the sweep and "the **invariant** — a recorded finding of what the sweep, run now, reaches and how each match reads against the rule, naming at minimum the task's own target among what it finds, so a reader can tell a genuinely narrow set from a broken pattern — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found." It then says "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`." No open task above this one edits the file.

That finding is a snapshot of the tree: `docs/what-a-task-carries.md` § "Blast radius: the rule, not the snapshot" says a spec records the rule that defines the affected set and never "a snapshot of what a search returned", which the planner runs itself at plan time. Its purpose clause judges a set as "narrow", a size, and `docs/counts-go-stale.md` names "how many files a sweep reaches" as a measurement a durable text does not carry.

## What must be true after

In that paragraph the invariant reads:

"the **invariant** — a recorded finding that the sweep reaches the task's own target, so a reader can tell a working pattern from a broken one — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found."

The sentence "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`." stays as it is: it is a judgement about the shape of a task, made where the whole roadmap is readable, and not a count written into a spec.

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it asks a spec to record what a sweep reaches beyond the task's own target, or how large the reached set is.

**Sweep:**
```
grep -rn "run now\|narrow set\|how each match\|too large to enumerate" src docs --include="*.md"
grep -rn -i "blast-radius\|blast radius" src docs --include="*.md" -l
```

**Finding.** The first search reaches only the invariant and the "too large" sentence in this paragraph, the targets. The second reaches `src/skills/roadmap-engine/SKILL.md`, which names blast-radius detail as living in the task spec and asks no record of a sweep; `docs/sakshi-harness/skill-cycle.md`, which describes the class's record as "записью того, что поиск достигает цели самого таска" and so agrees; and `docs/what-a-task-carries.md` § "Blast radius: the rule, not the snapshot", which holds the rule and the sweep in the spec and no snapshot, and agrees.

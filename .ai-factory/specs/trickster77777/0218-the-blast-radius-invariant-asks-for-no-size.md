# 77.4 — the blast-radius invariant asks for no size

## What is true now

`src/commands/command-pin-gaps.md`, the bold lead-in "Blast-radius holes", gives the repair as the rule, the sweep and "the **invariant** — a recorded finding of what the sweep, run now, reaches and how each match reads against the rule, naming at minimum the task's own target among what it finds, so a reader can tell a genuinely narrow set from a broken pattern — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found." It then says "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`."

The purpose clause judges a set as "narrow", a size, and so asks the writer of a spec to say how big the reached set is. `docs/counts-go-stale.md` names "how many files a sweep reaches" as a measurement a durable text does not carry.

## What must be true after

In that sentence the purpose clause reads:

"… naming at minimum the task's own target among what it finds, so a reader can tell a working pattern from a broken one — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found."

The sentence "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`." stays as it is: it is a judgement about the shape of a task, made where the whole roadmap is readable, and not a count written into a spec.

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it asks a finding, an invariant or a report of a sweep to say how large the reached set is.

**Sweep:**
```
grep -rn "narrow set\|too large to enumerate" src docs --include="*.md"
grep -rn -i "blast-radius\|blast radius" src docs --include="*.md" -l
```

**Finding.** The first search reaches only the invariant and the "too large" sentence in this paragraph, the targets. The second reaches `src/skills/roadmap-engine/SKILL.md`, which names blast-radius detail as living in the task spec and asks nothing of size; `docs/sakshi-harness/skill-cycle.md`, which describes the class as "записью того, что поиск достигает сейчас", a record of what the search reaches, and carries no size word, so it stays true; and `docs/what-a-task-carries.md` § "Blast radius: the rule, not the snapshot", which says a spec "never records" a snapshot of what a search returned, a standing tension with a recorded finding of what the sweep reaches that this task leaves as it is.

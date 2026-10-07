# 77.2 — the doc that governs a spec's shape says what exact values are and leaves out the measurement

## What is true now

`docs/what-a-task-carries.md` § "What a spec holds" reads: "What a spec holds follows from who reads it: what is true now, read from the code with exact values, so the planner does not re-derive it; what must be true after, in the code's own terms — which file, which text, which value; and what breaks on contact. Three parts, and none of them is a check. The reviewer already holds the spec and already does the checking; a spec that also says how to verify hands the implementer a job that was never the implementer's, and a planner turns each such passage into a task in the plan — checking work, written twice, carried out by the wrong reader the first time."

It does not say what an "exact value" is or that a measurement of the tree is not held. `docs/counts-go-stale.md` names such a measurement as what a durable text does not carry, and `roadmap-engine`'s "What a task spec holds" mirrors this paragraph; docs lead, so the doc carries the change before the engine does.

## What must be true after

The paragraph reads in full:

"What a spec holds follows from who reads it: what is true now, read from the code with exact values — the code's own values, a literal, a symbol, a type, a path — so the planner does not re-derive it; what must be true after, in the code's own terms — which file, which text, which value; and what breaks on contact. Three parts, and none of them is a check. The reviewer already holds the spec and already does the checking; a spec that also says how to verify hands the implementer a job that was never the implementer's, and a planner turns each such passage into a task in the plan — checking work, written twice, carried out by the wrong reader the first time. A measurement of the tree is not held either: a count is false before the task is reached ([counts-go-stale](counts-go-stale.md))."

Nothing else in the doc changes. The wording agrees with the engine's change in meaning: the code's own values and the measurement excluded with the same reason.

## What breaks on contact

**Rule:** a text breaks on this change if it restates what a spec holds with another meaning of "exact values", or lists what a spec excludes as complete without the measurement.

**Sweep:**
```
grep -rn "What a spec holds\|exact values" docs src --include="*.md"
grep -rn "what-a-task-carries" docs src CLAUDE.md --include="*.md"
```

**Finding.** The first search reaches the paragraph, the target; the engine's "What a task spec holds", which mirrors it and has its own task; and `src/commands/command-pin-gaps.md`, which points at the engine's paragraph and does not restate it. The second reaches `docs/names-and-reasons-not-laws.md`, whose list of what a spec holds names the parts and what is left out and stays true; `docs/philosophy/principles-at-their-moment.md`, which cites a different section of the doc; the pointer in `docs/sakshi-harness/skill-cycle.md`; and the `CLAUDE.md` row, which describes the shape and what it excludes and stays true.

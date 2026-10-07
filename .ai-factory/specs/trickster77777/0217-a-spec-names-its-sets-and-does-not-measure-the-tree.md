# 77.3 — the engine's paragraph says what exact values are and leaves out the measurement

## What is true now

`src/skills/roadmap-engine/SKILL.md`, the bold lead-in "What a task spec holds", reads: "three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, pinned rather than hedged. Nothing else means, concretely: no clause is a check that the instruction was carried out, which belongs to the review the orchestrator already runs; no clause is a position in the file — each states what the artifact must hold, never where to write it; and no clause fences off a neighbour by name — scope is stated positively, as what the task changes, never as a prohibition standing in for it."

No open task above this one edits the engine, so its "what is true now" is the engine as it stands. It names the implementer as the one who does not re-derive it, where `docs/what-a-task-carries.md` and the pipeline name the planner, who reads the spec to its leaf while the implementer works from the plan. "Exact values" is not defined, and a writer reads it as asking for the size of a set among the values. The "Nothing else means" list names checks, positions and fences and holds no measurement of the tree, which `docs/counts-go-stale.md` names as the thing a durable text does not carry.

## What must be true after

The paragraph reads in full:

"**What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values — the code's own values, a literal, a symbol, a type, a path — so the planner does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, pinned rather than hedged.
Nothing else means, concretely: no clause is a check that the instruction was carried out, which belongs to the review the orchestrator already runs; no clause is a position in the file — each states what the artifact must hold, never where to write it; no clause is a measurement of the tree — a count is false before the task is reached; and no clause fences off a neighbour by name — scope is stated positively, as what the task changes, never as a prohibition standing in for it."

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it restates what a task spec holds with a different meaning of "exact values", or asks a spec to hold a measurement of the tree.

**Sweep:**
```
grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md
grep -rn "What a task spec holds\|exact values\|Nothing else means" src docs --include="*.md"
```

**Finding.** The first search reaches the engine's callers; none of them restates the paragraph, and each depends on the engine only for format and flow. The second reaches the paragraph, the target; `src/commands/command-pin-gaps.md`, which points at the paragraph and says it is "not restated here", so it stays; and `docs/what-a-task-carries.md` § "What a spec holds", which says what is true now is "read from the code as every open task above it leaves it, with exact values", and that "A measurement of the tree is not held either: a count is false before the task is reached". That document carries the same exact-values and measurement changes in its own voice, from 77.2, which this task follows.

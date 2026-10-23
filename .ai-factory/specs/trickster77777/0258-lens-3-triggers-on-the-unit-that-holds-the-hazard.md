# 90.1 — Lens 3 triggers on the unit that holds the hazard

## What is true now

`src/skills/roadmap-decompose-skeleton/SKILL.md`, "Lens 3 — Concurrency", fires "for a **heavy** task (the 45–80 min wall-clock kind) that touches **≥2 of** three hazard classes" — async I/O, a stateful buffer or event queue, a lifecycle — and splits out a contract-task: the invariant's definition plus test scenarios per concurrent caller, no production code, ahead of the implementation task. The lens ends in a bullet headed "Restraint": never split a simple task, even one that nominally touches two classes, into a contract-task. The same bullet carries an example under the label "Canon (m37)": `clearHeap()` traded double-commit for silent loss, `drainHeap()` with a dedup-key merge, buffered winning, fixed it, and had the drain-and-merge invariant been a contract-task first it would have been caught at plan review instead of in the field.

The `description:` says the skill extracts "no-prod-code contract tasks for surfaces mixing async I/O + stateful buffer + lifecycle".

The trigger is the task, a whole surface, while the hazard lives in one unit of it, and in the field the contract-task was cut over the whole mixed surface. What a decomposer gets from the lens is a skeleton whose bodies do not run and a red suite over it, so none of that suite's assertions has ever run. Whether it covers the wrong implementations of the next task can be judged only by imagining them, and imagination has no floor: each review imagines another wrong implementation that would pass.

## What must be true after

Lens 3 fires on the unit that holds the lifecycle hazard together with async I/O or a stateful buffer. A unit is a part of a task's surface, not a task. The lens produces the contract-task for that unit; cutting the rest of the surface into tasks stays with `roadmap-decompose`'s atomicity. The clause "heavy task (the 45–80 min wall-clock kind)" is gone.

The lens carries the reason. A contract-task is a skeleton and a red suite whose assertions have never run, so its coverage is judged by imagining wrong implementations, and imagination has no floor. That is the price of this lens's contract-task. The rest of the surface is built with its tests, and a test that runs has a floor.

The drain-and-merge example stays in the lens as a story told whole, as what the price buys: what the first fix traded, what fixed it, and that a contract-task first would have caught it at plan review instead of in the field. The label "Canon (m37)" goes. The "Restraint" bullet goes with the move: with the trigger on the unit there is nothing left for it to guard. The `description:` follows: its sentence on contract tasks names the unit that holds the lifecycle hazard together with async I/O or a stateful buffer in place of "surfaces mixing" the three hazard classes, and the field stays within its limit.

## What breaks on contact

**Rule:** a text breaks on this change if it reads Lens 3's trigger as the task or as a surface, or points at the restraint bullet, the wall-clock clause or the label "Canon (m37)".

**Sweep:**
```
grep -n -i -E "heavy|surface|simple task|wall-clock|Canon|Restraint" src/skills/roadmap-decompose-skeleton/SKILL.md
```

**Finding.** The search returns Lens 3, its restraint bullet and the `description:` sentence on "surfaces mixing"; each is a target above. The other hits stay. "Heavy" and "hazardous" in the `description:`, the opening and the closing list of what not to do name the skill's reach across all three lenses. "Surface" in Lens 1, the opening's question about a hazardous concurrent surface and the shared type surfaces are not Lens 3's trigger. The restraint in Lens 1 and the label "Canon (m36)" in Lens 2 are other lenses'.

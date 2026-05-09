---
name: roadmap-decompose atomicity problem and solution
description: Why tasks in roadmap-decompose keep bundling multiple concerns, and the deployability test that fixes it
type: project
---

# roadmap-decompose: Atomicity Problem and Solution

**Date:** 2026-05-09
**Source:** conversation context

## Key Findings

- The existing "one concern / one reason to revert" rule in the skill is a declaration without an enforcement mechanism — it doesn't prevent mixed tasks.
- The only reliable atomicity criterion is: **"Can the first half be deployed without the second half and still make sense?"** If yes → split.
- File count and verb count are too noisy to use as criteria — rejected.
- The fix is a mandatory **Atomicity Gate** step after each task description is drafted, before it is saved.

## Details

### How concerns slip in

Three recurring patterns observed in practice:

1. **"While I'm here"** — writing a component task, author notices a service method is also needed and adds it inline. Example: `exitSubscription` in `BrokerApiService` was bundled into the orders panel component task.
2. **Mode bundling** — create/view modes of a component feel like one thing but are sometimes independently shippable.
3. **No verification pass** — once a task is written and saved, nobody re-reads it with the atomicity question in mind.

### The deployability test

Single question, applied after every drafted task description:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two tasks, then apply the gate to each half recursively.
If **no** → the task is atomic, save it.

"Make sense" means: the partial change compiles, doesn't break existing functionality, and delivers some independently observable value (even if small).

### Where to add it in the skill

- **Mode 1, Step 1.3** — after drafting each milestone in the initial roadmap generation, before writing to file: apply gate, split if needed.
- **Mode 2, Step 2.4** — after drafting each new task in update mode: apply gate, split if needed.

Label it **Step 1.3.1** and **Step 2.4.1** respectively. The gate question should appear verbatim in the skill body so the agent always uses identical wording.

### Rejected alternatives

- **File count heuristic** ("more than 2 files = not atomic") — too noisy; legitimate atomic tasks often touch 3+ files (e.g. adding a field to a model, service, and component together).
- **Verb count heuristic** ("more than 1 action verb = not atomic") — too restrictive; a single concern can require multiple verbs to describe accurately.

## Open Questions

- Should the gate also run retroactively when `/decompose check` scans existing unchecked tasks? Could flag known violations without requiring a full rewrite pass.

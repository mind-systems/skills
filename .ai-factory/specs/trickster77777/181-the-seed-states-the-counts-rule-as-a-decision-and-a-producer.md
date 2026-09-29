# 65.2 — the buffer seed states the counts rule as a decision and a producer

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, under `## Method`, holds the bold-led entry **Standing entry — the counts rule**, which reads: "Keep a contract, delete a census: a number stays in a durable artifact only where the sentence would still read true after someone adds a member without touching it; where it would not, state the rule instead of the tally. Date a measurement instead of asserting it as permanent. Two counts that disagree are not reconciled against each other — ask which member is missing." The text wraps in the file at a fixed column. The entry says nothing of specs.

`docs/counts-go-stale.md` now holds a different account: a number someone decided stays, a measurement of the current tree goes whether dated or not and what produces it is written instead, and two counts that disagree are never reconciled. The entry's "contract" and "census" vocabulary and its "Date a measurement" sentence belong to the account the doc has left. `agent-architect/SKILL.md`, in "Spawn once, message thereafter", reads the seed once at founding and has a new buffer copy it whole.

## What must be true after

The entry keeps its bold lead-in, **Standing entry — the counts rule.**, and its body reads: "A number someone decided is written: it stays true however the tree grows. A measurement of the current tree is not written, dated or not — write what produces it, the rule or the search that gives it fresh each time. A spec least of all carries a number measuring the tree: tasks run one after another, and each one changes the tree the next was written against, so such a number in a queued spec is false before the orchestrator reaches it, and the orchestrator cannot execute a spec whose facts no longer hold. Two counts that disagree are not reconciled against each other; ask which member is missing." It points to no doc and carries no tally and no date of its own.

## What breaks on contact

**Rule:** a text breaks on this change if it depends on the entry's wording, or restates the entry's old account as live guidance.

**Sweep:**
```
grep -rln "census\|Date a measurement\|counts rule" src/ docs/ CLAUDE.md .ai-factory/notes
```

**Finding.** The search reaches the seed itself, the task's own target. It reaches one architect buffer under `.ai-factory/notes`, which uses the words "census" and "counts rule" in prose of its own and holds no copy of the old entry. A buffer founded from the old seed does hold a copy of it, made at its founding: a record of what the seed said then, a memory its head alone writes, and not this task's to edit. The tasks that rework the architect's founding read the seed as the source of a new buffer and edit none of it. It reaches no skill, no command and no doc besides the seed; `agent-architect/SKILL.md` names the seed's path and the copy-whole rule, and reads none of the entry's wording. `docs/counts-go-stale.md` states the account the new entry follows and holds none of the old fragments.

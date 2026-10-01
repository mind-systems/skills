# 66.4 — the counts entry opens with its scope

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, under `## Method`, holds **Standing entry — the counts rule.**, which opens "A number someone decided is written: it stays true however the tree grows. A measurement of the current tree is not written, dated or not — write what produces it, the rule or the search that gives it fresh each time." and goes on to the queued spec, the reading of a stale number, and two counts that disagree. The text wraps in the file at a fixed column.

Read as written, the opening is a ban wherever a number appears. Architects in another repository applied it to plain conversation and stripped numbers from speech. The reason the entry gives — a number in a queued spec is false before the orchestrator reaches it, and the orchestrator cannot execute a spec whose facts no longer hold — covers only text that is read later by someone who cannot ask back. `docs/counts-go-stale.md` scopes itself to "a number in a durable artifact", and the entry carries no scope.

The user's ruling, which he confirmed in this chat: "скилы, это не макросы, которые обязательно надо выполнить, это просто модификаторы поведения." A rule applies where its reason holds.

## What must be true after

The entry keeps its bold lead-in, **Standing entry — the counts rule.**, and its body opens with this sentence, directly after the lead-in: "It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply." The entry then reads, wrapped at the file's own column:

> **Standing entry — the counts rule.** It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply. A number someone decided is written: it stays true however the tree grows. A measurement of the current tree is not written, dated or not — write what produces it, the rule or the search that gives it fresh each time. A spec least of all carries a number measuring the tree: tasks run one after another, and each one changes the tree the next was written against, so such a number in a queued spec is false before the orchestrator reaches it, and the orchestrator cannot execute a spec whose facts no longer hold. A number met in a spec, a plan or a report is read as an order of magnitude; one that has gone stale is not a defect to correct, count again or stop on. Two counts that disagree are not reconciled against each other; ask which member is missing.

## What breaks on contact

**Rule:** a text breaks on this change if it states the counts rule with no scope, so that it now disagrees with the entry, or if it depends on the entry's opening wording.

**Sweep:**
```
grep -rn "counts rule" src/ docs/ CLAUDE.md
grep -rn "durable artifact" src/ docs/ CLAUDE.md
grep -rn "measurement of the current tree" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the entry itself, the task's own target. The entry is read by every new buffer, since the founding passage of `agent-architect` copies the seed whole, and by every living buffer through the refresh at rehydration, which matches a standing entry by its bold lead-in and takes the seed's text where the two differ; the lead-in does not change, so a living buffer receives the new opening at its next rehydration. The editor holds no seed and reads the founded buffer whole, so it holds the opening too. The second and third reach `docs/counts-go-stale.md` and the `CLAUDE.md` row that describes it, both of which state the rule for "a number in a durable artifact" and agree with the new opening. `agent-architect` mentions a number only where a work-order pins a value, which is a decision, and `editor.md` states no rule on counts. Nothing in the seed, in `agent-architect`, in `editor.md` or in the doc states the rule without a scope, apart from the entry's own opening.

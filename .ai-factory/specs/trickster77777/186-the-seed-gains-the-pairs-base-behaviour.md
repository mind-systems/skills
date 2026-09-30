# 66.1 — the seed gains the pair's base behaviour

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, under `## Method`, holds a placeholder line in angle brackets and bold-led entries. **Standing entry — the counts rule.** reads: "A number someone decided is written: it stays true however the tree grows. A measurement of the current tree is not written, dated or not — write what produces it, the rule or the search that gives it fresh each time. A spec least of all carries a number measuring the tree: tasks run one after another, and each one changes the tree the next was written against, so such a number in a queued spec is false before the orchestrator reaches it, and the orchestrator cannot execute a spec whose facts no longer hold. Two counts that disagree are not reconciled against each other; ask which member is missing." **Standing entry — what a spec holds.** follows it, and the section after is `## Orientation`. The text wraps in the file at a fixed column.

The counts entry has the writing half of `docs/counts-go-stale.md` and not the reading half: the doc says a figure that does appear is read as an order of magnitude and never failed on, and the seed says nothing of reading one. More of the pair's base behaviour is in no seed and so in no new buffer: a rule states the behaviour and stops, with no sentence for each case it excludes; a task is not retold in the code; and the orchestrator's commit takes the whole tree — `_git_commit` in `orchestrator/orchestrator/main.py` runs `git add -A`, so whatever the pair leaves uncommitted in a repository while a queue runs there lands inside a task's commit.

`docs/paired-loop.md` § "Where the pair's behaviour lives" states that the behaviour both halves must keep holding lives in the buffer and enters every new one through the seed, and the user's ruling on the hand is "для редактора это ещё важней, чем для архитектора, тк он пишет."

## What must be true after

In the counts entry, the sentence "A number met in a spec, a plan or a report is read as an order of magnitude; one that has gone stale is not a defect to correct, count again or stop on." stands directly after "…the orchestrator cannot execute a spec whose facts no longer hold." and before "Two counts that disagree are not reconciled against each other; ask which member is missing." Nothing else in the entry changes.

Three standing entries follow **Standing entry — what a spec holds.** and precede `## Orientation`, each in the same shape, a bold lead-in and then the body, separated from its neighbours by a blank line. They read, verbatim, wrapped at the file's own column:

> **Standing entry — state the behaviour and stop.** A rule says what happens and ends there: no sentence for each case it excludes, no guard against its own misuse. A rule or a fix that needs guards against its own machinery is the wrong one.

> **Standing entry — a task is not retold in the code.** A spec's reasons are for whoever plans, and the code keeps none of them. A task says what must be true and what to delete or link; it never asks for a comment carrying its reasoning, a skeleton's contract or its scope. A comment in code says only what a reader would get wrong from the code alone, where the reader meets it, in a line or three.

> **Standing entry — the orchestrator's commit takes the whole tree.** While it runs a queue in a repository, leave nothing uncommitted there, or it lands inside a task's commit.

## What breaks on contact

**Rule:** a text breaks on this change if it reads the seed, or if it states one of these behaviours in a way that disagrees with the new text.

**Sweep:**
```
grep -rn "buffer-seed" src/ docs/ CLAUDE.md
grep -rn "order of magnitude" src/ docs/ CLAUDE.md
grep -rn "add -A" orchestrator/orchestrator
grep -rn -i "guardrail" src/skills/agent-architect src/agents
```

**Finding.** The first search reaches the founding passage of `agent-architect`, which copies the seed whole into a new buffer, so the entries reach every buffer founded afterwards; a buffer founded earlier holds none of them until the head refreshes from the seed, which the next task describes. The editor holds no seed and reads the founded buffer whole, so it holds the entries too. The second reaches `docs/counts-go-stale.md` alone, whose reading rule the new sentence states in other words without disagreeing, and whose "never fail anything on arithmetic" the sentence's "not a defect to … stop on" matches. The third reaches the places where `orchestrator/orchestrator/main.py` stages with `git add -A`, the commit function and the step before review, the ground of the commit entry. The fourth reaches the sentence in `agent-architect` that has a work-order state "what NOT to touch" and the sentence in `editor.md` on pinning "every value, path, and guardrail". Those address an order to the hand, where a boundary is drawn from what the drawer can see; the new entry on stating the behaviour speaks of a rule written into a skill, a doc or a spec, and does not reach an order's boundary, but a reader could take it to, which a later task may want to make explicit. No skill, command or doc states that a task is not retold in the code, that the orchestrator's commit takes the whole tree, or how a stale figure is read, so nothing else disagrees with the entries.

# roadmap-prune — Overview

## What it solves

A roadmap accumulates. After 50+ completed tasks the file becomes noise: too long to
scan, too expensive to load into context, too granular to communicate architecture.
But deleting the history loses the decisions behind the code.

`roadmap-prune` moves completed tasks out of ROADMAP.md into ARCHITECTURE.md —
compressed into named features with commit hashes as GPS coordinates. The tasks
disappear from the roadmap; the history is preserved in a form that's actually useful.

---

## The two artifacts it maintains

### ROADMAP.md — stays short

Before:
```markdown
## Milestones
- [x] gRPC client — grpc-swift 2 client connecting to core...
- [x] Watcher stream listener — Subscribe to watcher gRPC streams...
- [x] GrpcBroker — new BrokerProtocol implementation...
... (40 more tasks)
- [ ] GUI foundation
- [ ] Live monitoring dashboard
```

After:
```markdown
## Milestones
- [ ] GUI foundation
- [ ] Live monitoring dashboard
```

No Completed table. The tasks are gone — they live in ARCHITECTURE.md now.

### ARCHITECTURE.md — gains a Features table

```markdown
## Features

| Feature | Hashes |
|---------|--------|
| **Execution** | |
| UserExchange model | 9e1b3f5 |
| OrderBook stream | c7d4a88 |
| **Transport** | |
| gRPC transport | a3f9c12 |
| **Internal** | |
| PLR worker refactor | 7a2d1c9 |
| Roadmap drop history | abc1234 |
```

Rows are grouped by domain — natural product boundaries of the codebase. Bold rows are
section headers with an empty Hashes cell. Features within a domain are adjacent, making
the table a navigational index rather than a flat list.

Hashes accumulate over time — when a feature gets a structural change, a new hash is
appended. A feature with one hash was born and never structurally changed. A feature
with several hashes has a recorded evolution.

```markdown
| gRPC transport | a3f9c12 e04b91c |
```

---

## How tasks become features

Before grouping, every completed task gets classified by one question:

> "Could you write an e2e test for this that didn't exist before?"

If yes — it's a feature. A feature is any behaviour that can be verified end-to-end: a user
action, a service-to-service contract, a data pipeline output, a server integration.
If no — it's internal.

Three outcomes:

| Outcome | Signal | Result |
|---------|--------|--------|
| **New feature** | New e2e scenario becomes possible | New row in Features table |
| **Extended feature** | Existing e2e scenario gains new parameters or coverage | New hash appended to existing row |
| **Internal only** | No new e2e behaviour — refactor, cleanup, dep fix, arch change | Hash recorded in drop history only |

Tasks that share the same feature outcome are grouped together — one group, one row, one name.

Feature names describe what the system does from the operator's perspective, in 2–5 words.
Phase headers from the roadmap are never used as feature names: phases organise work,
features describe capabilities.

---

## Why commit hash, not date

A date like `2026-03-01` covers 20 commits. A hash like `c7d4a88` points to one
state of the world. From that hash you recover the full context of the moment:

```bash
git show c7d4a88                        # the diff that completed the feature
git show c7d4a88:.ai-factory/ROADMAP.md # what was open and closed at that moment
git log --oneline c7d4a88~5..c7d4a88   # surrounding commits
git diff c7d4a88~1 c7d4a88 -- .ai-factory/plans/  # plans committed in that window
```

The agent sees the tasks that were closing around that hash — no need to store them
in the table. The patch shows the neighborhood.

---

## What a hash represents

Each hash is the "Roadmap update" commit where the **last task of a feature batch**
was marked `[x]` in ROADMAP.md. The convention is: when a set of tasks closes, the
developer marks them `[x]` and commits with message "Roadmap update". That commit
hash is the GPS coordinate — it captures the exact moment the feature was declared done.

A feature that was never revisited has one hash. A feature that was refactored later
gets a second hash appended. The first hash is only erased when nothing of the original implementation remains —
regardless of whether that happened in one refactor or gradually over several commits.

---

## Relationship to temporal-tree

`roadmap-prune` produces the Features table that `temporal-tree` consumes. When an
agent needs to understand when and why a feature was built, it looks up the feature in
ARCHITECTURE.md, takes a hash, and reconstructs the decision moment from git.

Without `roadmap-prune`: the history is buried in 50+ tasks inside ROADMAP.md.
With `roadmap-prune`: `temporal-tree` gets a hash and goes straight to the source.

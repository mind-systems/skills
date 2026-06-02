# temporal-tree — Overview

## What it solves

`detangle` climbs the spatial tree — leaf → branch → trunk → forest. It answers
*where* an element lives in the architecture.

`temporal-tree` climbs in the opposite dimension — it answers *when* and *why*. Given
a feature, it reconstructs the moment it was born: the decisions that shaped it, what
was open and closing around it, and what the codebase looked like at that exact point.

Use it when the spatial context is clear but the reason behind a pattern is not.

---

## The entry point

`ARCHITECTURE.md` contains a Features table maintained by `roadmap-prune`:

```markdown
## Features

| Feature | Hashes |
|---------|--------|
| gRPC transport | a3f9c12 e04b91c |
| OrderBook stream | c7d4a88 |
| PLR worker refactor | 7a2d1c9 |
```

Each hash is a GPS coordinate — the commit where a batch of tasks for this feature
was closed in ROADMAP.md. The first hash is the birth. Subsequent hashes are
structural changes. One hash means the feature was born and never structurally changed.

---

## Climbing the temporal tree

### Step 1 — Identify the feature

From the element under discussion, identify which feature in ARCHITECTURE.md it
belongs to. If it spans multiple features, start with the most recent one.

### Step 2 — Pull the birth patch

```bash
git show <hash>
```

This shows the diff that closed the last task of the feature's birth batch. The patch
reveals what was added, what was removed, and what the code looked like at that moment.

### Step 3 — Read the roadmap at that moment

```bash
git show <hash>:.ai-factory/ROADMAP.md
```

The roadmap snapshot shows which tasks were freshly closed (just landed) and which
were still open (next in line). The boundary between them is where the feature sits
in the project's timeline.

### Step 4 — Read surrounding commits

```bash
git log --oneline <hash>~5..<hash>
```

Shows the 5 commits leading up to this hash. Often reveals related changes that
landed together — proto updates, test coverage, doc updates.

### Step 5 — Find the plan

```bash
git diff <hash>~1 <hash> -- .ai-factory/plans/
```

If a plan was committed in the same window, it appears here. Plans contain the
reasoning behind implementation choices — the "why this approach" that code alone
doesn't show.

---

## Reading a multi-hash feature

When a feature has multiple hashes:

```
| gRPC transport | a3f9c12 e04b91c |
```

- `a3f9c12` — birth: read this to understand the original design
- `e04b91c` — structural change: read this to understand what shifted and why

The gap between them is the evolution. Reading both patches tells the full story:
what was intended originally, and what reality forced to change.

---

## When to use this

After `detangle` has identified the trunk-level invariant, use `temporal-tree` when:

- The pattern feels arbitrary and the code doesn't explain why
- You are about to change something that was explicitly refactored before
- The trunk-level invariant contradicts what the code appears to be doing
- The feature has multiple hashes — something structural shifted, and you need to know what

---

## What this is NOT for

- Understanding current behavior — always read the current file first. The patch
  explains *why*; the file says *what*.
- Every task — most changes don't need temporal context. Use when the reason matters.
- Replacing `detangle` — spatial and temporal context are complements, not alternatives.

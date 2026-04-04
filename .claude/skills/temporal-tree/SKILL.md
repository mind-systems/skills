---
name: temporal-tree
description: >-
  Reconstructs the decision context behind a feature by walking its commit hashes through git
  history — reads the ## Features table from ARCHITECTURE.md (produced by roadmap-prune) and
  surfaces the patch, roadmap snapshot, surrounding commits, and plan files at each hash. Invoke
  after detangle when the reason behind a pattern is non-obvious or a change touches something
  previously refactored.
argument-hint: "[element or topic]"
allowed-tools: Read Bash(git *) Glob Grep
---

# Temporal Tree

`detangle` climbs the spatial tree — leaf to branch to trunk to forest. It answers *where* an
element lives in the architecture. `temporal-tree` climbs in the opposite dimension. Given the
element under discussion, locate its feature in ARCHITECTURE.md, pull the commit hash that marks
its birth, and reconstruct the decision context: the patch, the roadmap snapshot at that moment,
the surrounding commits, and the plan files that record the reasoning. Use this skill after
detangle has resolved the spatial context and the *why* behind a pattern still isn't clear.

---

## Before you start

Read `.ai-factory/ARCHITECTURE.md` and locate the `## Features` table. That table is the entry
point for every temporal walk — it maps feature names to space-separated commit hashes anchored
by `roadmap-prune`.

If no `## Features` table exists in ARCHITECTURE.md (or if ARCHITECTURE.md itself does not exist),
stop and tell the user: run `roadmap-prune` first to build the Features table before using
this skill.

---

## Step 1 — Identify the feature

From the element under discussion (the argument `$ARGUMENTS`, or the element named in the
conversation), find which row in the `## Features` table it belongs to. Extract the hashes from
the Hashes column.

If the element spans multiple feature rows, start with the most recent one — its hashes are
the most directly relevant.

If no matching feature row is found, stop and tell the user: the element either predates the
Features table or was never pruned into it. The roadmap may contain older `[x]` tasks that
cover it — suggest running `roadmap-prune` to anchor them.

---

## Step 2 — Pull the birth patch

Run `git show` on the first (leftmost) hash in the Hashes cell. This is the diff that closed
the feature's birth batch — the moment the last task of the first implementation landed.

```bash
git show <first-hash>
```

Read the patch. Note what files were added or modified, what was removed, and what the code
structure looked like at that exact moment. This is the original design surface.

---

## Step 3 — Read the roadmap at that moment

Run `git show` with a path argument to read ROADMAP.md as it existed at the birth hash.

```bash
git show <first-hash>:.ai-factory/ROADMAP.md
```

The snapshot reveals which tasks had just been marked `[x]` (landed with this batch) and which
were still `[ ]` (next in line). The boundary between them is where this feature sits in the
project timeline — what was being built before it, and what came immediately after.

---

## Step 4 — Read surrounding commits

Run `git log --oneline` to show the five commits leading up to and including the birth hash.

```bash
git log --oneline <first-hash>~5..<first-hash>
```

These commits reveal related changes that landed in the same window — proto updates, migrations,
config changes, dependency additions. A feature rarely lands in isolation; the surrounding
commits show what it depended on and what it enabled.

---

## Step 5 — Find the plan

Run `git diff` to detect whether a plan file was committed in the same window as the birth hash.

```bash
git diff <first-hash>~1 <first-hash> -- .ai-factory/plans/
```

If the diff shows added plan files, read them:

```bash
git show <first-hash>:<plan-path>
```

Plans contain the reasoning behind implementation choices — the "why this approach" that code
alone does not show. Also check for plan-reviews committed in the same window:

```bash
git diff <first-hash>~1 <first-hash> -- .ai-factory/plan-reviews/
```

Read any plan-review files that appear. Plan-reviews record the constraints and trade-offs the
reviewer added before the implementation was accepted.

---

## Step 6 — Multi-hash features

When a feature has multiple space-separated hashes, repeat Steps 2–5 for each hash in order.

- First hash = birth: the original design
- Subsequent hashes = structural changes: what shifted and why

After reading all patches and their surrounding context, synthesize: what was the original
intent at birth, what shifted in each subsequent hash, and what forced the change — external
constraint, new requirement, or discovered flaw. The gap between patches is the evolution.
Reading birth and change together tells the full story.

---

## Synthesis output

After completing the steps, produce a brief temporal context block:

```
Feature:  <feature name from ARCHITECTURE.md>
Birth:    <first-hash> — <one-line summary of what it introduced>
Changes:  <subsequent hashes + what shifted, if any; "none" if single-hash>
Plan:     <plan file path if found, or "none">
Timeline: <what was open and closing around the birth — one sentence>
```

This block is the reasoning foundation. Now answer the question or continue the task.

---

## What NOT to do

- Do not use temporal-tree to understand current behavior — read the current file first; the
  patch explains *why*, not *what*
- Do not invoke on every task — most changes need no temporal context; use when the reason
  matters
- Do not replace detangle — spatial and temporal context are complements, not alternatives
- Do not modify any files — this skill is read-only
- Do not fabricate hashes — if a feature is not in the Features table, say so

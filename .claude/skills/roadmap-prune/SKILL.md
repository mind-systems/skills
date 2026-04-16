---
name: roadmap-prune
description: >-
  Prunes completed tasks from ROADMAP.md by grouping them into named features,
  anchoring each feature to its commit hash in ARCHITECTURE.md, and deleting the
  pruned tasks from the roadmap. Use when ROADMAP.md has accumulated many [x] tasks
  and needs to be trimmed without losing navigational history.
argument-hint: "[path/to/ROADMAP.md]"
allowed-tools: Read Write Edit Bash(git *)
---

# Roadmap Prune

Cleans up a roadmap by collapsing completed tasks into architectural features with
commit-level precision. The tasks disappear from the roadmap; the features appear in
ARCHITECTURE.md with GPS-accurate commit hashes so the history is never lost — just
moved to the right place.

---

## Before you start

Read the target ROADMAP.md in full — do not start grouping until you have read every `[x]` task.

---

## Step 1 — Identify the pruning slice

Count all `[x]` tasks. The goal is to leave ~20 lines of active context in Milestones
(open tasks + the most recent completed tasks that still provide context for what's
coming next). Everything older than that is a candidate for pruning.

Determine the slice: tasks to prune = all `[x]` tasks except the most recent N that
provide active context. N is usually 0–5. When in doubt, prune more — the history
is preserved in git and ARCHITECTURE.md.

---

## Step 2 — Group tasks into features

Before grouping, read `.ai-factory/ARCHITECTURE.md` `## Features` table (if the file
exists) to learn what features have already been anchored. Map tasks onto existing
features first — only create a new feature when no existing one fits. If ARCHITECTURE.md
does not exist yet (first-ever prune), skip gracefully and proceed with fresh grouping.

Read the pruning slice and group tasks into features. A feature is a coherent unit
of capability that was delivered together. Grouping rules:

- Tasks that implement the same capability belong together
  (e.g. "gRPC client" + "gRPC signal stream" + "Remove `/webhooks/core` route" → **gRPC transport**)
- Tasks that set up a model + repository + endpoints belong together
  (e.g. "UserExchange model" + "UserExchange CRUD" + "registration flow update" → **UserExchange model**)
- Tasks that are explicitly marked as sub-items of a larger item belong together
- When uncertain: prefer fewer, larger features over many small ones

Name each feature in 2–5 words. The name becomes a row in ARCHITECTURE.md — it must
be meaningful enough to navigate to without reading the tasks.

---

## Step 3 — Find the commit hash for each feature

For each feature, find the commit where its last task was closed. That commit is the
GPS coordinate: it captures the moment the feature was complete enough to prune.

```bash
# Find commits that touched ROADMAP.md
git log --oneline -- .ai-factory/ROADMAP.md

# Show ROADMAP.md as it looked at a given commit
git show <hash>:.ai-factory/ROADMAP.md

# Find the commit where a specific task was first checked off
# Strategy: look at diffs on ROADMAP.md, find the commit where
# the last task of the feature changed from [ ] to [x]
git log -p -- .ai-factory/ROADMAP.md | grep -B5 "\+- \[x\].*<task-keyword>"
```

Pick the commit where the **last task of the feature** was marked `[x]`. That is the
hash to record in ARCHITECTURE.md.

---

## Step 4 — Update ARCHITECTURE.md

**4.1 — Capture the prune snapshot hash**

Before touching any files, record the current HEAD:

```bash
git rev-parse --short HEAD
```

This hash points to the last commit where ROADMAP.md still contains all the tasks being pruned. Anyone can run `git show <hash>:.ai-factory/ROADMAP.md` to restore the full picture.

**4.2 — Write Features and drop history**

Open ARCHITECTURE.md. Find or create a `## Features` section. For each feature:

- If the feature already exists → append the new hash to its Hashes cell (space-separated).
- If the feature does not exist → add a new row with the hash from Step 3.

For the drop history row: find or create it at the bottom of the Features table and append the snapshot hash from Step 4.1 (comma-separated).

Table format:

```markdown
## Features

| Feature | Hashes |
|---------|--------|
| UserExchange model | 9e1b3f5 |
| gRPC transport | a3f9c12 |
| OrderBook stream | c7d4a88 |
| PLR worker refactor | 7a2d1c9 |
| Roadmap drop history | abc1234, def5678 |
```

Use short (7-char) hashes throughout.

---

## Step 5 — Update ROADMAP.md

Delete the pruned `[x]` tasks from `## Milestones`. Do not replace them with a table —
the tasks are gone from the roadmap. Their history lives in ARCHITECTURE.md.

Keep `## Milestones` with all remaining `[ ]` tasks and the few recent `[x]` tasks
that provide active context (if any).

---

## Step 6 — Verify

Before finishing, verify:

- Every pruned task group is represented by a feature row in ARCHITECTURE.md
- Every feature row has a real, resolvable commit hash:
  ```bash
  git cat-file -t <hash>   # should output "commit"
  ```
- ROADMAP.md has no orphaned `[x]` tasks (all checked items are either deleted
  or intentionally kept as recent context)
- The Milestones section still reads coherently without the pruned tasks

---

## What NOT to do

- Do not prune `[ ]` tasks — only `[x]` tasks are candidates
- Do not invent commit hashes — find real ones from `git log`
- Do not merge unrelated features into one row to save space
- Do not delete the notes/ directory or individual note files — they are referenced
  by commit hash and must stay in the repo
- Do not update the first hash when a feature only had minor internal changes

---

## Reading the history later

When a future agent needs context on a feature:

```bash
# See the feature's patch
git show <hash>

# See the roadmap state at that moment
git show <hash>:.ai-factory/ROADMAP.md

# See plans committed around that time
git log --oneline <hash>~5..<hash>
git diff <hash>~1 <hash> -- .ai-factory/plans/
```

The first hash in a feature row is a permanent GPS coordinate. It never changes unless
the feature is completely rewritten from scratch — only erase it when nothing of the
original implementation remains.

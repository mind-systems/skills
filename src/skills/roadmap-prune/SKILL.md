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

## Step 2 — Classify, then group tasks into features

Before grouping, read `.ai-factory/ARCHITECTURE.md` `## Features` table (if the file
exists) to learn what features have already been anchored. If ARCHITECTURE.md does not
exist yet (first-ever prune), skip gracefully and proceed with fresh grouping.

### 2.1 — Classify every task

For every task in the pruning slice, ask one question:

> "Could you write an e2e test for this that didn't exist before?"

If yes — it's a feature. The Features table is the answer to "what does this system know how to do?" — a capability inventory that stays current because the system changes through the roadmap. Any verifiable interaction counts: user→system, system→system, system→external service, or a distinct internal subsystem with its own behaviour contract (e.g. structured logging with disk persistence and replay). If no — it's internal.

Based on the answer, assign one of three outcomes:

| Outcome | Signal | Action |
|---------|--------|--------|
| **New feature** | New e2e scenario becomes possible | Create a new feature row |
| **Extended feature** | Existing e2e scenario gains new parameters or coverage | Append hash to existing row |
| **Internal only** | No new e2e behaviour — refactor, cleanup, dep fix, arch change | Hash goes to drop history only — no feature row |

Rules:
- Never copy a phase or section header as a feature name. Phase headers organise work; feature names describe what the system can do.
- A refactor that enables a future feature is still internal — record it in drop history, not as a feature.
- When uncertain between new vs. extended: prefer extending an existing row.
- **Internal-only items never get a named row in the Features table.** Refactors, renames, cleanups, doc fixes, migration changes, and dependency updates all go to the drop history hash only. The only named row under **Internal** is `Roadmap drop history`.

### 2.2 — Group and name

Group tasks that share the same capability outcome. A group that spans many tasks but
delivers one operator-visible thing is still one feature row.

- Tasks that implement the same capability belong together
  (e.g. "gRPC client" + "gRPC signal stream" + "Remove `/webhooks/core` route" → **gRPC transport**)
- Tasks that are explicitly marked as sub-items of a larger item belong together
- When uncertain: prefer fewer, larger features over many small ones

Name each feature in 2–5 words from the operator's perspective (what it does, not how it's built).
The name becomes a row in ARCHITECTURE.md — meaningful enough to navigate to without reading the tasks.

Then sort the features by domain and group them under bold section headers. Features in the same
domain (e.g. all transport-layer work, all persistence work, all UI panels) should be adjacent.
Domain names reflect the product boundaries of this specific project, not generic labels.

Internal/refactor work goes last under an **Internal** header. The only rows under **Internal** are:
- Named rows for significant architectural subsystems established during this prune (e.g. a new layer pattern, a new protocol integration) — only if the subsystem has its own behaviour contract
- `Roadmap drop history` — always the last row; all maintenance work (refactors, cleanups, dep fixes, renames, doc changes) goes here as hashes, never as named rows

Example structure:

```
| Feature | Hashes |
|---------|--------|
| **<Domain A>** | |
| <What a user can do> | abc1234 |
| <What a user can do, extended> | def5678 9a3bc12 |
| **<Domain B>** | |
| <What service A delivers to service B> | c7d4a88 |
| <What the system does end-to-end> | e1f2g3h |
| **Internal** | |
| Roadmap drop history | 5d1284c |
```

Use an empty Hashes cell (`| |`) for section header rows — they are visual separators, not features.

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

Follow the table format and grouping rules from Step 2.2. Additional rules:

- Section headers are bold rows with an empty Hashes cell — pure visual separators.
- Domain names reflect the product boundaries of this specific project, not generic labels.
- Features are named from the operator's perspective (what the system can do), not from the implementation.
- `Roadmap drop history` is always the last row of the **Internal** section. All maintenance work (refactors, arch cleanup, dep fixes, renames, doc changes) is absorbed into that row's hashes only — never as a named row.
- Use short (7-char) hashes throughout.

---

## Step 5 — Update ROADMAP.md

Delete the pruned `[x]` tasks from `## Milestones`. Do not replace them with a table —
the tasks are gone from the roadmap. Their history lives in ARCHITECTURE.md.

Keep `## Milestones` with all remaining `[ ]` tasks. Additionally, always retain the
last phase header and its 2 most recent `[x]` tasks — this preserves phase numbering
continuity so agents can follow the sequence without confusion.

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

# Plan: 1.8.2 — roadmap-prune: sweep only the pruned tasks' specs; keep-recent rule removed

## Context
Fix two defects in `roadmap-prune`: the spec sweep captures/deletes every `[x]` line's spec (leaving user-kept lines with dangling `Spec:` tags), and two automatic keep-recent heuristics silently decide retention for the user. After this milestone the default prunes all `[x]` tasks, only an explicit user instruction retains a line, the last-phase-header stays as the numbering anchor, and the sweep touches only the pruned lines' specs.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Remove automatic keep-recent retentions

- [x] **Task 1: Delete Step 1's "most recent N" slice heuristic**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Rewrite Step 1 (`## Step 1 — Identify the pruning slice`, lines ~74-82). Remove the "~20 lines of active context" framing and the "all `[x]` tasks except the most recent N that provide active context / N is usually 0–5" heuristic. The slice becomes: **all `[x]` tasks** are pruned by default. State that the only way a `[x]` line is retained is an **explicit user instruction** — named either at invocation or at the confirmation step. Keep the "history is preserved in git and ARCHITECTURE.md" reassurance. Keep the step instructions-only (no rationale prose), consistent with the "What NOT to do" mandate.

- [x] **Task 2: Drop Step 6's "2 most recent `[x]` tasks" retention; keep the last-phase-header anchor**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Edit Step 6 (`## Step 6 — Update ROADMAP.md`, lines ~232-234). In the "Keep the task-holding sections…" paragraph, delete the "and its 2 most recent `[x]` tasks" clause. The **last phase header is still always retained** as the numbering anchor (the engine continues phase numbers from the file-wide maximum; deleting the last header would reset the sequence) — the header is kept even when emptied of all its tasks. Only an explicit user-named keep leaves a `[x]` task in place. Ensure the emptied-phase and emptied-direction sweep paragraphs below still read coherently: their "a phase that still holds a kept `[x]` task is not emptied" caveats now refer to user-kept tasks, not auto-retained ones — adjust that wording so it no longer implies automatic retention.

### Phase 2: Scope the spec sweep to pruned lines

- [x] **Task 3: Scope Step 5's `Spec:` capture to the pruned lines only** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Edit Step 5 item 1 (line ~214). Change "the `Spec:` tag path of every `[x]` line — both the lines being pruned and any `[x]` lines kept as recent context" to capture the `Spec:` tag paths of **the lines being pruned only**. A user-kept `[x]` line keeps both its roadmap line and its spec file untouched (its tag stays valid at HEAD). Keep verbatim: the capture-before-delete ordering, and "A `[x]` line with no `Spec:` tag contributes nothing — skip it, never synthesize a path." Do not touch Step 5 item 2 (the four-dir `rm -rf` sweep of `plans/`/`plan-reviews/`/`reviews/`/`patches/`) — it is unchanged; kept tasks' pipeline artifacts still go, reachable via the Step 4.1 snapshot hash. Item 3 (`rm -f` each captured spec path) is unchanged; it now naturally operates only on pruned lines' specs.
  Also reconcile the two trailing guard sentences that still speak of "`[x]` lines' `Spec:` tags" without distinguishing pruned from kept, so the scoped step reads coherently:
  - Step 5 trailer (line ~218): "Spec deletion goes only through `[x]` lines' `Spec:` tags — no spec directory is ever scanned or swept…" → scope to the **pruned** `[x]` lines' tags (a user-kept `[x]` line's spec is likewise never deleted). Keep the open-`[ ]` reassurance intact.
  - "What NOT to do" (lines ~295-296): "spec deletion goes only through `[x]` lines' `Spec:` tags; never touch a path an open `[ ]` line's tag names" → same scoping to the **pruned** `[x]` lines' tags. Wording coherence, not a behavior change — the sweep is correct either way.

- [x] **Task 4: Fix the stale "kept as recent context" wording in Step 7** (depends on Task 2)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 7 (`## Step 7 — Verify`, line ~262-263), the check "all checked items are either deleted or intentionally kept as recent context" now describes a removed mechanism. Reword so retention reads as explicit user instruction (e.g. "either deleted or explicitly kept by the user"). After this task, `grep -n -i "recent context\|kept" src/skills/roadmap-prune/SKILL.md` should show no surviving automatic-retention language — the capture and verify steps speak only of pruned lines and user-named keeps.

## Verification (manual, not a task)
- `grep -n -i "recent context\|kept" src/skills/roadmap-prune/SKILL.md` → the auto-retention rule is gone; capture speaks only of pruned lines.
- Dry-run mentally with one user-named keep: the delete list contains every pruned line's spec and **not** the kept line's; the kept line's `Spec:` tag still resolves at HEAD.
- Dry-run with no keeps: every `[x]` line and every captured spec goes — no silent survivors; the last phase header remains as the numbering anchor.

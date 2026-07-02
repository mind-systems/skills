# roadmap-prune: delete the pruned tasks' whole artifact trail — specs, plans, reviews

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review)

## Key Findings

- After a prune, everything a pruned task left behind is dead weight at HEAD: its spec, its plan (+ sidecar), its plan-reviews, reviews, and patches. All content stays reachable forever through the feature anchors (`git show <hash>:…`) and the drop-history snapshot; `temporal-tree` reads history, not HEAD. Yet prune currently forbids deleting spec files, and plans/reviews are cleaned by hand.
- Invert: **pruning a task deletes its artifact trail** — git-natively, so history keeps every byte. Per-task resolution, never per-directory:
  - the **spec** — the exact file the pruned line's `Spec:` tag names (wherever it lives; works across the lazy `notes/`→`specs/` migration);
  - the **orchestrator artifacts** — files matching the task's `<seq>-<slug>` prefix in the four artifact directories (`plans/` incl. the `.json` sidecar, `plan-reviews/`, `reviews/`, `patches/`), slug derived from the title the same way the orchestrator derives it.
- `notes/` as a directory is **not this skill's concern** — legacy notes are cleaned by hand, and once the roadmap family writes to `specs/`, prune only ever meets specs there via tags. The skill does not mention `notes/` at all.

## Details

### Edit 1 — delete with the prune

In the prune execution (alongside deleting the `[x]` lines from `## Milestones`), for every pruned task:

1. `git rm` the file its `Spec:` tag names (skip silently if the line carries no tag).
2. `git rm` its slug-matched files in `plans/` (both `.md` and `.json`), `plan-reviews/`, `reviews/`, `patches/`.

Only artifacts of *pruned* lines — specs and artifacts of surviving open or kept-context tasks are untouched. The prune commit removes lines and their artifact trail together; the snapshot hash recorded in the drop-history row (Step 4.1) preserves the last state where everything existed.

### Edit 2 — replace the old rule

The What-NOT-to-do line "Do not delete the notes/ directory or individual note files…" is replaced by: delete **only** the artifacts of tasks pruned in this run — the spec via its `Spec:` tag, the orchestrator artifacts via the `<seq>-<slug>` match — never sweep a directory, never touch files belonging to surviving tasks.

### Edit 3 — orphan report (report-only)

After deletion, scan `.ai-factory/specs/` for `[0-9][0-9]-*.md` files not referenced by any `Spec:` tag in the roadmap files, and the four artifact directories for slug prefixes matching no roadmap line. List them to the user as orphans — no automatic action.

### Edit 4 — the prune commit (on request, never automatic)

The run ends with all changes in the working tree and the summary report — **no commit is made**; the user reviews first. When the user says to commit (in any wording — "commit", "коммить"), make **one commit containing all the run's changes** — the trimmed roadmap, the updated ARCHITECTURE.md Features table, and every deleted artifact — with the message exactly:

```
Roadmap prune
```

Nothing else: no body, no prefixes, no co-author line, no per-file commits — the fixed message exists so the user never has to spell it out. The Step 4.1 snapshot hash is captured **before any changes** (it must point at the last state where everything pruned still existed).

### Constraints

- Verify step (Step 6) extends: every pruned task's spec and artifacts are gone; every surviving task's are present.
- `handoffs/` and `notes/` are never scanned or mentioned.
- Depends conceptually on note 54's follow-the-tag principle; safe to implement in the same queue.

## What NOT to do

- Do not delete by directory or by age — only by tag and slug of pruned lines.
- Do not auto-delete orphans — report only.
- Do not commit automatically — the user reviews the working tree first and says when.
- Do not make multiple commits or embellish the message — exactly one commit, exactly `Roadmap prune`, no questions about the message.
- Do not touch `handoffs/`, `notes/`, or `test-runs/` of surviving tasks (test-run artifacts of pruned test tasks follow the same slug rule when pruning `ROADMAP_TESTS.md`).

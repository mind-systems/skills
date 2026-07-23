# task-rescue: sidecar rollback markers gain an iteration index (`planned:1` / `implemented:1`)

The sibling **orchestrator** repo is changing the sidecar `step` grammar. Orchestrator task 18.2 (governing spec `orchestrator/.ai-factory/specs/trickster77777/32-resume-carries-verify-iteration.md`) indexes both "artifact produced" markers — bare `"planned"` → `"planned:N"` and bare `"implemented"` → `"implemented:N"` — and **empties the bare always-valid tuple** in `_validate_sidecar_step` (clean break, no legacy branch): after 18.2 a bare `"planned"` / `"implemented"` passes validation, matches no `_detect_step` dispatch branch, and degrades to the disk heuristic. `task-rescue` is the **only skill-side writer** of these markers (per `orchestrator-artifacts` §3), and its rollbacks write the bare values. This is the paired skills-side change: write the indexed values and re-sync the grammar table so the skill's documented closed set never lies about what the orchestrator accepts.

The rescue always writes **N = 1**: both rollback depths delete *all* plan-review / review files for the slug (spec+plan depth deletes all plan-reviews; spec+plan+code depth deletes all reviews), so the next round is always 1 — the rescue never retains partial review artifacts at these depths and never needs a higher `N`. `plan_reviewed` is single-state and never indexed — it is untouched.

## Current state (grounded, verified live in `src/skills/task-rescue/SKILL.md`)

The bare markers appear at these spots (line numbers as read, may drift):

- **Depth summary block** (:240, :243): `sidecar step → "planned"` and `sidecar step → "implemented"` in the Step 4 depth menu.
- **spec + plan depth** (:295 heading "roll back to `"planned"`", :304 "Set the `step` key to `"planned"`", :310 Emit `Sidecar updated: step set to "planned"; implementer session dropped.`).
- **spec + plan + code depth** (:314 heading "roll back to `"implemented"`", :323 "Update the sidecar `step` to `"implemented"`", :326 Emit `Sidecar updated: step set to "implemented".`).
- **Closed-set table** (:353–356 preamble + :358–364 rows): the reminder already says it "mirrors `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py` — if the orchestrator's accepted set changes, update this table". Rows `| "planned" | plan-review, attempt 1 | none — always valid |` (:360) and `| "implemented" | review, iter 1 | none — always valid |` (:363).
- **Always-valid guard** (:368): "`"planned"` and `"implemented"` carry no artifact reference and always validate — write `"planned"` only when the plan `.md` is present; write `"implemented"` only when the plan `.md` is present and a non-empty working diff exists."
- **Note paragraph** (:370–375): "the flow writes only `"planned"` (spec+plan depth), `"implemented"` (spec+plan+code depth), or deletes the sidecar".
- **"Do not write" guard** (:462–465): "Do not write `"planned"` or `"implemented"` when the corresponding artifact is absent".

The referent this table mirrors is `orchestrator/orchestrator/resume.py` `_validate_sidecar_step` / `_detect_step` in their post-18.2 state.

## Change

One concern — re-sync `task-rescue`'s sidecar marker grammar to orchestrator 18.2's indexed form — one reason to revert. Bare `"planned"` → `"planned:1"` (spec+plan depth) and bare `"implemented"` → `"implemented:1"` (spec+plan+code depth) at every spot above; the two grammar rows generalise to `"planned:N"` / `"implemented:N"`, with a note that the rescue always writes **N = 1**.

- **Depth summary, both rollback procedures, and all Emit lines** carry the indexed value: `"planned:1"` / `"implemented:1"`. The Emit strings become `Sidecar updated: step set to "planned:1"; implementer session dropped.` and `Sidecar updated: step set to "implemented:1".`.
- **Closed-set table** — the two rows become `| "planned:N" | plan-review, attempt N | none — always valid |` and `| "implemented:N" | review, iter N | none — always valid |`, and a one-line note under the table records that the rescue always writes **N = 1** (all prior-round artifacts are deleted at both depths) and that the bare `"planned"` / `"implemented"` forms are retired — no longer accepted by the orchestrator.
- **Always-valid guard, Note paragraph, "Do not write" guard** — the values gain the `:1` index; the guard *conditions* are unchanged (write `"planned:1"` only when the plan `.md` is present; write `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists; never write after deleting the plan `.md`).

## Files & types

- edit: `src/skills/task-rescue/SKILL.md` — the only file changed.
- confirm-only (no edit): `src/skills/orchestrator-artifacts/SKILL.md` §3 delegates the closed set to `task-rescue`; verify the delegation line still reads true after the table update — no content edit needed.

## Guards

- **`plan_reviewed` is byte-identical.** Single-state, never indexed; its rollback depth, validation contract, and every occurrence stay untouched.
- **The reference-only rows are untouched** — `"plan_review_failed:N"` and `"review_failed:N"` (and test-mode `test_run_failed:N`) are orchestrator-contract values `task-rescue` never writes; leave them exactly as they are.
- **Guard conditions unchanged, only the written value gains the index** — the always-valid guard's plan-`.md`-present and non-empty-diff preconditions, and the "Do not write … when the corresponding artifact is absent" rule, keep their exact semantics.
- **Scope is the marker grammar only** — the repair-depth procedures (which files are deleted, `implementer`-key handling, JSON read/update/write mechanics) stay byte-identical apart from the literal `step` value written.
- **Preserve register** — targeted string edits to the skill's existing voice, not a rewrite.

## Sequencing

This change is only *correct* once orchestrator 18.2 is in effect (18.2 empties the bare always-valid tuple). Before 18.2 lands, the bare forms still validate and dispatch; the `:1` forms would be unrecognized by the *current* orchestrator and degrade to the disk heuristic. Because both the old heuristic and the new explicit marker reach round 1 for these rollbacks (all prior-round artifacts are deleted → the no-artifact branch returns attempt/iter 1), there is **no hard breakage window** either way — but land this **paired** with orchestrator 18.2 so the skill's table never lies about the accepted set. 18.2 is decomposed into `orchestrator/.ai-factory/roadmaps/trickster77777.md` Phase 18 but **not yet implemented** (a separate orchestrator run implements it).

## Verification

All checks are static — readable in the changed text or `git diff`:

- Every `step`-writing spot at the spec+plan depth writes the literal `"planned:1"`; every spot at the spec+plan+code depth writes the literal `"implemented:1"`; no bare `"planned"` / `"implemented"` marker remains as a value the skill writes.
- The two Emit lines read `… step set to "planned:1" …` and `… step set to "implemented:1".`.
- The closed-set table rows read `"planned:N"` / `"implemented:N"`, and the note under it states the rescue always writes N = 1 and that the bare forms are retired.
- The always-valid guard, Note paragraph, and "Do not write" guard carry the `:1` values with their preconditions unchanged.
- `plan_reviewed`, `plan_review_failed:N`, `review_failed:N`, and `test_run_failed:N` are byte-identical to their pre-change text.
- `orchestrator-artifacts` §3's delegation line still reads true — the closed set it points at is the updated one.

# Review — 21.1 task-rescue: sidecar rollback markers gain an iteration index

## Scope

The only executable change is `src/skills/task-rescue/SKILL.md`. The other modified/new
files (`plans/…`, `plan-reviews/…`, `specs/…`, `handoffs/…`, `roadmaps/trickster77777.md`,
the `.json` sidecar) are the orchestrator's own planning/bookkeeping artifacts for this
run, not product code, and are out of scope for a code review.

## What the change does

Every sidecar `step` value the skill *writes* is indexed to `"planned:1"` /
`"implemented:1"`; the two closed-set table rows generalise to `"planned:N"` /
`"implemented:N"`; a note under the table records that the rescue always writes N = 1 and
that the bare forms are retired. This is a faithful string-level re-sync — no procedural
logic (deletion order, `implementer`-key handling, JSON read/update/write) was touched.

## Verification performed

- **Completeness of the indexing.** Grepped the file for `"planned"` / `"implemented"`:
  the only remaining bare occurrence is line 368, the intentional "the bare … forms are
  retired" note. Every written value — Step 4 depth menu (:240/:243), both rollback
  procedure headings, the `step`-key set lines, both Emit lines, the always-valid guard,
  the Note paragraph, and the "Do not write" guard (:467) — carries `:1`.

- **Table semantics checked against the live referent.** The table claims to mirror
  `_validate_sidecar_step()` / `_detect_step()` in `orchestrator/resume.py`. Read that
  file: `planned:N` dispatches to `("plan_review", n)` and `implemented:N` to
  `(verify_step, n)`, so the new "plan-review, attempt N" / "review, iter N" cells are
  accurate. The `_validate_sidecar_step` no-artifact branch confirms both are
  structurally valid with no disk reference — the "none — always valid" cell holds.

- **Retirement claim is true.** In post-18.2 `resume.py`, a *bare* `"planned"` does not
  match `startswith("planned:")`, so it hits the unrecognized→heuristic fall-through — the
  note's "the orchestrator no longer accepts them" is correct, and the sequencing is
  already satisfied (resume.py implements 18.2 in the sibling repo, so the mirror is honest
  and there is no breakage window).

- **Guards untouched in substance.** `plan_reviewed`, `plan_review_failed:N`,
  `review_failed:N`, and the test-mode `test_run_failed:N` rows/mentions are byte-identical.
  The always-valid guard and "Do not write" guard changed only the written value; their
  plan-`.md`-present and non-empty-diff preconditions are unchanged.

- **Confirm-only dependency verified.** `orchestrator-artifacts` §3 delegates the closed
  set to `task-rescue` without naming any specific bare value ("the closed set and its
  artifact requirements live in `task-rescue`, its only skill-side writer"), so it still
  reads true after the table update — Task 7's no-op is correct.

## Findings

None. The change matches the spec exactly, the table's resume semantics are verified
against the actual orchestrator code, and no procedural mechanics were altered.

REVIEW_PASS

# temporal-tree: one home for the walk

Source observation: `plan-reviews/82-1-13-temporal-tree-pyramid-revision-plan-review-1.md:26` (+ sibling in `-plan-review-2.md:28`), re-verified live 2026-07-12: `SKILL.md` is 172 lines, `docs/overview.md` 115, and `grep -n overview SKILL.md` → zero — no link between them.

## Current state

`src/skills/temporal-tree/SKILL.md` and `src/skills/temporal-tree/docs/overview.md` both carry the Step 1–5 walk procedure and an example `## Features` table. Two homes for one procedure is guaranteed drift; 1.13's pyramid revision consciously scoped itself to SKILL.md (overview.md marked read-only in its plan) and left open which of the two is canonical.

## Change

SKILL.md is the canonical home of the walk — it is what loads. Audit `docs/overview.md` paragraph by paragraph:

- a paragraph teaching something SKILL.md doesn't → moves to `references/overview.md` (the repo's standard depth location), linked from SKILL.md at its load-bearing moment;
- a paragraph restating SKILL.md → deleted.

A fully-redundant file is deleted whole, along with the `docs/` directory if emptied. Deleting is the expected outcome; keeping a `references/` remainder needs each kept paragraph to justify itself.

## Files & types

- `src/skills/temporal-tree/SKILL.md` (link only, if a remainder survives), `src/skills/temporal-tree/docs/overview.md` (move or delete), possibly new `src/skills/temporal-tree/references/overview.md`.

## Guards

- SKILL.md's walk procedure behavior-identical — this task relocates/deletes duplication, never edits the procedure.
- The roadmap-prune ledger-coupling sentence (versioned `## Features` header prefix match) untouched on both sides.

## Verification

- Exactly one file carries the walk procedure; if a `references/` file survives, SKILL.md links it; `src/skills/temporal-tree/docs/` no longer exists or every kept line is non-duplicative.

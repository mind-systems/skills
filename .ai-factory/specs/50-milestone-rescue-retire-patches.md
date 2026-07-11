# milestone-rescue: retire `patches/` from the rescue vocabulary

Source observation: `plan-reviews/93-4-6-orchestrator-artifacts-mirror-…-plan-review-1.md:28`, re-verified live 2026-07-12: `grep -i patch src/skills/orchestrator-artifacts/SKILL.md` → zero (spec 48 retired the bridge), while `milestone-rescue` was last touched in 4.3 — before the retirement.

## Current state

`src/skills/milestone-rescue/SKILL.md` still names `patches/` (line numbers indicative; locate by section):

- frontmatter `description` — "plans, plan-reviews, code reviews, patches" (:4)
- Step 1 artifact-dir filter — `plans/`, `plan-reviews/`, `reviews/`, `patches/` (:47)
- non-convergence deliverable check — "confirm via patches or reviews that the change landed" (:100)
- all four Step-4 rollback deleted-file sets (:239, :242, :245, :249)
- Step 5 non-convergence keep-all list — "plans, plan-reviews, reviews, patches, and sidecar" (:276)

The orchestrator no longer produces the directory, so the rollback lines delete a directory that never exists — a harmless no-op today, but stale drift in a live caller of the protocol engine.

## Change

Delete the `patches` token from every spot above: the description enumerates three artifact kinds; the Step-1 filter lists three dirs; the deliverable check reads "confirm via reviews that the change landed"; each rollback deleted-file set and the keep-all list lose the token.

## Files & types

- edit `src/skills/milestone-rescue/SKILL.md` only.

## Guards

- The sidecar `step` closed-set table and every rollback's semantics byte-identical otherwise.
- The per-variant deleted-file sets are protected blocks (spec 25's criterion); this token removal is their one sanctioned amendment.
- Frontmatter otherwise unchanged; ≤500 lines holds.

## Verification

- `grep -in "patch" src/skills/milestone-rescue/SKILL.md` → zero hits.
- `git diff` shows token removals only — no reflowed rollback semantics.

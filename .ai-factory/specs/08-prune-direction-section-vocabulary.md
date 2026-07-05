# roadmap-prune: Step 6 speaks the direction-section grammar, not just `## Milestones`

**Date:** 2026-07-05
**Source:** deferred observation carried through milestone 52's plan-reviews 1–3 and review-1, evaluated in chat

## Problem today

`src/skills/roadmap-prune/SKILL.md` Step 6 names the section it prunes literally:
"Delete the pruned `[x]` tasks from `## Milestones`" (`:218`) and "Keep `## Milestones`
with all remaining `[ ]` tasks" (`:222`). New-grammar roadmaps (roadmap-engine
"Roadmap File Format") hold tasks under `## <Direction name>` direction sections with
`### Phase N` subheaders — there is no literal `## Milestones` block. An agent pruning
a two-level roadmap gets instructions that name a section that doesn't exist.

This is a **widening of coverage, not a regression fix**: `## Milestones` remains
exactly correct for flat roadmaps (including this repo's own), and the emptied-phase
sweep + retain-last-phase-header rules (`:222-231`) already landed in milestone 52 and
stay as they are.

## The change (one file: `src/skills/roadmap-prune/SKILL.md`, Step 6 only)

1. **Generalize the section vocabulary** (`:218`, `:222`): the deletion and keep
   instructions name "the task-holding sections" covering both shapes — a flat
   `## Milestones` list, and direction sections (`## <Direction name>` →
   `### Phase N` → `N.M` tasks). The two literal `## Milestones` references become
   shape-covering wording; flat-roadmap behavior is unchanged.
2. **Emptied-direction sweep** (one sentence, parallel to the emptied-phase rule one
   level up): when a direction section loses its last phase (all its phase headers
   removed by the emptied-phase sweep and no tasks remain), delete the `## <Direction
   name>` header and its preamble prose too. Never renumber anything — phase numbering
   is historic and file-global; a deleted direction's phase numbers stay as gaps.
3. **Retain-rule interplay stated**: the existing "always retain the last phase header
   and its 2 most recent `[x]` tasks" rule (`:222-224`) means the newest direction is
   never emptied; the emptied-direction sweep can only fire on older, fully-pruned
   directions. One clause, mirroring how the emptied-phase rule already declares its
   coexistence with the retain rule.

## Guards

- **Step 6 only** — the Step 0 deferred-observations gate, Steps 1–5 (slice, grouping,
  hashes, ARCHITECTURE.md, sweep), Step 7–8, and the commit policy are untouched.
- The Step 2 rule "Never copy a phase or section header as a feature name" (`:101`)
  already covers direction headers — untouched.
- No renumbering anywhere; gaps are historic (same invariant as the emptied-phase
  sweep).
- Instructions only, no rationale prose in the skill body (prune's own register).
- ≤500 lines (file is 306 today).

## How to verify

1. `grep -n "## Milestones" src/skills/roadmap-prune/SKILL.md` → remaining mentions
   (if any) present `## Milestones` as the flat shape alongside direction sections,
   never as the only section name Step 6 knows.
2. Step 6 contains the emptied-direction sweep sentence with the no-renumber clause
   and the retain-rule coexistence clause.
3. Steps 0–5, 7, 8 byte-identical to HEAD.

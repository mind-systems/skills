# roadmap-prune: prose reconciled with the real flow and both roadmap shapes

Source observations, re-verified live 2026-07-12: `plan-reviews/54-…-plan-review-1.md:28` (residual — Step 6 and Step 1 were since fixed by spec 08 and the 1.8.x passes; the Step-7 literal remains) and `plan-reviews/75-1-8-2-…-plan-review-1.md:31` (+ siblings in `-plan-review-2.md:26`, `reviews/75-…-review-1.md:32`).

## Current state

Two sentences in `src/skills/roadmap-prune/SKILL.md` describe things that don't exist (line numbers indicative):

- Step 7 verify bullet (:343): "The Milestones section still reads coherently without the pruned tasks" — a direction-grammar roadmap has no `## Milestones` section; Step 6 already speaks both shapes ("task-holding sections").
- Retention sentence (:99): a retained `[x]` line is named "at invocation or at the confirmation step" — the flow (Step 0→8 + commit-on-request) has no discrete confirmation step; the wording was inherited verbatim from spec 38. The only reliable retention channel is invocation.

## Change

- Step 7 bullet → "The task-holding sections still read coherently without the pruned tasks."
- Retention sentence → retained lines are named **at invocation**; the pre-commit working-tree review may be named explicitly as the informal second chance, never as a "confirmation step".

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only. Runs after 5.2 (same file, serial).

## Guards

- Doc-only, behavior-identical; exactly two sentences change.
- Step 6's flat-shape enumeration (`a flat ## Milestones list, or direction sections …`) is correct and stays.

## Verification

- `grep -n "Milestones" src/skills/roadmap-prune/SKILL.md` → only Step 6's shape enumeration.
- `grep -n "confirmation step" src/skills/roadmap-prune/SKILL.md` → zero.

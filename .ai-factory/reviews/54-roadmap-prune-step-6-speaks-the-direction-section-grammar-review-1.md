# Review: roadmap-prune: Step 6 speaks the direction-section grammar — review 1

**Date:** 2026-07-05
**Scope:** `git diff HEAD` — one changed file, `src/skills/roadmap-prune/SKILL.md` (Step 6). The other staged files are planning artifacts (plan `.md`/`.json`, plan-review), not code.

## What changed

Step 6 only, three edits:
1. `:218` delete instruction generalized from literal `## Milestones` to "the task-holding sections — a flat `## Milestones` list, or direction sections (`## <Direction name>` → `### Phase N` → `N.M` tasks)".
2. `:222` keep instruction generalized the same way; the retain-last-phase-header clause and emptied-phase sweep are untouched.
3. New **Emptied-direction sweep** paragraph, parallel to and one level above the emptied-phase sweep, carrying the no-renumber invariant and the retain-rule coexistence clause.

## Verification

- **Spec conformance.** All three spec items (generalize vocabulary, emptied-direction sweep, retain-rule interplay stated) are present and match the spec's wording intent.
- **Guards.** Diff is confined to Step 6; Steps 0–5, 7, 8, the "Before you start" preamble, the commit policy, the "What NOT to do" list, and the Step 2 `:101` rule are byte-identical to HEAD. No renumbering introduced. File is 315 lines (≤500). Flat-roadmap behavior unchanged — `## Milestones` still named as one of the two shapes.
- **Logic — retain rule vs. sweep.** The retain rule keeps "the last phase header," which lives under the newest direction, so that direction always retains ≥1 phase and can never be emptied. The claim that the emptied-direction sweep "can only fire on older, fully-pruned directions" holds. An earlier phase inside the newest direction can still be swept individually without emptying the direction — no contradiction between the two rules.
- **Register.** Instructions only; the sweep's brief historic-gap justification mirrors the neighboring emptied-phase sweep's existing style, no new rationale prose.
- **Runtime.** No executable surface, migrations, types, or concurrency to break — this is skill-instruction text.

## Notes (non-blocking, out of scope)

Step 7's verify line `:256` ("The Milestones section still reads coherently") still names only `## Milestones`, not direction sections. This is a pre-existing narrowness inside a section the spec explicitly guards as byte-identical, so it is intentionally out of scope for this change — not a defect introduced here.

REVIEW_PASS

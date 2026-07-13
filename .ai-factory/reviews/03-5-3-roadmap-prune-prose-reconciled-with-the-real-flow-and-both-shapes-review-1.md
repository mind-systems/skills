# Review: 5.3 — roadmap-prune: prose reconciled with the real flow and both shapes

## Scope
Doc-only change to `src/skills/roadmap-prune/SKILL.md` (two sentences reworded). Reviewed `git diff HEAD`, `git status`, and the changed file in full against the plan and `.ai-factory/specs/52-prune-prose-reconciliation.md`.

## Verification against spec
- `grep -n "Milestones" src/skills/roadmap-prune/SKILL.md` → only Step 6's shape enumeration (line 325). ✓
- `grep -n "confirmation step" src/skills/roadmap-prune/SKILL.md` → zero results. ✓

## Findings
- **Step 7 bullet (line 361):** `The Milestones section still reads coherently` → `The task-holding sections still read coherently`. Correct — matches Step 6's dual-shape vocabulary ("task-holding sections") and subject/verb agreement is right. Step 6's literal `## Milestones` in the flat-shape enumeration is preserved as required.
- **Step 1 retention (lines 98–102):** `at invocation or at the confirmation step` → `at invocation`, plus an added clause naming the pre-commit working-tree review as an "informal second chance… not a formal gate", cross-referencing the existing `## Commit (on request only, never automatic)` section via `(see Commit, below)`. This is exactly the spec's Change directive; the working-tree review really is the run's end-state (Commit section, lines 380–385), so the description is accurate. The trailing "Absent such an explicit instruction…" sentence is preserved intact.

The spec guard "exactly two sentences change" is satisfied in spirit: the two drifted sentences are the ones reworded; the extra clause is the spec-sanctioned naming of the informal second chance, not new behavior.

## Runtime / correctness
No runtime surface — this is an instruction document for the roadmap-prune skill. The prune flow (Step 0→8 + commit-on-request), sweep semantics, and all cross-file couplings are untouched. Behavior-identical, as specified.

REVIEW_PASS

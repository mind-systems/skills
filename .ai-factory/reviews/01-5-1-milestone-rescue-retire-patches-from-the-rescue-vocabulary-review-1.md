# Code Review: milestone-rescue — retire `patches/` from the rescue vocabulary

**Target:** `src/skills/milestone-rescue/SKILL.md` (single file, 476 lines)
**Plan:** `.ai-factory/plans/01-5-1-milestone-rescue-retire-patches-from-the-rescue-vocabulary.md`
**Spec:** `.ai-factory/specs/50-milestone-rescue-retire-patches.md`

## Method
Ran `git status` and `git diff HEAD`, read the changed file in full, and verified against the spec's authoritative acceptance test.

## Verification against spec
- **`grep -in "patch" src/skills/milestone-rescue/SKILL.md` → zero hits** (exit 1, no match). The spec's mandated verification passes.
- **File is 476 lines** — the `≤500 lines` invariant holds (removals only shrink the file).
- **Frontmatter otherwise unchanged** — only the `description`'s `, patches` token dropped; `name`, `argument-hint`, `allowed-tools`, `loads` untouched.
- **Sidecar `step` closed-set table (:353–:377) byte-identical** — no line in that block changed; the `orchestrator/main.py` mirror contract is preserved.

## Change-by-change audit (all 14 original occurrences)
Every occurrence maps to a clean edit; rollback→`step` semantics are unchanged in each case:

- Frontmatter description (:4) — `code reviews, patches` → `code reviews`. Clean.
- Step 1 dir filter (:47) — `patches/` dropped; three real dirs remain, line reflowed with no semantic change.
- Step 1 narrative (:70) — `a patch from round 2 shows whether the implementer addressed it` → `a review from round 2 …`. Semantically sound: a review is precisely what evaluates the implementer's fix.
- Step 2 deliverable check (:100) — `confirm via patches or reviews` → `confirm via reviews`. Meaning intact.
- Step 3 narrative (:119) — `even with a patch` → `across rounds`. Preserves the recurring-issue point without the retired concept.
- Step 4 menu, four rollback sets (:239, :242, :245, :249) — `patches` token dropped from each list; every rollback→`step` mapping (deleted / "planned" / "implemented" / "plan_reviewed") is unchanged.
- Step 5 non-convergence keep-all list (:276) — `reviews, patches, and sidecar` → `reviews, and sidecar`. Clean 4-item Oxford list.
- Step 5 `Delete:` lines, four depth branches (:288, :303, :323, :338) — `all patch files for this slug` clause removed. The three comma-joined lines read cleanly (`… all review files for this slug`), and the *and*-joined line 338 (`all review files and all patch files for this slug`) correctly drops the connective → `all review files for this slug`, avoiding the `all review files and for this slug` grammar trap the plan review flagged.

## Runtime / correctness considerations
- This is agent-instruction markdown, not executable code — no migrations, types, or race conditions apply.
- No rollback deleted-file set now instructs deletion of a directory that never exists; the stale drift the spec targeted is gone.
- Reverse-graph check: the change is internal to the skill's own vocabulary and does not alter any cross-file contract (`orchestrator-artifacts` already retired `patches/` in 4.6; the sidecar `step` table mirror is untouched).

## Findings
None. All edits are pure token removals plus two meaning-preserving narrative rewrites; the spec's Guards (byte-identical rollback semantics and sidecar table, frontmatter otherwise unchanged, ≤500 lines) and its zero-grep verification all hold.

REVIEW_PASS

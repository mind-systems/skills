## Plan Review Summary

**Plan:** `01-5-1-milestone-rescue-retire-patches-from-the-rescue-vocabulary.md`
**Target file:** `src/skills/milestone-rescue/SKILL.md` (single file, 477 lines)
**Files Reviewed:** 1 plan + spec `50-milestone-rescue-retire-patches.md` + target SKILL.md + prior plan-review-1
**Risk Level:** 🟢 Low

### Context Gates

- **Spec traceability (`.ai-factory/specs/50-milestone-rescue-retire-patches.md`):** Read in full.
  The spec's authoritative verification is `grep -in "patch" … → zero hits`, but its `## Change`
  section itemizes only the ~5 enumeration spots (description, Step-1 filter, deliverable check,
  the four Step-4 rollback sets, keep-all list). The plan's `## Scope note` explicitly names this
  tension and resolves it by following the ground-truth grep and the milestone directive "Drop the
  token everywhere" — the authoritative reading. It correctly folds in the occurrences the Change
  section omits: the two narrative lines (:70, :119) and the four Step-5 `Delete:` lines (:288,
  :303, :323, :338). WARN-level note only, no action — a correct spec-vs-verification resolution,
  matching plan-review-1's assessment.
- **Premise re-verified live:** `grep -in "patch" src/skills/milestone-rescue/SKILL.md` returns 14
  hits this session (:4, :47, :70, :100, :119, :239, :242, :245, :249, :276, :288, :303, :323,
  :338). Every hit is mapped: Task 1 covers 12, Task 2 covers the 2 narrative lines. No occurrence
  is left unassigned. All quoted before/after text matches the file byte-for-byte.
- **Prior-review closure:** plan-review-1's single Minor issue — line 338's `and`-joined pair
  (`all review files and all patch files for this slug`) needs the connective dropped, not just the
  clause — is now explicitly handled in Task 1's last bullet: "Line 338 is an *and*-joined pair …
  so drop the connective too: → `all review files for this slug` (not `all review files and for this
  slug`)." The precision gap is closed.
- **Guard preservation (`.ai-factory/ARCHITECTURE.md` boundary check):** The sidecar `step`
  closed-set table (:353–:377), which mirrors `_validate_sidecar_step()` / `_detect_milestone_step()`
  in `orchestrator/main.py`, is untouched — no task edits it. Rollback→`step` mappings in the Step-4
  menu and Step-5 branches keep their semantics; only the token drops. The `loads:` graph
  (`orchestrator-artifacts roadmap-engine`) is unaffected. `≤500 lines` holds trivially (removals
  only shrink the file). Frontmatter otherwise unchanged. No cross-file mirror to sync: the premise
  (patches already gone from `orchestrator-artifacts`) is re-confirmed, and the frontmatter
  description is the single source for the runtime skill description — no duplicate copy elsewhere.
- **Roadmap alignment:** Milestone 5.1 in `.ai-factory/ROADMAP.md:91` matches the plan's intent
  exactly (drop the token everywhere; rollback semantics and sidecar table byte-identical; verify
  `grep -in patch → zero`). No milestone-linkage gap.
- **Skill-context / RULES:** `.ai-factory/skill-context/aif-review/SKILL.md` and
  `.ai-factory/RULES.md` are both absent — no project-specific overrides to apply.

### Critical Issues

None.

### Minor Issues

None. The one Minor issue from plan-review-1 (line 338 connective) is resolved.

### Positive Notes

- The `## Scope note` is exemplary: it names the exact tension between the spec's enumerated Change
  list and its stricter grep verification, grounds the resolution in a live grep, and distinguishes
  pure token drops (mechanical, safe) from the two narrative lines that need rewording — with the
  reasoning stated, not assumed.
- Every rollback deleted-file set is quoted with its precise before/after, and the note that
  "rollback semantics — which sidecar `step` each maps to — stay byte-identical" keeps the
  protected-block guard front of mind.
- Both narrative rewrites preserve meaning without reintroducing the retired concept: line 70's
  "a review from round 2 shows whether the implementer addressed it" is sound (a review is what
  evaluates the implementer's fix), and line 119's "across rounds" keeps the recurring-issue point.
- Task 3 is a proper verification gate — the same `grep -in "patch" → zero` the spec mandates, plus
  a `git diff` audit that the rollback→step mappings and the sidecar table are unchanged and the
  file stays ≤500 lines.
- Correct target: `src/skills/milestone-rescue/SKILL.md`, not the `active/` symlink, per the repo's
  three-way split.

The plan is sound, implementation-ready, and fully addresses the prior review round.

PLAN_REVIEW_PASS

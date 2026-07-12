## Plan Review Summary

**Plan:** `01-5-1-milestone-rescue-retire-patches-from-the-rescue-vocabulary.md`
**Target file:** `src/skills/milestone-rescue/SKILL.md` (single file, 477 lines)
**Risk Level:** 🟢 Low

### Context Gates

- **Spec traceability (`.ai-factory/specs/50-milestone-rescue-retire-patches.md`):** Read. The
  spec's authoritative verification is `grep -in "patch" … → zero hits`, but its `## Change`
  section only itemizes ~5 enumeration spots (description, Step-1 filter, deliverable check,
  the four Step-4 rollback sets, keep-all list). The plan's `## Scope note` correctly recognizes
  that the zero-grep target demands removing occurrences the spec's Change section does not
  itemize — the two narrative lines (:70, :119) and the four Step-5 `Delete:` lines (:288, :303,
  :323, :338). This is a **correct resolution of spec-vs-verification tension**: the plan follows
  the ground-truth grep and the milestone directive "Drop the token everywhere," which is the
  authoritative reading. Handled well and explicitly justified. WARN-level note only, no action.
- **Premise re-verified live:** `grep -i patch src/skills/orchestrator-artifacts/SKILL.md` → 0
  occurrences (confirmed this session). The protocol engine no longer names `patches/`, so
  milestone-rescue is genuine stale drift, exactly as the spec states.
- **Coverage of ground truth:** Live `grep -in "patch"` returns 14 hits. Every one is mapped:
  Task 1 covers 12 (:4, :47, :100, :239, :242, :245, :249, :276, :288, :303, :323, :338),
  Task 2 covers 2 narrative lines (:70, :119). No occurrence is left unassigned. All quoted
  before/after text matches the file exactly.
- **Guard preservation:** The sidecar `step` closed-set table (:353–:377) is untouched — no
  Task edits it, and it is the block that mirrors `orchestrator/main.py`. Rollback→`step`
  mappings in the Step-4 menu and Step-5 branches keep their semantics; only the token drops.
  The `≤500 lines` invariant holds trivially (removals only shrink the file). Frontmatter
  otherwise unchanged. All spec Guards respected.

### Critical Issues

None.

### Minor Issues

- **Task 1, last bullet (Step-5 `Delete:` lines) — line 338 uses a different connective than the
  worked example, and the "leaving punctuation intact" instruction misfits it.** The plan's
  example is the comma-separated form: `all review files, all patch files for this slug` →
  `all review files for this slug`. Three of the four lines (:288, :303, :323) match that form.
  But line 338 reads `all review files **and** all patch files for this slug` — an *and*-joined
  pair, not a comma-joined list. Following the instruction literally ("remove the `all patch
  files for this slug` clause… leaving the remaining delete targets and their punctuation
  intact") would leave `all review files and for this slug` — a broken sentence. The correct edit
  drops the connective too: `all review files and all patch files for this slug` →
  `all review files for this slug`. Suggest the plan add a one-clause note that line 338's
  `and` must be removed with the clause. A competent implementer will likely produce clean
  grammar anyway, and Task 3's "clean diff" check is a backstop — hence Minor, not Critical —
  but the instruction as written is inaccurate for this one line.

### Positive Notes

- The `## Scope note` is exemplary: it names the exact tension between the spec's enumerated
  Change list and its stricter grep verification, grounds the resolution in a live grep, and
  distinguishes pure token drops (safe, mechanical) from the two narrative lines that need
  rewording — with the reasoning stated, not assumed.
- Both narrative rewrites preserve meaning without reintroducing the retired concept. Line 70's
  "a review from round 2 shows whether the implementer addressed it" is semantically sound (a
  review is precisely what evaluates the implementer's fix); line 119's "across rounds" keeps the
  recurring-issue point intact.
- Task 3 is a proper verification gate — the same `grep -in "patch" → zero` the spec mandates,
  plus a `git diff` audit that the rollback→step mappings and the sidecar table are unchanged and
  the file stays ≤500 lines. This closes the loop against accidental semantic drift.
- Editing `src/skills/milestone-rescue/SKILL.md` (not the `active/` symlink) is the correct
  target per the repo's three-way split.

The plan is sound and implementation-ready. The single Minor issue is a wording precision
improvement to Task 1, not a blocker.

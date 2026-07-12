# Plan: milestone-rescue: retire `patches/` from the rescue vocabulary

## Context
The protocol engine retired `patches/` in 4.6 and the orchestrator no longer produces it; this milestone removes every `patch`/`patches` token from `src/skills/milestone-rescue/SKILL.md` so the rescue vocabulary matches the live artifact set, leaving all rollback semantics and the sidecar `step` table byte-identical otherwise.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Scope note
The spec (`.ai-factory/specs/50-milestone-rescue-retire-patches.md`) enumerates the list-style occurrences (frontmatter, Step-1 dir filter, non-convergence deliverable check, the four Step-4 menu rollback sets, Step-5 keep-all list). Its verification, however, is `grep -in "patch" src/skills/milestone-rescue/SKILL.md → zero hits`, and the milestone directs "Drop the token everywhere." Ground truth `grep` reveals occurrences the spec's Change section does not itemize: narrative prose in Step 1 (`a patch from round 2 …`) and Step 3 (`even with a patch`), plus Step 5's four `Delete:` instruction lines (`all patch files for this slug`). To satisfy zero-grep, all of these are removed too. The list/enumeration removals are pure token drops; the two narrative lines require minimal rewording that preserves the sentence's point without introducing the retired concept. No rollback deleted-file set, keep-all list, or the sidecar `step` table changes in any way beyond dropping the token.

## Tasks

### Phase 1: Retire the token

- [x] **Task 1: Drop `patches` from all list/enumeration spots**
  Files: `src/skills/milestone-rescue/SKILL.md`
  Remove the token, leaving surrounding punctuation clean, at each of these enumeration spots (locate by section, not by fixed line number):
  - Frontmatter `description` (~:4): `plans, plan-reviews, code reviews, patches` → `plans, plan-reviews, code reviews`.
  - Step 1 artifact-dir filter (~:47): the dir list `plans/`, `plan-reviews/`, `reviews/`, `patches/` → drop `patches/`, leaving the three real dirs.
  - Step 2 non-convergence deliverable check (~:100): `confirm via patches or reviews that the change landed` → `confirm via reviews that the change landed`.
  - Step 4 `AskUserQuestion` menu, all four rollback deleted-file sets (~:239, :242, :245, :249): drop `patches` from each list (`plan, plan-reviews, reviews, patches, and sidecar deleted` → `plan, plan-reviews, reviews, and sidecar deleted`; `plan-reviews, reviews, patches deleted` → `plan-reviews, reviews deleted`; the two `reviews, patches deleted` → `reviews deleted`). Rollback semantics — which sidecar `step` each maps to — stay byte-identical; only the token is removed.
  - Step 5 non-convergence keep-all list (~:276): `plans, plan-reviews, reviews, patches, and sidecar all describe completed…` → `plans, plan-reviews, reviews, and sidecar all describe completed…`.
  - Step 5 `Delete:` instruction lines, all four depth branches (~:288, :303, :323, :338): remove the `all patch files for this slug` clause from each, leaving the remaining delete targets and their punctuation clean. Three lines (:288, :303, :323) are comma-joined lists (e.g. `all plan-review files, all review files, all patch files for this slug` → `all plan-review files, all review files for this slug`). Line 338 is an *and*-joined pair — `all review files and all patch files for this slug` — so drop the connective too: → `all review files for this slug` (not `all review files and for this slug`).

- [x] **Task 2: Reword the two narrative `patch` mentions** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  These two are prose, not lists — reword minimally to remove the retired concept while preserving the sentence's meaning:
  - Step 1 (~:70): `A plan-review from round 1 reveals what the planner missed first; a patch from round 2 shows whether the implementer addressed it.` → replace the `patch from round 2` clause with a review-based equivalent (e.g. `a review from round 2 shows whether the implementer addressed it`).
  - Step 3 (~:119): `the implementer could not fix them even with a patch, so the description is the only reliable enforcement` → drop the retired-artifact reference while keeping the point (e.g. `the implementer could not fix them across rounds, so the description is the only reliable enforcement`).
  Keep changes surgical — no reflow of surrounding rollback semantics or the sidecar `step` table.

- [x] **Task 3: Verify zero hits and clean diff** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Run `grep -in "patch" src/skills/milestone-rescue/SKILL.md` → must return zero hits. Run `git diff` and confirm it shows only token removals / minimal narrative rewordings — no changed rollback→step mappings, no altered sidecar `step` table, frontmatter otherwise unchanged, file still ≤500 lines.

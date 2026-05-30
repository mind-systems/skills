# Code Review 2: milestone-rescue — update JSON sidecar after artifact cleanup

**Plan file:** `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.md`
**Changed files:**
- `.claude/skills/milestone-rescue/SKILL.md`
- `.claude/skills/milestone-rescue/docs/overview.md`
**Prior review:** `review-1.md` (🔴 High — cleanup deleted sidecar before update; overview drift)

## Risk Level
🟢 **Low** — both review-1 blockers are properly resolved with no new issues introduced.

---

## Resolution of review-1 findings

| # | Finding | Status |
|---|---|---|
| Critical 1 | Cleanup deleted the sidecar before the new sub-step could read it (lost `planner`/`implementer`/`elapsed`) | ✅ **Resolved** — review-1's Option (B) applied. Cleanup language now reads "delete all uncommitted files from `plan-reviews/`, `reviews/`, and `patches/`, and `.md` files from `plans/`" (SKILL.md line 185–187). An explicit `Do NOT delete .json sidecar files from plans/` line (193–194) reinforces the carve-out. The sidecar survives cleanup, so the read-modify-write path in the new sub-step preserves keys as intended. |
| Medium 2 | `docs/overview.md` Step 5 went out of sync | ✅ **Resolved** — `docs/overview.md` Step 5 now mirrors the SKILL.md cleanup carve-out (lines 138–140 + 143–145) and adds a brief `Update the sidecar` paragraph (148–153) that points readers at the SKILL.md mapping table for the full rules (avoiding duplicate-source-of-truth risk). The "What NOT to do" list (line 165–166) gains the same preservation bullet. |
| Medium 3 | "Reviews exist" rows assume non-deletion that the cleanup contradicts | (carryover, not in scope) — the plan author deliberately scoped this PR to the sidecar; the row 2/3 wording is verbatim from `notes/08` per the source-note's "include verbatim" mandate. Re-flagging would be noise. |
| Minor 4–7 | Fall-through reachability, `Glob` semantics, `{value}` template, re-check-disk after cleanup | (carryover, all non-blocking) — unchanged, still non-blocking. |

---

## Cross-checks against the codebase

- **Frontmatter** (SKILL.md line 11). `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion`. `Write` inserted directly after `Read`. Single-line YAML preserved; no parsing risk. ✅
- **Cleanup carve-out actually protects the on-disk sidecar.** Current working-tree sidecar `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.json` (status `A`, contains `planner`/`step`/`elapsed`/`implementer`) matches `.json` in `plans/` for the rescue slug — explicitly excluded by the new "Do NOT delete `.json` sidecar files" rule. The reorder bug from review-1 is verifiably fixed. ✅
- **Mapping table** (SKILL.md lines 208–213) reproduces `notes/08-milestone-rescue-sidecar-update.md` lines 14–20 character-for-character. ✅
- **Sub-step placement.** Sits between the cleanup block (ends 195) and the final "Show the user the list of deleted files…" line (230), inside Step 5 and before Step 5.5 (starts 233). Matches the plan's "Positioning" design decision. ✅
- **`docs/overview.md` cross-reference** (line 151) — `(see the mapping table in SKILL.md Step 5)` keeps the table single-sourced in SKILL.md. ✅
- **Mirrored "What NOT to do" bullets.** SKILL.md line 280–281 and `docs/overview.md` line 165–166 carry identical preservation language. ✅

---

## New observations from this iteration

### Minor 1. Cleanup sentence grammar is a touch awkward

SKILL.md line 185–187:

> delete all uncommitted files from `plan-reviews/`, `reviews/`, and `patches/`, and `.md` files from `plans/`, that belong to this milestone's slug.

The trailing relative clause "that belong to this milestone's slug" syntactically attaches only to ``.md` files from `plans/`" because of the comma before it. Grammatically loose, but the intent is unambiguous from context (and is reinforced two lines later by "Do NOT delete files belonging to other milestone slugs"). Optional rewording for clarity:

> delete all uncommitted files belonging to this milestone's slug — from `plan-reviews/`, `reviews/`, and `patches/`, plus `.md` files from `plans/`.

Non-blocking.

### Minor 2. Sub-step says "the sub-step below" / "the next sub-step"

SKILL.md line 193: "the sub-step **below** reads…"
`docs/overview.md` line 144: "the **next** sub-step reads…"

Minor wording inconsistency between the two files. Both are correct in their own context (the SKILL sub-step is below the cleanup paragraph; the overview sub-step is "next" in flat prose). Not a defect.

### Observation. Sidecar JSON now contains the explicit precondition the carve-out protects

`.ai-factory/plans/01-…-cleanup.json` carries `"planner"`, `"step"`, `"elapsed"`, `"implementer"`. The rescue's preservation invariant would have erased three of those four keys before this fix — useful corroboration that the bug review-1 flagged was real and that the fix actually solves it.

---

## Critical Issues
None.

## Medium Issues
None.

## Positive Notes

- Review-1 Critical #1 was resolved via the smaller-diff option (narrowing cleanup) rather than reordering — preserves the existing "delete first, then summarize" flow of Step 5 and doesn't require carrying state across the cleanup boundary.
- Explicit "Do NOT delete `.json` sidecar files" callout means a future maintainer broadening the cleanup back to all-of-`plans/` will see the invariant in-line, not just buried in the sub-step below.
- `docs/overview.md` was updated as part of the same change set — no documentation drift introduced.
- The overview's sidecar paragraph defers to the SKILL.md mapping table instead of duplicating it; only one source of truth to maintain.
- Mirror-bullet in `docs/overview.md` "What NOT to do" provides defense-in-depth at the orientation-doc layer too.

---

REVIEW_PASS

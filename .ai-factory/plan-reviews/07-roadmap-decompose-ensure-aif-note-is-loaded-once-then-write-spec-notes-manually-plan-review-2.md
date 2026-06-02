# Plan Review 2 — roadmap-decompose: ensure aif-note is loaded once, then write spec notes manually

## Summary

**Plan:** `.ai-factory/plans/07-roadmap-decompose-ensure-aif-note-is-loaded-once-then-write-spec-notes-manually.md`
**Target:** `src/skills/roadmap-decompose/SKILL.md`
**Risk Level:** 🟢 Low — this revision incorporates every finding from review 1. The edit list is now exhaustive (verified by grep against the live file), the self-contradiction is resolved, and the inherited-template observation is captured. The plan is implementation-ready.

The intent — load `aif-note` once so its note-writing instructions are in context, then `Write` each spec note manually, while preserving the two-tier shape, contract line, `Spec:` tag, char budget, and Atomicity Gate — faithfully matches the spec note `16-task-decompose-inline-notes-aif-note-format.md` and the ROADMAP milestone.

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): PASS. Doc-only edit to one skill's `SKILL.md`; no module boundary or dependency-model impact. Skill-invokes-skill coupling remains runtime-text only.
- **Rules** (`.ai-factory/RULES.md`): not present — WARN (optional file absent, no action).
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS. Maps exactly to the open milestone (line 19) and links the same spec note. Strong linkage.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project overrides to apply.

## Review-1 Findings — Resolution Check

- **Finding 1 (step 2 kept the cruft):** RESOLVED. Task 1 now explicitly rewords step 2 — change the `(two note invocations + two contract lines, sequentially)` parenthetical to `two notes + two contract lines`, dropping "invocations" and "sequentially". Matches line 289 verbatim.
- **Finding 2 (incomplete enumeration):** RESOLVED. Task 2 now lists all previously-missed locations — line 16 (intro), line 105 (Step 1.3), line 115 (Step 1.3.1), lines 193/197 (Step 2.4.1) — alongside the frontmatter, Step 1.4, Step 2.4, Step 2.5, line 321, and Critical Rule 6.
- **Finding 3 (research-summary template):** CAPTURED. "Notes for the implementer" explicitly tells the implementer the in-context template is `Key Findings / Details / Open Questions`, not the `Current state / Target / Guards / Verify` shape, and not to "improve" it.

## Exhaustiveness Verification

Grep of `aif-note` / "note invocation" / "invocations" / "sequentially" / "reports back" / "subject" against the live file returns lines 6, 16, 105, 115, 136, 187, 193, 197, 209, 210, 289, 290, 291, 296, 321, 332. Every one is covered:

- Task 1 covers 289 (step 2), 290–291 (steps 3–4 → replaced), 296 (Sequential-invocations paragraph → deleted/replaced).
- Task 2 covers 6, 16, 105, 115, 136, 187, 193/197, 209/210, 321, 332.

Nothing is left behind. Line references in the plan all match the current file.

## Critical Issues

None. This is a documentation edit to a skill; no runtime code, security, migration, or API-correctness surface.

## Observations (non-blocking)

### NN allocation across multiple notes in one run

Task 1's replacement rule says `aif-note` is loaded at most once, and "when writing several notes, scan existing note numbers first so `<NN>` never collides." Under the old model, aif-note guaranteed no collision by writing one note fully to disk before the next invocation's scan. Under manual `Write`, the agent must reproduce that sequencing itself: compute `<NN>` → `Write` → re-scan for the next note. If the implementer reads "scan existing note numbers first" as a single up-front scan and then writes notes 17, 18, 19, the second and third would collide. The plan's intent is correct and the guard is preserved; the implementer should simply allocate each `<NN>` immediately before writing that note (so each scan sees prior writes). Worth keeping in mind, but the wording is adequate and this does not block.

## Things the plan gets right

- **Targeted edits over literal `git revert 0bfa177`** — correctly flags the file moved from `.claude/skills/` to `src/skills/`, so a literal revert would touch wrong paths.
- **`allowed-tools` reasoning** — keeps `Skill` (one-time aif-note load) and `Write` (manual authoring); `Glob` already present for scanning `.ai-factory/notes/`. Correct.
- **"No note-format of its own" guard** — Task 1 and Task 2 both explicitly forbid adding any decompose-owned note format and forbid modifying the aif-note skill.
- **Guards mirror the spec note** — at-most-once invocation, no per-task invocation anywhere, no self-described format, unchanged two-tier shape / contract line / `Spec:` tag / char budget / Atomicity Gate.

## Recommendation

The plan is solid and ready to implement. The single observation above is a wording nuance for the implementer, not a defect in the plan.

PLAN_REVIEW_PASS

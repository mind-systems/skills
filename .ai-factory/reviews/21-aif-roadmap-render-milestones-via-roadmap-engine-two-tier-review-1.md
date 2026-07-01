# Code Review: aif-roadmap — render milestones via roadmap-engine (two-tier)

**Plan:** `.ai-factory/plans/21-aif-roadmap-render-milestones-via-roadmap-engine-two-tier.md`
**Files changed (code):** `src/skills/aif-roadmap/SKILL.md`, `CLAUDE.md` (plus plan/review/json artifacts — not reviewed as code)
**Scope:** prompt/skill text refactor — no executable code, no migrations, no runtime types. "Runtime" here is an LLM following the SKILL instructions; correctness = internal consistency and faithful delegation.
**Risk Level:** 🟢 Low

## Verification performed

- **Frontmatter (Task 1).** `allowed-tools` line 5 gains `Skill` and nothing else. Necessary and sufficient: the skill must load `roadmap-engine` (and, transitively per the engine, `aif-note`) via the `Skill` tool. `Write`/`Edit` are retained, so the skill can still author both the notes and `ROADMAP.md`. Matches sibling `roadmap-decompose`. ✅
- **Step 1.3 repoint (Task 2).** The inline ```markdown``` format block (old 77–87) is removed and replaced by engine glue. The `<note pending>` placeholder + "notes written after confirmation in 1.4" mechanism is coherent and mirrors `roadmap-decompose`. Vision-sourcing cue ("from `DESCRIPTION.md` or user input") retained (review-1 rec 2). The old lead-in "Create `.ai-factory/ROADMAP.md` with this format:" is folded into the new sentence — no orphaned lead-in (review-2 rec 2). ✅
- **Granularity philosophy preserved.** The "Rules for milestones:" list (lines 77–81) and Critical Rule 1 (line 224) are byte-identical to the original. No 5–15/high-level-goal wording changed. Regression guard satisfied. ✅
- **Step 2.4 repoint (Task 3).** Insert-render line added; "Ask user to describe…" and "Insert them in logical order…" kept verbatim; Modes 2.3/2.5/2.6 and Mode 3 untouched (mark/reorder only). ✅
- **Format section removed (Task 4).** `## ROADMAP.md Format` gone; the `---` before `## Critical Rules` (line 220) is correctly preserved (not orphaned — review-1 rec 3). A grep confirms **no remaining reference** to "short description" or the inline format anywhere in the file. ✅
- **CLAUDE.md (Task 5).** `aif-roadmap` added to "Custom skills — never overwrite"; the "Intentionally diverged" bullet removed, leaving only `aif-plan` there — coherent. ✅
- **No AskUserQuestion block altered.** All five blocks are identical to the original. ✅

## Critical Issues

None.

## Observations (non-blocking, no action required)

1. **Note-writing instruction physically lives in Step 1.4's trailing line (line 97), not purely inside 1.3.** The plan's carve-out listed Step 1.4 among "byte-identical preserved" sections, and plan-review-2 flagged the resulting tension. The implementer resolved it the pragmatic (and correct) way: the 1.4 `AskUserQuestion` block itself is kept verbatim, and only the trailing "Apply changes … save" instruction was extended to write notes for the confirmed set. This is exactly how `roadmap-decompose` places its equivalent "After 'Looks good — save it': …" instruction inside Step 1.4, and it is the only place the deferred write can correctly happen. No correctness problem — the confirmed-set-only rule closes the orphaned-note risk cleanly.

2. **Mode 2.4 writes notes without a confirm gate.** Unlike Mode 1, 2.4 has no post-hoc rewrite step — the user has just described the milestones they want — so writing notes directly carries no orphan risk. Consistent with the original 2.4 and with `roadmap-decompose`. Correct.

## Positive Notes

- Faithful, minimal diff: every hunk maps to a plan task; the granularity philosophy is untouched, satisfying the plan's explicit regression guard.
- The `<note pending>` → confirm → real-tag lifecycle is internally consistent and matches the engine's two-tier contract-line format (`Spec:` tag always terminates the line).
- Load-once discipline ("don't re-invoke if already loaded") is stated at both render sites, honoring the engine's load-once requirement.
- CLAUDE.md upstream-sync bookkeeping — the easily-forgotten consequence of taking a local-only dependency — is handled.

REVIEW_PASS

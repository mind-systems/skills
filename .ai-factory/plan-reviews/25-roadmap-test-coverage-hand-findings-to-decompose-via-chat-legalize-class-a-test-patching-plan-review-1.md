# Plan Review: roadmap-test-coverage — hand findings to decompose; legalize Class-A test patching

**Plan:** `25-roadmap-test-coverage-hand-findings-to-decompose-via-chat-legalize-class-a-test-patching.md`
**Target:** `src/skills/roadmap-test-coverage/SKILL.md` (297 lines)
**Risk Level:** 🟡 Low–Medium

## Verification of Assumptions

All line references in the plan match the current file:
- Layer 6 at lines 191–201 ✓ (step 1 writes `## Test Infra` task to `$ROADMAP_PATH`, step 2 appends `## Refactor Required` to the Layer-4 note)
- Layer 7 Class B write at lines 257–258 ✓
- Layer 7 classification table at lines 245–250 ✓, Class-A patch instruction at 254–255 ✓
- Layer 8 at lines 264–282 ✓ (summary lines 275–277)
- Critical Rule 1 at line 288 ✓

Architectural direction is sound and consistent with repo conventions:
- Handing task descriptions to the user for a manual `/roadmap-decompose` fits that skill's interface — its `argument-hint` is `"[task description or requirements]"`, and it auto-routes test-flavored input to `.ai-factory/ROADMAP_TESTS.md` (decompose SKILL.md lines 9, 37–38). So the handoff format is valid input downstream.
- Removing the `$ROADMAP_PATH` writes aligns with the planning/implementation separation and with Critical Rule 2 ("Never write ROADMAP_TESTS.md — that is `/roadmap-decompose`'s job"). The skill moving to write *neither* roadmap file is more consistent, not less.
- Line-count constraint (≤ 500) is safe: current file is 297 lines and the net change is roughly neutral.

## Findings

### 1. Class B handoff items may have no "source note path" (Task 2 + Task 3) — Medium

Task 3 requires the Layer 8 handoff list to print "refactor items and Class B bug items, **each with its source note path**." Refactor items always have a note (they derive from Layer 5 verdicts on `$RESEARCH_AREAS`, each of which produced a Layer-4 note). **Class B items do not.**

Layer 7 runs the whole suite via `$TEST_CMD`, so a failing test can belong to an area that was dropped before research — e.g. a "Full coverage" area dropped in Layer 2, or a loud-failure area dropped by Layer 3's silent-failure filter. Those areas never got a Layer-4 note, so there is no note path to attach.

Two related gaps:
- Task 2 collects only "area name + reason from the classification table" for Class B — it does not capture a note path or the source file, and the classification table (line 247) has no note-path column.
- Task 3 then asks to print a note path per Class B item with no defined way to resolve it.

**Recommendation:** In Task 2, capture the source file (the table already has a `Source file` column) for each Class B item. In Task 3, specify the fallback: attach the Layer-4 note path when the failing test's area was researched, otherwise print the source file path. This makes the handoff line well-defined for every Class B case.

### 2. Frontmatter description goes slightly stale under "frontmatter is unchanged" (Task 4) — Low / WARN

Task 4 instructs confirming the frontmatter is unchanged. The `description` (SKILL.md line 7) still reads "…**emits refactor tasks**, runs existing tests and classifies failures…". After this change the skill no longer emits refactor tasks to the roadmap — it collects them and hands them off. "hands off to /roadmap-decompose" (line 8) remains accurate, but "emits refactor tasks" now implies a roadmap write that no longer happens.

This is non-blocking (the phrase can be read loosely as "surfaces refactor findings"), but if the intent is precision, allow a one-word tweak (e.g. "collects refactor findings") rather than freezing the whole frontmatter. Flag so the implementer doesn't treat "unchanged" as a hard prohibition against fixing a now-inaccurate description.

## Context Gates

- **Architecture:** `.ai-factory/ARCHITECTURE.md` present; no rules governing this skill's roadmap-write behavior (only a passing mention of `command-handoff`). No boundary conflict. — PASS
- **Rules:** `.ai-factory/RULES.md` — not present. — WARN (optional file absent)
- **Roadmap:** change is a skill rework; no milestone-linkage expectation for this repo's meta-skill edits. — N/A
- **Skill-context:** `.ai-factory/skill-context/aif-review/SKILL.md` — not present. No project overrides to apply. — WARN (optional file absent)

## Positive Notes

- Task boundaries are crisp and correctly scoped: each task names the exact layer and the exact lines to touch, and explicitly lists what to leave intact (Layer 7 table, agent prompt, Class-A patch text, re-run requirement).
- Dependencies (Task 3 depends on 1+2; Task 4 depends on 2) are correct — the handoff list must exist before Layer 8 prints it, and Rule 1's rewording must match the Class-A instruction it legalizes.
- Task 4 correctly identifies the real contradiction being resolved (Rule 1 "never write test files" vs. Layer 7's legal Class-A patch) and scopes the exception tightly (assertions intact, call signature only).
- Keeping Layer 6 step 2 (the note-append) while removing step 1 (the roadmap write) is the right cut — note content stays, roadmap pollution goes.

## Verdict

The plan is well-structured and its codebase assumptions are accurate. Finding #1 is a genuine spec gap that will surface as an ambiguous/blank note path for out-of-research Class B failures and should be closed before implementation. Finding #2 is a minor wording caveat.

# Plan Review 2: roadmap-decompose-skeleton (plan 19)

**Plan:** `.ai-factory/plans/19-roadmap-decompose-skeleton-new-skill-skeleton-tdd-concurrency-decomposition-lens.md`
**Files Reviewed:** plan 19 + round-1 review, spec note 27, sibling `roadmap-decompose/SKILL.md` (frontmatter + Step 0/1), `roadmap-engine/SKILL.md`, `test-engine/SKILL.md`, `CLAUDE.md` (Repository Structure tree + Upstream Sync custom-skills list)
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy"):** ✅ PASS. The skill owns only policy (three lenses + restraint), loads `roadmap-engine` and `test-engine` as load-once engines, copies neither body, and correctly refuses a pure-router `roadmap-tdd` middle skill. Fully aligned.
- **Rules (`.ai-factory/RULES.md`):** ⚠️ WARN — file absent; no explicit convention rules to check (non-blocking).
- **Roadmap (`.ai-factory/ROADMAP.md`):** ✅ PASS. Source milestone linkage is present; this plan is the second-pass consumer described in note 27.
- **skill-context (`.ai-factory/skill-context/aif-review/SKILL.md`):** ⚠️ WARN — absent; no project-specific review overrides to apply.

## Round-1 Blocking Issue — Resolved

The single blocking item from review 1 was that `allowed-tools` (`Read Glob Grep Bash(git *) AskUserQuestion Skill`) lacked `Write`/`Edit`, so the skill had no sanctioned way to insert contract lines into `ROADMAP.md` (no delegate performs that write: `roadmap-engine` is `Read`-only, `aif-note` writes only `.ai-factory/notes/`, and calling `roadmap-decompose` is forbidden).

Plan 19 now addresses this directly and correctly:
- The **"Correction to note 27 frontmatter"** section (lines 8) documents the divergence and its rationale.
- **Task 1** specifies `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill` with an explicit note that `Write Edit` are added beyond note 27.
- **Verified:** this exactly matches the sibling `roadmap-decompose`'s grant (`Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`, confirmed in its SKILL.md line 10), the correct model since both do equivalent `ROADMAP.md` editing.

No blocking issues remain.

## Verification of Remaining Claims

- **`test-engine` vs `test-philosophy` naming:** ✅ Confirmed. Installed skill is `src/skills/test-engine/` (`user-invocable: false`, `allowed-tools: Read`), and its own description already names `roadmap-decompose-skeleton` as a consumer. The plan's alias handling and out-of-scope rename call are correct.
- **`roadmap-engine` is `Read`-only:** ✅ Confirmed (`allowed-tools: Read`), so the write grant genuinely must live on the calling skill — the fix is necessary, not redundant.
- **Frontmatter shape:** ✅ `disable-model-invocation: true` with no `user-invocable: false` is right for a user-invocable decompose command (matches sibling `roadmap-decompose`, unlike the `user-invocable: false` engines). Quoted `argument-hint`, `name` = directory name all conform.
- **Task 3 / CLAUDE.md accuracy:** ✅ Confirmed. The Upstream Sync "Custom skills — never overwrite" list (line 116) does not yet contain `roadmap-decompose-skeleton` — the plan adds it. The Repository Structure tree lists `roadmap-engine`/`roadmap-prune` but not `roadmap-decompose` or `roadmap-test-coverage`; the plan's Task 3 note about the `aif-*/` catch-all and partial enumeration is accurate, so "insert one alphabetically-reasonable line" is the right instruction.
- **File paths:** ✅ `src/skills/roadmap-decompose-skeleton/SKILL.md` and `CLAUDE.md` are correct targets.

## Minor Notes (non-blocking)

- **Pre-existing gap, not this plan's job:** `roadmap-test-coverage` is missing from the CLAUDE.md custom-skills list despite existing under `src/skills/`. Out of scope here; flag for later cleanup (also noted in review 1).
- **Line budget:** Task 2 packs three lenses + m36/m37 canon + ordering/fusion into one `SKILL.md` under 500 lines. No structural risk, but the implementer should keep prose tight.

## Positive Notes

- The round-1 fix is not a silent patch — the plan documents the divergence from note 27 with reasoning (lines 8, and the Task 1 inline note), which is exactly how a plan should handle a deliberate spec override.
- Naming discrepancy, load-once discipline, restraint-as-first-class, target-file discipline (`ROADMAP.md`, never `ROADMAP_TESTS.md`), and the explicit "What NOT to do" list all faithfully carry note 27's intent.
- Call graph, canon references (m36 `PassThroughIndicator`, m37 `drainHeap()`/dedupKey), and the fusion/exception rules are transcribed accurately from the spec note.

The plan is architecturally sound, faithful to the spec note, and the one round-1 blocker is fully resolved and verified against the codebase.

PLAN_REVIEW_PASS

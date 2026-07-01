# Plan Review: roadmap-decompose-skeleton (plan 19)

**Plan:** `.ai-factory/plans/19-roadmap-decompose-skeleton-new-skill-skeleton-tdd-concurrency-decomposition-lens.md`
**Files Reviewed:** plan + spec note 27, sibling `roadmap-decompose/SKILL.md`, `roadmap-engine/SKILL.md`, `test-engine/SKILL.md`, `aif-note/SKILL.md`, `roadmap-test-coverage/SKILL.md`, `CLAUDE.md`, `ARCHITECTURE.md` (composition section)
**Risk Level:** 🟡 Medium

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy"):** ✅ PASS. The plan follows the engine/philosophy model precisely: the new skill owns only policy (the three lenses + restraint), loads `roadmap-engine` (format mechanism) and `test-engine` (silent-failure rule) as load-once engines, and copies neither body. It correctly refuses a `roadmap-tdd` middle skill (pure-router = negative value). Fully aligned.
- **Rules (`.ai-factory/RULES.md`):** ⚠️ WARN — file absent; no explicit convention rules to check against (non-blocking).
- **Roadmap (`.ai-factory/ROADMAP.md`):** ✅ PASS. The working tree shows the source milestone line being consumed from ROADMAP.md into this plan; linkage is present.
- **skill-context (`.ai-factory/skill-context/aif-review/SKILL.md`):** ⚠️ WARN — absent; no project-specific review overrides to apply.

## Critical Issues

### 1. `allowed-tools` cannot write the artifacts the skill is required to produce (HIGH)

Task 1 fixes `allowed-tools: Read Glob Grep Bash(git *) AskUserQuestion Skill` — no `Write`, no `Edit`. But the skill's core stated behavior (Task 2 → "Rendering"; note 27 §Call graph) is to **render skeleton/TDD/contract contract-lines into the same `ROADMAP.md`**. Inserting those contract lines into an existing `ROADMAP.md` is an `Edit` operation, and there is no delegate that performs it:

- `roadmap-engine` has `allowed-tools: Read` — it only *describes* the format, never writes (confirmed in its SKILL.md).
- `aif-note` (`allowed-tools: Read Write ...`) writes only the numbered spec-note files under `.ai-factory/notes/`; it never touches `ROADMAP.md`.
- The sibling `roadmap-decompose`, which this skill is modeled on and which does the equivalent ROADMAP.md editing, deliberately carries `allowed-tools: Read Write Edit ...`.
- The one skill that avoids the write grant — `roadmap-test-coverage` — does so by **handing off to `/roadmap-decompose`** for the actual roadmap write. This skill is explicitly forbidden from calling `roadmap-decompose` at runtime (plan Task 1/Task 2 "Critical Rules"), so that escape hatch is closed.

Net: with the grant as specified, the skill can compute the decomposition and get spec notes written (via `aif-note`), but has no sanctioned way to insert the resulting contract lines into `ROADMAP.md`. Under a strict allowlist it cannot; under a permissive harness it will trigger an out-of-band permission prompt on every run.

**Fix:** add `Edit` (and `Write`, to cover the rare case where the target roadmap must be created) to `allowed-tools` — matching `roadmap-decompose`. The plan/note omission is inherited from note 27 §Frontmatter, so update Task 1's frontmatter spec explicitly rather than copying the note verbatim. Alternatively, if the design intent is truly proposal-only (emit tasks to chat, human pastes them), Task 2's "Rendering" section must say so — but that contradicts "render results into the same ROADMAP.md" and the whole two-tier `roadmap-engine` flow, so adding the tools is the right resolution.

## Minor Notes

- **Task 3 — Repository Structure tree:** The tree in `CLAUDE.md` currently does **not** list `roadmap-decompose` or `roadmap-test-coverage` (it uses an `aif-*/` catch-all and enumerates only a subset). Adding `roadmap-decompose-skeleton/` is fine, but "alongside the other roadmap family members" slightly overstates what's there. Cosmetic — implementer should just insert one alphabetically-reasonable line and not expect existing siblings to all be present.
- **Pre-existing gap (not this plan's job, worth noting):** `roadmap-test-coverage` is missing from the `CLAUDE.md` "Custom skills — never overwrite from upstream" list even though it exists under `src/skills/`. Out of scope here; flag for a later cleanup.
- **Line budget:** Task 2 correctly repeats the ≤500-line constraint. Given the density of the three-lens content plus canon (m36/m37), the implementer should keep prose tight; no structural risk.

## Positive Notes

- **Naming discrepancy handled correctly.** The plan's up-front "Assumption (naming)" section catches that note 27/the roadmap say `test-philosophy` but the installed skill is `test-engine` (verified: `src/skills/test-engine/`, and its own description already names `roadmap-decompose-skeleton` as a consumer). Invoking `test-engine` with `test-philosophy` as an alias, and declaring a rename out of scope, is exactly right — this is the kind of codebase-truth check plan reviews exist to confirm.
- **Load-once discipline** for `roadmap-engine`, `test-engine`, and (transitively) `aif-note` is stated explicitly and matches each engine's own load-once contract.
- **Restraint as first-class** and the explicit "What NOT to do" list (no `roadmap-tdd`, don't copy bodies, don't call `roadmap-decompose` at runtime, don't touch the orchestrator, operate only on open `[ ]` tasks) faithfully carry note 27's intent.
- **Target-file discipline** (outputs go to `ROADMAP.md`, never `ROADMAP_TESTS.md`; the engine never infers the target) is correctly preserved from the note.
- File paths, directory name = `name`, quoted `argument-hint`, and `disable-model-invocation: true` all match repo conventions and the sibling skill.

Overall the plan is architecturally sound and the decomposition is faithful to the spec note; the single blocking item is the tool-grant gap in Issue 1, which is a small frontmatter fix.

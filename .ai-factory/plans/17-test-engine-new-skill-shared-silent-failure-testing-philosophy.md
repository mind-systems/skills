# Plan: test-engine — new skill — shared silent-failure testing philosophy

## Context
Extract the "test only silent failures, skip loud ones" rule — currently inline in `roadmap-test-coverage` (Layer 3 filter + Layer 7 Class A/B) and about to be duplicated in `roadmap-decompose-skeleton` — into a pure-content skill `src/skills/test-engine/SKILL.md` that both callers load for the discriminator, caller in control, load-once.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the skill

- [x] **Task 1: Create `test-engine/SKILL.md` with the silent-failure discriminator**
  Files: `src/skills/test-engine/SKILL.md`
  Create the skill package directory and its single `SKILL.md`. Frontmatter exactly per spec note `.ai-factory/notes/29-test-engine-skill.md` §Frontmatter: `name: test-engine` (must match dir name), the given `description`, `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`. Body follows the `roadmap-engine/SKILL.md` framing pattern (a short paragraph stating this is a shared pure-content philosophy unit — no procedure, no I/O; the calling skill stays in control; load once per chat), then the content **lifted verbatim** from the authoritative source `src/skills/roadmap-test-coverage/SKILL.md`:
    1. The core question (`SKILL.md:64-68`): "If the logic here is wrong, does the system signal it immediately (compile/TypeScript error, runtime exception, DI failure, 4xx/5xx response), or does it continue running and produce wrong output silently?" — generalize "TypeScript" to compile-error since test-engine is stack-agnostic (do NOT couple to any runner/stack).
    2. The loud→skip / silent→test table (`SKILL.md:70-76`), copied as-is; keep the column header wording as "test" (not "keep") to match this skill's phrasing, per the spec note table.
    3. The rule line: **test only silent-failure surfaces** — loud-failure surfaces are already caught by the compiler/runtime/DI/HTTP layer.
    4. The after-the-fact corollary for test triage (`SKILL.md:244-250`): **Class A — API drift** (source API changed, test outdated → patch the test) and **Class B — silent bug** (source behavior changed in a way the test was designed to catch, wrong output → the test is doing its job → escalate, never suppress).
  Do NOT include any test-generation procedure, coverage pipeline, agent orchestration, `$RESEARCH_AREAS`/roadmap output blocks, or stack-specific detail — that logic stays in `roadmap-test-coverage`. Body ≤ 500 lines (this will be far shorter). Use relative paths only.

### Phase 2: Register the skill

- [x] **Task 2: Register `test-engine` in CLAUDE.md** (depends on Task 1)
  Files: `CLAUDE.md`
  Two edits: (a) add `test-engine` to the "Custom skills — never overwrite from upstream" list (`CLAUDE.md:115`), so the next upstream sync does not wipe it; (b) add a `test-engine/` entry to the Repository Structure tree under `src/skills/` (near `roadmap-engine/ #  two-tier artifact-output engine` at `CLAUDE.md:30`), with a one-line comment such as `#   shared silent-failure testing philosophy`.

## Notes
- Single logical change (new skill + its registration) → one commit, no commit plan needed.
- The spec note's reproduced content is a pointer; the authoritative text is `roadmap-test-coverage/SKILL.md` — copy from there.

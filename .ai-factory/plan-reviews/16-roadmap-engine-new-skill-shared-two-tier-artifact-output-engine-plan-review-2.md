# Plan Review 2: roadmap-engine — shared two-tier artifact-output engine

**Plan:** `.ai-factory/plans/16-roadmap-engine-new-skill-shared-two-tier-artifact-output-engine.md`
**Files reviewed:** plan, plan-review-1, spec note 28, spec note 30, spec note 27 (existence), `roadmap-decompose/SKILL.md`, `CLAUDE.md`, frontmatter conventions across `src/skills/`
**Risk Level:** 🟢 Low — the plan is well-scoped, accurate against the codebase, and has incorporated every substantive fix from plan-review-1.

---

## Context Gates

- **ARCHITECTURE.md** — the composition doctrine ("mechanism vs policy", engine vs philosophy) is honored: the engine holds only render mechanism, and the explicit "What the engine does NOT own" section keeps all policy (mode, target, gate, confirmation, lenses, silent-failure) in the calling skill. WARN: none.
- **RULES.md / CLAUDE.md conventions** — frontmatter fields, `allowed-tools`, ≤500-line body, relative paths, and the "Custom skills — never overwrite from upstream" registration bucket all match repo conventions. No violations.
- **ROADMAP linkage** — this is a `feat`-shaped milestone (new skill) tracked via the `.ai-factory/plans/` + spec-note workflow (notes 27/28/30 form the family sequence). Linkage is present and coherent. WARN: none.

---

## Verification performed

- **Prior review issue #1 (move → copy) is resolved.** Plan Task 1 body item 4 now says **"copy verbatim"** and carries the explicit guard: *"Do NOT remove this section from `roadmap-decompose/SKILL.md` in this milestone — the duplication is intentional and temporary … the decompose copy is deleted later (spec note 30)."* This matches the milestone's "no consumer is refactored here" scope and pre-empts the single-source-of-truth false positive. ✅
- **Prior review issue #2 (note creation vs update-in-place) is addressed.** Plan Task 1 body item 2 now explicitly states the contract covers **note creation only** (always a fresh `<NN>`), and that in-place update of an existing note (decompose Mode 2.5) is **out of scope for this engine version**, deferred to a later milestone (note 30) that may add an optional existing-note-path input. This closes the forward-looking gap cleanly. ✅
- **Frontmatter matches spec note 28 verbatim.** The `name`, `description`, `user-invocable: false`, `disable-model-invocation: false`, and `allowed-tools: Read Write Edit Glob Grep Skill` block in the plan is byte-identical to note 28 lines 50–59. ✅
- **Both frontmatter fields are valid in this repo.** `disable-model-invocation` is used across many skills; `user-invocable: false` is used in `aif-skill-generator/templates/research.md`. The `false`/`false` pairing correctly makes the engine a non-slash-command that callers invoke via the Skill tool. No `argument-hint` needed. ✅
- **Line references are correct.** "Two-Tier Output (per task)" in `roadmap-decompose/SKILL.md` is at lines 284–298; steps 3–5 (aif-note load + write note + write contract line) are exactly the render steps, and steps 1–2 (draft spec + Atomicity Gate) are correctly excluded as policy. The "Roadmap File Format" section is at lines 302–323 as the plan states. ✅
- **`Glob`-not-`find` is consistent with allowed-tools.** Note 28 line 22 hedges "`Glob`/`find`", but the plan pins note-number scanning to `Glob` — correct, since `allowed-tools` has no `Bash`. The plan improved on the note here. ✅
- **`$TARGET_FILE` → "caller-named roadmap file" adaptation is correct.** The engine must not infer main-vs-test; the plan carries this rule from note 28/74 into both the input-contract and exclusion sections. ✅
- **Task 2 registration targets are correct.** "Custom skills — never overwrite from upstream" (CLAUDE.md line 114) is the right bucket for a brand-new local-only skill; the guard against touching "Intentionally diverged" is present and correct. ✅
- **Clean create.** No pre-existing `src/skills/roadmap-engine/` directory. Spec notes 27, 28, and 30 all exist as referenced. ✅

---

## Critical Issues

None.

---

## Minor / Informational (non-blocking)

### 1. 🟢 Repository Structure tree edit remains cosmetically inconsistent (harmless)
The CLAUDE.md tree (lines 21–41) is illustrative — it uses an `aif-*/` wildcard and does not enumerate every skill (`roadmap-decompose`, `roadmap-prune` is listed but `roadmap-test-coverage`, `observe-logs`, `aif-note` are not). Adding `roadmap-engine/` there is fine but not strictly consistent with its uninlisted siblings. Not a blocker; the plan's short-comment approach is acceptable.

### 2. 🟢 Description advertises a not-yet-wired consumer (`roadmap-decompose-skeleton`)
The engine `description` names `roadmap-decompose-skeleton` as a caller; that skill is still spec note 27 (future milestone). This is acceptable for an incrementally built family — the description is aspirational and does not affect correctness. Carried over from review 1 for the record.

---

## Positive Notes

- **Every actionable item from plan-review-1 was folded into the plan** (copy-not-move + do-not-delete guard, note-creation-only scoping). This is exactly the right response to the prior review.
- **Scope discipline stays excellent** — "create + register only, no consumer refactor" de-risks the extraction; callers migrate one at a time in notes 30/31/32.
- **Mechanism-vs-policy split is clean** and enforced by an explicit exclusion list, matching the repo's composition doctrine.
- **Load-once seams are specified at both hops** (caller → engine, engine → aif-note), preventing per-task re-invocation.
- **"Lift verbatim, don't rewrite"** guarantees the engine and current decompose behavior stay byte-identical, which is what makes the later consumer migration safe.
- **Frontmatter, `allowed-tools`, and registration bucket are all accurate** against actual repo conventions.

---

The plan is sound and implementation-ready. No changes required before implementation.

PLAN_REVIEW_PASS

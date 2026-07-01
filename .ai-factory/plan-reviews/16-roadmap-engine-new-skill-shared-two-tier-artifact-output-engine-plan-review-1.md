# Plan Review: roadmap-engine — shared two-tier artifact-output engine

**Plan:** `.ai-factory/plans/16-roadmap-engine-new-skill-shared-two-tier-artifact-output-engine.md`
**Files reviewed:** plan, spec note 28, spec note 30, `roadmap-decompose/SKILL.md`, `CLAUDE.md`, frontmatter conventions across skills
**Risk Level:** 🟡 Low–Medium — the plan is well-scoped and accurate; one wording hazard should be fixed before implementation.

---

## Verification performed

- **Frontmatter fields are valid.** `user-invocable` and `disable-model-invocation` are both recognized fields already used in the repo (`aif-note`, `roadmap-test-coverage`, and many others). `user-invocable: false` + `disable-model-invocation: false` correctly makes the engine non-slash-command but Skill-tool-invocable by callers. No `argument-hint` needed (only user-invocable skills carry one). ✅
- **`allowed-tools: Read Write Edit Glob Grep Skill` is sufficient and consistent.** No `Bash` is required — note-number scanning uses `Glob` (the plan says `Glob`, not `find`), note+roadmap writes use `Write`/`Edit`, aif-note load uses `Skill`. ✅
- **Line references are correct.** "Two-Tier Output (per task)" steps 3–5 in `roadmap-decompose/SKILL.md` are exactly the aif-note-load + write-note + write-contract-line steps (steps 1–2 are draft-spec + Atomicity Gate, correctly excluded as policy). The "Roadmap File Format" section is at lines 302–323 as stated. ✅
- **Input contract matches the spec note.** `{ task name, full spec, target roadmap file }` and the "engine never infers main-vs-test" rule match note 28 verbatim. ✅
- **Exclusion list matches note 28.** Mode determination, exploration, `AskUserQuestion`, Atomicity Gate, skeleton lenses, silent-failure, target selection — all correctly kept in the philosophy caller. ✅
- **Task 2 registration targets are correct.** The "Custom skills — never overwrite from upstream" list (CLAUDE.md line 114) is the right bucket for a brand-new local skill; not "Intentionally diverged." ✅
- **No pre-existing `roadmap-engine/` directory** — this is a clean create. ✅

---

## Critical Issues

None that block implementation.

---

## Issues to Address

### 1. 🟡 "move verbatim ... from roadmap-decompose" contradicts the milestone's stated scope (copy, don't delete)

Task 1, body item 4 says:

> "**move verbatim** the entire 'Roadmap File Format' section **from** `roadmap-decompose/SKILL.md` (lines ~302–323) ... This becomes the engine's ... single source of truth."

The word **"move"** (and "from roadmap-decompose") reads as *delete from decompose*. But:

- The plan's own Context states: *"This milestone only creates and registers the engine — **no consumer is refactored here**."*
- Task 1's `Files:` list is only `src/skills/roadmap-engine/SKILL.md`; Task 2's is only `CLAUDE.md`. `roadmap-decompose/SKILL.md` is **not** in scope for either task.
- Spec **note 30** (`30-roadmap-decompose-render-via-engine.md`, line 26) explicitly assigns the deletion of decompose's "Roadmap File Format section" and its Two-Tier steps to a **separate later milestone**.

If an implementer takes "move" literally and deletes the section from `roadmap-decompose`, they would (a) exceed this milestone's declared scope, and (b) break `roadmap-decompose` — it would lose its format/render definition while still not routing through the engine (that routing is milestone 30). The result is a temporarily broken decompose.

**Fix:** Change "move verbatim" → **"copy verbatim"**, and add an explicit guard: *"Do NOT remove this section from `roadmap-decompose/SKILL.md` in this milestone — the duplication is intentional and temporary; the decompose copy is deleted later when decompose is refactored to render via the engine (spec note 30)."* This also pre-empts a reviewer flagging the temporary two-copies-of-the-format state as a single-source-of-truth violation.

(Note: the same ambiguity exists in note 28, which uses both "extracted"/"moved" and "copy"; the note's line 13 clarifies "copy ... into the engine." The plan should carry that clarification explicitly so the implementer doesn't have to infer it.)

---

## Minor / Informational

### 2. 🟢 Engine render procedure covers only note *creation*, not in-place note *update*

The lifted steps 3–5 (and the plan's per-task procedure) always **create a new note** (scan `.ai-factory/notes/` for the next `<NN>`). `roadmap-decompose` Mode 2.5 ("Decompose Existing") has an *update-the-existing-note-in-place* branch (SKILL.md lines 208–210). The engine's input contract `{ name, full spec, target roadmap file }` has no field to express "update existing note at path X."

This is **not a defect for this milestone** — the engine is only being created here, and note 30 owns the decompose refactor. But when milestone 30 routes Mode 2.5 through the engine, the contract will need an optional "existing note path" input or the update-in-place semantics will regress to always-create-new. Worth capturing now as a known forward-looking gap so the engine's input-contract section can be written to accommodate it (or explicitly note that update-in-place is out of the current engine's contract).

### 3. 🟢 Repository Structure tree edit is cosmetically inconsistent (harmless)

Task 2 adds `roadmap-engine/` to the CLAUDE.md tree, but that tree (lines 21–41) is an **illustrative** listing using an `aif-*/` wildcard and does not enumerate every skill — `roadmap-decompose`, `roadmap-test-coverage`, `observe-logs`, `aif-note`, etc. are all absent. Adding `roadmap-engine/` while its sibling `roadmap-decompose/` is not listed is slightly odd but harmless. Consider either adding a short comment as planned (fine) or leaving the tree alone; not a blocker either way.

### 4. 🟢 Description references a not-yet-existing consumer (`roadmap-decompose-skeleton`)

The engine `description` names `roadmap-decompose-skeleton` as a caller, but that skill does not exist yet (it is spec note 27, a future milestone). This is acceptable for a family being built out incrementally — the description is aspirational — and does not affect correctness. Just be aware the engine will ship advertising a consumer that isn't wired up yet.

---

## Positive Notes

- **Scope discipline is excellent.** "Create + register only, no consumer refactor" is exactly right for de-risking an engine extraction — the callers migrate one at a time in later milestones (notes 30/31/32).
- **The mechanism-vs-policy split is clean and matches the repo's composition doctrine** (CLAUDE.md "Composition — mechanism vs policy"): the engine holds only render mechanism; every decision (mode, target, gate, confirmation, lenses) stays in the philosophy caller. The explicit "What the engine does NOT own" section enforces this.
- **Load-once seam is correctly specified** at both hops (caller → engine, engine → aif-note), preventing per-task re-invocation.
- **"Lift verbatim, don't rewrite"** is the right instruction for the format section and render steps — it guarantees the engine and the current decompose behavior stay byte-identical, which is what makes the later consumer migration safe.
- **Frontmatter, allowed-tools, and registration bucket are all accurate** against actual repo conventions.

---

Address issue #1 (change "move" → "copy" + add the do-not-delete-from-decompose guard) before implementation. Issues #2–#4 are informational and do not block. With #1 clarified, the plan is sound.

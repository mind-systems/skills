# Plan: roadmap-decompose: extract `roadmap-engine` (artifact format) from the philosophy

## Context
Rewrite `roadmap-engine` from a rigid render *procedure* (input contract, per-task steps, save-ownership, phantom "append-only" limits) into the shared **explanation of the roadmap artifacts** — the contract-line format + two-tier note — verbatim from decompose's format sections; then trim `roadmap-decompose` to the philosophy remainder that references the engine for format.

## Caller reality (read before implementing)
Verified against the codebase — the engine's "3 callers" framing is aspirational, not current:
- **`roadmap-decompose`** is the **only real caller**, and it is *this* plan (Task 3) that first wires it to the engine. Today decompose carries its own inline format + Two-Tier Output procedure.
- **`aif-roadmap`** does **not** invoke the engine (no reference; its `allowed-tools` lacks `Skill`, so it cannot as written). Leave it untouched.
- **`roadmap-decompose-skeleton`** does **not exist** as a skill directory yet — it is only named in the repo's planned-skills list.

Implication: after this plan the engine has exactly one caller, so its descriptions must not silently assert three. The engine is retained as **forward-looking shared-format infra**; wiring `aif-roadmap` / `roadmap-decompose-skeleton` to it is out of scope here and belongs to later milestones. This is a pre-existing condition the plan does not fix beyond making the wording honest (see Task 2).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rebuild the engine as a format explanation

- [x] **Task 1: Rewrite `roadmap-engine/SKILL.md` as the artifact-format explanation (verbatim from decompose)**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Replace the entire body with decompose's format content, moved as-is (same content, not a rewrite):
  - The **"Roadmap File Format"** section — the roadmap structure block (lines 302–314 of current `roadmap-decompose/SKILL.md`) **plus** its "Rules for writing a contract line" list (lines 316–323). Carry these over verbatim.
  - The **two-tier note explanation** as descriptive format knowledge (not numbered steps): each milestone = a contract line in the roadmap + a full spec note; the note is written following `aif-note`'s note format, with `aif-note` loaded once per chat; `<NN>` is scanned against `.ai-factory/notes/` so it never collides; the line ends with the `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag. Keep the "Why two tiers" rationale and the "Never write a full spec inline in the roadmap" rule.
  **Remove entirely** (do not carry over): the "Input Contract" section, the numbered "Per-Task Render Procedure", and the "What This Engine Does NOT Own" list. The engine describes the artifacts; it does not prescribe an append-vs-edit procedure, own the file save, or expose modes/parameters/input signature.
  **Do NOT carry over the Atomicity Gate.** The current inline Two-Tier Output procedure embeds the gate as its step 2 (decompose line 289) — that is philosophy and must stay in decompose (which keeps its standalone 1.3.1 / 2.4.1 gate blocks). The engine holds no gate.
  Reframe the intro paragraph and top-of-body sentence away from "render layer / receives a confirmed task / renders when handed work" toward "shared explanation of the roadmap artifacts, applied contextually by the one agent." Keep `load-once` guidance.
  **Guard:** the engine body must be decompose's removed format text as **the same content, reflowed from numbered steps into prose** — no invented modes, no procedure, no input contract, no append-only/insertion-point/content-return machinery, no "does NOT own" list. (Content preserved; only the form changes from steps to descriptive knowledge.)

- [x] **Task 2: Update `roadmap-engine` frontmatter description**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Rewrite the `description` field so it no longer says "Renders a confirmed task … and saves the roadmap" (procedure/API framing). Describe it as the shared **explanation of the canonical two-tier roadmap artifact format** (contract line + spec note) applied by the calling agent. **Do not assert three callers.** Name `roadmap-decompose` as the current caller and describe the engine as forward-looking shared-format infra for the roadmap family (not "invoked by roadmap-decompose, roadmap-decompose-skeleton, and aif-roadmap"). State it holds no decomposition philosophy; load-once. Keep `name`, `user-invocable`, `disable-model-invocation`, and `allowed-tools` unchanged.

### Phase 2: Trim decompose to the philosophy remainder

- [x] **Task 3: Trim `roadmap-decompose/SKILL.md` to the philosophy + reference the engine** (depends on Task 1)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  - **Remove** the "Roadmap File Format" section (lines 302–323) and the inline two-tier render detail — the "Two-Tier Output (per task)" procedure block (lines 284–298) — since both now live in the engine.
  - **Collapse the orphaned `---` separators** left behind by those removals (the horizontal rules that surrounded lines 284–298 and 302–323) so the philosophy body reads cleanly with no doubled/dangling rules.
  - Where decompose produces artifacts, replace **all five** references to the removed "Two-Tier Output" procedure with: "load `roadmap-engine` once for the artifact format, then produce the two-tier artifacts per that format." The five references are at lines **136** (Mode 1 Step 1.4 finalization), **187** (Mode 2.4 Add New Tasks), **198** (Mode 2.4.1 Atomicity Gate, closing "→ proceed with the Two-Tier Output procedure"), and **208 + 210** (Mode 2.5 Decompose Existing). The agent renders per each mode using the engine's format — create writes the file, add appends, decompose-existing edits the named note in place — with **no** scaffold/append-only/content-return/insertion-point machinery (there is no rigid engine procedure to work around).
  - Update the frontmatter `description` and the intro line (line 16): the two-tier entry is "rendered per `roadmap-engine`'s format" instead of "written manually following aif-note's note format."
  - Update Critical Rule 6 (line 332) to point at the engine's format rather than restating "written manually following aif-note's note format."
  - **Keep byte-identical** — the philosophy text is unchanged in wording: Step 0 context loading, Step 1 target/mode determination, the Atomicity Gate blocks (Steps 1.3.1 and 2.4.1), the mode *structure and descriptions* (create / update / decompose-existing / reprioritize / check), exploration steps, and every `AskUserQuestion` block.
  - **Carve-out to the byte-identical guard:** the *only* spans that change inside the mode descriptions are their `Two-Tier Output` references — lines 136 / 187 / 198 / 208 / 210 — repointed at the engine per the bullet above. Note that **line 198 lives inside the Step 2.4.1 Atomicity Gate block**: the gate's *decision logic and wording* (the yes/no branches, the "make sense" definition) stay verbatim, but its trailing `Two-Tier Output procedure` reference is repointed like the others so no pointer to the deleted section survives (e.g. "→ the task is atomic; produce the two-tier artifacts per the engine's format"). Step 1.3.1's gate needs no such edit — it closes by pointing at "Step 1.4", which stays. Everything else in those modes — the gate wording and all `AskUserQuestion` blocks — stays verbatim. (This resolves the byte-identical-vs-repoint contradiction: the guard protects mode/gate wording *except* the five Two-Tier Output references being repointed.)
  **Guard:** decompose must no longer restate the roadmap/contract-line format or the numbered Two-Tier Output procedure anywhere; its philosophy wording is otherwise unchanged.

- [x] **Task 4: Verify the split** (depends on Task 3)
  Files: `src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`
  Confirm: (a) the engine body is decompose's original "Roadmap File Format" + two-tier note content — same content reflowed to prose, not a rewrite; (b) decompose no longer contains the format block, contract-line rules, or the numbered Two-Tier Output procedure, and has no orphaned `---` separators; (c) decompose's philosophy (Atomicity Gate wording, mode descriptions, exploration, `AskUserQuestion`) is unchanged apart from the repointed Two-Tier Output references; (d) the engine has no Input Contract, Per-Task Render Procedure, modes, Atomicity Gate, or "does NOT own" list; (e) neither skill's description asserts the false 3-caller set. **Do not** modify `aif-roadmap` or `roadmap-decompose-skeleton` in this task.

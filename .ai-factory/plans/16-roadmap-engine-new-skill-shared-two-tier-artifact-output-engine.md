# Plan: roadmap-engine: new skill — shared two-tier artifact-output engine

## Context
Extract the two-tier artifact-render machinery (spec note + ~600-char contract line, canonical roadmap format) out of `roadmap-decompose` into a new content-only engine skill `roadmap-engine`, so `roadmap-decompose`, `roadmap-decompose-skeleton`, and `aif-roadmap` all render through one source of truth. This milestone only *creates and registers* the engine — no consumer is refactored here.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the engine skill

- [x] **Task 1: Create the `roadmap-engine` SKILL.md**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Create the new skill package with a single `SKILL.md`. Follow the exact structure below.

  **Frontmatter** (copy verbatim from spec note `28-roadmap-engine-skill.md`):
  ```yaml
  ---
  name: roadmap-engine
  description: >-
    Shared output engine for the roadmap family. Renders a confirmed task into the
    canonical two-tier roadmap artifact — a ~600-char contract line plus a full spec
    note written via aif-note — and saves the roadmap. Invoked by roadmap-decompose,
    roadmap-decompose-skeleton, and aif-roadmap; holds no decomposition philosophy of
    its own. Caller stays in control; load-once.
  user-invocable: false
  disable-model-invocation: false
  allowed-tools: Read Write Edit Glob Grep Skill
  ---
  ```

  **Body** — author these sections, keeping engine = mechanism only (no policy):
  1. **Intro / role** — one paragraph: this is the shared output/render layer for the roadmap family; it owns the *form* of external artifacts (contract line + spec note + roadmap format), not any decomposition philosophy. The calling philosophy skill stays in control; the engine renders when handed a confirmed task. Load-once at each seam.
  2. **Input contract** — the engine receives one confirmed task = `{ task name, full spec, target roadmap file }`. The caller drafts the full spec and **names the target roadmap file**; the engine writes there and **never infers main-vs-test** from keywords. State explicitly that the current contract covers **note creation only** (always allocates a fresh `<NN>`); in-place update of an existing note (decompose Mode 2.5's "Decompose Existing" branch) is **out of scope for this engine version** — a later milestone (spec note 30) may extend the contract with an optional existing-note-path input when it routes that branch through the engine.
  3. **Per-task render procedure** — lift verbatim from `src/skills/roadmap-decompose/SKILL.md` "Two-Tier Output (per task)" steps 3–5 (the aif-note load-once + write note + write contract line steps), adapted so the target is "the target roadmap file the caller named" rather than `$TARGET_FILE`. Concretely:
     - Ensure `aif-note` is loaded once in this chat (invoke via Skill only if not already invoked; never re-invoke per task).
     - Write the spec note manually with `Write`, following aif-note's in-context format → `.ai-factory/notes/<NN>-<slug>.md`; determine `<NN>` by scanning existing `.ai-factory/notes/` (`Glob`) so it never collides; `<slug>` = lowercase, hyphenated task name.
     - Write the ~600-char contract line (range 400–1000) to the caller-named roadmap file, naming key files/types/guards, ending with the exact tag `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``
     - Save the roadmap.
     - Keep the "Why two tiers" and "aif-note at most once per chat" clarifications.
  4. **Roadmap File Format** — **copy** verbatim the entire "Roadmap File Format" section from `roadmap-decompose/SKILL.md` (lines ~302–323): the markdown skeleton (`# Project Roadmap` / vision one-liner / `## Milestones` / contract-line bullets with `Spec:` tag) **and** the "Rules for writing a contract line" list. This becomes the engine's canonical source of truth for the format. **Do NOT remove this section from `roadmap-decompose/SKILL.md` in this milestone** — the duplication is intentional and temporary. `roadmap-decompose` is not refactored here (its `Files:` are out of scope); the decompose copy is deleted later, when decompose is migrated to render via the engine (spec note 30). Until then, two copies of the format coexist by design — not a single-source-of-truth violation.
  5. **What the engine does NOT own** — explicit exclusions (from the note): no mode determination (create/update/check), no codebase exploration, no `AskUserQuestion` confirmation, no Atomicity Gate, no skeleton lenses, no silent-failure rule, no target main-vs-test selection. All of that stays in the calling philosophy skill.

  Guards: do not add a second/rewritten roadmap format — this is the sole copy; do not re-document aif-note's note template (load aif-note for it); do not drive interaction; body ≤ 500 lines; all content in English; relative paths only.

### Phase 2: Register the skill

- [x] **Task 2: Register `roadmap-engine` in CLAUDE.md** (depends on Task 1)
  Files: `CLAUDE.md`
  Two edits:
  - Add `roadmap-engine` to the **Repository Structure** tree under `src/skills/` (add a `roadmap-engine/` entry with a short comment, e.g. `# two-tier artifact-output engine`).
  - Add `roadmap-engine` to the **Upstream Sync → "Custom skills — never overwrite from upstream"** list so the next upstream sync never wipes this local-only skill.

  Guard: do not touch the "Intentionally diverged" or other Upstream Sync lists; this is a brand-new local skill, so "never overwrite" is the correct bucket.

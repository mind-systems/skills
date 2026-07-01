# roadmap-engine: shared two-tier artifact-output engine

**Date:** 2026-06-30
**Source:** conversation context

> **⚠️ Superseded by note 30.** This note frames the engine as a render *procedure* / *layer* that callers "hand a task to" — that framing is wrong and caused milestone 18 to loop 3× at review. The engine is the shared **explanation of the roadmap artifacts** (format + rules), applied contextually by the one agent — **not** a procedure/API/modes. Note 30 is authoritative for the corrected extraction; follow it, not the procedure framing below.

## Key Findings

- New skill `roadmap-engine` — the shared **output/render layer** for the roadmap family. It owns the *form of external artifacts*, not any decomposition philosophy.
- Content extracted from `roadmap-decompose/SKILL.md`: the rendering steps of "Two-Tier Output (per task)" (the aif-note load + write note + write contract line) and the entire "Roadmap File Format" section.
- Consumers: `roadmap-decompose`, `roadmap-decompose-skeleton`, `aif-roadmap` — each hands the engine a confirmed task and the engine renders it. The engine in turn invokes `aif-note` (load-once) for the note format.
- **Caller stays in control.** The engine is loaded for its *content* (the render procedure); the philosophy skill drives the run. Load-once at each seam: a caller ensures `roadmap-engine` is loaded once per chat; the engine ensures `aif-note` is loaded once per chat.
- The engine does **not** own decomposition, target selection, modes, interaction, or any gate. It receives already-decided tasks and renders them.
- **The moved text is lifted verbatim** from `roadmap-decompose`: copy the exact "Roadmap File Format" section + "Two-Tier Output" steps 3–5 into the engine. The reproductions below in this note are pointers to that source text, **not** a rewrite to follow — the source skill is authoritative.

## Details

### What the engine owns — the per-task render procedure

Input: one confirmed task = `{ task name, full spec, target roadmap file }` — the philosophy skill drafts the full spec and **names the target roadmap file**. The engine writes there; it never infers main-vs-test from keywords.

1. Ensure `aif-note` is loaded once in this chat (if not yet invoked, invoke via Skill; if already, do not re-invoke).
2. Write the spec note manually, following aif-note's in-context format → `.ai-factory/notes/<NN>-<slug>.md`. Determine `<NN>` by scanning existing notes (`Glob`/`find`) so it never collides; `<slug>` = lowercase, hyphenated task name.
3. Write the **contract line** to the **target roadmap file the caller named**: target ~600 chars (range 400–1000), naming the key files, types, and guards, ending with the exact tag `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` The engine compresses the full spec into the contract line — that compression is the "form" work.
4. Save the roadmap.

### The roadmap file format (moved here from decompose)

The engine owns the canonical roadmap structure and contract-line rules:

```markdown
# Project Roadmap

> <project vision — one-liner>

## Milestones

- [ ] **Name** — <problem today + the exact change + key files/types/guards>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
```

Contract-line rules (verbatim from decompose's current "Roadmap File Format"): name specific files/methods/types; state the problem before the change; name guards only for real pitfalls; ~600 chars; always end with the `Spec:` tag; one reason to revert; full detail lives in the note.

### What the engine does NOT own

Mode determination (create/update/check), codebase exploration, `AskUserQuestion` confirmation, the Atomicity Gate, the three skeleton lenses, the silent-failure rule. All of that stays in the calling philosophy skill — the engine is purely the artifact form.

### Frontmatter

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

### Files

- Create `src/skills/roadmap-engine/SKILL.md`.
- Register `roadmap-engine` in `CLAUDE.md` → "Custom skills — never overwrite from upstream" and the Repository Structure tree.

### What NOT to do

- No decomposition philosophy or gate inside the engine.
- Do not drive interaction — the caller stays in control; the engine renders when handed a task.
- Do not re-document aif-note's note format — load aif-note for it (load-once).
- Do not invent a second roadmap format — this is the single source of truth that decompose/skeleton/aif-roadmap all render through.
- Do not infer the target roadmap file (main vs test) — the caller names it; the engine writes where told. Selecting main-vs-test is a philosophy decision (skeleton's TDD tasks go to the main roadmap, test-coverage's go to the test roadmap), so it cannot be a content heuristic in the engine.

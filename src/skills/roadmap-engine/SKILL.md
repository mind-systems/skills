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

# Roadmap Engine — Shared Two-Tier Artifact Output

This is the shared output/render layer for the roadmap family. It owns the *form* of
the external artifacts — the contract line, the spec note, and the roadmap file
format — not any decomposition philosophy. The calling philosophy skill (`roadmap-decompose`,
`roadmap-decompose-skeleton`, `aif-roadmap`) stays in control of what to build and when;
this engine renders a task once the caller has already decided it. Load this skill
once per chat at each seam where a caller needs to render a task.

## Input Contract

The engine receives one confirmed task:

```
{ task name, full spec, target roadmap file }
```

The caller drafts the full spec and **names the target roadmap file** — the engine
writes there and **never infers main-vs-test** from keywords. Selecting the correct
target (e.g. main roadmap vs. test roadmap) is a philosophy decision made by the
caller, not a content heuristic in this engine.

**Scope of this contract version:** note *creation* only — the engine always
allocates a fresh `<NN>` and writes a new note. In-place update of an existing note
(the "Decompose Existing" branch of decompose's Mode 2.5) is **out of scope for this
engine version**. A later milestone (spec note 30) may extend the contract with an
optional existing-note-path input when that branch is routed through the engine.

## Per-Task Render Procedure

Run this for every confirmed task handed to the engine:

1. **Ensure `aif-note` is loaded:** if the `aif-note` skill has not yet been invoked in
   this chat, invoke it once now (via the Skill tool) so its note-writing instructions
   are in context; if it has already been invoked, do not invoke it again.
2. **Write the spec note manually** with the `Write` tool, following aif-note's
   in-context instructions — to `.ai-factory/notes/<NN>-<slug>.md` (determine `<NN>` by
   scanning existing files in `.ai-factory/notes/`; `<slug>` = lowercase, hyphenated
   task name). Determine `<NN>` by scanning so it never collides. Use that path
   verbatim in the `Spec:` tag.
3. **Write the contract line** to the **target roadmap file the caller named** — target
   ~600 characters (range 400–1000; 1000 is an extreme edge), naming the key files,
   types, and guards (the "signature"), ending with the exact tag
   `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``
4. **Save the roadmap.**

**Why two tiers:** the contract line lets the user verify intent while fitting 3–4
tasks on screen; the note holds the full implementation detail. The char budget is
guidance, not a hard clamp.

**`aif-note` is invoked at most once per chat** to load its instructions, never per
task; when writing several notes, scan existing note numbers first so `<NN>` never
collides.

**Never write a full spec inline in the roadmap** — the contract line is the header;
the note is the implementation.

## Roadmap File Format

```markdown
# Project Roadmap

> <project vision — one-liner>

## Milestones

- [ ] **Name** — <problem today + the exact change + key files/types/guards involved>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
- [ ] **Name** — <same pattern>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
- [x] **Name** — <same pattern>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
```

**Rules for writing a contract line:**
- Name the specific files, methods, types, or fields involved — not just the module
- State the problem today before stating what needs to change
- Name guard conditions ("do not touch X", "skip Y") only for real pitfalls, not obvious things
- Target ~600 characters (range 400–1000) — enough to verify intent, short enough to fit 3–4 tasks on screen
- Always end with the `Spec:` tag pointing at the spec note
- One reason to revert — if two concerns are independently shippable, make two milestones
- Full current-state / target / guards / verify detail lives in the spec note, not the roadmap line

## What This Engine Does NOT Own

- Mode determination (create / update / check)
- Codebase exploration
- `AskUserQuestion` confirmation
- The Atomicity Gate
- The skeleton lenses
- The silent-failure rule
- Target main-vs-test selection

All of the above stays in the calling philosophy skill. This engine receives
already-decided tasks and renders them — it does not decide what to build, when, or
where.

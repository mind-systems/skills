---
name: roadmap-engine
description: >-
  Shared explanation of the canonical two-tier roadmap artifact format — a ~600-char
  contract line plus a full spec note written via note — applied by the calling
  agent. Currently loaded by roadmap-decompose; retained as forward-looking
  shared-format infra for the rest of the roadmap family. Holds no decomposition
  philosophy of its own. Load-once.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
loads: note
---

# Roadmap Engine — Shared Two-Tier Artifact Format

This is the shared explanation of the roadmap artifacts — the contract line, the spec
note, and the roadmap file format — not any decomposition philosophy. The calling
philosophy skill (currently `roadmap-decompose`) stays in control of what to build and
when; this engine describes the artifact format the caller applies once a task is
decided. **Load this skill once per chat** — once loaded, the format stays in context; never re-invoke it per task or per mode.

## The two-tier artifact

Each milestone is a two-tier entry: a contract line in the roadmap plus a full spec
note at `.ai-factory/notes/<NN>-<slug>.md` (`<NN>` scanned against `.ai-factory/notes/`
so it never collides; `<slug>` lowercase-hyphenated). The contract line ends with the
exact tag `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``

The note follows `note`'s format — **load `note` once per chat** (via the Skill
tool, only if not already loaded), never per task.

**Why two tiers:** the contract line lets the user verify intent while fitting 3–4
tasks on screen; the note holds the full implementation detail. The char budget below
is guidance, not a hard clamp.

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

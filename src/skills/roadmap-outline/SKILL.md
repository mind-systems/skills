---
name: roadmap-outline
description: Create or update a project roadmap with major milestones. Generates .ai-factory/ROADMAP.md — a strategic checklist of high-level goals. Use when user says "roadmap", "project plan", "milestones", or "what to build next".
argument-hint: "[check | project vision or requirements]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill
loads: roadmap-engine
disable-model-invocation: true
---

# Roadmap - Strategic Project Planning

Create and maintain a high-level project roadmap where every milestone is a strategic
goal, rendered per `roadmap-engine`'s two-tier format.

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) and run its **Roadmap maintenance flow** with the hooks below.

## Hooks for `roadmap-engine`'s flow

### (a) Granularity

Each entry is a **high-level goal** — a capability the system gains, not a task
(that's `/roadmap-decompose`). 5–15 milestones is the sweet spot: fewer means too
vague, more means too granular. Milestones later serve as **phase names** for the
decomposition pass. Order by logical sequence (dependencies first).

Two parity carry-overs the engine's create flow does not itself hold:
- On first run, mark already-completed milestones as `[x]`.
- Create-mode gather-input question (fills the engine's
  `AskUserQuestion: <caller phrases this…>` placeholder): *"What are the major goals
  for this project?"*

Two-tier rendering at this tier: entries render per the engine's format (contract line
+ spec note) at strategic granularity; the vision line is sourced from user input.
The spec note is **optional at this tier** — when the
contract line alone fully carries the milestone (often just a named capability), skip
the note and end the entry with no `Spec:` tag rather than pointing at an invented
one. Write a note only when there is real strategic content the line can't hold
(constraints, ordering rationale, scope boundaries) — never pad a note to justify its
existence; `roadmap-decompose` writes the real notes later.

### (b) Per-entry gate

None. Outline supplies no per-entry gate hook — restraint at the strategic tier is the
5–15 rule, not a split gate. Do not improvise an atomicity-style gate here; that is
decompose's gate.

### (c) Target-file routing

Always `.ai-factory/ROADMAP.md` — trivial policy, no keyword/argument branching.

### (d) Extra update-mode actions

None beyond the engine's built-in menu (review progress / add / reprioritize /
rewrite). Outline registers no added action.

## Critical Rules

1. **Milestones are high-level** — granular tasks belong to `/roadmap-decompose`.
2. **Every milestone renders two-tier per `roadmap-engine`'s format** — but the spec
   note is optional at this tier (per hook a); never invent note content to fill a
   `Spec:` tag.
3. **NO implementation** — this skill only plans; the orchestrator implements in a
   separate run.

---
name: roadmap-outline
description: Create or update a project roadmap with major milestones. Generates .ai-factory/ROADMAP.md — a strategic checklist of high-level goals. Use when user says "roadmap", "project plan", "milestones", or "what to build next".
argument-hint: "[project vision or requirements]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill
loads: roadmap-engine
disable-model-invocation: true
---

# Roadmap - Strategic Project Planning

Create and maintain a high-level project roadmap where every direction breaks into
**phases** — headers with prose intros, per `roadmap-engine`'s format. Tasks under
those phases are `/roadmap-decompose`'s tier, not this skill's.

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) and run its **Roadmap maintenance flow** with the hooks below.

## Hooks for `roadmap-engine`'s flow

### (a) Granularity

Each entry is a **phase**: a `### Phase N — <Title>` header plus a prose intro
paragraph (the gate/"blocked on X", the problem today, key contracts and pinned
decisions the phase rests on) — **never a checkbox bullet, no contract line, no
`Spec:` tag**. 5–15 phases is the sweet spot: fewer means too vague, more means too
granular. Phases are what `/roadmap-decompose` fills with tasks. Order by logical
sequence (dependencies first).

Numbering: continue from the highest phase number anywhere in the file (per the
engine's file-level invariant) — never restart at 1, even for the first phases of a
new direction. When creating the first phases of a new direction section, also emit
the `##` direction header and its preamble prose.

One parity carry-over the engine's create flow does not itself hold:
- Create-mode gather-input question (fills the engine's
  `AskUserQuestion: <caller phrases this…>` placeholder): *"What are the major goals
  for this project?"*

Links to handoff/spec notes are allowed as plain markdown links inside the intro/
preamble prose — no formal `Spec:` tag, no invented notes.

### (b) Per-entry gate

None. Outline supplies no per-entry gate hook — restraint at the strategic tier is the
5–15 rule, not a split gate. Do not improvise an atomicity-style gate here; that is
decompose's gate.

### (c) Target-file routing

Always `.ai-factory/ROADMAP.md` — trivial policy, no keyword/argument branching.

### (d) Extra update-mode actions

None beyond the engine's built-in menu (review progress / add / reprioritize /
rewrite). Outline registers no added action.

## Check mode

Outline registers no check mode. With no checkboxes at the phase tier there is
nothing to scan or mark — phase progress is a derivative of its tasks (`N.M`
checkboxes, `/roadmap-decompose`/`roadmap-prune` territory). Create and update
modes, and the engine's confirm cycle, work as described above.

## Critical Rules

1. **Phases are high-level** — granular tasks belong to `/roadmap-decompose`.
2. **Phases render as headers + prose per the engine's format** — never a checkbox,
   never a `Spec:` tag; tasks are decompose's tier.
3. **NO implementation** — this skill only plans; the orchestrator implements in a
   separate run.

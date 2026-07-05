---
name: roadmap-decompose
description: >-
  Create or update a project roadmap with atomic, granular milestones. Each roadmap
  entry is a ~600-char contract line naming the key files, types, and guards, with
  the full spec persisted as a note, rendered per roadmap-engine's format. Use when user says
  "decompose", "break down tasks", "spec tasks", "create tasks", or when adding
  milestones that need to be implementation-ready.
argument-hint: "[check | task description or requirements]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill
loads: roadmap-engine
disable-model-invocation: true
---

# Decompose — Granular Task Planning

Create and maintain a project roadmap where every milestone is a two-tier entry: a
contract line in the roadmap and a full spec note, rendered per `roadmap-engine`'s
format.

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) and run its **Roadmap maintenance flow** with the hooks below.

## Hooks for `roadmap-engine`'s flow

### (a) Granularity

Each entry is **one atomic task** — one file boundary, one concern, one reason to
revert. Two-tier discipline applies: a contract line in the roadmap plus a full spec
note per `roadmap-engine`'s format — never a full spec inline. Order entries by
logical sequence (dependencies first).

Numbering: tasks render as flat checkbox bullets directly under their parent
`### Phase N` header, numbered `**N.M — Name**` (`N` from the header, `M` a 1-based
ordinal continuing after the highest existing `M` in that phase). **Flat fallback:**
when the target file/region has no phase headers, emit unnumbered bullets exactly as
today — never invent a phase header to hang a number on (covers `ROADMAP_TESTS.md`,
legacy flat roadmaps, and this repo's own ROADMAP.md).

Two parity carry-overs the engine's create flow does not itself hold:
- On first run, mark already-completed milestones as `[x]`.
- Create-mode gather-input question (fills the engine's
  `AskUserQuestion: <caller phrases this…>` placeholder): *"What tasks should I
  decompose into the roadmap?"*

### (b) Per-entry gate — the Atomicity Gate

After drafting each entry's full spec, before writing its contract line — apply the
gate:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two entries, apply the gate to each half recursively until no
half passes. If **no** → the entry is atomic.

"Make sense" means: compiles, breaks nothing, and delivers independently observable
value.

### (c) Target-file routing

Resolve `$TARGET_FILE` before the flow runs:
- Default → `.ai-factory/ROADMAP.md`
- An explicit filename argument (e.g. `ROADMAP_TESTS.md`) wins
- Test-context keywords (test, tests, spec, testing, тест, тесты) →
  `.ai-factory/ROADMAP_TESTS.md`

### (d) Extra update action — "Decompose existing"

Register an added update-menu action: expand a vague milestone into a full spec (what
exists today, the exact change, files/types/methods to touch, guards, how to verify).

Note-handling rule:
- Existing `Spec:` tag → update the named note in place with `Write`; the tag stays
  unchanged.
- Legacy inline (no tag) → write a new note per `roadmap-engine`'s format and add the
  `Spec:` tag.
- If the milestone bundles 2+ independent concerns, offer a split (a split → two notes
  + two contract lines). When the target task is already numbered `N.M`, number the
  split per the engine's sub-numbering rule — children `N.M.1 … N.M.k` in chain
  order, with the original line renumbered to the last child `N.M.k`; an unnumbered
  (flat) task's split stays unnumbered.
- Never bulk-migrate untouched legacy tasks.

## Critical Rules

1. **Milestones are atomic and specific** — each is one concern, one reason to revert
2. **Every task is two-tier** — a contract line in the roadmap plus a spec note,
   rendered per `roadmap-engine`'s format; never write a full spec inline in the
   roadmap
3. **NO implementation** — this skill only plans; the orchestrator implements in a
   separate run

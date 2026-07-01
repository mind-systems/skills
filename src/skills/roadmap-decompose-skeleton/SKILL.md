---
name: roadmap-decompose-skeleton
description: >-
  Second decomposition pass over open roadmap tasks along the spec-before-code
  axis (skeleton-first, TDD, concurrency contract) rather than atomic
  deliverability. Extracts interface/abstract skeleton tasks, tests-first tasks
  filtered by test-philosophy's silent-failure rule, and no-prod-code contract-tasks
  for heavy tasks mixing async I/O + stateful buffer + lifecycle. Renders via
  roadmap-engine, sources the test rule from test-philosophy — copies neither. Use
  when a task is heavy/hazardous or shares a type surface and needs splitting
  before implementation. Trigger: "skeleton", "tdd tasks", "concurrency contract".
argument-hint: "[phase/slug or task description]"
disable-model-invocation: true
allowed-tools: Read Write Edit Glob Grep AskUserQuestion Skill
---

# Roadmap Decompose Skeleton — Skeleton / TDD / Concurrency Decomposition Lens

A **second** decomposition pass over already-atomic **open** `[ ]` roadmap tasks. Where
`roadmap-decompose` splits on atomic deliverability, this skill splits the same tasks
along the **spec-before-code** axis: does the surface need a skeleton laid first, does
it need tests written against that skeleton before the implementation, does it need a
concurrency contract before touching a hazardous concurrent surface. It applies to
heavy or hazardous tasks and shared type surfaces only — most open tasks pass through
untouched.

## Load-once / dependencies

This skill owns no reusable body of its own — only the three lenses below (targeting,
skeleton, TDD, concurrency, ordering/fusion, restraint). Everything reusable is
delegated to two shared skills, each loaded **once per chat** via the `Skill` tool and
never re-invoked per task:

- `roadmap-engine` — the shared two-tier artifact format (contract line + spec note)
  that every lens renders its output through.
- `test-philosophy` — the silent-failure discriminator the TDD lens applies to decide
  what gets a test.

Call graph:

```
roadmap-decompose-skeleton ─→ roadmap-engine ─→ note
                           └─→ test-philosophy
```

This skill does **not** call `roadmap-decompose` at runtime — the atomic task list it
operates on already exists; this is a second pass over it, not a re-decomposition. It
never reads or modifies the orchestrator.

## Targeting

Optional arg — a phase, slug, or single task description. Default: infer the target
open-`[ ]` task set from conversation context (a named phase, a described task, or the
current pending set). It can operate on a single task — any task may warrant a
skeleton, TDD, or concurrency split on its own. Do not over-engineer targeting.

## Workflow

### Step 0: Load Project Context

**Read `.ai-factory/DESCRIPTION.md`** if it exists, for tech stack and conventions.

**Read `.ai-factory/ARCHITECTURE.md`** if it exists, for architecture pattern and
module boundaries.

**Read the target roadmap** (`ROADMAP.md`, or the file named by the arg/context) and
collect its open **`- [ ]`** tasks — this is the set the three lenses run over. Never
touch closed `- [x]` tasks — those are `roadmap-prune` / `roadmap-test-coverage`
territory.

### Step 1: Apply the three lenses

**Lens 1 — Skeleton (primary).** Scan the target task(s) for a shared type/interface
surface — shared between 2+ tasks, or a single task whose shape is non-obvious — where
an interface / abstract-class skeleton genuinely makes the surface testable. Where
appropriate, extract a **skeleton task**: interfaces, types, abstract classes only —
**no implementation bodies**. This is the scaffold the TDD lens writes tests against.
- Restraint: contracts/protos are usually laid first anyway — do not blanket-cover
  tasks with abstract classes. Only extract a skeleton where it makes a shared or
  non-obvious surface testable.

**Lens 2 — TDD.** Against the skeleton's public surface, insert a **tests-first task**.
Ensure `test-philosophy` is loaded once this chat, then apply its silent-failure
discriminator: write tests only for surfaces that fail *silently* (wrong output, no
crash); skip surfaces that fail *loudly* (compile error, exception, DI failure, 4xx/5xx).
Not blanket coverage. Canon (m36): a stateless `PassThroughIndicator` double let cases 3
and 4 pass even when `loadHistory` omitted re-instantiation — a stateful double, forced
by writing the test against the skeleton first, would have caught it.

**Lens 3 — Concurrency.** For a **heavy** task (the 45–80 min wall-clock kind) that
touches **≥2 of** three hazard classes — (a) async I/O, (b) stateful buffer / event
queue, (c) lifecycle (create / deactivate) — split out a **contract-task**: invariant
definition plus test scenarios per concurrent caller, **no production code**, before the
impl task.
- Restraint: never split a simple task, even if it nominally touches two classes, into
  a contract-task. Canon (m37): `clearHeap()` traded double-commit for silent loss;
  `drainHeap()` plus a dedup-key merge (buffered wins) fixed it — had the
  drain-and-merge invariant been a contract-task first, it would have been caught at
  plan-review instead of in the field.

### Step 2: Order and fuse

- Default order: **skeleton → TDD → impl**.
- **Fuse** skeleton + red specs into one "contract" milestone when skeleton:impl is
  **1:1** — interfaces/abstract classes plus red tests over the silent-failure points,
  in one commit (compiles, has red tests); the impl milestone turns them green. This
  dissolves both the skeleton↔TDD ordering question and the concurrency-contract↔TDD
  overlap (same artifact).
- **Exception:** when the skeleton is shared across **2+** impl tasks, it becomes its
  own standalone shared-scaffold milestone, and each impl task gets its own TDD task.

### Step 3: Deliverability

"Deliverable" shifts from "working feature slice" to "coherent reviewable artifact in
the spec-before-code chain." A skeleton-only commit compiles and breaks nothing;
TDD/contract commits are red tests. The orchestrator does exactly what the spec
describes — this skill neither reads nor modifies it.

### Step 4: Render

All outputs — skeleton, TDD, and contract tasks alike — render into the **same
`ROADMAP.md`** the source tasks live in, **never** `ROADMAP_TESTS.md` — even the TDD
tasks, since they belong to the impl chain (skeleton → TDD → impl), not the test
roadmap. Ensure `roadmap-engine` is loaded once this chat, then produce the two-tier
artifact (contract line + spec note) for each resulting task per its format. Target-file
selection is this skill's to make (the source roadmap); `roadmap-engine` never infers
it.

**Disposition of the original task:** the original open task already carries a
contract line and a `Spec:` note — it becomes the **impl** milestone. Keep its existing
line and note **in place** (update the note's content to reflect that skeleton/tests
are now separate milestones); do not render a second contract line or a new note for
it. **Insert** the new skeleton/TDD/contract milestones immediately **before** it in
`ROADMAP.md`. This mirrors `roadmap-decompose`'s in-place note-update discipline and
avoids duplicating the impl entry or orphaning its spec note.

## Critical Rules / What NOT to do

1. No `roadmap-tdd` middle skill — the one TDD-specific sentence ("tests come first,
   as their own task, filtered by test-philosophy's rule") lives inline in this skill.
2. Do not copy `roadmap-engine`'s render machinery or `test-philosophy`'s discriminator
   into this skill — load them, once per chat, and let them stay in control of their
   own content.
3. Do not call `roadmap-decompose` at runtime — the atomic task list already exists;
   this is a second pass over it.
4. Do not read or modify the orchestrator.
5. Do not split simple tasks, blanket-cover surfaces with abstract classes, or write
   tests for loud-failure surfaces — restraint is first-class; this skill earns its
   keep only on heavy, hazardous, or shared-surface tasks.
6. Do not touch closed `- [x]` tasks — that is `roadmap-prune` / `roadmap-test-coverage`
   territory.

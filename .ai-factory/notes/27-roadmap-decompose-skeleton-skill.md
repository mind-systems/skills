# roadmap-decompose-skeleton: skeleton/TDD/concurrency decomposition lens

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- `roadmap-decompose` splits tasks on **atomic deliverability**. There is no pass that splits on **spec-before-code** axes, so heavy tasks (the 45–80 min wall-clock outliers) discover their type shape and concurrency invariants during code-review instead of up front.
- New skill `roadmap-decompose-skeleton` — personal-scope member of the `aif-roadmap` family. Operates on **open** `[ ]` tasks (`roadmap-prune` / `roadmap-test-coverage` work on closed tasks).
- **It does not copy any other skill's body.** It owns only the three-lens analysis, then calls the shared engines for everything reusable:
  - `roadmap-engine` (note 28) — renders the resulting tasks as two-tier roadmap artifacts.
  - `test-engine` (note 29) — the silent-failure rule the TDD lens applies.
- **No `roadmap-tdd` middle skill.** A skill that only routes to test-engine + roadmap-engine with no content of its own is negative value (pays context for pure routing). The one TDD-specific sentence — "tests come first, as their own task" — lives inline in this skill.
- Load-once at each seam: ensure `roadmap-engine` and `test-engine` are each loaded once per chat; do not re-invoke if already loaded.
- All three lenses share one spine — **spec the silent-failure surface before coding it.** Skeleton is the scaffold that makes the surface specifiable; the TDD lens tests it by test-engine's rule; the concurrency contract-task is the same rule applied to the most hazardous silent-failure zone.
- **Restraint is first-class.** Don't split simple tasks, don't blanket-cover with abstract classes, don't test loud-failure surfaces. The skill earns its keep on heavy / hazardous / shared-surface tasks only.

## Details

### Call graph

```
roadmap-decompose-skeleton ─→ roadmap-engine ─→ aif-note
                           └─→ test-engine
```

The skill determines the target, runs the three lenses to produce a sub-atomic task set (with ordering/fusion), then hands each task to `roadmap-engine` to render. For the TDD lens, it loads `test-engine` and applies the silent-failure discriminator against the skeleton surface. It does **not** call `roadmap-decompose` at runtime — the atomic task list it operates on already exists.

All outputs — skeleton, TDD, and contract tasks — render into the **same roadmap the source tasks live in, the main `ROADMAP.md`**, passed to `roadmap-engine` as the target file. The TDD tasks belong to the impl chain (skeleton→TDD→impl), **not** the test roadmap (`ROADMAP_TESTS.md`) — even though they are test tasks. Target-file selection is the caller's; the engine never infers it.

### The three lenses

**1. Skeleton lens (primary).** Scan the target task(s) for a shared type/interface surface — shared between 2+ tasks, or a single complex task whose shape is non-obvious — where an interface / abstract-class skeleton genuinely aids testing. Where appropriate, extract a **skeleton task**: interfaces, types, abstract classes — **no implementation bodies**. This is the scaffold the tests are written against.
- Restraint: proto/contracts are usually laid first anyway; do not blanket-cover code with abstract classes — only extract a skeleton where it makes the surface testable.

**2. TDD lens.** Against the skeleton's public surface, insert a **tests-first task**. Load `test-engine` and apply its silent-failure rule: tests go only where the logic fails *silently*; loud-failure surfaces are skipped. Not blanket coverage. Canon: m36 — a stateless `PassThroughIndicator` double let cases 3 & 4 pass even if `loadHistory` omitted re-instantiation; a stateful double forced by a TDD-against-skeleton task would have falsified it.

**3. Concurrency lens.** A **heavy** task (the 45–80 min kind) that touches **≥2 of three** hazard classes — (a) async I/O, (b) stateful buffer / event queue, (c) lifecycle (create / deactivate) — gets a **contract-task** split out: invariant definition + test scenarios per concurrent caller, **no production code**, before the impl task.
- Restraint: a simple task is never split, even if it nominally touches two classes. Canon: m37 — `clearHeap()` traded double-commit for silent loss → `drainHeap()` + dedupKey merge (buffered wins); had the drain-and-merge invariant been a contract-task first, it would have been caught at plan-review.

### Ordering and fusion

- Default order: **skeleton → TDD → impl**.
- **Fuse skeleton + red specs into one "contract" milestone** when skeleton:impl is **1:1** — interfaces/abstract + red tests over the silent-failure points, in one commit (compiles + has red tests). The impl milestone turns them green. This dissolves both the skeleton↔TDD ordering question and the concurrency-contract↔TDD overlap (same artifact).
- **Exception:** when the skeleton is shared across **2+** impl tasks, it is its own shared-scaffold milestone, and each impl task gets its own TDD task.

### Deliverability

"Deliverable" shifts from "working feature slice" to "coherent reviewable artifact in the spec-before-code chain." A skeleton-only commit compiles and breaks nothing; TDD/contract commits are red tests. The orchestrator does exactly what the spec describes — not read, not modified.

### Frontmatter

```yaml
---
name: roadmap-decompose-skeleton
description: >-
  Second decomposition pass over open roadmap tasks along the spec-before-code
  axis (skeleton-first, TDD, concurrency contract) rather than atomic
  deliverability. Extracts interface/abstract skeleton tasks, tests-first tasks
  filtered by test-engine's silent-failure rule, and no-prod-code contract-tasks
  for heavy tasks that mix async I/O + stateful buffer + lifecycle. Renders results
  via roadmap-engine and sources the test rule from test-engine — copies neither.
  Use when a task is heavy/hazardous or shares a type surface and should be split
  before implementation. Trigger phrases: "skeleton", "decompose skeleton",
  "skeleton first", "tdd tasks", "concurrency contract", "spec before code".
argument-hint: "[phase/slug or task description]"
disable-model-invocation: true
allowed-tools: Read Glob Grep Bash(git *) AskUserQuestion Skill
---
```

### Targeting

Optional arg — a phase, slug, or task description. Default: infer from context what is being decomposed (the pending `[ ]` set, a named phase, or a single described task). It can work on a single task — any task may warrant skeleton + TDD + split. Do not over-engineer targeting.

### Files

- Create `src/skills/roadmap-decompose-skeleton/SKILL.md` (body ≤ 500 lines).
- Register `roadmap-decompose-skeleton` in `CLAUDE.md` → "Custom skills — never overwrite from upstream" and the Repository Structure tree.
- Depends on `roadmap-engine` (note 28) and `test-engine` (note 29) existing first.

### What NOT to do

- Do not create a `roadmap-tdd` skill — its only content (one sentence) lives inline here.
- Do not copy roadmap-engine's output machinery or test-engine's rule into this skill — load them.
- Do not call `roadmap-decompose` at runtime — the atomic task list already exists; this is a second pass.
- Do not read or modify the orchestrator.
- Do not split simple tasks, blanket-cover with abstract classes, or test loud-failure surfaces.
- Do not touch closed tasks (prune / test-coverage territory).

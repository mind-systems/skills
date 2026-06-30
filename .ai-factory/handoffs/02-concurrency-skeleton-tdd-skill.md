# Handoff — concurrency-skeleton-tdd-skill

## 1. Frame
We audited 7 looped indicator-engine milestones in tradeoxy_core and diagnosed two structural gaps in the planning pipeline — one about concurrency concern decomposition, one about skeleton-first + TDD phasing — and the user wants these expressed as a new standalone skill in ~/projects/skills.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `~/projects/skills/` — browse the existing skills to understand the naming convention, directory layout, and SKILL.md format before authoring anything new
- `~/projects/tradeoxy/tradeoxy_core/.ai-factory/ROADMAP.md` lines 135–141 — milestone 37 (Phase 6.2) is the concrete case that motivated this skill; read the contract line and the [1h 14m 29s] wall-clock to feel the cost

### Read on demand
- `~/projects/skills/roadmap-decompose/SKILL.md` — the existing decompose skill; the new skill is a **separate, downstream companion**, not a patch to this one
- `~/projects/tradeoxy/tradeoxy_core/.ai-factory/plan-reviews/37-phase-6-2-*.md` (all 2) and `reviews/37-phase-6-2-*.md` (all 3) — the full artifact chain that revealed the concurrency gap
- `~/projects/tradeoxy/tradeoxy_core/.ai-factory/plans/37-phase-6-2-indicatorruntimeservice-self-warm-public-loadhistory.md` — the plan that the concurrency concern gate would have split

## 3. Current state

**Done:**
- Ran /milestone-rescue-audit in parallel across 7 looped milestones (21, 22, 24, 26, 35, 36, 37)
- Verdicts: 5 independent-legitimate-fixes, 2 mixed
  - 22 and 24: code correct at review 1, reviews 2–3 ran on byte-identical code — process waste, not design rot (missing "non-blocking findings = REVIEW_PASS" rule in reviewer protocol)
  - 37: one real whack-a-mole — `clearHeap()` → traded double-commit for silent loss → `drainHeap()` + merge; root cause: heap-drain-before-replay invariant absent from spec note 50
- Diagnosed that `roadmap-decompose`'s Atomicity Gate (axis: "deployable independently?") cannot catch the 37-class problem (axis: "how many concurrent access patterns must be specified?")
- Decided: new skill, not a patch to decompose — different conceptual planes, different trigger point

**In-flight:**
- New skill not yet written — this handoff is the briefing for that work

**Uncommitted working-tree state:**
- none (audit was read-only)

## 4. Next step
Design and write a new skill in `~/projects/skills/<skill-name>/SKILL.md`. The skill has three independent capabilities the user described — author them as a coherent unit with a clear trigger and workflow:

1. **Concurrency concern gate** — after decompose runs, scan the pending task list for tasks that simultaneously touch (a) async I/O, (b) stateful buffer / event queue, (c) lifecycle (create/deactivate). Any two of three → propose splitting out a "contract task" (invariant definition + test scenarios per concurrent caller, no production code) as a prerequisite, before the implementation task.

2. **Skeleton-first phase** — scan the pending tasks for a shared type/interface surface (shared between 2+ tasks). If found, propose a new task-0 that writes only the skeleton (interfaces, types, abstract classes — no implementation bodies), so downstream tasks implement against a stable contract rather than discovering the shape during code review.

3. **TDD phase** — after skeleton exists (either proposed by step 2 or already committed), offer a "tests-first task" that writes specs against the skeleton's public surface before any implementation. This is a separate task in the roadmap, not bundled with the implementation.

Skill should be **read-only analysis + proposal** (no file writes, no ROADMAP edits) — outputs a chat-only recommendation the user decides whether to act on. Follows the same pattern as `milestone-rescue-audit`.

## 5. Working discipline
- Plan → stop; do not implement until confirmed
- No memory writes unless user says "запомни" / "remember this" / exact trigger phrases
- English in all generated files regardless of conversation language
- No commit without explicit permission

## 6. Error log
*(none this session)*

## 7. Orientation
**`roadmap-decompose` Atomicity Gate vs. the new skill's Concurrency Gate are orthogonal axes:**
- Atomicity Gate: "can half A deploy without half B?" → functional split
- Concurrency Gate: "does this task mix async I/O + stateful buffer + lifecycle?" → hazard-class split
Do not conflate. The new skill is triggered *after* decompose has already produced an atomic task list — it is a second pass over that list, not a replacement of the gate inside decompose.

**Three proposed capabilities are independent but related:**
- Concurrency gate → catches 37-class bugs (clearHeap whack-a-mole)
- Skeleton-first → catches shape-discovery bugs during code review
- TDD phase → catches test-falsifiability bugs (36-class: stateless double can't falsify the guarantee)
All three are "spec-before-code" disciplines applied at different granularities.

## 8. Domain model spine
- **Milestone 37 is the canonical motivating case** — 1h 14m, whack-a-mole on EventBus heap semantics during async I/O gap. The drain-and-merge invariant (`drainHeap()` + dedupKey merge, buffered wins on conflict) was the correct design; `clearHeap()` was the band-aid. Had this invariant been a separate "contract task" first, it would have been caught at plan-review, not code-review round 2.
- **Milestone 36 is the TDD motivating case** — plan-review found CRITICAL: test used stateless `PassThroughIndicator`, so cases 3 & 4 passed even if `loadHistory` omitted re-instantiation. A TDD task against the skeleton interface would have forced a stateful double before the implementation was written.
- **Milestones 22 and 24** are a process issue (reviewer withholding REVIEW_PASS on non-blocking findings), not a planning issue. The new skill does not address these — mention this clearly so the skill author doesn't scope-creep into reviewer protocol.

## 9. Hard rules
- Skill file language: English
- New skill lives in `~/projects/skills/<name>/SKILL.md` — match the directory+SKILL.md layout of existing skills
- Skill is read-only / chat-output-only (no file writes by the skill itself)
- Trigger: runs after `/roadmap-decompose` has produced a task list, before `/aif-implement` starts

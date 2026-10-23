# Phase 95 — the whole flow, from a phase to a landed task

The first account of the whole system in one place, chat and orchestrator together, as the user and head 07 laid it out on 2026-10-23 over phase 80. It is the material this phase's doc is written from: `docs/sakshi-harness/skill-cycle.md` holds only the chat's steps, and lags them; the orchestrator's docs hold its own pipeline apart. The deepening of this phase rewrites this note in place.

## The flow

**At the phase, once for all its tasks.**
1. The user reasons, then `roadmap-outline` drafts the phase, then the user looks at it.
2. Reasoning, then `roadmap-outline-deep`: the phase note, what diverges now, grounded in the code. The razor looks at the update; the third view reads.
3. Docs: the governing doc corrected or written in the genre, with no call to `aif-docs`. Where the skill is its own doc, the step is skipped and the head says so in a line.

**At the task.**

4. Reasoning, then `roadmap-decompose`: the head's hand drafts, the razor reads independently in parallel, the head reconciles the two; the razor reads the written specs again; the third view reads. Cut by reason to revert, by the change a reviewer judges as one; a spec may carry a list.
5. The user's walk over each task: the head explains why it exists and what it does, and he walks them — «по таскам - зачем они и что делают, по каждому. Прохожу я. А не ты с руками».
6. `roadmap-decompose-skeleton` over the whole phase. Skipped in the skills repository, which has no interfaces in the ordinary sense.
7. The orchestrator, started by the user: plan → plan review, up to its round budget → implementation → code review, up to its round budget → commit. Each plan review and each code review round is a fresh session; the planner and the implementer are one session per task.
8. When a task stops: `task-rescue` writes its report with the intended repair and rollback; the third view reads after the diagnosis; the user's word; the repair and rollback run and the report is extended; the orchestrator resumes from the state the rollback left.

**After the phase.**

9. The user asks «есть отложенные наблюдения?». Each is routed to a phase or an open task, or dismissed, and pinned. One met once is parked unless it blocks the goal or has been met again.
10. One phase at a time: «пока она не ляжет, дальше не двигаемся».

**Later.** `roadmap-prune`, by head 08, when the done tasks fill about the first 150 lines of the roadmap.

Under every step of a head runs a round of its hand: the hand writes, the head checks the files. The chronicle of catches and vector turns (`.ai-factory/chronicle/<project>.md`) is added to when a head writes its snapshot.

## Who reads

The user, at three points: after the deepening, after decomposition, at a rescue — «Мне всё равно надо рассуждать и учавствовать после дипа, после декомпоза и на таск рескью. Других рычагов у меня нет. Задавать вектор.» He rules every fork. The builder (07) asks what must exist; the razor (05) asks what should not exist, after every step; the third view (09, Fable) asks whether this goes where the user wants, at his three points. The hand writes and reports. In the orchestrator: the planner, the plan reviewer, the implementer, the reviewer. Five of all these read with a question of their own — the user, the builder, the razor, the third view and the reviewer; the rest execute, or repeat a role for another round.

## What phase 80 showed

Read from its artifacts. 80.2 went the short path: one plan, one plan review, one implementation, one code review. 80.1 spent most of its plan-review budget and passed at its last round. 80.3 spent the whole budget without a pass, was rescued, spent another set of plan reviews, and passed code review on its second round. A task's chat side gives it about as many readings as the orchestrator does; what makes a task expensive is the tail — the review rounds and a rescue.

## Where each piece lives now

- `docs/sakshi-harness/skill-cycle.md` — the chat's order, lagging the user (see this phase's preamble).
- `docs/paired-loop.md` — the head and its hand, personalities, the vector of attention; not when each partner is called.
- `agent-architect` — the pair and the peers; not the cycle (phase 96), not the personalities (phase 85).
- `task-rescue` — the rescue, with its report and its pause.
- The orchestrator's docs — its pipeline and round budgets.
- The heads' buffers — the user's rulings on the cycle, until phases 95 and 96 land.

Nowhere: the flow whole, as above.

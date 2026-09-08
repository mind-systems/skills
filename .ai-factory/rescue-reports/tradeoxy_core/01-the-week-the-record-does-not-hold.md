# The week the record does not hold — orchestrator failures, 2 – 8 September 2026

**Project:** tradeoxy_core
**Date:** 2026-09-08
**Written by:** the lead architect, by hand, not by a rescue run

## What this file is, and why it is not shaped like its neighbours

Every other report in this tree is written by a single rescue run, from the artifacts that run had in front of it, and carries that run's `step` and `elapsed`. This one is a backfill. It covers a week of failures that happened **before** the rescue skill gained the ability to leave a durable record, reconstructed from what survives: committed artifacts, the roadmap, two architect buffers, and the session's own memory of files that no longer exist.

It exists because the week's most expensive work left the least evidence, and because that is not an accident of this week — it is how the pipeline is built.

## Two blind spots in the record, both structural

**No durable reports exist for this project.** The capability writes to `rescue-reports/<project>/`, and until this file that directory held nothing for `tradeoxy_core`. Every rescue run of this week predates it.

**The surviving artifacts are biased toward success, by construction.** A rescue at spec or spec+plan depth deletes the plan-reviews of the attempt it repairs. So a task that died three times and then passed on the fourth attempt is recorded, permanently, as a task that passed cleanly. Task 40.5 is the proof: its committed artifacts are one plan-review and one review, while the architect buffer records three dead planning rounds and the rule they produced. Anyone reading the artifact tree to learn where this pipeline struggles will conclude it rarely struggles.

## What the week cost, where the cost is visible

Seven tasks shipped, 17 239 seconds — 287 minutes — of orchestrator time on the runs that completed:

| slug | task | plan rounds | review rounds | elapsed |
|---|---|---|---|---|
| 134 | 42.1 | 1 | 1 | 9 min |
| 135 | 42.2 | 3 | 1 | 27 min |
| 136 | 45.1 | 2 | 1 | 14 min |
| 137 | 39.6.2.1.1 | 2 | 3 | 70 min |
| 138 | 39.6.2.1.2 | 2 | 3 | 60 min |
| 140 | 38.5 | 2 | 2 | 70 min |
| 141 | 38.6 | 2 | 3 | 36 min |

Destroyed attempts are not in this table and are not counted anywhere.

## The ceiling, measured

Across the 71 slugs whose artifacts are on disk: 35 passed plan review on round 1, 27 on round 2, 9 on round 3, and **none on round 4**. Three planning rounds is a hard wall, not a soft budget.

It bites harder than the numbers suggest, because the reviewer's own contract permits a pass only when there are **no findings at all** inside the task's boundary — cosmetics included, and scope and severity are explicitly independent axes there. So a stale comment in a file the task edits is a finding, and three such trivia across three rounds end the task. A run does not have to be going badly to run out.

## The incidents

### 39.6.2.2 and its child — the week's largest expenditure, still unshipped

The parent died at three planning rounds and was dissolved into two children. The child `39.6.2.2.1` then burned two slugs. The first, 139, was orphaned when a tree-wide `git add -A` tracked its in-flight plan and sidecar: a tracked artifact reads as a completed task under the artifact protocol, so the orchestrator treated the slug as closed, allocated 140, and re-planned from scratch with a fresh planner. Every fold-in the rescue had made to plan 139 was lost; the spec repairs from the same rescue survived only because they live in a tracked spec file. Slug 140 then failed three more planning rounds before the spec was rewritten at spec depth and both slugs' artifacts were destroyed.

Both tasks of that family are still open. The largest effort of the week bought nothing that shipped, and its evidence is gone.

One survival, by accident: slug 139's plan is recoverable from git history — because of the very commit that orphaned it. It is the only failed attempt of the week that can be read back.

### 38.5 — the one rescue with a measurable payoff

The run stopped at three planning rounds with no pass, 1790 seconds spent. The repair went in at spec+plan depth: six holes closed in the task spec, four fold-ins into the plan, plan-reviews deleted, resume point rolled back. The second attempt passed plan review in two rounds and review in two, at 4211 seconds cumulative — roughly forty minutes of new work.

None of the six closed holes reappeared. What cost the second attempt's extra round was a different class entirely: two declarations elsewhere in the repository that enumerate a set the change alters — the endpoint's Swagger status codes, and a module-graph sentence in the architecture map. Neither is code that calls the changed thing; both are declarations that list it.

### 38.6 — the ceiling of preparation

Its spec was repaired before the run: six holes closed, including a second hand-construction of the service that the spec named nowhere and that would have failed to compile. The first planning round came back green with zero critical issues — and the task still took two rounds, because the pass bar is zero findings and the reviewer found two documentation surfaces that had gone stale.

Preparation removes the mechanical holes. It does not buy a first-round pass.

### 39.6.2.1.1 and 39.6.2.1.2 — 70 and 60 minutes, on new files

Both created their files from scratch. Neither touched `replay-rpc.spec.ts`, the 1259-line suite that carries no `beforeEach` and shares its doubles file-wide. That kills the comfortable explanation: the expensive thing this week was not one monolithic test file, it was the order-axis concern itself, which has to be threaded through several large stateful test surfaces at once.

### 38.7 — cancelled rather than rescued

Never reached the orchestrator. After 38.6 shipped, every `params.subscriptionId` reaching the runtime had already been authorized at the point it was written, and no rows predate that change. The task would have bought nothing and cost a hard dependency on broker reachability at every process start, in a path that tolerates the broker being down today. Contract line, spec and the doc clause that promised the runtime check were removed together, and the governing document now states where the invariant is actually enforced.

## Context from outside the window, because its rule governs inside it

Task 40.5 shipped on 28 August, eleven days before this report. It died on three planning rounds against a gap that a pin-gaps sweep had walked straight past: the sweep pinned every gate the task must pass and never asked what the repository's own verification commands do to a task that guarantees untouched lines. Both `npm run lint` and `npm run format` rewrite files in place, so the ordinary reflex after finishing would have breached the task's own fence while the type-check and the tests stayed green — a silent breach by construction.

That produced a standing rule in the project's `RULES.md`. Its blind spot recurred this week in a second shape and became a third finding class for the lens: alongside value holes and meaning holes, the **blast-radius hole** — what the repository already contains that the change breaks. Both existing classes interrogate the artifact's own text; neither asks what exists outside it.

## What cannot be recovered

The plan-reviews of 39.6.2.2, of both slugs of 39.6.2.2.1, of 38.5's first attempt, and of 40.5's three dead rounds. Their content is described in two architect buffers and in the handoffs of the sessions that fought them, and nowhere else. The specific findings — which sentence the reviewer objected to, which fixture it named — are gone.

That loss is the reason the capability this file backfills exists.

## What the week teaches

The lever is not writing better plans. It is not leaving the planner anything it is obliged to discover on its own. Both halves of that were demonstrated in the same week: the holes closed before 38.5's second attempt did not come back, and the ones that cost it a round were the ones nobody had thought to look for.

The next failure is most likely in Phase 46, which is fully decomposed into seven tasks and has never run. Its exposed points are the wire change, which edits a proto file four other RPCs share and cannot be staged in halves because the service is served live at bootstrap, and the eviction cron, which is modelled on the candle store's behaviour while deliberately reusing none of its machinery. Both are seams between tasks that neither task can see from inside — the class that cost the most this week.

# 61.4 — a radius swept by its words, not its mechanism

**Project:** tradeoxy_core
**Date:** 2026-09-27
**Stopped at:** planned:3
**Elapsed before the rescue:** 983

The task moves the order stream off its hand-rolled reference count and onto the shared pool of named holders. The stream's `onEmpty` becomes single-flight behind a closing flag, which also repairs a present defect: a take and a release within one drain used to re-arm the stream twice and orphan one stream. The fatal branch removes its own entry, and `release` stays awaitable through the in-flight close. The planner produced this design on the first attempt, and every reading confirmed it by trace. The rescue of the dynamic candle-series task had already rewritten this task's specification: it now carried a rule, a sweep and a recorded result for the part of the change the compiler cannot see, and it listed the comments and titles that spoke of the count.

The first reading found four places that sweep never reached.
- A runtime banner still justified its rule with the word «decrement». After the fatal-branch reorder, that justification was also false.
- A test comment still read «at refCount: 1».
- A section banner in the service spec read «reference counting», which the sweep's pattern did not match.
- The plan's own reasoning about when its sweep would come back empty was wrong for the same reason.

The reading also found a false claim that the reorder changes what the asynchronous dead-stream listener observes, a closing assertion left to the implementer's choice, and an ambiguous signature form. The planner closed all of it and folded its checks into one sweep over every touched file.

The second reading found one false claim about the codebase: that the neighbouring assertions already carried the slot holder's name. That was true for only a few of the sixteen sites. The planner replaced it with the rule that each site builds the name from its own test's fixture.

The third reading found two more places, and neither spoke of the count at all. They narrated the map this task also retires: «The entry stays in the map» in the stream's backoff comment, and a test title ending «…clear the map on onModuleDestroy». Every round had found another word for the same retired mechanism — decrement, reference counting, map. All three readings also repeated one deferred observation. The shutdown pass awaits each entry's task, and a close already mid-drain on that task resumes first. It finds the runtime's holders still present at shutdown and re-arms. The shutdown pass then removes the entry, orphaning the new stream.

> The specification swept its radius by a list of the count's words, when it needed to sweep by the mechanism being retired: every phrase in the touched files that describes the map, the count, its increment or decrement, or a «reference» had to be reworded, found by one sweep whose recorded result is exactly those sites plus the named survivors.

**Classification:** specification gap (blast radius). The recurring signal is the same retired mechanism, found under a new word in each round.

## What was done

This was a spec-depth rescue with a full reset, on the user's choice: the plan, its three plan-reviews and the sidecar were deleted.

The order-stream specification now carries, as clauses of its own, every ground fact the discarded plan and its readings established. That includes:
- the fatal-branch order, and that it has no observable effect on the asynchronous listener;
- the holder at each runtime site, built from that test's own fixture;
- the new cases with their closing paths pinned;
- the parameterless `onRetaken`.

The radius is now restated by mechanism, with the round-one and round-three sites, the untyped `streams.size` read, and a tuned sweep with its recorded result. The intents twin gained the same rule, and the sweep found a hyphenated «ref-count» title that the previous pass had missed.

The shutdown race went to the user, who asked whose capability the shutdown flag is before placing it. The answer was the owner's, meaning the service holding the pool, which is neither a holder nor a party that releases. The documentation went first. `docs/architecture.md` § «Держатели общего ресурса» now states that a shared resource has an owner, that when the owner ends it ends every resource regardless of holders, and that the one decision after a close reads «holders remain and the owner is not ending». Both stream specifications then carry that condition, each with a case that fails before the task.

`docs/backtest-replay/02-wire-contract.md` § **Authorization** was reworded in holder terms. `.ai-factory/ARCHITECTURE.md` gained the building blocks a module is assembled from, and names the pool as an in-memory repository of live objects, not a database repository.

# 52.1 — A catch-all translator bound to a door that does more than one thing

**Project:** tradeoxy_core
**Date:** 2026-09-18
**Stopped at:** escalated
**Elapsed before the rescue:** 56

Task `52.1` asks for one thing: the door `GET /api/layouts/:layoutId/active-indicators/:id/init-state`, which today lets a broker outage escape as the framework's own unrendered `500`, should answer `502` instead — and should do it with the translator that already exists, `OrdersGrpcStatusFilter`, the one the orders door already uses. The plan did exactly that and nothing more: one decorator on one method, never on the controller class, no `catch` anywhere in the service chain, plus the matching `502` declaration in the endpoint's own documentation block.

The review of that plan confirmed every mechanical claim it made — the import alias the layouts module already uses for orders, the alphabetical position in the import list, the fact that no module needs editing because a filter named on a handler is registered against that handler's own host module, the fact that the controller's existing suite instantiates the controller directly and so needs no change. On the plan's own terms there was nothing to fix.

What the review saw instead was in what the task's own description had decided. The translator is a catch-all: bound to a handler, it intercepts everything that handler can throw, and its third branch renders anything it cannot recognise as `502 'Upstream broker error'`, logging it as an unexpected error in the orders controller. On the orders door that blanket costs nothing — those handlers *are* the broker call. The init-state door is not one thing: before it ever reaches the broker it checks that the layout belongs to the caller and reads the activation row from the database, it takes the slot's own metadata, it resolves a timeframe, and it replays history through the user's own indicator code — and on one of its two branches it never calls the broker at all. Three of those paths were verified reachable: a database failure on either read; the `Unresolvable timeframe` throw on the branch for candle-axis indicators, where no broker call exists; and the indicator's own code on the warm-up, swallowed today but deliberately released by a later task of the next phase. Each of them, once the translator is bound, would be announced to the caller as the broker's fault.

That is precisely the rule the whole phase exists to enforce — whose failure it is decides the answer, with a different answer for an outside dependency, for this service's own inability, and for the user's indicator code failing, the last carrying its reason inside. The task's own description had claimed nothing would break on contact; that one claim was the only part of it that did not survive contact with the code.

> The decision the run stopped on: is a blanket translation of every failure of this door into `502` an acceptable price for reusing the existing translator, or must the translator translate only what it can actually classify and hand everything else on untouched?

The user ruled the second. The translator's own unclassified branch stops naming the broker and hands the exception to the framework's own rendering, which fixes both doors at once and keeps the door — not the service — the place where an outcome is rendered.

## What was done

The decision was recorded where it belongs and the task was reset to re-plan from a repaired description.

A new task was written and placed ahead of `52.1` in execution order: the status filter passes through what it cannot classify — its first branch (an already-rendered exception) and its whole gRPC branch untouched, its unclassified branch narrowed to the framework's own default, its log line no longer naming a controller it no longer exclusively serves. Its own description pins how the private mapping method and the public catch divide once the unclassified branch has no rendered exception to return, and enumerates what it re-points: the three cases in the filter's own suite that pin the old fallback, and the orders door's own answer to an unclassified failure, which changes deliberately.

Task `52.1`'s description gained the blanket fact it had been missing, the precondition that the narrowing lands first, and an honest blast radius in place of its «nothing». The binding itself — method-level, no module edit, no catch in the service chain — was left exactly as planned, because that part had been verified correct.

Two further statements elsewhere asserted the old behaviour as fact and were corrected: the description of the task that makes the init-state door render the indicator's own failure, and the contract line of that same task, both of which said the filter would answer that failure as a broker outage; and a deferral clause in the activate-door task naming the same old answer.

The failed attempt's own artifacts — the plan, its review, and the run's record of where it stopped — were deleted, so the task re-plans from the repaired description rather than resuming into a decision that no longer stands.

# 79.4 — a death left to transport timing

**Project:** tradeoxy_core
**Date:** 2026-10-07
**Stopped at:** planned:3
**Elapsed before the rescue:** 1022

The task moves a run's `ORDER_EVENT`/`ORDER_STREAM_DEAD` traffic off the application `EventEmitter2` onto a bus the run's own `ReplayRunAssembly` builds for itself, so a live GUI listener and the run no longer share a wire. Three plans were written on top of `a737a24` (79.3.2 landed); the design held clean through all three, and every found defect but one was closed round over round.

The first round found three test-scaffolding defects and one stale comment: the new isolation test raced its own run-bus double, because the test's open-order snapshot could fire before the double was attached; a prototype spy was never restored outside group 12; the factory suite's emit-count assertion never tied the verdict to the assembly's own bus instance; and two comments in `orders-stream.service.ts` described only the live instance once a run's emit could go on either bus.

The second round closed all four, and found that the rewrite had quietly emptied one of its own test cases: with no bus listener registered before `build`, both "a rejected acquire…" and the retitled "one answer…" now answer through the build catch's non-aborted branch, leaving the catch's own aborted early return — reachable in production when a client cancels during the 5 s first-ready wait — with nothing exercising it. It also found a second stale comment, in case 6e, whose premise was the very filter this task drops, and a duplicated capture of the factory's original `build`.

The third round closed all three, and found that the second round's own fix still raced wall-clock time: gating the late rejection on an 80 ms timer against a client cancel delivered over the network, rather than on the server's own observed `'cancelled'` emit, so the case could fail on a loaded CI worker even with correct code.

Both the first and the third rounds additionally recorded, as a deferred observation rather than a plan defect, a design hole in the task's own spec: its sentence "any other verdict can only arrive on a later macrotask" rests on grpc-js transport timing, not on anything `OrdersStreamService` enforces. A broker end buffered directly behind the `SUBSCRIBED` frame can reach the run's bus within a few microtasks of `firstReady` resolving — before `build`'s own resolution has unwound back to `runDial` and either listener exists. A verdict arriving in that window is lost silently: the pool entry is gone, `intakeCount` reads 0, and the run parks forever instead of ending `UNAVAILABLE`. The plan implemented the ratified spec faithfully, so neither round held this against it — but the window is real, and two independent rounds found it the same way.

> The specification rested the run's hearing of its own stream's death on transport timing — listeners registered after the build, on the premise that no verdict can arrive before a later macrotask — instead of on construction, and again handed the planner the census of comments the change falsifies and the test branches it moves.

**Root-cause category:** specification gap. **Recurring signal:** stale comments outside the spec's sweep (first and second rounds); the dead-verdict window raised independently by the first and third rounds.

## What was done

Repaired at the specification depth, with a full reset of the plan under it, reconciled with core 123, who read all three rounds independently and agreed on the design: a stream's death is held as a state the assembly's own constructor latches before any acquire, not an event a later listener might or might not be registered in time to catch.

Spec `.ai-factory/specs/0299-a-runs-order-events-travel-on-its-own-bus.md` is rewritten in full. "What is true now" restates HEAD `a737a24` — the two `runDial` comments quoted verbatim, `orderEventListener`'s guard and its stated reason, and `IndicatorRuntimeService.handleOrderStreamDead`'s own spurious log, moved here from "What breaks on contact". "What must be true after" replaces the macrotask premise entirely: the assembly's constructor registers one `once(ORDER_STREAM_DEAD, …)` on its own bus before any acquire and exposes the payload as `ended: Promise<OrderStreamDeadPayload>`, which only ever resolves and never rejects; `runDial` subscribes to it once `build` resolves, so a death before or after that moment is caught the same way, because a promise reaches a late subscriber; `orderEventListener`'s own `signal.aborted` guard is deleted outright, together with the test case that exists only to pin it, on the strength of the run model itself — the broker's door refuses a subscription already holding an order, so nothing is on the run's stream to miss. "What breaks on contact" keeps and refreshes both symbol sweeps, states the consequence for the two group-12 cases whose aborted branch goes untested without a rewrite gated on the server's own observed cancel, names the factory suite's new ever-present listener and its harmless extra `ended` resolution on a first-attempt fatal, and replaces the deferred sweep with the read census itself — comments in `orders-stream.service.ts`, the harness's own DI comment, test 6's "shared EventEmitter2" capture, test 6e's filter-premised comment, and both rejected-acquire-adjacent comments in `replay-rpc.spec.ts`, plus the controller's own two registration-order comments.

Spec `.ai-factory/specs/0298-the-run-builds-its-own-order-side.md` gained one sentence beside its owed dead-stream case: once the run's own bus lands, the death reaches the run through the assembly's `ended` instead of a listener on the shared bus, and the rule itself — the run ends on its stream's own verdict, and the gate never reads `intakeCount` again afterward — is unchanged. Nothing else in 0298 moved.

`ROADMAP.md`'s 79.4 contract line was brought to the design: the assembly's own `once`/`ended` latch, `runDial` subscribing after `build`, and the dropped dead-stream listener and `signal.aborted` guard.

Full reset: the plan `.ai-factory/plans/152-79-4-a-run-s-order-events-travel-on-its-own-bus.md`, its `.json` sidecar, and the three plan-reviews were all deleted (`git clean -f --`, all five untracked). Nothing under task 151 was touched.

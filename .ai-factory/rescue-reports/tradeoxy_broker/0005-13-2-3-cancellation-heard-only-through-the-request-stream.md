# 13.2.3 — cancellation heard only through the request stream

**Project:** tradeoxy_broker
**Date:** 2026-10-06
**Stopped at:** planned:3
**Elapsed before the rescue:** 1356

The planner built the run handler almost entirely from its spec: the door in the spec's order, the per-event clock-advance-and-apply with alerts entering the shared intake, the event-bus counter giving the watermark, and a single `defer` evicting only what the call itself opened. The first review found no broken logic. It asked for the test `Application`'s lifecycle to be pinned, since the suite needs a `StrategyDispatcher` and leaks event loops without `asyncShutdown()`. It also corrected a premise that `BrokerGRPCServerTests` stayed under swiftlint's type-body limit, which it already exceeds. The plan took both.

The second review confirmed those and found one in-scope nit: both header comments of the `BrokerGRPCServerTests` pair still claim the type fits the limit. The plan set out to rewrite them. Its deferred observations raised, for the first time, that a run's alerts entering the shared intake reach every subscription on the same strategy source, live production and staging ones included.

The third review found the real gap. The spec says the call's own cancellation ends the run the same way a thrown status does; the plan read that as a cancellation arriving as a throwing `next()` on the request sequence. In grpc-swift 2 that holds only for a peer reset. Server graceful shutdown and an expired deadline fire only the server context's cancellation handle and leave the inbound stream open — exactly what the NOTE in `OrderServiceProvider.subscribeOrders` pins, which is why that method is wrapped in `withRPCCancellationHandler`. With the plan as written, a broker shutting down mid-run leaves the handler parked in `next()`: the run keeps consuming events while `App` tears down, `BrokerGRPCServer.shutdown()` never returns, and no teardown runs. A test that finishes the request stream with an error cannot catch it. No finding recurred: each round closed the last, and the plan was converging.

> The spec did not pin that an RPC cancellation reaches the handler only through the server context's cancellation handle, not as a throwing `next()`, nor that a cancellation is never core's half-close and ends the run through the same teardown.

Category: specification gap; no recurring finding. The governing doc is not violated: `backtest-replay.md` requires one teardown on every exit, and the spec did not carry the mechanism down to the code.

## What was done

Repair depth spec + plan. Note 76 now pins the cancellation mechanism, the not-a-half-close rule and a handle-cancel test, and its stale `closeTime` description is corrected; the contract line carries one clause. The plan folds in observing `context.cancellation` through the same `defer`, the four named exits and the new test. It drops the header-comment rewrite and the 350-line split guidance, both made moot by a new `Tests/.swiftlint.yml` that disables `type_body_length` for tests. The three plan reviews were deleted and the sidecar set to `planned:1`; the plan was kept. The alert fan-out observation was routed to Phase 46, now ordered above the creation gate (13.3.2) so that no run is reachable before its signal path is isolated.

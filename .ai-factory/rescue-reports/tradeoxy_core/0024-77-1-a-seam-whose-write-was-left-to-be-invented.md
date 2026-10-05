# 77.1 — a seam whose write was left to be invented

**Project:** tradeoxy_core
**Date:** 2026-10-04
**Stopped at:** planned:3
**Elapsed before the rescue:** 822

The task moves the backtest run's loop out of the gRPC handler the broker calls, and puts it behind a new interface, `IReplayRunCall`, so that a later task can drive the same loop over a call core itself opens. The handler keeps only its register-and-park path and plugs its own stream into the interface. Three plans were written; each was stopped by its review before any code changed.

The first plan laid the runner and the served-call adapter out correctly, but left three gaps. Its guard against starting a run on a call that had already ended checked only for cancellation, reasoning that registration "has already aborted the runner's own controller"; a call that merely closed runs the cleanup without aborting, so the loop would still start and add the subscription to the run registry after the only place that removes it had already fired — the silent freeze of live metrics the governing document names. It also made the adapter's write wait on the controller's own abort signal, the one reserved for the park's cleanup, and it missed two imports the slimmed controller no longer needs, which neither the compiler settings nor the acceptance run would ever report.

The second plan closed all three: the guard checked both the settled and the aborted state, the adapter's drain wait moved onto its own terminal latch, and the import list was completed. But the new way of releasing a write raced every write against one per-run promise that settles only on abort. Each race left a reaction on that promise for the rest of the run; the reviewer measured about 150 MB retained for half a million writes of the same shape, where today's code holds at most one subscription at a time and drops it as soon as the write settles.

The third plan replaced the shared promise with a listener scoped to each write and removed when it settles — the shape the review accepted — but consumed the write's promise through a fulfilment-only handler. A write that ever rejected would raise an unhandled rejection, hang the run, and never reach the internal-error answer today's code gives. The same review found comments in the transport suites naming `replay.controller.ts` for code moving to the runner, which the plan's sweep for the old function's name could not catch.

> The spec gave the new interface's `write` a promise-returning signature and stated neither what that promise means nor how the run races it against its own abort, though today's `waitForDrainOrAbort` already embodies that discipline over Node's own `write → boolean` plus `drain` — so each plan had to invent the mechanism and got a different corner of it wrong.

**Root-cause category:** specification gap. **Recurring signal:** the write's release-and-abort mechanism drew a critical finding in all three rounds, a different facet each time.

## What was done

While the diagnosis was being discussed, the user rejected the mechanism the task was moving rather than its seam: the live tick pass skipping a run's orders through an exemption list is a crutch — backtest is meant to run exactly as live does, with only the differing parts split into implementations. He ruled a new phase ahead of this one, in which an order's metrics are driven by a price-and-time source bound to its subscription (live ticks or the run's own minute closes), with the exemption list gone, and declared this whole phase invalid until that lands. The attempt was reset in full: the plan, its sidecar and all three plan reviews were deleted; the task's contract line and spec were left as they are, to be re-cut after the new phase. A note for that re-cut: the run's call should mirror the stream's own `write → boolean` plus `drain`, so the loop keeps `waitForDrainOrAbort` unchanged and nothing has to be invented.

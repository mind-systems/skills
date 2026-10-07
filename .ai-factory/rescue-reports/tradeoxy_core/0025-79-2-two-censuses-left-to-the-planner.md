# 79.2 — two censuses left to the planner

**Project:** tradeoxy_core
**Date:** 2026-10-06
**Stopped at:** planned:3
**Elapsed before the rescue:** 905

The task makes the order stream configurable at construction — a policy saying whether it reconnects, how long its first subscribe may wait, and whether a timed-out wait proceeds lazily or refuses — and gives the stream its own count of the snapshots it received, so that a backtest run can later build a private stream that never reconnects and counts exactly what the broker counts. Three plans were written; every review rated the risk low, and none of them reopened anything the previous round had settled.

The first plan was essentially right. Its review found one missing test — nothing showed that a stream refusing lazy connection still resolves when its subscribe frame arrives in time and stays up after its timer — and two comments in the stream loop that said an ended stream "falls through to backoff", which stops being true when the stream does not reconnect; it also corrected how the plan silenced the logger in tests and an ambiguous import step.

The second plan closed all four. Its review found that every planned test used a 500 ms timeout, today's live value, so an implementation that ignored the new timeout field would pass everything while a backtest run, which hands in five seconds, would refuse at half a second.

The third plan closed that with a five-second case. Its review found two more comments, above the sets of status codes, that still claimed those codes are always retried and stay on backoff.

Two reviews also recorded, outside the plan's reach, that the specification's own rule was false: it said an end during the first subscribe attempt emits no "stream dead" signal because nobody yet holds the stream, but a caller that proceeded lazily, or a holder that survived a restart of the entry, does hold it and is dropped without notice — and the fatal branch the rule claimed to mirror already emits in that case.

> The specification enumerated the code its constructor change breaks but not the comments its policy falsifies or the tests its unreachable-in-production branches owe, and it invented a no-signal exception the existing fatal path does not have — so each review found one more member of a census the planner had been left to take.

**Root-cause category:** specification gap. **Recurring signal:** stale comments in the rewritten file (two rounds) and missing silent-failure tests for the new policy branches (two rounds).

## What was done

Repaired at the specification-and-plan depth, reconciled with the project's second architect, who read the three rounds independently and supplied the test census and the rule's repair. The specification now lists, by quoted text, every comment in the stream file the policy makes false; names the tests the new branches owe, under the run's own policy; and replaces the exception with one rule — without reconnection, every end of the stream is terminal and handled as the fatal branch is: reject a waiting subscribe, remove the entry, emit the "stream dead" signal, clear the cache. The roadmap line was brought to match, and the kept plan was patched for all three. The three plan reviews were deleted and the plan returned to review at its first attempt. The next task's specification gained two facts the reviews had found for it: which registry the run's private stream is constructed with, and that the run ends on its stream's "dead" signal and never trusts the snapshot count after it.

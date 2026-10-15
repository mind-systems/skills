# 90.6.1 — A seed that belonged to no one

**Project:** tradeoxy_core
**Date:** 2026-10-15
**Stopped at:** planned:3
**Elapsed before the rescue:** 1047
**Sessions:** planner: 7f0d58e5-e0a5-4856-9b2d-da656e5c844c; plan-reviewer-1: cec9f778-d773-4f25-802f-54c408d4fd90; plan-reviewer-2: 90d93ed8-58f8-4af4-a512-79f510d0f5fc; plan-reviewer-3: 865b2588-6f2f-41ba-9615-368320c38c3c

The task stopped in planning; no code was written and nothing escalated. The governing doc, what a bar is, was not violated by any plan.

The first plan built the red suite through construction points that throw and that the next task fills with production code, but left the seed order as a one-line comment on an interface, although the contract line promises it red. The review caught that, and also that case 9 fed its seconds as one stream across three scenarios, that the resubscribe case could not tell a fresh seed from a kept close, that the shutdown scenario repeated the unsubscribe one, and that the concurrent scenarios named no shared setup.

The second plan fixed all of it and added a second construction point for the previous-close source. Its size brought three inconsistencies: a second pair's constant declared in one task and used in another, a shutdown variant that never asserted the state was cleared, and an interface block that promised a comment for every member and gave some.

The third plan closed those, and the review reached the layer the spec never decided. No case made the stored-close read itself fail, so an implementation awaiting it unguarded would pass and, in production, leave the seed rejected and the pair's quiet seconds never closed, with nothing reporting why. No case covered a resubscribe landing while the earlier subscription's seed was pending; two wrong implementations passed every scenario, one applying the stale close to the new subscription, the other blocking the new seed and dropping the old. One spec said the seed is never in flight twice for a pair, the other that a resubscribe starts fresh; neither said whose the seed is.

> The spec did not say that a seed belongs to one subscription, nor that a failing read of the stored close counts as nothing stored.

Classification: specification gap; the seed path drew findings in the first and third rounds.

## What was done

The rescue ran at the spec + plan depth. Two rulings were written into both specs. A seed belongs to the subscription that started it, so a resubscribe starts its own seed even while the earlier one is pending, and the earlier result is dropped whenever it lands. A failing read of the stored close counts as nothing stored, so the exchange is asked once, and the source resolves `null` after one logged warning when both fail and never rejects. The second clock's contract spec carries both rulings, the implementation spec carries them too, and the roadmap contract line now names the failing reads and the resubscribe case among its red specs.

Three review observations that belong to the implementation task were folded into its spec: the connection counts a pair as connected only while its state is connected, a quiet second that falls due with no close held is a hole that is passed over and whose later trade is discarded, and trades in the first batch from before the connect are discarded and hold no bucket that blocks the first whole second. The matching deferred entry in the earlier write-never-overwrites review was marked dismissed.

In the plan, Decision 5 now states both rulings, the seed-order block gained cases (iv) and (v) for a failing stored read and for both reads failing, and the concurrent block gained the resubscribe scenario in both settle orders. The three plan reviews were deleted, and the sidecar was set to planned:1 with the planner, elapsed and reviewer ids kept.

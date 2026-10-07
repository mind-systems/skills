# 79.3.2 — a third census: the spec swept by symbol

**Project:** tradeoxy_core
**Date:** 2026-10-07
**Stopped at:** planned:3
**Elapsed before the rescue:** 1800

The task wires the skeleton 79.3.1 laid: `ReplayRunAssemblyFactory.build` constructs a `ReplayRunAssembly` owning its own `OrdersCacheService`, `OrdersStreamService`, and `OrderMetricsStamper`, and `runDial` reaches that assembly instead of the live collaborators `ReplayOrderEnrichmentService` forwarded to. Three plans were written; every review rated the risk low-to-medium, and each one found comments the previous round had not — never a design objection.

The first plan was mostly right. Its review found that the delivery suite's own isolation premise breaks once a run's store is real — a stamped open order gets a new dedup key and the settlement gate's re-drive steps the scripted indicator an extra time, breaking four cases the plan never reworked — and gave the fix the plan adopted: starve the run stores' read path with a prototype spy, in that one suite only. It also found a sweep instruction that contradicted the plan's own required class-header comment, a captured-after-the-spy-was-installed original method, a case missing a wait, and two stale comments: one justifying a case by a now-unreachable production path, one still citing a 500 ms wait a run's own policy no longer uses.

The second plan closed all five. Its review found six more comments going stale — a banner stating a premise the plan itself called gone, a case title whose "membership" lost its referent, two in-handler comments sitting directly above assertions the plan removes, and two push/close-site comments narrating the registry mechanism by name — plus three precision gaps in the delivery suite's case-3 rework (a missing wait before reading the first run's stream, the second run's acks never listed, a live-handle count given as 1 instead of 2 while the first run was still held) and an unrestored prototype spy that would have leaked into every later case in the file.

The third plan closed all of that. Its review found exactly two comments still not listed: the controller's registration-site pin comment, whose "alongside the add(S) above" clause loses its referent once that call is dropped, and one case's ack-site comment, whose "two prior bumps" phrasing survives the move from a hand-emitted bump to a pushed snapshot. Nothing else moved — the design review (factory flow, every controller exit path, the duplicate-event hazard, the real-store arithmetic, the pool-code match) held unchanged across all three rounds.

> The specification swept the retiring mechanism by its symbols but not by the prose that narrates it, and named a suite whose premise breaks without saying how, so each review found one more stale comment the planner had been left to census.

**Root-cause category:** specification gap. **Recurring signal:** stale comments narrating a retiring mechanism, found one at a time across three independent review rounds, in files the spec's own symbol-keyed sweeps already covered for code but never for prose.

## What was done

Repaired at the specification-and-plan depth, reconciled against HEAD and against the three review rounds' own findings (core 123, a peer reviewer, independently reached the same diagnosis).

Spec `.ai-factory/specs/0298-the-run-builds-its-own-order-side.md`: "What is true now" gained a paragraph stating that `ReplayRunAssembly` and `ReplayRunAssemblyFactory` already exist as skeletons (landed by 79.3.1, commit `1201eb7`) with a red suite pinning the factory's three leak cases; "What must be true after" dropped the "new plain class"/"new provider" framing in favour of "already declared as a skeleton … is implemented". "What breaks on contact" gained two paragraphs: one stating the prose-radius rule (a comment narrating a retiring mechanism is invisible to any sweep over code symbols) — the paragraph pins the sweep and the quoted list of comments it reaches, by fragment, file, and enclosing case title or method name — the other stating the delivery suite's broken read-isolation premise under a real run store, its fix (a prototype spy starving `OrdersCacheService.prototype.getLiveBySubscription`, in that suite only), and the real arithmetic's own coverage in `replay-rpc.spec.ts`'s own order-axis case, named by its HEAD title.

`ROADMAP.md`'s 79.3.2 contract line: "new plain class `ReplayRunAssembly`" became "`ReplayRunAssembly` … implements the skeleton laid before it"; no other line touched.

`.ai-factory/plans/151-79-3-2-the-run-builds-its-own-order-side.md`, additive only: the controller's registration-site pin comment instruction gained the re-anchor to "the run's order-side build above"; the rpc suite's case-6 comment-rewrite list gained the ack-site rewrite ("withhold the next pushed snapshot … the two prior pushes"); the delivery suite's case-3 instructions gained an explicit drop of the case's old inline "re-armed runStream" comment, now covered in full by the case's own rewritten steps; each of the plan's three comment-rewrite lists gained one line naming spec 0298's prose-radius paragraph as that list's own source, not a separate one.

Spec `.ai-factory/specs/0300-replaysubscriptionregistry-retires.md`: "What breaks on contact" gained a paragraph naming the same prose-radius rule for the registry's own retirement, quoting `orders-stream.service.ts`'s `handleSnapshot` SUBSCRIBED-branch comment's "no registry bump" clause by name, pinning the sweep that rule runs on over all of `src`, and stating explicitly that this task's own fuller sweep runs at its own time, over whatever 79.3.2 leaves behind, rather than enumerating hits inside files 79.3.2 already rewrites.

The same gap propagates one task further: spec `.ai-factory/specs/0299-a-runs-order-events-travel-on-its-own-bus.md` gained the same prose-radius paragraph, for the comments narrating that a run's order events share the application bus before that sharing ends.

Rollback: the three stale plan-review files were deleted (`git clean -f --`, all three untracked); `151-79-3-2-the-run-builds-its-own-order-side.json` was rewritten to `{"planner": "0bd50cc0-2cae-4034-94b3-0dc9f2ba3260", "step": "planned:1", "elapsed": "1800"}`, returning the plan to its first review attempt with the patched plan.md kept in place.

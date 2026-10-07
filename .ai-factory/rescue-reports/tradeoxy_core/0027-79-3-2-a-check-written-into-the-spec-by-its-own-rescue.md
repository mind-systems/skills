# 79.3.2 — a check written into the spec by its own rescue

**Project:** tradeoxy_core
**Date:** 2026-10-07
**Stopped at:** planned:3
**Elapsed before the rescue:** 3005

The task wires the skeleton 79.3.1 laid, narrowing `ReplayOrderEnrichmentService` to the indicator factory and moving `runDial`'s acquire/stamp/drive calls onto a per-run `ReplayRunAssembly`. This is the task's second rescue: its first rescue (report `0026`) repaired spec 0298's own prose-radius gap, then the orchestrator wrote three further plan rounds against the repaired spec and stopped again, on top of commit `c9178ad`. All three rounds traced the design clean; both defects this time trace to the repair itself, not to the design.

The first round found the repaired spec cited unverified: the Verification task never ran the pinned prose sweep spec 0298 demanded, so a stale English comment could still slip through a suite marked green. It also found a `closeSpy` assertion in the reworked rpc case 6 that would race the server's own `finish()` event, and a `poolOf` helper typed so loosely that the plan's own new case could not compile.

The second round closed all three, and found a fourth: the owed "after the run's own `ORDER_STREAM_DEAD`, the gate never reads `intakeCount` again" case, now added with a guard on `orderEventListener`, carried a test that could not fail without that guard. `awaitCanEmitPast` already exits safely, because `terminate` aborts synchronously; nothing in the planned test ever drove the listener the guard actually protects.

The third round closed that, and found the one defect that traces to the spec rather than the plan: the Verification task's own prose-sweep acceptance rule — follow the sweep, and every surviving hit must be one of five named kinds — could not be satisfied as written. The pinned pattern's `run:` alternative matches every `run: ResolvedReplayRun` type annotation in the controller; its `member\b` alternative matches the rpc suite's own "Scripted scenario registry" banner and the delivery suite's `'NON-MEMBER'`/`'non-member'` literals in case 7, none of which the plan rewrites and none of which fits any of the five allowed kinds. An implementer following the rule literally would have to guess whether to rewrite accurate code the spec never asked to touch, or leave the gate failing.

> The previous rescue wrote an acceptance check into the specification — a prose sweep that must find nothing once the task lands — over a pattern that also matches type annotations, an unrelated test registry and test literals, and the owed dead-stream case named a read site already safe instead of the one it guards; the plan had to turn the check into a gate no implementation could pass.

**Root-cause category:** specification gap, introduced by the previous repair. **Recurring signal:** the prose-sweep gate (first and third rounds).

## What was done

Repaired at the specification-and-plan depth, reconciled with core 123, who read the three new rounds independently and reached the same diagnosis: a spec holds what is true now, what must be true after, and what breaks on contact; it carries no check that the instruction was carried out.

Spec `.ai-factory/specs/0298-the-run-builds-its-own-order-side.md`: the prose-radius paragraph's closing acceptance sentence, "The invariant this sweep protects: …", is deleted outright. The quoted list of stale comments stays — that list is the census, not the check. The pinned sweep stays only as the list's provenance, worded as "Found by `rg …`" rather than "pinned verbatim", and its pattern drops the `run:` and `member\b` alternatives that matched code, keeping `live enrichment`. The owed dead-stream case is restated to name the read it actually guards: a later `confirmed: true` `ORDER_EVENT` reaching `orderEventListener` on the shared application bus after the run's own `ORDER_STREAM_DEAD`, not `awaitCanEmitPast`, which already exits safely because `terminate` aborts synchronously.

The plan `.ai-factory/plans/151-79-3-2-the-run-builds-its-own-order-side.md`: the "Type-check and run the named suites" task's "Prose sweep" step and its five-kind acceptance rule are deleted whole. Nothing else in the plan changed — its `poolOf` typed with `StreamEntryView`, the `closeSpy` `waitFor` before the case-6 assertion, and the dead-stream case's already-discriminating `lateEventListener` design (R2/R3's own fix) all stand untouched.

Spec `.ai-factory/specs/0299-a-runs-order-events-travel-on-its-own-bus.md`: "What breaks on contact" names `IndicatorRuntimeService.handleOrderStreamDead` as a third application-bus listener that stops hearing a run's verdicts, beside the two already named, quoting its exact log text for the non-fatal case it currently misfires on.

Rollback: the three new plan-review files were deleted (`git clean -f --`, all three untracked); `151-79-3-2-the-run-builds-its-own-order-side.json` was rewritten to `{"planner": "0bd50cc0-2cae-4034-94b3-0dc9f2ba3260", "step": "planned:1", "elapsed": "3005"}`, returning the plan to its first review attempt with the patched plan.md kept in place.

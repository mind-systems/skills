# 77.1 — the runner did not own its own failure

**Project:** tradeoxy_core
**Date:** 2026-10-09
**Stopped at:** planned:3
**Elapsed before the rescue:** 1021

The planner moved the run correctly into its own runner behind the call port. The first review found that the body's six early returns could let the run resolve before its teardown, a handful of comments still naming `runDial` or the controller as the run's owner, and a doc section cited by its number; the planner fixed all three. The second review found a contradiction in the spec itself: it said the call latches on `end()` so a later cancel does nothing, and also that a failure out of the run is answered by the controller cancelling `INTERNAL` — but the moved `finally` half-closes on a throw, so that cancel could never answer, and a run failing midway would end as a clean completion. The planner chose on its own to half-close only on a clean exit, a behaviour change the spec never authorised; the review again found comments the spec had not listed. The third review raised one low wording in the plan's own header. Read with core 123, the deeper gap is ownership: the spec gave the failure's cancel to the caller, while every later caller only logs, so from the start door's rewrite on, a run that throws mid-loop would leave its call open — no teardown on either side and the layout busy until a stop.

> The spec did not make the runner own a throw out of its own body — cancel its call `INTERNAL` and rethrow, half-closing only on a clean exit — and left that cancel to a caller that, from the start door's rewrite on, only logs.

Category: specification gap. Recurring: comments narrating the moved owner (rounds 1 and 2).

## What was done

Repaired at the specification-and-plan depth. Spec `.ai-factory/specs/0290-the-run-loop-runs-behind-ireplayruncall.md` and line 77.1 of `.ai-factory/ROADMAP.md` now make the runner own a throw out of its body (abort, `cancel(INTERNAL)` unless latched, rethrow), half-close only on a clean exit, and name that one behaviour change. The neighbours 0292, 0293, 0294, 0311 and 0312 were aligned to the new wording. The plan `.ai-factory/plans/157-77-1-the-run-loop-runs-behind-ireplayruncall.md` was amended and kept. The three plan reviews were deleted, and the sidecar was set back to `planned:1`.

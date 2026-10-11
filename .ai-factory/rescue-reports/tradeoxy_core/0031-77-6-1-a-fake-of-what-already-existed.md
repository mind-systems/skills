# 77.6.1 — a fake of what already existed

**Project:** tradeoxy_core
**Date:** 2026-10-11
**Stopped at:** planned:3
**Elapsed before the rescue:** 908

The task lays the run starter's skeleton and a red suite the next task turns green. The skeleton held for all three rounds; every finding was in the suite half, about a hundred and eighty lines of fake-heavy test code pinned as prose that no one could compile or run. The first review found seven defects — a close counter that never counted, aborts racing builds that had already settled, a no-unhandled-rejection check with no mechanism, the record's entry members placed on the record itself, among others. The second found that the first round's own unhandled-rejection check never fires inside Jest's sandbox, a `toBe` against a freshly built object, and an incoherent fixture. The third found that Jest treats two live abort signals as equal and an incomplete import list. Each round fixed the last and found a new class. Read with core 123, the spec made that surface large: it asked for a fake of the runs record, which already existed as a small synchronous class; it named a stop point «between» two awaits that is no await, so the planner invented same-turn orderings; it left open whether the next task may correct the suite, so the plan declared it frozen and every fake defect became critical; and it never named where an outcome's message comes from.

> The spec asked for a fake of a collaborator that already existed in pure form, left the stop points and the suite's mutability to the planner, and did not name the source of an outcome's message.

Category: specification gap. Recurring: the suite's test mechanics, a new class each round.

## What was done

Repaired at the specification-and-plan depth. Spec `.ai-factory/specs/0311-the-run-starter-is-laid-with-its-unwinds-red.md` and line 77.6.1 of `.ai-factory/ROADMAP.md`, spec 0312 and spec 0292 were repaired: the suite runs over the real record, the stop points are the four an abort can land on, the abort reasons and the source of an outcome's message are named, the next task may correct the suite but never weaken it, and the gRPC door's message carries the broker's code once. The plan `.ai-factory/plans/163-77-6-1-the-run-starter-is-laid-with-its-unwinds-red.md` had its suite half rewritten onto the real record and its skeleton half kept. The three plan reviews were deleted, and the sidecar was set back to `planned:1`.

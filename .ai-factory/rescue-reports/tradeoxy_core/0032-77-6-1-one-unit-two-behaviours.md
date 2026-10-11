# 77.6.1 — one unit, two behaviours

**Project:** tradeoxy_core
**Date:** 2026-10-11
**Stopped at:** planned:3
**Elapsed before the rescue:** 1575

After the first rescue the plan went Medium, Low, Low, with four, three and two findings, and every review said nothing was blocking while withholding the pass. No new spec hole surfaced: the findings were precision nits — a missing flush between build and open, a reference left implicit, an import list, a header's wording — on a plan of some twenty-four thousand characters pinning about twenty-five cases as prose. Two mattered beyond style: a single merged refusal set would have passed every case, and a type-only import of an injected class would fail the app at boot with no gate seeing it. Read with core 123, the surface was large because the planned starter held two behaviours in one unit — sequencing and unwinding a start, and classifying a broker-side rejection — so one suite multiplied every rejection kind by both steps and every stop point by both causes. Three earlier red-suite-first tasks with half the surface passed plan review in one round.

> The spec put the classification of broker rejections inside the starter, so the starter's one suite had to enumerate every rejection on every step alongside every stop point; a pure classifier with its own table suite keeps both surfaces small.

Category: scope overload within one unit. Recurring: precision nits on the suite's prose, a new set each round.

## What was done

Repaired at the specification-and-plan depth. The classification was split out of the starter into its own pure unit, `src/replay/replay-start-rejection.ts`, with a flat table suite; the starter's suite now covers sequencing and unwinding only. Specs `.ai-factory/specs/0311-the-run-starter-is-laid-with-its-unwinds-red.md` and `.ai-factory/specs/0312-the-run-starter-takes-its-body.md` were rewritten with lines 77.6.1 and 77.6.2 of `.ai-factory/ROADMAP.md`, and the phase note `.ai-factory/specs/0289-phase-77-note-what-diverges-now.md` was repointed at the new home of the run call's refusal set. The plan `.ai-factory/plans/163-77-6-1-the-run-starter-is-laid-with-its-unwinds-red.md` was kept and restructured into the two suites, with the review's two findings folded in. The three plan reviews were deleted, and the sidecar was set back to `planned:1`.

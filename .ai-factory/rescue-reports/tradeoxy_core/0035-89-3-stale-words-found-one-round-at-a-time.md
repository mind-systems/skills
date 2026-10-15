# 89.3 — stale words found one round at a time

**Project:** tradeoxy_core
**Date:** 2026-10-15
**Stopped at:** planned:3
**Elapsed before the rescue:** 635
**Sessions:** planner: 026e2e89-a4b8-4d31-b3a2-8cd24afa6a33, plan-reviewer-1: bb382c8a-2de1-4e91-a9f6-268900284f9a, plan-reviewer-2: 453d73c9-945e-4a67-aa1c-09911f166a84, plan-reviewer-3: 58e61773-7235-43ca-afd3-3984f0eb2795

The planner moved the live detector onto the grid and planned to re-assert its old private-reach cases through emitted bars. The first review found three real errors. The first was an assumption that a label with no grid «cannot happen in practice». That was false: `'0M'` passes `resolveTimeframe` and `isValidTimeframe` but has no grid, so the detector would now throw after a socket has joined its room. The second was a wrong epoch-floor figure in the `7m` case. The third was a new interface named without its `I` marker. The plan fixed all three. It pinned the throw before any write, added a `0M` case, corrected the figure, and used `Omit<DynamicEntry, 'grid'>` in place of the new name.

The second review confirmed every value by running the grid and raised one cosmetic point. The plan rewrote the `3m` case's comment and said «Reword nothing else». The same file holds three more test titles and comments that narrate the retired epoch floor: «aligned to floor(epochSec/60)*60», «// floor(75/60)*60 = 60», and the `5s` and `1h` equivalents. The plan added them. The third review found the next layer of the same thing: three section banners still naming the deleted `getBucketStartSec`. Each round surfaced a new batch of words about the old mechanism, because the spec never listed them.

The governing spec, `docs/candle-pipeline/what-a-bar-is.md`, was not at issue.

> The spec lacked the rule that a task retiring a mechanism lists every place in the touched files where that mechanism is named in words — test titles, comments, banners — with the search that finds them; with that census the plan would have reworded them in one pass.

Category: specification gap. Recurring across rounds 2 and 3: the words narrating the retired mechanism.

## What was done

Depth: spec + plan.
- **Spec `0331` and the 89.3 contract line** now carry the rule, the sweep `rg -n "getBucketStartSec|floor\(" src/candles/candle-close-detector.service.spec.ts src/candles/candle-close-detector.service.ts`, and the census of what it reaches on HEAD, quoted.
- **Plan `171`** names the four titles, their comments and the three banners as reworded. Its postcondition is that the detector spec matches neither `floor\(` nor `getBucketStartSec`. Its stale `0M` assumption was rewritten.
- **The deferred observation** carried by all three reviews was routed at the user's choice into a new task placed before 89.3: 89.5, «A calendar label with no months is not a timeframe», spec `0333`. The observation is that `resolveTimeframe`'s calendar branch accepts `'0M'`/`'00M'`.
- **Artifacts:** the three plan reviews were deleted. The sidecar was set to `planned:1`, and the plan was kept.

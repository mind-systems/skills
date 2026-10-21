# 93.18.1 — A mark that missed later bars

**Project:** tradeoxy_core
**Date:** 2026-10-20
**Stopped at:** escalated
**Elapsed before the rescue:** absent
**Sessions:** planner: 8f307d62-9497-4221-b187-e9009c6b6f4a

The planner stopped on a decision outside its authority; no code was written and no review ran.

The task makes the gap top-up fold only where the gap was marked. A bar of a minute or more used to take a gap's lost trades into every bucket holding their time, so a bucket that had also taken the exchange's minute, which holds those trades, counted them twice. The task records on each bucket whether it took a primed source and whether it was amended, and answers whether a gap key is held. The top-up then folds only into unprimed buckets that carry the key, and an amended bucket refuses later primed sources, so such a bar warns instead of doubling.

The planner worked the spec's expectations against the code, case by case, and found one the spec's own rule cannot produce. The spec says the case of a gap that straddles the seconds' start «flips»: the bar of a minute or more goes out with the not-whole warning and without the straddling gap's trade, because its mark stays. In the code the order is different. The connect starts the live seconds at the next whole second, and the stream discards the trade below that start. The gap reaches the catch-up before the first second of the connect has closed, so the detector holds no bucket for the pair, and the mark finds nothing to mark. The connect's prime then creates the buckets of a minute or more, primed and unmarked. Under the task's rule the top-up folds into a bucket only if it carries the key and was never primed, so it touches nothing, and the bar goes out whole, with no warning, and without the lost trade. That is a silently incomplete bar, against the governing doc's rule that a bar core did not see whole goes out with one warning. The same hole applies to the spec's new case of a bucket created after the mark: it asserts only bucket values, so it passes while the bar would go out whole without its lost trades.

The planner could not choose among three outcomes, and each is a decision about the design, not about this plan. One was to accept the hole and route a follow-up task. One was to hold a pair's open gap marks in the detector and mark any bucket created later that overlaps an open key, which widens the task and its spec. One was to let the catch-up exclude a gap that straddles the live start, which changes the catch-up's own rule and suite. It wrote the attempt as a partial plan with the straddle case blocked and escalated.

> Whether a gap in the live stream is topped up and marked at all, given that a mark reaches only the buckets held when it is made and so lets a bucket created later go out whole without the trades the gap lost.

## What was done

The user ruled, on research showing that charting platforms and data vendors never patch a live bar: a gap in the live stream is only logged, with the pair and the id range, bars go out as collected, and nothing is topped up or marked. The in-connection top-up was the pair's own extension of «catch up a partly seen bar», never the user's ruling. The catch-up at a connect and at a reconnect stays as built.

The whole top-up mechanism is retired by a removal task, 93.18.1 renamed «A gap in the live stream is only logged», with a new spec in place of the old one. The task removes `markLost` and `amend` from the detector, `fold`, `markLost`, `clearLost` and the lost-key state from `TimeBucket` so that a bucket is whole by its cover alone, the gap run and `onGap` from the catch-up, its interface and the watch loop's calls, and `readIds` from the reader; the watch loop's gap log stays as the one record. The landed suites' cases for these go with them. The new-series and registered-series specs dropped their gap-mark rules, and the docs state that a gap is only logged and that a bar's warning says only that core did not see it whole.

The attempt's plan and its sidecar were deleted; it had no plan reviews. The spec the plan was written against was deleted, and nothing was left to pin.

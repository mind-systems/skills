# 88.6 — A plan that did not settle on hole-filling

**Project:** tradeoxy_core
**Date:** 2026-10-21
**Stopped at:** planned:3
**Elapsed before the rescue:** 1018
**Sessions:** planner: 36e36887-7acd-4604-a9e6-9c9d79a9ab80, plan-reviewer-1: ad6a9551-1feb-41ee-b1e4-aa2b5ded27ea, plan-reviewer-2: fa9392fd-781d-4955-83d0-1ad8b8046974, plan-reviewer-3: b464a578-bb47-442d-8c8e-e3daf9c252c7

The task asks the history reader to judge a hole on the source table's own grid, wherever it lies, to call the fill provider once per absent span, and the provider to fetch only the span it is given. The spec leaves one decision to the planner: whether the absent-run rule reuses `detectGaps` or generalizes the private helpers of `ClosedMinutes`, "there is one home for the rule". The planner took the largest branch. It generalized the minute helpers into a new `absent-spans.ts` and moved the clock-grid-or-throw rule into one exported `clockBarGridOf`. It added a source-table lookup in `candle.types.ts`, a lean uncapped `findStoredOpens` read in the repository, and a span-sized fetch in `backfillOnDemand`. The one task grew to cover several files and four new homes, with tests spread across five suites.

The first reading found no blocking defect, but three problems inside the task's own boundary. The new `findStoredOpens` read had no test that pinned its bounds, its binding order, the absence of a limit or its mapping to epoch milliseconds, and a mistake there would fail silently. The clock-grid-or-throw rule would have had three copies once the planner added its own. The rewrite of the paging case was underspecified, and following it literally gave the wrong result.

The planner fixed all three. The second reading then found two cosmetic leftovers, both created by the fix. The detector kept two dead imports after the helper moved out. The rewritten case kept the name of the predicate it replaced, and the deleted suites left their banner comments behind.

The third reading found one more compile problem. Two overrides the plan prescribed would not compile against the narrower mock types that some describes in the reader spec declare for themselves. No finding recurred across the three readings. Each reading found a new small defect in the surface the plan itself had widened, and none questioned the design.

A walk through the code, not any review round, found what none of the readings raised. The spec pins one fill attempt for the whole source window before the first page is read, and the plan implements this literally: it reads the stored opens of the whole window in one uncapped query and holds them as a set. After the preceding whole-window task, `rangePages` is meant to be pulled lazily. The replay still pages its own one-day windows through `fetchInRange`, so each judgement covers a day and the plan was safe. When the replay delegates to the reader's pages, a run would judge its entire range and fetch every absent span before delivering its first candle, holding a stored-open entry for every bucket of the run in memory. The replay semantics say the pass is lazy end to end and that no stage materializes more than its current window. The plan conforms to the reading-candles contract and would break the lazy-run contract once the replay task lands. The spec's wording had also drifted from the code: it still named `fetchInRange` and its doc comment, where the head predicate and the fill now live in `rangePages`.

> The task spec pinned whole-window hole judging before the first page and left a helper fork open in a task that already held two behaviours (the reader judging holes, the provider fetching only a span), so the plan swelled and the lazy-run memory contract was never stated as a constraint.

Classification: scope overload, with a secondary specification gap on the whole-window judgment. No finding recurred across readings.

## What was done

Spec depth, with a split into three the user chose. The plan, its sidecar and the three plan-reviews of this task were deleted. The task became three: a fill that fetches only the span it is given (new spec `0391`), the grid helpers getting one home as a behaviour-preserving preparation (new spec `0392`), and the original task, renumbered last, rewritten in place (spec `0385`). The rewritten spec grounds itself on `rangePages` as the whole-window task left it and pins per-page judging: each page judges and fills only the source window it is about to read, never the whole read's window up front, and a short page no longer tells where the window ends. How a page's end is found before the page is read is left to the planner, since `rangePages` today learns a page's extent only by reading it. The per-page rule was carried to the count-before task (`0386`, the same per-window fill attempt) and to the replay task (`0388`, a run's memory does not grow with its range). The one deferred observation, the parity spec's inline copy of the clock-grid rule, was folded into the grid-helpers spec, and no review file remained to pin.

## 2026-10-21

Core 130 extended this report after core 123's razor, by message. The work is uncommitted in core and waits on 123's second pass. The root cause above stands whole: whole-window judging, plus a helper fork left open in a task that held two behaviours. «No review round raised» the lazy-run finding stays true.

The final cut is five children of 88.6, not three.
- **88.6.1 (`0391`):** a fill fetches only the span it is given.
- **88.6.2 (`0392`):** one home for the grid helpers, now including the mapping from a source table to its grid, behaviour unchanged.
- **88.6.3 (`0393`):** a page's end is fixed before the page is read, as the end of the cap-th bar on the grid from the cursor or the window's end, whichever comes first. An empty page is not yielded, and a short page does not end the read.
- **88.6.4 (`0394`):** a pair's live line has one home.
- **88.6.5 (`0385`):** holes are judged and filled per page, below the line.

Tasks 88.7 to 88.10 (`0386` to `0389`) were edited to match, and `docs/candle-pipeline/reading-candles.md` § 3 gained the sentence «A pair core streams is not read ahead of its live pipeline». The page end is no longer left to the planner. It is its own task, because the original spec was carrying five changes, and that bloat is what this report names as the cause.

The razor found that this rescue's own repair carried a new path of silent corruption, which the diagnosis above missed. The persistence service flushes once a second through insert-absent. Judging holes on the tail side would fill a bucket that has just closed and is not yet flushed, with an exchange row or a flat sub-minute stub, and insert-absent would then drop the real core bar for good. The first fix, the detector's frontier plus a drain, was cut: delivery to the buffer is asynchronous, so the drain would chase a live buffer. The replacement is the live line, per pair and source table. A connect sets it to the restart point, and every flush, written or failed, moves it to the end of the latest bucket of that table in the batch; it only grows. The reader judges holes and closedness only below it. Two pins keep it honest: the line is read before the store, and it is lifted only after a flush, an empty one included. The line also closes a silent partial bar already in landed code, against `what-a-bar-is.md` § 6, and it covers the user's rule that a failed write is filled from the exchange on read, with no branch of its own.

The user ruled on the window the line leaves at a break: «Окно обрыва — наверное лучше закрыть». So every change of the line on a disconnect, an unsubscribe, a failure or a reconnect waits for the next flush. What remains is a bar delivered asynchronously after that flush.

Smaller cuts came with it. The count-before read was unbounded below, so it gained a lower bound. A fill formula contradicted its own case. Tests of SQL text on a mock gave way to a database suite. One spec shrank to the dropping of two guards. The eager reconnect path, which wrote sub-minute stubs, is deleted, so the read is the stubs' only writer. A probe recorded in `0389` showed that Binance Futures 1m klines include zero-trade minutes, flat with volume 0, with no gaps, so a quiet minute is a stored row and never a repeated miss.

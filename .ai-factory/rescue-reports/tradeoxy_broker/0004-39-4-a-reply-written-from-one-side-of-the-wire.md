# 39.4 — a reply written from one side of the wire

**Project:** tradeoxy_broker
**Date:** 2026-09-25
**Stopped at:** planned:3
**Elapsed before the rescue:** 1161

The task writes one handoff into core. It tells core that `entries[].percent` is a share of what remains unfilled, answers core's objections, and asks core to reissue the fixture's multi-entry expectations.

The first plan checked the spec against the files before relying on it and corrected three of its facts. Core's handoff `37` lives in the broker's repository, not core's. The `96.667` average belongs to the long two-entry case; the short case averages `103.333`. And core's handoff sequence had moved past the number the spec gave. The first review accepted all three corrections and found gaps the spec had never asked about. Core had asked, in `38` § 4, to be told which values the repaired Swift disagrees with and by how much. The spec prescribed no run and no table, so the reply would have asserted what it could measure. The strongest producer evidence, `TakeFilter.PositionSlicer.getSlicePercent`, whose `min(1, …)` makes the final slice exactly `100`, went uncited. And the plan told core to expect the `closePrice` fix on the parity run, which never reads `closePrice`.

The revised plan took all of it. The second review then opened core's own calculator, which neither the spec nor the plan had read, and found three things. Core reads `entries[].percent` in two places, `weightedAverageOpen` and `walkTakes`'s `openedFraction`, and the reply named neither. A core planner fixing only the multiplier its own earlier trace had isolated would recreate the one-field-two-readings defect the whole exchange started from. Core's `walkTakes` already compounds `takes[].percent`, and its `unrealizedPercent` closes a position with a synthetic take of `100`, so the spec's item telling core its takes reading diverges was false. That item was added during a gap-pinning pass that never looked at core's code. And the broker had told core twice that the fixture stays as it is; a reply asking core to change it had to withdraw those statements.

The plan took that too. The third review found the last gap in the arithmetic itself. Both 50/50 cases average at `290/3` and `310/3`, so their results never terminate. The broker's `XCTAssertEqual` on `Decimal` and core's `toBe` on a forty-digit string both compare exactly, and the two sides round differently somewhere past the twenty-ninth significant digit. As planned, the reply's cross-check would have sent core after a divergence made of rounding noise, and a fourth round of the exchange would follow.

Every round found something real and new, and every one traces to the same place: the spec was written from the broker's side of the wire alone. It never read core's calculator, the broker's own earlier statements to core, or the comparison mechanics both suites share.

> The spec should have grounded the reply in both sides' code: core's two readers of `entries[].percent` and its already-agreeing reading of takes, the broker's own earlier statements about the fixture to withdraw, a measured tally, and fixture inputs on which two exact comparisons can agree.

**Classification:** specification gap. Recurring signal: spec `0045` was contradicted by the files at the same points in every round.

## What was done

Repaired at spec + plan depth, with the user choosing that the reply ask core to reshape the fixture inputs.

Spec `0045` now states:
- the correct location of `37` and the correct case for each average;
- no hardcoded handoff number;
- `isFullyOpen` quoted exactly;
- `getSlicePercent` as producer evidence;
- both of core's readers, with `Order.filledFractions(of:)` as the reference expression;
- the takes item reversed into agreement, with core's synthetic `100` take as core-side evidence;
- the correct tense for landed and pending tasks.

Three items were added to the spec:
- a withdrawal of the broker's earlier statements, for the multi-entry cases only, acknowledging that the 30/30 case was the broker's own request;
- a measured tally answering `38` § 4;
- the ask to reshape the two 50/50 cases so their fill-weighted averages terminate. The suggested inputs are long `50%@90` then `50%@120` and short `50%@110` then `50%@80`, both averaging exactly `100`. No tolerance is offered, since that would need a broker test change no task covers.

The `39.4` contract line gained one clause for the two readers and the reshape.

The plan was kept, with its Context no longer calling the repaired spec wrong. Its Measure step now also records each 50/50 case's exact rational value and where the measured value departs from it. The cross-check is exact only on terminating inputs, and the reshape ask is in its explicit ask. The three plan reviews were deleted. The sidecar was set to `planned:1`, keeping the planner session and the elapsed time.

Spec `0047` (`39.5`) was checked for the same false claim about core's takes reading and carries none.

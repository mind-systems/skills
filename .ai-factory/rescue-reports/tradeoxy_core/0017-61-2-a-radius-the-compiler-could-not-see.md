# 61.2 — a radius the compiler could not see

**Project:** tradeoxy_core
**Date:** 2026-09-27
**Stopped at:** planned:3
**Elapsed before the rescue:** 811

The task moves dynamic candle-series tracking off a hand-rolled reference count and onto the shared pool of named holders that the task before it built. Each caller now takes and releases a series in its own name: a slot in the runtime under `slot:<uid>`, and a socket in the streaming gateway under `socket:<id>`. The planner produced the right production design on the first attempt, and every reading confirmed it. That design kept a per-symbol label index so the hot path never scans the pool's flat keys. It kept today's synchronous cleanup inside the lifecycle's empty notification, followed by an identity-checked removal. And it removed entries over a snapshot of the keys at shutdown. The specification said that everything the change touched was a typed change the compiler would enumerate on its own. The whole run turned on that claim.

The first reading found the claim false for test doubles. The runtime suites assert the registry's `register` and `unregister` arguments on untyped `jest.fn()` mocks. A positive assertion with the old argument count only turns red at runtime. One negative assertion, the cross-symbol isolation case's `.not.toHaveBeenCalledWith(...)` with three arguments, would never match a four-argument call again and would stay green forever, guarding nothing. The plan's discovery grep did not match the `.not.` form. The same reading found a comment above the run-owned order-axis teardown that justified its rule by «would decrement a live chart's refcount», a count this task retires. The planner widened the grep, named the negative assertion with its fixture's holder, and reworded the comment.

The second reading found the same kind of defect one step further out. The runtime's acquire-catch comment in `activate` still explained its guard as «would take a dynamic-TF reference belonging to another holder». Under named holders that is false: the real hazard is a slot re-activated under the same id, which shares the name. The plan had asserted that the existing comments «stay true». The detector suite and two runtime suites also kept test titles and describes that name `refCount`, `dynamicRefs` and «decrement», or spell out the old argument list. The planner retitled all of them and added a grep gate on the word.

The third reading found a single leftover: a title in the registry suite that still named «the exact argument values» as the old four without the holder. Apart from that, the reading confirmed the plan in full. The same class of omission had moved outward one ring per round, and each round closed only the instances in front of it. Nothing ever came back. In the same round, a reviewer's deferred observation surfaced a defect larger than the task. The close detectors key live series by symbol alone, so two exchanges streaming one symbol share one bucket. One exchange's consumers receive a candle mixed from both markets, and the other exchange's consumers receive nothing for it. This is reachable today: watch loops run per exchange and symbol, three exchange ids work, and the WebSocket door checks only that an exchange is present.

> The specification never named the part of the change's radius that the compiler cannot see. That part is every argument assertion on an untyped double for the changed methods, every private reach into the retired structure, and every comment or test title that explains behaviour by the retired count. Each needed its rule, a runnable sweep, and a recorded result.

**Classification:** specification gap (blast radius). The recurring signal is the same class of omission in all three rounds, at a new location each time.

## What was done

This was a spec-depth rescue with a full reset: the plan, its three plan-reviews and the sidecar were deleted.

Before the rescue, the user ruled that the exchange goes into the series key everywhere it had dropped out. The fix is one pool keyed by the full triple, not a pool per exchange, and holder names stay as they are. The documentation went first: a postulate in `docs/candle-pipeline/data-flow.md` § «Идентичность серии» says a live series is its exchange, symbol and timeframe together. A new phase placed ahead of this task carries three tasks: the tick detector keys its buckets by exchange, the close detector does the same, and a dynamic timeframe's registration names its exchange. That phase was pin-gapped task by task before anything runs. The pass found:
- every sweep line was written with a ripgrep flag that does not exist, so none of them ran;
- one invariant recorded something false;
- tests reach privately into the detectors' maps, and some of those assertions go vacuous once the top level becomes the exchange;
- one described failure did not match the mechanics of a shared count.

This task's specification was rewritten on top of that phase. The key is now composed from exchange, symbol and label. The specification carries the ground facts the discarded plan and its readings established, pinned as clauses of its own. Its untyped radius is written out as rule, runnable sweep and recorded result: mock argument assertions, with the cross-symbol negative pinned literally at five arguments; `mock.calls` positional reads; private reaches; count-worded comments and titles. The observation about the slot-map subscription registering after an unchecked `await` was routed to the task that already owns that re-read.

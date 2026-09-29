# 64.5 — a test count that aged under a neighbour

**Project:** tradeoxy_core
**Date:** 2026-09-30
**Stopped at:** planned:3
**Elapsed before the rescue:** 723

The first plan review found a hole neither the spec nor its gap-closing pass had seen. An empty page from the broker does not arrive as `{ orders: [] }` but as `{}`: proto-loader is loaded without `arrays`/`defaults`, and an empty repeated field is never encoded. The broker hands back a cursor whenever a page is exactly full, so a chain whose length is a multiple of the page size ends on an empty page, and the planned loop would throw on `page.orders` — silently, into `doLoad`'s dependency catch, leaving an active slot waiting with no warm-up. The reviewer proposed normalising the response at the gRPC client door (`orders ?? []`), which also repairs the same crash in the REST order history and the init-state reader; the planner adopted it with a client-spec case and an empty-final-page load case.

The second plan review found that removing the «capped at 200 rows» log line left `SlotHistoryFetchContext.configId` without a reader, exactly like the `logger` parameter the plan already dropped; the planner swept both together.

The third plan review failed the plan on a number. The acceptance step said «the spec's baseline is 24 tests; expect 27 passing», but the load-history suite now held 25: task 64.4 had landed first and added a case. The 24 came from the task spec, which recorded the gate's test count on the HEAD it was written against; the plan copied it, and a neighbour landing ahead of it made the copy wrong. The rounds ran out on that single stale figure, with the plan otherwise converged.

> The spec should have named its gate's suites and known reds without a count of tests — a count measured on one HEAD goes stale the moment a neighbour task lands first — and should have known that an empty repeated field decodes as an absent key.

Category: specification gap.

## What was done

Spec + plan depth. Spec 0255 now carries both resolved findings as the plan had them — `OrdersGrpcClient.fetchOrders` resolves `{ ...response, orders: response.orders ?? [] }` with a client-spec case feeding `{}` and the two repaired consumers named; the empty-final-page load case; `configId` retired beside `logger` — and its acceptance names suites and «all passing», with no count. The 64.5 contract line names the door normalisation and the dead fields. In the plan only the acceptance step changed: every expected test count replaced by the named cases passing beside every existing case. The same stale-count class was stripped from the open specs 0256 and 0257. The three plan reviews were deleted; the sidecar's `step` is `planned:1`, `planner` and `elapsed` kept.

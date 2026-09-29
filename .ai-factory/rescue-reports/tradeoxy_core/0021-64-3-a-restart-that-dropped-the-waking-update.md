# 64.3 — a restart that dropped the waking update

**Project:** tradeoxy_core
**Date:** 2026-09-30
**Stopped at:** escalated
**Elapsed before the rescue:** 241

The planner wrote its plan exactly to the task spec: while a watcher is stopping, a take keeps the same entry, and once the loop has run to the end of the stop, the continuation decides — holders remain, restart the loop; none, close. The first plan review accepted the plan with one correction taken from the governing document: `docs/architecture.md` § «Держатели общего ресурса» reads the one-time decision as «holders remain **and** the owner is not ending», a half the spec had dropped and the planner restored with an `ending` flag; the rest were assertion details.

The second plan review read down into ccxt and found the real hole. While the watcher is stopping, its loop is parked on `await entry.exchange.watchOrders()` — on a quiet account that lasts until the account's next event, possibly hours, so a broker reconnecting later than the grace period lands exactly here, the common case rather than a corner. When the event arrives, `watchLoop` sees `!entry.active` and breaks before the mapping loop, discarding the event; only then does `loopPromise` settle and the continuation restart the loop — and with ccxt's `newUpdates` delta mode the restarted `watchOrders()` never returns that update again. The holder that had just retaken the watcher loses, for instance, the fill of a market order, and nothing reports it. The old, divergent code did not lose it: its fresh entry shared the pooled ccxt instance and the same pending future. The spec called its code shapes exact and placed the revival in the continuation, so the reviewer could not repair it and escalated, offering three options — accept the loss, emit the waking result before the restart, or revive in place so the parked loop never exits.

The design came from decomposition, not from the orchestrator: the architect read the governing sentence («decided once, when the closing finishes») literally and put the decision after the loop exits, without asking whether the stop could simply be cancelled — the way a take during grace already cancels its timer through `onRetaken`. Two gap-closing rounds then added guards to that restart machinery (no second grace timer on a stopping entry, a reset error counter, new `WatcherEntry` fields); each polished the design, none questioned it, and none traced what happens to the update the loop wakes on.

> The spec should have made a take during stopping cancel the stop in `onRetaken` — `active = true` on the still-parked loop, unless the owner is ending — so the loop never exits and the update it wakes on is emitted through the normal path; no restart was ever needed.

Category: specification gap — introduced at decomposition and reinforced by gap-closing passes.

## What was done

Escalation, option 1: the decision was recorded in this task's spec. The user chose revival in place («в»). Spec 0253 was rewritten in full: `isClosing` covers grace and stopping; the `subscribe`/`subscribePublic` pre-checks evict only a `FAILED` entry; `onRetaken` revives a `STOPPING` entry in place (`active = true`, `connectionState = CONNECTING`) unless a new service-level `ending` flag — set first in `onModuleDestroy`, whose own loop also marks entries `STOPPING` — says the owner is ending; the grace continuation acts only on an entry still current and still `STOPPING`. The restart branch, the new entry fields, the error-counter reset and the `onEmpty` guard are gone. The rewritten stopping case resolves the parked watch with a non-empty payload and asserts both the pre-stop and the retaking subscriber receive it. The 64.3 contract line was rewritten to match. Full reset: the plan, both plan reviews and the sidecar were deleted; no code had been written.

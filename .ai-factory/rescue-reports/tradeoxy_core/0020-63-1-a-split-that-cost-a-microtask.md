# 63.1 — a split that cost a microtask

**Project:** tradeoxy_core
**Date:** 2026-09-30
**Stopped at:** escalated
**Elapsed before the rescue:** 123

The implementation carried out the split exactly as the task spec pinned it: it added `recordActivationFailed` and `recordDeadSubscriptionFailed`, rewrote the `mark…` functions to await them before emitting the owner notice, and removed both the emitter and the `notify` flag from the REST resume handler. Three scenarios in `indicator-runtime.step-failure.spec.ts` then went red, although the spec promised that the server-originated paths stay unchanged.

The cause was the shape the spec pinned for `record…`: an `async` function awaiting `repository.update(…)`. With `mark…` awaiting that function, one async promise waits on another, so the owner notice — and, when the write rejects, the logged rejection — lands one microtask later than before. Scenarios 1, 9 and 11 pin exactly that tick, and the codebase already guards it on purpose: `ActiveSlotKind.onFailure` in `slot-kind.ts` returns `markActivationFailed`'s promise directly rather than awaiting it, and its comment says why. The implementer saw two ways out — accept the extra tick and rewrite three assertions and that comment, or return the repository's promise directly against the letter of the spec — and neither was within its authority, so it stopped.

The spec's shape came from a gap-closing pass that fixed a type mismatch — `ActiveIndicatorRepository.update` returns `Promise<ActiveIndicator | null>`, not `Promise<void>` — by making `record…` `async` and awaiting inside, without weighing the timing that change imposes. The earlier form, `return repository.update(…)`, preserved the tick and lacked only the right return type.

> The spec should have pinned `record…` as non-`async` functions returning `ActiveIndicatorRepository.update`'s own promise, typed `Promise<ActiveIndicator | null>`, so that `await record…` inside `mark…` is tick-for-tick the inline `await repository.update(…)` it replaces — as `ActiveSlotKind.onFailure` already does.

Category: specification gap — introduced by a repair of the spec, not by the original decomposition.

## What was done

Escalation, option 1: the decision was recorded in this task's spec. The user chose the form without the extra step. Spec 244 now pins both `record…` functions as non-`async`, each returning the repository's own promise typed `Promise<ActiveIndicator | null>`, with the `ActiveIndicator` type import, the reason stated once by name, and the three step-failure scenarios named in the gate as untouched and green. The contract line needed no change. Full reset: the plan, its plan-review and the sidecar were deleted. By the user's ruling that a spec-depth rescue rolls back everything, the attempt's uncommitted code in `active-indicator-outcome.ts`, `active-indicator.service.ts` and `active-indicator.service.spec.ts` was reverted to HEAD, so the next plan starts from the code the spec describes.

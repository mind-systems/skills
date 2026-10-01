# 67.4 — a resolved retry that left no slot

**Project:** tradeoxy_core
**Date:** 2026-10-01
**Stopped at:** planned:3
**Elapsed before the rescue:** 678

The task was to tell an activation's owner, over the socket, that a wait on a failed dependency had ended — an `active` notice sent once when a boot-time wait's retry succeeds. The first plan did what the spec said: send the notice at the point the wait already logs a successful end. The reviewer found that a retry resolving without an error is not the same as an activation that runs. An order-axis indicator waiting at boot can have its retry cut by the broker declaring the subscription dead: the dead-stream listener tears the slot down, writes the row `failed` and tells the owner so, and the retry's own warm-up then returns quietly with no slot. The wait would have followed the `failed` notice with `active`, showing the owner a running indicator over a failed row with nothing behind it. The reviewer proposed that the retry report whether it left a live slot, and that the notice go out only when it did.

The second plan adopted that: the runtime's retry closure reads back whether the config still has a slot, and the wait acts only on that answer. The reviewer then found that nothing tested the read-back itself — the wait's suite stubs the yes/no answer directly, so a later edit that broke the read-back would bring the original defect back with every suite green. It asked for a runtime-level scenario: a dead stream cutting the retry sends only `failed`; a clean retry sends exactly one `active`.

The third plan added that scenario and was sound in substance; the reviewer stopped it on three precision points — the new scenario missing from the test file's own list of scenarios, a logging note that described a rename where the task adds a new warning line, and one place where a type had to change left out of the plan's list of such places.

> The spec said to tell the owner where the wait logs a successful end without defining success; success is a retry that leaves a live slot for the config, and a retry can resolve without one when the subscription is declared dead mid-attempt.

Classification: specification gap; no recurring issue — each round's finding was new, and the plan converged.

## What was done

Repaired at spec + plan depth. The task spec now defines a successful end as a retry that leaves a live slot, has the retry callback report it, sends the notice only then, ends a no-slot wait silently with a warning, and names the runtime scenario and the test-file header item among what the task changes. The plan folds in the third review's three precision points. The three plan-review files were deleted; the plan and the sidecar were kept, the sidecar's step set to `planned:1` with the planner session and elapsed time preserved, so the orchestrator resumes at plan review with the repaired plan.

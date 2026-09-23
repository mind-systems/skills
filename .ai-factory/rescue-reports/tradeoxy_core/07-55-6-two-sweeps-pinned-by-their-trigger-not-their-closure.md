# 55.6 — two sweeps pinned by their trigger, not their closure

**Project:** tradeoxy_core
**Date:** 2026-09-22
**Stopped at:** planned:3
**Elapsed before the rescue:** 1673

The plan turned spec `183` into a file-by-file retype driven by the compiler: every `string`-typed id parameter of the logic layer becomes `UUID`, `tsc --noEmit` drives the sweep, and each site that stops compiling either canonicalises through `toUUID` at a boundary or threads a `UUID` it already held; the three replay doors drop their case-refusal clause and canonicalise once, their three tests flip, and a round-trip case is added. Its ground was checked and held: every "already `UUID`" claim true in the tree, the spec's own sweep reproducible, `DeadSubscriptionError` and `OrderStreamDeadPayload` landed exactly as the spec anticipated.

The first read found one real defect. The flipped gRPC register test leaned on a client `call.end()` to evict the parked entry, but a client half-close never reaches the server's own finish — the stream stays half-open — and the test carried no await point between writing to the channel and asserting on the spy, so it asserted before the server had even read the message. The repair was a distinct literal for each of the three gRPC cases and a deterministic wait threaded through the spy itself.

That closed, the second read found no blocking defect — only that a file the task edits, `output-handlers.spec.ts` under `src/indicators/runtime/__tests__/`, sat outside the suites the task's own acceptance run names: the task would change a file whose tests it never ran. One wording correction rode alongside it: `02-wire-contract.md` § Shape states the sender's own discipline truthfully; what the door comment got wrong was the inference drawn from it, that a door must refuse a case.

That closed too, and the third read found less still: the fixture-rename rule replaced the ids only where they sat inside single quotes, leaving test titles and comments in two files still spelling the old one — a title naming a call the test would no longer make.

Each round's own findings shrank, and none recurred verbatim; what recurred was their shape. The task rides two mechanical sweeps — the compile-driven retype and the fixture rename — and the spec pinned each sweep's own trigger without ever pinning where it ends.

> The spec never said where a sweep closes — that every file it touches belongs to the task's own acceptance run, and that renaming a fixture id renames every mention of it, quoted or bare — so each round closed one instance and the next found another.

**Root-cause category:** specification gap. **Recurring signal:** the unfinished-sweep shape, twice running.

## What was done

The repair went to spec and plan depth. Spec `183` gained the two closure rules and a sentence leaving the doors' own error strings to the boundary-constructor task (spec `187`), which took that observation into its own scope along with the one assertion it rewrites; spec `188` lost its now-false claim that `AlertEngineService.process` keeps a `string` parameter. The plan's own fixture-rename rule widened to every mention and named the lines, including two more a fresh sweep found. The three prior reads were deleted; the plan and the planning session were kept, and the run resumes at the reading of the plan.

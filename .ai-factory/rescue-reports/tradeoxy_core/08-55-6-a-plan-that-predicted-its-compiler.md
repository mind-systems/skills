# 55.6 — a plan that predicted its compiler

**Project:** tradeoxy_core
**Date:** 2026-09-22
**Stopped at:** planned:3
**Elapsed before the rescue:** 4860

This is the second rescue of this task. The first repair closed a different shape — a sweep pinned by its own trigger and never its closure. This run tells its own story.

Round one opened on a citation to a sentence that no longer exists: the plan's test section argued against a line in spec `183` that the previous repair had deleted, and nothing had swept the plan for it. The reader verified twice — read the file, then searched it — and named the risk exactly: an implementer told to reconcile against the spec finds nothing there, and either stalls or assumes the plan knows something the spec does not. Beside it, two test snippets used a scenario key variable nothing bound, in a file whose scenario map is shared across the whole suite.

Both closed. Round two then took the plan at its word: it applied every retype the plan names, ran the compiler, and compared the result against the plan's own list of files it expected to break. In one directory the compiler named four files where the plan named three, and one file the plan named does not break at all; the two it missed are specs sitting beside their service rather than under a tests directory — the very shape the same sentence goes out of its way to correct in three other directories. The same round found that the plan's resolution rule, "exactly two forms", had no form for the one site that is neither a literal nor a production boundary: a test that mirrors the runtime's own JSONB read into a hand-built slot.

Both closed. Round three found that the reason the plan gives for one of its predictions — a spec file compiles untouched because a set it builds infers its type contextually — describes a line that lives in the production gateway, not in that spec. The observation is true; the file it is attached to is the wrong one.

The thread only shows from the third round: the plan predicts the compiler's output file by file, attaches a reason to each prediction, and every reader runs the compiler and audits them. The predictions have no consumer — whoever implements runs the compiler too, and its list is the authoritative one — while the audit surface is as large as the number of files and reasons.

> The spec made the compiler the sweep's driver but left the plan free to carry an enumeration of the compiler's own output as though it were a requirement, and a prediction of a tool's output is not a constraint — auditing it has no end.

**Root-cause category:** specification gap. **Recurring:** an audit of predicted compiler output, three rounds running.

## What was done

The repair went to spec and plan depth. Spec `183`'s first closure rule now puts the obligation on the acceptance command's coverage — the compiler is the sweep's only enumerator, and no artifact of the task predicts which files fail or argues why one will not — and the plan's per-file prediction and its reasons are gone, replaced by "whatever the compiler names", with the same genre removed in three other bullets; the fact about contextual type inference moved to the two gateway tasks whose own lines it explains. Two errors of the previous repair were corrected on the way: a phase pointer left naming a document section that had been emptied, and a phase note still narrating the story the ruling had ended. One factual defect in the spec was repaired at its home rather than routed around in the plan: the trio of boundary reads it names lives in `activate`, `computeWarmupRange` and `subscribeLayout`, not `doLoad`. The three prior readings were deleted; the plan and the planning session were kept, and the run resumes at the reading of the plan.

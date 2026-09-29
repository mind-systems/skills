# 59.6 — a spec that aged under its own phase

**Project:** tradeoxy_core
**Date:** 2026-09-28
**Stopped at:** planned:3
**Elapsed before the rescue:** 552

This task is the last of a six-task phase. It retires a field that says whether a runtime slot is an activation or a chart preview. The five tasks before it moved every read of that field onto an object the slot carries. What remains for this task is to delete the field, to add a plain-string label for the one log line that still names the kind, and to reword whatever still quotes the field. Its spec was written, and pin-gapped by the planning pair, before any of those five tasks had landed. Every sweep it records was measured against a tree that no longer existed by the time the task ran.

The first plan was correct in substance. Every production edit it proposed matched the tree as it stood, and the reviewer raised nothing critical. It did raise five inaccuracies, and each traced back to the spec rather than to the planner.

- The plan expected an alert-decision function to live in the runtime service, as the spec said. The fifth task had moved it into its own class.
- The plan told the implementer that the compiler would flag only one test file once the field was gone. The spec had filed two test assertions reading the field under the untyped radius, reachable only by sweep. Both actually read the slot through the registry's typed lookup, and the project's compiler configuration includes the test files, so the compiler reports them the moment the property disappears.
- One test was located under the wrong describe block.
- Two stale comments sat outside the two files the spec's comment sweep had covered: a test file's header, and the event docblock beside the one the plan already fixed. That second docblock named an emitter that an earlier task in the phase had replaced.

The planner fixed all five, word for word as suggested.

The second reading found one more defect of the same shape. Two test titles quote the field in double quotes, with a space after the colon. The spec's sweep pattern matched single quotes only, and so did the plan's acceptance check. The check would have passed with both stale titles still in place. The planner added them and widened the pattern to every quote style.

Its third plan was never reviewed, because the run ended there. Swept independently against the tree, that plan's acceptance pattern reaches thirty-five lines across eight files. The plan names every one of them and nothing beyond them.

The failure chain was therefore not a planner struggling. It was a planner discovering, one round at a time, a radius the spec should have handed it whole. The spec's own rule said that nothing quoting the field in code form was carved out. Yet its sweep was scoped to two named files and one quote style, both chosen at a moment when the neighbouring tasks had not yet changed which files carried the quotes.

> The spec's comment sweep should have run over the whole source tree with a pattern matching every quote style, and should have filed the two test reads that go through the registry's typed lookup under the typed radius. Phrased that way, it stays true however the earlier tasks in its own phase reshape the file.

**Category:** specification gap — a spec aged under the earlier tasks of its own phase.
**Recurring:** the code-form quote outside the spec's sweep appeared in both rounds.

## What was done

The repair depth was spec plus plan, with the plan left untouched because it was already correct.

The spec was rewritten against the current tree:
- one whole-tree sweep, run as printed, with its result recorded by site;
- the three backticked narrations the pattern cannot reach, named individually;
- the two test assertions moved into the typed radius, with the reason (the registry's typed lookup, and the test files falling under the compiler's include);
- both event docblocks named with their current emitters;
- the acceptance baseline re-measured on the current tree (378 passed, one known red, named);
- every stale pre-phase count and location deleted.

The contract line lost its counts of literal sites and comments, and now names the radius by kind instead.

Both plan-review files were deleted. The sidecar was rolled back to `planned:1`, so the orchestrator re-reviews the standing plan against the repaired spec. The plan-review's deferred observation, that the gateway spec's slot-building test helper is typed `any`, went nowhere this session because both files are gone. The planning pair holds it as a debt for the next phase, whose task will touch that helper if the next field it retires lives there too.

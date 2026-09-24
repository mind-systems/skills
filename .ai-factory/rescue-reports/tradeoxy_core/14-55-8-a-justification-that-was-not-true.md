# 55.8 — a justification that was not true

**Project:** tradeoxy_core
**Date:** 2026-09-24
**Stopped at:** planned:3
**Elapsed before the rescue:** 1941

This task had already stopped once, on a decision no agent could make, and that decision was ruled and the task reset whole. What follows is its first ordinary run: a fresh planner, from nothing, three readings, all of them low risk, and no ratified plan.

The findings shrank as the rounds went: two, then one, then one, each closed by the next round's plan. The first reading noticed that two suites named in the acceptance run do not exist on disk — they are the ones this task itself creates, so the naming was right and only its silence about that was wrong — and that one of the sites the sweep must reach was left unnamed. The second found that the change leaves an import dead in two files and alive in a third, where one use survives it, and that nothing in the gate would see it: the type-checker is not configured to report an unused local, and the linter is deliberately not part of the acceptance run. The third found a single sentence, justifying why the gate must not call the repository's own lint script, that was simply false about what that script's automatic repair would do to the rule in question.

Only the last of the three was still open when the run ended, and it turned out not to belong to the plan at all. The same false sentence stood in the task's own specification, and the plan had inherited it rather than invented it. Repairing only the plan would have let it return on the next planning.

Two of the four findings were one family, and it has now produced findings in four consecutive tasks of this phase: residue a mechanical sweep leaves where no gate can see it — a file the sweep touched that the acceptance run never names, a symbol left imported after its last use went. Patching the instances had not stopped it.

> The specification carried a false reason for a correct instruction, and the plan inherited it; and the residue a sweep leaves where neither the compiler nor the linter looks had been closed four times by enumeration and never once by a rule.

**Root-cause category:** specification gap. **Recurring signal:** the sweep-residue family, four tasks running.

## What was done

The false sentence was replaced at both homes, the plan's and the specification's, with the reason that is actually true: the repository's own lint script repairs in place across the whole tree, which a gate is forbidden to do, and would bury the one expected report inside a known formatting baseline. The instruction it justified — lint the probe by path — was correct and stands untouched.

The family got a rule rather than a fifth patch. The specification now states, once, that the sweep is closed when every file it edits belongs to the task's own acceptance run and every symbol whose last use it removes is dropped with it and named in a residue check that run executes — because neither ordinary gate reports it: the type-checker is not configured to, and the linter is not in the gate. The enumeration below it stays what it always was, a candidate set the rule is checked against.

One thing belongs in the record because it is the coordinator's own error and it nearly cost a run. The diagnosis was drawn from the first reading's findings as though they were the run's open defects; two of them had already been closed by the plan two rounds earlier. A reading's findings are a chain, not a list — each round's plan answers the last round's findings, so what is open is on disk and not in the earliest review. A newly spawned hand, holding none of this pair's history, found that by opening the file and said so rather than following the order.

Three readings were deleted; the plan and its planning session were kept, and the run resumes at the reading of the plan.

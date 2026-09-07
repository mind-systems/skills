# 29.1 — the task was decomposed from a governing text that described a different command

**Project:** skills
**Date:** 2026-09-07
**Stopped at:** `planned:3` — three plan-review rounds, no pass, nothing implemented
**Elapsed before the rescue:** 896 seconds

Written by hand, ahead of the capability task 30.1 adds. A report the mechanism produces will carry the same four fields and the same two sections.

## What the task was for, and what it said

`command-pin-gaps` exists to answer one question: where would the implementing agent have to invent? The rewrite in 29.1 was supposed to give that question a method — read the task, its spec and the code it lands in, and reason the way the orchestrator's planner and reviewer will, so that what reaches the run is joined to the code that already exists. Nothing in the family had ever read code at decomposition time, and on a large codebase a task written away from its code is almost entirely fantasy, which is what exhausts the run's budget.

What the task actually said was different. Its contract line opened with "walks the transformation the task claims — this governing spec, through this task, into that code", and half of its spec's central item was machinery for locating the phase section, reading both pointers on the phase header, and emitting a finding when the phase named no document. That is phase-tier bookkeeping. It belongs to `roadmap-outline-deep`, which writes the phase note, and to `roadmap-decompose`, which reads both pointers when it cuts tasks. The command's own subject — the code — got one clause.

## Where that came from

Not from the planner, and not from the decomposition alone. The governing text the task was cut from said it first: § "Пины" of `docs/sakshi-harness/skill-cycle.md` described the command as walking "из governing spec через task в код" and reading "оба указателя на заголовке phase". The task spec inherited that sentence, the contract line repeated it, and the plan expanded it faithfully. Every artifact in the chain was consistent with the one above it; the chain was consistent with the wrong thing.

The doc had drifted there under the pull of neighbouring work. Task 28.1 had just given the phase tier its note and its two header pointers, and 28.2 had just given those pointers their readers. Both were fresh, both were correct, and their vocabulary leaked one tier down into a command whose subject is not the phase at all. Nobody asked, for this command specifically, what the task would give in the end and who would read what it produced.

## The three rounds

Round one found the plan citing the ratified doc at two paths that do not exist, and reasoning from Phase 29 carrying no `Governing spec:` that the phase preamble was its authority. It also found the walk had no stated behavior for a target with no phase under it, though the command's own target resolution allows exactly that.

Round two closed all six of those. Writing the no-phase exit out in full exposed two more holes in the same paragraph: the walk never said which roadmap file to open before locating the phase, and the no-document branch had been nailed to a directory named `docs/`, which is wrong for a command that ships into projects whose documentation directory is named otherwise.

Round three, with both branches finally complete, found that they contradict each other. A phase that is located but names neither pointer satisfies both: the exit says emit nothing, the branch says emit a finding owned by `aif-docs`. That is Phase 29 of this very roadmap. The origin was a borrowed sentence: `task-rescue` reads "no phase, or neither pointer is named, proceed as today", and there it is right, because at that step the only question is whether to open a file. For this command, "no document is named" is the finding itself, so the two conditions must be disjoint, and no artifact in the chain ever said so.

Every finding in all three rounds landed inside that one paragraph. The capability the task existed for — read the code, reason as the planner and the reviewer will — was never exercised by a single round.

## Why the ordinary repair would not have worked

The rescue's own depth menu offers spec, spec plus plan, spec plus plan plus code. All three assume the task is aimed correctly and mis-specified in detail. This task was aimed at the wrong tier, so any of them would have produced a fourth round inside the same paragraph. What was needed first was a decision that the paragraph should not exist, and that decision was not the pipeline's to make: it came from the user, in words, restated three times, because the architect kept re-centring the command on documentation.

> The task was decomposed from a governing text that described a different command, so every artifact below it was faithful to the wrong subject, and nothing in the chain compares a task against what its skill is actually for before planning begins.

## What was done

Repaired in the order the family's own direction requires, docs before roadmap before code.

The doc first: § "Пины" was rewritten to say that the pass reads the task, its spec and the code it lands in, and mentally walks what the orchestrator will do — how the planner builds a plan against this code, how the reviewer judges the implementation — while never checking the pointers on a phase header, that being the other tier's work. Reading a document to understand a task stays ordinary, exactly as the orchestrator reads one when it needs one, and behavior no document describes stays a hole, because documentation is the foundation the code stands on.

Then the specification, at depth **spec**, full reset. Spec 103's central item was replaced; the stale figure in its class item was corrected; the verification bullets that tested for the phase-header branch were replaced by bullets testing that the pass does not check those pointers, that both halves of the emulation are stated, and that a fundamental conflict or code that does not come apart is raised as a blocker. A paragraph was added naming § "Пины" as the text the task is executed against, which is what round one lacked. The contract line lost the docs-first formula and gained the code side.

Then the rollback: the plan, all three plan-review files and the sidecar were deleted, so nothing of the discarded attempt survived into the next run.

**Result:** the orchestrator re-planned from the repaired specification, and 29.1 passed and was committed as `0762ab8` — one run, no second rescue. That run took three plan rounds and two code-review rounds of its own, and its sidecar records 1379 seconds. The repair let the task converge; it did not make it quick.

## What this run says about the system

Three planning rounds were spent inside a paragraph that should not have existed, and every one of them was a competent round. Review converges on the artifact it is given; it does not ask whether the artifact is aimed at the right thing. That question was answered only when a human said, in plain words, that checking the preamble is not this command's job.

The same shape had already appeared once this week on task 28.1, where a one-sentence ruling grew into a routed finding class with an owner, and the rescue that followed invented a term for it and wrote two lines into the roadmap that nobody asked for. Both incidents share a cause: a phrase from a neighbouring, correct piece of work carried one tier further than it belonged, and no step in the chain compares the task against the purpose of the skill it changes.

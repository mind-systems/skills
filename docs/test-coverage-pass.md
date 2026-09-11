# The test-coverage pass — where the operator is load-bearing

Read cold, a run of the test-coverage pass looks like a chain of mechanical steps. It is not: several of those steps stop and wait on a person, not because the pass is unfinished there but because the decision at that exact point cannot be made by anyone who is not the operator. Read the skill body alone, a deliberate stop and an unfinished gap look identical — both are a place the pass does not decide something for itself. This document draws that line, so a reader, and a future change to the skill, knows which of the two it is looking at.

## The operator vets scope before research spends anything

The pass sorts every candidate area into kept and dropped before any research begins, and shows both sets to the operator before committing to either. That is the one point where scope can be vetoed cheaply — before an agent has read a single file over it — which is why the sorting happens there rather than being folded silently into a later step.

The pass ends the same way it opens: on a question only a person can answer, about what to do with what it found. A run with no operator actually present to answer that — the pass invoked end-to-end by something else, not read by a person — cannot answer it, and the pass stops there by design, not by an omission a later revision should close.

## Grouping is left unpinned, on purpose

Related tasks land on the same file across a feature's whole life, not inside one run, and the call about which of them belong together in one coverage area is left to whoever is running the pass rather than fixed by a rule. A rule would eventually group two unrelated tasks that happen to touch the same file, or split two tasks that are really one piece of work, and the person who owns the tasks is the one who can tell the difference — the pass does not try to stand in for that judgment.

## Research runs in disposable hands, never a persistent one

Once scope is confirmed, research fans out into one throwaway agent per area, run in parallel. Each exists to keep the deep reading — every method, every branch, every edge case a test must cover — out of the caller's own context, and each is spent the moment it reports back; nothing about it persists across the pass the way a paired hand persists across a session. That shape carries a structural consequence: the pass itself must run somewhere that can spawn agents of its own, and cannot be handed off to run inside one instead — a subagent spawning further subagents is not a shape every harness supports, and the pass depends on that fan-out to keep the deep reading affordable at all.

## The pass plans; it never writes a test

Everything the pass produces is research and a plan to act on it — never a test file of its own. The one narrow exception is patching an existing test whose assertions are still sound but whose call signature drifted out from under it, which is a repair to something already written, not new coverage. That boundary is what keeps the whole pass inside planning: crossing it would make the pass an implementer, which answers to a different review than a planner does.

## A production defect goes home through the operator

The most valuable thing one run finds is often not a coverage gap at all — it is a real bug, met while reading source to plan tests against it. The pass never routes that finding onward on its own initiative. It hands the finding to the operator, who has just watched the triage and already knows where in the roadmap it belongs, in the two-tier shape `roadmap-engine` already governs, in a way a rule reaching into the roadmap on the pass's own behalf could not reconstruct as reliably. This is a choice about who holds that judgment, not a missing wire between two systems that should really be joined.

## Every drop states why, because that is what makes a wrong one visible

What stays and what drops is decided by `test-philosophy`'s own silent-failure discriminator, applied to each candidate in turn — but every area the pass drops still carries the one sentence that explains the drop. An unexplained drop cannot be checked by anyone reading the result later: the stated reason is the only thing that lets a wrong call be caught rather than simply trusted, and a wrong drop has in fact been caught this way once already.

## One note per area, phrased as a behavior under a condition

A finding never merges two areas into one note — merging would make the note about a component instead of about the finding, and lose the boundary a later reader needs to act on just one of them. Each case inside it is written as a behavior under a condition, never as a description of the code: that phrasing is what lets the result be used directly, rather than read once more before anyone can act on it.

## A number is fixed before research; a name is not

The number a new note is filed under has to be settled before research starts, or two areas researched in parallel collide on the same file. The name cannot be settled at the same moment: research is what can show that an area named for one thing is really something else, and an area has had to be renamed after the fact for exactly this reason. The two are pinned at different moments on purpose — the number early enough to prevent a collision, the name late enough to still be true once research has actually looked.

## Where things are normed

This document governs `roadmap-test-coverage`; its behavior is the skill's own, described here rather than restated in the skill body. `test-philosophy` supplies the silent-failure discriminator the drop reasons above lean on, and `roadmap-engine` supplies the two-tier shape a routed defect ultimately takes — neither is restated here.

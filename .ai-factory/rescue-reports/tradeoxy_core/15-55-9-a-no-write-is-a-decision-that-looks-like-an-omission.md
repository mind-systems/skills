# 55.9 — a no-write is a decision that looks like an omission

**Project:** tradeoxy_core
**Date:** 2026-09-24
**Stopped at:** planned:3
**Elapsed before the rescue:** 2166

This task was blocked by the planning pair for a fortnight, deliberately, until the task it re-expresses had landed and the assertions it flips had been seen to pass. Both conditions were checked — the second by running the scenario rather than reading it — and the block was lifted. Then the task failed on its first run, and it failed for a reason the coordinator had predicted it would not.

The task replaces a boolean and a nullable hint with one four-state value. Its extent is the easy half: remove a typed field and the compiler names every site that breaks. The coordinator, having spent the week on tasks whose extent was discovered rather than declared, classified this one as the cheap kind and said so out loud before the run.

The first reading found what that classification cannot see. The old encoding reaches one of its combinations — not ready, nothing pending — by two different routes: a slot that has never loaded, and a slot whose own indicator code threw part-way through a range extension and survived. The boolean pair collapses the two harmlessly, because nothing tells them apart. The new union does tell them apart, so the mapping has to choose; and on that one exit the plan wrote nothing at all, leaving a surviving slot in the state that means an extension is in flight over a slot that was already ready. The consequence is not cosmetic: the next dependency failure on that slot would falsely restore its readiness, start it stepping on an engine whose own replay had thrown, and record no pending range, so the retry that fires today would never arm — all of it under a task whose own stated constraint is that no production behaviour changes.

The second reading found that closed and raised three precision defects in the plan's prose, two of which would have been copied verbatim into code comments. The third found those closed and three more, all of them in the acceptance gate, one of which made the gate unpassable as written: it demanded every named suite come back green from a suite that carries a deliberately red skeleton, left there by an earlier phase for a machinery retirement still to come.

> The old representation reached one field combination by two routes and collapsed them; the richer one distinguishes them, so the mapping had to choose — and at the one exit where the plan wrote nothing, the omission silently chose the wrong state.

**Root-cause category:** specification gap — a re-encoding stated as a field rename, without the obligation that makes a re-encoding safe. **Behavioural severity:** one finding of the six could have shipped wrong behaviour, and it was found on the first reading.

## What was done

The specification carried a sentence saying the failing path was untouched by this task, which the repaired plan already contradicted — so a re-plan would have dropped the write again and returned the first reading's defect. It now states what that exit writes and why, in terms of the ambiguity rather than as an exception.

Beside the closure rule the specification already carried, which governs the sweep's extent, it gained a second, which governs the mapping's faithfulness: every reachable combination of the old representation maps to exactly one state of the new, and where the old was ambiguous the choice is made at the exit that produces it, never by leaving the state unwritten. The file now says plainly that these are two different obligations. The first was written before this run, from a week of paying for it; the second exists because this run showed the first does not cover a re-encoding.

The gate was repaired where it could not pass: its suite list is now composed from the paths whose behaviour changes rather than the files the task edits, which brought in the one suite that drives the exit the task adds a write to and that no file-derived list could reach; the pre-existing red skeleton is named as the expected baseline instead of demanded green; and a restated count was replaced by the command that produces it. The red skeleton was checked independently before being blessed — it was created red by its own task, and a later task retires the file with the machinery it covers, so it is a pin with an end rather than a regression.

The coordinator's prediction was wrong, and the way it was wrong is the useful part. Its measure separated tasks by whether their extent is a property of the code or a consequence of the change. That measure is sound and correctly called this task's extent cheap. It simply does not see a second kind of cost: a change that preserves behaviour while re-encoding it owes a per-path proof, and the proof's failures are silent and behavioural rather than loud and mechanical. There are at least two kinds of expensive task, and they want different rules.

Three readings were deleted; the plan and its planning session were kept, and the run resumes at the reading of the plan.

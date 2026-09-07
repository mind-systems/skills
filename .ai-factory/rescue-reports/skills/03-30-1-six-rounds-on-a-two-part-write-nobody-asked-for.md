# 30.1 — six rounds spent on a two-part write nobody asked for

**Project:** skills
**Date:** 2026-09-08
**Stopped at:** `planned:3` — three rounds of plan review, no pass, nothing implemented
**Elapsed before the rescue:** 2565 seconds cumulative, of which this run spent 1333

The second failure of this task. The first, and the repair that followed it, are the previous entry in this folder. Written by hand, like both siblings, because the capability that would write it is this task.

## What stopped it

Three rounds inside one branch, and the branch should not have existed.

The task was specified to write its report in two moments: open the file as soon as the diagnosis is written, complete it later, in place, once the repair is done. Between those two moments the file's path lives only in the session's own memory, with no durable home. So the plan had to say what happens when that memory is gone, and every answer it reached for needed another answer to make it usable.

The first round found six things. Three were left behind by the previous repair: the roadmap line still forbade the tool grant the specification had just come to require, the plan's own closing checklist still demanded that same tool line stay untouched, and its list of edit sites omitted the line the grant lands on. Two were staleness — the wrong lines cited for a category list, and the report folder described as holding a single file when the previous rescue had already written the second one into it. The sixth opened the funnel: the closing step said what to do when no report was ever written, and nothing about the case the plan itself predicted two bullets earlier, the file on disk and its name no longer in hand.

The second round closed five of those, and found the recovery branch written for the sixth resting on an input of its own. It said to reopen "this run's report by its slug" — but the slug is not written on disk in any form that identifies a run, and the folder can hold several reports for one task. The fix named a disk-readable rule: the highest-numbered report for this task whose closing section is still empty.

The third round found that rule's justification refuted two bullets above it. A run that ends early also leaves its section empty, so emptiness does not identify this run's report; and the re-resolution named one command where the address needs two, taking the project's name from the very memory the branch exists because it decayed.

> The report was specified to be written in two parts separated by an arbitrary stretch of work, so the plan had to reconstruct session state from disk, and each rule it invented for that needed a further rule to disambiguate it.

## Where the two parts came from

Not from the requirement, and not from either failure. The task was written with a single write at the end. The split was added afterwards by the planning side, as an amendment answering a remark that a long stretch of work can pass between a rescue's start and its finish. That remark named a difficulty; it did not ask for a mechanism. The amendment turned it into one, and the specification went to its first run already carrying it.

## What was done

Repaired at depth **spec**, full reset.

The report is written once, at the end, when the repair is done and the task is ready for a new run: the four facts, the diagnosis as it was written, and what the repair did. Everything the split had grown was deleted with it — the path carried across a gap, the recovery from lost context, the section left open, the branch for having nothing to close. Where the report cannot be written at all, the rescue says so plainly and finishes; there is no second write and nothing is reopened later, which is the accepted cost of writing once.

The roadmap line was corrected in the same pass: it still forbade the tool grant that the previous repair had made mandatory in the specification.

The plan, its three rounds of review and the sidecar were deleted. Nothing of either attempt remains on disk.

**Result:** not yet known — the task has not been re-run.

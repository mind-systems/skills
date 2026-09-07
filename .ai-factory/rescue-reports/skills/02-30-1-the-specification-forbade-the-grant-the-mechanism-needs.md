# 30.1 — the specification forbade the one grant the mechanism needs

**Project:** skills
**Date:** 2026-09-08
**Stopped at:** `planned:3` — three rounds of plan review, no pass, nothing implemented
**Elapsed before the rescue:** 1232 seconds

Written by hand, like the first entry in this folder, and for a sharper reason: the capability that would have written this report on its own is the task that failed.

## What the task was for

`task-rescue` already writes a full diagnosis of every failure it examines, and prints it to chat only. The moment the repair runs, the artifacts that diagnosis was drawn from are deleted, and at the deepest repair the record of time spent and the stage reached goes with them. A task later dropped or re-decomposed takes the rest. 30.1 makes that record durable: the report is opened through the shared distiller as soon as the diagnosis is written, and completed in place once the repair is done, in a folder in this repository that collects runs from every project.

## What stopped it

The distiller creates its destination directory before saving. It does that unconditionally, on every invocation, whether the directory exists or not. `task-rescue` has no grant for that command, and the caller carries it — the one other caller that delegates writing to the same distiller carries it for exactly this reason.

The task specification forbade it. One guard said no new tool grant of any kind, and the verification pinned the tool line to be byte-identical to the one already committed. Together they left the planner one route: declare the directory a setup precondition, and add a clause for the moment the run is refused. That route was taken, and it costs the feature its reason for existing — a first rescue in any other project would end without a report.

## The three rounds

The first round verified every citation in the plan, ran the path resolution live, and still found four gaps. The grant was the first and it was the one the plan had no power to close. The other three were narrower: the heading of the outcome section was described but never pinned literally, so a session returning to the file hours later would have nothing fixed to match; the template asked for the diagnosis "exactly as it was written", which does not exist in that shape for a run that stopped on a decision rather than a defect; and the failure clause covered only a destination that cannot be written, not a repository root that does not resolve at all.

The second round closed those and found the same gap one line above where it had just been fixed: the report's filename still assumed a root cause, on branches that have none. It also found that the first round's repair had planted a false premise — the directory was called a precondition, when the command that creates it runs on every invocation regardless. The exposure was not the first run in a new project. It was every run, everywhere.

The third round confirmed those closed and found the same shape a third time, in a new place. The failure clause now correctly says the run continues without a report, so a degraded run reaches the closing step — and the closing step was written for a run that has a file to close. The two things an agent reaches for there, calling the distiller a second time or writing the outcome somewhere else, are both forbidden elsewhere in the same plan and neither ban is restated at that spot.

The gap was reachable before any of this. A pass whose whole purpose is to find where the run would have to invent was run over this task beforehand, by two readers, and both stopped at the distiller's list of caller hooks instead of descending thirty lines to the shell command it actually issues.

> The specification forbade the grant the mechanism requires, so three rounds of planning were spent building the only workaround left, and each round repaired one instance of a step assuming an earlier step's output while its nearest sibling instance went unswept — because no line anywhere stated the general rule that a step must say what it does when that output is absent.

## What was done

Repaired at depth **spec + plan**.

The specification now requires exactly one new entry on the tool line and names why: the distiller issues its directory command unconditionally, and the one existing caller that delegates to it carries the same grant for the same reason. The verification bullet changed from demanding the line be untouched to demanding exactly one addition and no other. The plan stopped building a workaround: the grant is taken, and the failure clause stays only where a failure is still real, a session that has not been given this repository as a writable directory. The closing step gained the branch it lacked — where the report could never be opened there is nothing to close, said plainly, with no second call to the distiller and no other path.

Both questions the planner had deferred were answered rather than carried: the grant, by the specification; and whether the skill's always-loaded description should mention the new file, by the ruling that the description decides when a skill is invoked and a durable side effect does not change that moment.

The three rounds of review were deleted, the plan kept, and the run set back to its first round of review.

**Result:** not yet known — the task has not been re-run. This report was opened by the repair and its outcome closed with what the repair did; whether the next run converges is the next entry's business, not this one's.

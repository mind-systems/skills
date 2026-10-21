# The head that starts the run answers for it

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

A run of the orchestrator is started by someone, and that someone is a head. This document
describes what follows when the family takes that at its word: the head that starts the run is the
one that answers for it, and it needs nothing from the orchestrator beyond what the orchestrator
already does.

## Who answers for the run

A head launches the orchestrator as a background process. The harness wakes the head when that
process ends, and the head reads what the run left in its artifacts and acts. The head that
launched the run is the responsible one, so nothing has to say who that is: no head is named in
a file of the target project, no second head exists for stops, and the orchestrator carries no
channel to a head and no wait of its own. It needs no upgrade.

On any stop, a failure, an escalation or a halt, the run ends, the head wakes, and it reads the
artifacts and rescues, as [the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md)
lays out for a head that meets a stopped task. A decision that is the user's goes to the user, as
for any head. The head is the same architect with the same skill
([paired-loop](../paired-loop.md)): what it learns to do is talk to the orchestrator through the
artifacts the orchestrator already writes.

## Deferred observations between tasks

The orchestrator already stops at a `---STOP---` in the roadmap and takes no task below it. A head
that wants to read a task's review before the next one starts can place a stop after that task.
The run ends there by the existing rule, the head wakes, and it reads the review's
`## Deferred observations`.

The head acts only when that section has entries; a clean task needs nothing from it. When there
are entries, the head reads each against the "now" of the open tasks below it. A task often lands a
little differently from its plan, and the specs after it drift; this is the moment that drift is
cheapest to catch, because the task above has just become code and nothing below it has been
planned yet. The head fixes the tasks below that the observation touches, moves the stop, and
starts the run again. The reviewer is the filter: what reaches the head is what the reviewer
chose to leave.

This is a live pin-gaps, triggered by a signal and not run on every close. One task's questions
are asked at the moment its "now" can first be read against real code, and not by a lens run over
every task in advance.

## What stays from the earlier idea

Pinning observations as they come, so that pruning no longer stumbles on a pile of unpinned ones
and its gate becomes a safety check.

The "met again" mark on a phase. An observation met once is a fact; met twice it is a debt
([paired-loop](../paired-loop.md) § "Where the pair's behaviour lives"). One worth fixing later
becomes a phase through the ordinary outline, or, where a phase for it already exists, a mark on
that phase that it was met again. So an observation stops turning into a task by itself.

Reading an observation as a colleague's suggestion and never as a ruling, just as a peer's message
is never the user's go. Once deferred observations steer future tasks, the pipeline's agents gain
a way to influence what comes next, and a chain that can only add is how a swarm of unwanted tasks
grows ([the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md) §
"What has to come before more autonomy"); the mark, and not a new task for each meeting, is what
keeps this from being one more operator that adds.

## Where the family lives

This is open. A head's session lives on the user's machine, and the run it starts can too: that
works today, but the machine sleeps, and a run that waits on a sleeping head waits for the
morning. A server would keep pace with the heads, but sessions are tied to an account, so a head
on a server and a head on the user's machine are not the same kind of peer.

The long-running service the family has described, the herald
([a monthly analysis sprint, and the service that holds the environment](a-monthly-analysis-sprint-and-the-service-that-holds-the-environment.md)),
has never been deployed. Nothing may be laid on it as if it ran.

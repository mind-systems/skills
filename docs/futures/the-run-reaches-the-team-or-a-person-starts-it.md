# The run reaches the team, or a person starts it

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

A run of the orchestrator ends in a stop, a failure or a finished roadmap, and some of what it
leaves needs a head to read it. This document describes how a head comes to read it without
becoming the run's watcher: a head is called only when there is something to read.

## The head does not launch or watch the run

A head that starts the orchestrator and waits for it pays in its own context. The run's outputs
and tool calls carry no reasoning, and they fill the head's window with what it will never need;
a hand spent on watching is wasted the same way. The head is the same architect with the same
skill ([paired-loop](../paired-loop.md)), and its context is what the pair thinks with, so
nothing in the run is routed through it by default.

## Two forms, neither chosen

**A run that starts itself and can speak to the team.** A script launches the orchestrator and,
beyond what the orchestrator does today, reaches a head when a task stops, fails, escalates or
leaves deferred observations. The script decides when to speak, from the artifacts it already
writes, and a head is spoken to only then. This is an upgrade of the orchestrator, and it has
not been chosen.

**A person starts it, as today.** The user launches the run, and the heads are called by the
user's word when a run has left something to read.

Either way the head that is called is the same ordinary architect, and it reads what the run left
in its artifacts.

## A head is called only when there is something to read

**A rescue.** When a task stops, a head reads the artifacts and rescues, as
[the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md) lays out for a
head that meets a stopped task. It writes its report and waits, paused, for the user's word: the
report is the interface and no question is put to the user. A decision that is the user's goes to
the user, as for any head.

**Deferred observations after a phase.** After each phase the user asks whether there are deferred
observations. That habit is the second call: the head reads what the reviews left, acts on it, and
a clean phase needs nothing from it.

## Deferred observations between tasks

The orchestrator stops at a `---STOP---` in the roadmap and takes no task below it. A person who
wants a task's review read before the next one starts places a stop after that task, and the run
ends there by the existing rule. That is how a person gets the wait.

The head reads the review's `## Deferred observations` and acts only when that section has
entries. It reads each against the "now" of the open tasks below it. A task often lands a little
differently from its plan, and the specs after it drift; this is the moment that drift is cheapest
to catch, because the task above has just become code and nothing below it has been planned yet.
The head fixes the tasks below that the observation touches. The reviewer is the filter: what
reaches the head is what the reviewer chose to leave.

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

This is open. The heads' sessions live on the user's machine, which sleeps, and sessions are tied
to an account. A run that speaks to the team has to find a head there, so a run on a server and a
head on the user's machine are not the same kind of peer.

The long-running service the family has described, the herald
([a monthly analysis sprint, and the service that holds the environment](a-monthly-analysis-sprint-and-the-service-that-holds-the-environment.md)),
has never been deployed. Nothing may be laid on it as if it ran.

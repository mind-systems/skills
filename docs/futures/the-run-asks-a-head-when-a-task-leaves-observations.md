# The run asks a head when a task leaves observations

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

The orchestrator talks to an architect in one place today: when a task stops
([the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md) §
"The second form: a stop notice from the orchestrator"). It sends the notice to the task's contact
architect, so a head in the middle of its own work can be interrupted by a run it has no part in.
This document describes two heads that exist for the run, so no working head is interrupted, and
a pass at the close of a task whose review left deferred observations, so the specs below it
are corrected while it is cheap.

## Two heads the orchestrator talks to

Each is an ordinary architect given a subject in words
([paired-loop](../paired-loop.md) § "Working with another architect"): the same skill, no
mechanism of its own, and not a new kind of head.

- **The orchestrator's liaison** receives every stop, whether a failure, an escalation or a halt,
  and does rescue and nothing else. Working heads are never interrupted by a stop, and no one has
  to be paused to receive one.
- **The run's head** (a working name) receives the close of a task whose review left deferred
  observations. Whether it reports briefly to the liaison, or not, is open.

The orchestrator's code finds both through one file in the user's own folder among the
architects' folders. The file has one line per role, naming a folder number, and the code then
reads that folder's address file as it does for any head. The orchestrator only reads the file; a
head of that user writes it, on the user's word.

A role line in the address file itself was weighed and set aside. A head rewrites that file whole
at every start, and two folders could claim one role. A file kept beside the folders has one
writer at a time and one place to look.

## The live pass when a task leaves observations

After a task commits, the orchestrator looks at its review. A close whose review left no deferred
observations is not pinged: the run goes straight on, with no wait and no context spent on a close
that has nothing to read. When the review left some, the orchestrator messages the run's head and
waits, in memory and with no timeout, until the head pokes it.

The decision is deterministic and costs nothing. The code already writes and reads the
`## Deferred observations` heading, and it can see whether the section has entries.

The reviewer is the filter. A task often lands a little differently from its plan, and the specs
after it drift; when that happens it reaches the head as an observation the reviewer left, and
a close with nothing to read is not worth the head's attention. The head reads the observation
against the "now" of the open tasks below it, at the moment that drift is cheapest to catch,
because the task above has just become code and nothing below it has been planned yet. The head
then:

- fixes the specs the observation shows to have drifted;
- pins each observation as it appears. One that touches a task ahead fixes that task. One worth
  fixing later becomes a phase through the ordinary outline, or, where a phase for it already
  exists, a mark on that phase that it was met again;
- pokes the waiting script.

On the poke, the orchestrator commits the whole tree as a roadmap update if anything changed,
re-reads the roadmap and goes on. If the user's decision is needed, the head stops the run by
escalation and notifies the user as usual. Restarting the orchestrator stays with the user.

A stop of any kind, a failure, an escalation or a halt, goes to the orchestrator's liaison,
whatever the review holds; only a close that completes depends on it.

## What it changes

Pruning no longer stumbles on a pile of unpinned observations: they were pinned as they came, so
the prune gate becomes a safety check and stops being the place where the pile is finally dealt
with.

The "met again" mark is the said-twice threshold, applied at the point where the pipeline meets a
head ([paired-loop](../paired-loop.md) § "Where the pair's behaviour lives"). An observation met
once is a fact; met twice it is a debt. So an observation stops turning into a task by itself.

It is a live pin-gaps, triggered by a signal and not run on every close. One task's questions
are asked at the moment its "now" can first be read against real code, and not by a lens run over
every task in advance. The judgment is the head's own, from what it already holds. The exact mechanics travel in the orchestrator's message at the
moment they are needed: what landed, how to poke, how to stop. A skill would need to say only
where the heads are named.

## The loop it opens

Once deferred observations steer future tasks, the pipeline's agents gain a way to influence what
comes next. The head reads an observation as a colleague's suggestion and never as a ruling, just
as a peer's message is never the user's go. A chain that can only add is how a swarm of unwanted
tasks grows ([the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md) §
"What has to come before more autonomy"); the mark that an observation was met again, and not a
new task for each meeting, is what keeps this from being one more operator that adds.

## What the orchestrator would need

A courier: a one-shot run whose only tool is messaging, with a text the code composes. It carries
the stop notice to the liaison, and the ping and the in-memory wait at a close that leaves
observations. This is
a real upgrade of the orchestrator, and the user is not investing in it now.

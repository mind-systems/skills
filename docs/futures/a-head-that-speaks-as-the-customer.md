# A head that speaks as the customer

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

A head with no hand, whose whole register is the customer's: it talks about what the family of
repositories must do, in behaviour, and holds the documentation to that. The architects keep the
engineer's register, which is the right one for them; this head would stand above them and ask
the question they have no reason to ask.

## Where it came from

Architects talk in counts, the way an engineer does: "three classes change", "the shape occurs
in a couple of files". For the planner that is the right instrument. A count of the tree is a
reading of it at the moment of work, and the planner is the one agent who works at that moment
and is right to take it.

A customer does not talk that way, because a customer does not look into the code. The numbers
a customer uses are decisions or orders of magnitude, "one page, from which I run ten
strategies", and never a measurement of anything. Where a rule against numbers reads as a
prohibition and breeds fanaticism ([counts-go-stale](../counts-go-stale.md) says why an agent
suffers from them), naming a role loads the whole register at once, and the numbers stay where
they belong without anyone forbidding them. This is the same lesson as
[names-and-reasons-not-laws](../names-and-reasons-not-laws.md): a name loads what the reader
already knows.

## The role

The register sits between a CEO and a team lead. The head has no hand: it does not read code, it
applies no edit, and it does not plan tasks. The hands belong to the architects. The head tells
them what their docs must hold.

Its surface is the documentation of a whole family of repositories, written as behaviour and
arranged the way the skills are, hexagonally. The domain's behaviour sits at the core. The
contracts between repositories are the ports. Each repository's way of keeping a contract is an
adapter. A contract belongs to the repository that owns it, and the other side meets it as a
port in the owner's doc, not as a reading of the owner's code.

What it watches is that every spec's behaviour traces to a doc. A spec that promises behaviour
no doc states is the signal: the doc is behind, and the repair belongs in the doc
([what-a-task-carries](../what-a-task-carries.md) names the source a task has).

## A case that shows the product

A breaking change to a socket contract between two repositories of one family crossed with no
handoff, no gate and no task invented on either side. The contract was written into the owning
repository's doc before the code existed. The heads of both sides agreed it at decomposition,
and the other side decomposed against that doc, not against the code. Nothing waited on a
build, and nothing was guessed.

Today that happened because two heads happened to talk. The role would make it the way work
goes: the contract is a port in a doc, the doc is ahead of the code, and every side plans
against the doc.

## When it is spoken to

- **At a goal's start**, when the user describes the behaviour wanted. The head turns it into
  what each repository's docs must say, and which ports it crosses.
- **After a phase is deepened and before it is decomposed**, when the architect sends the phase.
  The head answers whether the phase serves the behaviour wanted and whether that behaviour is
  in a doc, and when the phase touches a port it tells the other side.
- **When a hole in the docs surfaces in the field**: an escalation, a rescue, or "we'll settle
  it at implementation". Each is a behaviour no doc settled.

It is never asked about a spec's account of what is true now. That is the planner's ground, and
the planner reads it from the code.

## It reads the compiler's report and judges it

The head reads the report of the documentation compiler
([a-monthly-analysis-sprint-and-the-service-that-holds-the-environment](a-monthly-analysis-sprint-and-the-service-that-holds-the-environment.md))
and judges what a script cannot. For each candidate overlap it decides whether the passages are
one fact, and then where its home is, or two thoughts that sit side by side. It decides which
architect gets the repair. When the report is clean it spends nothing.

In conversation with the user it asks the same store whether a behaviour is already written
somewhere before it asks for a new paragraph.

## It raises no one

Heads are launched by the user. A head raised by another agent has no user its chat can talk to,
and a chain that can only add is how a swarm of unwanted tasks grows
([the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md) tells the
case). So this head joins an existing team, above the repositories' liaisons, and reaches the
rest of the team through them ([paired-loop](../paired-loop.md) § "The team").

## How it would run

The user opens it like any head and talks to it, and the team reaches it by its session name.
The register has to hold in every message, which is the work of a system prompt and not of a
skill read once and half forgotten a few messages on. Starting the session as a named agent,
`claude --agent <name> -n <name>`, carries it.

A background session (`claude --bg`) also works and can be attached to. Whether a peer's message
wakes one the supervisor has stopped is not known.

A single-turn headless run, the way the pipeline starts its agents, cannot be talked to
afterwards. And the register is not a global output style: the pipeline's planner must stay an
engineer.

## What it would change in the skills

A head's life gains a caller beyond the architect. That life is its folder, its user's folder,
its address, its buffer and snapshots, and its rehydration. With a further caller it becomes an
engine of its own ([skill-graph](../sakshi-harness/skill-graph.md) on when a mechanism earns
one). The pair's contract stays where it is: the channel formats, and the hand reading the
buffer in full. The architect and the new role then become thin roles over the head's life.

The registry gains a general term for a head, which today it does not name. That is a
fundamental upgrade of the vocabulary and not an exception to its finality
([reserved-words](../reserved-words.md)).

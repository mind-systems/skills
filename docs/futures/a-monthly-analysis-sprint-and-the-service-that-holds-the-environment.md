# A monthly analysis sprint, and the service that holds the environment

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

The family changes its skills and its docs constantly and has no regular look at what those
changes did. Phases pile up, each reasonable alone, and nothing asks whether the agents behave
any differently for them. This document describes a rhythm that asks, and the standing part of
the system that makes it cheap.

## A long-running service is the environment

An agent thinks only when there is something to think about. Everything that can be known by
reading, counting or comparing belongs to a service that is always up, and the agents are called
when a judgment is left. The user calls this service the herald. It receives pushes from the
repositories, keeps read copies of them, holds a vector store over their documents and an
episodic memory with search, writes reports and delivers them to whoever reads them. It is part
of the system beside the orchestrator: the orchestrator executes a task, the service watches
the family and remembers it.

One instance watches many projects at once. For each project it gives what is specific to that
project, and alongside, always, feedback to the family across every project it watches, not
only the family's own repository.

The service is described here only by what it does. Where it lives and what it is built from
are not this document's business.

## What it runs on a schedule, as scripts

**A compiler for the documentation.** A script reads the docs the way a compiler reads source
and reports what does not resolve:
- every link and every section anchor resolves;
- no doc is an orphan, unreachable from the trunk by links;
- no doc cites the plan layer, addresses by position, or carries a measurement of the tree
  ([reference-by-name](../reference-by-name.md), [counts-go-stale](../counts-go-stale.md));
- one concept is not called by two registry names ([reserved-words](../reserved-words.md));
- where the docs are arranged hexagonally, the direction of links holds: a core doc does not
  reach down into an adapter's doc, and a port is seen from both sides.

**Candidate overlaps.** The vector store answers, for each paragraph, where else the same thing
is said. A script can find two passages that sit near each other; it cannot decide whether they
are one fact with two homes or two thoughts that happen to be neighbours. The script produces
candidates and stops there; the decision belongs to a reader
([one home per fact](../philosophy/context-tree.md)).

**The behaviour of the pipeline and its agents.** Beside the compiler runs the analysis of how
the pipeline and the agents behaved: how a skill was invoked, how many rounds a task took to
plan, what its spec carried, where a rescue was needed. The family already keeps a method and
draft scripts for this, written for its rescue analysis; the service runs that method on a
schedule instead of by hand.

This analysis is the feedback to the family that the service gives across every project it
watches. The skills are loaded into every project's sessions, so how they move agents shows in
all of those projects, and an analysis of one repository sees only one slice of it. The rescue
analysis so far was done by hand over a few repositories at once, which is the same need.

## The cadence is monthly, and that has a reason

The analysis reads session transcripts, and some of the sessions it needs can still be asked
questions. Transcripts are cleaned up on about a monthly cycle, so the analysis runs before they
go. The cadence follows the record's life, not a calendar habit.

## A sprint over accumulated phases

Phases accumulate between analyses. At each analysis it is decided, on what the record shows,
which phases are implemented and which are left. That is the first answer the family gets to
whether its changes to skills move agents' behaviour at all.

It is also the deleting operator the chain lacks. Every other operator in the planning chain
adds, and only the user removes ([the-pipeline-speaks-to-an-architect](../the-pipeline-speaks-to-an-architect.md)
§ "What has to come before more autonomy"). At an analysis a phase can simply not be taken, and
the reason is the record, not a mood.

## The split between a script and an agent

A product the family reads arrived at this split under cost pressure. A watcher had an agent
walk a checklist on a short interval. Every item cost a turn, and every turn re-read the whole
context, so the price was the number of turns inside a run and not the number of runs. The
checklist became a single deterministic endpoint that answers whether everything is clear, and
the agent now spends turns only when the answer is that something needs judging.

The documentation compiler and the behaviour analysis are the same shape. The script says
"all clear" or hands over a short list, and a head or an architect spends thought on the list
and on nothing else.

## Who reads the report

The report goes to the head that speaks as the customer
([a-head-that-speaks-as-the-customer](a-head-that-speaks-as-the-customer.md)), which judges it
and sends the repairs to the architects whose docs they belong to.

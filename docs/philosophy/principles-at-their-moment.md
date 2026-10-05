# principles-at-their-moment — a well-known principle is carried as a question asked where the decision is made

The aim is that agents write code better than the user does, not worse. The principles that make
code good are well known, and an agent knows them as well as anyone. What this system adds is not
the principle but the moment: each one is asked, as a single question, at the point where the
decision it governs is being made.

## The aim and the form

A principle stated in general words constrains nothing. "Keep responsibilities single" or "depend
on abstractions" is true everywhere and decides nothing anywhere; an agent agrees with it and builds
what it was going to build. A law written to enforce it is worse, because a law outlives its case
([names-and-reasons-not-laws](../names-and-reasons-not-laws.md)).

So the family carries a principle in one form: a **question**, put by the skill that is in the
middle of the decision, to the thing being decided. The question names the principle's classic
wording, is short enough to be answered on the spot, and fires on an event, never on style. The
agent brings the knowledge; the question brings the moment.

## The principles, one by one

**Single responsibility.** A unit changes for one reason. It is asked wherever work is cut into
units. When a task is drafted, `roadmap-decompose` puts the Atomicity Gate to it: "Can the first
half be deployed without the second half and still make sense?" — and when the answer is yes, the
task is two. The contract-line rule in `roadmap-engine` says the same thing as an obligation on the
writer: "One reason to revert — if two concerns are independently shippable, make two tasks".
Documents are cut by the same measure: split "where its reason to change differs, never where it
merely grows long — the same rule that separates modules"
([reference-by-name](../reference-by-name.md)).

**Open/closed.** A kind is added without editing what already uses it. `polymorphism-philosophy`
holds the one question, "To add a third kind, how many places must change?", and the moment it
fires: "The arrival of the second invariant — an event, not a count of branches and not a
threshold." The first lens of `roadmap-decompose-skeleton` loads it and then will "apply its
question to the target task(s)"; where it fires, the task that cuts the seam, interfaces and types
with no bodies, comes first. Before the second member there is nothing to ask.

**Dependency inversion, and where to invert.** Details depend on abstractions the core owns. The
hard part is not the rule but finding where it applies, and that is what the architecture map is
for. `aif-architecture` writes it by reading the built design first: which interfaces have several
implementations, where and by what key one is chosen. The map then names the axes of variation, the
port each axis has, owned by the core, an adapter for each value, and the one composition root that
assembles them — Ports and Adapters, called by its name. The question it leaves behind is the
same at every junction: is this a difference between values of an axis? One repository's map says
what follows: "A new difference between modes or roles is a new implementation chosen at the
composition root, never a branch inside the flow." The map is a reference for every later
decision, and the lens above has something to be asked of only because the map names the kinds.

**Mechanism and policy; engine and model.** A shared how is separated from a deciding what. The
architecture of this repository puts it as a rule about when to factor a skill out: "only when it
carries shared content — a mechanism, rule, or format used by two or more callers". The question is
asked whenever a skill is written. An engine "holds no policy and never drives"; "the caller
supplies the hook points listed below; the engine supplies the mechanism around them", so a caller
that needs another shape adds a hook instead of copying the flow.

**Silent and loud failure.** `test-philosophy` asks, of any surface being considered for a test:
"If the logic here is wrong, does the system signal it immediately … or does it continue running
and produce wrong output silently?" Loud surfaces are skipped, because the compiler, the runtime or
the response code already tests them; silent ones are tested. It is asked when a test is planned
and again when one fails.

**One home per fact.** A fact has one place; every other mention links to it. The global
discipline states it once, as part of grounding: a fact kept in two places leaves no single thing
to ground on, and its second home is a link. It is asked whenever a sentence is about to be written
that something else already says.

**A task has a source.** `what-a-task-carries` asks of every task, when it is about to be written,
what it answers to: a document's promise, the user's ruling or the path to his goal. "A find that
has none of these is real and still not a task. It goes to the user". The question stops an agent
from turning a discovery into work nobody asked for
([what-a-task-carries](../what-a-task-carries.md)).

## What is not asked

Liskov substitution and interface segregation have no question: no operator in the family asks
about substitutability or about narrow interfaces. Where an architect designed the orchestrator's
verify step as a port, nothing asked how narrow it should be or whether its implementations must
be interchangeable. The design came out as one method, `verify`, for the code review and the test
run to implement, each returning whether it passed and writing its artifact, so either can stand
for the other — which is what both principles say. The user's hypothesis is that agents already do
this at a senior's level when nothing writes the answer for them, so the question is held back
until a case shows it is needed. This is one observation, not a rule.

## Where a question stops short

The lens asks whether a seam was cut at the arrival of a second member: in its own words, "does it
cut a seam at that arrival or not". It does not ask whether the cut is whole. One choice can still
sit in two sibling fields that must agree, and a pass that stops at "a seam was cut" does not see
it. This is a known gap, held until it recurs.

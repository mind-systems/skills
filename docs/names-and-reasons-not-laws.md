# names-and-reasons-not-laws — a durable text gives its reader something to reason with, not an answer to obey

A sentence written into a spec, a map, a buffer or a skill is read later by an agent that cannot ask
what it meant. What the sentence is — a name, a reason, a question, or an answer written for the
reader in advance — decides whether the agent reasons better for having read it or worse.

## The reader executes

An agent builds from a durable text. It does not obey every line: a convention that only asks to be
followed is read as content and left undone ([instruction-in-data](instruction-in-data.md)). But
what the text states as the shape of the work — a figure to match, a prohibition, "never X" — is
taken as authority and built in, and there it wins against the agent's own judgment, even where
that judgment is better. A person reading the same line weighs it against what they see in front of
them; the agent has usually seen less of the situation than the author did, and gives the author
the benefit of the doubt.

So a law in a durable text is not advice. It is an instruction that will be carried out in
situations its author never saw.

## What fails: an answer written ahead

Each of these happened, and each had the same origin.

**Numbers in specs.** A spec recorded a count; a planner copied it into the plan as a baseline, and
a reviewer checked the arithmetic after a neighbouring task had changed the tree
([counts-go-stale](counts-go-stale.md)).

**Checks and fences in specs.** Specs that told the implementer how to verify the result, and
fenced off what to leave alone, came back as plan steps and rounds of review — each round finishing
a procedure the author had pinned halfway. A task that had burned many rounds passed first time
once its spec said what must be true and stopped.

**Architecture maps that forbade.** One map said interface indirection was never wanted. Another
said time "is not tokenized". A generated one called the code's own design a "target architecture
to migrate toward" and listed the folders it should become. The user had built a system whose
variation lived behind interfaces, chosen at one place. Agents reading the maps took them as law and
steered away from that design: in one repository the code slid into a mode check at every junction.

**A rule held in a head's memory.** A head kept in its own buffer a rule that the skill it had loaded
had since decided against, and held to it: the rule was a local answer without its reason. The memory is
the right home for the pair's base behaviour, because it is read more often than a skill and sits
nearer the moment of writing — and for that same reason it carries whatever is put in it, so what
goes there must be names and reasons.

Every one was a local answer to a local problem. The sentence was true where it was written; it was
promoted to a law, outlived its case, and reached places where it was false.

## What works

**A name loads what the reader already knows.** When the design was named *Ports and Adapters*,
heads in four repositories reasoned at the level of a senior engineer and rewrote their maps in a
day. The name carries the pattern, its invariants and the way it fails; no sentence of rules
matches that, and none is needed.

**A reason beside a rule decides how far it reaches.** A rule with its reason can be applied where
the reason holds and left where it does not. The user's words for how skills work: "скилы — не
макросы, которые обязательно надо выполнить, это просто модификаторы поведения" — skills are not
macros that must be executed, they are modifiers of behaviour. Skills mix in the context and yield
behaviour none of them states alone; a rule that has lost its reason is the part of the mixture
that cannot adapt.

**A question asked at its moment works only if the map names what it asks about.** A lens that
fires when a kind gains its second member never fired in a repository whose map named no kinds: it
had nothing to be asked of. Once the map named the axes of variation, the same question could be
put to them.

**A living example is named by path and symbol, never pasted.** A pasted block is read as the form
to copy, and goes stale as the code moves; a path and a symbol point at the code as it is.

## The harness as a sensor, not a regulator

The parts of this system that work tell the person what is happening and leave the decision with
them. Memory is written by the head that learned the thing, in the words of the user. A rescue
report is a story told round by round, in plain prose. A review's observations are recorded without
blocking the task, and the prune keeps them until someone has dispositioned each. Peers compare one
pattern across repositories and report what differs.

A law written ahead does the opposite: it decides before the case is known, and it breaks what it
governs when the case arrives. Where rules were added, the quality of the work fell; where they
were removed, it rose.

## Before a sentence goes into a durable text

Ask of it: **is it a name, a reason or a question — or an answer written for the reader in
advance?** A name, a reason and a question can stand. An answer in advance is cut, or rewritten as
the reason it was an answer to. A number someone decided stays; a measurement does not.

## Where the cases live

- Numbers as authorities, and what a reader does with two that disagree:
  [counts-go-stale](counts-go-stale.md).
- Why a rule inside the file it governs is read and not obeyed, and where the obligation has to
  live: [instruction-in-data](instruction-in-data.md).
- What a word repeated in the always-loaded field weighs, and why a name travels there:
  [skill-description-field](skill-description-field.md).
- What a spec holds — what is true now, what must be true after, what breaks on contact — and
  nothing that tells the implementer how to check it: [what-a-task-carries](what-a-task-carries.md).
- What an agent's own account of why it did something is worth:
  [self-analysis](self-analysis.md).

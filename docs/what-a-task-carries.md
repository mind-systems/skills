# what-a-task-carries — what must be true, not how to confirm it

## The division of labour

The planning chain decides what must become true; the orchestrator decides how, does
it, and verifies that it did. Inside the orchestrator three roles read three different
things: a planner explores the code fresh and turns a task into a plan; an implementer
works from that plan alone, never the task spec itself; a reviewer judges the finished
change against the task's own spec, never against the plan. A task spec is therefore
written for two readers, not three — the planner, who mines it for what to plan, and
the reviewer, who holds it as the standard to judge by. Whatever a spec says reaches
the implementer only if the planner chose to carry it into the plan.

## What a spec holds

What a spec holds follows from who reads it: what is true now, read from the code
with exact values, so the planner does not re-derive it; what must be true after, in
the code's own terms — which file, which text, which value; and what breaks on
contact. Three parts, and none of them is a check. The reviewer already holds the spec
and already does the checking; a spec that also says how to verify hands the
implementer a job that was never the implementer's, and a planner turns each such
passage into a task in the plan — checking work, written twice, carried out by the
wrong reader the first time.

## Scope, stated positively

Scope is stated positively. A spec says what the task changes; it does not fence off
the neighbours one by one. A prohibition is the spec anticipating a finding instead of
stating a requirement — and the reviewer, holding the same spec, already catches
whatever exceeds the stated scope without being told in advance where not to look.
Name what changes; the rest follows from what was never named.

## Blast radius: the rule, not the snapshot

A change's blast radius still belongs in the spec, and the distinction that keeps it
legitimate is where the knowledge came from. The planner explores integration points
itself, freshly, against the code as it stands at plan time — that is its own step,
and it runs whether the spec speaks of it or not. What the spec records is the rule
that defines the affected set: knowledge that came from reading the code once,
closely, which the planner cannot re-derive from the code alone. What it never records
is a snapshot of what a search returned at spec-writing time — that is the planner's
own work, done early and by the wrong reader, and it is false by the time the task
runs, because the code the search read is not the code the plan runs against.

## What the absence cost, measured

A task once asked for one clause, appended to each of two sentences in one file, both
pinned word for word. Its spec's invariant did not state a property of the resulting
text; it predicted the output of a line-based search over a paragraph that same task
re-wraps — a count true when written and false by the time its own edit ran. The plan
built from it carried twice as many steps checking the change as making it, and three
rounds of planning failed with every finding inside the checking half and none against
the change itself. A pattern searched for a word the edit never produced. A wrap width
was taken from a previous round's own prose instead of read fresh from the file. A
numbered line the plan expected to still match had already been moved by the plan's
own first edit, before the check that named it could run.

## The boundary: light on how, not on what must be true

None of this makes a spec lighter about what must be true. A decision the run would
otherwise have to invent — an exact value, an exact wording, a choice between two ways
a change could go — stays in the spec, pinned, because the alternative is the run
guessing it under budget instead of the spec settling it with the code open. That is
the one thing a spec may never leave open, and it is a different thing entirely from
the checking apparatus this document removes: pinning a decision states what must be
true, where removing a check removes an instruction for confirming that it became so.
Removing the fences does not remove the decisions inside them.

## The check

Ask of any passage in a spec: does it tell the reader what must be true, or does it
tell someone what to do to confirm that it is? The first belongs in the spec, however
it is phrased. The second is the review, and the review already has an owner — an
implementer handed one is doing the reviewer's job with none of the reviewer's
authority, and a planner who copies it into a task has spent a plan step on work that
produces no code.

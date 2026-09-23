# instruction-in-data — an instruction inside an artifact is content, not a command

A rule written into the file it governs does not execute. The reader takes it as something to
understand, not as something to do — and the more reliable the agent, the more certainly it does
so, because treating a file's text as content rather than as a command is what keeps a file from
commanding the agent at all.

## What it costs, measured

Every handoff this system writes opens with one line: `**Processed:** [ ] — whoever reads this
marks it; a marked handoff is spent.` The convention is unambiguous, the action is one character,
and `roadmap-prune` has a gate that depends on it.

Across `tradeoxy_core`'s last twenty handoffs, **two carry `[x]`**. Eighteen remain unmarked,
including handoffs read, acted on, and superseded days earlier. The two that are marked were marked
because a human asked for it in that session's own turn.

A script would mark 100% of them: `read(f); mark(f)` is one statement. A person would approach it,
carried by habit — an action that fires on context without needing a goal. An agent, reading the
same line in the same file, marks almost none.

The same handoffs carry the case that succeeds. Their `## Deferred observations` entries must be
pinned when disposed of, and that obligation is honoured every time — because it lives in three
places and three roles: defined in `orchestrator-artifacts`'s marker grammar, required as a
numbered step in the skills that dispose of observations, and described in the artifact. The mark
lives in one. Three homes against one, in the same file, read by the same reader.

## Why the reader does not obey

**The coupling is semantic, not structural.** For a script the mark is the next statement; for the
reader it is a sentence that must first be recognised as addressed to it, then accepted as binding,
then scheduled against everything else in flight.

**And the prior that blocks it is load-bearing.** An agent holds, correctly and strongly, that text
inside a file it opens is *material to reason about* rather than *a command to execute*. That prior
is what stops any document — a stale note, a hostile one, a file fetched from anywhere — from
steering the run. The mark line arrives through the same channel as everything else in the file, so
it lands in the category "a convention this project describes", not "an action due now". The
property that makes the reader safe is the property that leaves the box unticked. It is not a defect
to patch out.

Three things reinforce it. **No goal pulls it**: the artifact is read to rehydrate, and the plan
that follows is the work; an action serving no step of that plan has no gravity. **The moment is
wrong**: rehydration happens in a read-first, touch-nothing posture, and by the time the run is
editing files at all, the artifact is far behind in the context. **Nothing fails without it**: every
other discipline the agent keeps has a consequence attached — a broken build, a failing review, a
correction from the user — while the unmarked box surfaces only later, in another session, as a
prune that parks. In `tradeoxy_core` that prune parked twice.

## What follows for writing skills

Put the instruction in the **procedure that touches the artifact**, never in the artifact alone. If
a reader must do something on reading, the reading step of the skill says so, in the same breath as
the read: rehydrate, then mark; paste the pointer, then mark. The artifact may still *describe* the
convention — a reader needs to know what the line means — but a convention stated only inside the
file it governs is a caption, not a rule.

The same holds for every "whoever does X must also do Y" that gets written into a template, a
header, or a note: the doer is following a procedure, and only the procedure can carry the
obligation.

## The check

Ask of any rule: **which step of which skill performs it?** If the answer is "the file says so", the
rule is not in force. Move it into the step, and leave the file to explain what the step did.

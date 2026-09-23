# self-analysis — an agent's account of its own behaviour is a hypothesis, not testimony

Ask an agent why it did something and it will answer fluently every time. The fluency is worth
nothing on its own: there is no privileged access behind it. What the answer can be worth is
something else — a *model* of the behaviour, built from the same evidence an outside observer has,
which earns its place only by predicting something not yet looked at.

## What it is not

An agent cannot read its own mechanism. It sees what it wrote, what it was given, and what changed
on disk — the same surface anyone else sees. An explanation of "why I did that" is therefore
constructed after the fact, from the trace, in exactly the way an explanation of someone else's
behaviour would be. Treating it as a report from inside is the mistake; it is the outside view,
spoken in the first person.

This is why unqualified introspection is worse than none: it produces a confident cause for every
effect, and a confident wrong cause is more expensive than an open question.

## What makes an account usable

Two conditions, both checkable by the person asking.

**It must explain a measured discrepancy, not a single behaviour.** "Why do you do X" invites a
story. "X fires every time and Y never does — both arrive in the same file" forces a mechanism,
because any story must now account for the difference.

**It must predict something else.** An account that only explains what has already happened is
unfalsifiable and therefore worthless as evidence, however true it sounds. An account that says
*and therefore this other thing should also be true* can be checked against the corpus, and either
survives or dies there.

## The worked case

This system's handoffs open with a line asking whoever reads them to mark the file as spent. Across
`tradeoxy_core`'s last twenty handoffs, two are marked. The same handoffs also carry deferred
observations that must be pinned when disposed of — and that obligation is honoured every time.
Same file, same reader, opposite outcomes.

The account that came out of that contrast: an obligation written *only* into the artifact is read
as content, while an obligation that also lives in a loaded procedure is executed as a step — and
the pinning rule lives in three places and three roles (defined in `orchestrator-artifacts`'s
marker grammar, required as a numbered step in the skills that dispose of observations, and
described in the artifact), while the mark lives in one. Three homes against one; a hundred percent
against almost zero.

That account is usable because it predicts: give the mark a second and third home — a step in the
rehydration procedure, a line in the pointer that gets pasted forward — and compliance should move
to match the pins. Nothing about it depends on believing the agent's introspection; the prediction
is checkable in the next twenty handoffs. The structural claim it rests on is the subject of
[instruction-in-data](instruction-in-data.md).

## How to ask for it

Supply the contrast. The agent sits inside the loop and can notice its own asymmetries, but usually
only once someone hands it the case that should have behaved the same way and did not — that is the
part it is worst at finding alone, because the thing it did not do leaves no trace in what it wrote.

Then ask what else the account implies, and go look. An account that names a mechanism, points at
where the mechanism would show up elsewhere, and turns out to be right there too is evidence. One
that explains only the case in hand is a story, and should be held as one — including every account
in this document.

# architect-pairing-engine: cut the applying half's check back to a check

Task 26.5 was asked for one thing: the applying half reads an arriving
work-order and reports a problem back instead of applying it blindly. The
paragraph it shipped carries that, and three powers past it. Each of the
three has already cost something visible — one contradicts the paragraph
directly above it, one exists only to patch that contradiction, and one
left the pair's text asymmetric and is the deferred observation still open
against 26.5.

## Current state (grounded, read fresh)

`src/skills/architect-pairing-engine/SKILL.md:58-70`:

> "Applying exactly is not obeying blindly. Read the arriving work-order
> against the files before you touch them: where it is underspecified,
> contradicts itself, or would break something it never named, report that
> back instead of guessing your way through it; where it is outright
> wrong — a stale reference, a mismatched value, an unaccounted
> collision — correct it inside the change the work-order already asks for
> and say so explicitly rather than deviating silently; and name in your
> report every decision the work-order left unpinned. Correcting an order
> while executing it is not originating an edit of your own: it stays
> within what the work-order pins and it is never silent. That report
> closes the round back through the user, the path the work-order arrived
> by; the deciding half verifies what landed against the files, so an
> unflagged judgment call is the one thing its check cannot see."

The `description:` field's applying clause already states the check alone —
it reports back an order that is underspecified, self-contradicting, or
would break something it never named, instead of applying it in silence.
No correction licence, no round-closing. The field is already right; only
the body overshoots.

## What was asked, and what the paragraph adds past it

The requirement: the applying half reviews the work-order and reports a
problem back rather than applying it blindly. The paragraph's first
sentence, and the first clause of its second, carry exactly that.

Three additions stand past it:

- **A correction licence** (`:61-64`) — "where it is outright wrong …
  correct it inside the change the work-order already asks for". Reporting
  a defect was what was asked; repairing one is a power beyond it.
- **The reconciliation sentence** (`:65-67`) — "Correcting an order while
  executing it is not originating an edit of your own …". It exists only
  because the licence collides with `:52`'s "never to its own judgment".
  Remove the licence and it has nothing left to reconcile.
- **The round-closing clause** (`:67-68`) — "That report closes the round
  back through the user, the path the work-order arrived by". When a round
  closes is a different subject from whether an order is checked.

## Why each removal is safe

Removing the licence resolves the contradiction with `:52-53` rather than
needing a bridging clause: with no power to originate a repair, every
change the applying half makes traces to the arriving work-order again —
which is what the paragraph above it already says.

Removing the round-closing clause moots the deferred observation carried by
26.5's review rounds, that the applying half states a round-closing rule
its counterpart never states. With the clause gone there is no asymmetry,
and no later task is needed to write the deciding half's mirror.

The report needs no establishing clause of its own. The skill's opening
already states that every message between the pair crosses through the
user; a report travelling that path is the general rule applied, not a new
mechanism.

## The change

Replace `src/skills/architect-pairing-engine/SKILL.md:58-70` — the whole
paragraph, bounded by the blank lines at `:57` and `:71` — word-for-word
with:

```
Applying exactly is not obeying blindly. Read the arriving work-order
against the files before you touch them: where it is underspecified,
contradicts itself, or would break something it never named, report that
back instead of guessing your way through it, and name in your report every
decision the work-order left unpinned. The deciding half verifies what
landed against the files, so an unflagged judgment call is the one thing
its check cannot see.
```

Nothing else in the file changes.

## Files & types

- edit: `src/skills/architect-pairing-engine/SKILL.md` — the applying-half
  paragraph at `:58-70` only.

## Guards

- The `description:` field is untouched: its applying clause already
  carries the check alone and nothing past it.
- `## The deciding half`, the load-only-when-assigned rule, and both the
  originates-no-edit and supersession paragraphs of `## The applying half`
  are untouched.
- `src/agents/editor.md`, `src/skills/agent-architect/SKILL.md`, and
  `src/skills/architect-editor-engine/SKILL.md` are untouched. The
  correction discipline stays where it already lives — in the editor's own
  definition, for the editor. It is not restated here and not pointed at
  from here.
- No new channel-message format, no third mode, no round-closing rule.

## Verification

- Manual read: "## The applying half" holds three paragraphs — the
  originates-no-edit paragraph, the replacement paragraph, the supersession
  note — and the replacement is byte-identical to the pinned text above.
- `grep -c "correct it inside the change" src/skills/architect-pairing-engine/SKILL.md`
  → 0.
- `grep -c "Correcting an order while executing it" src/skills/architect-pairing-engine/SKILL.md`
  → 0.
- `grep -c "closes the round" src/skills/architect-pairing-engine/SKILL.md`
  → 0.
- `grep -c "Applying exactly is not obeying blindly" src/skills/architect-pairing-engine/SKILL.md`
  → 1.
- `git diff --stat` shows exactly one file under `src/` changed, and the
  `description:` block does not appear in that diff.

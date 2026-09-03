# architect-pairing-engine: the applying half checks the work-order before it applies

`src/skills/architect-pairing-engine/SKILL.md` § "The applying half" tells
the applying architect to apply what the arriving work-order pins "the way
an editor would". The check that phrase stands for is real and written
down — but written down in `src/agents/editor.md`, a file the applying
architect never loads. What it actually holds is one sentence that reads as
unconditional obedience.

## Current state (grounded, read fresh)

`src/skills/architect-pairing-engine/SKILL.md:50-54`:

> "It originates no edit of its own: every change it makes to a shared
> artifact traces to an arriving work-order, never to its own judgment. It
> applies exactly what that work-order pins, the way an editor would, and
> does not route it onward to an editor of its own — its hands are its own,
> not delegated a second time."

`src/agents/editor.md:79-83` — the discipline that phrase reaches for:

> "If a round is underspecified, contradicts itself, or would break
> something unintended, flag it back rather than guessing; if you catch it
> outright wrong (a stale reference, a mismatched value, an unaccounted
> collision), fix it and say so explicitly — never silently deviate and let
> the architect discover the difference later."

together with `:77-79`, which requires every decision the round did not pin
to be surfaced explicitly.

## The defect — the check is reachable only through a file its reader never loads

An architect assigned the applying role loads two files: `agent-architect`
and this skill. `editor.md` is an agent definition — the harness supplies it
when the `editor` subagent is spawned, and no architect ever reads it. So
"the way an editor would" points at a discipline the reader does not hold,
and the generic skill offers nothing to fall back on: it has no notion of an
architect *receiving* a work-order at all.

What survives in context is the literal sentence — apply exactly what the
work-order pins. That reads as unconditional obedience, and a contradictory
or underspecified order is then executed in silence. The deciding half's own
safeguard does not catch it: that half verifies what landed against the
files, which surfaces a wrong change but never surfaces that the applying
half saw the contradiction and proceeded anyway.

This is the same shape as the defects this phase already closed — an intent
the text holds and a mechanism it leaves to be inferred. An inference
survives neither a compact nor haste.

## The change

One paragraph added to `src/skills/architect-pairing-engine/SKILL.md`,
inserted between the two existing paragraphs of "## The applying half" —
after the originates-no-edit paragraph, before the "This half supersedes"
paragraph — word-for-word:

```
Applying exactly is not obeying blindly. Read the arriving work-order
against the files before you touch them: where it is underspecified,
contradicts itself, or would break something it never named, report that
back instead of guessing your way through it; where it is outright wrong —
a stale reference, a mismatched value, an unaccounted collision — fix it
and say so explicitly rather than deviating silently; and name in your
report every decision the work-order left unpinned. The deciding half
verifies what landed against the files, so an unflagged judgment call is
the one thing its check cannot see.
```

The `description:` field is amended in the same pass, so the always-loaded
field does not keep describing this half as applying alone: its applying
clause gains the report-back behavior.

## Files & types

- edit: `src/skills/architect-pairing-engine/SKILL.md` — one inserted
  paragraph in "## The applying half", plus the applying clause of the
  `description:` field.

## Guards

- "## The deciding half" is untouched, including its spawn-trigger
  departure.
- The load-only-when-assigned rule and the never-in-an-unpaired-session
  rule are untouched.
- `src/agents/editor.md` is untouched. This task does not restate the check
  there and does not point at it from the pairing skill — the pairing skill
  says it in its own words, because a pointer to an unloaded file is the
  defect being fixed.
- `src/skills/agent-architect/SKILL.md` and
  `src/skills/architect-editor-engine/SKILL.md` are untouched — no new
  channel-message format, no third mode, and the generic skill gains no
  notion of a receiving architect.
- The applying half still originates no edit of its own: reporting a defect
  back is not originating one, and nothing here licenses it to act on its
  own judgment.

## Verification

- Manual read: "## The applying half" holds three paragraphs in order —
  originates-no-edit, the new check paragraph, the supersession note.
- `grep -n "the way an editor would" src/skills/architect-pairing-engine/SKILL.md`
  → exactly one hit; the phrase is kept, not replaced.
- `grep -n "editor.md" src/skills/architect-pairing-engine/SKILL.md` → no
  hits; the fix adds no pointer to an unloaded file.
- The `description:` field stays under 1024 characters.
- `git diff --stat` shows exactly one file under `src/` changed.

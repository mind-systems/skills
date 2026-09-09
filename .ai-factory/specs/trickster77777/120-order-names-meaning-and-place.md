# An order names meaning and place, not the characters

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:156-159` instructs the apply work-order to "pin every value, path, and exact string it needs." That instruction is the textual source of the register `docs/paired-loop.md` § "What crosses the channel" (`:23`) argues against — not a bare habit with no home: "An order names what a sentence must say and where it goes. It does not compose the sentence: the text is written by whoever has the file open, because a writer looking at a passage does not restate what already stands beside it, and a head composing a replacement blind does exactly that."

The same section (`docs/paired-loop.md:29`) states the anchoring discipline this task leaves untouched: "Every address in what crosses is a name, never a position... Position addresses do not survive an edit above them, and two sessions editing one file collide on positions and not on names."

## The change

An order names what a sentence must say and where it goes; the text itself is written by whoever has the file open. State the reason as non-stylistic: a writer looking at the passage does not restate what already stands beside it, and composing a replacement blind is exactly how that restatement happens.

The boundary this task must hold: a value is still pinned — a path, a number, a literal that must appear verbatim, an anchor a match is asserted against are the thing itself, not a description of it, and stay pinned exactly as before. What stops is composing prose for a file the order's author does not have open. Write the section so a reader cannot take it as license to pin nothing.

## Blast radius

The anchoring mechanism does not change: a match is still asserted against a unique string rather than a position, which is what lets two sessions edit one file without collision (`docs/paired-loop.md:29`).

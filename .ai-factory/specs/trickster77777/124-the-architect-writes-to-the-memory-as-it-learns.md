# The architect writes to the memory as it learns

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` carries one section naming what the architect records in its own buffer: "the editor's handle, any pairing role the user has assigned for the session, and the deferral entries below." Two of the three get an occasion, both narrow and specific: the editor's handle is written "At the moment you spawn the editor (see above), write its handle into the buffer"; a pairing role is written "at the moment the user assigns it — which may be mid-session and need not coincide with the spawn." A deferral entry's own format is stated — "Each deferral entry names *what*, *why deferred*, and the *trigger* that resolves it" — but nothing says when one is created, only that it is deleted once done.

`docs/paired-loop.md` § "What the memory holds, and who holds it" describes the settled zone's content as "the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice." After 36.1 this is what the engine both halves load states the memory holds. Nothing in `agent-architect` — not at spawn, not at pairing-role assignment, not anywhere else — instructs the architect to write any of it: the hand is given a zone to hold that the head has no instruction to fill.

The same governing section states the occasion and the form: "The head writes to the memory at the moment it learns something a later beginning would otherwise pay for again, not at the end of the stretch of work that produced it — the stretch of work is exactly what does not survive, and a conclusion left in the conversation dies with it, so the next beginning repeats the correction that made it." And: "An entry is written as what will hold again — a ruling of the user's in the user's own words, a mistake as the pattern behind it and the reason that pattern holds — never as the episode that revealed either."

`docs/paired-loop.md` also states the hand's own side of a change, in the same section: "The editor re-reads the settled zone when it changes, not once at birth". Nothing in `agent-architect` tells the architect to announce that a change has happened — the file says nothing about the hand learning of a change at all; who, if anyone, tells it is unstated.

## The change

`agent-architect` gains, in the section naming what the architect records, the occasion and the form the governing spec states: when to write, and what shape a written entry takes. It names no zone — the engine characterises both after 36.1, and this task is the entry side only — and it enumerates nothing new to record: the governing spec deliberately states this as a form, not a list, and the settled-zone paragraph already names the kinds of thing that qualify. The section states what the skill must carry; the wording is the implementer's to write.

The same section also gains the announce-obligation the governing spec's amended paragraph closes on: the architect names it to the hand when the settled memory moves. This is not a second thing added beside the occasion and the form — it is the same obligation seen from both ends, the memory kept current and the hand told it moved, and it lands in the same place because writing to the memory and telling the hand it changed are one act, not two.

## Blast radius

This task lands after 36.1: the section it edits is the one 36.1 cuts one sentence from — the path-and-numbering sentence, replaced by a pointer naming the engine as the buffer's home — and narrows a second — the "editor is never told about it..." sentence, dropping two of its three clauses and giving the third a new reason. That pointer restates nothing the engine holds, which is what this task's own zone-silence follows: the recording-list sentence and the deferral-entry-format sentence this task grounds itself on are neither cut nor narrowed, and 36.1 leaves them in place, un-zoned — consistent with this task's own occasion-and-form addition naming no zone either.

This task does not restate the drain rule; that rule moves into the engine with 36.1 and stays there.

Nothing else in the file cross-references this section by position or by count that this addition would disturb — checked directly.

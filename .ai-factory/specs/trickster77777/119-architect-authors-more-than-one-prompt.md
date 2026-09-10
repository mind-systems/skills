# The architect authors more than one kind of prompt, and the skill says so

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` states the same misdescription in three places. The section heading reads "## Relay on the marker; author a prompt in exactly one case". Its body reads "You author your own prompt in exactly one case: the **apply work-order**, once the user has confirmed the edits." And, later in the same section, a third sentence generalizes both into a closed inventory: "Two channel-message formats, nothing else: the `REPORT-ONLY` relay carries the before-mark payload, worked in parallel and enriched only with named context; the `APPLY-EDIT` channel carries the apply work-order alone, and it **never** carries your own analysis of an analysis target."

All three are false in the same way, from two angles. The heading and body ignore a second authored case the file's own text already needs — a `REPORT-ONLY` round the architect authors on its own initiative, delegating its own legwork, carrying no relayed user payload and asking for no edit. The third sentence goes further: read plainly, it claims the two forms are the whole of what the architect may ever send the editor.

`docs/paired-loop.md` § "What crosses the channel" now states the boundary the third sentence misses: "An order and a relay govern what opens a round — a unit of work sent out and reported back on — not an inventory of everything the head may ever say to its hand. Keeping the hand current is not a round: naming that the shared memory has moved, or handing the hand what it needs in order to work at all, is ordinary communication between a head and its own hand, and needs no form, no permission, and no carve-out to travel."

`docs/paired-loop.md` § "The user's marker" already draws the narrower distinction this task's first half needs: "The marker governs whose words cross the channel; it has nothing to do with the head delegating its own legwork, which needs no permission."

## The change

The heading and the body sentence both name both authored cases: the apply work-order, and a `REPORT-ONLY` round the architect authors on its own initiative to delegate its own legwork, carrying no relayed user payload.

Widening that sentence to name two authored cases leaves the pronoun opening the next sentence without a single candidate — the pronoun resolved only because one thing was named. That next sentence — "Send it as an `APPLY-EDIT` channel-message: pin every value, path, and exact string it needs; state the guardrails — what NOT to touch, a collision-safe method where order matters; and an explicit **"do not commit."**" — names the apply work-order explicitly in place of the pronoun, rather than carrying it forward into a sentence that now has two candidates to resolve against.

The third sentence is rescoped rather than dropped: it states what the two forms actually govern — what opens a round, a unit of work sent out and reported back on — not everything the architect may ever send. An ordinary act of keeping the hand current, per the governing spec, is not a round and needs no form of its own; the sentence says so instead of implying the two forms exhaust the architect's communication.

The marker's own rule is untouched: a marker on the user's message still forwards that message for an independent reading, and an unmarked user message is still never forwarded. What is added is narrow — delegating the architect's own work needs no marker and no permission, exactly as `docs/paired-loop.md` § "The user's marker" already states.

## Blast radius

Checked, not assumed, whether 36.1 already reaches any of these three sites: it does not. 36.1's edits to `agent-architect` land in § "Your buffer is yours alone" and the handoff parenthetical in § "Spawn once, message thereafter" — neither the heading, the body sentence, nor the two-forms sentence in § "Relay on the marker; author a prompt in exactly one case" is named or touched anywhere in spec 116. The one adjacent change is in a different file entirely: spec 116 has `architect-editor-engine`'s own `description:` and body "stop claiming it holds only the two channel-message formats" — but that is a claim about what content the engine file itself holds, not about what the architect may ever send; the two claims read alike but say different things, and `agent-architect`'s "nothing else" sentence is untouched by that change. No ordering dependency exists between this task and 36.1.

This task and 37.2 edit adjacent sentences of the same paragraph in § "Relay on the marker; author a prompt in exactly one case," 37.2's landing sentence sitting immediately after the sentence this task disambiguates. This task lands first, per the roadmap's own order, so the sentence it disambiguates above is exactly 37.2's own landing sentence.

`architect-editor-engine` already holds both message formats and needs no change from this task either: naming a second authored case, and rescoping what "nothing else" governs, does not add a third format, and the mode rule keys off the opening token either way.

# The rule that no architect reads another's buffer gets a home

## Current state (grounded, read fresh)

`src/skills/architect-editor-engine/SKILL.md` holds, today, only the two channel-message formats: its own `description:` field states "Holds only the two formats; when-to-use policy stays with the caller," and its load instruction reads "Load this skill once at birth — the architect per the instruction in its own body, the editor as the first action on spawn — so the contract is resident before any channel-message arrives." Both halves load it unconditionally, at birth, before either has anything else to do.

`src/skills/architect-pairing-engine/SKILL.md` cannot carry a rule that must always apply, because its own load condition is conditional: "Load only when the user has assigned it one of these two roles for the session; never in an unpaired session." An architect working without a declared pairing role never loads this file at all.

`docs/paired-loop.md` states the rule with no such condition: "Two architects are two heads. No architect reads another's buffer, and an editor reads only its own architect's." The rule binds whenever more than one architect exists, not only when a pairing role has been assigned. No other artifact states it.

## The change

The sentence lands in `architect-editor-engine`, beside the buffer's definition 36.1 puts there: it carries both of the rule's clauses — that an architect's buffer is its own, and that an editor reads only the memory of the head it is the hand of — because both bind unconditionally, the same way the engine itself now loads. The engine both halves load at birth is the rule's home for the same reason it is the buffer's: neither is true only sometimes, so neither belongs to a file that is present only sometimes.

## Blast radius

36.1 puts the buffer's definition into `architect-editor-engine`; this task states the isolation rule beside that definition, so 36.1 must already be on disk before this task lands.

`architect-pairing-engine` is untouched by this phase — the task previously named it as the rule's destination; it no longer is, and nothing else in this phase edits that file.

Checked spec 116 for a fence against carrying the two-architect sentence into the engine: none exists. Spec 116 does not mention the two-architect rule, `architect-pairing-engine`, or this task anywhere in its current text — the fence a prior plan carried was in the plan, which is deleted, not in the spec that survives it.

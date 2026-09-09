# The architect authors more than one kind of prompt, and the skill says so

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` states the claim twice: in the section heading "## Relay on the marker; author a prompt in exactly one case", and again in the body — "You author your own prompt in exactly one case: the **apply work-order**, once the user has confirmed the edits."

It is false in practice. The same skill's own § "Verify the report by fact" and the general pattern of a `REPORT-ONLY` round with no relayed user payload behind it — an investigation the architect initiates on its own reading, asking for no edit — is a second case the file never names: the marker section describes only two things crossing the channel, a before-mark relay of the user's payload and the apply work-order, with nothing for a self-initiated research batch that is neither.

`docs/paired-loop.md` § "The user's marker" already draws the distinction this task needs: "The marker governs whose words cross the channel; it has nothing to do with the head delegating its own legwork, which needs no permission."

## The change

The heading and the body sentence both name both cases: the apply work-order, and a `REPORT-ONLY` round the architect authors on its own initiative to delegate its own legwork, carrying no relayed user payload.

The marker's own rule is untouched: a marker on the user's message still forwards that message for an independent reading, and an unmarked user message is still never forwarded. What is added is narrow — delegating the architect's own work needs no marker and no permission, exactly as `docs/paired-loop.md` § "The user's marker" already states.

## Blast radius

`architect-editor-engine` already holds both message formats and needs no change: naming a second reason to send `REPORT-ONLY` does not add a third format, and the mode rule keys off the opening token either way.

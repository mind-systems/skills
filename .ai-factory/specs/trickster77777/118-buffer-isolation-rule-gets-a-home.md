# The rule that no architect reads another's buffer gets a home

## Current state (grounded, read fresh)

`src/skills/architect-pairing-engine/SKILL.md` governs exactly the scenario where two architects and their buffers coexist — § "The deciding half" and § "The applying half" state in detail how each half's editor and work-orders differ from the generic discipline — but the word "buffer" does not occur anywhere in the file, confirmed by a direct read of its full text.

`docs/paired-loop.md` states the rule this leaves homeless: "Two architects are two heads. No architect reads another's buffer, and an editor reads only its own architect's." Neither `agent-architect` nor `architect-editor-engine` states it either — it exists only in the governing spec, with no mechanism doc carrying it.

## The change

`architect-pairing-engine` states the rule directly, alongside its existing departures for the deciding and applying halves: no architect reads another's buffer, and an editor reads only its own architect's.

## Blast radius

`architect-pairing-engine`'s own `description:` field already scopes its load to an assigned pairing role — "Load only when the user has assigned it one of these two roles for the session; never in an unpaired session" — so an unpaired session, which never loads this file, is untouched by the addition.

No other artifact states this rule today, so nothing else has to move with it.

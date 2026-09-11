# The engine states that upkeep rides inside a message already going

## Current state (grounded, read fresh)

`src/skills/architect-editor-engine/SKILL.md` § "The mode rule" states: "A receiver keys its mode strictly off the token that opens the message — never off content, never off a referenced skill's own default. Ambiguity resolves to `REPORT-ONLY`." Nothing in the engine's text says anything about keeping a hand current — the engine holds only the two channel-message formats, the rule for telling them apart, and the buffer's own definition.

`docs/paired-loop.md` § "What crosses the channel" states the mechanism in one paragraph, in two parts, back to back. The permission: keeping the hand current "needs no form, no permission, and no carve-out to travel: it rides inside whatever message the head is already sending, never as one of its own, taking that message's form because it needs none — which is also why the rule for an unrecognised opening never reaches it." The bound, in the same paragraph, the very next sentence: "The relay's own protection is untouched: what crosses it still reaches the hand for an independent reading, undisturbed by anything else, because what that protection guards is the second reading itself — and a fact about where the shared memory sits carries no reading of it at all."

The engine is what both halves load at birth, unconditionally, in every project; the governing spec is not loaded at all in a project without our `docs/` — it is this repository's own account of the mechanism, resident nowhere else. A reader of the engine alone has neither half of that paragraph: not the permission, and not the bound that keeps the permission from reading as license to append anything to a relayed payload — exactly what the enrichment ban in `agent-architect` exists to stop.

§ "The architect's buffer" states the mechanism upkeep actually rides on: "The editor re-reads the settled zone when it changes, not once at birth." Task 40.2 widens this same sentence to cover the editor being named a different buffer's path outright, not only its own buffer's content changing in place. The section around that sentence is already bounded to the buffer's own facts; § "The mode rule" has no such bound of its own to lean on.

## The change

Two sites, in a stated order. 40.2 lands first: it widens § "The architect's buffer"'s re-read rule as its own task already specifies. 40.4 lands after it, anchoring beside what 40.2 left — the same section, once 40.2's widening is in place, gains a short statement of what may ride alongside a channel-message without opening one of its own: a fact about where the shared memory sits, or what the hand needs in order to work at all — and, in the same breath, the bound — never a reading of the payload, never a finding, a conclusion, or a verdict about it. The statement is worded in the engine's own register, short, grounded in the permission-and-bound pair quoted above without restating the buffer's own definition, the re-read rule's own wording, or the architect-side enrichment ban's own mechanics — the engine states the limit, not the argument behind it, which stays in `docs/paired-loop.md`, one home per fact.

§ "The mode rule" keeps only its own limit: the ambiguity rule — "Ambiguity resolves to `REPORT-ONLY`" — never reaches upkeep, because upkeep never opens a message of its own; it rides inside one that already carries its own token. This sentence stays beside the rule it explains the limit of and carries none of the substantive statement now living in the buffer section — a pointer to where the fact lives, not a second copy of it.

Nothing about the two channel-message formats changes, and no third format is named: this states a boundary on what triggers the mode rule, not a new thing the mode rule must classify.

## Blast radius

`agent-architect` is not edited by this task: the sentence being added states a fact already true of how the architect sends things, not a new obligation on the architect's own side. `editor.md` is not edited either — the receiving side's behavior (key off the opening token, ambiguity resolves to `REPORT-ONLY`) does not change; what changes is that a reader now has, in the engine itself, both the fact and the bound that keeps a formless notice from ever reaching that fallback or from being read as license to carry more than it does.

No new `loads:` edge, no new section at either site: the mode-rule sentence lands inside the existing "## The mode rule" section, and the buffer-section statement lands inside the existing "## The architect's buffer" section, beside 40.2's own edit — after it, not before, so the statement has the widened re-read rule already in place to anchor beside rather than an edit still pending on the same section.

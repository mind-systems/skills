# `editor.md` drops the false equation between REPORT-ONLY and a relay

## Current state (grounded, read fresh)

`src/agents/editor.md` opens: "Each round is either a `REPORT-ONLY` channel-message (a relayed analysis target — the architect forwarding the user's own payload, worked independently) or an `APPLY-EDIT` channel-message (a decided apply work-order — the architect's own, pinned instruction)." The parenthetical equates a `REPORT-ONLY` round with a relay: the architect forwarding the user's own payload. § "Analysis mode: reason independently" opens with a separate, narrower claim beside it: "A relayed message — a review, decompose, judge, hazard-hunt — carries no architect framing: no findings, no checklist, no verdict for you to confirm."

`src/skills/agent-architect/SKILL.md` names a second case the format now covers: "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits, and a `REPORT-ONLY` round on your own initiative, delegating your own legwork — a message you compose yourself, carrying no relayed user payload and asking for no edit, opening with the literal `REPORT-ONLY` token like every message of that format." This round is authored by the architect and forwards no user payload at all — the opposite of what `editor.md`'s round-type description equates a `REPORT-ONLY` round with.

The equation is what stopped being true, not the property beside it. `editor.md`'s own "carries no architect framing: no findings, no checklist, no verdict for you to confirm" makes no claim about origin, and `architect-editor-engine` agrees from the sending side, defining the format itself as "a research relay: the receiver reads or runs the target, reasons independently, reports by fact, writes no files" — neither sentence ties "reasons independently" to a relayed origin, and both hold for a self-authored round exactly as they do for a relayed one. Treating "relayed" as a defining property of the format belongs only to `editor.md`'s own round-type description: `agent-architect` names a round that forwards no user payload at all, and nothing in the engine or the governing spec ties the format to an origin. That clause is the defect.

## The change

`editor.md`'s round-type description drops the equation: a `REPORT-ONLY` channel-message is an analysis target, worked independently — its origin, relayed from the user or delegated by the architect on its own initiative, left unstated because nothing downstream depends on it. What survives from the original clause: "worked independently," and the contrast with `APPLY-EDIT`'s "a decided apply work-order — the architect's own, pinned instruction," both untouched.

§ "Analysis mode: reason independently" keeps its no-framing sentence exactly as written — "A relayed message — a review, decompose, judge, hazard-hunt — carries no architect framing: no findings, no checklist, no verdict for you to confirm" — true of a round from either origin, and this task does not touch it.

The phrase past that sentence changes: "Reason over the target yourself, from the ground up, exactly as if the user handed it to you directly" is written for the relayed case specifically, and is literally untrue of a delegated round, where the user handed over nothing at all. Its intent — full independence, no deference to the architect's own authority in sending it — holds for both origins; the wording carries that intent without tying it to a user handing anything over, so it reads true regardless of which kind sent it.

This task states no difference in what the editor does by origin, because there is none to state: the editor's conduct in Analysis mode is identical whether the target was relayed or self-authored, and the rewrite adds no marker, no branch, no distinction for the editor to act on. The whole difference between the two origins is how the architect weighs what comes back — signal from a relay, an echo from a delegated round — which is `docs/paired-loop.md`'s own rule, carried into the skill by 40.5, not a fact about how the editor works.

## Blast radius

`agent-architect` and `docs/paired-loop.md` are not touched. `architect-editor-engine` is not touched either — its "research relay... reasons independently" line is cited above as grounding only, the same way other tasks in this phase cite `docs/paired-loop.md` without editing it. The asymmetry this task closes is entirely `editor.md`'s own account lagging a change already landed in `agent-architect`; nothing on the sending side needs to change for the receiving side to stop asserting the equation.

§ "Apply mode: apply exactly, add no scope" and the rest of `editor.md` are untouched — this task's sites are the round-type description and the origin-specific phrase in the analysis-mode section immediately below it; the no-framing sentence between them is quoted here as grounding and is not touched.

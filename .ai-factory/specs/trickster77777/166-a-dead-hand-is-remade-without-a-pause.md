# Phase 60 — a dead hand is remade, not asked about

Governing spec: `docs/paired-loop.md`

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" states the dead-hand case in full:

> If the send fails, the editor is dead: report to the user **before anything
> is sent onward**; an undelivered payload is never auto-replayed into a fresh
> spawn, because the user phrased it for a warm context. The respawn is the
> next channel-message after that report, never eager with authored prose: the
> user re-phrases a relay as a self-contained spawn prompt, an apply
> work-order is resent as-is, or a `REPORT-ONLY` round delegating your own
> legwork is resent the same way. A respawned editor resumes through the same two
> channels, self-contained per round. Losing the editor is never fatal; losing
> it silently is the defect.

Three clauses in that passage turn a dead hand into a stop: report *before anything is sent onward*, an undelivered payload *never auto-replayed*, and the respawn waiting on the user to *re-phrase a relay or resend a work-order*. The user's own ruling overrules exactly these three, in his own words: «Редактор — твоя рука, не жди моего приказа трогать его! Пользуйся им! Умер — делай нового всегда!» The hand is the head's own; the architect never pauses to ask whether to spawn or re-spawn one, a hand's death is reported in passing rather than as a question, and the next channel-message *is* the new spawn. This is standing permission, not a per-death grant — the passage's own framing of the respawn as something that waits on the user is what the ruling removes, not the reporting itself: a death still gets named, in passing, in the same act as the next spawn, never withheld and never asked about first.

What survives the ruling is the reason the passage gave for pausing, even though pausing is no longer what that reason buys: a fresh hand holds none of the accumulated round history a live one had, so an undelivered payload cannot simply be replayed into it unchanged — it was phrased for a hand that already knew the session's ground, and the new one does not. That cost does not disappear when the wait does; it moves onto the next order. The architect that respawns still owns making the next channel-message self-contained — pinning the values, paths, and anchors a warmed-up hand would have carried in its own accumulated context — exactly as a fresh spawn already must per "Spawn once, message thereafter"'s own account of a respawn (`"A respawned editor resumes through the same two channels, self-contained per round"`). The ruling removes the wait; it does not touch this requirement, which was never about permission in the first place.

`src/agents/editor.md` carries no matching stop on its own side, checked directly: no mention of "dead," no report-before-anything-else language, no language holding a round open pending the user's word. This is expected rather than a gap — the stop the ruling removes lives entirely in the decision to *wait after* a send fails, which is the architect's own call to make, never the editor's; a dead hand cannot itself report anything, and `editor.md`'s two-mode contract has nothing to say about what happens after it can no longer answer.

Nothing under `docs/` is written.

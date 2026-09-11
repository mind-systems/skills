# Plan: 40.6 — more sites still treat relay-and-work-order as exhaustive

## Context
`src/skills/agent-architect/SKILL.md` still states, in three places 37.1 never touched, that a relay and an apply work-order are the whole of what the architect sends: the spawn sentence and the respawn sentence in § "Spawn once, message thereafter", and the closing sentence of § "Review in parallel, reconcile before the apply order". This task widens the first two to cover the architect's own delegated `REPORT-ONLY` round and narrows the third to say only what the marker actually decides. One file, three sentences, nothing else.

Grounding read fresh (per spec `.ai-factory/specs/trickster77777/133-...` and governing spec `docs/paired-loop.md` § "The user's marker"):
- The file names the delegated case in exactly one construction, in § "Relay on the marker; author the apply work-order and your own legwork": "a `REPORT-ONLY` round on your own initiative, delegating your own legwork — a message you compose yourself, carrying no relayed user payload and asking for no edit". There is no noun for that round; the task must not invent one.
- That same paragraph already holds the rule the third site needs ("That second case needs no marker and no permission: the marker governs whose words cross the channel, not you delegating your own work"). The third site neither restates nor points at it.
- No other site in the file states the pair as exhaustive (checked: the only "relay or … apply" shapes are the two sentences named here; the "nothing else" claim is already gone).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Widen the two spawn-path sentences

- [x] **Widen the spawn sentence to name the delegated round as a possible first channel-message**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the sentence beginning "The first channel-message is the spawn — the first `::` relay or, where none has arrived, the first authored apply work-order — and its content *is* the spawn prompt, …". Widen the em-dash parenthetical so it names three possibilities, whichever arrives first: the first `::` relay, the first authored apply work-order, or a `REPORT-ONLY` round of your own initiative delegating your own legwork — using the file's own construction "delegating your own legwork" (as it stands in § "Relay on the marker; author the apply work-order and your own legwork"), never a coined noun such as "delegated round" or "delegation". Keep the phrase "where none has arrived" doing its current work (no relay yet), keep "whichever … first" logic explicit so the sentence does not read as an ordered preference. Everything after "and its content *is* the spawn prompt" — the buffer-path pointer clause, the enrichment reference, "there is no spawn before one exists", the `Agent`/`SendMessage` sentences — stays byte-identical. Do not touch the preceding memory-snapshot paragraph (40.7 edits "Each new snapshot supersedes the last by name" there).

- [x] **Widen the respawn sentence the same way**
  Files: `src/skills/agent-architect/SKILL.md`
  Same section, the dead-editor paragraph: "The respawn is the next channel-message after that report, never eager with authored prose: the user re-phrases a relay as a self-contained spawn prompt, or an apply work-order is resent as-is." Add a third branch beside the two: the architect re-authors its own legwork-delegating `REPORT-ONLY` round, resent the same way an apply work-order is — again in the "delegating your own legwork" construction, no new noun. The clauses "never eager with authored prose" and "an undelivered payload is never auto-replayed into a fresh spawn, because the user phrased it for a warm context" stay as written: they still hold, since a relay is the user's words and is not auto-replayed, while the architect's own composed prompt is its own to resend. The sentences after it ("A respawned editor resumes through the same two channels, self-contained per round. Losing the editor is never fatal; losing it silently is the defect.") stay byte-identical. Do not touch the fallback-recovery paragraphs above it (40.2's territory: liveness probe, re-pointing rationale).

### Narrow the marker-decides sentence

- [x] **Narrow "You never decide *when* something goes to the editor; the marker does" to relays only** (depends on nothing; independent of the two above)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Review in parallel, reconcile before the apply order", the closing sentence "You never decide *when* something goes to the editor; the marker does." Rewrite it so it claims only what is true of the marker: the marker decides when a relay goes to the editor (i.e. you never decide when a *relay* goes; the marker does). Add nothing beside it — no mention of the delegated case, no "except when delegating your own legwork", and no pointer/cross-reference to § "Relay on the marker; author the apply work-order and your own legwork" — the spec is explicit that this site's repair is dropping the overreach, not restating or pointing at the rule already standing there. The preceding sentence about the apply work-order ("Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go.") is untouched: the apply work-order's timing rule (the user's confirmation) is not this task's.

### Guard

- [x] **Confirm the edit boundary held** (depends on all three above)
  Files: `src/skills/agent-architect/SKILL.md`
  Run `git diff` on the file and confirm: exactly three hunks, each on its own sentence; no coined noun for the delegated round anywhere in the diff (grep the added lines for "delegated round", "delegation round", "delegated legwork round" — none should appear; the construction is "delegating your own legwork"); the case-naming paragraph in § "Relay on the marker…" (including the echo sentences 40.5 added) is byte-identical; `src/agents/editor.md` and `src/skills/architect-editor-engine/` are untouched; the file's body stays ≤ 500 lines; the frontmatter is unchanged.

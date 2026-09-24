# 167 — a dead hand stops being a stop

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" reads, in full, the passage that governs a dead editor:

> If the send fails, the editor is dead: report to the user **before anything
> is sent onward**; an undelivered payload is never auto-replayed into a fresh
> spawn, because the user phrased it for a warm context. The respawn is the
> next channel-message after that report, never eager with authored prose: the
> user re-phrases a relay as a self-contained spawn prompt, an apply
> work-order is resent as-is, or a `REPORT-ONLY` round delegating your own
> legwork is resent the same way. A respawned editor resumes through the same two
> channels, self-contained per round. Losing the editor is never fatal; losing
> it silently is the defect.

Three clauses hold a dead hand as a stop: report *before anything is sent onward*, a payload *never auto-replayed*, and the respawn waiting on the user to *re-phrase a relay or resend a work-order*. The user's ruling — «Редактор — твоя рука, не жди моего приказа трогать его! Пользуйся им! Умер — делай нового всегда!» — overrules exactly these three; `docs/paired-loop.md` § "How the memory begins, and how it survives" now states the survived reason: "What a fresh hand costs is context, not permission: it holds none of the rounds already run, so what it is handed carries its own ground."

## What must be true after

The passage above is replaced with:

> If the send fails, the editor is dead: this is never a stop and never a
> question — the hand is your own, and permission to make a new one is
> standing, not asked for. Name the death in passing, in the same act as
> the next channel-message, which is the new spawn: never withheld, never
> delayed waiting on the user's word. What a fresh hand costs is context,
> not permission — it holds none of the accumulated round history a live
> one had, so the next order you compose **must be** self-contained in its
> own right: pin the values, paths, and anchors a warmed-up hand would
> have carried, the same way a first spawn already must. Losing the
> editor is never fatal; losing it silently is the defect.

The bolded `must be` is the one departure from a plain transcription of the reason: read as "is self-contained" the sentence only describes a fact about the reason, and a reason stated without being turned into an instruction is decoration, not a requirement on what the architect sends — the same failure this ruling is itself the repair for, one level up. `must be` is what turns "pin the values, paths, and anchors" into an obligation on every order that follows a respawn, not merely an observation about one.

`src/agents/editor.md` is not touched — checked directly (phase note `166-`) and confirmed to carry no matching stop on its own side: no mention of "dead," no report-before-anything-else language, no language holding a round open pending the user's word. The stop the ruling removes lived entirely in the architect's own decision to wait after a send fails, never in the editor's two-mode contract.

## What breaks on contact

**Rule:** any file that quotes this passage's current exact wording as ground truth for its own argument reads stale once the wording changes, except this task's own spec (records it as history), the roadmap's own contract line for this task (states the problem it describes, permanently), this phase's own note (`166-…`, which documents a moment, not a standing claim about the present), and an architect's own buffer, which this task never touches.

**Sweep (re-runnable, using line-wrap-safe substrings — the phrases as originally quoted wrap a line inside the actual file, so a naive single-line search for them silently returns nothing):**
```
grep -rln "sent onward\|auto-replayed\|editor is never fatal" src/ docs/ .ai-factory/
```

**Invariant:** after the change, `agent-architect/SKILL.md`'s dead-editor passage reads the new wording given in `## What must be true after`. The same file's earlier "Leaving both buffers live" paragraph still quotes "Losing the editor is never fatal; losing it silently is the defect" — the one clause this task carries forward verbatim — so that paragraph's own argument stays accurate against the file's current text. This task's own spec, this phase's own note `166-…`, and the roadmap's own contract line for this task all quote the old wording permanently as the problem they describe or the history they record; `.ai-factory/notes/01-architect-buffer.md` — a different architect's own buffer — is out of this task's scope and untouched, per the standing rule that no architect reads or edits another's buffer.

The target itself carries the phrase in more than one place, each checked: the passage being replaced, and the separate "Leaving both buffers live" occurrence above. This corrects an earlier version of this section, which searched for the un-wrapped phrases directly, found only the target's own passage as a result of the search silently missing the wrapped second occurrence, and did not check whether that occurrence's argument survives the change. The sweep locates candidates; reading decides.

The rest of the section — the liveness probe, the recovery path through the `meta.json` fallback, and the re-pointing procedure for a handle recovered with no buffer pointer — makes no reference to the wait this task removes: each defers to "the rule below for a dead editor" generically, without restating or depending on its content, so the reference stays correct whatever that rule says. The "Relay on the marker" section that follows makes no reference to this passage at all.

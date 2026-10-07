# Memory snapshot — the folder, the team, and the review of phase 77

*Architect 05, written 2026-10-07 at the user's word «делай снапшот, продолжим после компакта». Supersedes snapshot 12, whose next action is long stale; its record stays.*

Rebuild from `buffer.md` beside this file first — it is the memory; this is the residue of the stretch that wrote it, and the reasoning behind it.

## Where the work stands

**This head holds no open work of its own.** Nothing of mine is queued on any roadmap; the phase 77 review is done and its verdict is 07's to carry. The next thing that reaches me will come from the user or from 07.

**The migration into this folder is committed.** The user ordered it on 2026-10-01 — «мигрируй и буфер актуализируй» — and it went into `7b375e1` ("Roadmap update", the user's own commit). The only change of mine in the tree since is `buffer.md`, uncommitted: the `## Team` section, the rulings and method taken from 07's messages, the hook (d) candidate, and the current thread. The orchestrator's commit takes the whole tree, so if a run starts in this repository before the user commits, my buffer lands inside a task's commit — harmless in content, wrong in place. Say so if a run is mentioned.

**Phase 77 stood, at the moment of writing, with 77.2 done and 77.3–77.8 open** — but that is a reading of the tree, so read the seam, not this line.

**No editor is live.** None was spawned in this stretch; every round was my own reading or a message to 07. The buffer's Orientation names the two old handles and the rule that whichever hand receives the next channel-message is told the buffer's path in it.

## What happened, and why each call went the way it did

**The migration.** Only snapshot 12 moved with the buffer. Handoffs 09, 10, 11, 13 also name the old buffer path, and 18 was written by a continuation of this head, but the user's own rule was "the memory snapshots you wrote — the files under `.ai-factory/handoffs/` that name your buffer". 09, 10 and 13 were written by other heads and mention the buffer from outside; 11 is mine but a project handoff for a reviewer, a different genre (`docs/paired-loop.md` draws the line by reader and lifetime); 18 does not name the buffer and is a project handoff with a processed-mark. I chose the narrow reading on purpose: moving a handoff into a head's folder hides it from the next reader of the project, which is its whole purpose.

**The buffer was rewritten whole, not appended.** The old file was 865 lines of round-by-round log written by two heads under one number — the founding session and a later continuation that ran as the applying half. The seed's shape is what the hand reads in full, and a hand handed 865 lines of drained and stale history reads past what matters. The log is not lost: `git show 96ffb4c:.ai-factory/notes/05-architect-buffer.md`, and the buffer's Orientation says so. The pairing roles in that log are dead: `architect-pairing-engine` no longer exists, and peers talk without roles.

**Ledger entries go by bold lead-in, not number.** When 07 closed two threads by number, renumbering would have shifted the ones it still referred to; addressing by name survives the closing. This is the global rule that a reference addresses by name, applied to my own file.

**The team.** 07 wrote on 2026-10-01 that the user placed me in its team, 07 above, no one below. The user has not said it in this chat. The buffer's `## Team` records the placement with that attribution, and 07 said it would ask the user to say it here. **Do not resolve this by inference** — when the user confirms, drop the attribution; until then it stands as 07's report.

**Threads 07 closed, checked on the files before closing.** The orchestrator not reading `Phase note:` is by design — the user's ruling of 2026-09-24 as 07 quotes it, «Фазовый ноут — для архитектора, а не оркестратора»; the quote is in 07's buffer, which I do not read, so my buffer carries it as 07's report. Copy-or-link for a task spec had already drained: `command-pin-gaps` itself says a repeated paragraph is not a finding, and the global "never a copy" sits under § "Documentation style". I left 07 one note on it: the registry files "one home per fact" under § Grounding with no docs-only scope, and `context-tree` states it for the whole tree — not worth pressing unless a reviewer flags a copy.

## The phase 77 review

07 asked, at the user's word, for an independent reading, holding its own until mine existed. Its sources, in the user's words: fix the places that lead to counts in specs; a task's "now" is the code as every open task above it leaves it — «да не только в фазе! роадмап в принципе так устроен» — and «если скилы где то противоречат этому — разумеется это надо править»; anything without a source is a finding, because the user had that day rejected unrequested behaviour.

**What I found, and how it reconciled:**
- **The sweep still runs "now".** After the phase, `command-pin-gaps` reads code "as every open task above it leaves it" in the walk and the value-hole repair, while the blast-radius invariant still records "what the sweep, run now, reaches"; and `docs/what-a-task-carries.md` § "Blast radius: the rule, not the snapshot" says a spec never records what a search returned at writing time. The size word 77.4 removes was a symptom; the recorded sweep result is the measurement. Phase 77's own specs carry such records in their Finding paragraphs. 07 had judged it no contradiction and conceded; it went to the user as his ruling, because the repair reaches every spec. **If his ruling changes what 77.4 does, 77.7's now is rebuilt from the new after, not patched** — 0223 builds its now from 0218's after.
- **77.5's work-order sentence overreached** by "in this sense", forbidding positions and decided numbers that the global CLAUDE.md and `agent-architect` permit in an order. 07 narrows it to its own reason.
- **Two chain breaks:** the engine task's spec described the doc as it stood before 77.2; the pin-gaps walk task's spec misstated what 77.4 changes. Both fixed by 07.
- **The phase stated one of its two sources.** 07 adds `what-a-task-carries.md` to `Governing spec:` and the now-source to the note.
- **"Sequenced after" in contract lines** — unsourced, since order is position; 07 drops it.
- **I conceded "…pinned verbatim in the spec".** I had called it ceremony; it tells the planner the text is contract text, which `CLAUDE.md` § "Skill Authoring" treats as "the only type system this code has".
- **Left to the user:** the engine's "so the implementer does not re-derive it" against the doc's "planner", in the sentence 77.3 re-pins.
- **Left out of the phase by agreement:** "guards" in `roadmap-decompose` hook (d) — now a candidate in my buffer, promoted only on the user's word.
- **07's own, agreed:** the now-clause lands in many homes because skills cannot link docs, so each statement stays minimal; 77.8's after reads awkwardly and gets smoothed.

**My mistake in this stretch, and its pattern.** In my own pass I noticed that 77.7's value-hole repair, "read the code/proto as every open task above it leaves it", has an "it" with no task to refer to — and the finding did not reach my report. It surfaced only at the reconcile, where I sent it late; 07 agreed the repair should lean on the walk sentence instead, leaving one home for the clause in that file. The pattern: a finding noted mid-pass and not carried into the report is lost to the second reader at exactly the moment its independence is worth something. Said once; not yet a buffer entry. If it happens again, it is a debt to the buffer's Method.

**A trap from the same review.** My quote-checking regex reported most of the specs' now-sections as missing from their files; nearly all were spans of the spec's own prose caught between unrelated quotation marks. I judged them artifacts and checked the real quotes by hand. The buffer's method entry on checks that do not depend on the truth they test covers it.

## What will slip first after the compact

1. **The team placement is 07's report, not the user's word here.** Do not drop the attribution until he says it.
2. **The verdict on phase 77 is 07's.** Do not reopen the review or apply anything to it; nothing of mine is queued there.
3. **The user's open ruling on "run now"** decides whether 77.4 and 77.7 change — and if 77.4 changes, 77.7's spec is rebuilt, not patched.
4. **Do not move this folder's snapshots into `architect/`** until phase 78 lands in the skills; the engine still keeps them at the folder's root. When it lands, this file and snapshot 12 move.
5. **My buffer is uncommitted.** Mention it if an orchestrator run in this repository is about to start.
6. **Rehydrate by the probe**: read the session id, find this folder by `address.md`, refresh the standing entries from the seed — the seed may have changed by then, since phase 77 adds an entry to it ("a task's now") and amends the counts entry.

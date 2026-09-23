# 164 — the zone split comes out of the skill files

## What is true now

`src/skills/architect-editor-engine/SKILL.md` is the buffer's definition and the primary carrier of the zone split. Its frontmatter `description:` reads, in part:

> the definition of the
> architect's buffer the pair shares: its path and numbering, its settled zone
> held by both halves and its live zone held by the architect alone, the
> editor's re-read of the settled zone on change, and the drain rule that a
> ruling leaves the buffer once it reaches the artifact that should hold it,

Its body, § "The architect's buffer", reads:

> The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering; the architect's own skill points here rather than restating them.
>
> The buffer has two zones, and the split is load-bearing. The **settled** zone — the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice — is held by both halves: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time. The **live** zone — the editor's handle, the architect's current read of an open question, a diagnosis still forming — is the architect's alone: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted, and an independent reading is the only reason to ask for one.
>
> The editor re-reads the settled zone when it changes, not once at birth — and the same rule covers being named a different buffer's path outright by its architect: either way the memory has moved, and the hand adopts what it is now told, replacing what it held, holding one memory at a time.
>
> A channel-message the architect is already sending may carry, alongside its payload, what keeps the hand current: a fact about where the shared memory sits — that the settled zone has moved, or the buffer's path itself — or what the hand needs in order to work at all. [...]
>
> A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states.
>
> Two architects are two heads, and a head that reads another's memory is no longer holding its own. Several architects coexist under the numbering above, and each keeps its own buffer: no architect reads another architect's buffer. An editor reads only its own architect's buffer — the memory of the head it is the hand of — never another architect's, settled zone included.

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" reads, in the sentence about loading the engine: "it is where your buffer's path, zones, and rules are defined, so it is". Its § "Your buffer is shared; you alone write it" reads: "The buffer's path and numbering, its two zones and what each holds, the editor's re-read of the settled zone, and the drain rule are `architect-editor-engine`'s, loaded at birth — this section points there and restates none of them."

`src/agents/editor.md`'s opening paragraph reads: "load `architect-editor-engine` via the `Skill` tool — it is the shared contract for this pair, holding the two channel-message formats and the definition of the architect's buffer, whose settled zone you hold as your own working context from birth, and it must be resident before you read anything sent to you. Alongside that first channel-message, the spawn prompt gives you the buffer's own path — held from birth, never part of the message itself, since the format token alone still opens it and decides the mode — and it is where that settled zone lives."

The user has ruled the split out entirely (relayed in this round): the buffer has no zones and no region the editor may not read; what survives is that the head is the memory's only writer and the hand reads it in full and never writes to it. `docs/paired-loop.md` § "What the memory holds, and who holds it" already states this, and is the governing text this task conforms the code to.

## What must be true after

`src/skills/architect-editor-engine/SKILL.md`'s frontmatter `description:` reads, in the same position:

> the definition of the
> architect's buffer the pair shares: its path and numbering, the rule that the
> head is its only writer and the hand reads it in full and never writes to
> it, the editor's re-read of the memory on change, and the drain rule that a
> ruling leaves the buffer once it reaches the artifact that should hold it,

Its body, § "The architect's buffer", reads:

> The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering, and of the rule that governs who may write to it and who may only read; the architect's own skill points here rather than restating them.
>
> The head is the memory's only writer. The hand reads it in full — that is what makes the memory the link between the two halves — and never writes to it. It holds the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time.
>
> The editor re-reads the memory when it changes, not once at birth — and the same rule covers being named a different buffer's path outright by its architect: either way the memory has moved, and the hand adopts what it is now told, replacing what it held, holding one memory at a time.
>
> A channel-message the architect is already sending may carry, alongside its payload, what keeps the hand current: a fact about where the shared memory sits — that the memory has moved, or the buffer's path itself — or what the hand needs in order to work at all. [...]
>
> A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states.
>
> Two architects are two heads, and a head that reads another's memory is no longer holding its own. Several architects coexist under the numbering above, and each keeps its own buffer: no architect reads another architect's buffer. An editor reads only its own architect's buffer — the memory of the head it is the hand of — never another architect's.

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" now reads, in the same sentence: "it is where your buffer's path and rules are defined, so it is". Its § "Your buffer is shared; you alone write it" reads: "The buffer's path and numbering, the rule that the hand reads it in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth — this section points there and restates none of them."

`src/agents/editor.md`'s opening paragraph reads: "load `architect-editor-engine` via the `Skill` tool — it is the shared contract for this pair, holding the two channel-message formats and the definition of the architect's buffer, which you hold in full as your own working context from birth, and it must be resident before you read anything sent to you. Alongside that first channel-message, the spawn prompt gives you the buffer's own path — held from birth, never part of the message itself, since the format token alone still opens it and decides the mode — and it is where that memory lives."

No file gains a replacement boundary of any kind — no "always read, sometimes private," no renamed split. The two rules that survive, stated plainly wherever the buffer is defined or referenced: the head is the memory's only writer; the hand reads it in full and never writes to it.

## What breaks on contact

**Rule:** any hit in a repository-wide sweep for the buffer's zone vocabulary ("settled zone", "live zone", "two zones", "the split", bare "zone") that does not actually describe the buffer is a false positive, unrelated to this task, and stays untouched — the vocabulary recurs elsewhere for its own ordinary meaning (a factual/judgment split, a task's own scope-zone, a message-splitting verb, an unrelated data table, an unrelated heading in another skill's reference doc) and none of that usage is this task's to correct.

**Sweep (re-runnable):**
```
grep -rniE "settled zone|live zone|two zones|the split|zone" src/ docs/
```

**Invariant:** every result that is not one of this task's three named sites is a false positive by the rule above — checked individually: `docs/paired-loop.md`'s own "## Where the split falls" heading (a factual/judgment split); `docs/skill-description-field.md`'s "the zone of `command-pin-gaps`" (a task's territory); `src/commands/command-pin-gaps.md`'s "outside the task's zone" (a scope boundary); `src/skills/agent-architect/SKILL.md`'s occurrences of "split" as the marker-splitting verb ("trail the whole message or split it", "the marker splits mid-message") and "this skill is the architect alone"; `src/skills/aif-docs/references/split-state-b.md`'s "Execute the split" heading (document-splitting, an unrelated skill); and `src/skills/ui-ux-pro-max/data/*.csv`, which use "zone" for UI hover/magnetic regions, unrelated content in an unrelated skill's data tables. None of these needs any change and this task does not touch them. This corrects an earlier version of this section, which counted the false positives instead of naming them by category and, in counting them, missed two.

`.ai-factory/notes/07-architect-buffer.md` — the live architect buffer in this repository — is itself structured with literal `# Live — the architect's own` and `# Settled — the editor's to hold` headings, an actual instance of the split this ruling removes. It is out of this task's scope (not `src/`, not `docs/`, and per `agent-architect/SKILL.md` "It is the one file you edit directly: you are its only writer" — the architect's, never the editor's, to restructure) and this task does not touch it; flagged for the architect's own attention, not acted on here.

No other skill or command file references "§ The architect's buffer" or quotes any of the replaced sentences verbatim (confirmed by the same sweep) — this task's three edits do not invalidate any other file's grounding.

# 160 — the snapshot itself, not only its digest, is never delegated to the editor

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" reads, in the memory-snapshot paragraph:

> Either occasion records your buffer's path (defined in
> `architect-editor-engine`) and a digest of what the editor has accumulated;
> the digest is your own recovery note and is never sent to the editor.

This forbids delegating only the *digest* — nothing in the file says whether the snapshot file itself may be handed to the editor to compose. `docs/paired-loop.md` § "How the memory begins, and how it survives" now carries the governing claim this task leans on, in the paragraph beginning "The snapshot is written by the head, and a hand cannot write it...": the same channel principle that the hand who touched a surface writes about it, applied to the conversation as the surface and the head as what held it.

The same file's § "Relay on the marker; author the apply work-order and your own legwork" reads, describing what the two channel formats carry:

> A REPORT-ONLY message carries either the before-mark payload, worked in
> parallel and enriched only with named context, or your own delegated
> legwork; the APPLY-EDIT channel carries the apply work-order alone, and
> it **never** carries your own analysis of an analysis target.

Read on its own, this sentence licenses exactly what the digest sentence forbids: "the APPLY-EDIT channel carries the apply work-order alone" is unscoped as written — nothing here excludes the memory snapshot. The file's intro scopes "shared artifacts" as "roadmap, specs, code, docs," but the snapshot is merely absent from that list, not stated as excluded from it — a distinction a reader arriving at this later sentence, without walking back to the digest sentence or the intro, has no reason to draw. A reader stopping here could send the editor an `APPLY-EDIT` work-order for the snapshot and find nothing forbidding it.

## What must be true after

The sentence above is replaced with:

> Either occasion records your buffer's path (defined in
> `architect-editor-engine`) and a digest of what the editor has accumulated;
> the digest is your own recovery note and is never sent to the editor,
> and for the same reason the snapshot itself is never delegated to the
> editor to compose — the conversation is the surface a snapshot reports
> on, and only the head that held it can write what happened there.

No other sentence in this paragraph changes. The sentence in § "Relay on the marker; author the apply work-order and your own legwork" quoted above gains one clause, becoming:

> A REPORT-ONLY message carries either the before-mark payload, worked in
> parallel and enriched only with named context, or your own delegated
> legwork; the APPLY-EDIT channel carries the apply work-order alone, and
> it **never** carries your own analysis of an analysis target — nor,
> ever, the memory snapshot: composing that file is forbidden to the
> editor outright, not merely absent from this channel's ordinary cases
> (see "Spawn once, message thereafter").

No other sentence in that section changes.

## What breaks on contact

**Rule:** any file that quotes the digest sentence's current exact wording ("digest is your own recovery note") as ground truth for its own argument reads stale once the wording changes, except this task's own spec (records it as history, exactly as `## What is true now` does above), the roadmap's own contract line for this task (states the problem it describes, permanently), and this phase's own note (`152-…`, which documents a moment, not a standing claim about the present). Separately, and this is the rule the second edit exists to satisfy: no sentence in `src/skills/agent-architect/SKILL.md` may describe what an `APPLY-EDIT` work-order carries, or who composes a file's text, without excluding the memory snapshot — the digest sentence's prohibition must hold uncontradicted everywhere else in the file that touches the same ground.

**Sweep (re-runnable):**
```
grep -rln "digest is your own recovery note" src/ docs/ .ai-factory/
grep -n "written by the editor\|editor.*compose\|compose.*editor\|has the file open" src/skills/agent-architect/SKILL.md
```

**Invariant:** the first sweep returns this task's own target (unchanged by this edit — the phrase "digest is your own recovery note" survives verbatim, only gaining a clause after it), this task's own spec, and the roadmap's own contract line, plus this phase's own note — no historical handoff actually contains this phrase (checked directly: `.ai-factory/handoffs/` returns nothing, correcting the earlier version of this section, which wrongly claimed `26-` and `29-` as carriers). The second sweep, run after this task, returns exactly one line — the "text is written by the editor, who has the file open" sentence that opens the apply-work-order paragraph — which is not a second contradiction: it describes composing an `APPLY-EDIT` in general, and the exclusion this task adds sits later in the same section, closing the door before the section ends; no sentence anywhere in the file, read after this task, affirmatively licenses delegating the snapshot.

No sibling task of this phase addresses this task's own span; `58.1`, which immediately follows and now owns two adjoining sentences of its own, does not reach back into this one.

# 159 — the snapshot carries reasoning, not just residue, and is thick by default

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" reads, in the memory-snapshot paragraph:

> What a snapshot carries is only the volatile residue — where the work
> stands, what the hand knows, what will slip first, and what must not
> be resolved by inference — because everything durable already lives
> outside the conversation; never an inventory of the session.

This is the only sentence in the file governing what a snapshot's content must be, and it names nothing about the stretch's own reasoning — why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words. It also states no default for how much a snapshot carries: nothing distinguishes a thick snapshot from a thin one, or says which is the default.

The sentence immediately adjoining it, unchanged, reads:

> Each new
> snapshot supersedes the last by name — the numerically higher-numbered one
> is the current one — so a reader never follows a stale next action.

Once the first sentence requires a snapshot to carry a record — the reasoning above — this second sentence, left as it stands, reads against it: a plain reading treats an older snapshot's whole record as disposable the moment a newer one exists, which contradicts the record just made mandatory. The two live in one task because they are adjoining sentences of one paragraph and the second would otherwise argue with the first — not because they are the same requirement.

`docs/paired-loop.md` § "How the memory begins, and how it survives" now carries the governing claims this task leans on: the paragraph beginning "A break leaves the durable artifacts untouched..." (what a break destroys is the reasoning, not the state), the closing supporting fact that the durable artifacts — roadmap, specs, buffer — already survive a compact untouched, so restating their state is not the point, and the paragraph beginning "A newer snapshot supersedes the older one's next action, and nothing else..." (the record is not superseded, only the standing instruction is).

## What must be true after

The first sentence above is replaced with:

> What a snapshot carries is the volatile residue — where the work
> stands, what the hand knows, what will slip first, what must not
> be resolved by inference — and the reasoning that shaped it: why
> one option was taken over another, which premise proved false and
> how, what the user's own correction was and in what words;
> everything durable already lives outside the conversation, so
> restating it is never the point, and a snapshot that drops the
> reasoning is an inventory, not a history. It is thick by default,
> carrying that reasoning in full; thin only when asked for, or when
> what is plainly meant is a pointer list for raising context rather
> than a stretch's history.

The adjoining sentence gains a scoping clause, becoming:

> Each new
> snapshot supersedes the last by name — the numerically higher-numbered one
> is the current one — so a reader never follows a stale next action; what
> goes stale is the next action alone, and the record beside it stays.

No other sentence in the paragraph changes. The reasoning requirement leans on `docs/paired-loop.md`'s break-destroys claim by consequence (what a break destroys is exactly what this sentence now requires the snapshot to carry) without repeating that paragraph's own wording or justification; the scoping clause takes only the operative fact from the doc's supersession paragraph — what goes stale and what does not — and leaves the doc's own reasoning about the series of snapshots being a history to the document itself, since the reader that reasoning addresses is not the architect executing this skill.

## What breaks on contact

**Rule:** any file that quotes this paragraph's current exact wording — "only the volatile", "inventory of the session", or a sentence ending "stale next action." — as ground truth for its own argument reads stale once the wording changes, except this task's own spec (records the old wording as history, exactly as `## What is true now` does above), the roadmap's own contract line for this task (states the problem it describes, permanently), a phase note (`152-…`, which documents a moment, not a standing claim about the present), a handoff (`29-…`, a different genre, read once and never re-read unconditionally), or the architect's own working buffer (`.ai-factory/notes/07-…`, a living memory this command has no authority to edit — out of scope, not a defect this task closes).

**Sweep (re-runnable, anchors chosen short on purpose — this task re-wraps the very paragraph it edits, and a longer prose phrase can land across the resulting line break and silently match nothing):**
```
grep -rln "only the volatile\|inventory of the session\|stale next action\." src/ docs/ .ai-factory/
```

**Invariant:** after the change, this task's own target (`src/skills/agent-architect/SKILL.md`) reads the new wording in full — it says "is the volatile residue" without "only", calls a snapshot that drops the reasoning "an inventory, not a history" rather than invoking "the session", and continues "a stale next action" with a semicolon rather than ending the sentence there. What the sweep still returns beyond this file falls under the rule's own exceptions above: this task's own spec, the roadmap's own contract line, phase note `152-`, handoff `29-`, and the buffer. No other file, before or after this task. The sweep locates candidates; reading decides.

No sibling task of this phase addresses either of the two sentences this task now owns; every other task in the same paragraph targets a different sentence, so applying this task first, last, or in any order relative to them leaves every sibling's anchor text intact.

# A handoff says on itself that it is a spent, temporary buffer

## Current state (grounded, read fresh)

`src/commands/command-handoff.md` mines a session and writes the result to `<root>/.ai-factory/handoffs/` through `note`. Its emitted template opens with `# Handoff — <semantic slug derived from the session subject>` followed directly by `## 1. Frame`. Nothing on the file records whether it has been used.

Nothing reads a handoff as a step. This command writes them; `roadmap-prune` writes one when its gate blocks and states "Do not touch `handoffs/` — it is never swept". No other skill names the directory. A rule about use therefore has no enforcer in the family and needs none: the instruction travels on the artifact itself, addressed to whoever opens it.

Because a spent handoff is indistinguishable from a live one, it keeps being cited as confirmation after its facts have moved, and anyone may edit one that is already spent.

The `description:` block calls the result "a durable note" and names no lifetime for it. The word asserts the opposite of what the artifact is: a handoff is a temporary buffer holding context between two sessions, and it is spent once read.

## The change

1. The emitted template gains one line between `# Handoff — <slug>` and `## 1. Frame`, reproduced byte-for-byte:

   ```
   **Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.
   ```

   The processed state is the same line with `[x]` in place of `[ ]`. Both forms are already in use in the corpus, and the template reproduces them exactly so the corpus does not split into two forms. No alternative wording is invented for either state.

2. The prose shape carries the identical line. `**Prose shape.**` in the same file produces a handoff with no `## 1. Frame` to anchor against; its directive states that the file opens with the `# Handoff — <slug>` title and the mark line directly beneath it, then flows into prose. A handoff carrying no mark is the defect this task closes, and the shape it was written in does not change that.

3. Step 2's Template hook bullet states that the mark line is literal template text, reproduced verbatim into the written file and exempt from the "passed blank / do NOT pre-fill it" rule governing the rest of the skeleton: it is not a placeholder description and nothing is mined into it. That the shape is feasible without touching `note` is this spec's rationale and does not enter the shipped file — `note`'s own default template already carries a fully literal line, `**Source:** conversation context`, beside placeholder descriptions. No claim about another skill's internals is written into `command-handoff.md`: it would be a one-sided cross-file assertion with no counterpart declaration in `note`, which this task does not touch.

4. The `description:` names the entity and its lifetime: a temporary memory buffer that carries context from one session to the next, spent once read. The word `durable` leaves the block.

5. The skill body gains the rule that mark carries, stated as a property of the artifact addressed to whoever holds a handoff file — never as a permission granted to this command's own write path, which always produces a new numbered file through `note`: a processed handoff is never edited; only an unprocessed handoff is edited, and the flip is the same line with `[x]` in place of `[ ]`, nothing else changed; where a cross-project handoff is assembled in parts and the previous part is already marked processed, a new handoff is written rather than the old one extended.

## Files & types

- edit: `src/commands/command-handoff.md` — the emitted template's top, and the rule in the body

## Guards

- Two states and nothing else. No date, no author of the reading, no third status.
- Neither the `description:` nor the body states a rule about what may cite a handoff. The description says what the artifact is and stops there: `note`'s own description carries no such rule, and a handoff is `note` under a lens. Citing a spent handoff as confirmation needs no rule here — the global CLAUDE.md § "Grounding claims" names a handoff among the descriptions ground truth overrides, and that always-loaded guarantee holds in every session without a call; naming it here is the reliance declared at the point it is leaned on. Whether a durable surface may name a handoff at all is stated nowhere and is not this skill's to state — task 33.1 clears those references site by site.
- Nothing scans the mark. It is prose addressed to a reader, not a protocol token, and no skill gains a step that reads a handoff.
- `roadmap-prune` is not touched and keeps never sweeping `handoffs/`.
- The handoffs already on disk are not backfilled.
- `note` is not touched: the template reaches it through the caller hook it already has.
- The handoff citations already present in the plan layer — task specs and direction preambles opening with a source-handoff line — are not swept here. This task changes `command-handoff` and nothing else; those citations are the plan layer's own perishable content and leave with their tasks at prune.

## Verification

Counts against a whitespace-normalized read of the named file, never a line-oriented `grep`.

- the emitted template carries the mark on its own line between the `# Handoff` title and `## 1. Frame`, and the sentence naming the reader as the one who flips it → each 1
- the prose-shape directive names both the `# Handoff — <slug>` title and the mark line directly beneath it → each 1
- the Template hook bullet states the literal/verbatim exemption → 1
- the `description:` block names the buffer and its lifetime and no longer contains the word `durable` → the word `durable` in that block → 0
- the skill body states all four parts of the rule: the audience it addresses, that a processed handoff is not edited, that only an unprocessed one is edited with the flip being `[x]` in place of `[ ]` and nothing else changed, and that a spent previous part means a new handoff rather than an extended one → each ≥ 1
- no claim about `note`'s internals entered the shipped file → `**Date:**` and `**Source:**` in `src/commands/command-handoff.md` → 0 each
- `roadmap-prune` in that file → 0, and `git diff HEAD -- src/skills/` is empty — no skill gains a read of the mark
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/commands/command-handoff.md` and nothing else. The check presumes a tree clean at task start; where one of those paths was already dirty on entry, it is taken against this task's own changes rather than the tree's
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
- no citation rule entered the file: `cite`, `cited` or `citation`, case-insensitive, in `src/commands/command-handoff.md` → 0

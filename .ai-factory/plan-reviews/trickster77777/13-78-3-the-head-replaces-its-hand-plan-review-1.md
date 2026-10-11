## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/13-78-3-the-head-replaces-its-hand.md`
**Task:** 78.3 — the head replaces its hand (roadmap `.ai-factory/roadmaps/trickster77777.md`, Phase 78)
**Task spec:** `.ai-factory/specs/trickster77777/0240-the-head-replaces-its-hand.md`
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The change stays in the architect lens (`agent-architect`). The hand's rehydration in `src/agents/editor.md` is left to 78.4, and the `editor/` folder definition stays with the engine, where 78.2 put it. The plan's Scope paragraph keeps to that split.
- **Rules** (`.ai-factory/RULES.md`): not present — WARN (optional file missing; nothing to check).
- **Skill context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present.
- **Roadmap**: OK. The plan's title matches the open line `78.3 — the head replaces its hand`, which sits at the seam directly after `[x] 78.2`. The contract line, the task spec and the plan agree on all five edits: the replacement paragraph, the digest becoming a pointer, the greenlight scoped to a shared artifact, the confirmation scoped the same way, and "your own memory snapshot".
- **Governing spec** (`docs/paired-loop.md` § "How the memory begins, and how it survives"): OK. The spec's pinned replacement paragraph matches the doc. That covers the half-to-four-fifths window, the seam as the head's pick, the quiet act and "like a dead hand". The doc's spawning of a new hand that reads the snapshot belongs to 78.4, and the plan defers it there correctly.
- **Phase note** (`0215-…`): OK. Its "Who writes", "A fresh hand after a live one", "When the head acts" and "The digest" bullets are all covered by this task.

### Anchor verification against the file

I checked every anchor the plan names against the current `src/skills/agent-architect/SKILL.md`:

- The paragraph that opens "The memory snapshot continuing this same architect has two occasions" exists. It runs through "no template is consulted." and then "Either occasion writes the snapshot into your own folder…" through "…yours reports on the conversation.". The split point is correct, and the replaced tail matches the spec's "What is true now" quote.
- The paragraph that opens "If the send fails, the editor is dead" closes "…losing it silently is the defect." and is the last paragraph before `## Relay on the marker; author the apply work-order and your own legwork`. The insertion point exists as described. The spec does not pin a placement. Putting the new paragraph after the death paragraph, because it ends "like a dead hand", is a sound choice.
- "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits, and…" exists. The scoped insertion lands where the spec pins it.
- "…nor, ever, the memory snapshot: composing that file is forbidden to the editor outright…" exists in the paragraph that opens "The two channel-message formats govern what opens a round".
- "The user greenlights each apply work-order and authorizes every commit" exists in § "The user rules the forks and owns the commits".

I also re-ran the spec's sweep against the current tree. Each pattern returns only the hits the spec's Finding names, all in `agent-architect`. Nothing turns up in `docs/`, `CLAUDE.md` or any other skill.

Beyond the spec's sweep, I checked § "Review in parallel, reconcile before the apply order", which says "Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go." That sentence applies to a review-shaped target ("a review-shaped target adds only this on top"). The ask for the hand's snapshot is not drafted out of a review, so it does not leave that ask waiting on a greenlight, and the spec's breaks-on-contact rule is not triggered. I also checked the closing sentence of § "Your buffer is shared; you alone write it": "The buffer, `address.md` and your snapshots — your own folder — are the only files you edit directly: you are their only writer". It stays true with `editor/` in the folder, because the head still does not write `editor/`.

### Critical Issues

None.

### Issues

1. **The sweep's expected results describe grep lines that hard wrapping will not produce** (plan § "Sweep", "Expected results after the edits").
   The plan expects `forbidden to the editor` to return "only the line that now reads 'your own memory snapshot'". In the file, "nor, ever, the memory snapshot: composing that" and "file is forbidden to the editor outright, …" are two separate wrapped lines. After the edit, the first becomes "an analysis target — nor, ever, your own memory snapshot: composing that", which is 76 columns and still within the folder's 72–80 column style. Under the plan's own rule ("Re-wrap only the lines an edit touches"), the line that matches `forbidden to the editor` stays "file is forbidden to the editor outright, not merely absent from this" and does not contain "your own memory snapshot". The `greenlights` and `has confirmed` expectations have the same problem: once the touched lines are re-wrapped, "on a shared artifact" and "to a shared artifact" can fall onto the next line. Read literally, the check fails on a correct edit. An implementer could then re-flow the text to make the grep line match, or report a false failure. The plan also has no positive check that each pinned after-text landed verbatim. The sweep only proves that old phrases are gone.
   **Fix:** state the expected results as hit counts and locations, not line contents. For example: "`forbidden to the editor` returns exactly one hit, in § 'Relay on the marker…'". Then add one positive check. Read each edited passage, join its wrapped lines, and compare it with the spec's pinned after-text under "What must be true after", where only line breaks may differ. That covers the replacement paragraph, the snapshot paragraph's new ending, the two scoped sentences and the "your own memory snapshot" clause.

### Positive Notes

- The plan identifies each edit by its anchor text and leaves the wording to the spec. This follows one home per fact and avoids copy drift between the plan and the spec.
- The scope is tight and correct. 78.4's hand rehydration is explicitly excluded, the frontmatter description is checked and left alone, and "never a fresh spawn per task" is kept, with the spec's reason given.
- The "two cases stay two" guardrail on the "You author your own prompt" sentence correctly blocks a likely drift: a third case added for the snapshot ask.
- The placement of the new paragraph is reasoned from its content ("like a dead hand").
- The folder style is named and the wrapping rule is stated.

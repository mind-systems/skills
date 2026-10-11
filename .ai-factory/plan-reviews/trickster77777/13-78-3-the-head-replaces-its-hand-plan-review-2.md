## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/13-78-3-the-head-replaces-its-hand.md`
**Task:** 78.3 — the head replaces its hand (roadmap `.ai-factory/roadmaps/trickster77777.md`, Phase 78)
**Task spec:** `.ai-factory/specs/trickster77777/0240-the-head-replaces-its-hand.md`
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The edits stay inside the lens `agent-architect`. The `editor/` folder definition stays in `architect-editor-engine`, where 78.2 put it; the engine now defines `editor/` and the line "`editor/` is the hand's to write" (commit `15a02f7`). The hand's rehydration in `src/agents/editor.md` is left to 78.4.
- **Rules** (`.ai-factory/RULES.md`): not present. WARN: the file is optional, so there was nothing to check.
- **Skill context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present.
- **Roadmap**: OK. `78.3` is the first open line after `[x] 78.2`, so it is the task at the seam. The contract line, the task spec and the plan agree on all five edits.
- **Governing spec** (`docs/paired-loop.md` § "How the memory begins, and how it survives"): OK. The spec's pinned replacement paragraph matches the doc on the window from half to four fifths, the seam as the head's pick, the quiet act and "like a dead hand". The doc also says the head "spawns a new hand that reads the buffer and that snapshot". Per the 78.4 spec, that spawn goes through the skill's existing spawn rule and the reading is 78.4's work, so this plan correctly leaves both out.

### Anchor verification against the file

I re-read `src/skills/agent-architect/SKILL.md` and checked every anchor the plan names:

- **Snapshot paragraph.** It opens "The memory snapshot continuing this same architect has two occasions" and runs to "no template is consulted.". From "Either occasion writes the snapshot into your own folder" it runs to "…yours reports on the conversation.". The replaced tail matches the spec's "What is true now" quote.
- **Death paragraph.** It opens "If the send fails, the editor is dead", closes "…losing it silently is the defect." and is the last paragraph before `## Relay on the marker; author the apply work-order and your own legwork`. The insertion point exists.
- **Confirmation sentence.** "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits, and…" exists.
- **Prohibition clause.** "…nor, ever, the memory snapshot: composing that file is forbidden to the editor outright…" exists in the paragraph that opens "The two channel-message formats govern what opens a round".
- **Greenlight sentence.** "The user greenlights each apply work-order and authorizes every commit" exists in § "The user rules the forks and owns the commits".

On the current tree, each sweep pattern returns exactly one hit, in `agent-architect`, and nothing in `docs/`, `CLAUDE.md` or any other skill. The plan's expected results after the edits follow from that: zero hits for `digest of what` and `never delegated`, and one hit each for the other four patterns.

### Earlier review: resolved

Review 1 found one issue: the sweep's expected results named the content of grep lines, which hard wrapping would not reproduce. That is fixed. The expected results are now hit counts and section locations. There is an explicit instruction never to re-flow text to make a grep line match. A positive check now joins the wrapped lines of each edited passage and compares it with the spec's pinned after-text, where only line breaks may differ. It covers all five pinned passages.

### Other checks (no finding)

- **"Kept for the session".** The frontmatter description says "spawned on first contact, kept for the session", and the opening paragraph says "a persistent subagent you keep once spawned". Both stay true under the doc's framing, "one editor under successive handles". The spec's breaks-on-contact rule does not reach them, so leaving the description alone is correct.
- **Handle recording.** The paragraph "At the moment you spawn the editor (see above), write its handle into the buffer" applies to any spawn, including a replacement. The successor's handle is therefore recorded without a new sentence.
- **Approval rule in the review section.** "Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go" applies only to a review-shaped target. The snapshot ask is not drafted from a review, so this does not conflict with "needs no greenlight".
- **Writers of the folder.** "The buffer, `address.md` and your snapshots — your own folder — are the only files you edit directly" stays true: the head still does not write `editor/`.

### Critical Issues

None.

### Issues

None.

### Positive Notes

- Each edit is named by its anchor text, and the wording stays in the spec as its one home. This avoids drift between the plan and the spec.
- The guardrail that the two cases stay two blocks the likely mistake of adding a third case for the snapshot ask.
- The new paragraph's placement is argued from its content ("like a dead hand" refers back to the death paragraph). The plan also keeps "never a fresh spawn per task" and gives the spec's reason.
- The verification step now proves both that the old phrases are gone and that the new text landed verbatim. It does this without tempting the implementer to re-flow the text.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/0241-the-hand-rehydrates-from-the-buffer-and-its-predecessors-snapshot.md` — `agent-architect`'s death paragraph says a fresh hand "holds none of the accumulated round history a live one had". Once 78.4 has the successor read the latest snapshot in `editor/` "after a replacement and after a death alike", that claim is only partly true: the successor carries everything up to the last replacement and loses only the rounds since. The conclusion that the next order "**must be** self-contained" still holds. 78.4's sweep (`buffer's own path`, `spawn prompt`, `born fresh`) does not search this sentence, and 78.3's spec does not pin it. Whether it should be reworded, and in which task, is a planning decision for the phase, not for this plan.

PLAN_REVIEW_PASS

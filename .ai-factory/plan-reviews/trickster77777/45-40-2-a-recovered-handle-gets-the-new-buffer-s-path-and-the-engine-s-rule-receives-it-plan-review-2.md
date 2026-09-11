## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/45-40-2-a-recovered-handle-gets-the-new-buffer-s-path-and-the-engine-s-rule-receives-it.md` (revision after plan-review-1)
**Files Reviewed:** 6 (plan, task spec 129, `src/skills/agent-architect/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md`, `src/agents/editor.md`, `docs/paired-loop.md`) plus the roadmap line and phase 40 header in `.ai-factory/roadmaps/trickster77777.md`, and plan-review-1.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present, § "Composition: mechanism vs policy". The plan keeps the split: the engine widens one mechanism sentence and gains no policy (it is explicitly forbidden to mention the metadata fallback or how the architect came to hold no pointer); the lens gains policy and points at the engine's rule and at its own sibling sections by heading name, restating nothing. No new `loads:` edge, no inlining. Aligned.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (optional file, non-blocking).
- **Roadmap** — 40.2 is the first `[ ]` line in `.ai-factory/roadmaps/trickster77777.md` (40.1 `[x]`); the plan heading matches the contract line; the `Spec:` tag resolves to spec 129, and the plan's boundary (recovery paragraph + engine re-read sentence; respawn paragraph left to 40.6; `editor.md` left to 40.3; engine buffer section left in place for 40.4 to anchor beside) matches spec 129's "Blast radius" verbatim in substance. Governing spec `docs/paired-loop.md` is the one the phase header names; the plan's citations — § "How the memory begins, and how it survives" ("Each half holds the other's address. At the moment a hand joins, its own address is recorded in the memory, and the memory's place is given to the hand in turn") and § "What crosses the channel" (keeping the hand current rides inside whatever message is already going) — both resolve as quoted. Aligned.

### Review-1 follow-through

All three issues from plan-review-1 are closed in this revision:

1. **Handle-write at recovery** — now item 1(a): the recovered handle is written into the new buffer in the same act as the naming, pointing at the handle-write paragraph by concept and leaving it byte-identical. This carries both halves of the governing spec's symmetric address exchange. Closed.
2. **`own buffer` probe** — replaced: `recovered` (zero hits today, verified) is the primary probe, and the one pre-existing `own buffer` hit in the conditional rule is stated as expected. Closed.
3. **Two framings** — pinned to one (the editor was spawned by an architect whose buffer did not reach you; you are a new architect; the re-pointing is what makes it your hand), with the competing lineage phrasings explicitly banned from the new text. Closed — but the guard added for it introduces the one issue below.

### Grounding check (fresh)

Every anchor resolves against the files as they stand today: the recovery paragraph opens "Continue in the same conversation if the editor is still alive." and ends "…the id is the filename segment between `agent-` and `.meta.json`."; the next paragraph opens "If the send fails, the editor is dead"; the engine's "The editor re-reads the settled zone when it changes, not once at birth." is a standalone paragraph in § "The architect's buffer"; the upkeep classing sits under "Relay on the marker; author the apply work-order and your own legwork" ("Keeping the hand current — naming that the shared memory has moved … is not a round and needs no form of its own"); the buffer section's "When the memory the hand holds moves, you name the change to the editor in the same act as the write" and its by-concept reference "the editor's re-read of the settled zone" both exist as the plan says; "Losing the editor is never fatal; losing it silently is the defect" is the closing sentence of the respawn paragraph. `editor.md` names the buffer only at "whose settled zone you hold" and "gives you the buffer's own path — held from birth". Line counts 320 / 45 are correct. The reading of the spawn paragraph's "a later round sent via `SendMessage` never repeats it" — a different path is not a repeat — is sound, and the plan requires the new text to make that plain.

### Critical Issues

None.

### Issues

1. **Verification probe fails against the file as it stands, on a paragraph the plan orders byte-identical.** (`src/skills/agent-architect/SKILL.md`, task 1, guardrails: "`grep -n "earlier run\|same architect" src/skills/agent-architect/SKILL.md` must return nothing".)
   `same architect` already occurs today in the snapshot paragraph — "The memory snapshot continuing this same architect has two occasions" (verified by running the grep before any edit). That hit is legitimate: on the snapshot path the lineage *is* real, which is exactly the contrast the plan's one-framing rule draws against the recovery path. As written, the probe returns a hit before the implementer types a word, and the two ways to satisfy it literally are a false failure report or an edit to the snapshot paragraph the same guardrail forbids. This is the same class of defect as review-1's issue 2, reintroduced by the fix for issue 3.
   **Fix (plan text only):** scope the probe to the recovery paragraph — e.g. `sed -n '/^Continue in the same conversation/,/^If the send fails/p' src/skills/agent-architect/SKILL.md | grep -n "earlier run\|same architect"` must return nothing — or keep the file-wide grep and state the one pre-existing hit in the snapshot paragraph as expected, the way the plan already does for `own buffer`.

### Positive Notes

- Both halves of one act now land in one paragraph, each pointing at the paragraph that already owns its mechanics (handle-write, buffer-moves upkeep, engine re-read) by heading or by concept — the engine/lens discipline held exactly.
- The one-framing rule is a real improvement: it makes "an editor reads only its own architect's buffer" read correctly for the recovered pair, and it names the failure phrasings rather than hoping the implementer avoids them.
- The engine task keeps the "not once at birth" contrast alive and forbids any policy (the fallback, the pointer's absence) from leaking into the mechanism — precisely what keeps 40.4 able to anchor beside the widened sentence.
- The alternatives are named with their reasons, and the "Losing the editor…" sentence is pointed at, not touched.

## Deferred observations

- Affects: `docs/paired-loop.md` § "What the memory holds, and who holds it" / the final `aif-docs` verification pass — after this task the engine's re-read sentence covers being named a different path outright, while the doc's own sentence at the same place ("The editor re-reads the settled zone when it changes, not once at birth: a buffer earns its keep by being written to during a session") covers only in-place change. The meaning is carried elsewhere in the doc (§ "How the memory begins": "the head names the moment that memory moves"; § "What crosses the channel": "naming that the shared memory has moved"), so no contradiction; but spec 129 keeps the doc unedited, and docs → code direction says the doc's sentence is the one that should have widened first. Candidate for the next doc revision.
- Affects: task 40.3 / `src/agents/editor.md` — "gives you the buffer's own path — held from birth" describes the spawn moment only; once the engine's widened rule lands, the path the hand holds can be replaced by a naming inside a later message. Not false (the engine governs and is loaded at birth), but the clause reads as if the path were fixed. 40.3 edits the paragraph directly below it and can bring this clause level in passing, or leave it.
- Affects: governing spec `docs/paired-loop.md` § "How the memory begins, and how it survives" / phase 40 follow-up — the conditional rule closes "Either way the buffer exists before any editor does" and the doc says "creates its own buffer first, and only then takes on a hand". On the recovery path this task pins, an editor exists before the new buffer does; what stays true is that the buffer exists before the architect *addresses* a hand. Spec 129 keeps the conditional rule byte-identical, so nothing to do here; the wording is a candidate for the doc when it is next revised.

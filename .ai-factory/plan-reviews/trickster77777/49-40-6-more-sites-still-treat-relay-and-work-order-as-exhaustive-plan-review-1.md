## Plan Review — 40.6 — more sites still treat relay-and-work-order as exhaustive

**Plan:** `.ai-factory/plans/trickster77777/49-40-6-more-sites-still-treat-relay-and-work-order-as-exhaustive.md`
**Files the plan targets:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap** — the plan's `# Plan: 40.6 — …` heading matches contract line 40.6 in `.ai-factory/roadmaps/trickster77777.md` (Phase 40, `Governing spec: docs/paired-loop.md`). The plan's three sites are exactly the three the contract line names; the widen/narrow split per site matches the line and spec 133 § "The change". Aligned.
- **Task spec chain** — spec 133 read in full; its "Current state" quotes were checked against the file fresh: all three quoted sentences stand verbatim at § "Spawn once, message thereafter" (spawn sentence; respawn sentence in the dead-editor paragraph) and § "Review in parallel, reconcile before the apply order" (closing sentence). The rule the third site leans on — "That second case needs no marker and no permission: the marker governs whose words cross the channel, not you delegating your own work" — stands in § "Relay on the marker; author the apply work-order and your own legwork", as the spec says. Aligned.
- **Governing spec** — `docs/paired-loop.md` § "The user's marker": "The marker governs whose words cross the channel; it has nothing to do with the head delegating its own legwork, which needs no permission." The narrowing of the third site to relay timing, and the widening of the two spawn-path sentences, both conform to this. Aligned.
- **Architecture** — `.ai-factory/ARCHITECTURE.md`: SKILL.md body ≤ 500 lines (file is 367; three sentence-level edits cannot cross it); no module boundary crossed — the edit is the architect's own account of its sending behavior, so `editor.md` and `architect-editor-engine` correctly stay untouched (the plan's guard names both). No issue.
- **RULES.md** — absent; skipped (WARN: optional file missing, no effect).
- **Vocabulary** — the plan pins the file's own construction "delegating your own legwork" and forbids a coined noun for the round; this is the correct reading of the one-word-one-meaning contract on skill bodies (no new name for a concept the registry and the file do not have). No issue.

### Verification of the plan's grounding claims

- "No other site in the file states the pair as exhaustive" — verified by sweeping every `relay` occurrence in the file: the only closed-list shapes are the spawn sentence, the respawn sentence, and the marker-decides sentence. The "nothing else" inventory paragraph is indeed gone (§ "Relay on the marker…" now reads "not everything you may ever send the editor" and lists `REPORT-ONLY` as carrying "either the before-mark payload … or your own delegated legwork"). Claim holds.
- "The echo sentences 40.5 added" — present at the tail of the case-naming paragraph ("A report on your own delegated legwork carries no second opinion … it is not signal the way a relay's agreement is."); the plan's guard that this paragraph stays byte-identical is correctly scoped.
- "A respawned editor resumes through the same two channels" stays byte-identical — correct: "two channels" there means the two message formats, and a delegated round is a `REPORT-ONLY` message, so the sentence already covers it without change.
- The plan's reasoning for leaving "an undelivered payload is never auto-replayed into a fresh spawn, because the user phrased it for a warm context" untouched is sound and mirrors spec 133's own framing (only the user's words are the non-replayed payload; the architect's own composed round is its own to resend, exactly as the apply work-order already is).
- Three hunks: the three anchor sentences sit at roughly lines 49–51, 158–161 and 307–308, far outside each other's diff context, so the guard "exactly three hunks" is achievable as stated.

### Critical Issues

None.

### Positive Notes

- Every edit is anchored by name (the quoted sentence and its section heading), never by position — the implementer cannot land on the wrong paragraph.
- The plan pins the byte-identical tails on each edited paragraph and names the neighbouring tasks' territory (40.2, 40.7), so the collision analysis in spec 133 § "Blast radius" is carried into the plan as explicit guardrails rather than left to memory.
- The third-site instruction is precise about what *not* to add (no exception clause, no cross-reference) — this is the exact reading of the spec's "dropping the overreach, not restating or pointing at" and prevents the most likely over-edit.
- The guard step greps the added lines for the coined nouns the spec forbids, which is the one silent-failure surface this task has (a wrong noun would pass every other check).

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/133-sites-still-treat-relay-and-work-order-as-exhaustive.md` § "Blast radius" — the paragraph says the spawn-sentence site "sits directly after the paragraph 40.7 edits — the memory-snapshot paragraph". In the file the order is the reverse: the spawn sentence's paragraph ("Until the first channel-message arrives…") comes first, and the memory-snapshot paragraph ("The memory snapshot continuing this same architect…", holding "Each new snapshot supersedes the last by name") follows it. The plan inherited the inverted direction ("Do not touch the *preceding* memory-snapshot paragraph"), but its guard names the paragraph by its own sentence, so the edit lands correctly regardless; the non-collision conclusion is unaffected either way. The wording belongs corrected at its home in the spec (and 40.7's spec, if it repeats it), not in this plan.

PLAN_REVIEW_PASS

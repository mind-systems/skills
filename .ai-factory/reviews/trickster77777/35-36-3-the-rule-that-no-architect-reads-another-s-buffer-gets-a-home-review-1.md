# Review: 36.3 — the rule that no architect reads another's buffer gets a home

**Plan:** `.ai-factory/plans/trickster77777/35-36-3-the-rule-that-no-architect-reads-another-s-buffer-gets-a-home.md`
**Changed (tracked):** `src/skills/architect-editor-engine/SKILL.md` (+5 / −2). The other staged files are this task's own plan, sidecar, and plan-review artifacts.
**Risk:** 🟢 Low — one skill body, one new paragraph, one description clause; no callers, no `loads:` edges, no protocol tokens touched.

## What was checked

- **Full file read** (`src/skills/architect-editor-engine/SKILL.md`, 45 lines). The new paragraph closes § "The architect's buffer" after the drain-rule paragraph — the placement the plan pinned and the governing spec `docs/paired-loop.md` § "What the memory holds, and who holds it" uses itself.
- **Both clauses present, in the engine's own voice.** Architect clause: "each keeps its own buffer: no architect reads another architect's buffer." Editor clause: "An editor reads only its own architect's buffer — the memory of the head it is the hand of — never another architect's, settled zone included." The reason is one clause ("a head that reads another's memory is no longer holding its own"). Three sentences, as the plan asked. No restatement of the zone split, re-read rule, or drain rule; no mention of pairing roles, `architect-pairing-engine`, `docs/paired-loop.md`, or any task/phase number.
- **Description enumeration extended.** The clause lands before "When-to-use policy stays with the caller.", inside the existing `>-` folded block, indentation and line width matching the neighbours. Description is 871 characters (limit 1024). Frontmatter has no tabs or trailing spaces; `name`, `user-invocable`, `disable-model-invocation`, `allowed-tools` unchanged.
- **One home under `src/`.** `grep -rn "another" src/skills/architect-editor-engine/SKILL.md src/skills/architect-pairing-engine/SKILL.md src/skills/agent-architect/SKILL.md src/agents/editor.md` hits only the engine (description line 13, body line 45). `architect-pairing-engine` still mentions no buffer and is untouched, per spec 118 § "Blast radius".
- **Callers stay consistent.** `agent-architect` § "Your buffer is yours alone" is a writer rule (single writer) and does not conflict; `editor.md` tells the editor it holds the settled zone of *the architect's* buffer, which is exactly the editor clause. `architect-pairing-engine`'s applying role still routes an arriving work-order through the applying architect's own editor, so that editor still reads only its own architect's buffer — no contradiction introduced.
- **Live path.** `active/skills/architect-editor-engine` → `../../src/skills/architect-editor-engine`, so the change is what `~/.claude/skills` loads.
- **Governing spec direction.** `docs/paired-loop.md` already says the buffer's "shape and rules live in the engine both halves load at birth"; the doc needed no edit and received none. Docs → code, one direction.
- **Vocabulary.** "architect", "editor", "buffer", "settled zone" used with their registry meanings; no synonym introduced.

## Non-blocking notes

- The description now reads "…and the drain rule that …, and the rule that no architect reads another's buffer and an editor reads only its own architect's." — a doubled "and …, and …" that is grammatical but slightly heavy. Acceptable for an enumeration; not worth a round.
- "Several architects coexist under the numbering above" echoes the section's opening sentence ("so that several architects coexist without colliding"). It serves as the anchor tying the rule to the numbering, so it is a reference rather than a copy.

No correctness, security, or runtime findings.

REVIEW_PASS

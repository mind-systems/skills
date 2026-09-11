## Review — 40.7 — "supersedes the last by name" gets a referent

**Plan:** `.ai-factory/plans/trickster77777/50-40-7-supersedes-the-last-by-name-gets-a-referent.md`
**Changed files:** `src/skills/agent-architect/SKILL.md` (1 hunk, +3/−2); plan, plan-review, and sidecar under `.ai-factory/` (artifacts, not reviewed as code)
**Risk Level:** 🟢 Low

### What was checked

`git diff HEAD` and `git status` read; `src/skills/agent-architect/SKILL.md` read in full (371 lines), with the memory-snapshot paragraph of § "Spawn once, message thereafter" read in place rather than through the hunk. The edited sentence was checked against the plan's task instruction, spec 134 § "The change" and § "Blast radius", the referent in `src/skills/note/SKILL.md` (**Folder style** paragraph), `src/commands/command-handoff.md` § "Step 2 — Delegate to `note`", and the governing spec `docs/paired-loop.md` (the memory-snapshot paragraph).

**The sentence.** "Each new snapshot supersedes the last by name, so a reader never follows a stale next action." → "Each new snapshot supersedes the last by name — the numerically higher-numbered one is the current one — so a reader never follows a stale next action." The opening and the reason clause survive unchanged in meaning; the inserted em-dash clause is the comparison rule alone. "Numerically" pins the comparison to the parsed integer, which is what `note`'s folder-style step states ("decided over the parsed integer, not the string") and what 38.1 installed — the referent is real and the clause agrees with it. Correct.

**Scope of the clause.** The addition says nothing about how the number is produced (`note`'s scan-and-add-one), where a snapshot lands (`command-handoff`'s `<root>/.ai-factory/handoffs/`), or whether an old one is overwritten; it adds no pointer to `note`, `command-handoff`, or 38.1. Added lines grepped for `handoffs/`, `notes/`, `mkdir`, "zero-padded", "add 1", "overwrit", "38.1" — none. This is the spec's central constraint ("a comparison rule, not an account of the mechanism behind it") and it holds.

**The rest of the paragraph.** The two occasions, the on-request capability, what is recorded, the volatile-residue description, and "Of the recorded state, only the buffer's path travels: the pointer, never a copy …" are byte-identical in content. The clause the governing spec fixes — a snapshot "carries a pointer to the buffer's place, never a copy of what the buffer holds" — is untouched and still stated by the skill's own last sentence of the paragraph.

**Guards.** Exactly one hunk, confined to the target sentence. `src/commands/command-handoff.md`, `src/skills/note/SKILL.md`, `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, and `docs/paired-loop.md` are untouched (`git status`). Frontmatter unchanged; body is 371 lines, within the 500-line limit. "supersede" occurs once in the file, so no other site quotes the old wording and nothing went stale. The sidecar reads `"step": "implemented:1"`, consistent with the indexed marker grammar.

**Vocabulary.** "Memory snapshot", "buffer", "handle" keep their established meanings; no new term enters. "Current" is used as ordinary English for the snapshot a reader should follow, which is the sense the surrounding sentence already carries.

### Critical Issues

None.

### Non-blocking notes

- The re-flow left a short line: "recorded state, only the buffer's path travels:" (48 columns) followed by the untouched "the pointer, never a copy of the handle …" line. The plan asked not to re-wrap neighboring sentences, so this is the expected consequence, and it renders identically; a future edit to that sentence can absorb the wrap. Not worth a round.

## Deferred observations
- Affects: `docs/paired-loop.md` / Phase 40 owner — carried from plan-review-1: the skill states two snapshot occasions (before a compact; on request, "no command is invoked and no template is consulted") while the comparison rule now installed compares across numbered siblings; neither the skill nor the governing spec says both occasions land as numbered siblings in one folder. 40.7 was pinned to the comparison rule alone and correctly did not name a destination, so the gap is unchanged by this task and belongs to the governing spec, not here.

REVIEW_PASS

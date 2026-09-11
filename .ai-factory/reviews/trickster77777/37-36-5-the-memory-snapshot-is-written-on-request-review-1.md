## Review Summary

**Task:** 36.5 — the memory snapshot is written on request
**Plan:** `.ai-factory/plans/trickster77777/37-36-5-the-memory-snapshot-is-written-on-request.md`
**Files changed:** `src/skills/agent-architect/SKILL.md` only (17 insertions, 7 deletions); read in full, 282 lines. No other file in the working tree is modified beyond the plan/review artifacts; `.ai-factory/notes/07-architect-buffer.md` (the architect's own buffer) is untouched, as it must be.
**Risk Level:** 🟢 Low

### Verified on the file (not on the diff)
- `grep -c "the digest is your own recovery note and is never sent to the editor"` → `1`; the clause sits in the same position, directly after "a digest of what the editor has accumulated;". Byte-identical, as the contract line requires.
- `grep -c "pre-compact"` → `0`. The § "On every invocation" sentence now names the artifact — "the latest memory snapshot that recorded your buffer's path — written before a compact or on the user's request, either one recovers you the same way" — and keeps "if one exists", the wording spec 117's Blast radius leans on.
- `grep -c "command-handoff\|handoffs/"` → `0`: no destination, no filename convention, no command named. The on-request occasion is stated as the architect's own capability, "reached by a request rather than a command: no command is invoked and no template is consulted".
- "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer." → exactly one hit, still closing the reworked paragraph.
- Frontmatter (`name`, `description`, `argument-hint`, `user-invocable`, `disable-model-invocation`, `allowed-tools`, `loads`) has no diff lines. No `loads:` edge added.
- Cross-references resolve after the edit: the section's first paragraph "a memory snapshot naming a buffer — the handoff below that carries your buffer's path" points at the reworked paragraph, which still names the buffer's path and calls the artifact a handoff in its parenthetical; the spawn-moment paragraph's "(see above)" and "as defined above" still land on the paragraphs above it, which are unchanged.
- § "Your buffer is yours alone" is unedited (its sentences are true of the compact occasion and spec 123 names it as no site).
- The four residue items, "never an inventory of the session", and "supersedes the last by name" are spec 123's words; nothing beyond the spec's six facts was added, nothing from the engine (zones, drain rule) restated. One prose paragraph, hard-wrapped within the file's existing width (all new lines ≤ 77 columns).
- Vocabulary: "memory snapshot" is the governing spec's term and the file's own since 36.2; "handoff" remains only as genus. No reserved word repurposed.

### Critical Issues
None.

### Minor Issues
1. **`src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", reworked paragraph — "What it carries" has the wrong nearest antecedent.** The sentence "What it carries is only the volatile residue — where the work stands, what the hand knows, what will slip first, and what must not be resolved by inference — because everything durable already lives outside the conversation; never an inventory of the session." follows immediately on "the digest is your own recovery note and is never sent to the editor." The nearest singular subject is *the digest*, so a reader takes "it" as the digest — and then the residue (where the work stands, what must not be resolved by inference) and the "never an inventory of the session" rule read as constraints on the digest of the editor's state, not on the snapshot as a whole, while the very next sentence switches back to "Each new snapshot". The plan pinned this fact as "What a **snapshot** carries: only the volatile residue" precisely because the residue is the snapshot's content and the digest is one of its parts ("what the hand knows"). In an executable skill the antecedent is behavior: an architect reading it as the digest would still write an inventory into the rest of the snapshot without contradicting the text. Fix: name the subject — "What a snapshot carries is only the volatile residue …" (or "The snapshot carries only …"); no other change.

### Positive Notes
- The two occasions are stated once, in the one paragraph that owns the artifact, and the parenthetical "no other handoff has any reason to mention the buffer or the handle" now attaches to the artifact rather than to the compact — still true for both occasions.
- The § "On every invocation" rewrite names the artifact and keeps both the "if one exists" guard and the same recovery path for either occasion, exactly as the contract line asks.
- Nothing crept outside the two sites: editor.md, the engine, the governing spec, and the buffer note are all untouched.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/123-the-memory-snapshot-is-written-on-request.md` — "Each new snapshot supersedes the last by name" is now in the skill verbatim while the skill names no filename convention, so "by name" has no operational referent in the file (picked by its name, names the one it replaces, or overwrites under one name). The implementation correctly passes the spec's words through; the meaning belongs to the spec's owner. The "latest memory snapshot" wording in § "On every invocation" is consistent with the first reading.
- Affects: `.ai-factory/notes/07-architect-buffer.md` — the buffer paragraph "Taking a memory snapshot on request is a capability of the architect…" carries its own drain instruction ("Erase this paragraph when 36.5 lands"). The orchestrator correctly did not touch the buffer; the erasure is the architect's own act once this task is committed. [dismissed]
- Affects: task 36.6 / `.ai-factory/specs/trickster77777/124-the-architect-writes-to-the-memory-as-it-learns.md` — § "Your buffer is yours alone" still introduces the recovering artifact by the compact occasion alone ("The handoff continuing you across a compact carries this buffer's path alone"; "whatever of your own state must survive a compact"). True and out of 36.5's scope; 36.6 edits that section next, where naming the artifact would bring it level with the two sites reworked here. [fixed]

## Re-review Summary

**Task:** 36.5 — the memory snapshot is written on request
**Previous review:** `.ai-factory/reviews/trickster77777/37-36-5-the-memory-snapshot-is-written-on-request-review-1.md`
**Files changed:** `src/skills/agent-architect/SKILL.md` only (17 insertions, 7 deletions against `f6971a1`); re-read in full, 282 lines. No other file in the working tree is modified beyond the plan/review artifacts; `.ai-factory/notes/07-architect-buffer.md` remains untouched.
**Risk Level:** 🟢 Low

### Verdicts on the previous review's findings

1. **Minor — "What it carries" had the digest as its nearest antecedent** (§ "Spawn once, message thereafter", reworked paragraph). **Fixed.** Current content, read fresh from the file:

   > `the digest is your own recovery note and is never sent to the editor.`
   > `What a snapshot carries is only the volatile residue — where the work`
   > `stands, what the hand knows, what will slip first, and what must not`
   > `be resolved by inference — because everything durable already lives`
   > `outside the conversation; never an inventory of the session. Each new`
   > `snapshot supersedes the last by name, so a reader never follows a`
   > `stale next action.`

   The subject is now the snapshot, matching the plan's pinned fact ("What a snapshot carries: only the volatile residue"); `grep -c "What it carries"` → `0`. The re-wrap that followed the one-word change stays within the file's width (all lines of the paragraph ≤ 77 columns). Nothing else in the paragraph moved.

### Full pass for new issues — verified on the file
- `grep -c "the digest is your own recovery note and is never sent to the editor"` → `1`, still directly after "a digest of what the editor has accumulated;". Byte-identical to the pre-task text.
- `grep -c "pre-compact"` → `0`; § "On every invocation" reads "…and, if one exists, the latest memory snapshot that recorded your buffer's path — written before a compact or on the user's request, either one recovers you the same way." — names the artifact, keeps "if one exists" (spec 117's dependency), keeps the sentence's opening unchanged.
- `grep -c "command-handoff\|handoffs/"` → `0`: no destination, filename convention, or command named.
- "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer." → exactly one hit, closing the reworked paragraph.
- Frontmatter: zero diff lines touching `---`, `name:`, `description:`, `argument-hint:`, `user-invocable:`, `disable-model-invocation:`, `allowed-tools:`, `loads:`. No `loads:` edge added.
- Cross-references resolve: "a memory snapshot naming a buffer — the handoff below that carries your buffer's path" (first paragraph of the section) lands on the reworked paragraph, which records the buffer's path and names the artifact a handoff in its parenthetical; the spawn-moment paragraph's "(see above)" and "as defined above" still point at the unchanged paragraphs above it.
- § "Your buffer is yours alone", the editor definition, the engine, and the governing spec are unedited, per spec 123's Blast radius.
- Content is bounded to spec 123's six facts (two occasions; request not command, no command/template; path + digest with the digest clause; the four residue items and "never an inventory"; supersedes by name; only the path travels). Nothing from the engine restated; no fifth residue item; one prose paragraph in the section's register.
- Vocabulary: "memory snapshot" is the governing spec's term and the file's own; "handoff" appears only as the genus. No reserved word repurposed.

### Critical Issues
None.

### Minor Issues
None.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/123-the-memory-snapshot-is-written-on-request.md` — "Each new snapshot supersedes the last by name" is in the skill verbatim while the skill names no filename convention, so "by name" has no operational referent in the file (picked by its name, names the one it replaces, or overwrites under one name). Passing the spec's words through is correct; the meaning belongs to the spec's owner. The "latest memory snapshot" wording in § "On every invocation" is consistent with the first reading.
- Affects: `.ai-factory/notes/07-architect-buffer.md` — the buffer paragraph "Taking a memory snapshot on request is a capability of the architect…" carries its own drain instruction ("Erase this paragraph when 36.5 lands"). The orchestrator correctly did not touch the buffer; the erasure is the architect's own act once this task is committed. [dismissed]
- Affects: task 36.6 / `.ai-factory/specs/trickster77777/124-the-architect-writes-to-the-memory-as-it-learns.md` — § "Your buffer is yours alone" still introduces the recovering artifact by the compact occasion alone ("The handoff continuing you across a compact carries this buffer's path alone"; "whatever of your own state must survive a compact"). True and outside 36.5's sites; 36.6 edits that section next, where naming the artifact would bring it level with the two sites reworked here. [fixed]

REVIEW_PASS

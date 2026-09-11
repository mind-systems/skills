# Plan: 36.5 — the memory snapshot is written on request

## Context
`src/skills/agent-architect/SKILL.md` names a compact as the only occasion for a memory snapshot; this task adds the second occasion the governing spec (`docs/paired-loop.md` § "How the memory begins, and how it survives") implies — the user asks for one mid-session — and reworks the one sentence that identifies the recovering artifact by its occasion ("the pre-compact handoff") rather than by what it is. One file changes; the digest clause is byte-identical before and after.

Ground truth read fresh (post-36.4, commit `f6971a1`):
- § "Spawn once, message thereafter", first paragraph, already calls the artifact "a memory snapshot naming a buffer — the handoff below that carries your buffer's path" — so "memory snapshot" is the name already in the file (and the governing spec's bolded term). The handoff paragraph is the "below" it points at.
- The handoff paragraph currently reads: "Before a compact, the handoff continuing this same architect across it — no other handoff has any reason to mention the buffer or the handle — records your buffer's path (defined in `architect-editor-engine`) and a digest of what the editor has accumulated; the digest is your own recovery note and is never sent to the editor. Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer."
- § "On every invocation" currently closes: "rebuild your working state from whatever the user hands you and, if one exists, the pre-compact handoff that recorded your buffer's path."
- § "Your buffer is yours alone" says "The handoff continuing you across a compact carries this buffer's path alone" — a true statement about the compact occasion, not a claim that it is the only occasion; neither the contract line nor the spec names it as a site, so it is **not** touched.

Assumptions pinned from the spec (not invented):
- The on-request snapshot is the architect's *own* capability: reached by the user's request, not by `/command-handoff`; no command invoked, no template (the handoff grid) consulted. The plan names no destination path — the file names none for the pre-compact snapshot today either, and the spec does not add one.
- Its content is fixed by the spec: only the volatile residue — where the work stands, what the hand knows, what will slip first, what must not be resolved by inference — because everything durable already lives outside the conversation (buffer, files); never an inventory of the session. Each new snapshot supersedes the last by name, so a reader never follows a stale next action.
- The skill is bound by the reserved vocabulary: "memory snapshot" is the concept's name; "handoff" may stay where it already appears (the parenthetical, the first paragraph's "the handoff below"), since a memory snapshot is a handoff continuing this architect — the term "snapshot" must not be repurposed for anything else.

Out of scope, by the spec's own Blast radius: `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, `docs/paired-loop.md`, spec 117 (its pointer resolves against spec 123 as written). No `loads:` edge, no frontmatter change, no new file.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Widen the occasion

- [x] **Rework the handoff paragraph in § "Spawn once, message thereafter" to name both occasions**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the paragraph quoted in Context (the one beginning "Before a compact, the handoff continuing this same architect across it") so that it states, in this order and with these facts, wording the implementer's own:
  1. The memory snapshot continuing this same architect has two occasions: before a compact, and whenever the user asks for one mid-session. Keep the existing parenthetical "no other handoff has any reason to mention the buffer or the handle" attached to the artifact, not to the compact occasion — it stays true for both occasions.
  2. The on-request one is the architect's own capability, reached by a request rather than a command: no command is invoked and no template is consulted.
  3. Either occasion records the buffer's path "(defined in `architect-editor-engine`)" and a digest of what the editor has accumulated, followed **verbatim** by the digest clause: `the digest is your own recovery note and is never sent to the editor` — same characters, same position relative to "a digest of what the editor has accumulated;".
  4. What a snapshot carries: only the volatile residue — where the work stands, what the hand knows, what will slip first, and what must not be resolved by inference — because everything durable already lives outside the conversation; never an inventory of the session.
  5. Each new snapshot supersedes the last by name, so a reader never follows a stale next action.
  6. Close with the existing sentence unchanged: "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer."
  Guardrails: do not name a destination directory, a filename convention, or `command-handoff`; do not describe the buffer's zones or the drain rule (engine's, per 36.1); do not add a "what to record" list beyond the four residue items the spec names. Keep the paragraph as one prose paragraph in the section's existing register (no bullets, no headings). Follow the file's hard-wrap width (~76 columns). Do not touch the paragraphs before or after it — the "(see above)" and "as defined above" references in the spawn-moment paragraph, and the first paragraph's "the handoff below that carries your buffer's path", must still resolve to this reworked paragraph; confirm by reading, not by assumption.

### Identify the recovering artifact by what it is

- [x] **Reword the closing sentence of § "On every invocation"** (depends on the paragraph rework above — the name it uses must match)
  Files: `src/skills/agent-architect/SKILL.md`
  Change "and, if one exists, the pre-compact handoff that recorded your buffer's path" so it names the artifact rather than the occasion: the latest memory snapshot that recorded your buffer's path — written before a compact or on the user's request, either one recovers you the same way. Keep "if one exists" (spec 117 leans on this wording anticipating an architect that starts with nothing recorded — that claim must survive). Keep the sentence's opening ("You are re-invoked fresh after every compact and every new session — rebuild your working state from whatever the user hands you") unchanged.

### Verify against the file

- [x] **Confirm the invariants on the file, not on the diff** (depends on both edits)
  Files: `src/skills/agent-architect/SKILL.md`
  Run and read the results:
  - `grep -c "the digest is your own recovery note and is never sent to the editor" src/skills/agent-architect/SKILL.md` → exactly `1`.
  - `grep -c "pre-compact" src/skills/agent-architect/SKILL.md` → `0`. Today the string occurs exactly once, in the § "On every invocation" sentence this plan rewrites, so any hit after the edit is a leftover. (The liveness-fallback sentence's "an auto-compact that fired before any handoff was written" is a different string, describes an event rather than the artifact, and is untouched — it does not match this grep.)
  - `grep -n "command-handoff\|handoffs/" src/skills/agent-architect/SKILL.md` → no hits.
  - `grep -n "Of the recorded state, only the buffer's path travels" src/skills/agent-architect/SKILL.md` → exactly one hit, still inside the reworked paragraph.
  - `git diff --stat` → only `src/skills/agent-architect/SKILL.md`; frontmatter (`loads:`, `description:`) byte-identical; `wc -l` ≤ 500.
  - Read § "Your buffer is yours alone" once more and confirm it was not edited.
  Do not commit.

# Plan: 36.1 — the buffer's definition moves into the engine both halves load

## Context
Move the architect's buffer definition — path and numbering, the two zones and who holds each, re-read on change, the drain rule — out of `agent-architect` into `architect-editor-engine`, the engine both halves already load at birth; strip the two closed-to-the-editor claims from `agent-architect` and widen both callers' appositives (`agent-architect`, `editor.md`) so neither calls the engine a channel-message contract alone. Governing account: `docs/paired-loop.md` § "What the memory holds, and who holds it"; task spec: `.ai-factory/specs/trickster77777/116-buffer-definition-moves-into-the-engine.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Ground truth read for this plan
- `src/skills/architect-editor-engine/SKILL.md` is 30 lines: frontmatter (`description:` 488 chars, ending "Holds only the two formats; when-to-use policy stays with the caller. Loaded once at birth by both the architect (`src/skills/agent-architect`) and the editor (`src/agents/editor.md`)."), H1 "# Architect-Editor Engine — the Paired-Loop Channel-Message Contract", one load-once paragraph, then exactly two sections: "## The two channel-message formats" and "## The mode rule". The last sentence of "## The mode rule" reads "this engine holds only the two formats and the rule for telling them apart." No buffer, no zone, no path anywhere in the file.
- `src/skills/agent-architect/SKILL.md` names the buffer's path exactly once — `.ai-factory/notes/<NN>-architect-buffer.md`, in § "Your buffer is yours alone" — and it is the only file under `src/` or `docs/` naming that path. The same section's closing sentence carries the three clauses the spec dissects ("The editor is never told about it and no work-order references it — nothing is broken if it happens to see the file; it is the one file you edit directly, because it isn't a shared artifact."). § "Spawn once, message thereafter" holds the appositive ("— the shared channel-message-format contract —"), the handoff parenthetical ("since nothing outside this skill ever learns about either"), the "(below)" reference, and — untouched by this task, 36.2's boundary — the creation sentence "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet."
- `src/agents/editor.md` carries the appositive once, in its opening paragraph: "it is the shared channel-message-format contract for this pair and must be resident before you read anything sent to you." The word "buffer" appears 0 times in the file today.
- The phrase "channel-message-format contract" occurs in exactly three places under `src/`: `editor.md` (1), `agent-architect/SKILL.md` (1), the engine's `description:` (1). Nothing under `docs/`, `CLAUDE.md`, `README.md`, `AGENTS.md`, or `.ai-factory/ARCHITECTURE.md` uses it — those need no edit.
- `active/skills/architect-editor-engine`, `active/skills/agent-architect`, and `active/agents/editor.md` are already symlinks into `src/`; editing the sources is editing what `~/.claude` loads. No symlink work.
- The heading "Your buffer is yours alone" is addressed by name from specs 93, 116, and 119; it stays as-is (its surviving truth — the architect is the only writer, the live zone is the architect's alone — still holds).
- Seven buffer files `.ai-factory/notes/01..07-architect-buffer.md` exist; none is touched (spec § Blast radius). The working tree is clean at plan time.
- `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" gates a shared skill on content used by ≥ 2 callers; both halves load this engine, so the move conforms. `.ai-factory/RULES.md` does not exist.

## Scope fences — what this task does not do
Phase 36's later tasks own these; the engine and both callers must not gain any of them here:
- 36.2 — the buffer's creation moment and loading the engine at the architect's own start. The "Before that first channel-message" timing of the engine load and the creation sentence in § "Spawn once, message thereafter" stay word-for-word.
- 36.3 — the rule that no architect reads another's buffer / an editor reads only its own architect's. Not stated in the engine.
- 36.4 — how the editor learns the buffer's path at spawn. `editor.md` gains no path, no receiving account; the engine does not say how either half locates the file.
- 36.5 — the memory snapshot on request. § "On every invocation" untouched.
- 36.6 — when the architect writes to the buffer and the announce-on-change obligation. Neither the engine nor `agent-architect` states a write occasion, an entry form, or an announcement; `agent-architect` keeps naming the editor's handle, any pairing role, and deferral entries without labelling any with a zone.

## Tasks

### The engine gains the definition

- [x] **Widen the engine's frontmatter `description:`**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Replace the whole `description:` block (the `>-` folded scalar, all six lines) so it no longer says "Holds only the two formats". Target text (fold across lines as the current block does; keep it under 1024 chars — this is ~700):

  ```
  Shared contract for the architect↔editor paired loop, loaded once at birth by
  both the architect (`src/skills/agent-architect`) and the editor
  (`src/agents/editor.md`). Holds the two channel-message formats — REPORT-ONLY
  and APPLY-EDIT — with the rule that a receiver keys its mode strictly off the
  token that literally opens each message, and the definition of the
  architect's buffer the pair shares: its path and numbering, its settled zone
  held by both halves and its live zone held by the architect alone, the
  editor's re-read of the settled zone on change, and the drain rule that a
  ruling leaves the buffer once it reaches the artifact that should hold it.
  When-to-use policy stays with the caller.
  ```

  Every other frontmatter field (`name`, `user-invocable`, `disable-model-invocation`, `allowed-tools`) stays byte-identical. Register: the skill-description-field is one always-loaded layer — keep the description at the same abstraction level as its neighbours (what the engine holds and who loads it), no procedure.

- [x] **Widen every place the engine's body names itself** (depends on Widen the engine's frontmatter `description:`)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Three sites, no more:
  1. H1: `# Architect-Editor Engine — the Paired-Loop Channel-Message Contract` → `# Architect-Editor Engine — the Paired-Loop Contract: Channel-Messages and the Shared Buffer`.
  2. The load-once paragraph's first sentence: "…so the contract is resident before any channel-message arrives." → "…so the contract is resident before any channel-message arrives and the buffer's definition below is held by both halves from birth." The reverse-graph sentence that follows (the `grep -l` incantation) stays byte-identical.
  3. The closing sentence of "## The mode rule": "The full authoring and execution mechanics of each format stay with the callers; this engine holds only the two formats and the rule for telling them apart." → "The full authoring and execution mechanics of each format stay with the callers; this engine holds the two formats, the rule for telling them apart, and the buffer's definition below — when-to-use policy stays with the caller."

  "## The two channel-message formats" and the first two sentences of "## The mode rule" are untouched — the channel-message contract is not being edited, only the claim that it is all the file holds.

- [x] **Add the buffer section to the engine** (depends on Widen every place the engine's body names itself)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Append one new H2 after "## The mode rule", at the end of the file, in the file's existing register (prose paragraphs, one blank line between blocks; the file uses long single-line paragraphs, not hard-wrapped ones — match that). Heading: `## The architect's buffer`. It must state, and state only, the five things the spec assigns the engine — each derived from `docs/paired-loop.md` § "What the memory holds, and who holds it" (read it fresh before writing; take the meaning, do not paste the doc's paragraphs wholesale — the engine is the executable home, the doc is the governing spec; do not link the doc, since this skill loads in projects that do not carry it):

  1. **Path and numbering, named explicitly as this engine's home.** The buffer lives at `.ai-factory/notes/<NN>-architect-buffer.md` (backticked, exactly that string, the one being cut from `agent-architect`), numbered like the other temporary notes in that directory so several architects coexist without colliding; say in so many words that this engine is the home of the path and the numbering and the architect's own skill points here rather than restating them.
  2. **The two zones and what each holds.** The **settled** zone — the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice. The **live** zone — the editor's handle, the architect's current read of an open question, a diagnosis still forming. Use the words "settled" and "live" (bolded on first use, as the governing spec does); these are the names 36.3–36.6 and the buffer files on disk already use.
  3. **Which zone the editor holds, and why the live zone stays private.** The settled zone is held by both halves — the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating discipline. The live zone is the architect's alone, with the reason: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted, and an independent reading is the only reason to ask for one.
  4. **Re-read on change.** The editor re-reads the settled zone when it changes, not once at birth.
  5. **The drain rule.** A ruling recorded in the buffer is a debt against the skill, not a record of one; it leaves the buffer when it reaches the artifact that should hold it — without that drain the buffer accumulates decisions everyone follows and no artifact states.

  A worked draft the implementer may use verbatim or tighten (meaning pinned, wording free):

  ```
  ## The architect's buffer

  The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering; the architect's own skill points here rather than restating them.

  The buffer has two zones, and the split is load-bearing. The **settled** zone — the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice — is held by both halves: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time. The **live** zone — the editor's handle, the architect's current read of an open question, a diagnosis still forming — is the architect's alone: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted, and an independent reading is the only reason to ask for one.

  The editor re-reads the settled zone when it changes, not once at birth.

  A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states.
  ```

  Guards (see "Scope fences" above): no sentence about when the buffer is created or by whom, no isolation rule between architects, no account of how the editor learns the path, no write occasion, no announce obligation, no snapshot. Do not name deferral entries — `agent-architect` keeps that, unlabelled by zone. Do not state who writes the file — that reason stays in `agent-architect` (next phase of this plan). Body stays far under 500 lines.

### The architect points at the engine

- [x] **Widen `agent-architect`'s appositive and load-reason** (depends on Add the buffer section to the engine)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", second paragraph, replace the whole paragraph (wrapped at the file's ~76-column width like its neighbours):

  Current:
  ```
  Before that first channel-message, also make sure `architect-editor-engine`
  — the shared channel-message-format contract — is loaded once this session
  via the `Skill` tool, if it is not already loaded: the contract must be
  resident before a `REPORT-ONLY` or `APPLY-EDIT` message is ever composed.
  ```
  New:
  ```
  Before that first channel-message, also make sure `architect-editor-engine`
  — the shared contract holding the two channel-message formats and your
  buffer's definition — is loaded once this session via the `Skill` tool, if
  it is not already loaded: it must be resident before a `REPORT-ONLY` or
  `APPLY-EDIT` message is ever composed, and it is where your buffer's path,
  zones, and rules are defined.
  ```
  The opening "Before that first channel-message" timing is 36.2's to move — keep it exactly. The § "Relay on the marker; author a prompt in exactly one case" parenthetical "(the format is `architect-editor-engine`'s, loaded once at birth — see "Spawn once, message thereafter")" is a claim about the format, still true — leave it.

- [x] **Narrow the handoff parenthetical and reword "(below)"** (depends on Widen `agent-architect`'s appositive and load-reason)
  Files: `src/skills/agent-architect/SKILL.md`
  Same section, third paragraph. Two changes inside one sentence, nothing else in the paragraph changes (the digest clause "is your own recovery note and is never sent to the editor" and the "Of the recorded state, only the buffer's path travels…" sentence stay byte-identical):
  1. Drop the justification. `— no other handoff has any reason to mention the buffer or the handle, since nothing outside this skill ever learns about either —` → `— no other handoff has any reason to mention the buffer or the handle —`. The surviving rule is the narrowed one: no *other* handoff mentions them; the "nothing outside this skill ever learns" reason is false once the editor holds the settled zone.
  2. Reword the reference that would otherwise point at a pointer. `records your buffer's path (below)` → `records your buffer's path (defined in `architect-editor-engine`)` — the parenthetical now names where the path is, not a section this task empties of it.

  Re-wrap the paragraph to the file's width after the edit. The fourth paragraph — "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet." and everything after it in that paragraph — is 36.2's boundary: byte-identical.

- [x] **Turn § "Your buffer is yours alone" into a pointer** (depends on Narrow the handoff parenthetical and reword "(below)")
  Files: `src/skills/agent-architect/SKILL.md`
  Heading unchanged (addressed by name from specs 93, 116, 119). First paragraph: change only the opening words `Keep one private buffer file` → `Keep one buffer file` — "private" is the same closed-to-the-editor claim in a third wording, and after this task the settled zone is held by both; the rest of the paragraph (what survives a compact, the pointer-never-a-copy rule, the cross-reference to "Spawn once, message thereafter") stays byte-identical.

  Second paragraph: keep its first sentence byte-identical (`Each deferral entry names *what*, *why deferred*, and the *trigger* that resolves it; delete an entry once it's done — deferral entries remain the buffer's primary content.`) and replace everything after it — the path sentence and the three-clause closing sentence — with:

  ```
  The buffer's path and numbering, its two zones and what each holds, the
  editor's re-read of the settled zone, and the drain rule are
  `architect-editor-engine`'s, loaded at birth — this section points there
  and restates none of them. It is the one file you edit directly: you are
  its only writer.
  ```

  What this does, clause by clause, per the spec: the path `.ai-factory/notes/<NN>-architect-buffer.md` leaves this file (the engine is now its only home under `src/`); "The editor is never told about it and no work-order references it" and "nothing is broken if it happens to see the file" go; "it is the one file you edit directly" survives with its reason swapped from "because it isn't a shared artifact" to the narrower, still-true "you are its only writer". The pointer names the engine's contents so a reader knows what it will find there, but restates no zone content, no re-read rule, no drain rule. The editor's handle, the pairing role, and deferral entries stay named in this section with no zone label. Re-wrap to the file's width.

### The editor's appositive

- [x] **Widen `editor.md`'s appositive and load-reason** (depends on Add the buffer section to the engine)
  Files: `src/agents/editor.md`
  One clause in the opening paragraph; nothing else in the file changes — not the frontmatter `description:`, not any section, and no new section or rule. Replace:

  ```
  load `architect-editor-engine` via the `Skill` tool — it is the shared
  channel-message-format contract for this pair and must be resident before
  you read anything sent to you.
  ```
  with (re-wrapped to the file's width):
  ```
  load `architect-editor-engine` via the `Skill` tool — it is the shared
  contract for this pair, holding the two channel-message formats and the
  definition of the architect's buffer, whose settled zone you hold as your
  own working context from birth, and it must be resident before you read
  anything sent to you.
  ```
  The file names the buffer by the engine's word — "buffer" — and its zone by the engine's word — "settled"; it gains no path, no account of how the path reaches it, and no recovery account (36.4's). "from birth" is the widened load-reason the spec asks for: holding the settled zone is not triggered by any arriving message, so the engine's residency cannot wait for one.

### Verify

- [x] **Verify by grep and by diff** (depends on Turn § "Your buffer is yours alone" into a pointer, Widen `editor.md`'s appositive and load-reason)
  Files: `src/skills/architect-editor-engine/SKILL.md`, `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`
  All of the following must hold; report the actual command output, not "looks good":
  - `grep -rn "channel-message-format contract" src docs` → 0 hits.
  - `grep -rn "olds only the two formats\|holds only the two formats" src` → 0 hits.
  - `grep -rn "never told about it\|nothing outside this skill\|isn't a shared artifact\|happens to see the file\|path (below)\|one private buffer" src` → 0 hits.
  - `grep -rn "architect-buffer.md" src docs` → exactly one hit, in `src/skills/architect-editor-engine/SKILL.md`.
  - `grep -c "^## " src/skills/architect-editor-engine/SKILL.md` → 3; the third H2 is `## The architect's buffer`; the words "settled", "live", "re-read", and "debt against the skill" each appear in it; within that section the words "create", "spawn", "another's", "announce", and "snapshot" do not appear (scope fences; "spawn" legitimately appears once earlier, in the load-once paragraph).
  - `grep -n "buffer" src/agents/editor.md` → hits only inside the opening paragraph's one edited clause; `grep -c "notes/" src/agents/editor.md` → 0.
  - The engine's `description:` scalar is under 1024 chars (`sed -n '/^description:/,/^user-invocable/p' … | wc -c`); `name: architect-editor-engine` unchanged; the H1 and the `grep -l` reverse-graph sentence are as pinned above.
  - In `agent-architect`: the sentence beginning "At the moment you spawn the editor" is byte-identical to HEAD (`git diff HEAD -- src/skills/agent-architect/SKILL.md` shows no hunk touching it); the paragraph beginning "Before that first channel-message" still opens with those words; "the pre-compact handoff that recorded your buffer's path" in § "On every invocation" is untouched; the editor's handle, the pairing role, and deferral entries are still named in § "Your buffer is yours alone" and none carries the word "zone" beside it.
  - `git status --short` lists exactly the three files above as modified and nothing else — no buffer note under `.ai-factory/notes/`, no `active/` change, no doc change.
  - Read each of the three edited paragraphs back whole for wrap and grammar; a sentence broken mid-word by a re-wrap is a defect.

# Plan: 36.2 — the buffer's creation is conditional, and it moves to the architect's own start

## Context
Move the buffer's coming-into-being out of `agent-architect`'s spawn-moment sentence and into the architect's own start, as a conditional: a memory snapshot naming a buffer means the architect works in that buffer; no such pointer means the architect creates one first, before any editor exists. Loading `architect-editor-engine` becomes part of that same start, ahead of creating the buffer, because after 36.1 the buffer's path and numbering live in the engine. Governing account: `docs/paired-loop.md` § "How the memory begins, and how it survives"; task spec: `.ai-factory/specs/trickster77777/117-buffer-exists-from-the-architects-start.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Ground truth read for this plan
- `src/skills/agent-architect/SKILL.md` is 253 lines, hard-wrapped at ~76 columns. § "Spawn once, message thereafter" holds, in order: (1) the opening paragraph — "Until the first channel-message arrives, you work alone on the unit named and tell the user you are working alone until it exists. The first channel-message is the spawn — … and its content *is* the spawn prompt; there is no spawn before one exists. Spawn the editor with `Agent` on that first channel-message …"; (2) the engine-load paragraph — "Before that first channel-message, also make sure `architect-editor-engine` — the shared contract holding the two channel-message formats and your buffer's definition — is loaded once this session via the `Skill` tool, if it is not already loaded: it must be resident before a `REPORT-ONLY` or `APPLY-EDIT` message is ever composed, and it is where your buffer's path, zones, and rules are defined."; (3) the handoff paragraph — "Before a compact, the handoff continuing this same architect across it … records your buffer's path (defined in `architect-editor-engine`) …"; (4) the spawn-moment paragraph — opening "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet." and continuing with the `name:` parameter and the pairing-role recording moment; (5) the liveness/recovery paragraph with the `agent-<id>.meta.json` fallback; (6) the dead-editor paragraph.
- The 36.1 commit (`4eb7b0c`) has landed: the engine `src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" is the home of the path `.ai-factory/notes/<NN>-architect-buffer.md` and its numbering ("This engine is the home of that path and that numbering; the architect's own skill points here rather than restating them."). `agent-architect` no longer names the path anywhere — creation can therefore be stated against "the path and numbering the engine defines" without restating either.
- The phrase "if it does not exist yet" and the sentence "Until the first channel-message arrives, you work alone" occur only in `agent-architect/SKILL.md` — nothing under `src/`, `docs/`, or the repo's CLAUDE.md files quotes them, so no cross-file reference goes stale.
- The section name "Spawn once, message thereafter" is addressed by name from three places inside the same file (the intro paragraph, § "Relay on the marker…" parenthetical "loaded once at birth — see "Spawn once, message thereafter"", and § "Your buffer is yours alone"). The heading stays; the engine load stays inside that section, so the "loaded once at birth" pointer remains true.
- `docs/paired-loop.md` § "How the memory begins, and how it survives" is the governing spec for this task: "The memory exists before the hands do."; a head from a **memory snapshot** naming a buffer "works in the buffer it names — the same memory, resumed, not a new one under an old name"; a head "with no such pointer is a new head: it creates its own buffer first, and only then takes on a hand." — the doc is not edited (docs → roadmap → code; the doc is already ahead).
- `active/skills/agent-architect` is a symlink into `src/`; editing the source is editing what `~/.claude` loads. No symlink work.
- The review of 36.1 left no deferred observations addressed at this task. The working tree is clean at plan time. `.ai-factory/RULES.md` does not exist.

## Scope fences — what this task does not do
- 36.4 will attach a path-giving clause to the handle-writing clause of the spawn-moment sentence. This task keeps the words `write its handle into the buffer` intact as that anchor and removes only the `creating the buffer at its existing path if it does not exist yet` clause. The sentence "The first channel-message is the spawn — … its content *is* the spawn prompt; there is no spawn before one exists." stays word-for-word (36.4 widens it).
- 36.5 reworks the handoff paragraph's occasion ("Before a compact, the handoff continuing this same architect…") and § "On every invocation" ("the pre-compact handoff that recorded your buffer's path"). Both stay byte-identical here. The new start paragraph names the pointer by the governing spec's term — "a memory snapshot naming a buffer" — and bridges it in one appositive to the artifact this file already describes, "the handoff below that carries your buffer's path", so a reader knows the two words name one artifact. It ties the pointer to that *artifact*, never to a *compact* or to "pre-compact": 36.5 widens the occasions the handoff is written on and reworks § "On every invocation" to name the artifact rather than the occasion — it does not stop the handoff being the carrier of the buffer's path, so the bridge survives 36.5 unchanged.
- 36.3 (no architect reads another's buffer) and 36.6 (write occasions, announce obligation) — nothing about them is stated; the engine is not edited at all.
- The buffer's shape, its zones, the path, and the numbering are the engine's (36.1) and are not restated — creation names "the path and numbering `architect-editor-engine` defines", nothing more.
- The `agent-<id>.meta.json` recovery fallback, the liveness test, the dead-editor paragraph, the `name:` parameter clause, and the pairing-role recording moment are untouched.
- `docs/paired-loop.md`, `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, the roadmap, and the buffer files under `.ai-factory/notes/` are not edited.

## Tasks

### The architect's own start

- [x] **Open § "Spawn once, message thereafter" with the architect's start: engine first, then the conditional buffer**
  Files: `src/skills/agent-architect/SKILL.md`
  Insert one new paragraph as the first paragraph of the section, directly under the `## Spawn once, message thereafter` heading and before "Until the first channel-message arrives…". It must state, in this order and in the file's own second-person register, hard-wrapped at the file's ~76-column width:
  1. The start comes before any editor exists.
  2. Step one — load `architect-editor-engine` via the `Skill` tool if it is not already loaded this session; give its reason as the one the current engine-load paragraph gives (the contract holding the two channel-message formats and your buffer's definition; where your buffer's path, zones, and rules are defined) and state that it is loaded *ahead of* the buffer because the buffer's path lives there — and that, being resident from the start, it is in place long before a `REPORT-ONLY` or `APPLY-EDIT` message is ever composed. The load moment is the start, not a deadline somewhere before the first channel-message.
  3. Step two — the buffer, conditional: a memory snapshot naming a buffer — bridged, in one appositive, to the handoff below that carries your buffer's path, since the file calls that artifact "handoff" everywhere else and never "snapshot"; without the bridge an architect handed a pre-compact handoff naming a buffer would not recognise it as the pointer and would fork the memory under a new number — means you work in that buffer (the same memory resumed, never a new one under an old name); no such pointer means you are a new architect and create your own buffer first, at the path and numbering the engine defines. Either way the buffer exists before any editor does.

  A worked draft the implementer may use verbatim or tighten (meaning pinned, wording free):

  ```
  Your own start comes before any editor exists, and it has two steps in a
  fixed order. First, make `architect-editor-engine` — the shared contract
  holding the two channel-message formats and your buffer's definition —
  resident via the `Skill` tool, if it is not already loaded this session:
  it is where your buffer's path, zones, and rules are defined, so it is
  loaded ahead of the buffer, and being resident from your start it is in
  place long before a `REPORT-ONLY` or `APPLY-EDIT` message is ever
  composed. Second, the buffer — and which of two starts this is decides
  what you do: a memory snapshot naming a buffer — the handoff below that
  carries your buffer's path — means you work in that buffer, the same
  memory resumed, never a new one under an old name; no such pointer means
  you are a new architect and create your own buffer first, at the path
  and numbering the engine defines. Either way the buffer exists before
  any editor does.
  ```

  Guards: do not name the path `.ai-factory/notes/<NN>-architect-buffer.md` or the numbering rule (the engine's home); do not name a zone, a write occasion, an announcement, or an isolation rule; do not say which occasion writes the snapshot or call it "pre-compact" (36.5's surface) — the bridge names the artifact ("the handoff below that carries your buffer's path"), not the occasion. Call the architect "architect" or "you" and the editor "editor" or "hand" — the file's own names; do not introduce "head" as a name for the architect (`reserved-words.md` fixes `architect`, and the file uses "head" nowhere). Do not link `docs/paired-loop.md` — the skill loads in projects that do not carry it.

- [x] **Reword the "work alone" opening so holding the buffer is not the opposite of working alone** (depends on Open § "Spawn once, message thereafter" with the architect's start)
  Files: `src/skills/agent-architect/SKILL.md`
  In the paragraph now second in the section, change only its first sentence. Current: `Until the first channel-message arrives, you work alone on the unit named and tell the user you are working alone until it exists.` New meaning: alone means *without a hand*, not without state — the architect already holds its buffer. "hand" is already the file's figure for the editor's role (its intro paragraph); "head" is not a name the file uses for the architect and must not be introduced here. Draft:

  ```
  Until the first channel-message arrives, you work alone — holding your
  buffer, no editor's hand yet — on the unit named and tell the user you
  are working alone until it exists.
  ```

  Every following sentence of that paragraph — from "The first channel-message is the spawn —" through "it catches what you miss." — stays byte-identical (36.4's anchor lives there). Re-wrap only the edited sentence's lines.

- [x] **Delete the now-absorbed engine-load paragraph** (depends on Reword the "work alone" opening)
  Files: `src/skills/agent-architect/SKILL.md`
  Remove the whole paragraph beginning `Before that first channel-message, also make sure `architect-editor-engine`` and ending `and it is where your buffer's path, zones, and rules are defined.` — every fact in it (which tool, load-once-if-not-loaded, what the engine holds, resident before a message is composed, home of the path/zones/rules) now lives in the start paragraph, and keeping both would state the load moment twice with two different timings. Leave exactly one blank line between the surrounding paragraphs. The handoff paragraph that follows ("Before a compact, the handoff continuing this same architect across it …") is byte-identical — 36.5's surface.

### The spawn moment writes into a buffer that exists

- [x] **Shorten the spawn-moment sentence to the handle write alone** (depends on Delete the now-absorbed engine-load paragraph)
  Files: `src/skills/agent-architect/SKILL.md`
  In the spawn-moment paragraph, replace only its first sentence. Current: `At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet.` New:

  ```
  At the moment you spawn the editor (see above), write its handle into the
  buffer — a write into a file that exists by then, whichever of the two
  starts above you came through.
  ```

  Use a neutral verb for the start as drafted — a resumed architect does not *produce* the buffer, it finds the one the snapshot names; the clause states only that the file exists by the spawn moment.

  The words `write its handle into the buffer` must survive verbatim — 36.4 attaches its path-giving clause to that anchor. Everything after that sentence in the paragraph — the `Agent` `name:` parameter clause and the pairing-role recording moment with its `architect-pairing-engine` load — stays byte-identical. Re-wrap only the edited sentence's lines.

- [x] **Verify the section reads as one sequence and nothing outside it moved** (depends on Shorten the spawn-moment sentence to the handle write alone)
  Files: `src/skills/agent-architect/SKILL.md`
  Read § "Spawn once, message thereafter" top to bottom fresh and confirm the order is: start (engine → conditional buffer) → work alone until the first channel-message / spawn → handoff paragraph → spawn-moment (handle write into an existing buffer, `name:`, pairing role) → liveness/recovery → dead editor. Then check by grep: `if it does not exist yet` occurs 0 times in the file; `Before that first channel-message` occurs 0 times; `write its handle into the buffer` occurs exactly once; the start paragraph names `handoff` at least once, in the same sentence as `memory snapshot` (the bridge to the artifact the file already describes is in place); `head` as a name for the architect occurs 0 times in the file; `architect-editor-engine` still appears in the section (so the "loaded once at birth — see "Spawn once, message thereafter"" pointer in § "Relay on the marker…" resolves); the path `.ai-factory/notes/<NN>-architect-buffer.md` occurs 0 times in `agent-architect` (still the engine's alone); `git diff --stat` touches only `src/skills/agent-architect/SKILL.md`; frontmatter is byte-identical; body stays far under 500 lines. Fix anything the check turns up in place; do not commit.

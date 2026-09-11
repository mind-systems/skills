# Plan: 40.1 — the buffer section's heading and opening clause name what it now holds

## Context
`src/skills/agent-architect/SKILL.md`'s buffer section still opens with a heading ("## Your buffer is yours alone") and a first sentence ("Keep one buffer file for whatever of your own state must survive a compact: …") that describe the file as private, architect-only compact-survival state — while the same section's second paragraph already has the editor holding part of it ("When the memory the hand holds moves, you name the change to the editor…"), and `architect-editor-engine` (loaded at birth, pointed to from this very section) defines the settled zone as held by both halves. This task brings the heading and the opening clause into line with what the section already says below them, keeping the one still-true claim — the architect is the buffer's only *writer* — and rewrites the single by-name reference to the old heading elsewhere in the same file.

Grounded read (fresh): the section spans from `## Your buffer is yours alone` to the line before `## The user rules the forks and owns the commits`. Its closing sentence already states the writer fact: "It is the one file you edit directly: you are its only writer." The only other site naming the heading is the rescoped-inventory paragraph in "Relay on the marker; author the apply work-order and your own legwork": `(see "Your buffer is yours alone")`. `grep -rn "yours alone" src/ docs/` returns only these two lines — `editor.md`, `architect-editor-engine/SKILL.md`, and `docs/paired-loop.md` never name this heading.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the section's opening

- [x] **Rename the buffer section's heading to name the shared memory and the sole writer**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the heading `## Your buffer is yours alone` with a heading that no longer claims the buffer as the architect's private property but still carries the load-bearing truth that the architect alone writes it — e.g. `## Your buffer is shared; you alone write it` (the implementer may choose equivalent wording; the heading must (a) drop the "yours alone" possession claim, (b) state or clearly imply that the editor holds part of it / it is the pair's memory, and (c) keep the sole-writer fact). Use the reserved vocabulary where it applies (the engine and `docs/paired-loop.md` call it "the architect's buffer", "the pair shares one working memory"; the two zones are "settled" and "live"). Do not restate the zone definitions — those are `architect-editor-engine`'s; the section already says it "points there and restates none of them".

- [x] **Rewrite the opening clause so it stops framing the whole file as architect-only compact-survival state** (depends on heading rename)
  Files: `src/skills/agent-architect/SKILL.md`
  Rewrite only the first sentence of the section's first paragraph ("Keep one buffer file for whatever of your own state must survive a compact: the editor's handle, any pairing role the user has assigned for the session, and the deferral entries below."). The new opening must:
  - Present the buffer as the pair's memory of which the architect is the only writer (the editor holds and re-reads the settled zone; the live zone is the architect's alone — refer to the engine by name, per the section's existing pointer, rather than redefining zones).
  - Still list what the architect keeps there: the editor's handle, any pairing role the user has assigned for the session, and the deferral entries below.
  - Still tie the deferral entries and the recorded items (handle, role) to survival across a compact — that part is unchanged and stays true; what changes is that survival-across-a-compact is no longer the *whole* description of what the file is.
  Leave the remainder of the first paragraph intact ("The memory snapshot continuing you carries this buffer's path alone: … this section does not restate any of that.") — it is correct and is not in scope. Make sure the rewritten sentence still reads continuously into that remainder.
  Guardrails — nothing else in the section moves: not the second paragraph (occasion-and-form, including the announce-obligation "When the memory the hand holds moves, you name the change to the editor in the same act as the write"), not the third paragraph (deferral-entry format, the pointer to `architect-editor-engine`, and the closing "It is the one file you edit directly: you are its only writer."). No other section of the file, no other file.

### Move the by-name reference with the name

- [x] **Update the rescoped-inventory paragraph's reference to quote the new heading verbatim** (depends on heading rename)
  Files: `src/skills/agent-architect/SKILL.md`
  In the section "Relay on the marker; author the apply work-order and your own legwork", the sentence `Keeping the hand current — naming that the shared memory has moved (see "Your buffer is yours alone"), or handing it the buffer's path at spawn (see "Spawn once, message thereafter") — …` quotes the old heading. Replace the quoted string with the new heading's exact wording (byte-identical to the heading text after `## `), so the reference moves with the name. Change nothing else in that sentence or paragraph.
  After editing, verify with `grep -n "yours alone" src/skills/agent-architect/SKILL.md` that the old heading text no longer appears anywhere in the file, and `grep -rn "yours alone" src/ docs/` that no other file needs touching (expected: no hits). Confirm the SKILL.md body stays ≤ 500 lines.

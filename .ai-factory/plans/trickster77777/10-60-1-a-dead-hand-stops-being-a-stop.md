# Plan: 60.1 — a dead hand stops being a stop

## Context
Right now, when the editor dies, `agent-architect` treats it as a stop. The death is reported before anything is sent onward, an undelivered payload is never replayed, and the respawn waits for the user to re-phrase or resend. This task replaces that passage in `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" with the wording pinned in the task spec `.ai-factory/specs/trickster77777/167-a-dead-hand-stops-being-a-stop.md` § "What must be true after". Under the new wording, the death is named in passing, the next channel-message is the new spawn, permission is standing, and the next order must be self-contained. Governing spec: `docs/paired-loop.md` § "How the memory begins, and how it survives" ("What a fresh hand costs is context, not permission: …"). Phase note: `.ai-factory/specs/trickster77777/166-a-dead-hand-is-remade-without-a-pause.md`.

Ground truth checked before planning:
- The target is the last paragraph of § "Spawn once, message thereafter". It opens "If the send fails, the editor is dead: report to the user **before anything" and ends "Losing the editor is never fatal; losing / it silently is the defect." It sits directly before the `## Relay on the marker; author the apply work-order and your own legwork` heading.
- The paragraph above it, "Leaving both buffers live — …", quotes "Losing the editor is never fatal; losing it silently is the defect". The new wording keeps that sentence verbatim, so the quote stays accurate. The paragraph before that one ends "the rule below for a dead editor governs". That is a generic pointer and stays correct.
- I swept `src/` and `docs/` for the phrases this task removes ("sent onward", "auto-replayed", "self-contained per round", "eager with authored", "resent as-is", "warm context", "respawn"). They occur only in the target passage. `src/agents/editor.md` has no "dead"/"respawn" language, which confirms the spec's claim that editor.md is untouched.
- `.ai-factory/notes/01-architect-buffer.md` also matches the spec's sweep. It is another architect's buffer and is out of scope; do not touch it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Replace the dead-editor passage

- [x] **Replace the dead-editor paragraph with the spec's wording**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", replace the whole final paragraph with the replacement block in the task spec § "What must be true after". The old paragraph runs from "If the send fails, the editor is dead: report to the user **before anything" through "it silently is the defect.". Copy the replacement verbatim. Strip only the leading `> ` from each line and keep the spec block's line breaks exactly as they are; do not rewrap. The paragraph should read, line for line:
  ```
  If the send fails, the editor is dead: this is never a stop and never a
  question — the hand is your own, and permission to make a new one is
  standing, not asked for. Name the death in passing, in the same act as
  the next channel-message, which is the new spawn: never withheld, never
  delayed waiting on the user's word. What a fresh hand costs is context,
  not permission — it holds none of the accumulated round history a live
  one had, so the next order you compose **must be** self-contained in its
  own right: pin the values, paths, and anchors a warmed-up hand would
  have carried, the same way a first spawn already must. Losing the
  editor is never fatal; losing it silently is the defect.
  ```
  (Leave out the code-fence lines and the two-space list indent. Each line starts at column 1 in the file.)
  - Keep the bold on `**must be**`. The spec explains that it is deliberate.
  - The spec's line breaks keep `editor is never fatal; losing it silently is the defect.` on a single line. The blast-radius check below depends on that.
  - Keep exactly one blank line before the paragraph and one before the `## Relay on the marker…` heading that follows it.
  - Change nothing else in the file. That includes the "Leaving both buffers live" paragraph, the liveness-probe paragraph ("the rule below for a dead editor governs"), the frontmatter, and every other section.

### Blast-radius confirmation

- [x] **Run the spec's sweep and confirm what survives** (depends on Replace the dead-editor paragraph with the spec's wording)
  Files: none edited (read-only)
  1. File-level sweep, excluding this pipeline's own working artifacts, which quote the phrases on purpose:
     `grep -rln --exclude-dir=plans --exclude-dir=plan-reviews --exclude-dir=reviews "sent onward\|auto-replayed\|editor is never fatal" src/ docs/ .ai-factory/`
     Expect exactly these files:
     - `src/skills/agent-architect/SKILL.md`
     - `.ai-factory/roadmaps/trickster77777.md`
     - `.ai-factory/specs/trickster77777/167-a-dead-hand-stops-being-a-stop.md`
     - `.ai-factory/specs/trickster77777/166-a-dead-hand-is-remade-without-a-pause.md`
     - `.ai-factory/notes/01-architect-buffer.md`
     Every file other than `SKILL.md` either records history or is another architect's buffer. Leave them untouched. Also leave this task's own plan, plan-review, and review files under `.ai-factory/plans|plan-reviews|reviews/trickster77777/10-60-1-…` untouched; they are excluded above because they quote the phrases.
  2. Per-occurrence check on the target:
     `grep -n "sent onward\|auto-replayed\|editor is never fatal" src/skills/agent-architect/SKILL.md`
     Expect exactly two lines, both matching "editor is never fatal": one inside the "Leaving both buffers live" paragraph, and one as the last line of the new paragraph. Neither "sent onward" nor "auto-replayed" should remain.
  3. Run `git diff --stat -- src/ docs/`. Expect only `src/skills/agent-architect/SKILL.md` to be listed, with no change to `src/agents/editor.md`.

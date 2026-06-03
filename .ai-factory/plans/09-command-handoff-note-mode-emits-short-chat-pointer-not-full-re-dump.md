# Plan: command-handoff: note mode emits short chat pointer, not full re-dump

## Context
In note mode the command-handoff skill currently dumps the full handoff into chat AND writes it to the note file — re-bloating the context the user is about to `/compact`. This milestone makes note mode emit only a short paste-back pointer to chat while the file keeps the full handoff.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite note-mode output

- [x] **Task 1: Rewrite Step 3 Note-mode block to emit a chat pointer instead of a full re-dump**
  Files: `src/commands/command-handoff.md`
  In Step 3 (lines ~108–120), replace the "Note mode: Do both of the following" block. New behavior:
  - Reorder so the file write comes first conceptually: write the full handoff to the note file (keep existing sub-steps a–c verbatim — `ls .ai-factory/handoffs/`, find highest `<NN>`, derive semantic `<slug>`, Write the handoff body verbatim to `.ai-factory/handoffs/<NN>-<slug>.md`).
  - Then emit to chat **only a short pointer**: the written note path plus a 3–5 line orientation (the one-sentence frame from section 1 + the next step from section 4; optionally the count of work-units covered). Explicitly state: **do not** re-emit the full handoff body to chat — the file holds it.
  - Make the pointer **paste-back-able**: phrased so the user can drop it into the next session to point the fresh agent at the full note.
  - Fold the old sub-step (d) "report the path … as a one-line confirmation" into the pointer so the path confirmation is part of the pointer, not an addition to a full dump.
  - Leave Chat mode (line ~106) unchanged.

- [x] **Task 2: Scope the self-check gate to the file, not the chat pointer** (depends on Task 1)
  Files: `src/commands/command-handoff.md`
  Adjust the Step 2 self-check note (the line ~100 ending "This gate applies in both chat mode and note mode."). Clarify that the proportionality/completeness gate applies to the handoff **content written to the note file**; in note mode the **chat pointer is intentionally minimal regardless of session size** and is exempt from the proportionality gate. Keep the gate fully applicable to chat mode's chat output.

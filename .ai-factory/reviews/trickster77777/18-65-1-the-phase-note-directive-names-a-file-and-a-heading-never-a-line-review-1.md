## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-outline-deep/SKILL.md`). The plan, its JSON sidecar and the plan-review are orchestrator artifacts. `.ai-factory/notes/07-architect-buffer.md` is also changed, but by the architect, not by this task.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. This is a one-bullet prose edit inside a lens skill's body. No `loads:` edge changes, and no engine is touched. `note` still receives the directive as free text through its verbosity hook, as `src/skills/note/SKILL.md` defines it.
- **Rules:** OK. There is no `.ai-factory/RULES.md` convention this could violate. The new sentence follows the global CLAUDE.md § "Grounding claims" reference rule and `docs/reference-by-name.md` ("A `file:line` reference is a defect report against its target").
- **Roadmap:** OK. The change matches contract line 65.1 in `.ai-factory/roadmaps/trickster77777.md` and its task spec `180-the-phase-note-directive-names-a-file-and-a-heading-never-a-line.md`.
- **Working tree (WARN, non-blocking):** `.ai-factory/notes/07-architect-buffer.md` is staged. It is the architect's buffer, where the head writes and this task never does, and its change is not part of this task's diff. Whoever commits should know it sits in the same index.

### Critical Issues
None.

- The new bullet matches the spec's "What must be true after" sentence word for word: "short: a few sentences more than the preamble, grounded in the docs and code read at Step 0 — a claim that rests on a file names the file and the heading, symbol or quoted fragment that holds it, never a line number — and never a transcript of the conversation."
- The bold lead-in `**Verbosity directive**` and its dash are unchanged. The continuation lines keep the two-space indent the sibling bullets use.
- The wrap keeps the file's column. The longest new line is 85 characters, and the sibling **Destination directory**, **Template** and re-run-rule lines run up to the same width.
- Nothing else in the file changed. The re-run rule ("the template and verbosity directive above") names the directive, so it picks up the new sentence with no edit.
- Sweep: `grep -rn "file:line" src/ docs/ CLAUDE.md` no longer reaches `roadmap-outline-deep`. Every remaining hit is one the spec's **Finding** lists: the `command-pin-gaps` walk paragraph and the `roadmap-prune` handoff item, which 65.4 and 65.3 own; the `command-pin-gaps` scan line; the global CLAUDE.md; `docs/reference-by-name.md`; `docs/counts-go-stale.md`; and the root CLAUDE.md index row. `grep -rn "erbosity directive" src/ docs/` reaches only the new bullet, the re-run rule, `note`'s hook, and the unrelated directives in `command-handoff` and `task-rescue`. No caller depends on the old wording.

### Positive Notes
- The edit is minimal and exact, with no collateral rewording.
- The new clause keeps the old one's reach ("where a claim needs one" becomes "a claim that rests on a file"). A statement about the user's rulings, or about something that is absent, can still stand without a source, as the spec intends.

REVIEW_PASS

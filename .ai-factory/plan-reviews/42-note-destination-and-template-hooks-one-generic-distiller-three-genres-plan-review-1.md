## Code Review Summary

**Files Reviewed:** 1 plan (targets `src/skills/note/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Spec (`.ai-factory/notes/53-note-destination-template-hooks.md`)** — PASS. The plan is a faithful, complete decomposition of the spec's three edits. Every spec clause maps to a task:
  - Edit 1 (destination hook) → Task 1 (introduce) + Task 2 (thread through Steps 3–4 and Note File Handling).
  - Edit 2 (template hook) → Task 1 (introduce) + Task 3 (thread through Step 3).
  - Edit 3 (frontmatter/description) → Task 3.
  - Constraints (byte-identical standalone, load-once unchanged, no rename, default stays `.ai-factory/notes/`, no genre content in `note`) are all restated in the tasks and the implementer notes.
- **Roadmap (`ROADMAP.md:95`)** — PASS. The milestone line matches: mechanism stays, destination + template become caller-supplied hooks, unset → today's defaults, callers adopt in their own tasks (notes 54/55), no genre content, no rename, load-once unchanged. Plan does not touch callers, matching the roadmap's "callers adopt the hooks in their own tasks."
- **Architecture (`ARCHITECTURE.md:30` — Composition: mechanism vs policy)** — PASS. The split is exactly the engine/policy separation the doc mandates: `note` keeps mechanism (mining, `<NN>` numbering, slug, placement, concision, English); destination and template become the callers' policy. No new router-only skill is created; content stays in the one engine.

### Critical Issues

None.

### Codebase Verification

Confirmed against the actual `src/skills/note/SKILL.md`:
- Section names the plan edits all exist and are named correctly: Step 3 "Save Note to File" (line 33), Step 4 "Report" (line 71), "Note File Handling" (line 90), "Important Rules" (line 82), and the default template block Key Findings / Details / Open Questions (lines 46–69).
- Frontmatter fields the plan says to preserve both exist: `disable-model-invocation: false` (line 9) and `user-invocable: true` (line 10). `name: note` (line 2) is left unchanged as required.
- The numbering rule the plan says to preserve verbatim ("highest existing `NN` prefix + 1, start at `01`") matches lines 39 and 93.
- File path convention is correct: editing `src/skills/note/` is right — `active/skills/note` symlinks to it (per project CLAUDE.md), so no separate active-set change is needed. The plan's implementer note about this is accurate.
- The "Hooks (caller inputs)" subsection approach is consistent with existing repo convention: `roadmap-engine/SKILL.md:71` already uses a "Hook points (caller-supplied)" pattern, so the terminology and mechanism-passing model are established, not invented.

### Positive Notes

- **Correct resolution of a loose spec phrase.** Spec Edit 1 says the destination may come from "the caller (or the user's argument)." The plan deliberately treats destination as a *caller-only* hook and keeps standalone `/note` byte-identical (argument stays `[topic-slug]`). This is the right reading — introducing a user-facing destination argument would violate the spec's own "byte-identical standalone" constraint. The plan chose the consistent interpretation rather than the ambiguous one.
- Task boundaries are clean and single-file; the destination hook (Task 2) and template hook (Task 3) are threaded independently, so each task is reviewable in isolation.
- The "fewer than 5 tasks → single commit" convention is applied, and the commit message is pre-specified and descriptive.
- Implementer notes correctly fence off scope (don't touch callers, don't move the default, don't rename), pre-empting the most likely over-reach.

PLAN_REVIEW_PASS

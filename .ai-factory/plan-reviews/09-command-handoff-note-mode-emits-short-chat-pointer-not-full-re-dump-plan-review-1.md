# Plan Review — command-handoff: note mode emits short chat pointer, not full re-dump

**Plan:** `.ai-factory/plans/09-command-handoff-note-mode-emits-short-chat-pointer-not-full-re-dump.md`
**Target file:** `src/commands/command-handoff.md`
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): WARN — none. The only relevant line (`:22`) registers `src/commands/` as a hosted artifact type; this behavioral change stays inside the command and does not touch that boundary. No action needed.
- **Rules** (`.ai-factory/RULES.md`): WARN — file not present. No rule gate to apply.
- **Roadmap** (`.ai-factory/ROADMAP.md`): OK — the plan maps 1:1 to the open milestone at `:23` ("note mode emits short chat pointer, not full re-dump") and its spec note `.ai-factory/notes/19-task-command-handoff-chat-pointer-not-full-dump.md`. Milestone linkage is explicit and correct.

## Verification Against the Codebase

Cross-checked every line reference in the plan against the live file:

- Line 100 — ends with "This gate applies in both chat mode and note mode." ✓ (Task 2 target)
- Line 106 — "**Chat mode:** Emit the handoff prompt directly to chat." ✓ (correctly left untouched)
- Lines 108–120 — the "**Note mode:** Do both of the following" block with sub-steps a–d. ✓ (Task 1 target)
- Sub-steps a–c are the file-write mechanics (`ls .ai-factory/handoffs/`, find highest `<NN>`, semantic `<slug>`, verbatim `Write`); sub-step (d) is "Report the path … as a one-line confirmation after the handoff body." ✓

Path `.ai-factory/handoffs/` is the real target the command writes to (it does not yet exist on disk, consistent with sub-step (a)'s missing-dir handling). The plan correctly uses `src/commands/command-handoff.md` (the source-of-truth file), not the `.claude/commands/` symlink mentioned in the older milestone text.

## Critical Issues

None.

## Minor Notes (non-blocking)

1. **Implicit list renumbering.** Task 1 reorders the note-mode block so the file write comes first (step 1, sub-steps a–c) and the chat pointer second (step 2, absorbing old sub-step d). The current block is numbered `1. Emit to chat` / `2. Persist as note file (a–d)`. The implementer must renumber — the plan implies this ("Reorder so the file write comes first") but does not spell out the new numbering. Low risk; just flagging so the nested list stays coherent.

2. **Frontmatter description left as-is.** The frontmatter (`:2–7`) says "Optionally persist the handoff as a durable note" — still accurate after this change, so no edit is needed. The plan correctly does not touch it; calling this out only to confirm the omission is intentional, not a gap.

3. **Line 43 proportionality paragraph untouched — correct.** The "Output length and granularity must track how much was actually done" mandate governs the composed handoff (now the file content in note mode). It needs no change, and Task 2 already redirects the *self-check* gate (`:100`) to the file. Consistent; no action.

## Positive Notes

- The plan faithfully reflects spec note 19, including the file/chat audience split (machine vs. human) and the paste-back-able requirement.
- Task 2's scoping is correct on both branches: gate applies to the **file** in note mode and to the **chat output** in chat mode, with the chat pointer explicitly exempted from the proportionality gate.
- Scope is appropriately surgical — no doc/README/ARCHITECTURE updates pulled in, no migrations, no test scaffolding for a markdown command file. Settings (Testing: no, Docs: no, Logging: minimal) fit the change.
- The dependency declaration (Task 2 depends on Task 1) is reasonable since Task 2's wording references the pointer behavior Task 1 introduces.

PLAN_REVIEW_PASS

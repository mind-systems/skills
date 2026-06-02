# Code Review — command-handoff: scale handoff detail proportionally to session depth

**Scope:** `src/commands/command-handoff.md` (the only code change; other staged files are plan/note/review artifacts).
**Reviewed:** `git diff HEAD` + full read of the modified file in context.

## Summary

The change is purely additive to an executable prompt file. All four plan tasks are implemented faithfully and the spec's guard conditions hold. No correctness, security, or logic defects found.

## Verification against plan + spec

| Task | Location | Result |
|------|----------|--------|
| 1. Proportional-depth mandate | line 43 | Present; includes the "proportional, not maximal — a trivial session padded to migration-guide length is itself a failure" guard. ✓ |
| 2. Two new first-class sections | lines 91–95 | `## 10. Cross-cutting contracts / invariants checklist` and `## 11. Per-unit map with watch-points` appended after section 9, trigger-based ("Only if…"), matching the 7–9 convention. The optional-sections gate prose updated `(7–9)` → `(7–11)` at line 41 — no stale count left behind. ✓ |
| 3. Error-log requirement | line 80 | Tightened to demand named symbol/file/decision, explicitly rejects "some issues were fixed", preserves "Empty → omit section". ✓ |
| 4. Richness self-check gate | line 100 | Placed after "Populate every field" and before Step 3, so it runs before the chat/note split; restates the proportionality guard; explicitly "applies in both chat mode and note mode". ✓ |

**Guard conditions (spec §Guard conditions):**
- 9-section skeleton names/order unchanged — only section 6's *placeholder text* tightened (permitted by Task 3). ✓
- `note`/`ноут` trigger behavior and note-persistence path (Step 3) untouched. ✓
- `allowed-tools` unchanged (`Write Bash(ls *)`) — the additions introduce no new tool needs. ✓

## Logic / "runtime" checks (for a prompt file)

- **No contradictory instructions.** The proportional mandate ("enumerate each work-unit individually") operates *within* sections; it does not conflict with "do not change section names or order", which governs the skeleton structure.
- **Gate ordering is correct.** The self-check at line 100 sits before `## Step 3 — Output`, so it executes prior to the chat-vs-note branch — consistent with its "applies in both modes" claim.
- **Markdown integrity.** New `## 10`/`## 11` headings live inside the `~~~` fence as literal template text; the closing fence at line 96 is intact. No broken/duplicated structure.
- **Optional-section consistency.** Both new sections carry "Only if…" triggers consistent with the single "omit a section only if genuinely empty" rule at line 41, so the count update to `(7–11)` is internally coherent.

## Non-blocking observation (not a defect)

Sections 10–11 are positioned last (after the optional 7–9 block), while the spec calls the cross-cutting-contracts checklist "the densest, highest-leverage section." This placement was explicitly directed by Task 2 ("Append … after section 9") and the trigger-based treatment matches the spec's "triggered when the session covered many units" wording, so the implementation is faithful to the approved plan. Flagging only as a future design consideration — not a code issue with this change.

REVIEW_PASS

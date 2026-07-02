## Code Review Summary

**Files Reviewed:** 1 plan (targets `src/skills/milestone-rescue-audit/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): No boundary/dependency concern. This is a frontmatter-only `allowed-tools` widening; it touches no skill graph edges (`loads:` unchanged) and introduces no cross-file coupling. PASS.
- **Rules** (`.ai-factory/RULES.md`): file absent — gate skipped (WARN: optional file missing, non-blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md`): Plan maps 1:1 to the open milestone line 71 — *"milestone-rescue-audit: pre-approve discovery tools for cold runs"* — which prescribes exactly `Read Glob Grep Bash(git *)`, frontmatter-only, body unchanged. Linkage present and exact. PASS.
- **Spec note** (`.ai-factory/notes/40-rescue-audit-cold-run-tools.md`): exists and corroborates the plan verbatim — same target string, same "no body changes," same "do not add Write/Edit." PASS.

### Critical Issues
None.

### Verification performed
- **File path correct:** `src/skills/milestone-rescue-audit/SKILL.md` exists.
- **Line number correct:** line 13 is indeed `allowed-tools: Read` — the anchor the plan edits.
- **Target string correct:** the replacement `Read Glob Grep Bash(git *)` matches the spec note and the ROADMAP line character-for-character.
- **Syntax valid & conventional:** `Bash(git *)` is the established form across sibling skills — `milestone-rescue` itself uses `Read Write Edit Glob Grep Bash(git *) AskUserQuestion`, and several others use the identical `Bash(git *)` token. No new syntax introduced.
- **Contract preserved:** the chat-only / no-writes guarantee lives in the Inputs description, Step 6, and the "What NOT to do" section (lines 141–143, 184–185) — all untouched by this plan. Widening discovery tools does not weaken it; `Write`/`Edit` are correctly excluded.
- **Cold-path justification sound:** the Inputs section (lines 30–31) promises "If run cold, locate and read them before Step 1," which genuinely requires `Glob`/`Grep`, and `Bash(git *)` mirrors `milestone-rescue`'s discovery step. The gap the plan closes is real.

### Minor observations (non-blocking)
- The spec note motivates `Bash(git *)` via `git status --short -- .ai-factory/` for discovery, but the audit body never names a git command explicitly (it defers artifact layout to `milestone-rescue`). The pre-approval is still justified as parity with the rescue discovery flow, and the plan correctly declines to add body text for it — keeping the change frontmatter-only as specified. No action needed.
- Settings block declares Testing: no / Docs: no — appropriate; a one-token frontmatter change has no runtime surface to test and no user-facing behavior to document.

### Positive Notes
- Tightly scoped: single-line edit, explicit "This is the only edit," explicit exclusions (no `Write`/`Edit`, no Inputs/contract changes) — leaves no room for the implementing agent to drift.
- Full traceability: plan ⇄ spec note ⇄ ROADMAP line are mutually consistent with no contradictions.
- Correctly honors the repo's engine/contract discipline — the change is additive to capability only and preserves the behavioral contract word-for-word.

PLAN_REVIEW_PASS

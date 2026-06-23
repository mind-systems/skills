# Plan Review — milestone-rescue: document the closed set of valid sidecar `step` rollback states

**Plan:** `.ai-factory/plans/13-milestone-rescue-document-the-closed-set-of-valid-sidecar-step-rollback-states.md`
**Target file:** `src/skills/milestone-rescue/SKILL.md` (doc-only)
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** present. No boundary/dependency conflict — this is a doc-only edit to a skill body, no module structure or contract changes. Gate: OK.
- **Rules (`.ai-factory/RULES.md`):** not present. Gate: WARN (optional file absent) — non-blocking.
- **Roadmap (`.ai-factory/ROADMAP.md`):** present. The milestone is tracked; the spec note `notes/23-task-milestone-rescue-document-rollback-states.md` cleanly traces plan → note → roadmap. Gate: OK.
- **Skill-context (`.ai-factory/skill-context/aif-review/SKILL.md`):** not present — no project-specific review overrides to apply.
- **Custom-skill divergence:** `milestone-rescue` is listed in CLAUDE.md as a custom / never-overwrite-from-upstream skill. The plan correctly treats it as safe to edit directly; no divergence registration is required. The spec note (Guard, line 51) confirms this. Gate: OK.

## Codebase Verification

I verified the plan's claims against the actual SKILL.md and the source spec note:

- **Two-row `step` table both writing `"plan_reviewed"`** (plan Task 2) — confirmed at SKILL.md lines 290–294. Accurate.
- **Hardcoded `Emit:` message** `Sidecar updated: step set to "plan_reviewed".` (plan Task 2) — confirmed at SKILL.md line 303. The generalization is warranted.
- **Two documented outcomes (full reset / re-implement)** — confirmed: full-reset at lines 274–279, re-implement at 281–303. Adding a third is consistent with the existing structure.
- **Cleanup narrative keyed to Step 2 failure mode** — confirmed at lines 254–267.
- **`"planned"` always-valid / no-artifact precondition** — matches the spec note Guard (note line 49) and the historical contradiction it cites.
- **Test-mode swap** (`review_failed:N` → `test_run_failed:N`, `test-runs/...`) — matches note line 26.
- **Five-state closed set and the source-of-truth caveat** — the plan's table is a verbatim mirror of the note's table (note lines 18–24). Faithful.

The plan is a near-exact realization of the spec note's Change A / Change B / Guards. File path is correct. No missing migrations, no security surface, no API misuse (doc-only).

### Note on `orchestrator/main.py`

The referenced `orchestrator/main.py` (`_validate_sidecar_step()` / `_detect_milestone_step()`, `main.py:197`) does **not** exist in this repo — it is an external AI Factory component. This is correct and intentional: the plan (Task 1) and the note both treat the orchestrator as the external source of truth and instruct the skill to carry a "if the orchestrator changes, update this table" caveat. The plan does not assume the file is present in this repo, so there is no wrong-path assumption. Reviewer cannot independently confirm the five-state set against live source, but the plan inherits it from the spec note verbatim and adds the divergence caveat — which is the right mitigation.

## Observations (non-blocking)

1. **Disposition vs. failure-mode mapping.** Step 5's cleanup deletions are currently keyed to the **Step 2 failure mode** (plan-phase → full reset; implement-phase → re-implement). The new "Re-plan-review (plan corrected in place)" is a third *disposition* that crosses that mapping: it keeps the plan `.md` (like re-implement) but deletes the plan-reviews (like full reset). Task 2 does call for updating the cleanup narrative to acknowledge this, which is the right instinct — when implementing, make explicit that this disposition is an **operator choice within a plan-phase rescue**, not something auto-derived from the Step 2 classification, so the "set of files to delete depends on the failure mode" sentence (line 254) doesn't read as contradicting the new row.

2. **Entry point for the corrected-plan path.** Step 4 (the `AskUserQuestion` proposals) does not currently offer "correct the plan in place" as an option, so an operator reading top-to-bottom isn't routed to the new outcome. The spec note deliberately scopes this task to Step 5 documentation only, so this is out of scope here — but it's worth a one-line pointer in Step 5 (or a future milestone) noting how an operator arrives at this disposition, otherwise the well-documented outcome may go undiscovered.

Both are refinements to fold into the wording during implementation; neither blocks the plan.

## Positive Notes

- Tightly scoped, doc-only, with correct dependency ordering (Task 1 → 2 → 3).
- Each task maps 1:1 to a spec-note change (A / B / Guards) and preserves existing logic rather than rewriting it.
- The source-of-truth caveat and the `"planned"`/`"implemented"` precondition guard are both explicitly carried over — these are the exact items that caused the original failure the note documents.

PLAN_REVIEW_PASS

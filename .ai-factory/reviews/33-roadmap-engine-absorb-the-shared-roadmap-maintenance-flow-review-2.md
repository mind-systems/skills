# Code Review (round 2): roadmap-engine — absorb the shared roadmap-maintenance flow

**Scope:** `git diff HEAD` — only `src/skills/roadmap-engine/SKILL.md` is a code change (the `.json` / plan / plan-review / review-1 files are process artifacts, out of scope). Re-reviewed the full file, not just the diff.

This file is agent-runtime instruction content, so "correctness" = the absorbed flow behaves like the two callers' current flow, stays caller-agnostic, and leaks no philosophy.

## Round-1 finding — resolved

Round 1 flagged that the shared **update-mode "Rewrite — major revision"** action (present in both `roadmap-outline:125` and `roadmap-decompose:154`) had not been absorbed. It is now present:

- Update menu (lines 165–173) includes `4. Rewrite — major revision of the roadmap`.
- A matching action bullet (lines 181–183) defines it as re-running the Create-mode draft→confirm cycle (gather input, explore, draft in memory, apply the per-entry gate hook, confirm) over the existing `$TARGET_FILE`, replacing contents on confirmation.

The definition is clean mechanism — no philosophy leaked, per-entry gate correctly referenced as a hook, and consistent with the Create-mode finalize semantics. The create-mode and update-mode Rewrite options are now both present, resolving the round-1 inconsistency.

## Constraint checks (all pass)

- **Single code file:** only `src/skills/roadmap-engine/SKILL.md` modified; callers untouched. ✓
- **Line budget:** 246 ≤ 500. ✓
- **Caller-agnostic:** grep of the new section (line 63→end) for `milestone|atomic|strategic|roadmap-outline|roadmap-decompose|roadmap-decompose-skeleton` → none. `roadmap-prune` appears only as the downstream pruner in critical rule 3 (not a caller). ✓
- **No philosophy leaked:** granularity, per-entry gate, target-file routing, extra actions are all named as caller hooks (lines 71–80); no atomicity gate, no 5–15 rule, no granularity definition. ✓
- **Load-once restated** for the new section (lines 68–69). ✓
- **Two-tier + Roadmap File Format sections unchanged** (diff is an append plus the description edit). ✓
- **Description:** now names the create/update/check flow, stays caller-agnostic + load-once, well under 1024 chars. ✓
- **`allowed-tools: Read` unchanged:** correct — the engine is loaded (Read) by callers that already declare Write/Edit/Glob/Grep/Bash/AskUserQuestion/Skill; it does not execute the flow itself. ✓
- **Register:** prose + the callers' existing `AskUserQuestion` blocks — matches the rest of the file, not rigid pseudo-code. ✓

## Behavioral cross-check vs. callers

- Step 0, mode determination, create/update/check dialogs, finalize (notes-after-confirmation), summaries, and the three mechanism-tier critical rules all match the callers' current behavior, generalized to "entry" + `$TARGET_FILE`.
- Caller-specific actions correctly left as hooks: `Decompose existing` (decompose-only) is not in the engine menu (belongs to hook d); the atomicity gate is referenced only as the optional per-entry gate hook.
- Check-mode summary omitting `Total entries` matches both callers' check-mode summaries — intentional, not a regression.

No bugs, security issues, or correctness problems found.

REVIEW_PASS

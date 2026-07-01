# Plan Review: test-philosophy — rename `test-engine` + separate philosophy from algorithm

**Plan:** `.ai-factory/plans/20-test-philosophy-rename-test-engine-separate-the-test-philosophy-from-the-algorithm.md`
**Files Reviewed:** 4 target files + ROADMAP/spec-note/context gates
**Risk Level:** 🟢 Low

## Verification Against the Codebase

Every factual claim in the plan was checked against the actual files:

- **`grep -rn 'test-engine' src/ CLAUDE.md .ai-factory/ROADMAP.md`** — the plan's enumeration is exhaustive. Live source hits are exactly: `src/skills/test-engine/SKILL.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md` (lines 7, 9, 36, 44, 84, 141, 142), and `CLAUDE.md` (lines 34, 117). A broader sweep across all `*.md` (incl. `AGENTS.md`, `README.md`) confirms **no other live references** — remaining hits are all historical `.ai-factory/` artifacts (plans, plan-reviews, reviews, notes 27/29/31, ROADMAP), which the plan correctly leaves untouched.
- **Task 1 line refs** — `test-engine/SKILL.md` has `name: test-engine` (L2), `user-invocable: false` (L9), `disable-model-invocation: false` (L10), `allowed-tools: Read` (L11), H1 `# Test Engine — …` (L14). All match.
- **Task 2** — CLAUDE.md L34 (tree) and L117 (never-overwrite list) both contain `test-engine`. Confirmed.
- **Task 3** — all 7 skeleton lines confirmed; the alias note at L36–38 exists verbatim as quoted.
- **Task 4** — `roadmap-test-coverage/SKILL.md` `allowed-tools` (L13) has **no** `Skill` (correct — needs adding); Layer 3 inline question + table at L64–76; Layer 7 Class A/B at L244–265. All line ranges accurate.
- **ROADMAP guardrail** — L43 is the completed `test-engine` creation milestone, L47 (roadmap-decompose-skeleton, completed) already reads `test-philosophy`, L49 is this milestone. The plan's decision to leave these as history is confirmed accurate.

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** WARN-none. The plan is a textbook application of the repo's "mechanism vs policy" model — `test-philosophy` is a policy/philosophy unit loaded by callers that stay in control, exactly matching the composition rule. No boundary violation.
- **Rules (`.ai-factory/RULES.md`):** file absent — WARN (optional, non-blocking).
- **Roadmap (`.ai-factory/ROADMAP.md`):** aligned. This plan directly implements the open milestone at L49 and cites spec note 31.

## Critical Issues

None. The plan is internally consistent, byte-accurate about the codebase, and the architectural reasoning is sound.

## Strengths Worth Noting

- **Correct isolation insight (Task 4, Layer 7):** the plan explicitly recognizes that the Layer 7 classification subagent runs in an isolated context and cannot load the Skill, so the Class A/B definitions must stay inline in the agent prompt while only the orchestrator's decision prose points at the loaded corollary. This is the exact trap that would break a naive "just load it everywhere" refactor.
- **Load-once discipline:** the load happens once at Layer 3; Layer 7 reuses it. Consistent with the skill's own "Load this skill once per chat" contract.
- **`disable-model-invocation: false` preserved:** the plan correctly keeps this so consumers can still load `test-philosophy` via the Skill tool — flipping it would silently break both callers.
- **Symlink assumption is correct:** `~/.claude/skills` → `~/projects/skills/src/skills` is a parent-level symlink, so `git mv` of the child directory is transparently reflected. No manual symlink fix needed.
- **`Skill` already present** in `roadmap-decompose-skeleton`'s `allowed-tools` (L14) — no edit needed there, and the plan doesn't add a spurious one.

## Minor Advisory Notes (non-blocking)

1. **Body "engine" wording (Task 1):** in practice the only `engine` occurrence in `test-engine/SKILL.md` is the H1 (L14). The frontmatter `description` and body prose (L16 "shared pure-content philosophy unit") already say "philosophy." The plan already hedges this correctly ("verify no stray 'engine' remains"), so no change to the plan is needed — just confirming the implementer will find essentially only the H1 to change.
2. **ROADMAP vs spec-note tension:** spec note 31 (L41) says handle "all ROADMAP mentions," while the plan deliberately preserves ROADMAP L43/L49 as history. The plan's reasoning (history preservation, consistent with `roadmap-prune` philosophy and the repo's "history belongs in commit messages / completed milestones are records" stance) is the correct call and overrides the looser spec phrasing. Flagged only so the implementer doesn't "fix" those lines thinking they were missed. The verification grep on L49 of the plan correctly scopes to `src/ CLAUDE.md` (excluding ROADMAP), which enforces this intent.
3. **`argument-hint` on the newly user-invocable skill:** flipping `user-invocable: true` does not require an `argument-hint` since the philosophy takes no arguments. No action needed; noting for completeness.

## Conclusion

The plan is accurate, exhaustive in its reference enumeration, architecturally correct, and scoped tightly as a rename + extraction (not a rewrite). File paths, line numbers, and API/frontmatter assumptions all verified against the live codebase. No missing steps, no wrong assumptions, no missing migrations.

PLAN_REVIEW_PASS

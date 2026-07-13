## Plan Review Summary

**Plan:** 5.7 — repo docs: agents category registered completely
**Files Reviewed:** 2 target files (`.ai-factory/ARCHITECTURE.md`, `README.md`) + governing spec 56 + ROADMAP milestone line
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (WARN-scan): `.ai-factory/ARCHITECTURE.md` is itself a target of this plan. The edit *aligns* the three-zones enumeration with the boundary reality (three machine symlinks) rather than crossing any boundary — consistent, no conflict.
- **Rules** (skip): `.ai-factory/RULES.md` not present.
- **Roadmap** (PASS): milestone `5.7` exists as a `[ ]` line in `.ai-factory/ROADMAP.md:103` and names `Spec: .ai-factory/specs/56-repo-docs-agents-registration.md`. The plan tracks that spec's `## Change` and `## Guards` clause-for-clause.
- **Skill-context** (skip): no `.ai-factory/skill-context/aif-review/SKILL.md`.

### Ground-truth verification
Every factual claim in the plan was checked against the live files:

- **Task 1 anchor** — ARCHITECTURE.md line 24 reads verbatim "…and is the only layer `~/.claude/skills` and `~/.claude/commands` point at." ✓ The preceding paragraph (line 22) already names `src/agents/` as a category, so the plan's "stays byte-identical" claim for it holds. ✓
- **Task 2 anchor** — README.md line 30 begins "Our skills live under `src/skills/`; …" and names skills only. ✓ README Setup lines 10 (`ln -s ~/projects/skills/active/agents ~/.claude/agents`) and 13 (`active/agents/`) already cover the agents symlink, so the plan's "leave Setup untouched" instruction is correct. ✓
- **Spec fidelity** — spec 56's `## Change` prescribes exactly these two edits with the same example wording the plan reproduces. No divergence.
- **Scope** — docs-only, no code/tests/migrations/security surface. Testing/Logging/Docs settings ("no/minimal/no") are appropriate.

### Critical Issues
None.

### Positive Notes
- The plan pins exact line anchors and quotes the pre-edit text, so the implementer needs no guessing — no fantasy holes.
- The "byte-identical except this enumeration/sentence" guard is stated on both tasks and mirrored by the spec's guard and by the `git diff shows two one-sentence edits` acceptance test, giving a clean, checkable stop condition.
- Correctly recognizes CLAUDE.md registration is already complete and scopes it out, matching spec 56's boundary and specs 16/17's prior split.
- Task 2's proposed wording ("Our skills live under `src/skills/` (commands under `src/commands/`, agent definitions under `src/agents/`); …") reads naturally and preserves the rest of the sentence's clauses.

PLAN_REVIEW_PASS

# Review: command-pin-gaps default target retarget

## Scope
Single changed file: `src/commands/command-pin-gaps.md` (line 10 rewrite). The other staged files are planning artifacts, not code.

## Verification against spec (`notes/37-pin-gaps-default-target.md`)
The new target line implements the exact priority chain the spec requires:
1. `$ARGUMENTS` file(s), explicit plan targeting preserved — ✓
2. scope under discussion in chat (named task, phase, or note) — ✓
3. all open `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md`, scanning contract line **and** `Spec:` note — ✓

The `newest .ai-factory/plans/*.md` fallback is fully dropped — ✓. Everything the spec required to stay unchanged is untouched: hole taxonomy (line 14), `file:line` pinning rule (line 16), `## Blocking decisions` (line 16), scan mode (line 18), and the closing report format (line 19). Frontmatter and `allowed-tools` are unchanged; `Read`/`Grep`/`Glob` already cover reading ROADMAP.md and its notes, so no tool addition was needed (Task 2 confirmed).

## Findings
None. This is a prose instruction file for an agent — no code, no runtime surface, no migrations/types/concurrency to break. The rewrite is faithful to the spec, terse, and consistent with the surrounding style. The mild "the file" phrasing in lines 16/19 (which reads most naturally for a single-file target) predates this change and the spec explicitly froze those lines, so it is out of scope.

REVIEW_PASS

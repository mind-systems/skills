# Review: 5.7 — repo docs: agents category registered completely

## Scope
Two one-sentence doc edits across two files, per the plan and spec `56-repo-docs-agents-registration.md`.

## Verification against ground truth
- **ARCHITECTURE.md** (three-zones paragraph): the `active/` enumeration now reads `~/.claude/skills`, `~/.claude/commands`, and `~/.claude/agents` — the third machine symlink is added; serial comma and phrasing correct. The rest of the paragraph and the preceding `src/agents/` paragraph are byte-identical. ✅
- **README.md** (Structure layout sentence): now names all three `src/` categories — `src/skills/` with `(commands under src/commands/, agent definitions under src/agents/)`; the upstream-mirror clause, `active/` symlink clause, and per-skill layout clause are unchanged. ✅
- **CLAUDE.md**: untouched — `git status` shows no modification. Guard honored. ✅
- `git diff HEAD` shows exactly two one-sentence edits to the two source files (the plan `.md`/`.json` and plan-review are the expected planning artifacts, not code). ✅

## Findings
- No correctness, security, or runtime concerns. These are prose-only Markdown edits with no executable surface; enumerated facts (`~/.claude/agents` symlink live since task 17; `src/commands/` and `src/agents/` categories) match the repo's CLAUDE.md and existing ARCHITECTURE text.

REVIEW_PASS

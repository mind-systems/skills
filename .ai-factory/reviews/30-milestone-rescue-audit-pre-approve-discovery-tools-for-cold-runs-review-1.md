# Code Review: milestone-rescue-audit — pre-approve discovery tools for cold runs

**Scope of code change:** one line in `src/skills/milestone-rescue-audit/SKILL.md` frontmatter.
(The other staged files — plan `.md`/`.json`, plan-review — are orchestrator artifacts, not code.)

## Change reviewed

```diff
-allowed-tools: Read
+allowed-tools: Read Glob Grep Bash(git *)
```

## Verification

- **Matches spec & roadmap exactly.** The replacement string `Read Glob Grep Bash(git *)` is character-for-character what `.ai-factory/notes/40-rescue-audit-cold-run-tools.md` and ROADMAP line 71 prescribe.
- **Syntax valid and conventional.** `Bash(git *)` is the established token across sibling skills. `temporal-tree` is the closest precedent — a read-only + git-discovery skill declaring `Read Bash(git *) Glob Grep`, the same capability set; `milestone-rescue` (the discovery flow this mirrors) uses the identical `Bash(git *)` token. No new syntax introduced.
- **Frontmatter-only, as specified.** The diff touches only line 13. `name`, `description`, `argument-hint`, and the entire body are byte-unchanged. Read the full file to confirm — Steps 1–6 and "What NOT to do" are intact.
- **Contract preserved.** The chat-only / no-writes guarantee lives in the description (lines 8–9), Step 6 (line 143 "No files written, no ROADMAP edited"), and "What NOT to do" (lines 184–185). None are touched. Widening discovery capability does not weaken them — `Write`/`Edit` are correctly excluded, so the skill still cannot write by tool grant, not just by instruction.
- **Cold-path gap is real.** Inputs (lines 29–31) promises "If run cold, locate and read them before Step 1," which genuinely needs `Glob`/`Grep` to locate artifacts and `Bash(git *)` to inspect `.ai-factory/` status. The prior `Read`-only grant would have prompted at step one. The change closes exactly that gap.

## Findings

None. No bugs, security issues, or correctness problems. The change is a strict capability widening that adds no write/mutation surface, matches the repo's frontmatter conventions, and leaves the behavioral contract word-for-word intact.

REVIEW_PASS

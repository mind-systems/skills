# Frontmatter tool hygiene: drop `Questions` pseudo-tool; fix Bash rule syntax in aif-docs

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- Two skills declare a `Questions` tool that does not exist in the harness: `src/skills/roadmap-outline/SKILL.md` (`allowed-tools: … AskUserQuestion Questions Skill`) and `src/skills/aif-docs/SKILL.md` (`allowed-tools: … AskUserQuestion Questions WebFetch WebSearch`). The interactive numbered-options pattern (1/2/3 menus) works through `AskUserQuestion`, which both already declare — `Questions` is dead weight that at best is ignored and at worst confuses tool-permission matching.
- `aif-docs` also uses invalid Bash rule syntax: `Bash(mkdir, npx, python)` — comma-separated commands inside one rule. The correct form is one rule per command with a glob: `Bash(mkdir *) Bash(npx *) Bash(python *)`. As written, the rule likely matches nothing, so every mkdir/npx/python call prompts.

## Details

- **roadmap-outline frontmatter:** `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions Skill` → drop `Questions`.
- **aif-docs frontmatter:** drop `Questions`; replace `Bash(mkdir, npx, python)` with `Bash(mkdir *) Bash(npx *) Bash(python *)`.
- Frontmatter-only change in both files; no body edits. Numbered-option dialogs in both skills continue to run via `AskUserQuestion` exactly as before.

## What NOT to do

- Do not touch the upstream mirror copies — only `src/skills/`.
- Do not rework the dialogs themselves — the 1/2/3 menu pattern stays; only the tool declarations change.
- Do not touch aif-docs' body (its >500-line length is a known, accepted deviation — out of scope here).

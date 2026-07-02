# milestone-rescue-audit: add Glob/Grep/Bash(git *) to allowed-tools for cold runs

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `src/skills/milestone-rescue-audit/SKILL.md` frontmatter pre-approves only `allowed-tools: Read`, but the Inputs section promises cold-start capability: "If run cold, locate and read them before Step 1". Locating artifacts requires directory listing/search (`Glob`, `Grep`) and, mirroring `milestone-rescue`'s discovery step, `git status --short -- .ai-factory/` (`Bash(git *)`). A cold run today stumbles over permission prompts at the very first step.

## Details

- Change frontmatter to: `allowed-tools: Read Glob Grep Bash(git *)`.
- No body changes required — the Inputs section already describes the cold path and defers artifact layout to `milestone-rescue`.
- The skill stays read-only in effect: `Bash(git *)` is used for status/log inspection during discovery; the body's "no file writes, no ROADMAP edits" contract is unchanged and still enforced by the What-NOT-to-do section.

## What NOT to do

- Do not add Write/Edit — the skill is chat-only by contract.
- Do not touch the body; this is a frontmatter-only change.

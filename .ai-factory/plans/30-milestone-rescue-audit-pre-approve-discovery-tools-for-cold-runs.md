# Plan: milestone-rescue-audit: pre-approve discovery tools for cold runs

## Context
Widen `milestone-rescue-audit`'s `allowed-tools` so a cold run can locate artifacts (Glob/Grep) and inspect git status without permission prompts, while the chat-only/no-writes contract stays enforced by the body.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter

- [x] **Task 1: Widen `allowed-tools` to include discovery tools**
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In the frontmatter (line 13), change `allowed-tools: Read` to `allowed-tools: Read Glob Grep Bash(git *)`. This is the only edit — no other frontmatter fields, no body changes. Do NOT add `Write`/`Edit` (the skill is chat-only by contract). Do not touch the Inputs section or the "What NOT to do" contract; the cold-path description and the "no file writes, no ROADMAP edits" guarantee already live in the body and stay unchanged.

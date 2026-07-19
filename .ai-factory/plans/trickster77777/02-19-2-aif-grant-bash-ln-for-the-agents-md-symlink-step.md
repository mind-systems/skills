# Plan: 19.2 — aif: grant `Bash(ln *)` for the AGENTS.md symlink step

## Context
The `aif` skill's `## AGENTS.md Generation` section runs `ln -sfn CLAUDE.md AGENTS.md`, but `ln` is absent from the skill's `allowed-tools`, so the required symlink step has no standing grant and can block a headless orchestrator run. This task adds exactly `Bash(ln *)` to the grant list.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Widen the grant

- [x] **Task 1: Add `Bash(ln *)` to `aif` frontmatter `allowed-tools`**
  Files: `src/skills/aif/SKILL.md`

  Edit line 5 (frontmatter `allowed-tools`) only. Current live value — verified in the file, task 19.1's edit has already landed and dropped the retired `Bash(node *update-config.mjs*)` grant:

  ```
  allowed-tools: Read Glob Grep Write Bash(mkdir *) Skill AskUserQuestion
  ```

  Target value — insert `Bash(ln *)` immediately after `Bash(mkdir *)`, keeping every other entry unchanged in content and order:

  ```
  allowed-tools: Read Glob Grep Write Bash(mkdir *) Bash(ln *) Skill AskUserQuestion
  ```

  Constraints from the task spec (`.ai-factory/specs/trickster77777/80-aif-ln-grant-for-agents-symlink.md`):
  - **Grant only what the step needs** — add `Bash(ln *)`, never a broader `Bash(*)`; widen no other grant.
  - **Preserve 19.1's change** — do not reintroduce `Bash(node *update-config.mjs*)`. The two tasks share this one line; the second to land must preserve the first's edit. If the live line still carries the `update-config.mjs` grant when you read it, 19.1 has not yet landed — in that case add `Bash(ln *)` and leave the rest exactly as found; 19.1 removes its own grant.
  - **Do not touch the `## AGENTS.md Generation` section** (currently at L156, with the `ln -sfn CLAUDE.md AGENTS.md` command at L161). It is correct as written; no behavior there changes. Note the spec cites this section at L199–207, which has since drifted — the line numbers above are the live ones and take precedence.
  - Change nothing else in the file: no other frontmatter field, no body text.

  Verification: `grep -n 'allowed-tools' src/skills/aif/SKILL.md` shows `Bash(ln *)` present, `Bash(node *update-config.mjs*)` absent, and the surrounding entries intact. `git diff` on the file shows a single changed line.

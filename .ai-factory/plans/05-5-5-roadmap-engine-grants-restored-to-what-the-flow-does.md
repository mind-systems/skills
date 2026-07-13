# Plan: 5.5 — roadmap-engine: grants restored to what the flow does

## Context
Restore `roadmap-engine`'s `allowed-tools` frontmatter to match what its maintenance flow actually does (explore + write + git-log), fixing an unrecorded regression to `Read Skill`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter grant restoration

- [x] **Task 1: Restore the `allowed-tools` grant line**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Edit line 10 only. Change `allowed-tools: Read Skill` to `allowed-tools: Read Write Edit Glob Grep Bash(git *) Skill`. This restores milestone 41's original `Read Write Edit Glob Grep Skill` set and adds `Bash(git *)` for the flow's own `git log --oneline -20` exploration (per spec `.ai-factory/specs/54-engine-grants-restored.md`).
  Guards: body byte-identical — no changes below the frontmatter; do not touch any other frontmatter key (`name`, `description`, `user-invocable`, `disable-model-invocation`, `loads:` all stay). The diff must be exactly one line.
  Verify: `sed -n '10p' src/skills/roadmap-engine/SKILL.md` shows the new grant line; `git diff` is one line.

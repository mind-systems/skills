# Plan: 79.2 — the planning lenses enter the skill description field

## Context
The four planning lenses — `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose`, `roadmap-decompose-skeleton` — carry `disable-model-invocation: true`, so their descriptions are absent from the skill description field and no agent can load them through the `Skill` tool. This task flips the flag to `false` in each frontmatter, the way `architect-editor-engine` and the other engines carry it, so the descriptions join every session's field (the orchestrator's agents included). Per the task spec (`.ai-factory/specs/trickster77777/0229-the-planning-lenses-enter-the-skill-description-field.md`, § "What must be true after"), nothing else in those files changes. Per its § "What breaks on contact", no doc and no `CLAUDE.md` text mentions the flag, so no other file changes. The governing spec `docs/skill-description-field.md` already says, as 79.1 left it, that only a skill whose work is reviewed only before it happens stays out of the field. The planning lenses write additive text that is reviewed after the fact, so that rule does not keep them out. `agent-architect`, `roadmap-test-coverage`, `roadmap-prune` and `task-rescue` keep the flag and stay untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Frontmatter edits

- [x] **Flip the flag in the four planning lenses**
  Files: `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-outline-deep/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In each file's YAML frontmatter (between the opening and closing `---`), replace the line `disable-model-invocation: true` with exactly `disable-model-invocation: false`, the same form as in `src/skills/architect-editor-engine/SKILL.md`. Keep the line where it is: the field order differs between the files and stays as it is. Do not touch `name`, `description`, `argument-hint`, `allowed-tools`, `loads`, or anything in the skill body. Do not add `user-invocable` or any other field. Edit the `src/` files directly; `active/skills/<name>` are symlinks to them.

### Verification

- [x] **Run the spec's sweep and confirm the diff scope** (depends on Flip the flag in the four planning lenses)
  Files: none (read-only check)
  Run `grep -rn "disable-model-invocation" src docs CLAUDE.md`. The four planning lenses must now show `false`. `agent-architect`, `roadmap-prune`, `roadmap-test-coverage` and `task-rescue` must still show `true`. No hit may appear under `docs/` or in `CLAUDE.md`. Run `git diff --stat` and `git diff` and confirm two things: exactly the four `SKILL.md` files changed, and each changed by one line, `true` → `false`.

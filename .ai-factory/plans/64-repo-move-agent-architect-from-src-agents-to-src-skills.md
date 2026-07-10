# Plan: repo: move `agent-architect` from `src/agents/` to `src/skills/`

## Context
Relocate the `agent-architect` skill package out of the mixed `src/agents/` folder into the skills layer (`src/skills/`) so `src/` folders again name only the artifact type, leaving `src/agents/` holding agent definitions (`editor.md`) only. Pure move — `SKILL.md` stays byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Move and reactivate

- [x] **Task 1: Move the skill package and repoint its activation symlink**
  Files: `src/agents/agent-architect/` → `src/skills/agent-architect/`, `active/skills/agent-architect`
  Run `git mv src/agents/agent-architect src/skills/agent-architect` from the repo root — no content edits, `SKILL.md` must stay byte-identical (a `diff` of old vs new must be empty). Then repoint the activation symlink so `active/skills/agent-architect` → `../../src/skills/agent-architect` (currently `../../src/agents/agent-architect`): `ln -sfn ../../src/skills/agent-architect active/skills/agent-architect`. Do NOT touch `active/agents/`, `~/.claude/agents`, `editor.md`'s own location, or the completed `[x]` ROADMAP lines / specs 16-17 / handoffs (historical artifacts keep their original paths).

### Phase 2: Fix references to the old path

- [x] **Task 2: Fix the caller-path string in the editor agent definition** (depends on Task 1)
  Files: `src/agents/editor.md`
  In the frontmatter `description`, change the one caller-path string `The architect (src/agents/agent-architect) is the only caller` → `The architect (src/skills/agent-architect) is the only caller`. This is the only content edit in `src/`; no other change to `editor.md`.

- [x] **Task 3: Update `CLAUDE.md` — tree comment and Upstream Sync enumeration** (depends on Task 1)
  Files: `CLAUDE.md`
  Two edits: (1) Repository Structure tree — the `src/agents/` line comment `paired-loop agent skills (agent-architect + editor)` becomes an agent-definitions description that names only the `editor` paired-loop subagent (agent-architect no longer lives here). (2) Upstream Sync section — add `agent-architect` to the `src/skills/` "Everything else … is ours" custom-skills enumeration, and reword the trailing `src/agents/` sentence so it names only the `editor` agent definition (drop "the `agent-architect` skill (and its editor sibling)"). Leave the `active/agents/` tree line (`per-item symlinks → src/agents/*`, editor.md example) and the active-set enumeration (which already lists `agent-architect` correctly as a skill) unchanged.

- [x] **Task 4: Update `ARCHITECTURE.md` — the `src/agents/` sentence** (depends on Task 1)
  Files: `.ai-factory/ARCHITECTURE.md`
  Reword the one `src/agents/` sentence so the category holds agent definitions (`editor`), with the architect counterpart named as the `agent-architect` skill now living in `src/skills/` — remove the claim that `src/agents/` holds `agent-architect`.

### Phase 3: Verify

- [x] **Task 5: Verify the move is clean** (depends on Tasks 1-4)
  Files: (none — verification only)
  Confirm: `cat ~/.claude/skills/agent-architect/SKILL.md | head -3` resolves through the repointed symlink and shows `name: agent-architect`; `ls src/agents/` → `editor.md` only; `git diff --stat` shows the skill package as a pure rename; `grep -rn "src/agents/agent-architect" src/ CLAUDE.md .ai-factory/ARCHITECTURE.md README.md` → zero matches.

## Commit Plan
- **Commit 1** (after tasks 1-5): "Move agent-architect skill from src/agents to src/skills"

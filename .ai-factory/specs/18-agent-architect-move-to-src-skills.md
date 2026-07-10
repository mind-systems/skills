# repo: move `agent-architect` from `src/agents/` to `src/skills/`

## Current state

The `agent-architect` skill was authored into `src/agents/agent-architect/SKILL.md` (task 16), making `src/agents/` a mixed folder: one skill package (`agent-architect/`) plus one agent definition (`editor.md`). That breaks the zone taxonomy — `src/` folders name the **artifact type** (`skills/`, `commands/`, `global/`), never a feature pairing. The activation symlink already lives in the skills layer (`active/skills/agent-architect`), so the skill is a skill in every respect except its storage path.

## Change

Pure move, zero content changes — `SKILL.md` stays byte-identical:

- `git mv src/agents/agent-architect src/skills/agent-architect`
- repoint `active/skills/agent-architect` → `../../src/skills/agent-architect`
- `src/agents/editor.md`: the description's caller path `(src/agents/agent-architect)` → `(src/skills/agent-architect)` — the only content edit anywhere, one path string in frontmatter description
- `CLAUDE.md`: Repository Structure tree — `src/agents/` comment becomes "agent definitions (editor — the paired-loop subagent)"; Upstream Sync — add `agent-architect` to the `src/skills/` custom-skills enumeration, reword the `src/agents/` sentence to name only the `editor` agent definition
- `ARCHITECTURE.md`: the `src/agents/` sentence — category holds agent definitions (`editor`); the architect counterpart is the `agent-architect` skill in `src/skills/`

After the move `src/agents/` holds agent definitions only.

## Files & types

- move `src/agents/agent-architect/` → `src/skills/agent-architect/` (SKILL.md byte-identical)
- repoint symlink `active/skills/agent-architect`
- edit `src/agents/editor.md` (one path string), `CLAUDE.md` (tree comment + Upstream Sync), `.ai-factory/ARCHITECTURE.md` (one sentence)

## Guards

- **No content changes to the skill body** — this is a move, not an edit; `diff` old vs new `SKILL.md` must be empty.
- **Historical artifacts untouched** — completed `[x]` ROADMAP lines, specs 16/17, handoffs 09/10 keep their original paths as written; they record what was planned, not current layout. Current layout lives in `CLAUDE.md`/`ARCHITECTURE.md` only.
- `active/agents/`, `~/.claude/agents`, and `editor.md`'s own location are not touched (beyond the one description path string).

## Verification

- `cat ~/.claude/skills/agent-architect/SKILL.md | head -3` resolves through the repointed symlink and shows `name: agent-architect`.
- `ls src/agents/` → `editor.md` only.
- `git diff --stat` for the move shows a pure rename of the skill package.
- `grep -rn "src/agents/agent-architect" src/ CLAUDE.md .ai-factory/ARCHITECTURE.md README.md` → zero matches.

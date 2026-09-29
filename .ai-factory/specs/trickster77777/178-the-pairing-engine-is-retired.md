# 64.2 — the pairing engine is retired

## What is true now

This task follows 64.1, so `src/skills/agent-architect/SKILL.md` no longer loads or names `architect-pairing-engine` when it starts. The skill itself remains: `src/skills/architect-pairing-engine/` holds a single `SKILL.md`, named `architect-pairing-engine`, described as the "pairing-role contract for two architects working together with no direct channel between them — every message crosses through the user, who carries or confirms each relay", with a deciding half and an applying half. Its frontmatter reads `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, so its description sits in the always-loaded skill-description field of every session.

`active/skills/architect-pairing-engine` is a symlink to `../../src/skills/architect-pairing-engine`, and `~/.claude/skills` reaches the skill through it: `~/.claude/skills` is itself a symlink to `active/skills`, so `~/.claude/skills/architect-pairing-engine` resolves through this one entry, for every project that loads the user-level skills. Git tracks the entry as a symlink, beside the tracked `SKILL.md` of the directory.

`CLAUDE.md` names the skill in two lists. The active set reads "…, `agent-architect`, `architect-editor-engine`, `architect-pairing-engine` — plus one upstream original we use as-is: `aif-skill-generator`." The list under § "Upstream Sync" that opens "**Everything else in `src/skills/` is ours**" ends "…, `agent-architect`, `architect-editor-engine`, `architect-pairing-engine`. The same holds for `src/agents/` — the `editor` agent definition has no upstream counterpart; a re-sync must never overwrite it."

## What must be true after

`src/skills/architect-pairing-engine/` does not exist, and `active/skills/` holds no entry named `architect-pairing-engine`, a dangling link included.

`CLAUDE.md`'s active set reads "…, `agent-architect`, `architect-editor-engine` — plus one upstream original we use as-is: `aif-skill-generator`." and the list under § "Upstream Sync" ends "…, `agent-architect`, `architect-editor-engine`. The same holds for `src/agents/` — the `editor` agent definition has no upstream counterpart; a re-sync must never overwrite it." Both lists remain, each without the retired skill's name.

## What breaks on contact

**Rule:** any live file outside the plan layer that names `architect-pairing-engine`, or loads it, or speaks of its two halves, reads stale once the skill is gone — except a record of a past moment (a closed task's spec, plan, plan-review or review, a phase note, a handoff, a buffer, a row in the Features table of `.ai-factory/ARCHITECTURE.md`), which documents what was true when it was written.

**Sweep (re-runnable):**
```
grep -rn "architect-pairing-engine" src/ docs/ CLAUDE.md active/ .ai-factory/ARCHITECTURE.md README.md .claude/ scripts/ upstream/
grep -rln -i "pairing\|paired architect\|deciding half\|applying half" src/ docs/ CLAUDE.md
ls active/skills
```

**Finding.** The first search reaches the skill's own directory, `agent-architect`'s `loads:` line and its passage on recording a pairing role, both of which the previous task removes, and the two `CLAUDE.md` lists above. No other file under `src/`, `docs/`, `active/`, `.claude/`, `scripts/` or `upstream/`, and neither `.ai-factory/ARCHITECTURE.md` nor `README.md`, names it. The second search reaches the skill's own directory and `agent-architect`'s pairing passages, which the previous task removes; `docs/always-loaded-discipline.md`, which uses "pairing" for the map at entry and the leaf at the moment of action; and the review checklist of `aif-docs` and the font pairings of `ui-ux-pro-max`, ordinary uses of the word. The `ls` shows the symlink among the entries of `active/skills`. `.ai-factory/ARCHITECTURE.md` carries a Features row, "Two-architect pairing", anchored to a commit hash: a record of what was built, which stays true when the skill is retired. `AGENTS.md` is a symlink to `CLAUDE.md`, so the one edit covers both. No settings file, no other repository's `CLAUDE.md` or `AGENTS.md`, and nothing in the orchestrator repository names the skill. Removing the symlink also takes the skill's description out of the always-loaded field of every project that loads the user-level skills, from its next session on; nothing else reads it.

**On sequencing against 64.1.** `agent-architect`'s `loads:` line names the pairing engine until 64.1 removes it, so the engine is retired only after that task has landed.

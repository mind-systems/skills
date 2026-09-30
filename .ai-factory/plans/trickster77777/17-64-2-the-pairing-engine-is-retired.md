# Plan: 64.2 — the pairing engine is retired

## Context
After 64.1, nothing loads `architect-pairing-engine` (verified: the only remaining `src/` hit is the skill's own `SKILL.md`), yet the skill directory, its `active/skills/` symlink, and its name in two `CLAUDE.md` lists remain. This task deletes the skill and its symlink and drops the name from both lists, leaving each list otherwise intact. Task spec: `.ai-factory/specs/trickster77777/178-the-pairing-engine-is-retired.md`; governing spec: `docs/paired-loop.md` (no edit needed there).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Retire the skill

- [x] **Remove the skill directory and its active symlink**
  Files: `src/skills/architect-pairing-engine/` (delete), `active/skills/architect-pairing-engine` (delete)
  Run `git rm -r src/skills/architect-pairing-engine` (the directory holds only a tracked `SKILL.md`) and `git rm active/skills/architect-pairing-engine` (a tracked symlink to `../../src/skills/architect-pairing-engine`). Remove the symlink itself, not its target through it. Afterwards `src/skills/architect-pairing-engine/` must not exist and `ls -la active/skills` must show no entry named `architect-pairing-engine`, a dangling link included.

- [x] **Drop the name from both `CLAUDE.md` lists**
  Files: `CLAUDE.md`
  `AGENTS.md` is a symlink to `CLAUDE.md` — edit `CLAUDE.md` only, never replace the symlink.
  1. In the paragraph opening "**The active set** (what `~/.claude` actually loads)", change "…, `agent-architect`, `architect-editor-engine`, `architect-pairing-engine` — plus one upstream original we use as-is: `aif-skill-generator`." to "…, `agent-architect`, `architect-editor-engine` — plus one upstream original we use as-is: `aif-skill-generator`."
  2. Under § "Upstream Sync", in the paragraph opening "**Everything else in `src/skills/` is ours**", change "…, `agent-architect`, `architect-editor-engine`, `architect-pairing-engine`. The same holds for `src/agents/` …" to "…, `agent-architect`, `architect-editor-engine`. The same holds for `src/agents/` …".
  Every other word of both paragraphs stays unchanged.

### Confirm no live claim remains

- [x] **Re-run the spec's sweep** (depends on both tasks above)
  Files: none (read-only check)
  Run:
  ```
  grep -rn "architect-pairing-engine" src/ docs/ CLAUDE.md active/ .ai-factory/ARCHITECTURE.md README.md .claude/ scripts/ upstream/
  grep -rln -i "pairing\|paired architect\|deciding half\|applying half" src/ docs/ CLAUDE.md
  ls -la active/skills
  ```
  Expected: the first grep returns nothing; the second returns only ordinary uses of the word (`ui-ux-pro-max` font pairings, `aif-docs/references/REVIEW-CHECKLISTS.md`, `docs/always-loaded-discipline.md`); the `ls` shows no `architect-pairing-engine` entry. Leave `.ai-factory/ARCHITECTURE.md`'s Features row "Two-architect pairing" untouched — it records a past build. Leave plan-layer records (closed specs, plans, reviews, phase notes, handoffs, buffers) untouched. If any other live hit appears, stop and report it rather than editing outside this task's files.

# Plan: 5.7 — repo docs: agents category registered completely

## Context
Complete the agents-category registration left outside specs 16/17's boundary: extend ARCHITECTURE.md's `active/` symlink enumeration to name `~/.claude/agents`, and README's `src/` layout sentence to name `src/commands/` and `src/agents/`. Two one-sentence edits, two files; CLAUDE.md untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Complete the enumerations

- [x] **Task 1: Extend the ARCHITECTURE.md three-zones enumeration to all three symlinks**
  Files: `.ai-factory/ARCHITECTURE.md`
  In the three-zones paragraph (line 24), the `active/` clause reads "…and is the only layer `~/.claude/skills` and `~/.claude/commands` point at." Add the third machine symlink so it names `~/.claude/skills`, `~/.claude/commands`, and `~/.claude/agents` (live since task 17). Change only this enumeration inside that one sentence — the rest of the paragraph, including the preceding paragraph that already names `src/agents/`, stays byte-identical.

- [x] **Task 2: Extend the README.md `src/` layout sentence to name all three categories**
  Files: `README.md`
  The layout sentence (line 30) reads "Our skills live under `src/skills/`; …" and names skills only. Extend it minimally to name the two absent `src/` categories, e.g. "Our skills live under `src/skills/` (commands under `src/commands/`, agent definitions under `src/agents/`); …". Leave the rest of the sentence (upstream mirror, `active/` symlinks, per-skill layout) and README Setup lines 10/13 (which already cover the agents symlink) untouched.

## Guards
- Exactly two sentences across two files; `git diff` shows two one-sentence edits and nothing else.
- CLAUDE.md is not touched — its registration is already complete.

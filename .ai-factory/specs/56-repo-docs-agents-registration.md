# repo docs: agents category registered completely

Source observations, re-verified live 2026-07-12: `plan-reviews/63-agents-editor-…-plan-review-1.md:50` (+ siblings in `-plan-review-2.md:49`, `reviews/63-…-review-1.md:43`) and `plan-reviews/62-agents-architect-…-plan-review-1.md:35`. Specs 16/17 deliberately scoped registration to CLAUDE.md + README Setup; the two sentences below sat outside every milestone's file boundary and were never updated.

## Current state

- `.ai-factory/ARCHITECTURE.md`, three-zones paragraph: "`active/` is the curated working set … and is the only layer `~/.claude/skills` and `~/.claude/commands` point at" — the third machine symlink, `~/.claude/agents` (live since task 17), is missing from the enumeration. The preceding paragraph already names `src/agents/` as a category, so only this sentence lags.
- `README.md:30`: "Our skills live under `src/skills/`; …" — the `src/` layout sentence names skills only; `src/commands/` and `src/agents/` are absent. (README Setup lines 10/13 already cover the agents symlink — task 17 landed those.)

## Change

- ARCHITECTURE.md: the enumeration names all three symlinks — `~/.claude/skills`, `~/.claude/commands`, and `~/.claude/agents`.
- README.md: the layout sentence extends minimally to name the three `src/` categories, e.g. "Our skills live under `src/skills/` (commands under `src/commands/`, agent definitions under `src/agents/`); …".

## Files & types

- `.ai-factory/ARCHITECTURE.md` (one sentence), `README.md` (one sentence).

## Guards

- Two sentences, two files, nothing else; CLAUDE.md untouched (its registration is already complete).

## Verification

- The ARCHITECTURE sentence names `~/.claude/agents`; the README sentence names all three `src/` categories; `git diff` shows two one-sentence edits.

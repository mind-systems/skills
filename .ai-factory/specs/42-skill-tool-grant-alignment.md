# frontmatter: `Skill` joins `allowed-tools` wherever the body loads via the Skill tool

## Current state

`src/skills/roadmap-prune/SKILL.md:25` instructs "Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool…)" — the deferred-observations gate depends on the engine's marker grammar and **pinned** definition being in context. But `allowed-tools` (`:10`) is `Read Write Edit Bash(git *) Bash(rm *) Glob Grep` — no `Skill`. `allowed-tools` is the pre-approval list: an unlisted tool call raises a permission prompt interactively and is denied outright in headless orchestrator runs, so the gate executes with the grammar unloaded — judging "pinned" from the body's one-line paraphrase or detouring through a `Read` of the engine file (machine-dependent symlink path). The frontmatter `loads:` field is a dependency *declaration* for the grep-derived graph, not a runtime mechanism — only the Skill tool actually injects an engine into context. Same class as milestone 40 (rescue-audit cold-run tools: frontmatter granted fewer tools than the body needed). Origin: a deferred observation recurring across all three plan reviews of 1.8.3 — the rescue swept those files; the observation is preserved here.

## Change

- **Grep-driven inventory at execution time** (files are in flux mid-phase — never trust a static list): every `src/skills/*/SKILL.md` and `src/commands/*.md` whose **body** instructs invoking the Skill tool — start from the `loads:` declarers, then `grep -rn "Skill tool" src/skills/*/SKILL.md src/commands/*.md` to catch loads declared in prose only.
- For each hit whose `allowed-tools` omits `Skill`: append plain `Skill` to the `allowed-tools` line. Plain, unscoped — a scoped `Skill(<name>)` form is unverified frontmatter syntax; do not pin it.
- Frontmatter-only; every body byte-identical.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` (the live case) + whatever files the grep surfaces at execution time.

## Guards

- The `allowed-tools` line is the only edited line per file; `name`, `description`, `argument-hint`, `loads:` untouched.
- The grant is added only where the body demands it — a skill whose body never invokes the Skill tool gets no edit (an unused grant is noise, not hygiene).
- Runs **after 1.8.3** — prune's pyramid pass has an in-flight plan that pins its frontmatter unchanged; avoid the same-file collision.
- Never touch `upstream/ai-factory/`.

## Verification

- Pairing grep: every file whose body mentions the Skill tool carries `Skill` in its `allowed-tools`; zero files with the instruction and without the grant.
- `git diff` shows only `allowed-tools` lines changed.

# Plan: aif: fork into `src/` — CLAUDE.md-first bootstrap, cut the marketplace half

## Context
Fork `upstream/ai-factory/aif` into `src/skills/aif` as ours, repoint the `active/` symlink, and rework it recognizably: cut the skills.sh/security-scan marketplace half, retire DESCRIPTION.md, and make the project `CLAUDE.md` the first artifact every mode produces.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Assumptions / spec reconciliation
- **The ROADMAP line governs over spec note 50 where they diverge.** Note 50 (`.ai-factory/notes/50-aif-fork-claude-md-first.md`) predates the milestone line: it frames this as "targeted edits only" and lists skills.sh acquisition + security scanning + Python detection as **Untouched**. The milestone line supersedes that — "fork … cut the marketplace half", "rework **recognizably** (diff vs upstream shows whole sections deleted)". This plan follows the line: the marketplace half is **cut**. Note 50's four other edits (CLAUDE.md-first, drop DESCRIPTION.md, AGENTS.md one-liner, drop aif-evolve block) are consistent with the line and are all applied.
- **"Cut the marketplace half" is read as: remove the entire skill-acquisition apparatus** — skills.sh search/install, both security-scan levels, the Python-probe ceremony, and the skill-recommendation/custom-generation steps (they were gated on "search skills.sh first, else generate"). None appear in the milestone's Keep list. **MCP configuration is kept** (explicitly in Keep). If the user wants `/aif-skill-generator` custom-skill generation retained, that is the one boundary to confirm.
- Structure/headings of kept sections stay put so a `diff` against upstream reads as clean deletions + the CLAUDE.md addition, not a reshape.
- `references/update-config.mjs` and `references/config-template.yaml` are copied **verbatim** — no edits (they contain no template tokens).
- **Install-time mustache tokens must be resolved to concrete paths.** Upstream SKILL.md is written for the skills.sh installer, which substitutes `{{skills_dir}}`, `{{settings_file}}`, `{{skills_cli_agent_flag}}` at install time. This repo forks directly into `src/` and loads via the `active/` symlink — **there is no substitution step**, and no forked `src/` skill (verified: `aif-docs`) carries any `{{…}}` token. Resolution used throughout this plan: `{{skills_dir}}` → `.claude/skills`, so the `node …update-config.mjs` invocations (run via Bash from the *project* cwd, not the skill dir) become the absolute load path `~/.claude/skills/aif/references/update-config.mjs` (+ `…/config-template.yaml`); `{{settings_file}}` → `.mcp.json` (Claude Code project-scope MCP config); `{{skills_cli_agent_flag}}` disappears with the skills.sh cut.

## Tasks

### Phase 1: Fork & wire

- [x] **Task 1: Copy upstream `aif` into `src/` and repoint the active symlink**
  Files: `src/skills/aif/SKILL.md`, `src/skills/aif/references/update-config.mjs`, `src/skills/aif/references/config-template.yaml`, `active/skills/aif`
  `cp -R upstream/ai-factory/aif src/skills/aif` (brings SKILL.md + `references/` intact). Then repoint the working-set symlink: `ln -sfn ../../src/skills/aif active/skills/aif`. Verify `readlink active/skills/aif` now points at `../../src/skills/aif` and `upstream/ai-factory/aif` is untouched. Do **not** edit the two `references/` files at any point — they stay byte-identical to upstream.

### Phase 2: Cut the marketplace half

- [x] **Task 2: Rewrite frontmatter — drop marketplace/scanner tools, retune description** (depends on Task 1)
  Files: `src/skills/aif/SKILL.md`
  In `allowed-tools`, remove every skills.sh/scanner/Python entry: `Bash(npx skills *)`, all four `Bash(py* --version)` / `Bash(python* --version)` probes, `Bash(python3 *security-scan.py*)` and its `py`/`python` variants, all `*cleanup-blocked-skill.py*` variants, `WebFetch`, and the nonexistent `Questions` pseudo-tool (per note 41 hygiene, `AskUserQuestion` stays). Keep: `Read Glob Grep Write Bash(mkdir *) Bash(node *update-config.mjs*) Skill AskUserQuestion`. Rewrite `description` to drop "installs relevant skills from skills.sh" and the skills-marketplace framing — describe the new scope: analyze the stack, generate the project `CLAUDE.md` + `config.yaml` + `rules/base.md`, configure MCP, hand off to `/aif-architecture`. Keep the trigger phrases ("set up project", "configure AI").

- [x] **Task 3: Delete the security/skill-context/acquisition sections and strip marketplace steps from all modes** (depends on Task 2)
  Files: `src/skills/aif/SKILL.md`
  Delete whole sections (upstream line refs): `## CRITICAL: Security Scanning` + its Python-detection block (~16–69), the `### Project Context` skill-context/aif-evolve block (~73–94), `## Skill Acquisition Strategy` (~96–111), and the intro bullets 2–3 ("Installing skills from skills.sh" / "Generating custom skills"). In Modes 1/2/3 remove: "Recommend Skills & MCP" (keep MCP detection — split the skills column out), "Search skills.sh" steps, and the per-skill install+scan execute steps (Mode 1 Step 7–8). MCP configuration, `config.yaml` persistence, and `rules/base.md` creation stay. Leave headings of kept sections in place so the diff reads as clean deletions.
  **Resolve all surviving `{{…}}` template tokens to concrete paths** (per Assumptions) in the sections that are kept, not cut — no forked `src/` skill carries install-time mustache tokens. Specifically: the two `node ~/{{skills_dir}}/aif/references/update-config.mjs --template ~/{{skills_dir}}/aif/references/config-template.yaml …` invocations (upstream ~212–213 and ~378) → absolute load path `~/.claude/skills/aif/references/…`; every `{{settings_file}}` in the MCP section and Rules (upstream ~394, ~519, ~717) → `.mcp.json`. The `{{skills_cli_agent_flag}}` tokens vanish with the skills.sh install lines removed above. After this task, `grep '{{' src/skills/aif/SKILL.md` must return nothing.

### Phase 3: CLAUDE.md-first bootstrap & artifact rework

- [x] **Task 4: Add CLAUDE.md as the first artifact in every mode** (depends on Task 3)
  Files: `src/skills/aif/SKILL.md`
  Add a `## CLAUDE.md Generation` section and wire a step into each mode **before** any other artifact (before `config.yaml`/`rules/base.md`/MCP/AGENTS.md). The generated project `CLAUDE.md` carries, in English: `## Purpose` (what the project is), `## Status` **only when** there is a real built/target gap worth stating, `## Commands` (derived from the detected package manager / Makefile scripts), stack facts, and a `## Documentation` index section (`| Doc | What it covers |`, empty if no docs yet). Content sources in order of availability: chat context (the common case, not a precondition) → `$ARGUMENTS` → stack scan → the mode's own dialog answers. **Update-not-clobber:** if `CLAUDE.md` already exists, fill only missing sections and never overwrite existing content. State that this artifact does not bake in an assumption that rich chat context is always present.

- [x] **Task 5: Drop DESCRIPTION.md generation; repoint hand-offs to CLAUDE.md** (depends on Task 4)
  Files: `src/skills/aif/SKILL.md`
  Remove every `.ai-factory/DESCRIPTION.md` creation step and its template from Modes 1/2/3 (upstream Step 4 in Mode 1, Step 4 in Mode 2, Step 5 in Mode 3). Anywhere a later step used DESCRIPTION.md as input (the `/aif-architecture` hand-off, the `## Artifact Ownership` block, the completion summary), retarget the reference to the generated `CLAUDE.md`. Keep the final `/aif-architecture` invocation and the "CRITICAL: Do NOT Implement" guard intact — only the input reference changes.

- [x] **Task 6: Collapse the AGENTS.md template to the one-line pointer** (depends on Task 5)
  Files: `src/skills/aif/SKILL.md`
  Replace the multi-section `## AGENTS.md Generation` template (Project Overview / Tech Stack / directory tree / Key Entry Points / Documentation table / AI Context Files / Agent Rules) with a step that writes/ensures a single standing line:
  ```markdown
  See [CLAUDE.md](CLAUDE.md) as the single source of truth for this project.
  ```
  Keep the generation step itself (every mode still emits `AGENTS.md`); if `AGENTS.md` already exists and is richer, reduce it to the pointer per the standing convention. Filename stays `AGENTS.md`.

- [x] **Task 7: Trim the language ceremony; make all artifacts English** (depends on Task 6)
  Files: `src/skills/aif/SKILL.md`
  In `## Language Resolution`: keep resolving `language.ui` from config (`config.yaml` → existing project files) for communication, but **remove the mandatory two-question ceremony** — the "first user question MUST be about UI language, second about Artifact language" rules and the always-asked prompts. Ask the language question(s) **only when config is absent and repository/chat context is insufficient**. Remove `language.artifacts`-driven localized-heading templating everywhere: `rules/base.md`, the completion summary, and any remaining artifact templates now use fixed **English** headings (drop the `[Localized heading: …]` placeholders). The `config.yaml` write via `update-config.mjs` stays exactly as-is (managed keys unchanged; template verbatim) — note that `language.artifacts` therefore remains a **written-but-unconsumed** managed key (artifacts are always English now); this is deliberate to avoid touching the verbatim `update-config.mjs`/template, so a later reader should not "fix" it by re-wiring artifact localization.

- [x] **Task 8: Clean the completion summary/next-steps menu and confirm ≤500 lines** (depends on Task 7)
  Files: `src/skills/aif/SKILL.md`
  Rewrite the completion summary + next-step recommendations in English: list `CLAUDE.md`, `.ai-factory/ARCHITECTURE.md`, and `AGENTS.md` (drop the `DESCRIPTION.md` line). Prune **every** stale slash-command reference down to the active set — active `aif*` skills are `aif`, `aif-architecture`, `aif-skill-generator`, plus our `aif-docs`. In the completion summary drop `/aif-plan`, `/aif-implement`, `/aif-roadmap`. In the **Mode-1 "also suggest next steps" `AskUserQuestion` multi-select** (upstream ~752–768), `/aif-docs` is the only survivor — remove the `/aif-rules`, `/aif-build-automation`, `/aif-ci`, `/aif-dockerize` options (none are in the active set; selecting them invokes skills that don't resolve — the same defect note 36 fixed). If pruning empties the menu to a single option, collapse it to a plain `/aif-docs` recommendation rather than a one-item `AskUserQuestion`. (`## Artifact Ownership` is retargeted by Task 5 — do not touch it here.) Then run `wc -l src/skills/aif/SKILL.md` and confirm ≤ 500. If over, the tightening budget is the **reworked prose only** — the verbatim config-machinery invocation lines and the MCP runtime matrix/canonical-server templates are contract-sensitive (note stresses "template verbatim / managed keys unchanged") and are **excluded** from compression; squeeze the CLAUDE.md/AGENTS.md/language/summary prose instead, with no behavior loss.

### Phase 4: Repo bookkeeping

- [x] **Task 9: Move `aif` to the reconcile-by-diff list in the repo CLAUDE.md** (depends on Task 8)
  Files: `CLAUDE.md`
  In `/Users/max/projects/skills/CLAUDE.md`: (1) in the "active set" paragraph, remove `aif` from "three upstream originals we use as-is: `aif`, `aif-architecture`, `aif-skill-generator`" (now two). (2) In `## Upstream Sync` → "Reconcile reworked skills", add `aif` alongside `aif-docs`/`aif-plan` with its diff command: `diff -rq src/skills/aif upstream/ai-factory/aif`. (3) Ensure `aif` is **not** added to the "Everything else in `src/skills/` is ours … sync never touches it" list (it now has an upstream counterpart to reconcile). Leave the pristine-mirror statements and the `Repository Structure` tree otherwise intact.

## Commit Plan
- **Commit 1** (after tasks 1-3): "Fork aif into src and cut the marketplace half"
- **Commit 2** (after tasks 4-8): "Make CLAUDE.md the first aif artifact; drop DESCRIPTION.md and localized headings"
- **Commit 3** (after task 9): "Move aif to the reconcile-by-diff list in repo CLAUDE.md"

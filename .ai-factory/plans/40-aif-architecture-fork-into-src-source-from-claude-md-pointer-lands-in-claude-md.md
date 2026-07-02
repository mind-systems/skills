# Plan: aif-architecture: fork into `src/` — source from CLAUDE.md, pointer lands in CLAUDE.md

## Context
Fork `upstream/ai-factory/aif-architecture` into `src/skills/aif-architecture` (ours, reworked-from-upstream), repoint the `active/` symlink, and rework it recognizably so context comes from the project CLAUDE.md instead of DESCRIPTION.md and the architecture pointer lands in CLAUDE.md — after this the only upstream original left in `active/` is `aif-skill-generator`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Fork the skill into `src/`

- [x] **Task 1: Copy upstream skill into `src/` and repoint the active symlink**
  Files: `src/skills/aif-architecture/SKILL.md`, `src/skills/aif-architecture/references/architecture.md`, `active/skills/aif-architecture`
  Copy the whole upstream directory as-is first: `cp -r upstream/ai-factory/aif-architecture src/skills/aif-architecture` (brings `SKILL.md` + `references/architecture.md` verbatim — `references/` stays byte-identical, do NOT edit it). Then repoint the symlink: `ln -sfn ../../src/skills/aif-architecture active/skills/aif-architecture`. Do NOT touch the upstream mirror copy at any point. All subsequent edits happen only in `src/skills/aif-architecture/SKILL.md`. This mirrors the just-completed `aif` fork (task 89 / note 50).

### Phase 2: Rework SKILL.md — context source, pointer target, cuts

- [x] **Task 2: Rework Step 0 to source context from CLAUDE.md + codebase scan; cut the skill-context block** (depends on Task 1)
  Files: `src/skills/aif-architecture/SKILL.md`
  Keep the Step 0 `config.yaml` read for **paths** (`paths.architecture`) and **language** (`language.ui` / `language.artifacts`), and keep the config-absent defaults for the architecture path + language. Replace the `.ai-factory/DESCRIPTION.md` read (upstream lines ~28–45) with: read the project's **CLAUDE.md** (Purpose, tech stack, conventions — auto-present in every project) plus a **light codebase scan** (package-manager files, `src/` layout) to infer stack/size/complexity. Keep a manual-input fallback for empty projects (adapt the existing "describe your project manually" prompt so it no longer tells the user to run `/aif` for a DESCRIPTION.md — just ask for build/stack/scale). **Delete** the entire `skill-context` / aif-evolve block (upstream lines ~47–65, "Read `.ai-factory/skill-context/...`" through "Enforcement:") — aif-evolve is not in the active set. Drop the `DESCRIPTION.md: .ai-factory/DESCRIPTION.md` default line. Preserves note 52 direction (no DESCRIPTION.md dependency).

- [x] **Task 3: Keep Step 1 / 1.5 / 2 intact; add `## Features` anchor section to the template; strip localized-heading placeholders** (depends on Task 2)
  Files: `src/skills/aif-architecture/SKILL.md`
  Leave **verbatim**: Step 1 recommendation flow (argument mapping incl. legacy aliases, decision matrix, `AskUserQuestion` recommendation, and the **CRITICAL** "read `references/architecture.md` before generating" instruction), Step 1.5 Codebase Alignment Check, Step 2 template with **both** policy branches (Legacy vs New Code Policy / Code Organization Note), code-example and anti-pattern sections. In the Step 2 template, add a reserved empty section at the **bottom** of the generated `ARCHITECTURE.md`:
  ```markdown
  ## Features
  <!-- roadmap-prune anchors completed features here by commit hash (temporal-tree's anchor store). Leave empty. -->
  ```
  In `## Decision Rationale`, change `[from DESCRIPTION.md]` to `[from CLAUDE.md / codebase]`. Artifacts are English: generated headings stay in plain English (`language.artifacts` still governs body content); do not introduce `[Localized heading: ...]` placeholders in the reworked steps (leave Step 5's `language.ui` confirmation as-is — dialogs still follow config).

- [x] **Task 4: Replace Step 3 with a CLAUDE.md pointer (add-if-absent); delete Step 4 (AGENTS.md); fix frontmatter + Artifact Ownership** (depends on Task 3)
  Files: `src/skills/aif-architecture/SKILL.md`
  Replace **Step 3 "Update DESCRIPTION.md"** with **Step 3 "Update project CLAUDE.md"**: ensure the project's `CLAUDE.md` carries one `## Architecture` pointer line at the resolved architecture path, e.g. `See \`.ai-factory/ARCHITECTURE.md\` for module boundaries, folder structure, and dependency rules.` — **add only if absent**, never duplicate an existing pointer; use the resolved path from config, not the literal default. **Delete Step 4 "Update AGENTS.md"** entirely (AGENTS.md is a one-line pointer to CLAUDE.md — nothing is written there). Renumber the remaining Step 5 "Confirm" if desired but keep its content. Update the `## Artifact Ownership` block: companion update is now the `## Architecture` pointer in the project CLAUDE.md — remove the DESCRIPTION-pointer and AGENTS.md-row mentions. In the **frontmatter**: reword `description` so it no longer says "Analyzes tech stack from DESCRIPTION.md" (say "from the project CLAUDE.md and codebase"); remove `Questions` from `allowed-tools` if unused, and drop `Bash(mkdir *)` only if the mkdir step is gone (Step 2 still creates the parent dir — keep it). Do NOT inline `references/architecture.md` content into the body.

### Phase 3: Repo bookkeeping

- [x] **Task 5: Update repo CLAUDE.md — move aif-architecture to the reconcile list** (depends on Task 4)
  Files: `CLAUDE.md`
  Three edits in the skills-repo `CLAUDE.md`:
  1. Active-set paragraph (line ~62): change "plus **two** upstream originals we use as-is: `aif-architecture`, `aif-skill-generator`" to "plus **one** upstream original we use as-is: `aif-skill-generator`"; add `aif-architecture` to the "our skills" enumeration in that same sentence.
  2. Reconcile-reworked list (lines ~161–164): add a `- \`aif-architecture\` ↔ \`upstream/ai-factory/aif-architecture\`` bullet, and add a matching `diff -rq src/skills/aif-architecture upstream/ai-factory/aif-architecture` line to the example block.
  3. Leave the "Everything else in `src/skills/` is ours" list (line ~171) unchanged — `aif-architecture` is reworked-from-upstream, so it belongs on the reconcile list, not there.

## Commit Plan
- **Commit 1** (after tasks 1–4): "Fork aif-architecture into src with CLAUDE.md-sourced context"
- **Commit 2** (after task 5): "Point repo CLAUDE.md at forked aif-architecture"

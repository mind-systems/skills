---
name: aif
description: Set up agent context for a project. Analyzes tech stack, generates the project CLAUDE.md, config.yaml, and rules/base.md, and configures MCP servers. Use when starting new project, setting up AI context, or asking "set up project", "configure AI".
argument-hint: "[project description]"
allowed-tools: Read Glob Grep Write Bash(mkdir *) Bash(node *update-config.mjs*) Skill AskUserQuestion
---

# AI Factory - Project Setup

Set up agent for your project by:
1. Analyzing the tech stack
2. Generating the project `CLAUDE.md`, `.ai-factory/config.yaml`, and `.ai-factory/rules/base.md`
3. Configuring MCP servers for external integrations
4. Handing off to `/aif-architecture`

## Workflow

**First, determine which mode to use:**

```
Check $ARGUMENTS:
├── Has description? → Mode 2: New Project with Description
└── No arguments?
    └── Check project files (package.json, composer.json, etc.)
        ├── Files exist? → Mode 1: Analyze Existing Project
        └── Empty project? → Mode 3: Interactive New Project
```

---

## CLAUDE.md Generation

**Generate the project's `CLAUDE.md` as the first artifact in every mode** — before `.ai-factory/config.yaml`, `.ai-factory/rules/base.md`, MCP configuration, or `AGENTS.md`.

**Content sources, in order of availability** (use whichever exists; none is a precondition — don't assume rich chat context is always present): chat context (the project intent already discussed, the common case) → `$ARGUMENTS` → stack scan (Mode 1's Scan Project step, or detected package manager / Makefile) → the mode's own dialog answers (stack selection, project description question).

**Sections, fixed English headings:** `## Purpose` (what the project is, 1-3 sentences); `## Status` (only when there is a real built/target gap worth stating, e.g. scaffolding only — omit otherwise); `## Commands` (from the detected package manager or Makefile targets; leave light if no scaffolding exists yet); stack facts (language, framework, database, ORM, as applicable); `## Documentation` (a `| Doc | What it covers |` index table, empty if no docs exist yet).

**Update-not-clobber:** if `CLAUDE.md` already exists, fill only missing sections — never overwrite existing content.

---

## Language Resolution

Immediately after determining Mode 1, Mode 2, or Mode 3, resolve `language.ui` for the entire `/aif` run.

**Run-scoped language state:** `language.ui` drives all `AskUserQuestion` prompts, intermediate explanations, final summary, and next-step recommendations. `language.artifacts` is persisted to `.ai-factory/config.yaml` as a managed key (defaults to `language.ui` when missing) but no longer drives content — every generated artifact (`CLAUDE.md`, `.ai-factory/rules/base.md`, `AGENTS.md`, `.ai-factory/ARCHITECTURE.md`) uses fixed **English** headings and text regardless of this value. `language.technical_terms` preserves its existing value when already set; defaults to `keep` only when missing.

**Resolve `language.ui`** in this order: `.ai-factory/config.yaml` → `AGENTS.md` → `CLAUDE.md` → `RULES.md` → chat/repository context → ask the user only if still unresolved (a fallback, not a mandatory first question). Reuse an already-set value without asking again, and keep the resolved value fixed for the entire run.

All user-facing text examples below are structure examples only. Ask them in resolved `language.ui`, never hard-code English when another UI language was resolved.

**Question to ask only when `language.ui` is still unresolved:**

```
AskUserQuestion: What language should I use for communication during this `/aif` run?

Options:
1. English (en) — Default
2. Russian (ru)
3. Chinese (zh)
4. Other — specify manually
```

Git workflow detection and config.yaml persistence machinery → read `references/config-persistence.md`

Counter-default filter and the `rules/base.md` template → read `references/rules-generation.md`

---

### Mode 1: Analyze Existing Project

**Trigger:** `/aif` (no arguments) + project has config files

**Step 1: Scan Project**

Project-file scan list → read `references/stack-analysis.md`

**Step 2: Resolve Language Settings** — see [Language Resolution](#language-resolution); resolve before generating any setup-time text artifact.

**Step 3: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use Step 1's scan results, chat context, and `$ARGUMENTS`. First artifact written, before config.yaml.

**Step 4: Persist config.yaml**

Immediately after language resolution, create `.ai-factory/` if needed and write `.ai-factory/config.yaml` via `update-config.mjs`.

**Step 5: Recommend MCP**

MCP detection table → read `references/stack-analysis.md`

**Step 6: Present Plan & Confirm**

Present this setup analysis and confirmation prompt in resolved `language.ui`.

```markdown
## 🏭 Project Analysis

**Detected Stack:** [language], [framework], [database if any]

## Setup Plan

### MCP Servers
- [x] [relevant MCP servers]

Proceed? [Y/n]
```

**Step 7: Execute**

1. Save `CLAUDE.md` (generated in Step 3)
2. Create directory: `mkdir -p .ai-factory`
3. Write `.ai-factory/config.update.json` with helper payload (`mode: "create"` if config is missing, `mode: "merge"` if it already exists)
4. Run `node ~/.claude/skills/aif/references/update-config.mjs --template ~/.claude/skills/aif/references/config-template.yaml --target .ai-factory/config.yaml --payload .ai-factory/config.update.json`
5. Delete `.ai-factory/config.update.json` after the helper succeeds
6. **Create rules/base.md**:
   - Ensure `.ai-factory/rules/` directory exists
   - Write `.ai-factory/rules/base.md` with the filtered counter-default rules in English
7. Configure MCP in `.mcp.json`
8. Generate `AGENTS.md` in project root (see [AGENTS.md Generation](#agentsmd-generation))
9. Generate architecture document via `/aif-architecture` only after config exists with resolved language settings (see [CRITICAL: Do NOT Implement](#critical-do-not-implement))

---

### Mode 2: New Project with Description

**Trigger:** `/aif <project description>`

**Step 1: Resolve Language Settings** — see [Language Resolution](#language-resolution), immediately after reading `$ARGUMENTS`.

**Step 2: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use chat context and `$ARGUMENTS`. First artifact written, before config.yaml. Missing sections (e.g. stack facts not yet confirmed) get filled in later, update-not-clobber, once Step 4's dialog answers land.

**Step 3: Persist config.yaml**

Immediately after language resolution, create `.ai-factory/` if needed and write `.ai-factory/config.yaml` via `update-config.mjs`.

**Step 4: Interactive Stack Selection**

Based on project description, ask user to confirm stack choices in resolved `language.ui`. Show YOUR recommendation with "(Recommended)" label, tailored to the project type, and explain why — skip categories that don't apply (e.g. no database for a CLI tool, no framework for a library):
1. **Programming language** — recommend based on project needs (performance, ecosystem, team experience)
2. **Framework** — recommend based on project type (if applicable)
3. **Database** — recommend based on data model (if applicable)
4. **ORM/Query Builder** — recommend based on language and database (if applicable)

**Step 5: Plan MCP Servers**

Based on confirmed stack, identify relevant MCP servers to configure.

**Step 6: Setup Context**

Configure MCP, generate `AGENTS.md`, and generate architecture document via `/aif-architecture` after the earlier helper-driven config write, as in Mode 1.

---

### Mode 3: Interactive New Project (Empty Directory)

**Trigger:** `/aif` (no arguments) + empty project (no package.json, composer.json, etc.)

**Step 1: Resolve Language Settings** — see [Language Resolution](#language-resolution), before asking the project description.

**Step 2: Ask Project Description**

```
I don't see an existing project here. Let's set one up!

What kind of project are you building?
(e.g., "CLI tool for file processing", "REST API", "mobile app", "data pipeline")

> ___
```

Ask this prompt in resolved `language.ui`.

**Step 3: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use the Step 2 description and chat context. First artifact written, before config.yaml. Missing sections (e.g. stack facts not yet confirmed) get filled in later, update-not-clobber, once Step 5's dialog answers land.

**Step 4: Persist config.yaml**

Immediately after language resolution, create `.ai-factory/` if needed and write `.ai-factory/config.yaml` via `update-config.mjs`.

**Step 5: Interactive Stack Selection**

After getting description, proceed with same stack selection as Mode 2:
- Programming language (with recommendation)
- Framework (with recommendation)
- Database (with recommendation)
- ORM (with recommendation)

**Step 6: Setup Context**

Configure MCP, generate `AGENTS.md`, and generate architecture document via `/aif-architecture` after the earlier helper-driven config write, as in Mode 1.

---

## MCP Configuration

MCP runtime format matrix, canonical server templates, and wrapper examples → read `references/mcp-configuration.md`

---

## AGENTS.md Generation

**Generate `AGENTS.md` in the project root** (filename unchanged) as a one-line pointer to `CLAUDE.md`, the single source of truth for this project:

```markdown
See [CLAUDE.md](CLAUDE.md) as the single source of truth for this project.
```

If `AGENTS.md` already exists and is richer than the pointer, reduce it to the pointer per the standing convention; if it doesn't exist, create it with the pointer.

---

## Rules

1. **MCP in `.mcp.json`** — Project-level MCP configuration
2. **Remind about env vars** — For MCP that need credentials

## Artifact Ownership

- Primary ownership in this command: `CLAUDE.md`, setup-time `AGENTS.md`, and MCP configuration.
- Delegated ownership: invoke `/aif-architecture` to create/update `.ai-factory/ARCHITECTURE.md`.
- Read-only context in this command by default: the resolved roadmap, RULES.md, research, and plan artifacts.

## CRITICAL: Do NOT Implement

**This skill ONLY sets up context (MCP). It does NOT implement the project.**

After CLAUDE.md, AGENTS.md, and MCP are configured, **generate the architecture document**:

**Final step: Generate Architecture Document**

Invoke `/aif-architecture` to define project architecture. This creates `.ai-factory/ARCHITECTURE.md` with architecture pattern, folder structure, dependency rules, and code examples tailored to the project.

Present the completion summary and next-step recommendations in resolved `language.ui`. Cover:

```
[Localized completion heading in `language.ui`]

- [Localized project-description label in `language.ui`]: `CLAUDE.md`
- [Localized architecture label in `language.ui`]: `.ai-factory/ARCHITECTURE.md`
- [Localized project-map label in `language.ui`]: `AGENTS.md`
- [Localized MCP-configured label in `language.ui`]: [list]
```

**For existing projects (Mode 1), also suggest next steps:**

Present in resolved `language.ui`: `/aif-docs` — [Localized documentation recommendation in `language.ui`].

**DO NOT:** start writing project code, create project files (`src/`, `app/`, etc.), implement features, or set up project structure beyond CLAUDE.md/MCP/AGENTS.md.

**Your job ends when CLAUDE.md, MCP, and AGENTS.md are configured.** The user decides when to start implementation.

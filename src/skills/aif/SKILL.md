---
name: aif
description: Set up agent context for a project. Analyzes tech stack, generates the project CLAUDE.md and .ai-factory/RULES.md, and configures MCP servers. Use when starting new project, setting up AI context, or asking "set up project", "configure AI".
argument-hint: "[project description]"
allowed-tools: Read Glob Grep Write Bash(mkdir *) Skill AskUserQuestion
---

# AI Factory - Project Setup

Set up agent for your project by:
1. Analyzing the tech stack
2. Generating the project `CLAUDE.md` and `.ai-factory/RULES.md`
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

**Generate the project's `CLAUDE.md` as the first artifact in every mode** — before `.ai-factory/RULES.md`, MCP configuration, or `AGENTS.md`.

**Content sources, in order of availability** (use whichever exists; none is a precondition — don't assume rich chat context is always present): chat context (the project intent already discussed, the common case) → `$ARGUMENTS` → stack scan (Mode 1's Scan Project step, or detected package manager / Makefile) → the mode's own dialog answers (stack selection, project description question).

**Sections, fixed English headings:** `## Purpose` (what the project is, 1-3 sentences); `## Status` (only when there is a real built/target gap worth stating, e.g. scaffolding only — omit otherwise); `## Commands` (from the detected package manager or Makefile targets; leave light if no scaffolding exists yet); stack facts (language, framework, database, ORM, as applicable); `## Documentation` (a `| Doc | What it covers |` index table, empty if no docs exist yet).

**Update-not-clobber:** if `CLAUDE.md` already exists, fill only missing sections — never overwrite existing content.

**Language:** `aif` communicates in the ambient chat/repository language throughout the run — no persisted setting, no resolution step. Generated artifacts — `CLAUDE.md`, `.ai-factory/RULES.md`, `AGENTS.md`, `.ai-factory/ARCHITECTURE.md` — keep fixed **English** headings and text regardless of the ambient language.

---

## Rules Generation

Counter-default filter and the `RULES.md` template → read `references/rules-generation.md`

---

### Mode 1: Analyze Existing Project

**Trigger:** `/aif` (no arguments) + project has config files

**Step 1: Scan Project**

Project-file scan list → read `references/stack-analysis.md`

**Step 2: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use Step 1's scan results, chat context, and `$ARGUMENTS`. First artifact written.

**Step 3: Recommend MCP**

MCP detection table → read `references/stack-analysis.md`

**Step 4: Present Plan & Confirm**

Present this setup analysis and confirmation prompt in the ambient language.

```markdown
## 🏭 Project Analysis

**Detected Stack:** [language], [framework], [database if any]

## Setup Plan

### MCP Servers
- [x] [relevant MCP servers]

Proceed? [Y/n]
```

**Step 5: Execute**

1. Save `CLAUDE.md` (generated in Step 2)
2. Create directory: `mkdir -p .ai-factory`
3. Write `.ai-factory/RULES.md` with the filtered counter-default rules in English
4. Configure MCP in `.mcp.json`
5. Generate `AGENTS.md` in project root (see [AGENTS.md Generation](#agentsmd-generation))
6. Generate architecture document via `/aif-architecture` (see [CRITICAL: Do NOT Implement](#critical-do-not-implement))

---

### Mode 2: New Project with Description

**Trigger:** `/aif <project description>`

**Step 1: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use chat context and `$ARGUMENTS`. First artifact written. Missing sections (e.g. stack facts not yet confirmed) get filled in later, update-not-clobber, once Step 2's dialog answers land.

**Step 2: Interactive Stack Selection**

Based on project description, ask user to confirm stack choices in the ambient language. Show YOUR recommendation with "(Recommended)" label, tailored to the project type, and explain why — skip categories that don't apply (e.g. no database for a CLI tool, no framework for a library):
1. **Programming language** — recommend based on project needs (performance, ecosystem, team experience)
2. **Framework** — recommend based on project type (if applicable)
3. **Database** — recommend based on data model (if applicable)
4. **ORM/Query Builder** — recommend based on language and database (if applicable)

**Step 3: Plan MCP Servers**

Based on confirmed stack, identify relevant MCP servers to configure.

**Step 4: Setup Context**

Configure MCP, write `.ai-factory/RULES.md` with the filtered counter-default rules in English, generate `AGENTS.md`, and generate architecture document via `/aif-architecture`.

---

### Mode 3: Interactive New Project (Empty Directory)

**Trigger:** `/aif` (no arguments) + empty project (no package.json, composer.json, etc.)

**Step 1: Ask Project Description**

```
I don't see an existing project here. Let's set one up!

What kind of project are you building?
(e.g., "CLI tool for file processing", "REST API", "mobile app", "data pipeline")

> ___
```

Ask this prompt in the ambient language.

**Step 2: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use the Step 1 description and chat context. First artifact written. Missing sections (e.g. stack facts not yet confirmed) get filled in later, update-not-clobber, once Step 3's dialog answers land.

**Step 3: Interactive Stack Selection**

After getting description, proceed with same stack selection as Mode 2:
- Programming language (with recommendation)
- Framework (with recommendation)
- Database (with recommendation)
- ORM (with recommendation)

**Step 4: Setup Context**

Configure MCP, write `.ai-factory/RULES.md` with the filtered counter-default rules in English, generate `AGENTS.md`, and generate architecture document via `/aif-architecture`.

---

## MCP Configuration

MCP runtime format matrix, canonical server templates, and wrapper examples → read `references/mcp-configuration.md`

---

## AGENTS.md Generation

**Create `AGENTS.md` in the project root as a symlink to `CLAUDE.md`** (filename unchanged), so any tool that reads `AGENTS.md` gets `CLAUDE.md` — the single source of truth for this project — verbatim:

```bash
ln -sfn CLAUDE.md AGENTS.md
```

If `AGENTS.md` already exists as a regular file, replace it with the symlink; where it holds anything not already in `CLAUDE.md`, fold that into `CLAUDE.md` first, then symlink.

---

## Rules

1. **MCP in `.mcp.json`** — Project-level MCP configuration
2. **Remind about env vars** — For MCP that need credentials

## Artifact Ownership

- Primary ownership in this command: `CLAUDE.md`, setup-time `AGENTS.md`, `.ai-factory/RULES.md`, and MCP configuration.
- Delegated ownership: invoke `/aif-architecture` to create/update `.ai-factory/ARCHITECTURE.md`.
- Read-only context in this command by default: the resolved roadmap, research, and plan artifacts.

## CRITICAL: Do NOT Implement

**This skill ONLY sets up context (MCP). It does NOT implement the project.**

After CLAUDE.md, AGENTS.md, and MCP are configured, **generate the architecture document**:

**Final step: Generate Architecture Document**

Invoke `/aif-architecture` to define project architecture. This creates `.ai-factory/ARCHITECTURE.md` with architecture pattern, folder structure, dependency rules, and code examples tailored to the project.

Present the completion summary and next-step recommendations in the ambient language. Cover:

```
[completion heading]

- Project description: `CLAUDE.md`
- Architecture: `.ai-factory/ARCHITECTURE.md`
- Project map: `AGENTS.md`
- MCP configured: [list]
```

**For existing projects (Mode 1), also suggest next steps:**

Present in the ambient language: `/aif-docs` — documentation recommendation.

**DO NOT:** start writing project code, create project files (`src/`, `app/`, etc.), implement features, or set up project structure beyond CLAUDE.md/MCP/AGENTS.md.

**Your job ends when CLAUDE.md, MCP, and AGENTS.md are configured.** The user decides when to start implementation.

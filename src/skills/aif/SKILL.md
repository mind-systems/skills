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

**Git workflow detection (if `config.yaml` is missing or the `git:` section is incomplete):**

1. Check whether the project uses git:
   - If `.git` exists - set `git.enabled: true`
   - If `.git` does not exist - set `git.enabled: false` and `git.create_branches: false`
2. If git is enabled, detect the default/base branch from git metadata:
   - Prefer `origin/HEAD`
   - Fallback to remote metadata (`git remote show origin`)
   - Fallback to `main`
3. If git is enabled, ask whether full plans should create a new branch (sets `git.create_branches`):

```
AskUserQuestion: How should full plans behave in git?

Options:
1. Create a new branch (Recommended) - a full plan creates a branch and saves as a branch-scoped file
2. Stay on the current branch - a full plan still gets written, but without creating a new branch
```

**Persist resolved settings in `.ai-factory/config.yaml`:**

- Never reconstruct `config.yaml` from memory or by free-writing YAML text.
- Always use `~/.claude/skills/aif/references/update-config.mjs` with `~/.claude/skills/aif/references/config-template.yaml` as the canonical source.
- Write or update `.ai-factory/config.yaml` after `CLAUDE.md` is generated.
- This write MUST happen before `rules/base.md`, MCP config, `AGENTS.md`, and before invoking `/aif-architecture`.
- Ensure `.ai-factory/` exists before writing the payload or target file.
- First write a temporary payload file (for example `.ai-factory/config.update.json`) via `Write`.
- Then invoke the helper:

```bash
node ~/.claude/skills/aif/references/update-config.mjs \
  --template ~/.claude/skills/aif/references/config-template.yaml \
  --target .ai-factory/config.yaml \
  --payload .ai-factory/config.update.json
```

- Use `mode: "create"` when `.ai-factory/config.yaml` does not exist.
- Use `mode: "merge"` when `.ai-factory/config.yaml` already exists.
- Preserve `language.technical_terms` from existing config when present; otherwise set it to `keep` when writing config.
- In `set`, include only values explicitly resolved in the current run and that must be written now.
- In `fillMissing`, include canonical defaults that should be backfilled only when the key or section is missing or incomplete.
- Managed keys for this helper are limited to:
  - `language.ui`
  - `language.artifacts`
  - `language.technical_terms`
  - `paths.*` (including current schema keys such as `paths.qa`)
  - `workflow.*`
  - `git.enabled`
  - `git.base_branch`
  - `git.create_branches`
  - `git.branch_prefix`
  - `git.skip_push_after_commit`
  - `rules.base`
- Never normalize or overwrite `rules.<area>` entries — those are managed by area-specific rules tooling outside this skill.
- The helper must preserve comments, blank lines, section order, inline comments, unknown sections, custom user values outside targeted keys, and the commented `rules.*` examples from the template.
- If the helper reports an unsafe structure or invalid payload, STOP. Do **not** fall back to free-form YAML generation.
- After the helper succeeds, remove the temporary payload file.

**Payload shape:**

```json
{
  "mode": "create|merge",
  "set": {
    "language.ui": "en",
    "language.artifacts": "en",
    "language.technical_terms": "keep",
    "paths.qa": ".ai-factory/qa/"
  },
  "fillMissing": {
    "git.branch_prefix": "feature/",
    "rules.base": ".ai-factory/rules/base.md"
  }
}
```

- Initial create: pass the resolved canonical values through `set`.
- Rerun merge: use `set` only for values re-resolved in this run; use `fillMissing` for canonical defaults that should be restored only when absent or incomplete.

**Create `.ai-factory/rules/base.md` from codebase evidence:**

After language resolution and config write, analyze the codebase as a search for **counter-defaults** — branded/opaque types, serialization quirks, forbidden operations, non-obvious invariants — not as a style-inventory pass. Ground truth in the code shows what *is*; it never shows what must *never* change, so that second thing is what this file exists to carry.

A rule earns its line in `rules/base.md` iff **both**:
- **(a)** the executor would do otherwise by its own defaults, and
- **(b)** code alone cannot teach it.

Every emitted rule **carries its why** — the incident or invariant behind it. This is the costliest instruction surface per line in the whole system (see the composition-model reasoning in `.ai-factory/specs/41-aif-rules-counter-default-filter.md`): the orchestrator reads this file mandatorily at Step 0 of all four agents with override authority, treating every line as mandatory. A line that fails either gate is pure ongoing cost with no benefit.

**Excluded anti-pattern:** generic language/style conventions the agent already follows by default are **not** rules and must never be emitted — this includes case styles (`snake_case`, `PascalCase`, `UPPER_SNAKE_CASE`), formatting, idiomatic naming, and boilerplate error/logging idioms. These fail gate (b): code alone teaches them, so a generated rule restating them is waste, not guidance.

When the codebase surfaces no counter-default, the correct result is a **near-empty file** — header note plus nothing. The criterion admits nothing rather than manufacturing rules to fill sections.

Create `.ai-factory/rules/base.md` with only the rules that pass the filter above. Use fixed **English** headings and service text in this file:

```markdown
# Project Base Rules

> Counter-defaults the executor would otherwise violate by its own defaults, each with its why. Generic style/formatting conventions are deliberately excluded. If the codebase has no counter-default, this file stays empty below this note — that is the correct result, not a gap to fill in.

## Data Types

- Proto numeric fields are carried as strings, not native ints — why: cross-language proto codegen silently truncates int64 on JS clients.

## Identifiers

- Entity IDs use branded/opaque types (e.g. `UserId`), never raw `string` — why: prevents accidental mixing of unrelated entity IDs at compile time.

## Migrations

- No hand-written SQL migrations — all schema changes go through the generator — why: hand-written migrations previously drifted from the ORM schema and broke a prod rollback.
```

*The sections and rules above (modeled on `tradeoxy_core/RULES.md`) are illustrative of the **genre** only, not a literal scaffold — generation must substitute the target project's own counter-defaults. Never emit these literal proto/branded-ID/migration rules into a project that has no protos, branded IDs, or migrations. Emit a section only where a real counter-default was found; an idiomatic or greenfield project correctly yields just the header note with no sections below it.*

---

### Mode 1: Analyze Existing Project

**Trigger:** `/aif` (no arguments) + project has config files

**Step 1: Scan Project**

Read these files (if they exist):
- `package.json` → Node.js dependencies
- `composer.json` → PHP (Laravel, Symfony)
- `requirements.txt` / `pyproject.toml` → Python
- `go.mod` → Go
- `Cargo.toml` → Rust
- `docker-compose.yml` → Services
- `prisma/schema.prisma` → Database schema
- Directory structure (`src/`, `app/`, `api/`, etc.)

**Step 2: Resolve Language Settings** — see [Language Resolution](#language-resolution); resolve before generating any setup-time text artifact.

**Step 3: Generate CLAUDE.md** — see [CLAUDE.md Generation](#claudemd-generation); use Step 1's scan results, chat context, and `$ARGUMENTS`. First artifact written, before config.yaml.

**Step 4: Persist config.yaml**

Immediately after language resolution, create `.ai-factory/` if needed and write `.ai-factory/config.yaml` via `update-config.mjs`.

**Step 5: Recommend MCP**

| Detection | MCP |
|-----------|-----|
| Prisma/PostgreSQL | `postgres` |
| GitHub repo (.git) | `github` |

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

AI Factory writes MCP config to `.mcp.json`, but the outer settings shape depends on the runtime.

### Runtime Format Matrix

| Runtime | Write under | Entry shape |
|---------|-------------|-------------|
| Standard MCP runtimes (Claude Code, Cursor, Roo Code, Kilo Code, Qwen Code, Universal / Other) | `mcpServers.<server>` | `{ "command": "...", "args": [...], "env": {...} }` |
| OpenCode | `mcp.<server>` | `{ "type": "local", "command": ["...", "..."], "environment": {...} }` |
| GitHub Copilot | `servers.<server>` | `{ "type": "stdio", "command": "...", "args": [...], "env": {...} }` |
| Codex app | `[mcp_servers.<server>]` in `.codex/config.toml` | `command = "..."`, optional `args = [...]`, credential placeholders as `env_vars = ["VAR"]`, literal values under `[mcp_servers.<server>.env]` |

Use the canonical server templates below as the source values, then wrap them using the runtime-specific format above.

### Canonical Server Templates

#### GitHub
**When:** Project has `.git` or uses GitHub

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
  }
}
```

#### Postgres
**When:** Uses PostgreSQL, Prisma, Drizzle, Supabase

```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": { "DATABASE_URL": "${DATABASE_URL}" }
  }
}
```

#### Filesystem
**When:** Needs advanced file operations

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
  }
}
```

#### Playwright
**When:** Needs browser automation, web testing, interaction via accessibility tree

```json
{
  "playwright": {
    "command": "npx",
    "args": ["-y", "@playwright/mcp@latest"]
  }
}
```

### Runtime-Specific Wrapper Examples

Standard MCP runtimes (`mcpServers`):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

OpenCode (`mcp` + `type: "local"` + command array):

```json
{
  "mcp": {
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

GitHub Copilot (`servers` + `type: "stdio"`):

```json
{
  "servers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

Codex app (`.codex/config.toml` + `mcp_servers` TOML tables):

```toml
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "."]

[mcp_servers.github]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-github"]
env_vars = ["GITHUB_TOKEN"]
```

For GitHub Copilot, convert credential placeholders from `${VAR}` to `${env:VAR}` in the final config file. For OpenCode, use `environment` instead of `env` when the server requires credentials. For Codex app, convert credential placeholders from `${VAR}` to `env_vars = ["VAR"]`; only literal values belong under `[mcp_servers.<server>.env]`.

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

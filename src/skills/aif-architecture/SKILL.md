---
name: aif-architecture
description: Generate architecture guidelines for the project. Analyzes tech stack from the project CLAUDE.md and codebase, recommends an architecture pattern, and creates .ai-factory/ARCHITECTURE.md. Use when setting up project architecture, asking "which architecture", or after /aif setup.
argument-hint: "[microservices|layers|structured|structured-layers|structured-vertical|explicit|explicit-layers|explicit-vertical|explicit-flat] (legacy aliases: clean, ddd, monolith, vertical → mapped to explicit or structured)"
allowed-tools: Read Write Glob Grep Bash(mkdir *) AskUserQuestion
disable-model-invocation: false
---

# Architecture - Generate Architecture Guidelines

Generate `.ai-factory/ARCHITECTURE.md` with architecture decisions tailored to the project.

## Workflow

### Step 0: Load Config & Project Context

**FIRST:** Read `.ai-factory/config.yaml` if it exists to resolve:
- **Paths:** `paths.architecture`
- **Language:** `language.ui` for prompts and `language.artifacts` for generated architecture content

When invoked by `/aif`, assume `.ai-factory/config.yaml` has already been written for the current setup run and already contains the resolved `language.ui` / `language.artifacts` values.

If config.yaml doesn't exist, use defaults:
- ARCHITECTURE.md: `.ai-factory/ARCHITECTURE.md`
- Language: `en` (English)

**THEN:** Read the project's `CLAUDE.md` if it exists to understand:
- Purpose (what the project is)
- Tech stack (language, framework, database, ORM)
- Conventions already documented

**Also run a light codebase scan** to infer project size and complexity:
- Package-manager files (`package.json`, `composer.json`, `requirements.txt`/`pyproject.toml`, `go.mod`, `Cargo.toml`, etc.)
- `src/` (or equivalent) directory layout

**If `CLAUDE.md` does not exist and the codebase scan finds nothing:**
```
⚠️  No project context found.

Describe your project manually:
- What are you building?
- Tech stack (language, framework, database)?
- Team size?
- Expected scale?
```

Allow standalone usage — if user provides manual input, use that instead.

### Step 1: Recommend Architecture

Based on project context, evaluate against the decision matrix and recommend an architecture:

**If `$ARGUMENTS` specifies an architecture** (e.g., `/aif-architecture explicit`):
- **Direct mapping** (no suffix needed):
  - `layers` → Layered Architecture
  - `microservices` → Microservices
  - `structured` → Structured Modules (ask variant — see below)
  - `explicit` → Explicit Architecture (ask variant — see below)
- **Legacy aliases** (deprecated, mapped to current patterns — may be removed in future):
  - `clean` → Explicit Architecture
  - `ddd` → Explicit Architecture
  - `monolith` → Structured Modules
  - `vertical` → Explicit Architecture (Vertical Slice By Entity)
- **With suffix** (variant is determined, no need to ask):
  - `structured-layers` → Structured Modules (Technical Layer)
  - `structured-vertical` → Structured Modules (Vertical Slices By Entity)
  - `explicit-layers` → Explicit Architecture (Technical Layer)
  - `explicit-vertical` → Explicit Architecture (Vertical Slice By Entity)
  - `explicit-flat` → Explicit Architecture (Flat Vertical Slice - Simplified)
- **Without suffix** (ask user to choose variant):
  - If `structured` is specified without a suffix: ASK the user: "Which folder structure variant do you prefer for Structured Modules? 1. Technical Layer (simpler) or 2. Vertical Slices by Entity (better for large modules)". Wait for their answer before generating the artifact.
  - If `explicit` is specified without a suffix: ASK the user: "Which folder structure variant do you prefer for Explicit Architecture? 1. Technical Layer or 2. Explicit Architecture (Vertical Slice By Entity) or 3. Explicit Architecture (Flat Vertical Slice - Simplified)". Wait for their answer before generating the artifact.
- Use the resolved architecture directly, skip the recommendation step and proceed to Step 1.5

**If no specific architecture requested:**
- Evaluate the project against the decision matrix (see `references/architecture.md`)
- Consider: team size, domain complexity, scale requirements, tech stack
- Present recommendation via `AskUserQuestion`:

```
Based on your project context:
- [reason 1 from project analysis]
- [reason 2 from project analysis]

Which architecture pattern should we use?

1. [Recommended pattern] (Recommended) — [why it fits]
2. [Alternative 1] — [brief reason]
3. [Alternative 2] — [brief reason]
4. [Alternative 3] — [brief reason]
```

Architecture options:
- **Structured Modules (Technical Layer)**
- **Structured Modules (Vertical Slices By Entity)**
- **Explicit Architecture (Technical Layer)**
- **Explicit Architecture (Vertical Slice By Entity)**
- **Explicit Architecture (Flat Vertical Slice - Simplified)**
- **Microservices**
- **Layered Architecture**
(See `references/architecture.md` for detailed descriptions of these patterns to formulate your recommendation).

**CRITICAL INSTRUCTION:** You MUST read `references/architecture.md` before generating the `ARCHITECTURE.md` artifact to ensure correct terminology, dependency directions.

### Step 1.5: Codebase Alignment Check

**CRITICAL:** Before generating the document, compare the chosen architecture's ideal folder structure (from `references/architecture.md`) against the actual existing codebase structure.

- If the project is empty or mostly matches: proceed to Step 2.
- **If there are significant discrepancies:** DO NOT silently merge the ideal architecture with the messy reality. You MUST stop and ask the user how to proceed via `AskUserQuestion`:

```
The current project structure differs significantly from the ideal [Pattern Name] architecture.
[Briefly list 1-2 major differences]

How should we generate the ARCHITECTURE.md?
1. Adapt the guidelines to fit the existing application structure (document reality).
2. Generate the pure, strict architecture guidelines (requires refactoring the application later to match).
```
Wait for their decision before proceeding to Step 2.

### Step 2: Generate the Architecture Artifact

Create the parent directory for the resolved architecture path if needed.

Generate the resolved architecture artifact (default: `.ai-factory/ARCHITECTURE.md`) with the following structure, **adapted to the project's tech stack and language**:

→ read `references/architecture-template.md` and generate the artifact from it, adapted to the project's tech stack and language.

**The generated `ARCHITECTURE.md` MUST end with an empty `## Features` section** reserved for `roadmap-prune`/`temporal-tree` to anchor completed features by commit hash — never omit or pre-fill it.

### Step 3: Update project CLAUDE.md

Ensure the project's `CLAUDE.md` carries one `## Architecture` pointer line at the resolved architecture path. Use the resolved architecture path from config, not the default path literal.

- **Add only if absent** — if `CLAUDE.md` already has an `## Architecture` section or an equivalent pointer to the resolved architecture path, do not duplicate it.
- If `CLAUDE.md` doesn't exist, skip this step (standalone usage without `/aif` setup).

```markdown
## Architecture
See `[resolved-architecture-path]` for module boundaries, folder structure, and dependency rules.
```

### Step 4: Confirm

Present the confirmation in resolved `language.ui` and report the resolved architecture path:

```
[Localized success heading in `language.ui`]

[Localized pattern label in `language.ui`]: [chosen pattern]
[Localized file label in `language.ui`]: [resolved architecture path]

[Localized key-rules heading in `language.ui`]:
- [rule 1]
- [rule 2]
- [rule 3]

[Localized closing sentence in `language.ui` about workflow skills following these architecture guidelines.]
```

## Artifact Ownership

- Primary ownership: the resolved architecture artifact path (default: `.ai-factory/ARCHITECTURE.md`).
- Respect config overrides: write to the resolved architecture path from `config.yaml` when provided.
- Allowed companion update: the `## Architecture` pointer line in the project `CLAUDE.md`.
- Read-only context: roadmap, rules, research, and plan artifacts unless user explicitly requests otherwise.

---

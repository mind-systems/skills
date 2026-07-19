---
name: aif-docs
description: Generate and maintain project documentation as a present-tense governing spec of behavior, protocols, data flows, and connections — split by topic in the configured docs directory, with a lean README (plus its onboarding relatives) as the exception. Use when user says "create docs", "write documentation", "update docs", "generate readme", "document project", "напиши ТЗ", or "техническое задание".
argument-hint: "[--web]"
allowed-tools: Read Write Edit Glob Grep Bash(mkdir *) Bash(npx *) Bash(python *) AskUserQuestion WebFetch WebSearch
disable-model-invocation: false
metadata:
  author: AI Factory
  version: "1.0"
  category: documentation
---

# Documentation Generator

Generate, maintain, and improve project documentation as the project's **governing spec** — present-tense behavior, protocols, data flows, and connections — landing on a lean README + detailed docs-directory structure. README and its onboarding relatives (CHANGELOG.md, CONTRIBUTING.md, LICENSE) are the exception to that genre, not its center.

## Core Principles

Everything written under the resolved docs directory (`paths.docs`, default: `docs/`) is governing-spec genre — behavior, protocols, data flows, connections, stated in present tense — whether the code behind it exists yet or not. Only the onboarding surface (README + its relatives) is exempt from that genre.

1. **README is a landing page, not a manual.** ~80-120 lines. First impression, install, quick example, links to details.
2. **Details go to the resolved docs directory** (`paths.docs`, default: `docs/`). Each file is self-contained — one topic, one page. A user should be able to read a single doc file and get the full picture on that topic.
3. **No duplication — one home per fact.** Structure and boundaries live in ARCHITECTURE.md; behavior lives in the topic docs; the documentation index lives in the project's CLAUDE.md (a `## Documentation` table, `| Doc | What it covers |`); onboarding lives in README + its relatives (CHANGELOG.md, CONTRIBUTING.md, LICENSE). A fact stated in two homes becomes a link from the second to the first — README carries at most one pointer line to the docs directory, never an index table. Exception: the installation command can appear in both README and getting-started.md (users expect it in README).
4. **Cross-links use relative paths.** From README: link to the resolved docs directory path (for example `docs/workflow.md` by default). Between doc pages in the same directory: `workflow.md`.
5. **Scannable.** Use tables, bullet lists, and code blocks. Avoid long paragraphs. Users scan, they don't read.
6. **State, not process.** Every sentence describes **what is** — factual present-tense behavior, structure, or API. Never state how something came to be: no "we changed", "was added", "this replaces", "previously", "because we", "this milestone". History belongs in commit messages. This rule applies to every run, no exceptions.

## Workflow

### Step 0: Load Config & Project Context

**FIRST:** Read `.ai-factory/config.yaml` if it exists to resolve:
- **Paths:** `paths.architecture` and `paths.docs`
- **Language:** `language.ui` for prompts and `language.artifacts` for generated docs

If config.yaml doesn't exist, use defaults:
- ARCHITECTURE.md: `.ai-factory/ARCHITECTURE.md`
- Docs directory: `docs/`
- Language: `en` (English)

**Note:** `README.md` remains the landing page in the project root. Detailed docs are written to the resolved `paths.docs` directory (default: `docs/`).

**Also read `.ai-factory/ARCHITECTURE.md`** (use path from config) if it exists to align documentation with the project's structure and boundaries.

**Explore the codebase:**
- Read `package.json`, `composer.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, etc.
- Scan `src/` structure to understand architecture
- Look for existing docs, comments, API endpoints, CLI commands
- Check for existing README.md and the resolved docs directory

**Scan for scattered markdown files in project root:**

Use `Glob` to find all `*.md` files in the project root (exclude `node_modules/`, `.ai-factory/`, agent dirs):

```
CHANGELOG.md, CONTRIBUTING.md, ARCHITECTURE.md, DEPLOYMENT.md,
SECURITY.md, API.md, SETUP.md, DEVELOPMENT.md, TESTING.md, etc.
```

Record each file, its size, and a brief summary of its content. This list is used in Step 1.1.

### Step 0.1: Parse Flags

```
--web  → Generate HTML version of documentation
```

### Step 1: Determine Current State

Determine the subject to document — behavior, invariants, protocols, data flows, and connections. Where the code exists, read it and treat it as the referent. Where it does not yet exist, treat the doc itself as the contract: gather the target behavior from the stated user intent, task spec, or ROADMAP phase if one is discoverable, and write it in present tense as if it already ships. Then check what documentation already exists:

```
State A: No README.md                        → Full generation (README + docs dir)
State B: README.md exists, no docs dir      → Analyze README, propose split into docs dir
State C: README.md + docs dir exist         → Depends on flags (see below)
```

**State C with `--web` flag — ask the user:**

```
Documentation already exists (README.md + resolved docs directory).

AskUserQuestion: What would you like to do?

Options:
1. Generate HTML only — build site from current docs as-is
2. Audit & improve first — check for issues, then generate HTML
3. Audit only — check for issues without generating HTML
```

**Based on choice:**
- Generate HTML only → skip Step 1.1, Step 2, Step 4 — go directly to Step 3 (HTML generation), then done
- Audit & improve first → run Step 1.1 → Step 2 (State C) → Step 3 → Step 4 → Step 4.1
- Audit only → run Step 1.1 → Step 2 (State C) → Step 4 → Step 4.1 (skip Step 3)

**State C without `--web` flag** → run Step 2 (State C) as usual.

### Step 1.1: Check for Scattered Markdown Files

If scattered `.md` files were found in the project root (from Step 0), propose consolidating them into the resolved docs directory.

Consolidation targets and the sample proposal dialog → read `references/consolidation.md`.

**If scattered files found, ask the user:**

```
AskUserQuestion: Would you like to apply the consolidation?

Options:
1. Apply all suggestions
2. Let me pick which ones
3. Skip — keep files where they are
```

**Based on choice:**
- Apply all suggestions → move/merge all listed files, continue to Step 2
- Let me pick which ones → present each file individually for approval, apply selected
- Skip → leave files where they are, continue to Step 2

**When moving/merging:**
1. Create the target file in the resolved docs directory
2. If merging into an existing doc — append content under a new section header, avoid duplicating info that's already there
3. **Do NOT delete originals yet** — keep them until the review step confirms everything is in place
4. Add the new doc page to CLAUDE.md's Documentation section
5. Update any links in other files that pointed to the old root-level file
6. Record which files were moved/merged — this list is used in Step 4.1

**IMPORTANT:** Never force-move files. Always show the plan and get user approval first.

### Update the CLAUDE.md Documentation Index

Create or update the `## Documentation` section in the project's CLAUDE.md — this is the single home for the documentation index (not README):

```markdown
## Documentation

| Doc | What it covers |
|-----|-----------------|
| [Getting Started](<repo-root-to-docs-dir>/getting-started.md) | Installation, setup, first steps |
| [Architecture](<repo-root-to-docs-dir>/architecture.md) | Project structure and patterns |
```

- One row per doc page in the resolved docs directory — README is **not** listed
- Descriptions under ~12 words
- Rows follow the docs directory's logical reading order (getting started → workflow → details)
- If CLAUDE.md doesn't exist, create it with only this section plus a one-line header

### Step 2 (State A): Generate from Scratch

When no README.md exists, generate the full documentation set.

→ read `references/generate-state-a.md`

### Step 2 (State B): Split Existing README into the resolved docs directory

When README.md exists but is long (150+ lines) and there's no resolved docs directory yet.

→ read `references/split-state-b.md`

### Step 2 (State C): Improve Existing Docs

When both README.md and the resolved docs directory exist.

→ read `references/audit-state-c.md`

### Step 3: Generate HTML Version (--web flag)

When `--web` flag is passed, generate a static HTML site from the markdown docs.

File mapping: `README.md` → `index.html`, `<resolved docs dir>/*.md` → `*.html`.

HTML build mechanics → read `references/html-generation.md` when `--web` is passed.

## Step 4: Documentation Review

**MANDATORY after any content change** (generation, split, improvement, file consolidation). Do NOT skip this step.

**Skip this step** only when "Generate HTML only" was chosen — no content was modified, nothing to review.

Read every generated/modified file and evaluate it against both checklists from `references/REVIEW-CHECKLISTS.md`. Two checklists: **Technical Accuracy** and **Readability & Completeness**.

**No-motivation pass (mandatory):** Before presenting any result, scan every generated or modified file for motivation/history/process language. Flag and remove any sentence containing: "we changed", "was added", "was replaced", "this replaces", "previously", "because we", "this milestone", "was introduced", "has been". Rewrite flagged sentences to describe the current (or target) state in present tense.

Fix any issues found before presenting the result to the user. Display results as a compact table with ✅/❌/⚠️ status per item.

**Referent-conditional Technical Accuracy checks:** Each of the following Technical Checklist items is conditional on the referent existing — verified against the code where the documented surface exists, skipped (the doc is the spec) where it does not:
- "Code examples use the project's actual commands/syntax"
- "Installation instructions are real and work (verified from package manager files)"
- Stale-content / broken-reference checks against the live codebase

The Readability & Completeness checklist, README length, and the no-motivation pass (Principle 6) run unconditionally, regardless of referent.

### Step 4.1: Clean Up Moved Files

**Only if files were moved/merged from root into docs/ during Step 1.1.**

After the review confirms all content is correctly placed in `docs/`, offer to delete the original root-level files:

```
The following root files have been incorporated into docs/:

  CONTRIBUTING.md → now in docs/contributing.md
  ARCHITECTURE.md → now in docs/architecture.md
  DEPLOYMENT.md → now in docs/deployment.md
  SETUP.md → merged into docs/getting-started.md

AskUserQuestion: These originals are no longer needed. Delete them?

Options:
1. Yes, delete all originals
2. Let me pick which ones to delete
3. No, keep them (I'll clean up later)
```

**Based on choice:**
- Yes, delete all → delete all listed originals (see "When deleting" below)
- Let me pick → present each file individually, delete only approved
- No, keep them → leave originals in place, continue to Step 5

**When deleting:**
1. Verify one more time that the target docs/ file contains all content from the original
2. Delete the root file
3. Run `git status` to show what was deleted — user can restore with `git checkout` if needed

**Do NOT auto-delete.** Always ask. The user may want to keep originals temporarily for reference or diff comparison.

### Step 5: Update AGENTS.md

**After any documentation changes**, update the Documentation section in `AGENTS.md` (if the file exists).

Read `AGENTS.md` and find the `## Documentation` section. Update it to reflect the current state of all documentation files:

```markdown
## Documentation
| Document | Path | Description |
|----------|------|-------------|
| README | README.md | Project landing page |
| Getting Started | `<resolved docs dir>/getting-started.md` | Installation, setup, first steps |
| Architecture | `<resolved docs dir>/architecture.md` | Project structure and patterns |
| API Reference | `<resolved docs dir>/api.md` | Endpoints, request/response formats |
| Configuration | `<resolved docs dir>/configuration.md` | Environment variables, config files |
```

**Rules:**
- List README.md first, then all doc files in the resolved docs directory in the same order as the CLAUDE.md `## Documentation` section (docs directory's logical reading order)
- If files were moved/merged from root during Step 1.1, reflect the new locations
- If new doc pages were created, add them
- If doc pages were removed, remove them
- Keep descriptions concise (under 10 words)
- If `AGENTS.md` doesn't exist, skip this step silently
- If `AGENTS.md` is a symlink to CLAUDE.md, the CLAUDE.md `## Documentation` section (see "Update the CLAUDE.md Documentation Index") is the single source and AGENTS.md is left untouched

### Context Cleanup

Suggest the user to free up context space if needed: `/clear` (full reset) or `/compact` (compress history).

## Artifact Ownership

- Primary ownership: `README.md`, `<resolved docs dir>/*`, the Documentation section in `AGENTS.md`, and the `## Documentation` section in `CLAUDE.md`.
- Config use: `config.yaml` resolves `paths.architecture`, `paths.docs`, `language.ui`, and `language.artifacts`.
- Read-only context: `.ai-factory/ARCHITECTURE.md`, roadmap/rules/research artifacts unless the user explicitly asks for broader edits.

## Important Rules

1. **Always ask before making changes** to existing documentation — show the plan first
2. **Never delete content** without moving it somewhere else
3. **Detect real project info** — don't invent features, read package.json/config files
4. **Use the project's language** — if project README is in Russian, write docs in Russian
5. **Preserve existing badges/logos** — don't remove them during restructuring
6. **Add to .gitignore** if generating HTML: add `docs-html/` to .gitignore
7. **Ownership boundary** — this command owns documentation artifacts (`README.md`, `<resolved docs dir>/*`, the Documentation section in `AGENTS.md`, and the `## Documentation` section in `CLAUDE.md`), not the roadmap, RULES.md, or research artifacts resolved from config. The CLAUDE.md ownership is scoped to that section only, not the whole file

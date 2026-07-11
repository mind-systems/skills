# Plan: 1.9.2 — aif: pyramid pass

## Context
Slim `src/skills/aif/SKILL.md` (491 lines, the package's heaviest top) to a lens by moving stack-analysis detail, MCP mechanics, the `rules/base.md` template, and the config.yaml persistence machinery into `references/` **byte-identical** — progressive disclosure per the aif-docs diet. Behavior stays identical; only the body shrinks and gains per-topic pointers.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Discipline (applies to every task)
- **Byte-identical moves.** Text moved into `references/` is cut and pasted verbatim — no rewording, no reformatting, no re-filtering. The rules template is already the 1.9.1-filtered version (counter-default gate + why genre); the move must not resurrect any pre-filter example.
- **Verbatim-protected blocks** stay byte-identical wherever they land: the config.yaml machinery (`update-config.mjs` invocation, payload shape, managed-keys list — the fork's own contract), the CLAUDE.md update-not-clobber rule, and the mode-detection wording. Protection is by criterion, not enumeration — any sentence stating a contract is protected even if unlisted here.
- **Frontmatter unchanged.** `name`, `description`, `argument-hint`, `allowed-tools` stay exactly as they are.
- **Diffability.** The reconcile-by-diff relationship with `upstream/ai-factory/aif` (noted in the repo CLAUDE.md) must stay meaningful: moved content is diffable because it is byte-identical, merely relocated. Do **not** record the source→reference mapping in the skill body; the spec note (`.ai-factory/specs/29-aif-pyramid-pass.md`) already carries the "Move to references" mapping.
- **Body keeps the lens:** the three-mode skeleton + mode detection, CLAUDE.md-first ordering, the language-resolution rule, the final `/aif-architecture` call, AGENTS.md pointer, Artifact Ownership, "Do NOT Implement" — plus one-line pointers to each reference.
- **Pointer style** (match aif-docs): `<topic> → read \`references/<file>.md\``.

## Tasks

### Phase 1: Capture behavior baseline

- [x] **Task 1: Capture pre-change baseline artifacts**
  Files: (scratch project, no repo files)
  Before editing anything, run `/aif` against the **current** skill in a throwaway scratch project (or replay the last known-good run) and save the generated `CLAUDE.md`, `.ai-factory/config.yaml`, and `.ai-factory/rules/base.md` as the baseline for the final diff (spec Verification: baseline diff → empty). Note the exact mode/inputs used so the post-change run in Task 7 is identical.

### Phase 2: Extract detail into `references/` (byte-identical)

- [x] **Task 2: Move MCP mechanics to `references/mcp-configuration.md`**
  Files: `src/skills/aif/references/mcp-configuration.md` (new)
  Cut the entire `## MCP Configuration` section — Runtime Format Matrix, Canonical Server Templates (GitHub/Postgres/Filesystem/Playwright), Runtime-Specific Wrapper Examples, and the credential-conversion notes for Copilot/OpenCode/Codex — into the new file byte-identical. Give the file a short H1 heading only; no rewording of the moved content.

- [x] **Task 3: Move config.yaml machinery to `references/config-persistence.md`** (depends on Task 2)
  Files: `src/skills/aif/references/config-persistence.md` (new)
  Cut the **Git workflow detection** block and the **Persist resolved settings in `.ai-factory/config.yaml`** block (helper invocation, `update-config.mjs` command, managed-keys list, comment-preservation rules, Payload shape, create/merge guidance) into the new file byte-identical. This is the fork-contract machinery — verbatim, no edits. Leave the **Language Resolution** rule itself (resolution order + the language-selection question) in the body; only the git/config-persistence mechanics move.

- [x] **Task 4: Move rules template to `references/rules-generation.md`** (depends on Task 3)
  Files: `src/skills/aif/references/rules-generation.md` (new)
  Cut the "Create `.ai-factory/rules/base.md` from codebase evidence" block — the counter-default framing, the two-gate filter (a)+(b), the excluded-anti-pattern paragraph, the near-empty-file rule, the `# Project Base Rules` template, and the genre/illustrative note — into the new file byte-identical. This content is already the 1.9.1-filtered version; preserve it exactly, do not reintroduce pre-filter examples.

- [x] **Task 5: Move stack-analysis detail to `references/stack-analysis.md`** (depends on Task 4)
  Files: `src/skills/aif/references/stack-analysis.md` (new)
  Cut the project-file scan list (Mode 1 Step 1: `package.json` → Node, `composer.json` → PHP, `requirements.txt`/`pyproject.toml` → Python, `go.mod`, `Cargo.toml`, `docker-compose.yml`, `prisma/schema.prisma`, directory structure) and the MCP detection table (Mode 1 Step 5: Prisma/PostgreSQL → `postgres`, `.git` → `github`) into the new file byte-identical.

### Phase 3: Slim the body and wire pointers

- [x] **Task 6: Remove moved blocks from `SKILL.md` and insert pointers** (depends on Tasks 2–5)
  Files: `src/skills/aif/SKILL.md`
  Delete the four moved blocks from their original locations and replace each with a single one-line pointer at the same site:
  - Language Resolution section → `Git workflow detection and config.yaml persistence machinery → read \`references/config-persistence.md\``
  - Where the rules block was → `Counter-default filter and the \`rules/base.md\` template → read \`references/rules-generation.md\``
  - Mode 1 Step 1 (Scan Project) → `Project-file scan list → read \`references/stack-analysis.md\``; Mode 1 Step 5 (Recommend MCP) → `MCP detection table → read \`references/stack-analysis.md\``
  - `## MCP Configuration` → `MCP runtime format matrix, canonical server templates, and wrapper examples → read \`references/mcp-configuration.md\``
  Keep every Mode's step **sequence** intact (each mode still names its Persist-config / rules / MCP steps as brief instructions, now pointing to the reference for the machinery). Keep the CLAUDE.md Generation section, update-not-clobber rule, mode-detection block, AGENTS.md Generation, Rules, Artifact Ownership, and the CRITICAL/`/aif-architecture` final step in the body verbatim. Verify the body is **materially under 300 lines** and every reference file is reachable from a pointer.

### Phase 4: Verify behavior-identical

- [x] **Task 7: Baseline diff → empty** (depends on Tasks 1, 6)
  Files: (scratch project, no repo files)
  Re-run `/aif` in a scratch project with the **same** mode/inputs as Task 1 and diff the generated `CLAUDE.md`, `.ai-factory/config.yaml`, and `.ai-factory/rules/base.md` against the Task 1 baseline. The diff must be empty. If anything differs, a moved block was altered — fix to byte-identity, do not adjust the baseline.

## Commit Plan
- **Commit 1** (after tasks 2-5): "Move aif stack-analysis, MCP, rules, and config machinery to references"
- **Commit 2** (after tasks 6-7): "Slim aif SKILL.md body to a lens over references"

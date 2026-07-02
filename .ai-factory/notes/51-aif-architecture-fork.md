# aif-architecture: fork into src/ — source from CLAUDE.md, pointer lands in CLAUDE.md

**Date:** 2026-07-02
**Source:** conversation context (aif/aif-architecture review)

## Key Findings

- `upstream/ai-factory/aif-architecture` (260 lines) has a sound core — the pattern decision matrix (`references/architecture.md`), the Codebase Alignment Check (Step 1.5: document reality vs strict architecture), and the ARCHITECTURE.md template — but its edges violate our conventions: it sources context from DESCRIPTION.md (artifact being retired, note 52), Step 3 writes an architecture pointer into DESCRIPTION.md and Step 4 a row into AGENTS.md (both "second home for a fact"; AGENTS.md is a one-line pointer by convention).
- User's observation: agents don't always read ARCHITECTURE.md, but the pointer belongs in the project **CLAUDE.md** — the unconditional channel (in practice architecture gets pulled in when any skill's Step 0 runs, but the CLAUDE.md edge makes it reliable).
- Fork: copy to `src/skills/aif-architecture`, repoint `active/skills/aif-architecture` → `../../src/skills/aif-architecture`, rework **recognizably** — a diff against upstream must clearly show what was cut.

## Details

### Keep (visibly intact vs upstream)

- Step 0 config.yaml read (paths + language), standalone-usage fallback.
- Step 1 recommendation flow: argument mapping (incl. legacy aliases — harmless), decision matrix, the AskUserQuestion recommendation with reasons, the CRITICAL read of `references/architecture.md`.
- Step 1.5 Codebase Alignment Check verbatim — it is the best part.
- Step 2 template, including Legacy vs New Code Policy / Code Organization Note branches, code-example and anti-pattern sections. `references/` directory copied as-is.

### Change

- **Context source (Step 0):** instead of DESCRIPTION.md, read the project's **CLAUDE.md** (purpose, stack, conventions — auto-present in every project per our stack) plus a light codebase scan (package manager files, src layout). Keep the manual-input fallback for empty projects.
- **Step 3 → CLAUDE.md pointer:** replace the DESCRIPTION.md architecture-pointer with ensuring the project CLAUDE.md carries one line pointing at the resolved architecture path (e.g. an `## Architecture` section: "See `.ai-factory/ARCHITECTURE.md` for module boundaries, folder structure, and dependency rules."). Add only if absent — never duplicate.
- **Step 4 (AGENTS.md row) — delete.** AGENTS.md is a one-line pointer to CLAUDE.md; nothing is written there.
- **Template addition:** reserve an empty `## Features` section at the bottom of the generated ARCHITECTURE.md with a one-line comment that `roadmap-prune` anchors completed features here by commit hash — the anchor store for `temporal-tree`.

### Cut

- `skill-context` / aif-evolve block.
- Localized-heading placeholders — artifacts are English; UI language for dialogs still follows `language.ui` from config.

### Repo bookkeeping

- `ln -sfn ../../src/skills/aif-architecture active/skills/aif-architecture`.
- Update skills-repo `CLAUDE.md`: `aif-architecture` moves to the reworked-from-upstream reconcile list; after this task the only upstream original left in `active/` is `aif-skill-generator`.

## What NOT to do

- Do not rewrite beyond recognition — keep upstream's step numbering and headings; cuts read as deletions in a diff.
- Do not touch the upstream mirror copy.
- Do not write anything into AGENTS.md or DESCRIPTION.md.
- Do not inline `references/architecture.md` content into the body — it stays a reference read on demand.

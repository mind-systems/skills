# Plan: aif-docs: diet to ≤500 — rare branches to `references/`, drop the aif-evolve block

## Context
Bring `src/skills/aif-docs/SKILL.md` back under the repo's ≤500-line authoring norm (from 574 to ~450) with byte-identical runtime behavior — by moving three rare-branch sections into new `references/` files (body keeps rule + when-to-read pointer) and deleting the dead skill-context/aif-evolve block.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Drop dead machinery

- [x] **Task 1: Delete the Step 0 skill-context / aif-evolve block**
  Files: `src/skills/aif-docs/SKILL.md`
  In "Step 0: Load Config & Project Context", remove the block spanning the "**Read `.ai-factory/skill-context/aif-docs/SKILL.md`** — MANDATORY if the file exists." paragraph through the "**Enforcement:** After generating any output artifact…" paragraph (current lines ~55–74). No replacement text. Leave the surrounding "Explore the codebase" bullets (above) and the "Scan for scattered markdown files in project root" subsection (below) intact — the paragraph flow must read cleanly with no dangling blank lines. Do NOT touch any other Step 0 content.

### Phase 2: Progressive-disclosure extractions

Each extraction follows the existing `references/REVIEW-CHECKLISTS.md` pattern: the reference file is self-contained, the body keeps the operative rule plus a one-line pointer stating **when** to read it, and all references use relative paths. Verbatim AskUserQuestion dialogs are contract text — they are NOT compressed and, where noted, stay in the body.

- [x] **Task 2: Extract per-topic content guidelines → `references/topic-guides.md`**
  Files: `src/skills/aif-docs/references/topic-guides.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/topic-guides.md` containing the "Content guidelines per topic" material from Step 2.3 (the getting-started.md / architecture.md / api.md / configuration.md / deployment.md bullet lists, current lines ~337–369) verbatim. In SKILL.md Step 2.3, keep the "For each approved topic, create a doc file" instruction and the markdown skeleton block, then replace the moved bullet lists with a single pointer line, e.g.: "Content guidelines per topic → read `references/topic-guides.md` when generating State A pages." Do not alter the Step 2.3 heading or the doc-file skeleton example.

- [x] **Task 3: Extract HTML generation mechanics → `references/html-generation.md`**
  Files: `src/skills/aif-docs/references/html-generation.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/html-generation.md` containing the Step 3.1–3.4 mechanics verbatim (`mkdir -p docs-html`, template read/customize placeholders, markdown→HTML conversion steps, output tree/`open` hint; current lines ~467–488). In SKILL.md "Step 3: Generate HTML Version (--web flag)", keep: the `--web` trigger sentence, the file-mapping one-liner (`README.md → index.html`, `<resolved docs dir>/*.md → *.html`), and a pointer line reading the reference only when the flag is present, e.g.: "HTML build mechanics → read `references/html-generation.md` when `--web` is passed." Remove the now-migrated 3.1–3.4 subsections.

- [x] **Task 4: Extract consolidation table + sample dialog → `references/consolidation.md`**
  Files: `src/skills/aif-docs/references/consolidation.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/consolidation.md` containing, verbatim: the "Root file → Target in docs dir → Merge or move?" table, the "Files that stay in root" list, and the long "Found [N] markdown files in the project root:" example dialog (current lines ~156–197). In SKILL.md Step 1.1, KEEP in the body: the rule (propose moving scattered root `.md` files into the resolved docs dir; never force-move; ask first), the three AskUserQuestion options block ("Apply all suggestions / Let me pick which ones / Skip"), the "Based on choice" mapping, the six-point "When moving/merging" procedure, and the "IMPORTANT: Never force-move files" line — these are behavior, not reference. Replace the moved table/list/example with a pointer line, e.g.: "Consolidation targets and the sample proposal dialog → read `references/consolidation.md`." Ensure the retained AskUserQuestion options are not orphaned from their introducing sentence.

### Phase 3: Verify

- [x] **Task 5: Verify line count and byte-identical behavior via a live State C run** (depends on Tasks 1–4)
  Files: `src/skills/aif-docs/SKILL.md` (read-only check)
  Confirm `wc -l src/skills/aif-docs/SKILL.md` is ≤500 (target ~450). Confirm the three new `references/*.md` files exist and are self-contained, and that every body pointer names its reference with a correct relative path and a when-to-read condition. Confirm untouched sections are byte-unchanged: Core Principles, the 3D mode section, Step 4 (Documentation Review incl. no-motivation pass), Step 4.1, Step 5, Artifact Ownership, Important Rules. Confirm Task 48's CLAUDE.md-documentation-index edits (Step 1.1, 2.2b, State B/C) are preserved and not reverted. Then perform a live State C audit run of the dieted skill on one real repo and compare interaction shape and outputs against pre-diet behavior — every branch (normal, 3D, `--web`, States A/B/C) must be reachable and behave identically. Do NOT touch the upstream mirror (`upstream/ai-factory/aif-docs`).

## Commit Plan
- **Commit 1** (after tasks 1–4): "Diet aif-docs SKILL to under 500 lines with references extraction"
- **Commit 2** (after task 5): "Verify aif-docs diet preserves behavior" — only if the verification pass requires follow-up edits; otherwise fold into Commit 1.

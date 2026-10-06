# Plan: 73.4 — the skill reads the built design before it offers a menu

## Context
`src/skills/aif-architecture/SKILL.md` reads only the stack and folder layout, recommends a packaging pattern from a size/complexity matrix, offers a strict migration target as an equal option in Step 1.5, and writes a `CLAUDE.md` pointer naming packaging only. This task makes Step 0 read the built design (interfaces with several implementations and where one is chosen), Step 1 name it — or, for a new project, ask its variation axes — before the packaging menu, Step 1.5 compare packaging only with the migration target offered only on explicit choice, and the Step 3 pointer name what varies and the composition root first. Every after-text is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0211-the-skill-reads-the-built-design-before-it-offers-a-menu.md` and reproduced byte-for-byte below; on any disagreement the spec wins.

Ground truth checked: 73.1–73.3 are committed (`c6870fa`), and `references/architecture-template.md` already gates the "Legacy vs New Code Policy" section on "the user explicitly asked for a migration target in Step 1.5" and no longer names "Option 1"/"Option 2", so the new Step 1.5 option text lines up with it. The `description:` frontmatter, `argument-hint`, Step 2, Step 4 and "Artifact Ownership" stay untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the four steps in `src/skills/aif-architecture/SKILL.md`

- [x] **Step 0 — read the built design**
  Files: `src/skills/aif-architecture/SKILL.md`
  In `### Step 0: Load Project Context`, replace the lead line
  `**Also run a light codebase scan** to infer project size and complexity:`
  with
  `**Also run a light codebase scan** to see the stack and the layout:`
  Keep its two bullets (package-manager files; `src/` directory layout) unchanged. Directly after those bullets and a blank line, before the line `**If `CLAUDE.md` does not exist and the codebase scan finds nothing:**`, insert this paragraph (followed by a blank line), verbatim:

  ~~~~
  **For existing code, then read the built design.** Find the interfaces that have several implementations, where each implementation lives, and where and by what key one is chosen — a factory, a registry, the composition root. That is the variation the system already has: what varies (mode, environment, provider, role), its ports, its adapters and the root that assembles them. Step 1 describes and names it first; the packaging comes after.
  ~~~~
  Nothing else in Step 0 changes (the "No project context found" block, its bullets, and "Allow standalone usage…" stay).

- [x] **Step 1 — variation first, packaging second** (depends on Step 0)
  Files: `src/skills/aif-architecture/SKILL.md`
  In `### Step 1: Recommend Architecture`, replace exactly the single line
  `Based on project context, evaluate against the decision matrix and recommend an architecture:`
  with the following three paragraphs, verbatim (blank lines between paragraphs; the inner double-quoted question stays as written, `AskUserQuestion` and `$ARGUMENTS` in backticks):

  ~~~~
  Variation comes first, packaging second.

  **Where the system varies.** For existing code, describe and name the built design read in Step 0 before any menu: code whose axes have ports with an adapter per value, chosen at a composition root, is Ports and Adapters, and the document names it so. The architecture to recommend is the one the code already has, and the menu below only answers how it is packaged. For a new project, ask before the menu, via `AskUserQuestion`: "Where will this system vary — modes (live and test, for instance), environments, providers, roles — and which of those must be swappable without touching the logic?" Record the answer as the architecture's variation axes. A packaging named in `$ARGUMENTS` fixes only the packaging; the variation is still read or asked.

  **Packaging.** Based on project context, evaluate against the decision matrix, which scores packaging fit only, and recommend how the system is packaged:
  ~~~~
  Everything that followed the replaced line stays byte-identical: the `**If `$ARGUMENTS` specifies an architecture**` block with its direct mappings, legacy aliases, suffixes and variant questions; the `**If no specific architecture requested:**` block including "Consider: team size, domain complexity, scale requirements, tech stack" and the recommendation `AskUserQuestion` template; the "Architecture options" list; and the `**CRITICAL INSTRUCTION:**` line. The spec's "Nothing else in the file changes" is contract text — do not touch these.

- [x] **Step 1.5 — compare packaging only; migration target only on explicit choice** (depends on Step 1)
  Files: `src/skills/aif-architecture/SKILL.md`
  Replace the whole `### Step 1.5: Codebase Alignment Check` section — from its heading through the line `Wait for their decision before proceeding to Step 2.` inclusive — with the following, verbatim (the inner block is a plain triple-backtick fence, as today):

  ~~~~
  ### Step 1.5: Codebase Alignment Check

  **CRITICAL:** Before generating the document, compare the chosen packaging's ideal folder structure (from `references/architecture.md`) against the actual existing folder structure. The built design read in Step 0 is not part of this comparison; it is documented as it is.

  - If the project is empty or mostly matches: proceed to Step 2.
  - **If there are significant discrepancies:** DO NOT silently merge the ideal packaging with the messy reality, and do not offer a migration target as the default. You MUST stop and ask the user how to proceed via `AskUserQuestion`:

  ```
  The current project structure differs significantly from the ideal [Pattern Name] packaging.
  [Briefly list 1-2 major differences]

  How should we generate the ARCHITECTURE.md?
  1. Document the existing structure as it is (the default).
  2. Also write a migration target: strict guidelines the application must be refactored toward later. Only on your explicit choice.
  ```
  Wait for their decision before proceeding to Step 2.
  ~~~~
  Keep the blank line before `### Step 2: Generate the Architecture Artifact`.

- [x] **Step 3 — the pointer names what varies and the composition root first**
  Files: `src/skills/aif-architecture/SKILL.md`
  In `### Step 3: Update project CLAUDE.md`, inside the fenced `markdown` block, replace the line
  `See `.ai-factory/ARCHITECTURE.md` for module boundaries, folder structure, and dependency rules.`
  with
  `See `.ai-factory/ARCHITECTURE.md` for what varies and where it is chosen, the composition root, module boundaries, folder structure, and dependency rules.`
  The `## Architecture` heading line inside the block, the "Add only if absent" and "If `CLAUDE.md` doesn't exist" bullets, and the sentence above them stay unchanged.

### Verify the blast radius

- [x] **Run the spec's sweep and confirm nothing else needs editing** (depends on all four steps above)
  Files: none edited (read-only check)
  From the repo root run:
  ```
  grep -rn -i "size and complexity\|light codebase scan\|ideal folder structure\|ideal architecture" src docs CLAUDE.md --include="*.md"
  grep -rn "aif-architecture" src docs CLAUDE.md --include="*.md"
  grep -rn "module boundaries, folder structure" src docs CLAUDE.md --include="*.md"
  ```
  Expected: "size and complexity" and "ideal architecture" no longer appear in `src/skills/aif-architecture/SKILL.md`; "light codebase scan" and "ideal folder structure" appear only in the new Step 0 lead and Step 1.5 text. Per the spec, the remaining hits stay as they are and are NOT edited: `aif` (invokes the skill whole), `aif-docs`, `docs/reserved-words.md`, `CLAUDE.md` (name the skill only), `docs/philosophy/principles-at-their-moment.md` § "Dependency inversion, and where to invert." (already states the behaviour the new Step 0/Step 1 implement — "`aif-architecture` writes it by reading the built design first…" — so this change brings the skill into line with it; the spec's finding omits this hit, but it needs no edit), and `src/skills/roadmap-test-coverage/SKILL.md` line describing ARCHITECTURE.md as "module boundaries, folder structure" (says what that skill reads; stays true). Also confirm via `git diff --stat` that only `src/skills/aif-architecture/SKILL.md` changed, and that the frontmatter `description:` still reads "recommends an architecture pattern". Body stays well under 500 lines.

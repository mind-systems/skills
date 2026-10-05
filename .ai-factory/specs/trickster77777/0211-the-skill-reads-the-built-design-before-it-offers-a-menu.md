# 73.4 — the skill reads the built design before it offers a menu

## What is true now

`src/skills/aif-architecture/SKILL.md` Step 0 opens its codebase scan with "**Also run a light codebase scan** to infer project size and complexity:", and the scan reads package-manager files and the `src/` directory layout. Step 1 opens "Based on project context, evaluate against the decision matrix and recommend an architecture:", with the menu of packaging patterns and "Consider: team size, domain complexity, scale requirements, tech stack". The skill never reads which interfaces have several implementations or where one is chosen, and never asks a new project where it will vary. Step 1.5, "Codebase Alignment Check", begins "**CRITICAL:** Before generating the document, compare the chosen architecture's ideal folder structure … against the actual existing codebase structure.", and on significant discrepancies offers "1. Adapt the guidelines to fit the existing application structure (document reality)." and "2. Generate the pure, strict architecture guidelines (requires refactoring the application later to match)." with the discrepancy sentence "The current project structure differs significantly from the ideal [Pattern Name] architecture." Step 3 writes into a project's `CLAUDE.md`, when it carries no architecture pointer yet, the `## Architecture` section "See `.ai-factory/ARCHITECTURE.md` for module boundaries, folder structure, and dependency rules.", which names packaging only.

## What must be true after

In Step 0, the scan's lead line reads: "**Also run a light codebase scan** to see the stack and the layout:" and its two bullets are unchanged. Directly after the bullets, before "**If `CLAUDE.md` does not exist and the codebase scan finds nothing:**", one paragraph is added:

"**For existing code, then read the built design.** Find the interfaces that have several implementations, where each implementation lives, and where and by what key one is chosen — a factory, a registry, the composition root. That is the variation the system already has: what varies (mode, environment, provider, role), its ports, its adapters and the root that assembles them. Step 1 describes and names it first; the packaging comes after."

In Step 1, the line "Based on project context, evaluate against the decision matrix and recommend an architecture:" is replaced by:

"Variation comes first, packaging second.

**Where the system varies.** For existing code, describe and name the built design read in Step 0 before any menu: code whose axes have ports with an adapter per value, chosen at a composition root, is Ports and Adapters, and the document names it so. The architecture to recommend is the one the code already has, and the menu below only answers how it is packaged. For a new project, ask before the menu, via `AskUserQuestion`: "Where will this system vary — modes (live and test, for instance), environments, providers, roles — and which of those must be swappable without touching the logic?" Record the answer as the architecture's variation axes. A packaging named in `$ARGUMENTS` fixes only the packaging; the variation is still read or asked.

**Packaging.** Based on project context, evaluate against the decision matrix, which scores packaging fit only, and recommend how the system is packaged:"

Step 1.5 reads:

"### Step 1.5: Codebase Alignment Check

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
Wait for their decision before proceeding to Step 2."

In Step 3, the pointer block reads:

```markdown
## Architecture
See `.ai-factory/ARCHITECTURE.md` for what varies and where it is chosen, the composition root, module boundaries, folder structure, and dependency rules.
```

Nothing else in the file changes. The skill's `description:` still reads "recommends an architecture pattern", which stays true.

## What breaks on contact

**Rule:** a text breaks on this change if it describes what the skill reads, what it asks, or what the two Step 1.5 options mean.

**Sweep:**
```
grep -rn -i "size and complexity\|light codebase scan\|ideal folder structure\|ideal architecture" src docs CLAUDE.md --include="*.md"
grep -rn "aif-architecture" src docs CLAUDE.md --include="*.md"
grep -rn "module boundaries, folder structure" src docs CLAUDE.md --include="*.md"
```

**Finding.** The first search reaches only `SKILL.md`, at Step 0's scan lead and Step 1.5, both rewritten above. The second reaches `aif`, which invokes the skill as a whole and states its output in the sentence 73.3 pins; `aif-docs`, which names the skill as the owner of `ARCHITECTURE.md` without describing its steps; `docs/reserved-words.md` and `CLAUDE.md`, which name it likewise; and the "Reconcile reworked skills" list in `CLAUDE.md`, which concerns the upstream counterpart. All of these stay. The `## Architecture` pointer line Step 3 writes is rewritten above, so a newly written pointer names the variation and the root before packaging. The third search reaches that pointer and one line in `roadmap-test-coverage` that describes the file as "module boundaries, folder structure"; it says what that skill reads from the file, stays true, and is not edited. A project already carrying a pointer keeps its older line, because Step 3 adds the section only if absent, and no skill rewrites it. The template's two branches stop naming "Option 1" and "Option 2" in 73.3, so this rewrite of the option text is free of them.

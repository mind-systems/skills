Output template for the generated `ARCHITECTURE.md`. Both policy branches and the reserved `## Features` section land in the file exactly as written.

```markdown
# Architecture: [Pattern Name]

## Overview
[1-2 paragraphs: the pattern the code is built in, named for what it is; the one flow the system runs, what differs between its variants, and the rule that keeps them apart. Packaging comes second.]

## What varies
[One entry per variation axis — mode, environment, provider, role. For each: the values it takes, the port that holds the choice, the adapter each value gets, and where the code shows it, as a path and a symbol. A port that exists only so a test can substitute a fake is a test seam, listed apart from the axes.]

## Composition root
[Where the variants are assembled, and that nothing else constructs them: the only place that knows which implementation runs.]

## The rule
[The structural rule in this project's own words, and what breaks when it is not held.]

## Invariants
[One link per invariant to the document that governs it.]

## Decision Rationale
- **Project type:** [from CLAUDE.md / codebase]
- **Tech stack:** [language, framework]
- **Key factor:** [primary reason for this choice]

## Folder Structure
\`\`\`
[folder structure adapted to the project's tech stack]
[use actual framework conventions — e.g., Next.js app/ dir, Laravel app/ dir, Go cmd/ dir]
\`\`\`

## Dependency Rules
[What depends on what. Inner vs outer layers. Module boundaries.]

- ✅ [allowed dependency direction]
- ❌ [forbidden dependency direction, and what it breaks]

## Layer/Module Communication
[How layers or modules communicate with each other]
- [pattern 1]
- [pattern 2]

## Key Principles
1. [Principle 1 — adapted to this project]
2. [Principle 2]
3. [Principle 3]

[Only if the user explicitly asked for a migration target in Step 1.5, add the following section:]
## Legacy vs New Code Policy
- **New Features:** All new code MUST strictly follow the architecture defined in this document, or the target is a wish and not a rule.
- **Legacy Code Modification:** Do NOT automatically refactor unrelated legacy code to fit this architecture, because a refactor folded into a feature escapes review as a refactor. Touch legacy code only when necessary for bug fixes, when tasked with explicit refactoring, or when adapting it to be consumed by new features.
- **Interoperability:** When new code must call legacy code, isolate the interaction using adapters, interfaces, or facades so that legacy patterns do not pollute the new architecture.

[For existing code, unless a migration target was asked for, add the following lighter section:]
## Code Organization Note
- **New Features:** All new code should follow the architecture defined in this document where practical.
- **Existing Code:** Document the current structure as-is. When modifying existing code, prefer following the architectural conventions in this document, but do not force a rewrite of unrelated code, because a rewrite for tidiness carries risk and delivers no feature.
- **Interoperability:** When new code must call existing code, prefer clean interfaces but do not refactor purely for structural alignment, because that changes working code for no change in behavior.

## Living Examples
[Each entry names a path and a symbol in the project's code that shows the rule at work, and what to read in it.]

## Anti-Patterns
- ❌ [What NOT to do in this architecture, and what it breaks]
- ❌ [Common mistake to avoid, and what it breaks]

## Features
<!-- roadmap-prune anchors completed features here by commit hash (temporal-tree's anchor store). Leave empty. -->
```

**Rules for generation:**
- Read the variation from the code before writing: which interfaces have several implementations, and where and by what key one is chosen. The pattern name, the axes and the composition root come from that reading, and the folders follow.
- Write a migration target only on the user's explicit choice: it declares the built design wrong, and every later task reads it as a debt.
- Give every ❌ and every MUST NOT the thing it breaks, because a ban without its reason is read as taste and dropped at the first inconvenient task.
- Name each living example by a path and a symbol and paste no code: a pasted block is read as the form to copy and goes stale as the code moves.
- Write no counts and no thresholds: a number here measures today's tree, which the tree outgrows, so name what produces it instead.
- Link each invariant to the document that governs it and never restate it: a fact kept in two places drifts.
- Use the project's actual conventions (import paths, naming, etc.)
- Keep it practical — focus on rules that affect day-to-day development
- Base the generated folder structure on the user's decision in Step 1.5: the existing structure documented as it is, and a migration target written as well only on the user's explicit choice.

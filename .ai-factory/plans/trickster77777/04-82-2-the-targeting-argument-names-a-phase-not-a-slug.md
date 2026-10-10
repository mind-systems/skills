# Plan: 82.2 — the targeting argument names a phase, not a slug

## Context
`roadmap-outline-deep` and `roadmap-decompose-skeleton` offer a "slug" as a targeting argument in their `argument-hint` and in the opening sentence of § "Targeting". Neither skill defines that slug. The registry's slug is the user's git-email local-part, which names a user and not a target. This task removes the slug from both hints and both targeting sentences. The after-texts are pinned verbatim in the task spec (`.ai-factory/specs/trickster77777/0237-the-targeting-argument-names-a-phase-not-a-slug.md`, § "What must be true after"). Everything else in each sentence and section stays as it is. That includes the `<user-slug>` / `<NN>-<slug>.md` path placeholders elsewhere in `roadmap-outline-deep`, which 82.1 already settled.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Targeting edits

- [x] **`roadmap-outline-deep`: hint and targeting sentence**
  Files: `src/skills/roadmap-outline-deep/SKILL.md`
  - Frontmatter: `argument-hint: "[phase or slug]"` becomes `argument-hint: "[phase]"`. Keep the brackets quoted (project rule for `argument-hint`).
  - § "Targeting", first sentence: `Optional arg — a phase or slug (matching `argument-hint`).` becomes `Optional arg — a phase (matching `argument-hint`).` The rest of the paragraph stays word for word: "Default: infer the target phase set from conversation context. Resolve the roadmap in play per `roadmap-engine`'s …". You may reflow the hard-wrapped lines, but no wording may change.

- [x] **`roadmap-decompose-skeleton`: hint and targeting sentence**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  - Frontmatter: `argument-hint: "[phase/slug or task description]"` becomes `argument-hint: "[phase or task description]"` (quoted).
  - § "Targeting", first sentence: `Optional arg — a phase, slug, or single task description.` becomes `Optional arg — a phase or a single task description.` The rest stays word for word: "Default: infer the target open-`[ ]` task set from conversation context (a named phase, a described task, or the current pending set). It can operate on a single task — …". You may reflow the hard-wrapped lines, but no wording may change.

### Contact check

- [x] **Sweep confirms no slug target remains** (depends on both edits above)
  Files: none (read-only check)
  Run the spec's sweep: `grep -rn "phase or slug" src docs CLAUDE.md README.md`, `grep -rn "phase/slug" src docs CLAUDE.md README.md`, `grep -rn "phase, slug" src docs CLAUDE.md README.md`. All three must return nothing. Also check that each edited frontmatter still parses as YAML, with the `argument-hint` value quoted.

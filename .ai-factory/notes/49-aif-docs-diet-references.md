# aif-docs: restore the ≤500-line norm — move rare branches to references/, drop the aif-evolve block

**Date:** 2026-07-02
**Source:** conversation context (skill review)

## Key Findings

- `src/skills/aif-docs/SKILL.md` is 574 lines against the repo's ≤500 authoring norm — the only accepted deviation, which weakens the norm by precedent. Two moves restore it with byte-identical behavior; verbatim dialog templates are deliberately NOT touched (they stabilize behavior — contract text).
- **Move 1 — progressive disclosure (~100 lines).** The skill already uses on-demand loading (`references/REVIEW-CHECKLISTS.md`, `templates/html-template.html`). Three more body sections are paid on every invocation but needed only on rare branches; move their reference content out, keep the rule + pointer in the body.
- **Move 3 — dead machinery (~20 lines).** The Step 0 block "Read `.ai-factory/skill-context/aif-docs/SKILL.md`" (with its How-to-apply / Enforcement sub-blocks) serves `/aif-evolve`, which is not in the active set and whose skill-context files do not exist in any of the user's projects. Confirmed removable by the user.
- Depends on task 48 (`Spec: .ai-factory/notes/48-aif-docs-index-in-claude-md.md`) — it edits the same sections (Step 1.1, 2.2, State B/C audit); this task runs strictly after it and must preserve its changes.

## Details

### Move 1 — three extractions to `references/`

1. **Per-topic content guidelines** (Step 2.3, "Content guidelines per topic": getting-started / architecture / api / configuration / deployment bullet lists, ~45 lines) → `references/topic-guides.md`. Body keeps: "For each approved topic create a doc file per `references/topic-guides.md` — read it when generating State A pages."
2. **HTML generation mechanics** (Step 3.1–3.4 details, ~25 lines) → `references/html-generation.md`. Body keeps the trigger (`--web`), the file mapping one-liner (`README.md → index.html`, `docs/*.md → *.html`), and the pointer — read the reference only when the flag is present.
3. **Consolidation table + sample dialog** (Step 1.1: the Root file → Target table, the stays-in-root list, and the long "Found [N] markdown files" example, ~35 lines) → `references/consolidation.md`. Body keeps: the rule (propose moving scattered root `.md` files into the docs dir; never force-move; ask first), the three AskUserQuestion options, and the six-point When-moving/merging procedure (it is behavior, not reference).

Each extraction: reference file is self-contained; body pointer states *when* to read it (matching the existing REVIEW-CHECKLISTS.md pattern). All file references relative, per skill authoring rules.

### Move 3 — delete the skill-context block

Remove from Step 0: the "Read `.ai-factory/skill-context/aif-docs/SKILL.md` — MANDATORY" paragraph, the "How to apply skill-context rules" bullet list, and the "Enforcement" paragraph (~20 lines). No replacement text.

### Target and verification

- Target size: ~440–460 lines (574 − ~100 − ~20). Behavior byte-identical on every path: normal, 3D, `--web`, States A/B/C.
- Verification is a live run: invoke the dieted skill on one real repo in a State C audit pass and compare the interaction shape and outputs against the pre-diet behavior.

## What NOT to do

- Do not compress or paraphrase the AskUserQuestion dialog templates — verbatim dialogs are contract text and stay.
- Do not touch Core Principles, the 3D mode section, review Step 4, or the no-motivation pass.
- Do not undo task 48's changes (CLAUDE.md documentation index) — this task runs after it and preserves them.
- Do not touch the upstream mirror (`upstream/ai-factory/aif-docs`).

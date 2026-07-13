# Plan: 5.6 — temporal-tree: one home for the walk

## Context
Collapse the duplicated walk procedure in `temporal-tree` to a single home in `SKILL.md` (the canonical file, since it is what loads), removing `docs/overview.md` and its `docs/` directory once the paragraph-by-paragraph audit confirms every paragraph is pure restatement.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Audit result (paragraph-by-paragraph, `docs/overview.md` vs `SKILL.md`)
Per spec `.ai-factory/specs/55-temporal-tree-one-home-for-the-walk.md`, each paragraph is either restatement (delete) or teaches depth SKILL.md lacks (move to `references/`). Findings:

- **"What it solves"** (overview L1–13) → restates the detangle-vs-temporal-tree spatial/temporal contrast already in SKILL.md's intro (L16–21). Restatement.
- **"The entry point"** + Features-table example (overview L15–33) → covered by SKILL.md "Before you start" (L28–37). The overview example table carries **no** version-suffix / prefix-match note, so it holds nothing SKILL.md's ledger-coupling sentence (L32–33) doesn't already own. Restatement.
- **"Climbing the temporal tree" Steps 1–5** (overview L36–79) → covered by SKILL.md Steps 1–5 (L41–131), which are strictly richer. Restatement.
- **"Reading a multi-hash feature"** (overview L83–95) → covered by SKILL.md Step 6 (L134–144). Restatement.
- **"When to use this"** (overview L99–106) → the trigger conditions are covered by SKILL.md's intro ("after detangle … the *why* behind a pattern still isn't clear", L20–21) and "What NOT to do" (L164–172). Restatement.
- **"What this is NOT for"** (overview L110–115) → covered verbatim-in-substance by SKILL.md "What NOT to do" (L164–172). Restatement.

Conclusion: **no paragraph survives** — `docs/overview.md` is fully redundant. Expected outcome per spec: delete the file whole and the `docs/` directory with it. No `references/overview.md` is created; no SKILL.md link is added (nothing survives to link to). Confirmed no file references `temporal-tree/docs` or `overview.md` anywhere outside the roadmap/spec/handoff planning layer.

## Tasks

### Phase 1: Collapse to one home

- [x] **Task 1: Delete the redundant overview file and its directory**
  Files: `src/skills/temporal-tree/docs/overview.md`, `src/skills/temporal-tree/docs/`
  Delete `src/skills/temporal-tree/docs/overview.md`. The `docs/` directory contains only this file, so remove the now-empty `docs/` directory as well (`rm -rf src/skills/temporal-tree/docs`). Do not touch `SKILL.md`: the walk procedure stays behavior-identical and its `## Features` prefix-match / prune ledger-coupling sentence (L32–33) is untouched. Do not create `references/` — the audit above found nothing non-duplicative to relocate, so no new file and no SKILL.md link are added.

## Verification
- `src/skills/temporal-tree/docs/` no longer exists.
- `src/skills/temporal-tree/SKILL.md` is byte-identical to its pre-task state (no link added, walk procedure and ledger-coupling sentence unchanged).
- Exactly one file (`SKILL.md`) carries the walk procedure.

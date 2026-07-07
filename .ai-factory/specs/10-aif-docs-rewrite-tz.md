# aif-docs — write the ТЗ: stop refusing docs-ahead-of-code, weight docs as specs

**Target:** `src/skills/aif-docs/SKILL.md` **and** its `references/` (delete/verify scope spans both).

## The one complaint

The skill **refuses to write a ТЗ** — a governing spec ahead of implementation. Called to document a feature that isn't built yet, it assumes shipped code (`Step 1: Determine Current State` at `SKILL.md:93`, accuracy checks against a running referent) and argues instead of writing. `3d`/`3д` (note 14) was bolted on as an exception-mode to grant permission — a workaround for the refusal, not a feature. This is the whole task: kill the refusal, delete the workaround. File size is not a concern (rarely called) and the fork toward a lean ТЗ-only skill is **out of scope** — the README/onboarding genre, the state machine, `--web`, and the review ceremony all stay.

## Doctrine to weight up: docs are ТЗ

Give the ТЗ genre the weight it's missing. State plainly, up front (skill identity + Core Principles), that the documentation this skill writes **is a ТЗ** — behavior, protocols, data flows, connections — in present tense (Principle 6, state-not-process, unchanged). The single exception is the **onboarding surface**: README and its relatives (CHANGELOG, CONTRIBUTING, LICENSE). Everything under `docs/` is the ТЗ genre. Rephrase the skill's self-description ("Project Documentation Generator") and principles so this reads as the default, not README-generation with specs as an afterthought.

## Change

1. **Delete `3d`/`3д` wholesale — SKILL.md *and* references.** The flag (`Step 0.1`, `argument-hint`), the "Document-Driven Development (3D mode)" section (`:72-92`), every `MODE = 3D` branch (Step 1 content-source `:95`, Step 2.1 staleness `:345`, Step 4 accuracy carve-out `:395`), the conform-pointer, and the `MODE = 3D` carve-out lines in `references/REVIEW-CHECKLISTS.md` (`:11`, `:12`, the "(including 3D)" parenthetical at `:15`). One mode remains.

2. **The one mode writes the ТЗ natively, code or no code.** Reframe `Step 1: Determine Current State` so it determines *the subject* — behavior + invariants — without assuming shipped code; it reads the code where it exists, treats the doc as the contract where it doesn't. The accuracy checks that need a running referent (`REVIEW-CHECKLISTS.md:11-12`) become **per-item conditional on the referent existing** — verify against the code where the surface exists, otherwise the doc is the spec. This is a per-check condition, **not** a mode, and **not** a lead/lag explanation. **Never describe the lead/lag duality in the skill** — the present-tense voice already covers both; spelling it out is exactly the meta that spawned 3d (the insight that must not be undone).

3. **Feature-cross-link tree is the nav model; purge the linear-nav residue.** Where a doc names a feature a deeper doc expands, link it (relative path) — edges and leaves of a tree grown across runs; in ARCHITECTURE.md, module/subsystem mentions link to their topic docs. Delete the competing linear-nav prescriptions: `topic-guides.md:8` "Next steps links", `REVIEW-CHECKLISTS.md:43` "where to go next", the linear-path ordering in `:44`. No See Also, no prev/next, no "next steps" sections.

4. **Keep it terse — reference, don't reinvent.** Point at the existing CLAUDE.md `## Documentation` index (Principle 3), don't rebuild it. **One home per fact** (dedup by role — structure → ARCHITECTURE.md, behavior → topic docs, index → CLAUDE.md, onboarding → README + relatives; a fact found twice becomes a link): this is how the README-vs-docs genre split is enforced. On each run, check the coordination trio — README, the CLAUDE.md index, ARCHITECTURE.md — for staleness; refresh what aif-docs owns; for ARCHITECTURE.md just **check for staleness, don't clobber** its structural info — no descriptive-vs-structural boundary, no aif-architecture edit.

## Guards

- No lead/lag meta-commentary in the skill (item 2) — re-adding it re-creates 3d.
- **No fork this pass:** README/onboarding generation (Step 2 State A), the A/B/C state machine, `--web`/HTML, and the review checklists all stay. This is a reframe + delete-symptoms pass, not a spine extraction.
- Principle 6 (state-not-process) stays — cite by name, the numbering has drifted before.
- Never edit `upstream/ai-factory/` or `aif-architecture`; aif-docs stays ours / never-overwrite in CLAUDE.md.
- Body ≤500 lines (norm, not a goal); rare branches live in `references/`.

## Verify

- `grep -rin "3d\|3д\|MODE = 3D\|Document-Driven" SKILL.md references/` → zero.
- `grep -rin "see also\|next steps\|where to go next\|prev/next" SKILL.md references/` → zero.
- Skill identity + Core Principles state that docs are ТЗ (behavior/protocols/flows/connections), README + relatives the onboarding exception.
- A plain run against a **not-yet-built** feature produces a present-tense ТЗ **without arguing** that code must exist first; a run against shipped code produces the same voice; the README/onboarding path still works.

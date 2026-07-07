# Plan: aif-docs — write the ТЗ: stop refusing docs-ahead-of-code

## Context
Reframe `aif-docs` so its single mode writes a present-tense ТЗ (behavior, protocols, flows, connections) whether the code exists or not — deleting the bolted-on `3d`/`3д` exception-mode wholesale, weighting up the docs-are-ТЗ doctrine, and purging linear-nav residue in favor of a feature-cross-link tree. Scope spans `src/skills/aif-docs/SKILL.md` and its `references/`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Weight up the ТЗ doctrine and delete 3d from SKILL.md

- [x] **Task 1: Reframe skill identity + Core Principles as ТЗ-first**
  Files: `src/skills/aif-docs/SKILL.md`
  In the frontmatter `description` (`:3`), H1, and lead-in (`:13-15`), rephrase the "Project Documentation Generator" / "Generate and maintain project documentation" self-description so the default genre reads as **ТЗ**: the docs this skill writes under the resolved docs directory *are* a governing spec — behavior, protocols, data flows, connections — in present tense; README + its relatives (CHANGELOG, CONTRIBUTING, LICENSE) are the **onboarding exception**, not the center. The frontmatter `description` is **in scope** (it is the router-facing skill identity the spec's Verify names) — but **keep its invocation trigger phrases intact** ("create docs", "write documentation", "update docs", "generate readme", "document project") so auto-selection does not change; reword only the descriptive clause, not the triggers. Fold this into Core Principles: state up front that everything under `docs/` is the ТЗ genre and only the onboarding surface is exempt. Keep the **Principle 6 (state, not process)** *rule* intact and cite it **by name** (numbering has drifted before) — but drop its now-dangling "every run, every mode, no exceptions" clause (`:24`) to "every run, no exceptions", since after Task 2 there is no `mode` distinction left to reference. The present-tense voice Principle 6 mandates already covers both code-exists and code-absent cases. **Do not** add any lead/lag or docs-ahead-of-code meta-commentary anywhere — spelling out the duality is exactly what spawned `3d`. Point Principle 3 at the existing CLAUDE.md `## Documentation` index rather than rebuilding it; reinforce one-home-per-fact (structure → ARCHITECTURE.md, behavior → topic docs, index → CLAUDE.md, onboarding → README + relatives; a fact found twice becomes a link).

- [x] **Task 2: Delete the `3d`/`3д` mode wholesale from SKILL.md** (depends on Task 1)
  Files: `src/skills/aif-docs/SKILL.md`
  Remove every `3d` artifact: the `3d|3д` token in `argument-hint` (`:4`, leaving `"[--web]"`); the `3d` line and its `MODE detection` prose in Step 0.1 (`:64`, `:67-70`) — Step 0.1 keeps only `--web` parsing; the entire "Document-Driven Development (3D mode)" section and its `implementation must conform to <doc-path>` conform-pointer (`:72-92`, including the `---` separators); the `**If MODE = 3D:**` branch opening Step 1 (`:95`). After removal there is **one mode** — no `MODE = normal` vs `MODE = 3D` framing survives anywhere. Verify no `3d`/`3д`/`MODE = 3D`/`Document-Driven` token remains in the file.

- [x] **Task 3: Reframe Step 1 and make referent-dependent checks conditional** (depends on Task 2)
  Files: `src/skills/aif-docs/SKILL.md`
  Rewrite `Step 1: Determine Current State` (`:93-97`) so it determines **the subject** — behavior + invariants — without assuming shipped code: read the code where it exists and treat it as the referent; where it does not exist, treat the doc as the contract. The State A/B/C detection (what doc files exist) stays; drop the "use existing code as the content source" assumption. Rewrite the Step 2.1 (State C) **stale content** check (`:345`): remove the `MODE = 3D` suppression parenthetical and make it **per-item conditional on the referent** — flag stale references only for surfaces whose code exists; where the code does not exist the doc is the spec, not stale. Rewrite the Step 4 review carve-out (`:395-400`): delete the `MODE = 3D` heading/branch and instead state that the accuracy checks needing a running referent are **each conditional on that referent existing** — verified against the code where the surface exists, skipped (the doc is the spec) where it does not. This is a per-check condition, **not** a mode; add **no** lead/lag explanation. Sweep the residual "mode" vocabulary the collapse orphans: the "**No-motivation pass (mandatory, all modes):**" heading (`:391`) becomes "(mandatory)" — no mode qualifier survives. Keep the no-motivation pass and Principle 6 unconditional across the file.

  **Coordination-trio staleness (spec Change item 4).** In the Step 2.1 (State C) audit, add an explicit on-each-run check of the **coordination trio** — README, the CLAUDE.md `## Documentation` index, and ARCHITECTURE.md — for staleness. Refresh what aif-docs owns (README length/pointer, the CLAUDE.md index rows); for **ARCHITECTURE.md, check for staleness but do not clobber** its structural info — no descriptive-vs-structural boundary is drawn and no `aif-architecture`/ARCHITECTURE.md edit is made here (it stays read-only per Step 0 and Artifact Ownership). If existing State C audit wording (README length + CLAUDE.md-index staleness) already covers part of this, extend it to name the trio and the ARCHITECTURE.md check-don't-clobber stance explicitly rather than duplicating.

### Phase 2: Purge 3d and linear-nav residue from references

- [x] **Task 4: Rewire REVIEW-CHECKLISTS.md — referent-conditional accuracy, drop 3D, purge nav** (depends on Task 3)
  Files: `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md`
  Replace the `MODE = 3D` skip parentheticals on the Technical Checklist accuracy items (`:11` code-examples-match, `:12` installation-instructions-work) with a **per-item referent condition**: verify against the code where the documented surface exists; where it does not, the doc is the spec and the item does not apply — no mode language. Remove the "(applies in all modes including 3D)" parenthetical from the no-motivation item (`:15`), leaving the rule stated flatly (it always applies). Delete the linear-nav prescriptions: the "After reading README, is it clear where to go next?" item (`:43`) and the linear-path reading-order framing in the CLAUDE.md-ordering item (`:44`) — replace with the feature-cross-link tree model: where a doc names a feature a deeper doc expands, it links to it by relative path (edges/leaves of a tree grown across runs; in ARCHITECTURE.md, module/subsystem mentions link to their topic docs). The ARCHITECTURE.md tree-link line is **check-only for aif-docs** — verify the links' presence; authoring/repairing them is aif-architecture's or a human's job, since ARCHITECTURE.md stays read-only here (mirror Task 3's check-don't-clobber stance so the checklist item never drives an edit into that file). No See Also, no prev/next, no "next steps" sections. Verify no `3d`/`MODE = 3D`/`see also`/`next steps`/`where to go next` token remains.

- [x] **Task 5: Remove linear-nav residue from topic-guides.md** (depends on Task 4)
  Files: `src/skills/aif-docs/references/topic-guides.md`
  Delete the "Next steps links" bullet under `getting-started.md` (`:8`). Do not add a replacement "See Also"/next-steps line; cross-links follow the feature-tree model (link a named feature to the doc that expands it), not a fixed linear sequence.

### Phase 3: Verify

- [x] **Task 6: Run the spec's verification greps** (depends on Task 5)
  Files: (verification only — `src/skills/aif-docs/`)
  From `src/skills/aif-docs/`, confirm: `grep -rin "3d\|3д\|MODE = 3D\|Document-Driven" SKILL.md references/` → zero hits; `grep -rin "see also\|next steps\|where to go next\|prev/next" SKILL.md references/` → zero hits. Also sweep for orphaned mode vocabulary — `grep -rin "all modes\|every mode\|MODE = normal" SKILL.md references/` → zero hits (the collapse leaves one mode, so no "mode" qualifier should survive; a bare `mode` inside an unrelated word like "model" is fine — inspect any hit). Confirm the skill identity (frontmatter `description` + H1) + Core Principles now state docs are ТЗ (behavior/protocols/flows/connections) with README + relatives as the onboarding exception, that the `description`'s trigger phrases are intact, and that **no** lead/lag meta-commentary was introduced. If any grep is non-empty or a guard fails, return to the owning task and fix before finishing.

## Commit Plan
- **Commit 1** (after tasks 1-3): "Reframe aif-docs as ТЗ-first and delete the 3d mode"
- **Commit 2** (after tasks 4-6): "Purge 3d and linear-nav residue from aif-docs references"

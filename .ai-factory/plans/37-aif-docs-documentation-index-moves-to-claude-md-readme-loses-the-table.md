# Plan: aif-docs: documentation index moves to CLAUDE.md; README loses the table

## Context
Retarget every create/update/audit touchpoint of the README `## Documentation` table to a `## Documentation` section in the project's CLAUDE.md; README keeps only a one-line pointer to the docs directory. The touchpoints span **two** files, both inside `src/skills/aif-docs/`: `SKILL.md` (templates, steps, ownership) and `references/REVIEW-CHECKLISTS.md` (the enforced audit + auto-fix rules the skill reads at Steps 2.1.1 and 4).

### Deviation from spec note 48 (resolved, not escalated)
Spec note 48 line 25 lists "review checklists … unchanged," but line 14 requires "every place the README table is audited is retargeted." These contradict: `references/REVIEW-CHECKLISTS.md` **is** where the README-table audit lives, and its Standards-Compliance row (line 57) is an **auto-fix** that would re-add the README table on the next State C run — self-reverting the feature and producing false Step-4 review failures. The milestone's whole intent is to relocate the index, so the checklist file must move with it. This plan therefore treats the checklist retarget as in-scope (Task 8), overriding spec line 25 as a spec blind spot. No `milestone-rescue` escalation needed — the intent is unambiguous.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Scope & invariants
- Edits are confined to two files under `src/skills/aif-docs/`: `SKILL.md` and `references/REVIEW-CHECKLISTS.md`. Nothing else.
- Do **not** touch the upstream mirror (`upstream/ai-factory/aif-docs`). Frontmatter stays unchanged.
- The `SKILL.md` body is already over the 500-line guideline (known, accepted) — prefer rewording existing lines over adding new blocks; do not grow it materially.
- **AGENTS.md handling is out of scope beyond the redirect carve-out (Task 7).** Per spec item 6, Step 5's existing AGENTS.md `## Documentation` table is preserved as-is for standalone AGENTS.md projects — this milestone replaces the *README* index with CLAUDE.md, not the AGENTS.md section. The AGENTS.md/CLAUDE.md pairing is pre-existing behavior the spec explicitly keeps; only the redirect case defers to CLAUDE.md.

## Tasks

### Phase 1: Retarget the index home to CLAUDE.md (SKILL.md)

- [x] **Task 1: Reword Core Principle 3**
  Files: `src/skills/aif-docs/SKILL.md` (line 21)
  Rewrite Principle 3 ("No duplication") so it states: detailed info lives in the resolved docs directory and README links to it (not repeats it); the **documentation index lives in the project's CLAUDE.md** — a `## Documentation` table (`| Doc | What it covers |`), README not listed in it. README carries at most one pointer line to the docs directory, never an index table. Keep the existing installation-command exception. Keep it to roughly the current line count.

- [x] **Task 2: Strip the Documentation table from the State A README template + rules** (depends on Task 1)
  Files: `src/skills/aif-docs/SKILL.md` (Step 2.2, template lines ~291-298; rule line ~311)
  In the 2.2 README markdown template, remove the `## Documentation` table section and replace it with a single pointer line to the docs directory (e.g. `See [documentation](<readme-to-docs-dir>/) for full docs.`). In "Key rules for README", change the "Documentation table with links to the resolved docs directory" bullet to "Single pointer line to the docs directory (no index table)". Leave landing-page, tagline, quick-start, features, example, and license rules untouched.

- [x] **Task 3: Add the CLAUDE.md index step** (depends on Task 2)
  Files: `src/skills/aif-docs/SKILL.md` (new sub-step right after Step 2.2, or fold into Step 5)
  Add a concise step that creates or updates the `## Documentation` section in the project's CLAUDE.md: table shape `| Doc | What it covers |`, one row per doc page, README **not** listed, descriptions under ~12 words, rows in the docs directory's logical reading order. If CLAUDE.md does not exist, create it with only this section plus a one-line header. Keep the block tight (a handful of lines).

### Phase 2: Retarget update + audit touchpoints (SKILL.md)

- [x] **Task 4: Retarget the Step 1.1 consolidation link** (depends on Task 3)
  Files: `src/skills/aif-docs/SKILL.md` (line 208)
  Change "Add the new doc page to README's Documentation table using the correct path relative to README" → "Add the new doc page to CLAUDE.md's Documentation section".

- [x] **Task 5: Retarget State B split rules** (depends on Task 4)
  Files: `src/skills/aif-docs/SKILL.md` (Step 2 State B: lines ~374, ~395, ~410)
  In the "Stays in README" list (2.1), change "Documentation links table" to the single pointer line. In the 2.2 proposal example, change the "✓ Documentation links table" item to "✓ Pointer line to docs dir". In 2.3 "Execute the split", change "Rewrite README as landing page with Documentation links table" to "Rewrite README as landing page with a pointer line to the docs dir; create/update the `## Documentation` section in CLAUDE.md". Keep wording minimal.

- [x] **Task 6: Retarget State C audit + add legacy-table check** (depends on Task 5)
  Files: `src/skills/aif-docs/SKILL.md` (Step 2 State C 2.1: lines ~417-425)
  State C 2.1 in SKILL.md has no explicit README-table check (only the generic broken-links check at line 421 — leave that intact for docs cross-links). Add one audit check that flags a README still carrying a documentation table as a legacy layout and proposes moving the index to CLAUDE.md. Note: the *substantive* audit-and-auto-fix retarget lives in the checklist file (Task 8) — this SKILL.md check is only the surface-level legacy flag.

- [x] **Task 7: Note the AGENTS.md → CLAUDE.md redirect case in Step 5** (depends on Task 6)
  Files: `src/skills/aif-docs/SKILL.md` (Step 5, lines ~531-554)
  Two edits: (a) Keep existing AGENTS.md handling as-is (skip silently when the file/section is absent); add one sentence: when AGENTS.md is a one-line redirect to CLAUDE.md, the CLAUDE.md `## Documentation` section from Task 3 is the single source and AGENTS.md is left untouched. (b) **Fix the dangling ordering reference (review Issue 2):** line 549 says "in the same order as the README Documentation table" — Task 2 deleted that table. Retarget it to "in the same order as the CLAUDE.md `## Documentation` section (docs directory's logical reading order)", matching Task 3's ordering rule.

- [x] **Task 8b: Declare CLAUDE.md's Documentation section in ownership + rules** (depends on Task 7)
  Files: `src/skills/aif-docs/SKILL.md` ("Artifact Ownership" lines ~560-564; Important Rule #7 line ~574)
  The skill now creates/writes the project's CLAUDE.md `## Documentation` section. Add "the `## Documentation` section in `CLAUDE.md`" to the primary-ownership list in "Artifact Ownership" and to the ownership-boundary clause in Important Rule #7, alongside the existing README / docs-dir / AGENTS.md entries. Scope the ownership to that section only, not the whole CLAUDE.md file.

### Phase 3: Retarget the enforced review checklists (REVIEW-CHECKLISTS.md)

- [x] **Task 8: Retarget the README-table checklist rules to CLAUDE.md** (depends on Task 3; parallel to Phase 2)
  Files: `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md` (lines 8, 44, 57)
  Three retargets so the enforced audit stops mandating and auto-restoring the README table:
  - **Line 8 (Technical Checklist):** `README has: title, tagline, quick start, example, documentation table, license` → drop `documentation table`; the checked README items become title, tagline, quick start, example, license (+ optionally "single pointer line to docs dir").
  - **Line 44 (Readability):** "Is the Documentation table **in README** ordered by the path a new user would follow?" → retarget to the `## Documentation` section **in CLAUDE.md** (same "getting started → workflow → details" ordering intent).
  - **Line 57 (Standards Compliance auto-fix):** replace the "Missing Documentation table in README | … | Add table" row with two corrected rows: (1) missing/stale `## Documentation` section in CLAUDE.md → detect via CLAUDE.md having no such section (or rows out of sync with docs dir) → auto-fix "Create/update the CLAUDE.md `## Documentation` section"; (2) **legacy README table present** → detect via README still containing a documentation table → auto-fix "Move the index to CLAUDE.md and replace with a pointer line". This retires the self-reverting auto-fix (review Critical Issue 1) and puts the real audit where the skill enforces it.
  Keep every other checklist item (README length, broken links, no-motivation, scannability, etc.) unchanged.

## Verification
After edits, do a dry read-through of a State C audit path: confirm no remaining instruction (SKILL.md **or** REVIEW-CHECKLISTS.md) requires, orders, or auto-adds a README documentation table, and that the CLAUDE.md `## Documentation` section is the single index home. Grep both files for "documentation table" / "Documentation table" / "README Documentation" to catch stragglers.

## Commit Plan
- **Commit 1** (Tasks 1-3): "Move aif-docs documentation index from README to CLAUDE.md"
- **Commit 2** (Tasks 4-7, 8b): "Retarget aif-docs consolidation, audit, and ownership touchpoints to CLAUDE.md index"
- **Commit 3** (Task 8): "Retarget aif-docs review checklists off the README documentation table"

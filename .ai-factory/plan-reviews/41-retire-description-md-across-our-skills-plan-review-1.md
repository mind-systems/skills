## Code Review Summary

**Files Reviewed:** Plan (10 target files) + `update-config.mjs` (uncovered dependency)
**Risk Level:** 🔴 High

The plan is precise almost everywhere — every line reference in Tasks 1–7 was checked against the live codebase and matches (roadmap-engine 84/158, roadmap-outline 35, roadmap-test-coverage 28/35, roadmap-decompose-skeleton 62, detangle 30, aif-docs 31/35/42/475/476, aif-plan 16/47, EXAMPLES.md 24, config-template 36–38). The grep reference set is complete. But Task 8 removes one half of a lockstep pair and leaves the other half asserting the removed key exists, which hard-breaks the `aif` config generator.

### Context Gates
- **Architecture (`.ai-factory/ARCHITECTURE.md`):** WARN — the repo's own composition rule states "Cross-file invariants that grep can't derive … get one sentence declared at the coupling point in **both** files." `config-template.yaml` (schema) and `update-config.mjs` (`SECTION_KEYS`) are exactly such a coupled pair, and the plan edits only one side. See Critical Issue 1.
- **Rules:** No `.ai-factory/RULES.md` present — skipped.
- **Roadmap:** Not reviewed for milestone linkage (plan-only review); the plan's scope notes cite notes 50/51 as the governing upstream context, consistent with the milestone framing.

### Critical Issues

**1. Task 8 breaks `update-config.mjs` — `paths.description` is NOT consumed only by aif-docs.**
`src/skills/aif/references/update-config.mjs` line 9 lists `'description'` in `SECTION_KEYS.paths`. `parseTemplate()` (lines 394–398) iterates every key in `SECTION_KEYS[section]` and calls `fail(3, "Template is missing managed key ${sectionName}.${key}")` when the template lacks it. The `aif` skill invokes this script with `config-template.yaml` as the `--template` on every run (SKILL.md lines 87, 95–96, 240 — Modes 1/2/3 all write config via it).

Task 8 deletes the `description:` key from `config-template.yaml` but leaves `'description'` in `SECTION_KEYS.paths`. Result: **the very next `/aif` run exits 3 with "Template is missing managed key paths.description"** — config generation is dead for all modes. `Testing: no` means nothing catches it.

The plan's premise (Task 8: "the config schema and its only consumer stay in sync"; Scope note: "aif-docs is the config's only consumer") is wrong. `update-config.mjs` is a second, structural consumer that treats every `SECTION_KEYS` entry as mandatory-present-in-template.

Fix: extend Task 8 to also delete `'description'` from the `SECTION_KEYS.paths` array in `update-config.mjs` (line 9), in the same commit. Removing the template key and the code key must be atomic — the reverse order (code first) is equally required to keep them in sync. Note the plan's own scope carve-out ("aif skill generation … out of scope") does not cover this: Task 8 already edits an `aif/references/` file, so consistency inside `aif` is unavoidably in scope once the schema key is touched.

Secondary check for the implementer: confirm no default project `config.yaml` shipped in the repo or referenced payloads set `paths.description` (a `--payload` containing `paths.description` would now hit the `ALLOWED_PATHS` guard at line 234 and `fail(3, "Unknown managed key path")`). Grep found none in `src/`, but the aif SKILL.md payload construction should be eyeballed when Task 8 lands.

### Minor Notes (non-blocking)
- Scope-note counts are slightly under-stated vs. the tasks: `aif-plan (×2)` actually spans three edit points (SKILL.md 16, 47; EXAMPLES.md 24) and `aif-docs (×3)` spans five (31, 35, 42, 475, 476, two of them lowercase `paths.description`). Task 5 and Task 7 bodies correctly enumerate all locations, so this is a labeling imprecision only — no coverage gap.
- Task 5 leaves the "If config.yaml doesn't exist, use defaults" list (lines 34–38) with ARCHITECTURE/Docs/Language after dropping the DESCRIPTION default — correct and self-consistent.

### Positive Notes
- Line-level targeting is accurate throughout; the grep reference set matches the live tree exactly, and the `roadmap-decompose`-delegates-to-`roadmap-engine` reasoning (no direct hit, covered by Task 1) is correct.
- Correctly keeps `upstream/ai-factory/` untouched and correctly declines to add "read CLAUDE.md" replacements (matches the global doc-noise rule).
- Task 5/Task 8 coupling was *identified* by the plan and routed into one commit — the instinct was right; it just stopped one file short of the actual coupled set.
- Commit split (roadmap family, then aif-docs/detangle/aif-plan/config) is clean and each commit leaves the tree coherent — provided the Task 8 fix above is folded into Commit 2.

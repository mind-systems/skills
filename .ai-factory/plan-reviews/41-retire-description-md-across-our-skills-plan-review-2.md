## Code Review Summary

**Plan:** `41-retire-description-md-across-our-skills.md` (review round 2)
**Files Reviewed:** plan + 12 target files + governing spec note 52 + roadmap line 93 + `update-config.mjs` internals
**Risk Level:** 🟢 Low

### Context Gates

- **ARCHITECTURE.md** — WARN(none). Edits are confined to `src/skills/*` and one `references/` file; `upstream/ai-factory/` stays byte-pristine per the repo's three-way split. No `loads:` dependency edge is added or removed (only content is deleted), so the skill graph is unaffected. Boundary-clean.
- **RULES.md** — absent from `.ai-factory/` (only `ARCHITECTURE.md`, `ROADMAP.md`, and artifact dirs exist). Gate skipped; no blocking criteria requested.
- **ROADMAP.md** — milestone at line 93 ("Retire DESCRIPTION.md across our skills") matches the plan's `# Plan:` heading and scope. `Spec:` tag points at `.ai-factory/notes/52-retire-description-md.md`, which the plan honors faithfully. Linkage present.
- **Governing spec (note 52)** — the plan covers every "expected" edit point the spec names (roadmap-engine, outline, decompose, decompose-skeleton, test-coverage Layer 1, aif-docs Step 0) **and** correctly extends to the full grep set the spec instructs to discover ("plus whatever else the grep finds"): detangle, aif-plan, and the `aif` config machinery. The spec's "do NOT" list is respected — no CLAUDE.md-read replacements, ARCHITECTURE/RULES untouched, no project-file hunting, orchestrator left alone.

### Verification Performed

Every factual claim in the plan was checked against the codebase and holds:

- **Line numbers** — all match a fresh `grep -rni DESCRIPTION src/skills/ src/commands/`: roadmap-engine 84/158, roadmap-outline 35, roadmap-decompose-skeleton 62, roadmap-test-coverage 28/35, aif-docs 31/35/42/475/476, detangle 30, aif-plan SKILL 16/47 + EXAMPLES 24, config-template.yaml 36–38, update-config.mjs 9.
- **Prose descriptions** — read each target block; the plan's surgical instructions (which lines to delete, which to keep, the exact fallback rewrites) faithfully describe the real text in every case.
- **roadmap-decompose "no direct hit"** — confirmed: the only DESCRIPTION-family hits in that file are frontmatter `description:` and `argument-hint`, not a project-context read. Delegation to roadmap-engine's Step 0 (Task 1) genuinely covers it.
- **Repo-docs bookkeeping is a true no-op** — independent grep of `CLAUDE.md README.md AGENTS.md docs/ src/global/` surfaces only the frontmatter `description: >-` example and generic "task description" prose. No DESCRIPTION.md artifact-list entry exists, so note 52's "grep the repo docs too" bookkeeping correctly requires zero edits.
- **Task 8 config-machinery reasoning is fully substantiated:**
  - `parseTemplate()` (update-config.mjs 383–418) iterates `SECTION_KEYS.paths` and `fail(3, "Template is missing managed key paths.<key>")` at line 397 when the template lacks a key — so deleting the template `description:` block **without** deleting the `SECTION_KEYS` entry would exit 3.
  - The `aif` skill invokes this script with `config-template.yaml` as `--template` on every mode (SKILL.md 95–96, 240) — confirming the "kills config generation for all modes" claim.
  - `ALLOWED_PATHS` (34–36) + `validateValueMap` (234) would reject any payload carrying `paths.description`; grep confirms no `--payload`/`config.update.json` construction in `src/` sets it. The atomic-commit constraint (template + `SECTION_KEYS` + aif-docs resolution in one commit) is correct and necessary.
  - Merge-mode safety (not called out but worth noting it doesn't break): against an older project `config.yaml` that still carries `paths.description`, `parseSection` (309) simply `continue`s past the now-unmanaged key — it is left untouched, no crash. Out of this task's `src/`-only scope, as intended.

### Critical Issues

None.

### Positive Notes

- **Grep-anchored, flux-aware.** The plan re-derives its edit set from `grep` exactly as note 52 mandates, rather than trusting a stale file list — the right instinct given how many of these skills were just refactored.
- **Task 8 is the standout.** It catches a non-obvious coupled failure (template key and `SECTION_KEYS` entry must die together or the next `/aif` run hard-fails) that a naive "just delete the DESCRIPTION lines" pass would have missed, and pins the atomic-commit requirement plus an implementer eyeball check for stray payloads. This is precisely the kind of hidden contract the repo's "cross-file invariants get one sentence at the coupling point" rule targets.
- **Clean two-commit sequencing.** Roadmap-family reads (Tasks 1–4) separate cleanly from the aif-docs/config cluster (Tasks 5–8), and the dependency (Task 8 depends on Task 5) is stated with the in-same-commit rationale.
- **Fallback-source handling is correct.** Where DESCRIPTION was one branch among several (roadmap-outline vision line, test-coverage stack inference, roadmap-engine Update-mode "for context"), the plan drops only that branch and keeps user-input / package-manager-file sources — matching note 52's instruction.
- **Implementer nicety (not a defect):** for roadmap-engine Update mode (line 158), the plan's stated end-state — "leaving `$TARGET_FILE` and the brief codebase check" — is the clean result; the implementer should drop the stray comma so it reads "`$TARGET_FILE` and a brief codebase check" rather than "`$TARGET_FILE`, and …". The plan already describes the desired wording, so no change is required.

The plan is accurate, complete against its governing spec, architecturally sound, and free of missing steps, wrong path/API assumptions, or migration gaps.

PLAN_REVIEW_PASS

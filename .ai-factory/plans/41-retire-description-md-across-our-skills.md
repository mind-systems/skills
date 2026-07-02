# Plan: Retire DESCRIPTION.md across our skills

## Context
DESCRIPTION.md duplicated the project CLAUDE.md (which every agent already receives via the CLI) and its unique vision tier lives in the roadmap `>` line + CLAUDE.md Purpose; this milestone deletes every live "Read `.ai-factory/DESCRIPTION.md`" instruction and mention from our `src/` skills without adding CLAUDE.md-read replacements. Grep of repo docs (`CLAUDE.md`, `README.md`, `AGENTS.md`, `docs/`, `src/global/`) returned no DESCRIPTION mentions, so no bookkeeping edits are needed there.

## Scope notes
- All edits are in `src/skills/*` (and one `references/` file). `upstream/ai-factory/` is left byte-pristine — never touched.
- Full edit-point set (from `grep -rn DESCRIPTION src/skills/ src/commands/`, plus the `paths.description` lowercase hits and the coupled `update-config.mjs` code key): `roadmap-engine` (84, 158), `roadmap-outline` (35), `roadmap-decompose-skeleton` (62), `roadmap-test-coverage` (28, 35), `aif-docs` (31, 35, 42–45, 475, 476), `detangle` (30), `aif-plan` SKILL.md (16, 47) + `references/EXAMPLES.md` (24), `aif/references/config-template.yaml` (36–38) + `aif/references/update-config.mjs` (9). `roadmap-decompose` has **no** direct hit — it delegates Step 0 to `roadmap-engine`, so Task 1 covers it.
- `ARCHITECTURE.md` and `RULES.md` reads stay untouched everywhere.
- Do **not** add any "read CLAUDE.md" instruction — CLAUDE.md is auto-loaded; instructing it is noise.
- `aif` skill generation and `aif-architecture` sourcing are separate landed tasks (notes 50/51); the orchestrator's own prompts are a separate roadmap task. This task only removes the residual `paths.description` config machinery that note 50 left behind (Task 8), since note 50 explicitly deferred the DESCRIPTION concern here.
- `paths.description` has **two** consumers, not one: `aif-docs` (resolves/reads it) and `src/skills/aif/references/update-config.mjs` (the config generator, which treats every `SECTION_KEYS.paths` entry as mandatory-present-in-template and hard-fails otherwise). Both, plus the template default, must be removed atomically — see Task 8. Grep confirms no default project `config.yaml` or `--payload` in `src/` sets `paths.description`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Roadmap family

- [x] **Task 1: roadmap-engine — drop DESCRIPTION from Step 0 and Update mode**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In Step 0 (Project context, ~line 84) delete the whole **Read `.ai-factory/DESCRIPTION.md`** block (its heading + the three tech-stack/architecture/NFR bullets); keep the following **Read `.ai-factory/ARCHITECTURE.md`** block intact as the new first context read. In Update mode (~line 158) remove `` `.ai-factory/DESCRIPTION.md` for context, `` from the "Read current state" sentence, leaving `$TARGET_FILE` and the brief codebase check as the sources. This also covers `roadmap-decompose`, which delegates Step 0 here.

- [x] **Task 2: roadmap-outline — vision line sourced from user input only**
  Files: `src/skills/roadmap-outline/SKILL.md`
  At ~line 35 the vision line is "sourced from `DESCRIPTION.md` or user input". Drop the `DESCRIPTION.md` branch so it reads "sourced from user input" (keep the surrounding two-tier-rendering sentence and the optional-note guidance unchanged).

- [x] **Task 3: roadmap-decompose-skeleton — remove Step 0 DESCRIPTION read**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In Step 0 (~line 62) delete the **Read `.ai-factory/DESCRIPTION.md`** line entirely; keep the **Read `.ai-factory/ARCHITECTURE.md`** line and the target-roadmap read that follow.

- [x] **Task 4: roadmap-test-coverage — drop DESCRIPTION from Layer 1**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In Layer 1 (~lines 27–36) remove the `` - `.ai-factory/DESCRIPTION.md` — tech stack, test runner, conventions `` list item, keeping the `ARCHITECTURE.md` and `ROADMAP.md` items. Then rewrite the fallback "If no DESCRIPTION.md, infer stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`." to drop the DESCRIPTION conditional — make stack inference from the package-manager files the unconditional source (e.g. "Infer stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`.").

### Phase 2: aif-docs, detangle, aif-plan, aif config

- [x] **Task 5: aif-docs — remove DESCRIPTION read and config resolution**
  Files: `src/skills/aif-docs/SKILL.md` (five edit points: 31, 35, 42–45, 475, 476)
  Step 0: remove the `- DESCRIPTION.md: .ai-factory/DESCRIPTION.md` default line (~35) and the entire **THEN: Read `.ai-factory/DESCRIPTION.md`** block with its bullets (~42–45); keep the **Also read `.ai-factory/ARCHITECTURE.md`** block. Drop `paths.description` from the config resolution bullet (~31, leaving `paths.architecture` and `paths.docs`) and from the Artifact Ownership "Config use" line (~475). Remove `` `.ai-factory/DESCRIPTION.md`, `` from the Artifact Ownership "Read-only context" line (~476), leaving `ARCHITECTURE.md` and the roadmap/rules/research artifacts. (Coupled with Task 8 — the `paths.description` key is removed here, in the template, and in `update-config.mjs` together; do all three in the same commit.)

- [x] **Task 6: detangle — remove DESCRIPTION context read**
  Files: `src/skills/detangle/SKILL.md`
  In "Before you start — load project context" (~lines 30–32) delete the `If .ai-factory/DESCRIPTION.md exists — read it…` paragraph; keep the ARCHITECTURE.md and ROADMAP.md read paragraphs that follow.

- [x] **Task 7: aif-plan — remove DESCRIPTION reads from Step 0 and examples**
  Files: `src/skills/aif-plan/SKILL.md`, `src/skills/aif-plan/references/EXAMPLES.md`
  In `SKILL.md` Step 0 (~16–20) delete the **FIRST: Read `.ai-factory/DESCRIPTION.md`** block with its bullets so the **ALSO: Read `.ai-factory/ARCHITECTURE.md`** block becomes the leading read (adjust the "ALSO" wording to read naturally as the first item if needed). At ~line 47 rewrite "Skip if `.ai-factory/DESCRIPTION.md` already provides sufficient context." to drop the DESCRIPTION reference (e.g. "Skip if existing project context is already sufficient."). In `references/EXAMPLES.md` (~line 24) change "reads DESCRIPTION.md / ARCHITECTURE.md for context" to "reads ARCHITECTURE.md for context".

- [x] **Task 8: aif config machinery — drop the dead `description` path key from template AND generator (depends on Task 5)**
  Files: `src/skills/aif/references/config-template.yaml`, `src/skills/aif/references/update-config.mjs`
  In `config-template.yaml` remove the `# Project description file` / `# Default: .ai-factory/DESCRIPTION.md` / `description: .ai-factory/DESCRIPTION.md` block under `paths:` (~36–38), leaving `architecture:` and `docs:`.
  In `update-config.mjs` remove the `'description',` entry from the `SECTION_KEYS.paths` array (line 9), leaving `'architecture'` as the first key.
  **Why both:** `parseTemplate()` (`update-config.mjs` ~394–398) iterates every key in `SECTION_KEYS.paths` and calls `fail(3, "Template is missing managed key paths.<key>")` when the template lacks it; the `aif` skill runs this script with `config-template.yaml` as `--template` on every mode (SKILL.md 87, 95–96, 240). Deleting the template key without deleting the `SECTION_KEYS` entry makes the next `/aif` run exit 3 and kills config generation for all modes — so template + code + Task 5's aif-docs resolution must land in the **same commit**. Implementer check when this lands: eyeball the `aif` SKILL.md `--payload` construction to confirm nothing passes `paths.description` (it would now hit the `ALLOWED_PATHS` guard at ~line 234 and `fail(3, "Unknown managed key path")`); grep already shows no such payload in `src/`.

## Commit Plan
- **Commit 1** (after tasks 1-4): "Drop DESCRIPTION.md reads from roadmap skills"
- **Commit 2** (after tasks 5-8): "Retire DESCRIPTION.md from aif-docs, detangle, aif-plan, and aif config machinery" — Tasks 5 + 8 (aif-docs resolution + template key + `update-config.mjs` `SECTION_KEYS` key) must all be inside this one commit so the config schema and both its consumers stay in sync.

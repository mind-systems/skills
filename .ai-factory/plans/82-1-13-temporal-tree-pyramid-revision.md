# Plan: temporal-tree — pyramid revision

## Context
Audit `src/skills/temporal-tree/SKILL.md` (157 lines) against the pyramid, the two-reader register, and the walkable-tree rule; fix only what the audit finds. "No change" plus a one-paragraph audit report is a complete, legal outcome — padding a conformant skill is itself a failure.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Audit

- [x] **Task 1: Audit the skill against the philosophy and write the report**
  Files: `src/skills/temporal-tree/SKILL.md` (read-only in this task), `src/skills/temporal-tree/docs/overview.md` (read-only)
  Read the body in full against three lenses:
  - **Restated shared contracts** — the `## Features` table is owned by `roadmap-prune`/`ARCHITECTURE.md`. Judge whether "Before you start" (lines 24–32) and Step 1 restate that contract instead of linking to its owner (walkable-tree rule: a fact's second home is a link to its first). Also check whether SKILL.md narrative duplicates the existing `docs/overview.md`.
  - **Procedural ceremony** — per `docs/skill-composition-model.md` (what-to-pin vs what-to-trust): flag narration the executor performs unprompted (e.g. "Read the patch. Note what files were added…", obvious step sequencing). Distinguish it from **pinned values that must stay**: the exact `git show`/`git log`/`git diff` command templates with their path arguments, and the Synthesis output block format — these are contracts, not ceremony, and stay verbatim.
  - **Two-reader register** (`docs/skill-composition-model.md` § "У каждой строки два читателя") — verify each line addresses the right reader: instructions to the executor are imperatives; knowledge for the editor is declarative. Flag any misaddressed lines.
  Produce a one-paragraph audit report that names **each finding with its concrete fix**, or states conformance. This report is the task's primary deliverable and gates Task 2. Reference `docs/skill-pyramid.md` and `docs/skill-composition-model.md` as the audit standard.

### Phase 2: Apply findings (only if the audit finds any)

- [x] **Task 2: Apply only the audit-confirmed fixes** (depends on Task 1)
  Files: `src/skills/temporal-tree/SKILL.md`
  Apply **only** what Task 1's report names — restated shared contracts become links to their owner, procedural ceremony is cut, misaddressed lines are re-registered. Skip this task entirely if the audit reported conformance.
  Guards (from the spec's Guards + Guardrails):
  - Behavior-identical whatever the outcome; **frontmatter unchanged** (name, description, argument-hint, allowed-tools).
  - Pinned values stay pinned — git command templates with path args and the Synthesis output block are byte-identical.
  - **No mass moves to `references/`** unless the audit explicitly named a rarely-read branch — do not invent structure.
  - Do not add or expand content; a revision only removes/relinks/re-registers.

- [x] **Task 3: Live baseline verification (only if the body changed)** (depends on Task 2)
  Files: none (verification only)
  If and only if Task 2 changed the body, confirm behavior is identical. Note: this repo's `.ai-factory/ARCHITECTURE.md` has **no `## Features` table and no anchored hashes** (`roadmap-prune` has never run here), so the skill's Step 1 has no input and the full feature-walk cannot be exercised against this repo. The behavioral guarantee therefore rests on the Task 2 guard — the `git show`/`git log`/`git diff` templates and the Synthesis output block are byte-identical. To confirm the mechanics still resolve: pick any real commit hash from this repo's `git log --oneline` and manually dry-run each pinned template against it (`git show <hash>`, `git show <hash>:.ai-factory/ROADMAP.md`, `git log --oneline <hash>~5..<hash>`, `git diff <hash>~1 <hash> -- .ai-factory/plans/`), verifying each still produces the same shape of output pre/post. If Task 2 was skipped (conformance), no baseline is needed.

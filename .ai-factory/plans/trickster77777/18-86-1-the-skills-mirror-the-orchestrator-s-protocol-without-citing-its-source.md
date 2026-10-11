# Plan: 86.1 — the skills mirror the orchestrator's protocol without citing its source

## Context
Two skills cite orchestrator source files and functions that no longer hold what they are cited for. One is `orchestrator-artifacts` § "7. Mirrors-the-orchestrator invariant". The other is `task-rescue` § "Valid sidecar `step` states", where `_detect_task_step()` no longer exists. This task restates each mirror as behaviour, with no file, path or function named. The after-texts are pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0248-the-skills-mirror-the-orchestrators-protocol-without-citing-its-source.md`, § "What must be true after". Copy them exactly and do not paraphrase. The phase note (`.ai-factory/specs/trickster77777/0247-the-skills-speak-of-the-orchestrators-protocol-not-of-its-source.md`) states the governing rule: a skill speaks of the orchestrator as an executor and states a mirrored protocol as behaviour. No `.ai-factory/RULES.md` exists.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit the two skills

- [x] **Restate the § 7 mirror invariant in `orchestrator-artifacts`**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Under the heading "## 7. Mirrors-the-orchestrator invariant", replace the whole paragraph. It currently opens "This file mirrors the orchestrator's file protocol (`orchestrator/main.py`," and ends "… update this file; do not let them diverge." Use the spec's pinned sentence:
  "This file mirrors the orchestrator's file protocol, and a change to that protocol on the orchestrator's side is a change here, made in lockstep."
  The paragraph is that single sentence. Hard-wrap it at about 84 columns to match the surrounding lines. Leave the heading and every other section unchanged.

- [x] **Restate the mirror sentence in `task-rescue`'s valid-states section**
  Files: `src/skills/task-rescue/SKILL.md`
  Under "### Valid sidecar `step` states", the first paragraph has four parts in this order:
  1. "This is a **closed set** — Step 5 picks one of the six values below, never invents one."
  2. The mirror sentence: "This table mirrors `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py` — if the orchestrator's accepted set changes, update this table; do not let them diverge."
  3. "The artifact paths here … the way Step 1 locates the sidecar."
  4. The rest of the paragraph.

  Replace only the mirror sentence (part 2) with the spec's pinned text:
  "This table mirrors the orchestrator's accepted set of sidecar `step` values — if it changes, update this table; do not let them diverge."
  Keep the closed-set sentence before it and the artifact-paths sentence after it byte-identical, per the spec ("The rest of each paragraph stands"). Re-wrap only the lines the edit touches, at the file's existing hard wrap of about 88 columns. Leave the table, the "N = 1" paragraph, the silent-failure line and the test-mode line unchanged.

### Verify the blast radius

- [x] **Run the spec's sweep** (depends on both edits above)
  Files: none changed. This is a read-only check.
  From the repo root, run the four greps from the spec's § "What breaks on contact" over `src`: `orchestrator/`, `_validate_sidecar_step`, `_detect_task_step` and `\.py`. Expected results:
  - The first three greps return nothing.
  - The `\.py` grep returns only `ui-ux-pro-max`'s own scripts. They stay as they are.
  - Neither edited skill appears in any of the four greps.

  Per the spec, no other skill, command or agent text names an orchestrator source. Edit no other file. In particular, leave alone `docs/the-pipeline-speaks-to-an-architect.md`: a doc may name a sibling repository's file by its root-relative path. Also leave the frontmatter `description:` of both skills unchanged.

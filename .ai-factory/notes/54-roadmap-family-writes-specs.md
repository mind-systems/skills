# Roadmap family writes specs to .ai-factory/specs/; readers follow the tag, not a directory

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review)

## Key Findings

- `.ai-factory/notes/` changed genre under its name: only the roadmap family writes there now — the files are task **specs**, and the research-note genre moved to `handoffs/`. New spec notes should live in `.ai-factory/specs/`.
- **Migration is lazy — no project is touched.** `Spec:` tags carry literal paths: existing tags keep pointing into `notes/` and keep working; new tasks get `specs/` paths; content moves as roadmaps live. Depends on note 53 (the `note` engine's destination hook).
- Corollary for readers: any skill that *reads or edits* a spec must resolve it **through the `Spec:` tag (follow the mention), never through a hardcoded directory** — then the split-brain period (some specs in `notes/`, some in `specs/`) is invisible to them.

## Details

Grep-driven (`grep -rn "notes/" src/skills/ src/commands/ docs/`), files may have moved since this note; expected touchpoints:

### Writers — retarget to `specs/`

- **`roadmap-engine`**: the two-tier format section — note path becomes `.ai-factory/specs/<NN>-<slug>.md`, the `Spec:` tag example likewise; when loading `note`, pass the destination `.ai-factory/specs/` via the new hook. Numbering scans `specs/`.
- **`roadmap-test-coverage`**: Layer 4 note-number scan and agent prompt paths → `.ai-factory/specs/`.
- Philosophies (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) — fix any literal `notes/` paths the grep finds (post-slim they should mostly defer to the engine).

### Readers — de-hardcode the directory

- **`milestone-rescue`**: every literal `.ai-factory/notes/<NN>-<slug>.md` reference becomes "the note behind the milestone's `Spec:` tag"; the artifact-discovery filter ("ignore files outside the four artifact directories, e.g. `notes/`") and the guard ("never touch `.ai-factory/notes/` except the deliberate spec-note repair") are rephrased directory-agnostically — spec files are wherever the tag points.
- **`command-pin-gaps`**, **`temporal-tree`**, any other reader the grep finds: same follow-the-tag rephrasing.

### Docs

- `docs/workflow.md`, `docs/skill-composition-model.md` (if it names `notes/`), repo `CLAUDE.md` — mention the genre split once: `specs/` = roadmap-family task specs (new), `notes/` = legacy location still served via tags, `handoffs/` = session handoffs.

### Constraints

- Depends on note 53 being implemented first (destination hook exists).
- No project migration: never `git mv` an existing `notes/` directory, never rewrite existing `Spec:` tags.
- Upstream mirror untouched.

## What NOT to do

- Do not leave any reader resolving specs by directory — the tag is the only resolution path.
- Do not touch `command-handoff` here (note 55) or `note`'s defaults (note 53).
- Do not bulk-edit existing roadmaps or note files in any project.

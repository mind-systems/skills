# note: destination and template hooks — one generic distiller, three genres

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review)

## Key Findings

- The `note` skill is the **generic distillation engine**: chat → note, part of a chat → note, a task spec, a handoff. Its callers differ only in *policy* — what sections to write and where to put the file. Today both are hardcoded (its own template; `.ai-factory/notes/`), which forced `command-handoff` to build its own file-writing machinery instead of loading the engine.
- Fix per the composition model: the mechanism (context mining, `<NN>` numbering scan, slug derivation, file placement, concision rules, English) stays in `note`; **destination directory and section template become caller-supplied hooks** with the current behavior as defaults.
- Genre → destination mapping (callers set it; this note only defines the hooks): roadmap family → `.ai-factory/specs/` (note 54), handoff → `.ai-factory/handoffs/` (note 55), **unset → `.ai-factory/notes/` as today**. The default keeps standalone `/note` byte-identical and makes migration lazy — existing projects are not touched; content moves to the new directories as new files are written.

## Details

### Edit 1 — destination hook

Add a **destination directory** input: when the caller (or the user's argument) names a target directory, all steps use it — the `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path — scoped to that directory (numbering is per-directory). When unset, default to `.ai-factory/notes/` exactly as now.

### Edit 2 — template hook

Add a **template** input: when the caller supplies a section skeleton, the note body follows it verbatim — `note` contributes the mechanism (mining, distillation, numbering, placement) and does not reshape the caller's structure. When unset, use the current default template (Key Findings / Details / Open Questions). The existing Important Rules (concise, findings-focused, file paths included, English) apply to both cases.

### Edit 3 — frontmatter/description

Update the description to name the genre space: generic distiller for research notes, task specs, and handoffs; destination and template are caller-supplied, defaults unchanged. Keep `user-invocable: true` — standalone `/note` remains valid and unchanged.

### Constraints

- Standalone invocation with no arguments is **byte-identical** to today: same template, same `.ai-factory/notes/` destination, same numbering.
- Load-once discipline unchanged.
- This task does not touch any caller — `roadmap-engine` (note 54) and `command-handoff` (note 55) adopt the hooks in their own tasks.

## What NOT to do

- Do not change the default destination away from `.ai-factory/notes/` — lazy migration depends on the default staying put.
- Do not add genre-specific content (spec rules, handoff skeletons) into `note` — genres are the callers' policy.
- Do not rename the skill.

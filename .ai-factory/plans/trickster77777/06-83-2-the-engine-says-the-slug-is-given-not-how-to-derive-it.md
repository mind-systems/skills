# Plan: 83.2 — the engine says the slug is given, not how to derive it

## Context
`src/skills/roadmap-engine/SKILL.md`, § "Named roadmaps", still states the slug derivation rule in prose in its **Slug derivation** paragraph: the local-part rule, the `john.doe@example.com` → `john-doe` example, and the `user.name` fallback. Every session that loads the engine carries that rule. Since 83.1, the derivation lives in `src/skills/roadmap-engine/scripts/user-slug.sh`, which prints the bare slug. This task replaces the paragraph with the after-text pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0234-the-engine-says-the-slug-is-given-not-how-to-derive-it.md`, § "What must be true after".

Scope boundary: only that one paragraph changes. The section's other paragraphs stay as they are: **Resolution order**, **Owner line** (it verifies the full email, not the slug), **Test sibling** and **Spec destination**. The `SessionStart` hook and its README walkthrough belong to 83.3. Governing-spec docs (`docs/philosophy/multiuser-roadmaps.md`, `docs/reserved-words.md`, `docs/sakshi-harness/sakshi-harness.md`) are not touched. They are docs → roadmap inputs, not this task's file boundary. `docs/reserved-words.md` is also marked final.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The engine paragraph

- [x] **Replace the Slug derivation paragraph with the pinned after-text**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In § "Named roadmaps", replace the whole **Slug derivation** paragraph. It currently spans three wrapped lines, from `**Slug derivation:** the local-part of \`git config user.email\`, lowercased, every` to `` `john-doe`); fallback — slugified `user.name` when email is unset. `` The replacement is the spec's text, verbatim:

  ```
  **Slug derivation:** the user's slug is given at session start, as the line `The user's slug: <user-slug>`; a session that holds no such line runs `scripts/user-slug.sh` and takes its output as the slug.
  ```

  Wrap it at roughly 85 columns, as the neighbouring paragraphs are wrapped. Breaking a line between words is not a wording change, but never break inside a backtick span, and keep `The user's slug: <user-slug>` on one line intact. Keep the blank lines before and after the paragraph. The words must match the spec character for character: the bolded label, the comma after "session start", the semicolon, and `scripts/user-slug.sh` as a path relative to the skill directory, the same way the skill's other relative references are written. Nothing from the old paragraph stays: the local-part rule, the `john.doe@example.com` → `john-doe` example, and the `user.name` fallback all leave the engine. Do not edit any other line of the section.

### Contact check

- [x] **Run the spec's breakage sweep and confirm no pointer breaks** (depends on Replace the Slug derivation paragraph)
  Files: none (read-only)
  From the repo root, run the two greps the spec names:
  `grep -rn "Slug derivation" src docs CLAUDE.md` should return only the engine's rewritten paragraph.
  `grep -rn "slug/owner mechanics" src docs CLAUDE.md` should return the pointers in `roadmap-decompose`, `roadmap-outline`, `roadmap-test-coverage`, `task-rescue`, `temporal-tree` and `command-pin-gaps` to the engine's "Named roadmaps" section. They stay true because the section still holds the resolution order, the owner line and the test sibling. Leave them unedited.
  Also confirm that `grep -n "local-part\|john-doe\|user.name" src/skills/roadmap-engine/SKILL.md` returns nothing, so the derivation text is gone from the engine. Confirm that `src/skills/roadmap-engine/scripts/user-slug.sh` exists, because the new paragraph points at it.

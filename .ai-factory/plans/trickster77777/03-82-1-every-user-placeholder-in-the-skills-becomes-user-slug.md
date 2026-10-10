# Plan: 82.1 — every user placeholder in the skills becomes `<user-slug>`

## Context
The skills write the user's slug as `<slug>`. Their file names use the same placeholder for a title (`<NN>-<slug>.md`, `<seq>-<slug>`), so one name carries two meanings. `docs/paired-loop.md`, the registry's named-roadmap entry in `docs/reserved-words.md` and the `CLAUDE.md` rows already write the user's placeholder as `<user-slug>`. This task renames only the **user** placeholder at the sites the task spec lists (`.ai-factory/specs/trickster77777/0236-every-user-placeholder-in-the-skills-becomes-user-slug.md`, § "What must be true after"). Every title `<slug>` stays as it is: in `<NN>-<slug>.md`, in `<seq>-<slug>`, in the plain `.ai-factory/specs/<NN>-<slug>.md` tag form, in the "`<slug>` lowercase-hyphenated" clause, and in `note`, `aif-plan`, `roadmap-test-coverage`, `command-handoff` and `architect-editor-engine`. Per the spec, `architect-editor-engine` and `agent-architect` have no user placeholder of this kind. The "Slug derivation" paragraph and the example `roadmaps/john-doe.md` in `task-rescue` are not placeholders and stay untouched; 83.2 changes the derivation paragraph. 82.2 owns the targeting hints (`[phase or slug]`, `[phase/slug or task description]`), so they are out of scope.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Placeholder edits

- [x] **`roadmap-engine`: the two-tier text and § "Named roadmaps"**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Make these replacements and leave the rest of each sentence as it is:
  - § "The two-tier artifact", the sentence about scanning `<NN>`: `` `.ai-factory/specs/<slug>/` named — so it never collides; `<slug>` `` becomes `` `.ai-factory/specs/<user-slug>/` named — so it never collides; `<slug>` ``. The trailing `` `<slug>` `` (followed by "lowercase-hyphenated") is the title slug and stays. The `.ai-factory/specs/<NN>-<slug>.md` paths in this paragraph and in the closing `Spec:` tag stay.
  - The same section, the `note` destination sentence: `` `.ai-factory/specs/<slug>/` for a named one `` becomes `` `.ai-factory/specs/<user-slug>/` for a named one ``.
  - § "Named roadmaps", **Resolution order**: `` resolves to `.ai-factory/roadmaps/<slug>.md` `` becomes `` resolves to `.ai-factory/roadmaps/<user-slug>.md` ``.
  - **Test sibling**: `` `.ai-factory/roadmaps/<slug>-tests.md` `` becomes `` `.ai-factory/roadmaps/<user-slug>-tests.md` ``.
  - **Spec destination**: three replacements. `` `.ai-factory/specs/<slug>/`, passed through `` becomes `` `.ai-factory/specs/<user-slug>/`, passed through ``. `` the same `<slug>/` subdirectory `` becomes `` the same `<user-slug>/` subdirectory ``. `` (`.ai-factory/specs/<slug>/<NN>-<slug>.md`) `` becomes `` (`.ai-factory/specs/<user-slug>/<NN>-<slug>.md`) ``; the second `<slug>` is the title slug and stays.
  Do not touch the **Slug derivation** paragraph, the **Owner line** paragraph, the format example's `Spec: .ai-factory/specs/<NN>-<slug>.md` lines, or the prune section's `Spec:` tag mention. Reflowing a hard-wrapped line that a replacement makes longer is fine, but no wording may change.

- [x] **`roadmap-decompose`: hook (c)'s test sibling**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  In the hook (c) sentence ending in `the engine's "Test sibling" rule (...)`, change `` (`.ai-factory/roadmaps/<slug>-tests.md`) `` to `` (`.ai-factory/roadmaps/<user-slug>-tests.md`) ``. Nothing else changes.

- [x] **`roadmap-outline-deep`: destination directory and path form**
  Files: `src/skills/roadmap-outline-deep/SKILL.md`
  - **Destination directory** item: `` `.ai-factory/specs/<slug>/` for a named roadmap `` becomes `` `.ai-factory/specs/<user-slug>/` for a named roadmap ``.
  - **Path form** item: `` `.ai-factory/specs/<slug>/<NN>-<slug>.md` `` becomes `` `.ai-factory/specs/<user-slug>/<NN>-<slug>.md` ``; the second `<slug>` is the title slug and stays.
  Leave `argument-hint` and the targeting text ("a phase or slug") alone, since 82.2 owns them.

- [x] **`orchestrator-artifacts`: the `[routed → <path>]` entry**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In the `[routed → <path>]` marker entry, change `` `.ai-factory/roadmaps/<slug>.md` `` to `` `.ai-factory/roadmaps/<user-slug>.md` ``. The layout lines (`<seq>-<slug>.md`, `<seq>-<slug>.json`, `<seq>-<slug>-plan-review-N.md`, `<seq>-<slug>-review-N.md`, `<seq>-<slug>-test-N.txt`) carry the title slug and stay.

- [x] **`task-rescue`: the test-sibling step**
  Files: `src/skills/task-rescue/SKILL.md`
  In the step that picks `$TARGET_FILE` for test tasks, change `` `.ai-factory/roadmaps/<slug>-tests.md` `` to `` `.ai-factory/roadmaps/<user-slug>-tests.md` ``. The "Identify the task slug" step (`<seq>-<slug>`), the `plans/<seq>-<slug>.json` layout lines and the `roadmaps/john-doe.md` example stay.

### Verification

- [x] **Run the spec's sweep and check the diff scope** (depends on all edits above)
  Files: none (read-only check)
  Run the spec's sweep from the repo root:
  `grep -rn "<slug>/" src`, `grep -rn "roadmaps/<slug>" src`, `grep -rn "<slug>-tests" src`.
  All three must return nothing. Then run `grep -rn "<user-slug>" src` and confirm 12 hits: 7 in `roadmap-engine`, 2 in `roadmap-outline-deep`, and 1 each in `roadmap-decompose`, `orchestrator-artifacts` and `task-rescue`. Run `git diff --stat` and confirm that exactly these five `SKILL.md` files changed. Read `git diff` and confirm two things: every change is a `<slug>` → `<user-slug>` substitution (plus any line reflow), and no title `<slug>` changed.

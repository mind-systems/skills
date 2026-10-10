# 82.1 — every user placeholder in the skills becomes `<user-slug>`

## What is true now

`docs/paired-loop.md`, the registry's named-roadmap entry in `docs/reserved-words.md` and the `CLAUDE.md` rows write the user's placeholder `<user-slug>`. The skills write it `<slug>`, the placeholder their file names use for a title (`<NN>-<slug>.md`, `<seq>-<slug>`, `# Handoff — <slug>`), so one name carries two meanings. The user's `<slug>` stands in these sites:

- `src/skills/roadmap-engine/SKILL.md`, § "The two-tier artifact": "`.ai-factory/specs/<slug>/` named — so it never collides", and "`.ai-factory/specs/<slug>/` for a named one, via `note`'s destination hook".
- The same file, § "Named roadmaps": "resolves to `.ai-factory/roadmaps/<slug>.md`"; the **Test sibling** paragraph, "`.ai-factory/roadmaps/<slug>-tests.md`"; the **Spec destination** paragraph, "`.ai-factory/specs/<slug>/`, passed through `note`'s existing destination hook", "the same `<slug>/` subdirectory" and "(`.ai-factory/specs/<slug>/<NN>-<slug>.md`)", whose second `<slug>` is a file's title.
- `src/skills/roadmap-decompose/SKILL.md`, hook (c): "(`.ai-factory/roadmaps/<slug>-tests.md`)".
- `src/skills/roadmap-outline-deep/SKILL.md`: the **Destination directory** item, "`.ai-factory/specs/<slug>/` for a named roadmap"; the **Path form** item, "`.ai-factory/specs/<slug>/<NN>-<slug>.md`", whose second `<slug>` is a file's title.
- `src/skills/orchestrator-artifacts/SKILL.md`, the `[routed → <path>]` entry: "`.ai-factory/roadmaps/<slug>.md`".
- `src/skills/task-rescue/SKILL.md`, the test-sibling step: "`.ai-factory/roadmaps/<slug>-tests.md`".

`architect-editor-engine` and `agent-architect` carry no user placeholder of this kind today; phase 76 gives them theirs.

## What must be true after

Each site reads, with the rest of its sentence standing:

- `roadmap-engine`, § "The two-tier artifact": "`.ai-factory/specs/<user-slug>/` named — so it never collides; `<slug>` lowercase-hyphenated"; "`.ai-factory/specs/<user-slug>/` for a named one, via `note`'s destination hook".
- `roadmap-engine`, § "Named roadmaps": "resolves to `.ai-factory/roadmaps/<user-slug>.md`"; "`.ai-factory/roadmaps/<user-slug>-tests.md`"; "`.ai-factory/specs/<user-slug>/`, passed through `note`'s existing destination hook"; "the same `<user-slug>/` subdirectory"; "(`.ai-factory/specs/<user-slug>/<NN>-<slug>.md`)".
- `roadmap-decompose`: "(`.ai-factory/roadmaps/<user-slug>-tests.md`)".
- `roadmap-outline-deep`: "`.ai-factory/specs/<user-slug>/` for a named roadmap"; "`.ai-factory/specs/<user-slug>/<NN>-<slug>.md`".
- `orchestrator-artifacts`: "`.ai-factory/roadmaps/<user-slug>.md`".
- `task-rescue`: "`.ai-factory/roadmaps/<user-slug>-tests.md`".

## What breaks on contact

**Rule:** a text breaks on this change if it writes the user's placeholder `<slug>` beside `<user-slug>`.

**Sweep:**
```
grep -rn "<slug>/" src
grep -rn "roadmaps/<slug>" src
grep -rn "<slug>-tests" src
```

**Finding.** The search for `<slug>/` returns the spec-directory sites in `roadmap-outline-deep` and `roadmap-engine`. The search for `roadmaps/<slug>` returns `roadmap-decompose`, `task-rescue`, `orchestrator-artifacts` and the roadmap path and test sibling in `roadmap-engine`. The search for `<slug>-tests` returns `roadmap-decompose`, `task-rescue` and `roadmap-engine`. Every hit is a site listed above, and none comes from `architect-editor-engine` or `agent-architect`.

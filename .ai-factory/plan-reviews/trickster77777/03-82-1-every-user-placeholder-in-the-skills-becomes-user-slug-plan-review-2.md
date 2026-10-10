## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/03-82-1-every-user-placeholder-in-the-skills-becomes-user-slug.md`
**Task:** 82.1 in `.ai-factory/roadmaps/trickster77777.md`. Task spec: `.ai-factory/specs/trickster77777/0236-every-user-placeholder-in-the-skills-becomes-user-slug.md`. Governing spec: `docs/philosophy/multiuser-roadmaps.md`.
**Files targeted:** 5. Each is a `SKILL.md`, in `roadmap-engine`, `roadmap-decompose`, `roadmap-outline-deep`, `orchestrator-artifacts` and `task-rescue`.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The task replaces placeholder text inside skill bodies. It moves no boundary and adds no `loads:` edge.
- **Rules** (`.ai-factory/RULES.md`): WARN. The file isn't there, so there is nothing to check.
- **Skill context** (`.ai-factory/skill-context/aif-review/SKILL.md`): the file isn't there, so no project overrides apply.
- **Roadmap**: OK. 82.1 is the first open task of Phase 82 in the named roadmap. 82.2 (the targeting hints) and 83.2 (the "Slug derivation" paragraph) are neighbouring tasks, and the plan names both as out of scope.
- **Spec tree**: OK. The plan's after-texts match every site in the task spec's § "What must be true after". The Context section now names the same three sources as the task spec's § "What is true now": `docs/paired-loop.md`, the registry's named-roadmap entry and the `CLAUDE.md` rows. That fixes the only issue from plan-review 1.

### Verification against ground truth

I read every targeted line in the current tree (`grep -rn "<slug>" src` plus the surrounding paragraphs):

- **`roadmap-engine`**: the user `<slug>` appears on 7 lines. Two are in § "The two-tier artifact": "`.ai-factory/specs/<slug>/` named — so it never collides; `<slug>`" and "`.ai-factory/specs/<slug>/` for a named one". Five are in § "Named roadmaps": Resolution order, Test sibling, and three in Spec destination. Each before-string the plan quotes sits on a single line verbatim, so each replacement is unambiguous. The excluded occurrences are present and untouched by the plan: the format example's `Spec:` lines, the prune section's tag mention, the `<NN>-<slug>.md` in the two-tier sentence and the closing tag.
- **`roadmap-decompose`** hook (c), **`roadmap-outline-deep`** (Destination directory, Path form), **`orchestrator-artifacts`** (the `[routed → <path>]` entry) and **`task-rescue`** (the test-sibling step): each quoted string matches the file exactly. The `<seq>-<slug>` layout lines, the "Identify the task slug" step, the `roadmaps/john-doe.md` example and the "slug/owner mechanics" prose aren't placeholders of the user, and the plan leaves them alone.
- **Excluded skills**: in `note`, `aif-plan`, `roadmap-test-coverage`, `command-handoff` and `architect-editor-engine`, every `<slug>` is a title slug. The plan correctly leaves them out.
- **Sweep logic**: every sweep pattern requires `<` directly before `slug`, so no `<user-slug>` string can match. For example, `<user-slug>/<NN>-<slug>.md` doesn't match `<slug>/`. The sweep therefore comes back empty only when every site has been converted.
- **Positive count**: `grep -rn "<user-slug>" src` gives 0 hits today. After the edits it gives 12 line hits (7 + 2 + 1 + 1 + 1), with one occurrence on each line. The plan's count is right.
- **Diff scope**: the only uncommitted changes in the working tree are this run's untracked plan, sidecar and review files. `git diff --stat` ignores them, so the five-file check is clean.

### Issues

None.

### Positive Notes

- Every edit is pinned as an exact before → after string under its section name.
- On each line that holds both slugs, the plan says which `<slug>` is the title slug. Those lines are the only places where an implementer could replace too much.
- The plan names its boundaries with 82.2, 83.2 and phase 76, so no work overlaps.
- The verification checks three things: the sweep comes back empty, the positive count is right, and the diff touches only the five files.

## Deferred observations

- Affects: Phase 82 / `docs/philosophy/multiuser-roadmaps.md` — Phase 82 commits to "the user's placeholder is `<user-slug>`" and names `docs/philosophy/multiuser-roadmaps.md` as its governing spec. That spec still writes the user's placeholder as `<имя>`: `.ai-factory/roadmaps/<имя>.md`, `roadmaps/<имя>-tests.md`, `.ai-factory/specs/<имя>/`. Once 82.1 lands, the skills, the registry, `paired-loop` and `CLAUDE.md` will all write `<user-slug>`, and the governing spec will be the only surface with a different form. Under docs → roadmap → code, the governing spec should be the first to carry the placeholder the phase commits to. The fix belongs in `docs/`, outside 82.1's file boundary of five skill bodies. It falls to whoever owns Phase 82's governing spec.

PLAN_REVIEW_PASS

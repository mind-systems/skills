## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/03-82-1-every-user-placeholder-in-the-skills-becomes-user-slug.md`
**Task:** 82.1 in `.ai-factory/roadmaps/trickster77777.md`. Task spec: `.ai-factory/specs/trickster77777/0236-every-user-placeholder-in-the-skills-becomes-user-slug.md`. Governing spec: `docs/philosophy/multiuser-roadmaps.md`.
**Files targeted:** 5 (`roadmap-engine`, `roadmap-decompose`, `roadmap-outline-deep`, `orchestrator-artifacts`, `task-rescue` — each a `SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The task only substitutes placeholder text inside skill bodies. It moves no boundary and adds no `loads:` edge.
- **Rules** (`.ai-factory/RULES.md`): WARN. The file isn't present, so this gate has nothing to check.
- **Skill context** (`.ai-factory/skill-context/aif-review/SKILL.md`): the file isn't present, so no project overrides apply.
- **Roadmap**: OK. Task 82.1 is the open task at the seam of the named roadmap. The plan covers every site that the contract line names.
- **Spec tree**: OK, with one inaccuracy (see Issues). The plan's after-texts match the task spec's § "What must be true after" site by site, word for word.

### Verification against ground truth

I read every targeted line in the current tree:

- **`roadmap-engine`** has the user's `<slug>` on 7 lines: two in § "The two-tier artifact" ("`.ai-factory/specs/<slug>/` named" and "`.ai-factory/specs/<slug>/` for a named one") and five in § "Named roadmaps" (Resolution order, Test sibling, and three in Spec destination). Each quoted before-string in the plan appears verbatim on a single line, so the substitutions are unambiguous.
- **The other four skills**: `roadmap-decompose` hook (c) has 1 site, `roadmap-outline-deep` has 2 (Destination directory, Path form), `orchestrator-artifacts` has 1 (the `[routed → <path>]` entry) and `task-rescue` has 1 (the test-sibling step). All the quoted strings match.
- **Exclusions**: the plan correctly leaves out every title-slug occurrence. These are `<NN>-<slug>.md` everywhere, the `<seq>-<slug>` layout lines in `orchestrator-artifacts` and `task-rescue`, the `# Handoff — <slug>` title in `command-handoff`, `note`, `aif-plan`, `roadmap-test-coverage`, and the snapshot form in `architect-editor-engine`. It also leaves out the "Slug derivation" paragraph (owned by 83.2), the `roadmaps/john-doe.md` example and the targeting hints (owned by 82.2).
- **Sweep logic**: after the edits, `<slug>/`, `roadmaps/<slug>` and `<slug>-tests` cannot match a `<user-slug>` string, because each pattern needs a `<` directly before `slug`. The sweep therefore really does come back empty only if every site was converted. `grep -rn "<user-slug>" src` returns 0 hits today. After the edits it gives exactly 12 line hits (7 + 2 + 1 + 1 + 1), each line holding a single occurrence, so the expected count is right.
- **Diff scope check**: `git diff --stat` covers only tracked files. The plan and its sidecar are untracked, so they won't add noise to the five-file check.

### Issues

1. **The Context section says something false about the governing spec.**
   The plan's Context begins: "The governing spec `docs/philosophy/multiuser-roadmaps.md`, `docs/paired-loop.md`, the registry and the `CLAUDE.md` rows already write the user's placeholder as `<user-slug>`."
   - **Ground truth:** `docs/philosophy/multiuser-roadmaps.md` doesn't contain `<user-slug>` anywhere. It writes the named-roadmap path as `.ai-factory/roadmaps/<имя>.md` and the test sibling as `roadmaps/<имя>-tests.md`.
   - **What the task spec says:** its § "What is true now" names only `docs/paired-loop.md`, the registry's named-roadmap entry in `docs/reserved-words.md` and the `CLAUDE.md` rows. It doesn't name the governing spec.
   - **Impact:** no edit step depends on this sentence. Still, it presents a false claim about the codebase as background, and the implementer or a later reviewer may rely on it.
   - **Fix:** drop "The governing spec `docs/philosophy/multiuser-roadmaps.md`," from that sentence so that it lists the same three sources as the task spec.

### Positive Notes

- Every edit is pinned as an exact before → after string with its enclosing section named, so the implementer has nothing to guess.
- The plan says explicitly which `<slug>` on a mixed line is the title slug (`<user-slug>/<NN>-<slug>.md`, "`<slug>` lowercase-hyphenated"). That is the one place where an implementer could over-replace.
- Scope boundaries with the neighbouring tasks are named (82.2 owns the targeting hints, 83.2 owns "Slug derivation"), so there's no overlap.
- The verification step checks three things: the spec's sweep comes back empty, the positive hit count is right, and no file outside the five changed.

## Deferred observations

- Affects: Phase 82 / `docs/philosophy/multiuser-roadmaps.md` — The phase states "the user's placeholder is `<user-slug>`" and names `docs/philosophy/multiuser-roadmaps.md` as its governing spec. That spec, however, writes the user's placeholder as `<имя>` (`.ai-factory/roadmaps/<имя>.md`, `roadmaps/<имя>-tests.md`). Once 82.1 lands, the skills, the registry, `paired-loop` and `CLAUDE.md` will all write `<user-slug>`, and the governing spec will be the only surface with a different form. Under docs → roadmap → code, the governing spec should be the first to carry the placeholder the phase commits to. The fix lies in `docs/`, outside 82.1's file boundary (five skill bodies). It belongs to whoever owns Phase 82's governing spec.

## Code Review Summary

**Files Reviewed:** 5 (`src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-outline-deep/SKILL.md`, `src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/task-rescue/SKILL.md`). The staged plan, its sidecar and the two plan-reviews are pipeline artifacts, not product changes.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The diff only substitutes placeholder text inside skill bodies. It adds no `loads:` edge and moves no boundary.
- **Rules** (`.ai-factory/RULES.md`): WARN. The file isn't present, so there was nothing to check.
- **Skill context** (`.ai-factory/skill-context/aif-review/SKILL.md`): the file isn't present, so no project overrides apply.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md`): OK. Task 82.1 is the open task at the seam. Every site named in the contract line changed.
- **Spec tree**: OK. Each after-text matches the task spec's § "What must be true after" (`.ai-factory/specs/trickster77777/0236-…`) site by site and word for word.

### Verification

- **`roadmap-engine`, 7 sites.** § "The two-tier artifact": `specs/<user-slug>/` named, with the title clause "`<slug>` lowercase-hyphenated" kept, and `specs/<user-slug>/` for a named one. § "Named roadmaps": Resolution order `roadmaps/<user-slug>.md`; Test sibling `roadmaps/<user-slug>-tests.md`; Spec destination `specs/<user-slug>/`, "the same `<user-slug>/` subdirectory", `specs/<user-slug>/<NN>-<slug>.md`, with the title slug kept. The "Slug derivation" paragraph (owned by 83.2), the Owner line and every `Spec: .ai-factory/specs/<NN>-<slug>.md` tag form are untouched.
- **The other four skills.** `roadmap-decompose` hook (c), `roadmap-outline-deep` (Destination directory, Path form, with the title `<NN>-<slug>.md` kept), `orchestrator-artifacts` (the `[routed → <path>]` entry) and `task-rescue` (the test-sibling step) all match the spec. `roadmap-outline-deep`'s `argument-hint` and targeting text, owned by 82.2, are untouched.
- **The spec's sweep.** `grep -rn "<slug>/\|roadmaps/<slug>\|<slug>-tests" src` returns nothing. `grep -rn "<user-slug>" src` returns 12 lines (7 + 2 + 1 + 1 + 1). `git diff --stat` shows exactly these five `SKILL.md` files under `src/`, 12 lines in total, each a pure `<slug>` → `<user-slug>` substitution.
- **No over-replacement.** The title slug is untouched everywhere it stands: `note`, `aif-plan`, `roadmap-test-coverage`, `command-handoff`, `architect-editor-engine`, the `<seq>-<slug>` layout lines in `orchestrator-artifacts` and `task-rescue`, and the `roadmaps/john-doe.md` example.

### Critical Issues

None.

### Positive Notes

- The edits are minimal and exact. On the two lines that mix the user's placeholder with a file's title (`<user-slug>/<NN>-<slug>.md`), only the user's placeholder changed, so both meanings stay distinct as the phase intends.
- No hard-wrapped line was reflowed, which keeps the diff to one line per site and easy to audit.

## Deferred observations

- Affects: Phase 82 / `docs/philosophy/multiuser-roadmaps.md` — The phase commits to "the user's placeholder is `<user-slug>`" and names `docs/philosophy/multiuser-roadmaps.md` as its governing spec. That spec still writes the user's placeholder as `<имя>`: `.ai-factory/roadmaps/<имя>.md`, `roadmaps/<имя>-tests.md`, `.ai-factory/specs/<имя>/`. With 82.1 landed, the skills, the registry, `paired-loop` and `CLAUDE.md` all write `<user-slug>`, and the governing spec is the only surface with a different form. Under docs → roadmap → code, the governing spec should carry the placeholder the phase commits to. The fix is in `docs/`, outside 82.1's five-skill file boundary, and belongs to whoever owns Phase 82's governing spec.

REVIEW_PASS

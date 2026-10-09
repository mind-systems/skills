## Plan Review Summary

**Plan:** 77.3 — the engine's paragraph says what exact values are and leaves out the measurement
**Files Reviewed:** 1 target (`src/skills/roadmap-engine/SKILL.md`) plus the chain: contract line 77.3 in `.ai-factory/roadmaps/trickster77777.md`, task spec `.ai-factory/specs/trickster77777/0217-a-spec-names-its-sets-and-does-not-measure-the-tree.md`, governing specs `docs/what-a-task-carries.md` and `docs/counts-go-stale.md`, the sweep's reach (`src/commands/command-pin-gaps.md` and the engine's callers)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. The change stays inside the `roadmap-engine` engine's own format paragraph. `.ai-factory/ARCHITECTURE.md` does not restate the paragraph or the phrase "exact values", so no boundary concern.
- **Rules** — WARN (non-blocking): `.ai-factory/RULES.md` is absent, as is `.ai-factory/skill-context/aif-review/SKILL.md`; nothing to check against.
- **Roadmap** — OK. The plan heading matches the open line 77.3 in `.ai-factory/roadmaps/trickster77777.md`, Phase 77, at the `[x]`/`[ ]` seam directly after 77.2 `[x]`. The phase's governing specs are `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`. The task spec's "What is true now" claim that no open task above this one edits the engine is correct, because 77.2 is the only task above it in the phase and it is closed.

### Verification against ground truth

- **Current paragraph.** `src/skills/roadmap-engine/SKILL.md`, the bold lead-in `**What a task spec holds:**`, matches the spec's § "What is true now" quote word for word. The layout matches the plan's description: `Nothing else means, concretely:` starts on its own line right after `pinned rather than hedged.` with no blank line between them, and a blank line separates the paragraph from `**Never write a full spec inline in the roadmap**`. The prose is hard-wrapped at the surrounding width.
- **Target text.** The plan sends the implementer to copy the spec's § "What must be true after" verbatim. Its three orientation bullets were checked against that text and are accurate:
  - the inserted value clause ("— the code's own values, a literal, a symbol, a type, a path —");
  - implementer → planner;
  - the measurement clause, which goes before the existing "and" that opens the fence clause.
- **Agreement with the governing doc.** `docs/what-a-task-carries.md` § "What a spec holds" already carries "with exact values — the code's own values, a literal, a symbol, a type, a path — so the planner does not re-derive it" and "A measurement of the tree is not held either: a count is false before the task is reached". The pinned engine text agrees with it.
- **Blast radius.** Both sweep commands were run now and their reach matches what the spec found. The first search reaches only the engine's callers, all of which use it for format and flow. The second search reaches only:
  - the engine paragraph itself;
  - `src/commands/command-pin-gaps.md`, which points to the paragraph by name with "not restated here", so it stays;
  - `docs/what-a-task-carries.md`, which already agrees.

  The plan's instruction to stop and report any match outside this set, rather than edit it, is the right handling.
- **Scope.** The plan changes one paragraph and nothing else, which matches "Nothing else in the file changes". No docs or test steps are needed: the target is a skill body, and its governing doc was already updated by 77.2.

### Critical Issues

None.

### Positive Notes

- The plan treats the spec's verbatim text as the authority and labels its own bullets "for orientation only". This keeps a paraphrase from drifting away from the pinned wording.
- The plan spells out the layout rules that matter: hard-wrap width, the line break with no blank line before `Nothing else means`, and the blank lines around the paragraph. These are the details most likely to be lost when replacing a hard-wrapped paragraph.
- The blast-radius step runs the spec's own searches and gives a stop-and-report rule rather than permission to edit outside the boundary.

PLAN_REVIEW_PASS

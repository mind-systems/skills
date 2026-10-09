## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-engine/SKILL.md`). The other staged files are the orchestrator's own plan, plan JSON and plan-review artifacts, and were not reviewed as product.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture:** OK. The edit stays inside the `roadmap-engine` engine's own format paragraph. No module boundary or `loads:` edge changes.
- **Rules:** WARN (non-blocking). `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` are both absent, so there was nothing to check against.
- **Roadmap:** OK. Task 77.3 in `.ai-factory/roadmaps/trickster77777.md`, Phase 77, sits at the seam directly after 77.2 `[x]`. Its governing specs are `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`. The task spec is `.ai-factory/specs/trickster77777/0217-a-spec-names-its-sets-and-does-not-measure-the-tree.md`.

### Verification against the spec

- **Pinned text.** I took the paragraph from `**What a task spec holds:**` through `standing in for it.`, collapsed its whitespace, and compared it with the paragraph pinned in the spec's § "What must be true after". The two are identical, including every em dash, the italics on the three parts, and the order of the clauses. The new measurement clause comes before the existing "and" that opens the fence clause.
- **Layout.**
  - The prose is hard-wrapped at the surrounding width. The longest new line, `reached; and no clause fences off a neighbour by name — scope is stated positively, as`, matches the existing line it replaced.
  - `Nothing else means, concretely:` still starts on its own line directly after `pinned rather than hedged.`.
  - The blank lines before the paragraph and before `**Never write a full spec inline in the roadmap**` are kept.
- **Scope.** The diff touches only this paragraph. The frontmatter and other sections are unchanged, as the spec's "Nothing else in the file changes" requires.
- **Agreement with the governing doc.** The wording matches `docs/what-a-task-carries.md` § "What a spec holds": "the code's own values, a literal, a symbol, a type, a path — so the planner does not re-derive it" and "a count is false before the task is reached".
- **Blast radius.** I re-ran the spec's sweep against the current tree.
  - "What a task spec holds|exact values|Nothing else means" reaches only three places: the engine paragraph, `src/commands/command-pin-gaps.md` (which points to it by name, "not restated here"), and `docs/what-a-task-carries.md`, which already agrees.
  - An extra search for "re-derive" turns up no other place that names the implementer as the spec's reader.

### Critical Issues

None.

### Positive Notes

- The edit is a minimal, byte-faithful application of the pinned text, and it keeps the file's hard-wrap convention, so the diff reads clearly.
- The engine and its governing doc now say the same thing in their own voices, so the counts rule reaches spec writers through the paragraph they actually load.

REVIEW_PASS

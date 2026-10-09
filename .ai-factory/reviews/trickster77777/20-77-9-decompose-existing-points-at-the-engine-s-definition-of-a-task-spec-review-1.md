## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-decompose/SKILL.md`; the plan, its sidecar and the plan-review are orchestrator artifacts and were read for intent only)
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** OK. Task 77.9 is the first open line in `.ai-factory/roadmaps/trickster77777.md` under Phase 77. Every task above it is `[x]`, and none of them edits this file.
- **Spec:** OK. The new text under `### (d) Extra update action — "Decompose existing"` matches the sentence pinned in the task spec's § "What must be true after" (`.ai-factory/specs/trickster77777/0225-…`) word for word and wraps at the same point. The parenthesis is gone. No other line in the file changed, which is what the spec requires ("Nothing else in the file changes").
- **Architecture / Rules:** OK. The frontmatter already declares `loads: roadmap-engine`, so the new reference follows an edge that already exists. It cites the engine's bold lead-in `**What a task spec holds:**` by name, as `docs/reference-by-name.md` requires. That paragraph exists in `src/skills/roadmap-engine/SKILL.md`. The skill already refers to `roadmap-engine`'s rules elsewhere in the same form, for example "the engine's "Test sibling" rule", so the new sentence matches the file's style.
- **Governing specs** (`docs/counts-go-stale.md`, `docs/what-a-task-carries.md`): aligned. The skill no longer lists a spec's contents in its own words, so "what exists today" and "guards" have no second home. The engine's paragraph is now the only home for what a task spec holds.

### Verification
- I re-ran the spec's sweep (`grep -rn "exists today\|expand a vague task\|Decompose existing" src docs CLAUDE.md --include="*.md"`). It matches only the preamble-reading paragraph that names hook (d), the hook (d) heading, and the new sentence. "exists today" no longer matches anything. That is exactly the result the spec predicts.
- I read the whole file. Nothing else in it depended on the removed parenthesis. The task-spec-handling rule below the sentence still refers to `roadmap-engine`'s format and sub-numbering rule on its own.

### Critical Issues
None.

### Positive Notes
- The edit is minimal and copies the pinned text exactly, including the backticks and the straight quotes around the paragraph name.
- The fix removes duplicated content by linking to its one home, rather than updating the second copy.

## Deferred observations
- Affects: unknown — The skill's own `description:` field says each contract line names "the key files, types, and guards", and `roadmap-engine`'s contract-line template still reads "key files/types/guards involved". These are contract-line wording, not a task spec's contents. The task spec says nothing else in this file changes, and the engine's template is a file this task does not touch. Whether "guards" on the contract line also counts as the neighbour-fencing the engine's "What a task spec holds" refuses is a planning question for a later task, not something this diff introduced. [dismissed]

REVIEW_PASS

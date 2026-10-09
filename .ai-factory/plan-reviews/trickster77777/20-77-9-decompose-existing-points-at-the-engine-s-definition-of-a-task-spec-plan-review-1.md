## Plan Review Summary

**Plan:** 77.9 — "Decompose existing" points at the engine's definition of a task spec
**Files targeted:** 1 (`src/skills/roadmap-decompose/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** OK. The task is the first open line in the named roadmap `.ai-factory/roadmaps/trickster77777.md`, under Phase 77, which names `docs/counts-go-stale.md` and `docs/what-a-task-carries.md` as its governing specs. Every line above it in the phase is `[x]`, so no open task above it touches the target file. That matches both the spec's claim and the plan's.
- **Spec:** OK. The task spec `.ai-factory/specs/trickster77777/0225-decompose-existing-points-at-the-engines-definition-of-a-task-spec.md` pins the replacement sentence word for word. The plan reproduces it exactly, keeps the same line wrap, and names the spec's § "What must be true after" as the authority if the two ever disagree.
- **Architecture / Rules:** OK. The skill already declares `loads: roadmap-engine`, so the new reference follows an edge the skill already has, and no frontmatter change is needed. The reference points at a bold lead-in by its name (`**What a task spec holds:**` in `roadmap-engine/SKILL.md`), not at a position, so it holds to `docs/reference-by-name.md`.

### Ground-truth verification
- The current text under `### (d) Extra update action — "Decompose existing"` is word for word the two-line sentence the plan quotes, parenthesis included.
- The `active/skills/roadmap-decompose` symlink resolves into `src/`, so editing only the `src/` file is correct.
- I ran the sweep at review time. It returned exactly the matches the spec predicts: the preamble paragraph that names hook (d)'s "Decompose existing", the hook (d) heading, and the two lines of the target sentence. Nothing in `docs/` or `CLAUDE.md` restates the parenthesis. The plan's expected matches after the change are therefore right: "exists today" will no longer match, while "expand a vague task", the heading, and the preamble paragraph will still match.
- The plan explicitly protects everything the edit could disturb: the blank line, the "Task-spec-handling rule:" list, and the preamble paragraph.

### Critical Issues
None.

### Positive Notes
- The plan is narrow and stays inside the task's file boundary. It sets the spec above itself as the authority, so any disagreement resolves to the spec.
- The blast-radius step only reports what it finds and edits nothing, so the task does not expand into neighbouring files.
- The plan points at the target by its heading text, never by a line number.

PLAN_REVIEW_PASS

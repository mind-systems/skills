## Plan Review Summary

**Plan:** 77.6 — a task's now is the code after every open task above it
**Files targeted:** 1 (`src/skills/agent-architect/templates/buffer-seed.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap gate — OK.** The plan's heading matches the open task 77.6 in `.ai-factory/roadmaps/trickster77777.md`, Phase 77. I read the task's `Spec:` note (`.ai-factory/specs/trickster77777/0222-…md`) and checked the phase's governing specs, `docs/counts-go-stale.md` and `docs/what-a-task-carries.md`. `docs/what-a-task-carries.md` § "What a spec holds" already says what is true now is "read from the code as every open task above it leaves it", so the new entry repeats the doc's meaning and does not contradict it.
- **Architecture gate — OK.** The change is a template inside one skill. `active/skills/agent-architect` is a symlink to `../../src/skills/agent-architect` (verified), so editing only the `src/` file is correct.
- **Rules gate — WARN (non-blocking).** `.ai-factory/RULES.md` does not exist, so I had no explicit convention file to check against. The project's `.ai-factory/skill-context/aif-review/SKILL.md` does not exist either.

### Verification against ground truth

- **The seed matches the spec's "What is true now".** Under `## Method`, the counts entry already holds 77.5's work-order sentence. Next comes "**Standing entry — what a spec holds.**", which ends "…scope is / what the task changes.", then a blank line, then "**Standing entry — state the behaviour and stop.**". The plan places the insertion between these two entries, as the spec does.
- **The paragraph to insert matches the spec's § "What must be true after" exactly**: the same words, the same line breaks, straight quotes, a literal em dash. Each wrapped line stays within about 76 columns, like the entries around it.
- **Rehydration needs no extra change.** The seed's opening paragraph matches an entry by the lead-in "Standing entry —". `agent-architect/SKILL.md` § "Spawn once, message thereafter" matches an entry "by its bold lead-in" and "add[s] any entry the buffer lacks". So existing buffers take the new entry at their next rehydration, and the plan is right to leave `.ai-factory/architects/` alone.
- **No open task above 77.6 touches the file.** No `[ ]` line comes before 77.6 in the named roadmap. The next open task, 77.9, edits `roadmap-decompose`, not the seed.
- **The sweep finds what the plan says it will.** I ran both searches now:
  - `grep "Standing entry"` finds only the seed: its opening paragraph and its standing entries.
  - `grep "exact values\|read from the code"` finds `src/skills/roadmap-engine/SKILL.md` ("…from the code with exact values…") and `docs/what-a-task-carries.md` § "What a spec holds", and nothing else.
  - Neither search finds a text that states a task's now as the tree on the day of writing.
- **The task stays in scope.** The plan edits nothing outside the seed, adds no tests and no docs, and its only check step is a read-only sweep. That fits a one-paragraph addition to a template.

### Critical Issues

None.

### Positive Notes

- The plan copies the pinned text verbatim and names the spec as the authority if the two ever disagree.
- It places the insertion by bold lead-in, never by line number, so the placement survives other edits to the file.
- The blast-radius step reports anything it finds and does not edit it, which keeps the engine and the doc out of this task's scope.

PLAN_REVIEW_PASS

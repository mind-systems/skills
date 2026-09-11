## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/43-39-1-the-name-is-chosen-after-the-research-not-before-it.md`
**Files targeted:** 1 (`src/skills/roadmap-test-coverage/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present. The change stays inside one skill body, touches no `loads:` edge and no engine; `roadmap-test-coverage` remains a lens over `test-philosophy` / `roadmap-engine`. No boundary issue. OK.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (optional file missing; nothing to check against).
- **Roadmap** — Plan heading matches `.ai-factory/roadmaps/trickster77777.md` Phase 39, task 39.1. Chain walked: contract line → `Spec: .ai-factory/specs/trickster77777/127-the-name-is-chosen-after-the-research.md` → `Governing spec: docs/test-coverage-pass.md` § "A number is fixed before research; a name is not" → leaf `src/skills/roadmap-test-coverage/SKILL.md` Layer 4. All resolve. OK.
- **Settings** — `Docs: no` is correct: the governing spec already states the intended behavior (doc ahead of code, doing its job); this task brings the code up to it, not the other way round. `Testing: no` is correct for a skill body (no runnable surface). OK.

### Grounding verified against the leaf

Every factual claim in the plan checks out against the file as it stands after 38.2:

- The three template sites are exactly where the plan says: `Note to write: .ai-factory/specs/<NN>-<slug>.md` (header), `Write the following document to .ai-factory/specs/<NN>-<slug>.md:` (write instruction), `saved: .ai-factory/specs/<NN>-<slug>.md` (return line) — all inside the Layer 4 "Agent prompt template" code block.
- `grep -n "<NN>-<slug>"` returns exactly seven hits: the three above plus the Layer 6 refactor pointer, the Layer 8 "Notes written" line, and the two Layer 8 handoff-block pointers — matching the plan's boundary-check enumeration ("Layer 6 pointer, Layer 8 'Notes written' line, two Layer 8 handoff-block pointers"). Per the task spec those four need no edit. Correct.
- The `$NEXT_NOTE_NUM` computation block sits above the template and is not named in any task. Correct.
- The slug shape the plan cites ("lowercase, hyphens") is what `note` § "Step 2: Determine Slug" derives. Correct.
- Body is 437 lines; the edit adds a handful of lines. ≤ 500 holds.
- `Collect all one-line confirmations.` after the code block already consumes the `saved:` line, so once that line carries the real path, the orchestrator holds the only copy of the real name — the plan's reasoning for leaving Layers 6/8 alone is sound.
- The task spec's "easy to get backwards" point (agent holds the pen; caller never applies a name afterward) is carried into task 2 explicitly. Good.

### Findings

**Minor — the header-line form is left to the implementer, and one of the two offered forms sits closer to the wording the task spec rules out.**
Task 1 says: `Note number: <NN>` plus `Note directory: .ai-factory/specs/` *or* one line `Note to write: .ai-factory/specs/<NN>-<slug you choose after research>.md` — "pick one form". The task spec is more specific than either/or: "The prompt hands the agent the number alone for its destination, not a finished path". The first form (number + directory) is that sentence literally; the second still hands a path template with the slug slot inline, which an implementer could reasonably read as "a finished path with a hole in it", and a reviewer could then reasonably call a deviation. Both forms satisfy the invariant the plan states (no slug value carried in), so this is not a correctness risk — but a plan should not leave a spec-adjacent wording choice open when the spec text already prefers one. Pin the first form (number line + directory line, or a single line that names only the number and the directory) and drop the alternative.

No missing steps, no wrong assumptions about the file, no path or API errors, no security or migration surface.

### Positive Notes

- The plan re-grounded against the post-38.2 file rather than the state the task was decomposed from, and says so — exactly the discipline the task spec's "Blast radius" asks for.
- Task ordering (header → write instruction → return line → boundary grep) mirrors the order the sentences appear in and makes the final grep a real check, not a formality.
- The plan quotes the return-line example (`0042-actual-slug.md`) in a four-digit form consistent with the bound 38.2 landed — small, but it keeps the two tasks coherent inside one code block.

## Deferred observations

- Affects: `roadmap-test-coverage` (a later phase, outside 39.1's three-sentence boundary) — Once the slug is chosen after research, the note's own H1 `# <Area Name> — Test Plan` and the Layer 8 `(<area name>)` annotation still carry the `Area:` label handed in at spawn. A note whose slug says what the area turned out to be, under a title that says what it was called before research, is a small internal contradiction the governing spec's "name late enough to still be true" reasoning would also apply to. The task spec pins this task to the three template sentences, so it is correctly not in this plan; whoever next touches the template should decide whether the title follows the slug.
- Affects: unknown — The Layer 4 template is spawned as an `Explore` agent, which in at least one harness definition is read-only (no `Write`/`Edit`, though `Bash` remains). The template has always asked that agent to write a file, so this is pre-existing and untouched by 39.1; noting it because 39.1 makes the agent the sole holder of the pen, which raises the cost if the agent type cannot in fact write.

## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/43-39-1-the-name-is-chosen-after-the-research-not-before-it.md`
**Files targeted:** 1 (`src/skills/roadmap-test-coverage/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present. The change stays inside one skill body; the skill's `loads: test-philosophy roadmap-engine` edge is untouched and no engine is edited. OK.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (optional file missing; nothing to check against).
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent. WARN (no project-level overrides to apply).
- **Roadmap** — Plan heading matches `.ai-factory/roadmaps/trickster77777.md` Phase 39, task 39.1. Chain walked fresh: contract line → `Spec: .ai-factory/specs/trickster77777/127-the-name-is-chosen-after-the-research.md` → `Governing spec: docs/test-coverage-pass.md` § "A number is fixed before research; a name is not" → leaf `src/skills/roadmap-test-coverage/SKILL.md` Layer 4. All resolve. OK.
- **Settings** — `Docs: no` correct (the governing spec is already ahead of the code and this task brings the code up to it). `Testing: no` correct for a skill body. OK.

### Resolution of the review-1 finding

Review-1's only finding was that task 1 offered two header-line forms and left the choice to the implementer, with one form ("`Note to write: .ai-factory/specs/<NN>-<slug you choose after research>.md`") still reading as a finished path with a hole in it. The revised plan drops the alternative and pins the form the task spec's sentence names literally — `Note number: <NN>` plus `Note directory: .ai-factory/specs/` — and states the invariant alongside it ("no path template and no slug value is carried in from the spawn prompt"). Resolved.

### Grounding verified against the leaf (re-read fresh)

- The three template sites are exactly where the plan places them inside the Layer 4 "Agent prompt template" code block: the `Note to write:` header line, the `Write the following document to .ai-factory/specs/<NN>-<slug>.md:` instruction, and the closing pair `After writing the file, return exactly one line:` / `saved: .ai-factory/specs/<NN>-<slug>.md`.
- `grep -n "<NN>-<slug>"` returns seven hits today: the three above plus the Layer 6 refactor pointer, the Layer 8 "Notes written" line, and the two Layer 8 handoff-block pointers — matching the plan's boundary-check enumeration. Per the task spec those four need no edit.
- `Note directory: .ai-factory/specs/` is consistent with the file as it stands: the `$NEXT_NOTE_NUM` scan is explicitly scoped to the flat `.ai-factory/specs/` directory, so the directory the plan hands the agent is the one the number was computed against. No mismatch between where the number is scanned and where the file lands.
- The `$NEXT_NOTE_NUM` computation block (four-digit width, `9999` bound, computed once before the parallel launch) sits above the template and is named in no editing task. Correct.
- The slug shape the plan cites ("short, lowercase, hyphenated") is what `note` § "Step 2: Determine Slug" derives ("lowercase, hyphens"). Correct.
- `Collect all one-line confirmations.` follows the code block and is the only consumer of the `saved:` line; once that line carries the real path, the orchestrator holds the only copy of the real name — so leaving Layers 6/8 on the bare placeholder is sound, exactly as the task spec's "Blast radius" states.
- Task 2 carries the task spec's "easy to get backwards" point into the prompt wording explicitly (the agent holds the pen; the caller never applies a name afterward). Correct.
- Body is 437 lines; the edit adds a few lines. ≤ 500 holds. Frontmatter untouched.

One note on the boundary-check task, not a finding: after the edit the write instruction still contains the `<NN>-<slug>` substring (as `<Note directory>/<NN>-<slug>.md`), so the post-edit grep returns five hits, not four — the four out-of-scope sites plus the reworded write instruction. The task's wording ("the Layer 6 pointer, the Layer 8 'Notes written' line, and the two Layer 8 handoff-block pointers still carry the bare placeholder unchanged") is about those four being unchanged, which the grep does verify; the implementer should not read the extra hit as a leak.

### Findings

None. No missing steps, no wrong assumptions about the file, no path or API errors, no security or migration surface.

### Positive Notes

- The plan re-grounded against the post-38.2 file and says so — the discipline the task spec's "Blast radius" asks for.
- Task ordering (header → write instruction → return line → boundary grep) mirrors the order of the sentences in the template, and the final grep is a real check.
- The return-line example (`0042-actual-slug.md`) keeps the four-digit width 38.2 landed, so the one code block stays internally coherent.

## Deferred observations

- Affects: `roadmap-test-coverage` (a later phase, outside 39.1's three-sentence boundary) — Once the slug is chosen after research, the note's own H1 `# <Area Name> — Test Plan` and the Layer 8 `(<area name>)` annotation still carry the `Area:` label handed in at spawn. A note whose slug says what the area turned out to be, under a title that says what it was called before research, is a small internal contradiction the governing spec's "name late enough to still be true" reasoning would also apply to. The task spec pins this task to the three template sentences, so it is correctly not in this plan; whoever next touches the template should decide whether the title follows the slug.
- Affects: unknown — The Layer 4 template is spawned as an `Explore` agent, which in at least one harness definition is read-only (no `Write`/`Edit`, though `Bash` remains). The template has always asked that agent to write a file, so this is pre-existing and untouched by 39.1; noting it because 39.1 makes the agent the sole holder of the pen, which raises the cost if the agent type cannot in fact write.

PLAN_REVIEW_PASS

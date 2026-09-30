## Plan Review Summary

**Plan:** 65.4 — the gap pass stops suggesting a line or a count
**Files Reviewed:** 1 target (`src/commands/command-pin-gaps.md`) plus the task spec, phase note, and the sweep's hit set
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** OK. The plan matches the open `[ ]` contract line 65.4 in `.ai-factory/roadmaps/trickster77777.md`, which sits right at the seam after 65.1–65.3 `[x]`. Its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/183-the-walk-lands-on-a-file-and-a-named-thing.md`, and the plan follows it.
- **Governing spec / phase note:** OK. Phase 65 names `docs/counts-go-stale.md`, `docs/reference-by-name.md` and `docs/what-a-task-carries.md`. The phase note (`179-the-skills-still-ask-for-a-line-and-a-measurement.md`) says "Nothing under `docs/` is written", and the plan's decision to leave all docs alone matches that.
- **Architecture:** OK. The edit is a text change inside one command body. It does not touch frontmatter, `loads:` or the skill graph.
- **Rules:** WARN (non-blocking). There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`, so no project-specific rules applied.

### Verification against the codebase
- **Walk sentence:** I checked the source span with an exact fixed-string match. It appears once in `src/commands/command-pin-gaps.md`, inside the paragraph that opens "The unit of the walk is one behavior the task claims." The plan's replacement matches the spec's pinned sentence word for word.
- **Meaning holes clause:** "citing the code that grounds it where a concrete source exists" appears once. The replacement matches the spec, and the plan's full reconstructed sentence reads correctly.
- **Blast-radius holes sentence:** the full source sentence appears once. The replacement "report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`." matches the spec.
- **Single physical line:** each target paragraph really is one line of the file, so the plan's instruction to replace in place without adding line breaks is correct.
- **Things kept as they are:** the plan leaves the Value holes paragraph, the scan-mode line `[file:line|spec-location]` and the default report line `N closed from source · M blocking · K owned elsewhere` untouched. The spec's finding classes all three as correct already or as chat output, and the plan agrees.
- **Sweep, run now:**
  - `file:line` hits the walk sentence (the target), the scan line, `src/global/CLAUDE.md` § "Grounding claims", `docs/counts-go-stale.md`, `docs/reference-by-name.md` and the `CLAUDE.md` index row. The `roadmap-outline-deep` and `roadmap-prune` hits are gone because 65.1 and 65.3 already landed. This is exactly the plan's expected list.
  - `command-pin-gaps` hits only docs and the `CLAUDE.md` index, as the plan expects. In `docs/sakshi-harness/skill-cycle.md`, the pins chapter describes value-hole sources as "a file and the thing in it, not a line number", and its report sentence counts the run's outcomes. It says nothing about a landing, a grounding citation or a large-sweep count, so it does not meet the spec's Rule.
  - `and its count` and `citing the code` each hit only the target sentences, so once the change is applied they will return nothing, as the plan expects.

### Critical Issues
None.

### Positive Notes
- The plan quotes every source span and every replacement word for word and ties each one to the spec's pins, which leaves no room to paraphrase pinned contract text.
- The read-only sweep uses the spec's **Rule** as its only stop condition, so a mismatch in the hit list alone does not stop the run. It makes no edits outside the target.
- Its "Leave the rest untouched" list fences exactly the neighbours the spec's finding treats as correct already.

PLAN_REVIEW_PASS

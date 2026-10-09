## Plan Review Summary

**Plan:** 42.1 — the always-loaded rule separates a number assigned once from a heading's ordinal
**Files Reviewed:** plan, task spec `0197-…`, named roadmap `trickster77777.md` (Phase 42), `src/global/CLAUDE.md`, `docs/reference-by-name.md` § "Granularity, not size", project `CLAUDE.md`, `src/skills/agent-architect/SKILL.md`, the symlink chain `~/.claude/CLAUDE.md` → `active/CLAUDE.md` → `src/global/CLAUDE.md`
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** OK. The plan heading matches contract line 42.1 in `.ai-factory/roadmaps/trickster77777.md`. That line is the first unchecked one and sits right after the phase header. Its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0197-the-always-loaded-rule-separates-a-number-from-a-heading-ordinal.md`. The phase's `Governing spec: docs/reference-by-name.md` already states the distinction in § "Granularity, not size". The new sentence brings the always-loaded rule into line with that governing spec.
- **Architecture:** OK. A one-sentence prose edit in the global discipline file crosses no module boundary.
- **Rules:** WARN (non-blocking). There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.

### Verification of the plan against ground truth
- **Old text matches.** The exact text the plan replaces appears once in `src/global/CLAUDE.md`, in the paragraph that opens "A reference addresses by **name**, never by position."
- **New text matches.** The replacement text in the plan is identical to the sentence pinned in the task spec § "What must be true after", checked by substring comparison.
- **Wrapping deviation is correct.** The spec says the text "wraps in the file at a fixed column". In fact the whole paragraph is one physical line (line length 560). Keeping it on one line is right.
- **Project `CLAUDE.md` row deviation is correct.** The spec's finding quotes the `docs/reference-by-name.md` row as listing "a numbered item". The current row reads "a heading, a bold lead-in, a number assigned once — anything that will be depended on". `grep "numbered item"` over `src/ docs/ CLAUDE.md` matches only the global sentence. No edit is needed.
- **`agent-architect` anchor list is correctly left alone.** It reads "a bolded rule, a symbol, a unique string — never a position". It is the only hit for "unique string" and agrees with the new sentence.
- **Symlinks are handled correctly.** Both `~/.claude/CLAUDE.md` and `active/CLAUDE.md` are symlinks that resolve to `src/global/CLAUDE.md`. Editing only the source is right.
- **Sweep expectations hold after the edit.** The new sentence drops "numbered item", so the first grep returns nothing. The second returns only the new sentence. The third returns only `agent-architect`.
- **No hits outside the sweep scope.** A wider search across the grove root found nothing that needs the edit. The one other "numbered item" hit is in `upstream/ai-factory/aif-improve/references/VALIDATOR.md`. It is unrelated wording in the pristine mirror, which is never hand-edited.

### Critical Issues
None.

### Positive Notes
- Both deviations from the spec are checked against the files and stated with their evidence, not copied over from the spec.
- The scope is tight: one sentence. The plan names the text before and after it that stays untouched, and it treats any wider finding as stop-and-report.
- The em dash and the backticks around `N.M` are called out explicitly. This matters for a byte-for-byte pin in a file every session loads.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/0197-the-always-loaded-rule-separates-a-number-from-a-heading-ordinal.md` — The task spec's § "What is true now" claims the text "wraps in the file at a fixed column". Its § "What breaks on contact" finding says the project `CLAUDE.md` row still lists "a numbered item". Both claims are stale against the files. The plan correctly follows the files. The spec text itself sits outside this task's file boundary (`src/global/CLAUDE.md`). It is the planner's to correct if the spec is kept for future readers. [dismissed]

PLAN_REVIEW_PASS

## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-engine/SKILL.md`). The other staged files are pipeline artifacts: the plan, its sidecar, and the plan-review.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. The change adds one sentence to the body of an engine skill. The frontmatter, `loads: note`, and the reverse-graph marker are unchanged. The added sentence narrows what a task spec may contain and gives callers no new obligation.
- **Rules:** WARN, non-blocking. `.ai-factory/RULES.md` does not exist, and `.ai-factory/skill-context/aif-review/SKILL.md` does not exist either.
- **Roadmap:** OK. The work matches contract line 61.2 in `.ai-factory/roadmaps/trickster77777.md`, which sits at the seam. It is also consistent with Phase 61's governing spec `docs/what-a-task-carries.md` (§ "What a spec holds", § "Scope, stated positively") and with task spec `170-the-three-parts-are-the-whole-and-none-is-a-check-or-a-line.md`.

### Verification against the task spec
- **Wording:** I collapsed whitespace in the full **What a task spec holds** paragraph and compared it with the paragraph the spec pins in § "What must be true after", with the `> ` prefixes stripped. The two are identical: 702 characters, every word, em-dash, and semicolon.
- **Placement:** the sentence is appended inside the paragraph, with no blank line before it. The paragraph still ends before the blank line and the **Never write a full spec inline in the roadmap** paragraph.
- **Preserved text:** `git diff HEAD` on the file shows only 5 added lines and no removed or changed ones. The bold heading `**What a task spec holds:**`, the three original clauses and their line breaks, the **Why two tiers** paragraph, the following paragraph, and the frontmatter are all byte-identical.
- **Form:** the new lines are 85, 78, 84, 81, and 65 characters long. That fits the paragraph's existing hard wrap of 85 characters at most. Every break falls between words.
- **Blast radius:** `src/commands/command-pin-gaps.md` cites the paragraph only by its heading name, and that name still resolves. The file is unmodified. No other live file quotes the paragraph's body.

### Critical Issues
None.

### Positive Notes
- The edit is minimal and follows the file's own wrapping instead of copying the spec's blockquote layout, as the plan's stated assumption said it would.
- The implementation adds no stray checks, comments, or references to the plan layer.

REVIEW_PASS

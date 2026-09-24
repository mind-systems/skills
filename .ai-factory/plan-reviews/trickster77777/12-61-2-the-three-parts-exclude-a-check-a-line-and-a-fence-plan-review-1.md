## Plan Review Summary

**Files Reviewed:** 1 plan, the task spec (`.ai-factory/specs/trickster77777/170-the-three-parts-are-the-whole-and-none-is-a-check-or-a-line.md`), the governing spec (`docs/what-a-task-carries.md`), the target `src/skills/roadmap-engine/SKILL.md`, and the citing `src/commands/command-pin-gaps.md`
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** no boundary concern. The edit adds one sentence to an engine's body and does not change its `loads:`, its frontmatter, or its reverse-graph marker. Callers reach the paragraph for the task-spec shape. The added sentence narrows what a spec may hold and adds no new obligation that a caller has to satisfy.
- **Rules:** `.ai-factory/RULES.md` is absent (WARN, non-blocking). No project skill-context file for review exists.
- **Roadmap:** aligned. `.ai-factory/roadmaps/trickster77777.md` Phase 61 names `docs/what-a-task-carries.md` as its governing spec. The contract line for 61.2 sits at the seam, right after 61.1 `[x]`. The plan's title matches it, and the plan follows its `Spec:` tag.

### Verification against ground truth
- **Target paragraph:** `SKILL.md` has the **What a task spec holds** paragraph exactly as the plan describes it. It has four hard-wrapped lines ending with `*what breaks on contact*, pinned rather than hedged.`, then a blank line, then the **Never write a full spec inline in the roadmap** paragraph. The plan's anchor is correct.
- **Sentence text:** the sentence in the plan's code block is byte-identical to the one pinned in the spec's § "What must be true after" (checked programmatically: 397 characters, exact match).
- **Wrapping:** reflowing the new sentence to the file's ~85-character wrap, instead of copying the spec's single blockquote line, keeps the file's own form. It changes no words or punctuation, so the result conforms to the spec.
- **Blast radius:** the spec's sweep (`grep -rln "What a task spec holds" src/ docs/`) finds only the target paragraph and `command-pin-gaps.md`, which cites the paragraph by its heading name alone. The plan keeps the bold heading byte-identical, so that citation still resolves.
- **Consistency with the governing spec:** the sentence's three exclusions match the governing spec. § "What a spec holds" says none of the parts is a check. § "Scope, stated positively" says scope is stated positively with no fences. The ban on file positions follows the global rule that a reference addresses by name, never by position.

### Critical Issues
None.

### Positive Notes
- The plan records the ground truth it checked before planning (line widths, surrounding paragraphs, and how `command-pin-gaps` cites the heading) instead of assuming it.
- The byte-identical guard list matches the spec's "Untouched" list item for item.
- The plan has a single step and no invented verification tasks, which fits the phase's own point that checking belongs to the review.

PLAN_REVIEW_PASS

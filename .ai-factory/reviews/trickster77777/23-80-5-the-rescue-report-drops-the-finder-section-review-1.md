## Code Review Summary

**Files Reviewed:** 1 (`src/skills/task-rescue/SKILL.md`). The other staged files are the plan, its sidecar and the plan-review, which are pipeline artifacts.
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The change matches contract line 80.5 in `.ai-factory/roadmaps/trickster77777.md`, the first open line under Phase 80. I read the task spec `0257-the-rescue-report-drops-the-finder-section.md`. All three targets the spec names are gone: the `## Who found what` section of the template, the paragraph after the template, and the Step 3 mention. Everything the spec says stays is unchanged: `**Stopped at:**` with the step fact and what stopped the run, "Extending the file", the destination, the hooks, the title phrase and "When the write cannot happen". The phase's governing spec is `docs/names-and-reasons-not-laws.md`. The change only removes text and adds no new rule, so it fits that spec.
- **Architecture — OK.** The edit stays inside one skill body. No `loads:` edge changes. The removed paragraph held the only pointer in this file to `orchestrator-artifacts` § "3. Sidecar fields". The skill still loads and uses `orchestrator-artifacts` elsewhere, and the `**Sessions:**` line still takes its ids from the Step 1 capture, so no reference is left dangling.
- **Rules — WARN (non-blocking).** `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` are absent.

### Verification

- **Step 3, "First write of the report".** The sentence now reads "This first write holds the diagnosis and the intended repair and rollback." It is wrapped within the file's width, and the rest of the paragraph is word for word as before.
- **§ "Step 5.7 — Write the durable report", the template.** The diagnosis placeholder is now followed by one blank line and then `## Intended repair`. The title line, the five header lines and the `## Intended repair` body are unchanged.
- **The paragraph after the template.** The whole paragraph is removed. The closing fence is followed by one blank line and then "The title phrase names what stopped the run, never a root-cause claim." The diagnosis's prose form is still stated in Step 3, under "Form: a chronological narrative in plain prose".
- **Sweep.** `grep -n -i -E "who found|finder|not stated" src/skills/task-rescue/SKILL.md` returns no lines. A wider check for `round R`, `head N`, `who`, `caught` and `Sidecar fields` finds only the `**Stopped at:**` line's "round R". That text belongs to what-stopped-the-run and the spec keeps it. Step 3's "The narrative may name a round and the reviewer whose finding it tells" describes how the diagnosis is told, not the finder section, so it stays in scope as written.
- **Frontmatter.** The `description:` field does not mention finders. The file has 322 lines, under the 500-line limit.

### Critical Issues

None.

### Positive Notes

- The diff is limited to the three targets and leaves no orphaned whitespace or broken fence.
- The record of who caught what still exists in `.ai-factory/chronicle/skills.md`, which links rescue catches to their reports. Removing the section from the skill therefore loses no history.

REVIEW_PASS

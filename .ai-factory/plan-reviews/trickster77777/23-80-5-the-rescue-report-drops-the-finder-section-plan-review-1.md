## Plan Review Summary

**Plan:** 80.5 — The rescue report drops the finder section
**Files in scope:** 1 (`src/skills/task-rescue/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The plan's heading matches contract line 80.5 in `.ai-factory/roadmaps/trickster77777.md`, the first open line under Phase 80 (80.1–80.4 are `[x]`). I read the task spec `0257-the-rescue-report-drops-the-finder-section.md` and the phase's governing spec `docs/names-and-reasons-not-laws.md`. The plan's four tasks cover every target in the spec's "What must be true after": the template section, the paragraph after the template, and Step 3's first-write sentence. They also keep what the spec says stays: `**Stopped at:**`, the dated-section extension, the destination, the hooks, the title phrase and "When the write cannot happen".
- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` does not mention the finder section. The edit stays inside one skill body. No `loads:` edge changes, and no engine contract is touched. `orchestrator-artifacts` is still loaded and used elsewhere in the skill, at § 1 and § 3 for the Step 1 capture and at §6 for the pins. Removing the § "3. Sidecar fields" pointer along with the finders paragraph therefore leaves no dangling dependency.
- **Rules — WARN (non-blocking).** `.ai-factory/RULES.md` is absent. `.ai-factory/skill-context/aif-review/SKILL.md` is also absent, so no project overrides apply.
- **Chronicle — OK.** The spec says who-caught-what now lives in `.ai-factory/chronicle/skills.md`. That file exists and already links rescue catches to their reports, so removing the section loses no record.

### Verification against the codebase

- **Step 3, "First write of the report".** The last sentence reads, word for word, "This first write holds the diagnosis, the section on who found what, and the intended repair and rollback." The replacement "This first write holds the diagnosis and the intended repair and rollback." re-wraps cleanly under the file's ~86-column prose width. The plan correctly keeps the rest of the paragraph unchanged.
- **§ "Step 5.7 — Write the durable report", template.** The fenced template holds exactly the lines the plan deletes: `## Who found what`, `**Root cause found by:** <who>, <when>`, and `- <the finding> — <who>, <when>`, with blank lines between them. After the deletion, the diagnosis placeholder, one blank line and `## Intended repair` give the shape the spec asks for. The header lines, including `**Stopped at:**`, stay as written.
- **The finders paragraph.** It runs from "The diagnosis keeps its prose form; the finders live only in `## Who found what`," to "`## Who found what` holds one bullet per finding the diagnosis names." It is followed by a blank line and then "The title phrase names what stopped the run, never a root-cause claim." The plan's before/after boundaries match the file. The plan also claims the diagnosis's prose form is stated in Step 3 and survives there. That holds: Step 3's "Form: a chronological narrative in plain prose" stays.
- **Sweep.** Running `grep -n -i -E "who found|finder|not stated"` on the current file returns only these three targets. A wider grep over `docs`, `src`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `.ai-factory/ARCHITECTURE.md` and the orchestrator's non-`.ai-factory` tree finds no other text that names the section. This agrees with the plan's assumption and the spec's finding. The skill's `description:` frontmatter does not mention finders, so it needs no change.
- **Settings.** `Testing: no` and `Docs: no` fit this change: it deletes prose from a skill body and adds no behavior surface. The sweep task is the check the spec itself names, not one the planner invented.

### Critical Issues

None.

### Positive Notes

- Each deletion's boundaries are tied to verbatim anchor text, not line numbers, so the plan survives edits elsewhere in the file.
- The assumption about the `orchestrator-artifacts` § "3. Sidecar fields" pointer is reasoned explicitly and is correct: the `**Sessions:**` line keeps its source through the Step 1 capture.
- History artifacts (spec 0253, phase note 0226, earlier rescue reports, the `[x]` 80.1 line) are correctly left alone as strata.

PLAN_REVIEW_PASS

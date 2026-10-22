# Plan: 80.5 — The rescue report drops the finder section

## Context
In `src/skills/task-rescue/SKILL.md`, the report template in § "Step 5.7 — Write the durable report" has a `## Who found what` section. The paragraph after the template defines *who* and *when*, says where each one comes from, writes "not stated" for an unknown finder, and fixes one bullet per finding. The paragraph "First write of the report" in Step 3 also names "the section on who found what". The family's chronicle of catches, `.ai-factory/chronicle/skills.md`, now records who caught what. A rescue's job is the task and the report of its rescue, so all three of these go. `**Stopped at:**` keeps the step fact and what stopped the run. The template runs from the diagnosis to `## Intended repair`. Nothing else in § 5.7 changes.

The task spec `.ai-factory/specs/trickster77777/0257-the-rescue-report-drops-the-finder-section.md` is authoritative. The phase's governing spec is `docs/names-and-reasons-not-laws.md`.

Assumptions:
- The spec gives no exact after-text for Step 3's sentence. The draft below changes only that clause and keeps the file's hard wrap of about 86 columns.
- The spec's sweep finds only the three targets. No other doc, skill, `README.md` or `AGENTS.md` names the finder section. This was checked with `grep -rn -i -E "who found|finder" docs src README.md AGENTS.md`. Earlier rescue reports, the landed spec 0253 and phase note 0226 are history and stay as they are.
- In the finders paragraph, the pointer to `orchestrator-artifacts` § "3. Sidecar fields" exists only to say where the role and round come from. It goes with that paragraph. The `**Sessions:**` line still takes its ids from the Step 1 capture.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/task-rescue/SKILL.md`

- [x] **Step 3's first-write sentence names no finder section**
  Files: `src/skills/task-rescue/SKILL.md`
  In the Step 3 paragraph that starts with **First write of the report.**, change only the last sentence. It currently reads "This first write holds the diagnosis, the section on who found what, and the intended repair and rollback." Change it to:
  > This first write holds the diagnosis and the intended repair and rollback.
  Re-wrap the paragraph's last lines to the file's width. Keep the rest of the paragraph word for word: the pointer to § "Step 5.7 — Write the durable report", `note`, the destination, the three hooks, the topic slug, and keeping the returned path.

- [x] **The template drops `## Who found what`**
  Files: `src/skills/task-rescue/SKILL.md`
  In the fenced `markdown` template in § "Step 5.7 — Write the durable report", delete these lines: the `## Who found what` heading, the `**Root cause found by:** <who>, <when>` line, the `- <the finding> — <who>, <when>` bullet, and the blank lines between them. After the edit, `<the diagnosis, exactly as Step 3 wrote it>` is followed by one blank line and then `## Intended repair`. Leave the title line, the five header lines (including `**Stopped at:** <the Step 1 \`step\` fact, or "absent"> — <what stopped the run: the review cycle spent at its round R, or the role that escalated>`) and the `## Intended repair` body exactly as they are.

- [x] **The finders paragraph after the template goes whole** (depends on The template drops `## Who found what`)
  Files: `src/skills/task-rescue/SKILL.md`
  Delete the whole paragraph that follows the closing fence of the template. It starts with "The diagnosis keeps its prose form; the finders live only in `## Who found what`," and ends with "`## Who found what` holds one bullet per finding the diagnosis names." It covers the definitions of *who* and *when*, the sources of role, round, user and heads, the "not stated" rule, and the one-bullet rule. The diagnosis's prose form is stated in Step 3 and stays there. After the edit, the closing fence is followed by one blank line and then "The title phrase names what stopped the run, never a root-cause claim." Keep that sentence and the paragraph "When the write cannot happen" unchanged. Do not touch the rest of § 5.7: the intro, "Extending the file", the destination, the hooks, the slug and the template intro.

- [x] **Sweep confirms nothing names a finder** (depends on all tasks above)
  Files: `src/skills/task-rescue/SKILL.md`
  Run the spec's sweep: `grep -n -i -E "who found|finder|not stated" src/skills/task-rescue/SKILL.md`. It must return no lines. If it returns any, remove the reference in the same way as the tasks above.

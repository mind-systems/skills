## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/19-80-1-the-report-is-the-chronicle.md`
**Target:** `src/skills/task-rescue/SKILL.md` (single file)
**Risk Level:** 🟡 Medium. The plan is close to correct, but one of its own instructions makes its verification step fail.

### Context Gates

- **Roadmap — OK.** `# Plan: 80.1 — The report is the chronicle` matches task 80.1 in
  `.ai-factory/roadmaps/trickster77777.md`, Phase 80. The task spec
  `0253-the-report-is-the-chronicle.md` was read in full. The plan covers every clause of
  its § "What must be true after": first write at the end of Step 3, dated appended
  sections, the `Stopped at` line naming the stop, the `## Who found what` section with
  its *who* and *when* sets and "not stated", "What was done" moved to the first appended
  section, the three paragraphs removed, the vocabulary sentence and the "What NOT to do"
  bullet removed, and "When the write cannot happen" kept.
- **Governing spec / phase note — OK.** `docs/names-and-reasons-not-laws.md` and the
  phase note `0226` (§ "Who found what": "keeps the run's stop and the finder of the root
  cause apart") agree with the plan. The template keeps the stop on `Stopped at` and the
  root-cause finder on its own line.
- **Scope — OK.** The plan leaves Step 4, Step 5, § 5.5, § 5.6 and the `description:`
  frontmatter to 80.2 and 80.3, which matches those tasks' contract lines.
- **Codebase assumptions checked:**
  - `note` reports its saved path (`Note saved: <destination>/<NN>-<slug>.md`), so "keep
    the path `note` returns" works.
  - `allowed-tools` already grants `Write Edit`.
  - Every Step 2 class, including escalation, non-convergence and stale implementer
    session, passes through Step 3, so the first write is reached on every branch.
  - `orchestrator-artifacts` § "3. Sidecar fields" holds `planner`, `implementer` and
    `plan-reviewer-<N>`, with no reviewer key, so the reviewer's round has to come from
    the review file's number. The plan says exactly that.
  - The dated `## 2026-10-21` heading exists in `rescue-reports/tradeoxy_core/0044-…`.
- **ARCHITECTURE / RULES — not present / no conflict.**

### Critical Issues

1. **The plan's § 5.7 item 2 makes its own sweep fail, and the text it asks for narrates
   change history.**
   § "§ 5.7: reshape the report into a chronicle", item 2, last bullet, tells the
   implementer to say that the first appended section records "what the template's 'What
   was done' section used to hold". The sweep in § "Verify the blast radius", item 2, runs
   `grep … "What was done" …` and requires it to return nothing. An implementer who
   follows item 2 word for word produces a file that fails the plan's own check. The
   sentence also describes a past state ("used to hold") inside a skill body. The global
   instructions forbid this: present tense, never change history.
   **Fix:** state only what the section holds: what the repair did (the depth chosen, the
   escalation option taken, or the non-convergence choice made) and what was deleted or
   kept. Drop any mention of the old "What was done" section.

2. **"Write the report." collides with Step 3's own use of "the report".**
   Inside Step 3, "the report" already means the printed Diagnosis Report:
   - "**Write the Diagnosis Report**"
   - "the report says so and names it as already-recorded divergence"
   - "Attach the root-cause category … to the report as a classification", which is the
     paragraph directly before the new one.

   A new paragraph headed "**Write the report.**", placed right after that, reads as
   another instruction about the Diagnosis Report rather than the durable file. The skill
   already has a name for the file: its § 5.7 heading is "Write the durable report".
   **Fix:**
   - Head the new paragraph "**Write the durable report.**" and use "the durable report"
     in its body.
   - Make clear whether the plan's closing line "The write is mandatory at this point, so
     the order of the steps carries it." is text for the skill or a note for the
     implementer. As written, it can be read as either.

3. **§ 5.7 item 4 misses one place that pins the moment.**
   Item 4 changes "run **at this moment**, here in Step 5.7" and "resolved fresh at this
   point". The paragraph between them also says "Neither half is stored nor cached — both
   are re-resolved **here** regardless of anything computed earlier." Once the write moves
   to the end of Step 3, "here" in § 5.7 no longer names the moment of the write.
   **Fix:** add a third change, for example "both are re-resolved at the first write".

4. **The append paragraph does not say what happens when the first write failed.**
   "When the write cannot happen" says to tell the user and complete the rescue, never
   invoke `note` again and never defer the write. The new append paragraph says to append
   "directly to the path the first write returned" with Edit/Write. If the first write
   failed, there is no such path. An agent reaching the first append in § 5.7 is left to
   guess, and the likely guess is to create the file with Write at a path it builds
   itself. That is exactly the fallback path and deferred write the kept paragraph
   forbids.
   **Fix:** add one clause to the new append paragraph (not to the kept "When the write
   cannot happen" paragraph). When the first write returned no path, nothing is appended
   and no file is created by Write.

### Positive Notes

- The plan follows the spec closely and pins each edit to a named paragraph. It never
  cites a line number.
- It correctly notices that the "title phrase" paragraph's rule ("the template never
  demands a part that branch does not produce") already covers the escalation branch's
  missing root cause under the new `Root cause found by` line. It keeps that paragraph
  instead of adding a special case.
- It keeps Step 1's "Capture the report facts" unchanged and gives the reason that its
  references to Step 5.7 stay true.
- The verify step adds a second grep beyond the spec's sweep, which catches the removed
  paragraphs' own wording.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — The removed "Which runs" paragraph was the only place that said the scope-overload exit of Step 4 writes no report. After 80.1 that exit runs after the first write at the end of Step 3, so it leaves a report on disk. It never reaches § 5.7, so no dated section records that the task was flagged and pointed to `/roadmap-decompose`. Step 4 is outside 80.1's scope. 80.3 removes the scope-overload flag and makes "the rescue writes its report with the intended rollback, waits, then extends the report", so that task should make sure every ending of a rescue gets its dated section. [dismissed]

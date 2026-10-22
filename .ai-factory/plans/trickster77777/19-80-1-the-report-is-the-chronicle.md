# Plan: 80.1 — The report is the chronicle

## Context
`task-rescue` currently writes its durable report once, at the end of § "Step 5.7 — Write the durable report", and never reopens it. The report also records nothing about who found a finding, and Step 3 and § "What NOT to do" forbid the orchestrator's own words in the narrative. After this task, Step 3 ends with the first write of the report through `note`. Every later addition is appended as a section headed by its date, and no earlier line changes. The `Stopped at` line names what stopped the run. A new template section records who found the root cause and each finding, and when. The "When", "Which runs" and printout paragraphs and the vocabulary rule are removed.

The task spec `.ai-factory/specs/trickster77777/0253-the-report-is-the-chronicle.md` is authoritative. Its § "What must be true after" states the required behaviour, but it pins no texts word for word. Write the after-texts below in the skill's existing register. Keep the file's hard wrap at about 86 columns. The phase's governing spec is `docs/names-and-reasons-not-laws.md`.

Assumptions:
- An appended section is headed `## <YYYY-MM-DD>`. This matches the dated section a head already appended to `.ai-factory/rescue-reports/tradeoxy_core/0044-88-6-…md`.
- Step 1's "Capture the report facts" paragraph stays unchanged, as the spec's Finding says. Its mentions of "the report Step 5.7 writes" stay true because § 5.7 still defines the report.
- § "Step 5" (including its closing restate paragraph), Step 4, Step 5.5, Step 5.6 and the frontmatter `description:` are out of scope. Tasks 80.2 and 80.3 own them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/task-rescue/SKILL.md`

- [x] **Step 3: drop the vocabulary rule and end with the first write**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 3 — Extract root cause":
  1. Rewrite the paragraph that opens "Domain language only:".
     - Remove the label "Domain language only:".
     - Remove the whole sentence "Zero orchestrator vocabulary — no iteration counts, no PASS markers, no phase names, no sidecar."
     - Keep the instruction itself: describe what the task spec / contract line stated wrongly or left ambiguous, and how the plan or code went wrong as a consequence.
     - Add one sentence saying the narrative may name a round and the reviewer whose finding it tells.
     - In the escalation paragraph (the one that opens "For an escalation classification"), delete the parenthetical " (already domain language by construction)" that follows "artifact's `## Escalation` section". It only justified the vocabulary rule removed above. Leave the rest of that paragraph unchanged, and leave every other Step 3 paragraph unchanged.
  2. After the closing paragraph of Step 3 (the one that opens "Attach the root-cause category"), and before the `---` that precedes Step 4, add a new paragraph headed "**Write the durable report.**". In Step 3, "the report" already means the printed Diagnosis Report, so this paragraph's body says "the durable report" every time it refers to the file. The paragraph must say:
     - Step 3 ends with the first write of the durable report.
     - The write is made per § "Step 5.7 — Write the durable report", through `note`, with the destination, the three hooks and the topic slug that section gives.
     - The rescue keeps the path `note` returns, because every later section of the durable report is appended to that file.
     (Note for the implementer only, not text for the skill: the paragraph is written as a mandatory instruction at this position, so the order of the steps carries the first write. Do not add a sentence about the order.)

- [x] **§ 5.7: reshape the report into a chronicle** (depends on Step 3: drop the vocabulary rule and end with the first write)
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5.7 — Write the durable report":
  1. **Opening paragraph.** Keep the purpose: the report is written through `note` (loaded via `loads: note`) so a failed attempt leaves a record after Step 5 deletes the artifacts it was drawn from. Remove "Write one durable report for this run". Say that the first write happens at the end of Step 3 and that this section defines it.
  2. **Delete the "When." paragraph.** Replace it with one paragraph that says:
     - The file is extended while the rescue is hot.
     - Each addition is a section headed by its date (`## <YYYY-MM-DD>`) and appended directly to the path the first write returned, with Edit/Write and not through `note`.
     - The lines already in the file stay as written.
     - The first appended section is made here, once the repair is done. It records what the repair did (the depth chosen, the escalation option taken, or the non-convergence choice made) and what was deleted or kept.
     - When the first write returned no path, because it failed per "When the write cannot happen", nothing is appended and Write creates no file.
     Write all of this in the present tense. Do not mention the removed "What was done" section or any earlier behaviour. Nothing in the section may say the report is written once, at the end, or never reopened or read back.
  3. **Delete the "Which runs." paragraph entirely.**
  4. **"Destination, both halves resolved at write time."** Keep this paragraph, its two bullets and the next two paragraphs. Change only the wording that places the moment in this step:
     - "run **at this moment**, here in Step 5.7" becomes "run at the moment of the first write, at the end of Step 3". Keep the rule that nothing is carried from an earlier step.
     - "both are re-resolved here regardless of anything computed earlier" becomes "both are re-resolved at the first write regardless of anything computed earlier".
     - "resolved fresh at this point" becomes "resolved fresh at the first write".
     Keep the bullets on `note`'s three hooks and the topic-slug paragraph word for word.
  5. **The template.** Make these changes to the fenced `markdown` block:
     - Change the `Stopped at` line so it holds the Step 1 `step` fact and what stopped the run, for example: `**Stopped at:** <the Step 1 \`step\` fact, or "absent"> — <what stopped the run: the review cycle spent at its round R, or the role that escalated>`. Do not add a second line for the stop.
     - Keep the other four header lines and `<the diagnosis, exactly as Step 3 wrote it>` unchanged.
     - Remove the `## What was done` section and its placeholder.
     - After the diagnosis, add a section headed `## Who found what`. It holds a line for who found the root cause and when, kept separate from the stop (for example `**Root cause found by:** <who>, <when>`). Under that line, it holds one bullet per finding the diagnosis names, in the form `- <the finding> — <who>, <when>`.
  6. **New paragraph directly after the template.** It must say:
     - The diagnosis keeps its prose form. The finders live only in this section, outside it.
     - *Who* is one of: the user; head N, by its number; the editor; the plan-reviewer or the reviewer at round R; the implementer or the planner; the rescue itself.
     - *When* is one of: before the run; in the run; in the rescue; after the rescue, for a defect in the repair itself.
     - The role and round come from the sidecar's session keys (per `orchestrator-artifacts` § "3. Sidecar fields") and from the number each plan-review and review file carries. The user and the heads come from the conversation.
     - A finder that no artifact and no conversation states is written as "not stated".
  7. Keep the "The title phrase names what stopped the run…" paragraph unchanged. Its rule that the template never demands a part a branch does not produce covers the escalation branch, which has no root cause.
  8. Keep the "**When the write cannot happen.**" paragraph unchanged, with both of its rules: never invoke `note` a second time and never defer the write.
  9. **Delete the "The chat printout is unchanged." paragraph entirely.**

- [x] **§ "What NOT to do": drop the orchestrator-mechanics bullet**
  Files: `src/skills/task-rescue/SKILL.md`
  Delete the whole bullet that opens "Never present orchestrator mechanics", including its "This constrains your *output and reporting*, not your analysis…" clause. Leave every other bullet unchanged.

### Verify the blast radius

- [x] **Run the spec's sweep** (depends on all edits above)
  Files: none changed. This is a read-only check.
  1. From the repo root, run `grep -n -E "reopened|exactly once|reads it back|Zero orch|orchestrator mech" src/skills/task-rescue/SKILL.md`. It must return nothing.
  2. Run `grep -n -E "What was done|Which runs|printout is unchanged|once, at the end|domain language" src/skills/task-rescue/SKILL.md`. It must also return nothing.
  3. Confirm that Step 1's "Capture the report facts" paragraph is byte-unchanged.
  4. Confirm that the frontmatter is unchanged. Neither `loads:` nor `allowed-tools` needs to change: Edit/Write are already granted for the appends.
  5. Edit no file outside `src/skills/task-rescue/SKILL.md`. The spec's Finding states that `docs/the-pipeline-speaks-to-an-architect.md`, `docs/self-analysis.md` and `note` stay true as they are.

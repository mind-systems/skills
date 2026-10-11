# Plan: 84.1 — the capture records the session ids and the report names them

## Context
`task-rescue` captures `step` and `elapsed` from the sidecar at discovery but no session id, and its durable report has no line for one. So after a spec-depth reset or a re-run, the planner and implementer sessions cannot be resumed. This task makes the Step 1 capture record every session id the sidecar holds, under its key, and adds a `**Sessions:**` header line to the Step 5.7 report template. The capture's "four facts" loses its count. Every after-text is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0243-the-capture-records-the-session-ids-and-the-report-names-them.md`, § "What must be true after". Copy those texts exactly and do not paraphrase them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `task-rescue`

- [x] **Rewrite the Step 1 capture paragraph**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 1 — Discover artifacts", edit the paragraph that opens "**Capture the report facts.**". Keep the file's existing hard wrap (about 86 columns, matching the surrounding lines). Make only these edits:
  1. Lead sentence: replace "Record four facts now, at discovery, … and `step`/`elapsed` are unrecoverable once that happens." with the spec's pinned text: "Record these facts now, at discovery, before anything is deleted, and hold them for the report Step 5.7 writes — Step 5 deletes or rewrites the sidecar at some repair depths and a re-run overwrites its keys, so `step`, `elapsed` and the session ids are unrecoverable once that happens." Keep the leading bold "**Capture the report facts.**".
  2. The `step`/`elapsed` bullet becomes: "- **`step` and `elapsed`** — read from the task's sidecar, per `orchestrator-artifacts` § 3." This drops "the two fields worth keeping".
  3. Directly after that bullet, and before the "**Where the sidecar lives**" bullet, insert the new bullet: "- **The session ids** — every session id the sidecar holds, each under its key as the sidecar spells it. They are the sessions whose artifacts this rescue reads, and the report names them so that one can be resumed and asked to quote what it saw. The sidecar is the live state of the attempt and is overwritten; the report is the record of this attempt and its diagnosis."
  4. In the "**Where the sidecar lives**" bullet, replace only the closing clause "an absent one — both numbers lost, with no signal." with "an absent one — everything it holds lost, with no signal." Leave the rest of the bullet (the layout and named-roadmap stem text) untouched.
  5. The "**No sidecar on disk**" bullet becomes: "- **No sidecar on disk** → record `step`, `elapsed` and the session ids as **absent**; never guess, never reconstruct a number from anything else. Step 5.7 renders absence as absence."
  Do not touch the Project and Date bullets or the "**Read every artifact file found**" paragraph that follows.

- [x] **Add the Sessions line to the Step 5.7 template** (depends on Rewrite the Step 1 capture paragraph)
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5.7 — Write the durable report", in the fenced `markdown` template, insert this line directly after `**Elapsed before the rescue:** <the Step 1 \`elapsed\` fact, or "absent">` and before the blank line that precedes `<the diagnosis, exactly as Step 3 wrote it>`:
  `**Sessions:** <every session id the Step 1 capture holds, each as \`<key>: <id>\`, or "absent">`
  Leave nothing else in the template or the section changed.

### Verify the blast radius

- [x] **Run the spec's sweep and confirm nothing else breaks** (depends on Add the Sessions line to the Step 5.7 template)
  Files: none changed. This is a read-only check.
  From the repo root, run the sweep listed in the spec's § "What breaks on contact" (`grep -rn` for `report facts`, `unrecoverable`, `fields worth`, `both numbers`, `No sidecar on disk`, `Elapsed before`, `Stopped at`, `elapsed`, `resumable session` over `src docs CLAUDE.md`). Expected results:
  - `fields worth` and `both numbers` return nothing.
  - Every other hit is the edited targets or a site the spec's Finding marks as staying true. Those are the § "Step 5" dropped-key sentence and the `planner`/`elapsed` preservation lines, the "What NOT to do" bullet, and `orchestrator-artifacts` § "3. Sidecar fields".
  Edit no other file, including `orchestrator-artifacts`, `docs/` and `.ai-factory/rescue-analysis/method.md`. Also confirm that `src/skills/task-rescue/SKILL.md` stays a valid skill file with its frontmatter unchanged. Its body is already over 500 lines and this task adds only a few lines, so do not split it as part of this task.

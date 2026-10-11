## Code Review Summary

**Files Reviewed:** 1 (`src/skills/task-rescue/SKILL.md`). The other staged files are orchestrator artifacts: the plan, the plan-review and the sidecar.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. The edit stays inside one lens skill. It adds no `loads:` edge and edits no engine, and `orchestrator-artifacts` is read but not edited, as the spec's Finding requires.
- **Rules:** WARN. `.ai-factory/RULES.md` is not present.
- **Roadmap:** OK. The plan heading matches open line 84.1 in `.ai-factory/roadmaps/trickster77777.md`, and its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0243-…`. The phase note `0242-…` says no `docs/` governing spec covers this, so the task spec is the authority.
- **Spec conformance:** Each after-text in § "What must be true after" is in the file word-for-word, allowing only for hard-wrap line breaks:
  - The lead sentence of "**Capture the report facts.**". The count "four" is gone.
  - The `step`/`elapsed` bullet. "the two fields worth keeping" is gone.
  - The new "**The session ids**" bullet, placed directly after the `step`/`elapsed` bullet.
  - The "everything it holds lost, with no signal." clause in the "Where the sidecar lives" bullet. The rest of that bullet is unchanged.
  - The "**No sidecar on disk**" bullet.
  - The `**Sessions:** <every session id the Step 1 capture holds, each as `<key>: <id>`, or "absent">` line, placed directly after `**Elapsed before the rescue:**` in the Step 5.7 template.

  The Project and Date bullets, the frontmatter and the rest of Step 5.7 are untouched.
- **Blast radius:** I re-ran the spec's sweep on the edited tree:
  - `fields worth`, `both numbers` and `four facts` return nothing.
  - `report facts`, `unrecoverable` and `No sidecar on disk` hit only the rewritten Step 1 paragraph.
  - `Stopped at` and `Elapsed before` hit only the Step 5.7 template.
  - `resumable session` hits only `orchestrator-artifacts` § "3. Sidecar fields", which stays true per the spec's Finding.
  - Nothing appears in `docs/` or `CLAUDE.md`.
- **Ground truth note:** This task's own sidecar holds a `plan-reviewer-1` key, which `orchestrator/orchestrator/agents.py` writes through `_write_session`. § 3 does not yet name that key, so a rescue that reads ids by § 3's list would miss it. The spec's Finding assigns that to § 3's lockstep with the orchestrator, and open task 84.2 (`.ai-factory/specs/trickster77777/0246-the-engine-names-the-plan-reviewer-session-keys.md`) already tracks it. It is not a defect of this diff and is already on the roadmap, so I did not add it as a deferred observation.

### Critical Issues
None.

### Positive Notes
- The pinned texts are copied verbatim, and the hard wrap matches the surrounding prose. The line widths are within the file's existing spread, so they add no new irregularity.
- The `Sessions` line keeps the same "or "absent"" convention as its neighbours, so a report written without a sidecar still renders absence as absence.
- The diff touches only the two targets the spec names. No change leaks into `orchestrator-artifacts`, `docs/` or `.ai-factory/rescue-analysis/method.md`.

REVIEW_PASS

# Phase 84 — a rescue report leads back to the sessions whose artifacts it read

No doc states this: `task-rescue` is its own doc, and neither `docs/` nor `orchestrator-artifacts` says what a rescue report carries.

Where `src/skills/task-rescue/SKILL.md` stands:
- **The capture.** § "Step 1 — Discover artifacts", the paragraph "Capture the report facts", records the project, the date, and `step` and `elapsed` from the sidecar, "before anything is deleted", because "Step 5 deletes the sidecar at some repair depths". It records no session id, though the sidecar holds `planner` and `implementer` as "resumable session ids" (`orchestrator-artifacts`, § "3. Sidecar fields").
- **What the repair does to them.** § "Step 5 — Apply repair and roll back artifacts" deletes the sidecar at spec depth, drops `implementer` at spec+plan depth and at the plan-ratified depth, and a re-run of the orchestrator overwrites the keys, `_write_session` in `orchestrator/orchestrator/agents.py` setting `data[key] = value`. After any of these nobody can resume the planner or the implementer with `claude -p --resume <id>` and ask it to quote what it saw.
- **The report.** § "Step 5.7 — Write the durable report" has a template with `Stopped at` and `Elapsed before the rescue` and no line for a session, so the report that outlives the artifacts leads back to none of the sessions that produced them.
- **The reader.** `.ai-factory/rescue-analysis/method.md` takes the `planner` session id from a report's rewritten sidecar, which exists only where the repair kept it.

The sidecar is the live state of the attempt and is overwritten; the report is the record of this attempt and its diagnosis. They are two moments, not two homes of one fact.

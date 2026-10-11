# Phase 86 — the skills speak of the orchestrator's protocol and never cite its source

No doc states this beyond the standing rule that a skill is its own documentation: the skills run outside this repository's context, so what they need of the orchestrator is part of their own text.

The orchestrator moved its modules, so the files and a function that two skills name no longer hold what they are cited for. The remedy is not a fresher citation: a skill speaks of the orchestrator as an executor and states a protocol it mirrors as behaviour, and a doc is where a sibling's path may be named.

Where the skills stand:
- **`orchestrator-artifacts`**, § "7. Mirrors-the-orchestrator invariant", names `orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`, `prompts/escalation.md` and `resume.py` as the files it mirrors. The invariant is right and the citation is the defect: it should say that a change to the orchestrator's file protocol is a change here, in lockstep.
- **`task-rescue`**, § "Valid sidecar `step` states", says its table mirrors two functions "in `orchestrator/resume.py`", one of which no longer exists. The table mirrors the orchestrator's accepted set of sidecar `step` values; the file and the functions need not be named.
- No other skill, command or agent text names an orchestrator file, path or function.

The source is a reviewer of the orchestrator's task that moved the flow, who reported it to the architect that task named.

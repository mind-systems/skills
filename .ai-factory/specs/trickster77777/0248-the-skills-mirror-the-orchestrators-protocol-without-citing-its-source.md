# 86.1 — the skills mirror the orchestrator's protocol without citing its source

## What is true now

`src/skills/orchestrator-artifacts/SKILL.md`, § "7. Mirrors-the-orchestrator invariant", reads: "This file mirrors the orchestrator's file protocol (`orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`, `prompts/escalation.md`, `resume.py`) — if the protocol changes there, update this file; do not let them diverge."

`src/skills/task-rescue/SKILL.md`, § "Valid sidecar `step` states", reads: "This table mirrors `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py` — if the orchestrator's accepted set changes, update this table; do not let them diverge."

Both name the orchestrator's source files or functions, and neither is right any longer: the orchestrator's modules moved, and the second function no longer exists.

## What must be true after

In `orchestrator-artifacts`, § "7. Mirrors-the-orchestrator invariant", the sentence reads:

"This file mirrors the orchestrator's file protocol, and a change to that protocol on the orchestrator's side is a change here, made in lockstep."

In `task-rescue`, § "Valid sidecar `step` states", the sentence reads:

"This table mirrors the orchestrator's accepted set of sidecar `step` values — if it changes, update this table; do not let them diverge."

The rest of each paragraph stands.

## What breaks on contact

**Rule:** a text breaks on this change if a skill, command or agent names an orchestrator file, path or function.

**Sweep:**
```
grep -rn "orchestrator/" src
grep -rn "_validate_sidecar_step" src
grep -rn "_detect_task_step" src
grep -rn "\.py" src
```

**Finding.** The search for `orchestrator/` returns `orchestrator-artifacts`' mirror sentence and `task-rescue`'s sentence after the valid-states table, each a target. The searches for `_validate_sidecar_step` and `_detect_task_step` return the `task-rescue` sentence alone, the target. The search for `.py` returns the mirror sentence, the `task-rescue` sentence and the scripts of `ui-ux-pro-max`, that skill's own, which stay true. Beyond these, no skill, command or agent text names an orchestrator source: the texts that speak of "the orchestrator" speak of it as the executor that runs a roadmap, and stay true; `orchestrator-artifacts`' reverse-graph command names its own callers, not the orchestrator's sources, and stays true; the function-like names in `roadmap-test-coverage` and the shell functions of `observe-logs` belong to code under test or to that skill's own script, and stay true. `docs/the-pipeline-speaks-to-an-architect.md` names a sibling repository's file by its root-relative path, which a doc may do, and stays true.

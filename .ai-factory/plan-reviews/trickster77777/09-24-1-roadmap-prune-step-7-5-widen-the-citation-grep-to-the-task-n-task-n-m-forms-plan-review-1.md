## Plan Review Summary

**Plan:** roadmap-prune Step 7.5 — widen the citation grep to the `Task N` / `task N.M` forms
**Files Reviewed:** 1 plan + target `src/skills/roadmap-prune/SKILL.md` + ground-truth in `orchestrator/`
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture / Rules:** No `.ai-factory/ARCHITECTURE.md`/`RULES.md` boundary or convention conflict — the change is a two-alternation widening of a report-only grep inside one skill body, no module boundary crossed. WARN: none.
- **Roadmap linkage:** The plan is a Step 7.5 refinement of `roadmap-prune`; it stays within the skill body and does not touch cross-skill contracts. No missing linkage worth blocking.
- **Vocabulary/protocol tokens:** The edit leaves the `## Deferred observations` heading, PASS signals, and the "guidance, not contract" note byte-identical (Guards section confirms). Good.

### Verified correct
- **Edit anchors match ground truth.** Step 7.5 item 3 prose list (`Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`) sits at SKILL.md:375–376, and the fenced `grep -rInE` block at 379–382, exactly as the plan quotes. Task 1/Task 2 target the right two sites (the prose list is the contract, the invocation is guidance — the plan edits both consistently).
- **ERE validity.** The appended alternations `Task [0-9]` and `task [0-9]+\.[0-9]+` are valid POSIX ERE (`+` quantifier, `\.` literal dot); `grep -E` accepts the widened pattern without error (verified by running it against `orchestrator/`).
- **The widening adds real value.** The pre-change pattern matches **zero** `# Task N:` comment lines in `orchestrator/tests/` (confirmed: `grep -c "# Task"` on old-pattern output = 0); the widened pattern surfaces them (test_agents.py at :17, :51, :83…; test_main.py, test_runtime.py, test_notify.py, test_roadmap.py). Case-sensitivity is correct — `Task [0-9]` and `task [0-9]+\.[0-9]+` are both needed since the scan runs without `-i`.
- **Scope guards are sound.** Report-only placement unchanged, whole-repo scope preserved, five pre-existing alternations left in order, `--exclude-dir` flags preserved. The `src/global/CLAUDE.md:18` "do not mirror-restore" guard is correct — the scan is a deliberate superset, not a divergence.

### Critical Issues

**Task 3, acceptance criterion (a) — wrong file:line citation (wrong assumption about the codebase).**
The verification task instructs the implementer to "confirm … it now surfaces `tests/test_agents.py:260` and the other `# Task N:` lines the pre-change pattern missed." Ground truth in `/Users/max/projects/sakshi/orchestrator`:
- `tests/test_agents.py:260` is a **blank line inside a comment divider**, not a `# Task N:` line, and is **not** matched by the widened pattern (matched lines in that file are :17 :51 :83 :95 :107 :119 :131 :160 :179 :216 :278 :309 :355 :391 :448 :471 :492).
- The line that actually reads `# Task 1: Fresh start and sidecar-driven steps …` at **:260 is in `tests/test_main.py`**, not `test_agents.py` — the filename was transposed.

As written, an implementer running Task 3 will not find a match at `test_agents.py:260`, and could wrongly conclude the widening regressed or is broken. Fix: correct the citation to `tests/test_main.py:260` (the real `# Task 1:` line at that number), or make the criterion cite a genuine `test_agents.py` Task line (e.g. `:17`). This is a self-check grounded in a false fact and must be corrected before the plan is handed to the orchestrator; the fix is trivial and stays within the plan's boundary.

### Positive Notes
- Both the contract (prose shape list) and the guidance (invocation) are edited in lockstep, with byte-identical-preservation instructions for the surrounding sentence and the "guidance, not contract" note — exactly the discipline this skill's coupling rules demand.
- The plan correctly keeps the scan report-only and whole-repo, and explicitly forbids narrowing to touched files.
- Dependency ordering (Task 2 depends on Task 1; Task 3 depends on Task 2) is right.

Correct the Task 3 citation and the plan is otherwise ready.

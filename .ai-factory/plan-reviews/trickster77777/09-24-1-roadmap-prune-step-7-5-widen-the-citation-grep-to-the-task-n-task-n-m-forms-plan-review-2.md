## Plan Review Summary

**Plan:** roadmap-prune Step 7.5 — widen the citation grep to the `Task N` / `task N.M` forms
**Files Reviewed:** 1 plan + target `src/skills/roadmap-prune/SKILL.md` + spec 87 + contract line 24.1 + ground-truth in `orchestrator/`
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture / Rules:** No boundary or convention conflict. The change is a two-alternation widening of a report-only grep inside one skill body; no module boundary crossed, no cross-skill contract touched. WARN: none.
- **Roadmap linkage:** Contract line 24.1 in `roadmaps/trickster77777.md` matches the plan exactly — same two alternations (`Task [0-9]`, `task [0-9]+\.[0-9]+`), same guards (`--exclude-dir` preserved, report-only, whole-repo, Steps 0–8 + Commit byte-identical, `CLAUDE.md:18` untouched). Spec 87 (`87-prune-scan-task-citation-shapes.md`) is faithfully implemented: prose list + `grep -rInE` invocation edited in lockstep, resulting command byte-identical to the spec's stated pattern. Good.
- **Vocabulary / protocol tokens:** The edit leaves the surrounding sentence and the "guidance, not contract" note byte-identical (Task 1/Task 2 mandate this). No PASS signal or `## Deferred observations` heading touched. Good.

### Verified correct
- **Prior critical issue is resolved.** Review 1 flagged Task 3's acceptance citation `tests/test_agents.py:260` as a transposed / non-matching file:line. This revision replaces it with two genuine, live-verified anchors: `tests/test_main.py:260` (`# Task 1: Fresh start and sidecar-driven steps…`) and `tests/test_agents.py:17` (`# Task 1: match within the last-5-line window`). Both confirmed against ground truth today — the self-check now rests on true facts.
- **Edit anchors match ground truth.** The prose shape list (`Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`) sits at SKILL.md:375–376, and the fenced `grep -rInE` block at 379–382 — exactly as the plan quotes (`~:375`, `~:379-382`). Task 1 targets the contract (prose list), Task 2 the guidance (invocation); both edited consistently.
- **ERE validity + no regression.** Ran the widened pattern against `/Users/max/projects/sakshi/orchestrator`: `grep -E` accepts it (exit 0), so the appended `Task [0-9]` and `task [0-9]+\.[0-9]+` (literal `\.`, `+` quantifier) are valid POSIX ERE. The five pre-existing shapes still match (60 hits preserved). Case-sensitivity is right — capital `Task` for `# Task N:` and lowercase-decimal `task N.M` are both needed since the scan runs without `-i`.
- **The widening surfaces the real leak.** The pre-change pattern nets zero `# Task N:` comment lines; the widened one surfaces them across `test_roadmap.py`, `test_runtime.py`, `test_main.py`, `test_notify.py`, `test_agents.py`. Task 3's example anchors are among the confirmed matches.
- **Scope guards are sound.** Report-only placement unchanged, whole-repo scope preserved, five pre-existing alternations left in order, `--exclude-dir=.ai-factory --exclude-dir=.git` preserved. The `src/global/CLAUDE.md:18` "do not mirror-restore" guard correctly frames the scan as a deliberate, permanent superset of the home rule (spec §"Cross-artifact coupling"), not a divergence.
- **Dependency ordering** (Task 2 depends on Task 1; Task 3 depends on Task 2) is correct.

### Critical Issues
None.

### Positive Notes
- Contract (prose list) and guidance (invocation) are edited in lockstep with byte-identical-preservation instructions for the surrounding sentence and the "guidance, not contract" note — exactly the coupling discipline this skill demands.
- Task 3's verification anchors were re-grounded to real matches rather than copied from the spec, which itself carried a now-stale example (`test_agents.py:260` "semver ordering" no longer exists in the orchestrator tree). The plan is more accurate than its own source spec on this point — the right call.
- Guards explicitly forbid narrowing scope to touched files and preserve report-only placement.

PLAN_REVIEW_PASS

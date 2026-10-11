## Code Review Summary

**Files Reviewed:** 2 (`src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/task-rescue/SKILL.md`), plus the staged pipeline artifacts: the plan, its sidecar and plan-review 1
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. The change is confined to two skill bodies. `.ai-factory/ARCHITECTURE.md` cites no orchestrator source file and needs no change.
- **Rules** — WARN (informational): `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` do not exist, so no project overrides apply.
- **Roadmap** — OK. The diff implements open line **86.1** in `.ai-factory/roadmaps/trickster77777.md`. Its `Spec:` tag resolves to `0248`, and its phase note is `0247`. Phase 86 names no governing spec, which matches the phase note.

### Verification against the task spec
- **`orchestrator-artifacts` § "7. Mirrors-the-orchestrator invariant"** — Joining the hard wrap, the paragraph now reads: "This file mirrors the orchestrator's file protocol, and a change to that protocol on the orchestrator's side is a change here, made in lockstep." This matches the spec's pinned after-text byte for byte. No file, path or function is named. The heading is unchanged.
- **`task-rescue` § "Valid sidecar `step` states"** — Only the mirror sentence changed. Joined, it reads: "This table mirrors the orchestrator's accepted set of sidecar `step` values — if it changes, update this table; do not let them diverge." This matches the pinned text exactly.
  - The closed-set sentence before it ("This is a **closed set** … never invents one.") is byte-identical.
  - The artifact-paths sentence after it is byte-identical, as are the table, the N = 1 paragraph, the silent-failure line, the test-mode line and the always-valid guard.
  - The re-wrapped lines stay within the file's existing width of about 88 columns.
- **"it" antecedent** — In the new `task-rescue` sentence, "it" refers to "the orchestrator's accepted set of sidecar `step` values". This is unambiguous and is the spec's own wording.
- **Sweep** — I re-ran the spec's greps over `src`:
  - `orchestrator/`, `_validate_sidecar_step` and `_detect_task_step` return nothing.
  - `\.py` returns only `ui-ux-pro-max`'s invocations of its own `scripts/search.py`, plus that skill's own script files. These stay true.
  - Neither edited skill appears in the results.
- **Wider check** — Over `src`, `docs`, `CLAUDE.md` and `ARCHITECTURE.md`, `resume.py`, `main.py` and `agents.py` appear only in `docs/the-pipeline-speaks-to-an-architect.md`. That is a doc, and per the spec a doc may name a sibling repository's path. No text elsewhere refers to the removed file list in § 7.
- **Frontmatter** — The `description:` field of both skills is unchanged. Neither names an orchestrator source.
- **Runtime impact** — None. These are prose-only edits to skill bodies. The closed set of `step` values and every protocol token (`PLAN_REVIEW_PASS`, step literals, artifact paths) is untouched.

### Critical Issues
None.

### Positive Notes
- The edits are minimal and surgical. Each one replaces exactly the pinned sentence, and every neighbouring sentence stays byte-identical.
- The invariant itself is preserved. It now says to change this file in lockstep, without a citation that can rot.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/0248-the-skills-mirror-the-orchestrators-protocol-without-citing-its-source.md` — In the spec's "What breaks on contact" section, the **Finding** paragraph places the `task-rescue` mirror sentence "after the valid-states table". In the file, the sentence is in the paragraph that opens § "Valid sidecar `step` states", before the table. The implementation followed the file, so the edit is correct. Only the spec's prose is inaccurate, and that is outside this task's file boundary.

REVIEW_PASS

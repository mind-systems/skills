## Code Review Summary

**Files Reviewed:** 1 plan (it targets `src/skills/task-rescue/SKILL.md`). Also read the task spec `0243-…`, the phase note `0242-…`, roadmap line 84.1 in `.ai-factory/roadmaps/trickster77777.md`, and `orchestrator-artifacts` § "3. Sidecar fields".
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture (`.ai-factory/ARCHITECTURE.md`):** OK. The change stays inside one lens skill (`task-rescue`). It adds no `loads:` edge and edits no engine. `orchestrator-artifacts` is read but not edited, which matches the spec's Finding. Task 84.2 handles that engine's lockstep separately.
- **Rules (`.ai-factory/RULES.md`):** WARN. The file is not present, so there are no explicit conventions to check against.
- **Roadmap:** OK. The plan heading `84.1 — the capture records the session ids and the report names them` matches the open line in `.ai-factory/roadmaps/trickster77777.md` under Phase 84. That line's `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0243-…`, which the plan names. The phase note `0242-…` says no `docs/` governing spec covers this, so the task spec is the authority.
- **Spec conformance:** I checked every after-text in the plan against § "What must be true after":
  - The lead sentence matches the spec exactly.
  - The `step`/`elapsed` bullet matches exactly.
  - The new session-ids bullet matches exactly.
  - The clause in "Where the sidecar lives" matches exactly.
  - The "No sidecar on disk" bullet matches exactly.
  - The `**Sessions:**` template line matches. The plan escapes its inner backticks inside an inline code span, but it also tells the implementer to copy the spec's text verbatim, and the spec renders the line unescaped.

  The insertion points also match the spec: the new bullet goes directly after the `step`/`elapsed` bullet, and the template line goes directly after `**Elapsed before the rescue:**`.
- **Ground truth check:** The plan's "before" texts match the file as it stands:
  - The capture paragraph (lead sentence, bullets, the "both numbers" clause).
  - The Step 5.7 template's four header lines.

  The bold lead "**Capture the report facts.**" is kept, and the Project and Date bullets are left alone, both correctly.
- **Blast radius:** I ran the spec's sweep over `src docs CLAUDE.md` on the current tree. It gives the hits the spec's Finding predicts:
  - The Step 1 paragraph.
  - The Step 5.7 template.
  - The dropped-key sentence in Step 5 spec depth.
  - The `planner`/`elapsed` preservation lines in the spec+plan and plan-ratified procedures.
  - The "What NOT to do" bullet.
  - `orchestrator-artifacts` § 3.

  The sweep finds nothing in `docs/` or `CLAUDE.md`. An extra search for `four facts` hits only the target line, which the plan rewrites. The plan's expected post-edit results (`fields worth`, `both numbers` → empty) are correct.

### Critical Issues
None.

### Positive Notes
- The plan copies the pinned texts from the spec and does not paraphrase them. It names each edit by the bullet's bold lead and by section heading, never by line number.
- Edit 4 is scoped well: only the closing clause of the "Where the sidecar lives" bullet changes, and the named-roadmap stem text is protected.
- The plan correctly leaves the body-length issue alone. The body is already about 700 lines, over the 500-line guideline, but splitting it is outside this task, so the plan doesn't fold an unrelated refactor into a two-line semantic change.
- The verification task is read-only and checks against the spec's own Finding. It does not create a second list of what is expected to survive.

PLAN_REVIEW_PASS

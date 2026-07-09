## Plan Review — command-handoff: boundary-neutral framing + first-class narrative register

**Plan:** `.ai-factory/plans/60-command-handoff-boundary-neutral-framing-first-class-narrative-register.md`
**Governing spec:** `.ai-factory/specs/14-handoff-narrative-register-boundary-neutral.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The change is a single-file edit to an existing hosted slash command under `src/commands/`. No boundary or dependency shift; `command-handoff` still loads `note` and keeps `note` as the distiller engine for skeleton+note (composition model preserved — narrative-writes-directly is deliberately routed *around* the distiller, which the spec justifies). No violation.
- **Rules** (`.ai-factory/RULES.md`): WARN — file not present; nothing to enforce.
- **Roadmap** (`.ai-factory/ROADMAP.md`): OK. Milestone is line 131 (`[ ] command-handoff: boundary-neutral framing + first-class narrative register`), and its `Spec:` tag resolves to `.ai-factory/specs/14-…`, which the plan follows facet-by-facet. Line citations in the plan (`:3-7`, `:54-55`, `:13-18`, `:46`, `:48`, `:110`, `:136`) were checked against the live file and all resolve to the intended text. `grep -ni compact` confirms the four compact sites the plan targets (`:4`, `:5`, `:54`, `:136`) — the description rewrite (Task 1) covers `:4-5`.

### Critical Issues

**1. Stale "How Steps 1–2 apply per mode" paragraph (`:18`) will contradict narrative+note (Tasks 3–5).**
Line 18 currently states, in destination-only terms: *"In **note mode**, Steps 1–2 instead define the lens and blank skeleton that `note` executes in Step 3 — the agent does not mine the session or populate the skeleton itself here."* Task 5 makes **narrative + note** the exact opposite — the agent mines and composes the prose *itself* and `Write`s it directly, explicitly **not** through `note`. Task 3's scope is `:13-18`, but its instruction is only "add the register axis, keep the destination determination unchanged"; it never calls out reconciling this mining-responsibility paragraph with the new register. An implementer following the task literally can leave `:18` asserting "note mode → agent does not mine," which directly contradicts the behavior Task 5 introduces and would leave the skill internally inconsistent about who mines in narrative+note. This is inside the milestone's file boundary and inside the very block Task 3 edits, so it is a finding, not a deferral. **Fix:** have Task 3 (or Task 5) explicitly restate the `:18` paragraph as register-aware — mining/composition happens in the agent for chat destination *and* for narrative+note; only skeleton+note delegates mining to `note`.

### Minor Issues

**2. Narrative direct-write numbering is underspecified (Task 5).**
Task 5 says the agent Writes to `.ai-factory/handoffs/<NN>-<slug>.md` using "existing numbering/slug mechanics," but today those mechanics live inside `note` (Step 3 delegates `<NN>` derivation to it). On the direct-write path there is no `note` call, so the emitted skill text must itself tell the running agent how to compute `<NN>` (scan `.ai-factory/handoffs/`, take max + 1) — the granted `Bash(ls *)`/`Glob` tools make this feasible, but the instruction has to exist. The spec uses the same "existing mechanics" phrasing, so this is inherited rather than a plan defect, but the implemented Step 3 narrative branch should spell the numbering step out rather than gesture at a mechanic that only `note` currently owns.

**3. `argument-hint: "[note]"` is not revisited.**
The register axis introduces explicit user cues (`narrative` / `повествование` / `story`, "not the numbered skeleton"). The plan leaves `argument-hint` as `[note]`. This is optional (the spec does not require it and cues may arrive in the conversation rather than the argument), but since the milestone touches this file's frontmatter surface anyway, updating the hint to advertise the narrative cue would be consistent with making narrative a first-class register.

### Positive Notes
- The plan faithfully preserves the spec's hard guards: skeleton register byte-identical (section names/order, proportionality `:46`, read-first-map `:48`, self-check `:110`), register kept **orthogonal** to destination (no four-way enum collapse), and the "mine while context is live" timing truth retained while only compact-exclusivity is dropped.
- Correct call that no `allowed-tools` change is needed — verified: `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` already covers direct narrative writes and the `note` delegation.
- Anti-taxonomy instruction (Tasks 1–2: "enumerate no boundary kinds") correctly transcribes the spec's warning that a replacement taxonomy re-introduces the same over-fit — a subtle point the plan did not flatten.
- Task dependencies (3→4→5) and the two-commit split (Facet A, then Facet B) match the facet structure and satisfy the global commit-message rules (imperative, sentence case, no type prefix).

## Deferred observations
- Affects: unknown / receiving-agent behavior — The spec's motivating failure was a *receiving* agent narrating a false "we had a compact" premise. This plan correctly removes the false assertion at the source (the emitted handoff), which is the right and sufficient fix within this milestone's boundary; no change to any consuming skill is warranted here. Noted only so a future reader does not expect downstream edits.

Finding 1 above is a genuine internal-consistency gap within the edited block, so this review does not pass.

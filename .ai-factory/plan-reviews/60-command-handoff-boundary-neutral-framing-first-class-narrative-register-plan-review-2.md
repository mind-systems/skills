## Plan Review 2 — command-handoff: boundary-neutral framing + first-class narrative register

**Plan:** `.ai-factory/plans/60-command-handoff-boundary-neutral-framing-first-class-narrative-register.md`
**Governing spec:** `.ai-factory/specs/14-handoff-narrative-register-boundary-neutral.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Prior review:** `…-plan-review-1.md`
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. Single-file edit to a hosted slash command under `src/commands/`. The composition model is preserved — `command-handoff` still `loads: note` and keeps `note` as the distiller for skeleton+note; the narrative-writes-directly path is deliberately routed *around* the distiller, which the spec justifies (distillation flattens the causal thread). No boundary or dependency shift.
- **Rules** (`.ai-factory/RULES.md`): WARN — file not present; nothing to enforce.
- **Roadmap** (`.ai-factory/ROADMAP.md`): OK. Milestone is line 131; its `Spec:` tag resolves to `.ai-factory/specs/14-…`, which the plan follows facet-by-facet. All line citations (`:3-7`, `:8`, `:13-18`, `:46`, `:48`, `:54-55`, `:110`, `:136`) were checked against the live file and resolve to the intended text. `grep -ni compact` confirms the four compact sites the plan targets (`:4`, `:5`, `:54`, `:136`).

### Prior-review findings — all resolved
- **Review-1 Finding 1** (stale `:18` mining-responsibility paragraph): resolved. Task 3 now carries an explicit **"Reconcile the mining-responsibility paragraph (`:18`)"** instruction making it register-aware (agent mines for chat + narrative+note; only skeleton+note delegates to `note`).
- **Review-1 Minor 2** (narrative direct-write numbering underspecified): resolved. Task 5 now spells out the `<NN>` derivation in the emitted skill text (scan `.ai-factory/handoffs/` via `Bash(ls *)`/`Glob`, max prefix + 1, zero-padded) and the semantic `<slug>` rule (≠ literal "handoff").
- **Review-1 Minor 3** (`argument-hint` not revisited): resolved. Task 1 now updates `argument-hint: "[note]"` → advertise the narrative cue (e.g. `"[note] [narrative]"`).

### Critical Issues

**1. A second, identical stale note-mode paragraph at `:108` is not reconciled — the same defect review-1 blocked on, surviving in Step 2.**
The "note mode → agent does not mine/populate, `note` does" claim occurs in *three* places, keyed on the old note/chat **destination** binary. Two are handled: `:18` by Task 3's explicit reconciliation, and `:118` by Task 5's register×destination re-partition of Step 3. The third — line 108 — is missed:

> **Note mode:** do not populate the skeleton here — pass it blank to `note` in Step 3; `note` performs the mining and population itself.

Under **narrative + note**, the agent composes the prose *itself* and `Write`s it directly (Task 5) — it does **not** pass anything blank to `note`. So `:108`, exactly like the `:18` paragraph the plan carefully fixed, will contradict the narrative+note behavior once Facet B lands. Line 108 is inside Step 2, i.e. inside Task 4's edit block, but Task 4's only Step-2 instructions are "add a narrative path alongside the skeleton" and "guard `:46`/`:48`/`:110` byte-identical" — `:108` is neither protected nor flagged for reconciliation, so an implementer following the task literally leaves it asserting "note mode → agent does not populate." This is the identical internal-consistency class review-1 treated as blocking, within the milestone's file boundary, so it is a finding, not a deferral. **Fix:** add to Task 4 (or Task 5) an explicit instruction to restate the `:108` paragraph as register-aware, mirroring the `:18` reconciliation — the agent composes/populates itself for chat (either register) and for narrative+note; only skeleton+note passes the blank skeleton to `note`.

### Minor Issues

**2. Paste-back pointer for the narrative + note branch is unspecified in Task 5.**
Step 3's paste-back-pointer emission (`:125-139`) is written for today's note mode, and the self-check gate at `:110` (which Task 4 guards byte-identical) already asserts that in note mode "the chat pointer is intentionally minimal … and is exempt from the proportionality gate." Task 5 describes the narrative+note *file write* but is silent on whether that branch still emits the minimal paste-back pointer. Leaving it implicit risks the narrative+note path either double-emitting the full prose to chat or emitting nothing. Recommend Task 5 state that narrative+note also ends with the same minimal paste-back pointer (path + one-line frame + next step), consistent with `:110` and the existing skeleton+note pointer.

### Positive Notes
- The revision closes all three review-1 findings cleanly and with the right owner (the `:18` reconciliation lives inside Task 3's own edit block, not deferred).
- Hard guards from the spec are faithfully preserved: skeleton register byte-identical (section names/order, proportionality `:46`, read-first-map `:48`, self-check `:110`), register kept **orthogonal** to destination (no four-way enum collapse), and the "mine while context is live" timing truth retained while only compact-exclusivity is dropped.
- Anti-taxonomy instruction (Tasks 1–2: enumerate no boundary kinds) correctly transcribes the spec's warning that a replacement taxonomy re-introduces the same over-fit.
- Correct call that no `allowed-tools` change is needed — `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` already covers both the direct narrative write and the `note` delegation.
- Task dependencies (3→4→5) and the two-commit split (Facet A, then Facet B) match the facet structure and satisfy the global commit-message rules (imperative, sentence case, no type prefix).

Finding 1 is a genuine internal-consistency gap — the exact twin of the paragraph review-1 required reconciling, left unaddressed at `:108` — so this review does not pass.

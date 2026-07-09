## Plan Review 3 — command-handoff: boundary-neutral framing + first-class narrative register

**Plan:** `.ai-factory/plans/60-command-handoff-boundary-neutral-framing-first-class-narrative-register.md`
**Governing spec:** `.ai-factory/specs/14-handoff-narrative-register-boundary-neutral.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Prior reviews:** `…-plan-review-1.md`, `…-plan-review-2.md`
**Files Reviewed:** 1 (plan) against 1 target + spec + roadmap
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. Single-file edit to a hosted slash command under `src/commands/`. Composition model preserved — `command-handoff` still `loads: note` and keeps `note` as the distiller for skeleton+note; the narrative-writes-directly path is deliberately routed *around* the distiller, which the spec justifies (distillation flattens the causal thread the narrative exists to carry). No boundary or dependency shift.
- **Rules** (`.ai-factory/RULES.md`): WARN — file not present; nothing to enforce.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): WARN — not present; no project-specific overrides to apply.
- **Roadmap** (`.ai-factory/ROADMAP.md`): OK. Milestone is line 131; its `Spec:` tag resolves to `.ai-factory/specs/14-…`, which the plan follows facet-by-facet. All line citations (`:3-7`, `:8`, `:13-18`, `:46`, `:48`, `:54-55`, `:108`, `:110`, `:125-139`, `:136`) were re-checked against the live file and resolve to the intended text. `grep -ni compact` confirms exactly the four compact sites the plan targets (`:4`, `:5`, `:54`, `:136`), all removed by Tasks 1–2.

### Prior-review findings — all resolved
- **Review-1 Finding 1** (stale `:18` mining-responsibility paragraph): resolved. Task 3 carries an explicit **"Reconcile the mining-responsibility paragraph (`:18`)"** instruction, register-aware (agent mines for chat destination either register + narrative+note; only skeleton+note delegates to `note`).
- **Review-1 Minor 2** (narrative direct-write numbering underspecified): resolved. Task 5 spells the `<NN>` derivation into the emitted skill text — scan `.ai-factory/handoffs/` via granted `Bash(ls *)`/`Glob`, max numeric prefix + 1, zero-padded to match existing files; semantic `<slug>` ≠ literal "handoff".
- **Review-1 Minor 3** (`argument-hint` not revisited): resolved. Task 1 updates `argument-hint: "[note]"` → `"[note] [narrative]"` (brackets quoted, per the skill-authoring constraint).
- **Review-2 Finding 1** (twin stale note-mode paragraph at `:108` unreconciled): resolved. Task 4 now carries an explicit **"Reconcile the second note-mode paragraph (`:108`)"** instruction mirroring the `:18` fix, correctly noting `:108` is inside Task 4's Step-2 block and is *not* among the byte-identical guards (`:46`/`:48`/`:110`).
- **Review-2 Minor 2** (paste-back pointer for narrative+note unspecified): resolved. Task 5 states narrative+note ends with the **same minimal paste-back pointer** the skeleton+note path emits (`:125-139`: path + one-line frame + next step, optional work-unit count), one chat block, consistent with the `:110` exemption.

### Verification of the current revision
- Line 108 (`**Note mode:** do not populate the skeleton here…`) and line 18 (`**How Steps 1–2 apply per mode:**…`) are confirmed as the two destination-keyed twins; Tasks 3 and 4 reconcile them in their respective edit blocks — no third stale twin remains (`:118` is re-partitioned by Task 5's Step-3 rewrite).
- The byte-identical skeleton guard is coherent: `:110` is phrased in destination terms ("in note mode … applies to the content written to the note file; the chat pointer is intentionally minimal"), so it stays valid across both registers without edit — narrative+note still writes to a note file and still emits only the minimal pointer. Keeping it untouched introduces no contradiction.
- Task 2's edit of `:54-55` (Frame line) and `:136` (example pointer) does not collide with Task 4's guard, which lists `:46`/`:48`/`:110` and section names/order — not `:54-55`. This matches spec verify-point 4 ("skeleton unchanged apart from the Facet-A wording edits and the new register-axis prose").
- No `allowed-tools` change needed — `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` already covers both the direct narrative `Write` (into an existing `.ai-factory/handoffs/` dir) and the `note` delegation. Confirmed against the live frontmatter.
- Commit split (Facet A = tasks 1–2, Facet B = tasks 3–5) and task dependencies (2→3→4→5) match the facet structure; commit messages are imperative, sentence case, no type prefix — compliant with the global commit rules.

### Positive Notes
- The revision closes both review-2 findings with the correct owner: the `:108` reconciliation lands inside Task 4's own Step-2 edit block, not deferred — the same discipline review-1's `:18` fix set.
- Spec hard-guards faithfully preserved: skeleton register byte-identical (section names/order, proportionality `:46`, read-first-map `:48`, self-check `:110`); register kept **orthogonal** to destination (no four-way enum collapse); the "mine while context is live" timing truth retained while only compact-exclusivity is dropped.
- Anti-taxonomy instruction (Tasks 1–2: enumerate no boundary kinds) correctly transcribes the spec's warning that a replacement taxonomy re-introduces the same over-fit in longer form.
- Task 5 correctly justifies routing narrative+note *around* `note` (distillation would flatten the causal thread) and closes the numbering mechanic that `note` normally owns, so the direct-write path is fully self-contained.

The plan faithfully implements both facets of spec 14, every line citation resolves against the live file, all guards are preserved, and all five prior-review findings (three from review-1, two from review-2) are resolved within the milestone's file boundary. No new gaps found.

PLAN_REVIEW_PASS

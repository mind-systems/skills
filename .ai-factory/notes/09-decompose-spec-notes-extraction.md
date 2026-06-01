---
name: roadmap-decompose two-tier output (summary tasks + per-task spec notes)
description: roadmap-decompose must always keep ROADMAP.md as one-line summary tasks and push each full spec into its own .ai-factory/notes/<NN>-task-<slug>.md
type: project
---

# roadmap-decompose: Two-Tier Output — Summary Tasks in the Roadmap, Full Specs in Per-Task Notes

**Date:** 2026-05-31
**Source:** conversation context (validated in practice on a real 14-task backlog before writing this requirement)

## Key Findings

- Today the skill writes the **full spec inline** in each `ROADMAP.md` bullet. With detailed specs (current-state + target + guards + files), the roadmap becomes a wall of multi-hundred-word bullets — unscannable, and every spec edit churns the roadmap diff.
- **New required behavior:** the skill must ALWAYS produce a **two-tier output**:
  1. `ROADMAP.md` holds only a **one-line summary** per task (checkbox + bold name + 1–2 sentence what/why) ending with a tag pointing to its spec note.
  2. The **full spec** for each task lives in its own note file `.ai-factory/notes/<NN>-task-<slug>.md`.
- This is not an option or a mode — it is the default and only output shape for every task the skill creates, rewrites, or decomposes.
- The Atomicity Gate is unchanged in intent but now runs on the **full spec (in the note)**; the summary line is derived after the gate passes.
- Validated in practice: a 12+2 task backlog rendered as one-line summaries in the roadmap with 14 companion spec notes is dramatically more scannable, and `/aif-plan` / `/aif-implement` can load exactly one note per task instead of re-reading the whole roadmap.

## Details

### The two tiers

**Tier 1 — `ROADMAP.md` summary line (the only thing in the roadmap):**

```
- [ ] **<Task Name>** — <descriptive summary: the problem today + the change + key files or types involved>. Spec: `.ai-factory/notes/<NN>-task-<slug>.md`.
```

Rules:
- Keep the existing `- [ ]` / `- [x]` checkbox and `**bold name**`.
- The summary should be descriptive enough that a reader can understand scope and intent without opening the note. Name the key files, types, or methods involved. **Target length: 400–700 characters; up to ~1000 is fine when the task genuinely warrants it.** What to leave out: numbered step-by-step implementation, exhaustive guard lists, test-case enumerations — those live in the note.
- Always end with the exact tag form: `Spec: \`.ai-factory/notes/<NN>-task-<slug>.md\`.`
- Phase/section headings and their short intro paragraphs stay in the roadmap as today.

**Tier 2 — per-task spec note (`.ai-factory/notes/<NN>-task-<slug>.md`):**

Fixed template — emit these sections verbatim (omit a section only if genuinely empty):

```markdown
# Task Spec — <Task Name>

**Date:** <YYYY-MM-DD>
**Roadmap:** ROADMAP.md <Phase / section name>
**Provenance:** <where this task came from — review note, requirement, user request>

## Current state
<What exists today and what's wrong or missing. Name specific files, methods, types, fields.>

## Target
<Exact change: files/methods/types to touch, the behavior to implement, numbered steps if multi-step.>

## Guards
<Real pitfalls only — ordering constraints, "must live in X not Y", "do not auto-Z", backward-compat. Skip the obvious.>

## Files
<Bullet list of files to create/modify.>

## Verify
<Optional. How to confirm it works — on-device test, scenario to exercise. Omit if trivial.>
```

### Naming and numbering of the note

- `<NN>` = the next sequential two-digit prefix in `.ai-factory/notes/`, found by scanning existing `[0-9][0-9]-*.md` and incrementing the highest (identical rule to `aif-note`). One note per task. Never reuse a number.
- Notes live in `.ai-factory/notes/` alongside the target roadmap's `.ai-factory/` dir — for both `ROADMAP.md` and `ROADMAP_TESTS.md`, notes go to the same `.ai-factory/notes/`.
- `<slug>` = kebab-case of the task name, prefixed with `task-` for grep-ability (e.g. `46-task-meditation-stop-reset.md`).
- Ensure `.ai-factory/notes/` exists (`mkdir -p`) before writing.

### Operation order (per task)

1. Draft the **full spec**.
2. Apply the **Atomicity Gate** to the full spec. If it splits, each resulting half is its own task → its own note + its own summary line.
3. Allocate the next `<NN>`, write the spec note.
4. Write the **summary line** to the roadmap with the `Spec:` tag pointing at the note just written.

Allocate numbers sequentially across all tasks generated in one run so two tasks never collide on `<NN>`.

### Where to change the skill (SKILL.md)

- **Mode 1, Step 1.3 (Generate roadmap file):** generating the initial roadmap now writes, per milestone, a summary line in `ROADMAP.md` + a full spec note. The "Generate roadmap file" body and its example must show the summary+tag form, not inline specs.
- **Mode 2, Step 2.4 (Add New Tasks):** each new task → summary line + spec note.
- **Mode 2, Step 2.5 (Decompose Existing):** this step's whole purpose now maps cleanly to the model — "decompose" = write the full spec into a NEW per-task note and replace the roadmap bullet with the summary + tag. If the selected milestone was already a short summary with a note, expand/update the note, not the roadmap line.
- **"Roadmap File Format" section:** replace the inline-full-spec example with the two-tier format — show both the `ROADMAP.md` summary line and the `.ai-factory/notes/<NN>-task-<slug>.md` template above. Rename the "Rules for writing a description" guidance to apply to the **note's `## Target`**, not the roadmap line.
- **"Critical Rules":** add a rule: *"Every task is two-tier — a one-line summary in the roadmap and a full spec in `.ai-factory/notes/<NN>-task-<slug>.md`. Never write a full spec inline in the roadmap."*

### Interaction with other skill steps

- **Atomicity Gate (1.3.1 / 2.4.1):** unchanged logic; runs on the full spec in the note. A split produces two notes + two summary lines.
- **Mode 3 (`/decompose check`):** unaffected — it only flips `[ ]`→`[x]` on the summary line. The spec note stays as the historical record.
- **roadmap-prune:** when it groups completed `[x]` summaries into ARCHITECTURE.md, the per-task spec notes remain in `.ai-factory/notes/` as the durable spec history (prune does not delete them). Optional future nicety: prune could reference the note path in its ARCHITECTURE.md anchor.
- **aif-plan / aif-implement:** these consume a single task by reading its spec note directly — the summary line's `Spec:` tag is the pointer. This is the main payoff: one task = one self-contained spec file.

### Migration of existing roadmaps

- Going forward, ANY task the skill creates, rewrites, or decomposes is emitted two-tier.
- Do NOT bulk-rewrite pre-existing legacy inline-spec tasks just because the skill ran — that would churn unrelated roadmap history. Migrate an inline task to two-tier only when the skill is already touching that specific task (decompose/update), or when the user explicitly asks to convert the whole file.

### Concrete before/after

**Before (current skill output — full spec inline):**
```
- [ ] **Cap the gRPC reconnect backoff exponent** — `lib/Core/Grpc/GrpcConnectionManager._nextDelay()` computes `base = _initialDelay * math.pow(2, _reconnectAttempt)` and clamps only the result; `_reconnectAttempt` is unbounded ... [200+ words of spec] ...
```

**After (required output — summary + note):**

`ROADMAP.md`:
```
- [ ] **Cap the gRPC reconnect backoff exponent** — `GrpcConnectionManager._nextDelay()` computes `base = _initialDelay * pow(2, _reconnectAttempt)` with no cap on the exponent; on a long outage `_reconnectAttempt` grows unbounded and eventually overflows `Duration`. Clamp the exponent at source: `final exp = math.min(_reconnectAttempt, 6)`. Leave the increment for the log line — the cap applies only to the delay calculation. Spec: `.ai-factory/notes/49-task-grpc-backoff-exponent-cap.md`.
```

`.ai-factory/notes/49-task-grpc-backoff-exponent-cap.md`:
```markdown
# Task Spec — Cap the gRPC reconnect backoff exponent

**Date:** 2026-05-31
**Roadmap:** ROADMAP.md Phase 26
**Provenance:** code review finding

## Current state
`GrpcConnectionManager._nextDelay()` computes `base = _initialDelay * math.pow(2, _reconnectAttempt)` and clamps only the result; `_reconnectAttempt` is unbounded ...

## Target
Clamp the exponent at the source: `final exp = math.min(_reconnectAttempt, 6); ...`

## Guards
Leave the `_reconnectAttempt++` increment for the log line.

## Files
- `lib/Core/Grpc/GrpcConnectionManager.dart`
```

## Why (rationale)

- **Scannable backlog:** the whole roadmap reads as a one-line-per-task list — easy to see scope, count, order, and prioritize.
- **No diff churn:** revising a spec edits its note, not the roadmap; the roadmap diff only changes when tasks are added/removed/reordered/checked.
- **Self-contained task units:** `/aif-plan` and `/aif-implement` load exactly one spec note per task instead of scrolling a giant roadmap.
- **Durable spec history:** notes survive `roadmap-prune`, preserving the full rationale after the summary is archived.

## Rejected alternatives

- **Keep full specs inline (status quo):** rejected — unscannable roadmap, heavy diffs, specs and the backlog index conflated.
- **One big sidecar spec file for all tasks:** rejected — reintroduces a wall of text and couples unrelated task edits in one file/diff. One note per task is the unit.

## Open Questions

- Should the per-task note carry frontmatter (`name`/`description`/`type`) like project notes, or stay frontmatter-free as a plain spec doc? (Practice used frontmatter-free `# Task Spec — …`; either is fine — pick one and state it in SKILL.md.)
- Should `/decompose check` optionally flag legacy inline-spec tasks and offer to migrate them to two-tier?

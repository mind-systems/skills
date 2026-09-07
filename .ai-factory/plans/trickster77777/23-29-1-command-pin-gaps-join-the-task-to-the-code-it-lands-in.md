# Plan: 29.1 — command-pin-gaps: join the task to the code it lands in

## Context
`src/commands/command-pin-gaps.md` asks where an implementing agent would have to invent, but asks it of the artifact's text alone — nothing walks the transformation from the governing spec through the task into the code it lands in. This task rewrites that one file in place so the pass reads the code to the leaf, emulates what the orchestrator will do with the task, adds blast-radius as a third finding class, and routes what it may not close to a named owner.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Grounding

- [x] **Read the ground truth before writing a line**
  Files: `src/commands/command-pin-gaps.md`, `docs/sakshi-harness/skill-cycle.md`, `src/global/CLAUDE.md`
  Read the target file in full (26 lines: frontmatter `:1-12`, engine-load `:14-15`, target resolution `:17`, premise `:19`, value holes `:21`, meaning holes `:23`, scan mode `:25`, default mode `:26`). Read `docs/sakshi-harness/skill-cycle.md` § "Пины — `command-pin-gaps`" (`:37-41`) — per `CLAUDE.md:33` it is the authoritative home of the cycle's order and states this command's target behavior in present tense; it is the text this task is executed against and **is never edited by this task**. Read `src/global/CLAUDE.md` § "Grounding claims" for the direction change moves in (docs → roadmap → code) and the walk-to-the-leaf discipline — those two facts, and only those two, carry into the new body's reasoning, and both are already resident in every session, so the command fetches nothing. Do **not** carry into the file either of two rules that live elsewhere in that same always-loaded file: § "Documentation style" `:27` ("Docs form a walkable tree"), which states "A fact's second home is always a link to its first, never a copy", and § "Project CLAUDE.md authoring" `:31` ("**One home per fact.** Anything stated in two places will drift."). Neither sits in § "Grounding claims" — verify each at the line named before relying on it. At this tier the spec overrides both, and the step below states the override.
  Capture the byte-exact `allowed-tools:` and `loads:` lines with `git show HEAD:src/commands/command-pin-gaps.md` — they must survive the rewrite unchanged, whatever line numbers they end up on.
  Confirmed reconnaissance, no action needed: no file under `src/` invokes this command, and the three docs that mention it (`docs/skill-description-field.md:13`, `docs/sakshi-harness/skill-graph.md:49`, `CLAUDE.md:33`) reference it by name only — none quotes its `description:`, so none needs updating.

### Frontmatter

- [x] **Rewrite the `description:` block; move nothing else in the frontmatter** (depends on Read the ground truth)
  Files: `src/commands/command-pin-gaps.md`
  The `description:` is always-loaded contract, not a summary — a capability absent from it is one the invoking agent may never learn exists. Rewrite `:2-8` so it names all three finding classes (value, meaning, blast-radius) and states that the command walks the task's transformation into the code it lands in; keep the `scan` mode sentence. `argument-hint:` (`:9`), `allowed-tools:` (`:10`) and `loads:` (`:11`) stay byte-identical to `HEAD`. No `Write`, no `AskUserQuestion`, no `Agent` in the tool grant; `loads:` stays exactly `roadmap-engine`.
  Measure the block, do not estimate: `wc -m` in a UTF-8 locale over the block's text — it must be ≤ 1024 characters (the cap `CLAUDE.md:115` sets). It holds about 420 today, so there is room.

### Body

- [x] **Keep the container and the question; add the walk** (depends on Rewrite the `description:` block)
  Files: `src/commands/command-pin-gaps.md`
  Keep `:14-15` (load `roadmap-engine` once) and `:17` (target resolution order) as they are — the container does not change. Keep the premise at `:19` verbatim in force: any question needing an answer during implementation is space to fantasize. It is the identity; what follows is a method for answering it, never a replacement, and no pass/fail verdict displaces the finding list.
  Add the walk: the command reads the task, its task spec, and the code the task lands in, following named references to the leaf, depth along named edges and never a sweep across unrelated branches. It then walks what the orchestrator will do with the task — how the planner would build a plan for it against this code, and how the reviewer would judge the implementation that comes back. State explicitly that this emulation is a way of reasoning toward the finding list: it produces no plan and no verdict. Carry no orchestrator prompt into the file and name none.
  State the unit of the walk: one behavior the task claims. Each such behavior either ends at a `file:line` landing in the code or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question.
  State the two questions that decide a finding: would the run, holding this task and nothing else, have to invent — and can the task be implemented on the code that exists at all.
  State the boundary: the pass does not locate the phase, does not read the pointers on its header, and reports nothing about their presence or absence — that tier belongs to `roadmap-outline-deep` and `roadmap-decompose`. The tokens `Governing spec:` and `Phase note:` must not appear anywhere in the file.
  State that reading a document to understand the task is ordinary and needs no branch of its own, exactly as the orchestrator reads one when it needs one.
  State where the weight of the pass sits: the code side — nothing in the family has looked there until now.

- [x] **State the two ends of a hole and the direction change moves in** (depends on Keep the container and the question)
  Files: `src/commands/command-pin-gaps.md`
  A task states how the docs currently differ from the code and what it will change; a hole is wherever that statement fails to connect. Write both ends. **Toward the code:** desired behavior with no landing — no file named, no call site, an existing shape it must fit that nobody looked at, work already half-done, something that breaks on contact. Say plainly that this end is the one no other skill owns. **Toward the docs:** behavior the task assumes that no document states, because it surfaced during decomposition rather than during specification — the hole is then in the governing spec, not in the task, and the command points there.
  State the direction change moves in — docs → roadmap → code — as the reason the documentation is the foundation the code stands on, so behavior the task wants that no governing document describes is a hole like any other.
  State the counter-default exception, in the file itself: **a task spec that repeats a paragraph from a document instead of linking to it is not a finding.** An agent does not reliably walk to the leaf — it guesses a file's content from its name — so the copy earns its place; it goes stale, and that is proper to this tier, because the roadmap is the perishable seam between the documentation and the code, pruned as it closes, unlike the two surfaces it sits between. Without this sentence the produced command reports such a copy as a meaning hole to route to `aif-docs`, or as duplication to collapse, on every run — the global CLAUDE.md's link-never-copy rule is loaded in every session and points the other way, so the exception must be written, never left implicit.
  The two ends are **not** classes. Say so: every finding carries exactly one of the three classes; the end shows only in the repair — closed in place, or `owner: <skill>` in the scan line's `fix` token.

- [x] **Rewrite the three class paragraphs** (depends on State the two ends of a hole)
  Files: `src/commands/command-pin-gaps.md`
  Three paragraphs, all in the shape of today's `:21` and `:23` — a bold class name, the definition of what it looks for, then `Repair:`. The file grows no second register; `Repair:` appears exactly three times in the body.
  **Value holes** — keep the definition and the in-place repair of `:21` (pin the exact value from the code with a `file:line` citation, never invent). A missing file or call site is a value hole.
  **Meaning holes** — keep the definition and the in-place repair of `:23`; an existing shape nobody looked at, or work already half-done, is a meaning hole. Add the routed variant: a meaning hole whose constraint no document states is routed to `aif-docs` rather than written from the code. `## Blocking decisions` stays reserved for genuine product decisions and takes nothing else.
  **Blast-radius holes** (new, third) — what the repository already contains that this change breaks; something that breaks on contact is a blast-radius hole, stated in the same sentence shape as the other two mappings, since it is the one symptom of the toward-the-code end whose class has no prior usage a reader could lean on. `Repair:` a `Grep`/`rg` sweep whose **enumeration** goes into the task spec — never a sentence saying something may need updating. The repair verb is `Grep` or `rg`, never bare `grep`: `:10`'s grant allows `Bash(rg *)` and no bare `grep`. A contradiction that resolves against the code is closed in place; a fundamental conflict, or code that does not come apart, is raised as an explicit blocker instead of being quietly repaired. A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`, and never file it under `## Blocking decisions`.

- [x] **Name the owners; wield none** (depends on Rewrite the three class paragraphs)
  Files: `src/commands/command-pin-gaps.md`
  A task that cannot be planned coherently belongs to `roadmap-decompose` or `roadmap-decompose-skeleton`; behavior no document describes belongs to `aif-docs`; a surface that fails silently, by `test-philosophy`'s discriminator, owes a test. The command names which one and performs none: it does not decompose, does not write documentation, does not author tests, and loads none of the four — naming an owner needs no load, so no `loads:` entry is added and no instruction to invoke any of them appears. A hole it can close in place it closes, exactly as today; a hole whose repair belongs elsewhere is reported, in both modes.
  Also state, as the calibration behind two of these judgments: judging a task too large and judging a behavior undocumented are comparative — they are made where the whole roadmap is readable, which is where this command runs.

- [x] **Update both mode lines** (depends on Name the owners; wield none)
  Files: `src/commands/command-pin-gaps.md`
  **scan mode** (`:25`): the middle token carries all three classes, so the two-alternative form `value|meaning →` disappears from the file entirely. Describe the `fix` token's routed form: `owner: <skill>` for a hole whose repair belongs elsewhere.
  **default mode** (`:26`): the report line carries three counts — `N closed from source · M blocking · K owned elsewhere` — so a routed hole is counted rather than lost. The phrase `owned elsewhere` must appear.

### Verification

- [x] **Verify against the spec's checks, by the normalized method** (depends on Update both mode lines)
  Files: `src/commands/command-pin-gaps.md`
  Per the spec, take every count against a whitespace-normalized read of the file — never a line-oriented `grep` — with `**` normalized out of both sides before any quoted span is compared. No count is evidence until taken this way. Check: `allowed-tools:` and `loads:` byte-identical to `git show HEAD:src/commands/command-pin-gaps.md`; `Write`/`AskUserQuestion`/`Agent` absent from the tool grant (each 0); the string `orchestrator/` absent (0) and no path naming a file outside this repository; the direction docs → roadmap → code present (≥ 1); both ends of the hole present (each ≥ 1); all three class names inside the `description:` block (blast-radius and blast radius counted together, each ≥ 1) plus the statement that the command walks the task's transformation (≥ 1), block ≤ 1024 chars by `wc -m`; scan-mode middle token three alternatives and `value|meaning →` absent (0); all four owner skills named (each ≥ 1), no instruction to invoke any, none in `loads:`; `Repair:` exactly 3; default report's three counts with `owned elsewhere` (≥ 1); scan-mode `owner: <skill>` form (≥ 1); the phase-header-pointer boundary stated (≥ 1) with `Governing spec:` and `Phase note:` each 0; both halves of the emulation plus "no plan and no verdict" (each ≥ 1); the blocker rule and the ordinary-document-read rule (each ≥ 1); the oversized-sweep finding owned by `roadmap-decompose` (≥ 1).
  Two checks beyond the spec's list, guarding the guards: the file states that a task spec repeating a document's paragraph instead of linking to it is not a finding (≥ 1), and carries no rule telling the reader to collapse or route such a copy (0); and all three end→class mappings are stated explicitly — missing file or call site → value, existing shape nobody looked at or half-done work → meaning, breaks on contact → blast-radius (each ≥ 1).
  Scope check: the file still lives at `src/commands/command-pin-gaps.md`; no new file under `src/skills/`, no new symlink under `active/`; `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/commands/command-pin-gaps.md` and nothing else. Phase 28, task 28.1 and spec 102 are untouched.

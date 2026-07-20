# Plan: roadmap-test-coverage: give `$TEST_CMD` a first-class derivation rule and define Layer 7's no-command behavior

## Context

`$TEST_CMD` currently has no derivation rule of its own — it is read unconditionally from a closed four-manifest list (`src/skills/roadmap-test-coverage/SKILL.md` L49–54), none of which is a Python manifest, and Layer 7 executes it (L277) and re-runs it as a hard green gate (L333) with no behavior defined for the empty case. This task gives `$TEST_CMD` the same two-tier shape 20.1 gave `$STACK` (primary: the project's declared command; fallback: the unextended four-manifest sniff) and defines Layer 7 to skip the run and the gate — visibly — when no command resolves.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Grounding notes (read before implementing)

1. **`## Commands` has no pinned format.** The spec names "the `## Commands` table … the `Tests` row". Ground truth (`src/skills/aif/SKILL.md` L37) specifies only: `## Commands` (from the detected package manager or Makefile targets; leave light if no scaffolding exists yet). There is no mandated table, and no mandated `Tests` row label. **Therefore:** write the primary rule against the *section*, not a row shape — "the test command declared in the project's `CLAUDE.md` `## Commands` section" — with the table-row form (`| Tests | pytest |`) named as the typical shape, not as a parse contract. A rule that only matches a literal `Tests` table row would silently fall through on the majority of real `CLAUDE.md` files. (The spec's own wording overstates its upstream; that inaccuracy is filed as a deferred observation for a future spec pass and does not change this task.)

2. **The Layer 8 guard was narrowed in the spec; the skip does not go into `$HANDOFF_LIST`.** Plan review established that Layer 8 does not print `$HANDOFF_LIST` verbatim — L355 prints it "as concrete one-line task descriptions" through a fixed two-category structure (`Refactor:`, `Bugs (Class B — silent failures):`) closed by the invariant at L371–376, "Every handoff line resolves to a pointer; none are left blank." A skip entry belongs to neither category and has no pointer to resolve to (no Layer-4 note, no failing source file), so routing it there would collide with a stated invariant. The spec now resolves this: the skip is **logged in Layer 7** and surfaces as **one added line in Layer 8's counts block**, printed only on a skip. The spec's Guards were amended accordingly — Layer 8 is no longer byte-identical in the blanket sense; it takes exactly that one line, with the `$HANDOFF_LIST` print, both categories, and the pointer invariant untouched.

## Tasks

### Phase 1: `$TEST_CMD` derivation

- [x] **Task 1: Add `CLAUDE.md` to Layer 1's read list**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Layer 1's "Read in order (skip if absent)" list (L27–32) names only `.ai-factory/ARCHITECTURE.md` and the roadmap. Task 2's primary rule reads the project's `CLAUDE.md`, so add it to that list as an explicit input — one bullet, matching the existing bullets' voice, noting what it is read for (the declared test command in `## Commands`).

  Why this is needed here and was not in 20.1: `$STACK`'s primary source (`ARCHITECTURE.md`) was already in the read list, so 20.1 needed no addition; `$TEST_CMD`'s primary source is not. Do not rely on the ambient auto-loaded project `CLAUDE.md` — Layer 1 is an explicit read procedure, and the skill may run against a roadmap in a sub-repo whose `CLAUDE.md` is not the loaded one (this repo is a grove: root and each sub-repo have their own).

- [x] **Task 2: Replace the unconditional `$TEST_CMD` read with a two-tier rule** (depends on Task 1)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Rewrite the paragraph at L49–54 (`This resolution governs $STACK only … out of Cargo.toml`). Give `$TEST_CMD` a first-class rule mirroring the `$STACK` block's shape at L37–47 — numbered **Primary** / **Fallback**, same instruction voice, same sentence register:
  - **Primary** — the test command the project declares in its `CLAUDE.md` `## Commands` section (typically a table row such as `| Tests | pytest |`, but read the section for the declared test command whatever its shape — a list entry or a bare line counts). Take it verbatim.
  - **Fallback** — only when `CLAUDE.md` is absent, has no `## Commands` section, or that section declares no test command: read the same four manifests (`package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`) as today, e.g. `npm test` out of `package.json`'s scripts, `cargo test` out of `Cargo.toml`.
  - **Neither resolves** — `$TEST_CMD` is empty; state plainly that this is a defined state handled in Layer 7, not an error.

  Carry forward the never-extend rule explicitly: the four-manifest fallback list is never extended with per-language detectors — a project needing a command it cannot sniff declares it in `CLAUDE.md`. Keep the `$STACK` block (L37–47) byte-identical; the existing sentence fragment "the never-extend rule binds `$STACK` detection, not `$TEST_CMD`'s read" is now false and must go with the rewritten paragraph.

### Phase 2: Layer 7's no-command path

- [x] **Task 3: Guard the Layer 7 run and the green gate against an empty `$TEST_CMD`** (depends on Task 2)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Two edits inside Layer 7 (L273–333) only:
  - Ahead of the `<$TEST_CMD>` run block (L275–278): add the guard — when `$TEST_CMD` is empty, do not execute it. Treat the project as having no runnable existing-test suite: skip the run, skip the failure classification, skip the green gate, log it plainly (e.g. `No test command resolved — existing-test gate skipped`), and continue to Layer 8. Do **not** append anything to `$HANDOFF_LIST` — per grounding note 2, the skip is not a handoff task and has no pointer.
  - At the re-run gate (L333): scope it to the command-exists case — the "all tests must be green before Layer 8" gate applies only when `$TEST_CMD` resolved.

  Everything else in Layer 7 stays as it is: the Class A / Class B split, the `general-purpose` classifier prompt (L288–318), the Class A patch rule, and the existing Class B `$HANDOFF_LIST` append are untouched.

- [x] **Task 4: Surface the skip in Layer 8's counts block** (depends on Task 3)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Add one line to the counts block in Layer 8's printed template (L348–350, alongside `Refactor items handed off` / `Existing tests patched (API drift)` / `Class B items handed off`), e.g. `Existing-test gate: skipped (no test command resolved)`, and state that it prints only when Layer 7 skipped the gate. This is the whole of the Layer 8 change — the spec's amended guard allows exactly this one line.

  Touch nothing else in Layer 8: the `$HANDOFF_LIST` print instruction (L355–356), both category headings, the per-item pointer paragraph (L371–376), and `Next step: /roadmap-decompose` stay byte-identical.

- [x] **Task 5: Confirm the diff's scope against the guards** (depends on Task 4)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Run `git diff` on the file and confirm it touches exactly four regions: Layer 1's read list, the `$TEST_CMD` paragraph, Layer 7's empty-command handling, and Layer 8's one added counter line. Specifically verify: the `$STACK` resolution block is byte-identical to its post-20.1 state; Layers 2–6 are byte-identical; Layer 8's `$HANDOFF_LIST` machinery and pointer invariant are byte-identical; the four-manifest list is not extended; the `package.json` → `test`-script derivation still reads unchanged as the fallback. Frontmatter `allowed-tools` needs no change — the primary rule adds a `Read`, already granted at L10.

## Out of scope

Running the skill live on a Python project (the declared-command leg and the greenfield empty→skip leg) is the user's manual post-implementation check, explicitly not a pipeline obligation per the spec's verification note. Do not attempt it and do not report its absence as outstanding.

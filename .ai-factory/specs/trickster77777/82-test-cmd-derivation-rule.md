# roadmap-test-coverage: give `$TEST_CMD` a first-class derivation rule and define Layer 7's no-command behavior

Phase 20. Task 20.1 gave `$STACK` a declared-source primary (the project's own `ARCHITECTURE.md` Tech-stack line) with the four-manifest sniff as fallback, but it was scoped to `$STACK` only. Its sibling variable `$TEST_CMD` was left with no first-class rule — and the same closed-manifest-list bug 20.1 closed for `$STACK` still lives in `$TEST_CMD`, biting the exact projects 20.1 exists to serve. Surfaced as a deferred observation across 20.1's plan-review and code-review rounds ("belongs in its own task"), and confirmed live: `snake-core`, a Python/pytest project, resolves its stack from `ARCHITECTURE.md` but has none of the four manifests.

## Current state (grounded, verified live)

- `src/skills/roadmap-test-coverage/SKILL.md` Layer 1 stores `$STACK`, `$TEST_CMD`, `$ROADMAP_PATH` (:34). `$STACK` has a two-tier rule (primary: `ARCHITECTURE.md` `- **Tech stack:**` line; fallback: sniff `package.json`/`pubspec.yaml`/`go.mod`/`Cargo.toml`) — added by 20.1.
- `$TEST_CMD` has **no rule of its own**: the same block states "This resolution governs `$STACK` only … not `$TEST_CMD`'s read" and derives `$TEST_CMD` **solely** from the unconditional four-manifest read (:49–53: "still read the project's package manifest (the same four …) unconditionally for `$TEST_CMD`", e.g. `npm test` from `package.json`, `cargo test` from `Cargo.toml`). None of the four is a Python manifest, and there is no declared-source path and no rule for "none of the four exists".
- `$TEST_CMD` is consumed in Layer 7 (:277 "Run the test suite: `<$TEST_CMD>`") and re-run as a **hard gate** (:333 "Re-run `$TEST_CMD`. All tests must be green before Layer 8"). Layer 7 defines **no behavior for an empty `$TEST_CMD`** — it neither guards against it nor skips.
- **Failure shape:** a project with a filled `ARCHITECTURE.md` Tech-stack line and none of the four manifests (Python/pytest is the flagship case, and precisely what 20.1 targets) resolves `$STACK` correctly but leaves `$TEST_CMD` **empty**. Layer 7 then runs an empty command against a hard green gate — undefined behavior: the safety gate silently no-ops for exactly the stack 20.1 was built to support.

## Change

Two coupled edits to `$TEST_CMD`'s lifecycle — one concern (make `$TEST_CMD` trustworthy end to end), one reason to revert:

- **Give `$TEST_CMD` a first-class derivation in Layer 1, mirroring 20.1's `$STACK` shape.** Primary: the project's **declared** test command — the `## Commands` table `aif` writes into `CLAUDE.md` (the `Tests` row, e.g. `pytest`, `uv run pytest`), the same "read what the project already declares, don't re-guess it" move 20.1 applied to `$STACK`. Fallback: the existing four-manifest script read, unchanged and unextended (no new per-language detector as the primary path — the never-extend rule that binds `$STACK`'s fallback now also binds `$TEST_CMD`'s fallback).
- **Define Layer 7's no-command behavior.** When `$TEST_CMD` resolves to nothing (no declared command and no sniffable manifest — e.g. a greenfield project with no test runner yet), Layer 7 does **not** execute an empty command. It explicitly treats the project as having no runnable existing-test suite: skip the run and the green gate, and log it plainly (e.g. "No test command resolved — existing-test gate skipped"). The "all tests green before Layer 8" gate applies only when a command exists.
- **Make the skip visible at hand-off.** A Layer 7 log line scrolls past; the skip must still be readable at the end of the run, so it is **visible, never silent**. Layer 8's counts block gains one line, printed only when the gate was skipped (e.g. `Existing-test gate: skipped (no test command resolved)`). The skip does **not** enter `$HANDOFF_LIST` — it is not a task to paste into `/roadmap-decompose`, belongs to neither handoff category, and has no pointer to resolve to.

## Files & types

- edit: `src/skills/roadmap-test-coverage/SKILL.md` (Layer 1 `$TEST_CMD` derivation; Layer 7's empty-command guard ahead of the run and the re-run gate)

## Guards

- **Scope is `$TEST_CMD` + Layer 7's no-command path only.** `$STACK` resolution (20.1) stays byte-identical; Layers 2–6 stay byte-identical.
- **Layer 8 takes exactly one added counts-block line plus the sentence governing when it prints** — the skipped-gate counter, in the counts block, and the one-line note that it prints only when Layer 7 skipped the gate (needed for correctness: without it the line would read as unconditional and print on every run, including ones where the suite executed and passed). Everything else in Layer 8 is byte-identical: the `$HANDOFF_LIST` print, its two categories (`Refactor:`, `Bugs (Class B — silent failures):`), and the per-line pointer invariant ("Every handoff line resolves to a pointer; none are left blank") are untouched. This narrows the original "Layer 8 byte-identical" guard: written broadly, it collided with this task's own visibility requirement, since Layer 8's handoff print is a fixed two-category structure with a mandated pointer and has no slot a skip entry could occupy.
- **Layer 1's read list gains `CLAUDE.md`.** The primary `$TEST_CMD` source must be an explicit Layer 1 read, not an assumed ambient auto-load — the skill may run against a roadmap in a sub-repo whose `CLAUDE.md` is not the loaded one.
- **No per-language command detectors as the primary path.** The primary is the project's own declared command; the four-manifest read stays the fallback, unextended — the same discipline 20.1 pinned for `$STACK`.
- **Layer 7's failure-classification machinery is unaffected** — the Class A / Class B split, the `general-purpose` classifier prompt, and the `$HANDOFF_LIST` append all stay as they are; only the empty-command guard is added ahead of the run and the re-run gate.
- **Preserve register** — targeted edits to the skill's existing instruction voice, not a rewrite.

## Verification

All checks are static — readable in the changed text or `git diff`, satisfiable without running the skill:

- The edited Layer 1 gives `$TEST_CMD` a first-class rule readable in the changed text: primary is the project's declared command (CLAUDE.md `## Commands` `Tests` row, e.g. `pytest`), fallback is the four-manifest script read — and the four-manifest list is not extended.
- Layer 1's read list names `CLAUDE.md` alongside `ARCHITECTURE.md` and the roadmap — the primary source is an explicit read.
- The edited Layer 7 guards the empty-command case: when `$TEST_CMD` is empty it skips the run and the "all tests green before Layer 8" gate and logs the skip — it no longer emits an unconditional `<$TEST_CMD>` run ahead of an undefined gate.
- Layer 8's counts block carries the skipped-gate line, printed only on a skip; the `$HANDOFF_LIST` print, its two categories, and the pointer invariant are byte-identical.
- A JS project's `package.json` → `test`-script derivation is unchanged in the text (fallback path intact).
- `$STACK` resolution and Layers 2–6 are byte-identical to their post-20.1 state — `git diff` touches only Layer 1's read list, the `$TEST_CMD` read, Layer 7's empty-command handling, and Layer 8's one added counter line.

## Verification note — out of pipeline

Running the skill live on a Python project — the declared-command leg (`$TEST_CMD` resolves and Layer 7 runs it) and the greenfield empty→skip leg — is the real end-to-end confirmation, but it is a **manual, out-of-pipeline step, deliberately not a spec verification obligation**. The pipeline cannot run it, so it must neither attempt it nor flag it as outstanding — this is the user's post-implementation check, not the implementer's or reviewer's, and its absence from a run is expected, not a gap.

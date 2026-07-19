# Plan Review: 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Code Review Summary

**Files Reviewed:** 1 plan + 4 grounding artifacts (contract line, spec 79, `roadmap-test-coverage/SKILL.md`, `architecture-template.md`)
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — WARN (non-blocking, informational). `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is the governing rule for this repo's skill graph. The change is a pure edit inside one skill body's own layer, adds no `loads:` edge, and extracts nothing — no boundary implication. Aligned.
- **Rules** — WARN. `.ai-factory/RULES.md` is absent in this repo; gate skipped, nothing to check against.
- **Roadmap** — pass. The task resolves cleanly: contract line at `.ai-factory/roadmaps/trickster77777.md:24` → `Spec: .ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md`. The plan is a faithful restatement of that spec — primary/fallback order, the `[language, framework]` placeholder guard, the never-extend-the-list clause, the Layers 2–8 byte-identical guard, and both behavior-baseline fixtures all carry through intact. No linkage missing.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent; no project-specific review overrides to apply.

Path and API references in the plan check out against ground truth: Layer 1 really is `SKILL.md:25-37`, and `architecture-template.md:11` really is `- **Tech stack:** [language, framework]`.

### Critical Issues

**1. The primary path severs `$TEST_CMD`'s only derivation source — Layer 7 breaks (`SKILL.md:34`, `:37`, `:260`, `:316`)**

Layer 1 stores three variables, not one: `Store: $STACK (e.g. "NestJS/Jest"), $TEST_CMD (e.g. npm test), $ROADMAP_PATH` (`:34`). Today the single line at `:37` — "Infer stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`" — is the **only** instruction in the whole skill that opens a manifest, and it is where `$TEST_CMD` implicitly comes from: `npm test` is read out of `package.json`'s scripts, `cargo test` out of `Cargo.toml`, and so on. Nothing else in the file derives it.

The plan (Task 1, steps 1–2) makes that manifest read **conditional**: the fallback fires "only when the file is absent, the line is missing/empty, or the line still carries the unfilled template placeholder". An implementer following this literally produces a Layer 1 where, on the primary path — the common, intended path of a project with a filled-in `ARCHITECTURE.md` — no manifest is ever opened. `$STACK` resolves correctly; `$TEST_CMD` resolves to nothing.

`$TEST_CMD` is not decorative. Layer 7 executes it directly (`:260`, `<$TEST_CMD>`) and re-runs it as a hard gate (`:316`, "Re-run `$TEST_CMD`. All tests must be green before Layer 8"). So the failure lands on exactly the projects this task is meant to fix: a Python repo declaring `Python, pytest` in `ARCHITECTURE.md` now resolves `$STACK` (the win), but reaches Layer 7 with an empty test command and either stalls or guesses.

This is a regression the diff introduces, not a pre-existing gap. Today the manifest sniff is unconditional, so on any project with a manifest `$TEST_CMD` is always derivable; making the read conditional is what removes the source. Note also that `ARCHITECTURE.md` cannot cover for it — the template (`architecture-template.md:9-12`) has a `Tech stack` field and no test-command field, so the primary source supplies `$STACK` and nothing more.

The fix is one clause inside the block the task already owns (`:25-37`), so this is in scope and does not contradict the spec — spec 79's guard is "Layer 1 only", and this *is* Layer 1. Make the two resolutions independent rather than nesting `$TEST_CMD` under the `$STACK` branch. For example, keep the ordered rule for `$STACK` exactly as the plan describes, then carry a separate sentence that the manifest is still consulted for `$TEST_CMD` regardless of which source `$STACK` came from. Whatever wording is chosen, the plan should say so explicitly — otherwise the implementer has to invent the answer, and the two behavior-baseline fixtures in Task 2 will not catch it: fixture (1) deliberately has *no* manifest file, and fixture (2) exercises the fallback path where the manifest is read anyway. Neither fixture ever tests "ARCHITECTURE.md present **and** a manifest present", which is the precise combination that regresses.

Suggested addition to Task 2's checks: a third baseline fixture with both an `ARCHITECTURE.md` Tech-stack line and a `package.json` → `$STACK` comes from the former, `$TEST_CMD` still resolves to `npm test`.

**2. Task 2's Layer 5 line range understates the friction-axis prompt (`:~150-165` vs. actual `:155-234`)**

Task 2's first check reads: "nothing in Layer 5's friction-axis prompt (`:~150-165`, where `$STACK` is passed as `<stack>`) or its verdict grammar changes." The cited range is wrong. Layer 5's header is at `:155`, `$STACK` is passed as `<stack>` at `:158`, but the prompt body runs to `:234` and the verdict grammar it names sits at `:230-234` — outside the range given. An implementer diffing only `150-165` would confirm nothing about the verdict grammar the same sentence asks them to guard.

In practice the sibling check on the same line ("Layers 2–8 byte-identical") does cover it, so this is unlikely to let a real regression through — but it is a wrong reference in a file being changed, and the spec it derives from (`79`, "Current state" bullet 3) cites the correct `SKILL.md:158`. Correct the range to `:155-234`, or drop the parenthetical and lean on the byte-identical check alone.

### Positive Notes

- **The reframing is the right call, and the plan preserves it.** Spec 79's central insight — that "Layer 1 has no Python detector" is itself the defect's wrong framing, and the fix is to consult the project's declared stack rather than grow a hard-coded list — survives intact into Task 1, including the explicit never-extend sentence. This closes a class of gap rather than one instance, which is exactly what the contract line promises.
- **The placeholder guard is well-specified.** Naming the literal `[language, framework]` as a fall-through condition (Task 1 step 2, re-checked in Task 2) is the non-obvious edge case, and it is pinned to the actual template text at `architecture-template.md:11` rather than described from memory. An implementer cannot guess wrong here.
- **Guards are concrete and grep-checkable.** "Four items only, unreordered, unextended" with the exact grep that verifies it leaves no room for interpretive drift, and the read-only/edited file split in the spec is honored by the plan.
- **Register discipline is stated.** "Match the file's existing register (terse imperative prose, no tables)" is the right instruction for this repo, where a skill's output register is treated as behavior rather than formatting.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md` — `$TEST_CMD` has never had an explicit derivation rule anywhere in `roadmap-test-coverage/SKILL.md`; it is stored at `:34` and consumed at `:260`/`:316`, but the only thing resembling a source is the stack-inference line's incidental manifest read. Finding 1 above is scoped to not *worsening* this within Layer 1's boundary. Giving `$TEST_CMD` a first-class resolution rule of its own — including what Layer 7 should do when a project has no runnable test command at all, which is currently undefined behavior in front of a hard gate ("All tests must be green before Layer 8") — is a larger change to the skill's contract than task 20.1's Layer-1-only boundary admits, and belongs in its own task.

Two findings above; both are fixable inside the task's existing file boundary, so no `PLAN_REVIEW_PASS`.

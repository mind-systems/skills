# Code Review (round 2, re-review): 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Code Review Summary

**Files Reviewed:** 1 changed file (`src/skills/roadmap-test-coverage/SKILL.md`, re-read in full this round) + plan, spec 79, review-1
**Diff scope:** 17 insertions, 1 deletion, one hunk, Layer 1 only (`:37-54`)
**Risk Level:** 🟢 Low

## Round-1 finding — verdict

**Finding 1 — "the manifest" has no antecedent on the primary path, leaving Python's `$TEST_CMD` behavior agent-dependent (`SKILL.md:49-52`) → FIXED**

Current content of the cited lines, read fresh from disk (`:49-54`):

> This resolution governs `$STACK` only — the never-extend rule binds `$STACK`
> detection, not `$TEST_CMD`'s read. Regardless of which source `$STACK` came
> from, still read the project's package manifest (the same four: `package.json`
> / `pubspec.yaml` / `go.mod` / `Cargo.toml`) unconditionally for `$TEST_CMD`
> (e.g. `npm test` out of `package.json`'s scripts, `cargo test` out of
> `Cargo.toml`).

The bare "the manifest" is gone. The read is now pinned to an enumerated list — "the project's package manifest (the same four: `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`)" — which is in scope on the primary path regardless of whether fallback bullet 2 ever fired. Reading A and reading B can no longer diverge: an agent on a Python repo has a definite four-item list in the same sentence that issues the instruction, so it will not silently invent a fifth detector, and behavior is now deterministic across runs.

The added clause "the never-extend rule binds `$STACK` detection, not `$TEST_CMD`'s read" reads as defensive commentary — it forestalls the misreading that consulting a manifest for `$TEST_CMD` at all violates the never-extend rule three lines above. It is not in tension with the enumerated list that follows: never-extend prohibits growing the `$STACK` fallback's detector list, while `$TEST_CMD`'s read draws on those same four without being governed by that prohibition. The operative instruction is unambiguous.

## New issues this round

None. Re-verified live against the current file:

- **Layer 1 only / Layers 2–8 byte-identical** — `git diff HEAD -U0` reports exactly **one** hunk, at `:34-54`. Layer 5's friction-axis prompt and verdict grammar, and Layer 7's `$TEST_CMD` execute-and-gate sites (`Re-run $TEST_CMD. All tests must be green before Layer 8.`), are untouched — their line numbers shifted by +17 with no content change.
- **Tech stack is the primary source** — `grep -n "Tech stack"` → `:39`, inside Layer 1, naming `ARCHITECTURE.md`'s `## Decision Rationale` field.
- **Four detectors, unreordered, unextended** — the `$STACK` fallback at `:42-43` carries the same four in the original order; the new `$TEST_CMD` sentence at `:51-52` names the same four, again in the same order. No fifth detector anywhere in the file.
- **Placeholder-aware** — `:41-42` names the literal `[language, framework]` as a fall-through condition, matching `architecture-template.md:11`.
- **`$TEST_CMD` not severed** — `:50-52` makes the manifest read unconditional and independent of which branch supplied `$STACK`, which is what plan-review round 1 required.
- **Didn't fold into the friction axis** — no opinion about what counts as friction was introduced.
- **Register and constraints** — terse imperative prose, no tables; `Store:` line and its examples intact; frontmatter (`allowed-tools`, `loads:`) unchanged; body is 396 lines, within the 500-line limit.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md` — `$TEST_CMD` still has no first-class derivation rule; it is stored in Layer 1, executed in Layer 7 and re-run as a hard gate, and its only source remains a manifest read scoped to the same four files. A project with a filled `ARCHITECTURE.md` Tech-stack line and no manifest among those four — the Python-with-pytest shape this task exists to serve — still reaches Layer 7's "All tests must be green before Layer 8" gate with an empty command, which is undefined behavior. This change correctly avoids worsening that within its boundary; giving `$TEST_CMD` its own resolution rule and defining Layer 7's no-test-command behavior exceeds task 20.1's Layer-1-only boundary and belongs in its own task. Carried forward unchanged from plan-review rounds 1 and 2 and review round 1.
- Affects: task 20.1 verification — this review verified the change's text and all grep-checkable guards but did not execute the plan's three live behavior-baseline fixtures (ARCHITECTURE.md-only, manifest-only, both-present). Those runs remain the implementer's step; fixture (3) is the one that observes the `$TEST_CMD` independence this round confirmed by reading.

REVIEW_PASS

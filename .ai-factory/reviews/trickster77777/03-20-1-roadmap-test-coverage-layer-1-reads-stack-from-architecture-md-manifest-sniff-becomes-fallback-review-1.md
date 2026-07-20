# Code Review: 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Code Review Summary

**Files Reviewed:** 1 changed file (`src/skills/roadmap-test-coverage/SKILL.md`, read in full) + 4 grounding artifacts (plan, spec 79, plan-review-1/-2, `aif-architecture/references/architecture-template.md`)
**Diff scope:** 16 insertions, 1 deletion, one hunk, Layer 1 only
**Risk Level:** 🟢 Low

The artifact under review is a skill body — instructions executed by an agent, not compiled code. "Runtime" here means an agent reading Layer 1 and resolving two variables; the failure modes are ambiguity and unreachable branches, not type errors or migrations.

### Guards — all verified live

- **Layer 1 only / Layers 2–8 byte-identical** — `git diff HEAD -U0` reports exactly **one** hunk, at `:34-52`. Layer 5's friction-axis prompt (`:155-234`, `<stack>` pass-site at `:158`, verdict grammar at `:230-234`) and Layer 7's `$TEST_CMD` sites (`:260`, `:316`) are untouched. Guard holds.
- **Tech stack is the primary source** — `grep -n "Tech stack"` → `:39`, inside Layer 1, naming `.ai-factory/ARCHITECTURE.md`'s `## Decision Rationale` field. Guard holds.
- **Four detectors, unreordered, unextended** — `grep -n "package.json\|pubspec.yaml\|go.mod\|Cargo.toml"` → the fallback line at `:42-43` carries the same four in the same order, plus `:51-52` where two appear as `$TEST_CMD` examples only. No fifth detector anywhere. Guard holds.
- **Placeholder-aware** — `:41-42` names the literal `[language, framework]` as a fall-through condition, matching `architecture-template.md:11` exactly. The literal placeholder can never be stored as `$STACK`. Guard holds.
- **Didn't fold into the friction axis** — no opinion about what counts as friction was introduced; the change is pure stack-resolution plumbing. Guard holds.
- **`$TEST_CMD` not severed** (plan-review round 1's finding) — `:49-52` states the resolution governs `$STACK` only and that the manifest is read unconditionally for `$TEST_CMD`. The nesting the finding warned about is not present. Guard holds.
- **Register** — terse imperative prose, no tables; the numbered primary/fallback pair matches the file's existing style. `Store:` line at `:34-35` and its example values are intact. Frontmatter (`allowed-tools`, `loads:`) unchanged.

### Critical Issues

None. The change implements the spec's reordering correctly and introduces no regression.

### Issues

**1. "the manifest" has no antecedent on the primary path, leaving Python's `$TEST_CMD` behavior agent-dependent (`SKILL.md:49-52`)**

The `$TEST_CMD` sentence reads: "Regardless of which source `$STACK` came from, still read **the manifest** unconditionally for `$TEST_CMD`". The definite article points at a list that appears only inside fallback bullet 2 (`:42-43`) — the branch that by construction does *not* fire on the primary path. An agent that took the primary path is told to read "the manifest" with no manifest list in scope.

Two readings follow, and they diverge on exactly the projects this task exists to serve:

- **Reading A (inherits the four-item list):** on a Python repo declaring `Python, pytest` in `ARCHITECTURE.md`, `$STACK` resolves (the win) but no manifest among the four exists, so `$TEST_CMD` stays empty into Layer 7's hard gate at `:316`. This is the pre-existing gap both plan reviews deferred — not worsened, but not signposted either.
- **Reading B (any package manifest):** the agent opens `pyproject.toml`, finds `pytest`, and Layer 7 works. Better outcome, but it quietly does the per-language manifest reading that `:45-47` forbids one paragraph earlier — the agent has to decide whether the never-extend rule binds `$TEST_CMD` too.

Both readings are defensible from the text, so behavior on a Python project is non-deterministic between runs. The fix is one clause naming which list `$TEST_CMD`'s read draws on — e.g. "still read the project's package manifest (the same four) for `$TEST_CMD`" for reading A, or an explicit note that the never-extend rule constrains `$STACK` detection only, not `$TEST_CMD`'s read, for reading B. Reading A is the conservative choice: it preserves today's behavior exactly and leaves the underlying `$TEST_CMD` gap wholly to the deferred task, which is where both plan reviews put it.

This is a wording gap in new text, not a logic error — the implementation is otherwise faithful to the plan.

### Positive Notes

- **The reordering is correct and minimal.** One hunk, inside the block the task owns, with the four-detector fallback preserved verbatim in order. Nothing was rewritten that did not need rewriting, which is what makes the Layers 2–8 guard trivially verifiable.
- **The round-1 fix landed at the right altitude.** `:49-52` states `$STACK` and `$TEST_CMD` as two independent rules rather than bolting a second manifest read onto the same branch — the distinction that actually prevents the regression, carried through from the plan intact.
- **The never-extend clause is in the shipped text, not just the plan.** `:45-47` puts the rule in front of the next author who reaches for a fifth detector, which is what turns this from a Python fix into a closed class of gap — exactly what the contract line promises.
- **The placeholder guard is pinned to the template's literal text**, so the fall-through condition cannot be guessed wrong.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md` — `$TEST_CMD` still has no first-class derivation rule in `roadmap-test-coverage/SKILL.md`; it is stored at `:34`, consumed at `:260` and gated at `:316`, and its only source remains the stack-inference line's incidental manifest read. This change correctly avoids worsening that, but a project with a filled `ARCHITECTURE.md` Tech-stack line and no sniffable manifest — the Python-with-pytest shape this task exists to serve — still reaches Layer 7's "All tests must be green before Layer 8" gate with an empty command, which is undefined behavior. Giving `$TEST_CMD` its own resolution rule, and defining Layer 7's behavior when a project has no runnable test command at all, exceeds task 20.1's Layer-1-only boundary and belongs in its own task. Carried forward unchanged from plan-review rounds 1 and 2. [routed → .ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md]
- Affects: task 20.1 verification — the plan's Task 2 mandates three live behavior-baseline fixtures (ARCHITECTURE.md-only, manifest-only, both-present). This review verified the *text* of the change and all grep-checkable guards, but did not execute the three scratch-project runs; fixture (3) in particular is what would surface issue 1 above as an observed behavior rather than a reading of the instruction. [routed → .ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md]

One minor finding above, fixable with a single clause inside the block the task already owns.

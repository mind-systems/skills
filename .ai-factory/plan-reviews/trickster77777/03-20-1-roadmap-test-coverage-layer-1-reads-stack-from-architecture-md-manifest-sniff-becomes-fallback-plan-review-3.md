# Plan Review: 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Code Review Summary

**Files Reviewed:** 1 plan + 6 grounding artifacts (plan-review-2, contract line, spec 79, `roadmap-test-coverage/SKILL.md`, `architecture-template.md`, `ARCHITECTURE.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — pass. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is the governing rule for this repo's skill graph. The change stays inside one skill body's own layer, adds no `loads:` edge, extracts nothing — no boundary implication.
- **Rules** — WARN. `.ai-factory/RULES.md` is absent in this repo; gate skipped, nothing to check against.
- **Roadmap** — pass. Contract line at `.ai-factory/roadmaps/trickster77777.md:24` → `Spec: .ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md`. Both resolve; the plan is a faithful restatement of the spec's Change, Guards, and Verification sections, plus one annotated deviation.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent; no project-specific review overrides to apply.

Line references re-verified live this round against ground truth, all holding: Layer 1 is `SKILL.md:25-37`, the manifest line is `:37` (`Infer stack from package.json / pubspec.yaml / go.mod / Cargo.toml.` — the file's only manifest mention, confirmed by grep), the `Store:` line is `:34-35`; Layer 5's header is `:155` with `$STACK` passed as `<stack>` at `:158` and the verdict grammar at `:230-234`; Layer 7 executes `<$TEST_CMD>` at `:260` and re-runs it as a hard gate at `:316`; `architecture-template.md:11` is `- **Tech stack:** [language, framework]` under `## Decision Rationale` at `:9`.

### Round-2 finding — resolved

- **Fixture count contradicted its own enumeration (`plan:32`)** — closed. The bullet now reads "three scratch fixtures outside the repo tree (discard all three afterwards; commit none)", matching the three enumerated cases. The disposal instruction now covers fixture (3), and the sentence's internal arithmetic agrees.
- The optional half of that finding was also taken up: fixture (3) is now marked `**DEVIATION from spec 79:33**, which specifies two live runs`, with plan-review round 1 named as its origin and the regression it catches stated inline. Per the annotation convention this is a deliberate signal, not a defect — and it is the correct call: spec 79's two fixtures genuinely never exercise the ARCHITECTURE.md-plus-manifest combination, so the deviation adds the one guard that catches `$TEST_CMD` regressing on the primary path.

### Critical Issues

None.

### Issues

None. Both rounds' findings are closed, and re-reading the plan against ground truth this round surfaced nothing new:

- Task 1's boundary (`:25-37`, Layer 1 only) matches the spec's `Files & types` edit scope exactly.
- The independence mandate for `$STACK` and `$TEST_CMD` resolution is stated with its reason, which is what prevents an implementer from reintroducing the nesting while rewording.
- The placeholder guard names the literal `[language, framework]` and grounds it at `architecture-template.md:11`, verified to be the template's actual text.
- The never-extend sentence carries the spec's central reframing through to the instruction the implementer writes.
- `Settings → Testing: no` does not conflict with Task 2's live runs — those are throwaway fixtures outside the repo tree, explicitly uncommitted, not a test suite added to the product.

### Positive Notes

- **The plan now diffs cleanly against its spec.** The one place it exceeds spec 79 is labelled as a deviation with its cause and its purpose. A later reader comparing plan to spec reads the third fixture as a deliberate guard rather than scope creep — which is exactly what the annotation convention exists for.
- **Every guard is grep-checkable.** "Four items only, unreordered, unextended" with the exact grep, plus the Layers 2–8 byte-identical check with Layer 5's pass-site and verdict grammar pinned by line, leaves no interpretive room.
- **Fixture (3) states its failure mode, not just its setup.** Naming the regression it catches is what keeps a later editor from pruning it as redundant with (1) and (2).
- **The change closes a class, not an instance.** Consulting the project's declared stack instead of growing a hard-coded detector list is the right altitude, and Task 1 preserves that framing rather than flattening it into "add Python".

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md` — `$TEST_CMD` has never had a first-class derivation rule anywhere in `roadmap-test-coverage/SKILL.md`; it is stored at `:34` and consumed at `:260`/`:316`, but its only source is the stack-inference line's incidental manifest read. This plan correctly guards against *worsening* that within Layer 1's boundary, but the underlying gap remains: a project with a filled `ARCHITECTURE.md` Tech-stack line and no sniffable manifest — precisely fixture (1)'s Python-with-pytest shape, and precisely the projects this task exists to serve — still reaches Layer 7 with an empty `$TEST_CMD` in front of a hard gate ("All tests must be green before Layer 8"), which is undefined behavior. Giving `$TEST_CMD` its own resolution rule, and defining what Layer 7 does when a project has no runnable test command at all, is a change to the skill's contract that task 20.1's Layer-1-only boundary does not admit; it belongs in its own task. [routed → .ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md]

PLAN_REVIEW_PASS

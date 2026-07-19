# Plan Review: 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Code Review Summary

**Files Reviewed:** 1 plan + 5 grounding artifacts (plan-review-1, contract line, spec 79, `roadmap-test-coverage/SKILL.md`, `architecture-template.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — pass. `.ai-factory/ARCHITECTURE.md:30` § "Composition: mechanism vs policy" is the governing rule for this repo's skill graph. The change stays inside one skill body's own layer, adds no `loads:` edge, and extracts nothing — no boundary implication.
- **Rules** — WARN. `.ai-factory/RULES.md` is absent in this repo; gate skipped, nothing to check against.
- **Roadmap** — pass. Contract line at `.ai-factory/roadmaps/trickster77777.md:24` → `Spec: .ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md`. Both resolve; the plan is a faithful restatement of the spec's Change, Guards, and Verification sections.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent; no project-specific review overrides to apply.

Every line reference in the plan was re-verified live against ground truth this round, and all of them hold: Layer 1 is `SKILL.md:25-37` with the manifest line at `:37` and the `Store:` line at `:34`; Layer 5's header is `:155`, `$STACK` is passed as `<stack>` at `:158`, and the verdict grammar sits at `:230-234`; Layer 7 executes `<$TEST_CMD>` at `:260` and re-runs it as a hard gate at `:316`; `architecture-template.md:11` is `- **Tech stack:** [language, framework]` under `## Decision Rationale` at `:9`.

### Round-1 findings — both resolved

- **Finding 1 (`$TEST_CMD` severed on the primary path)** — closed correctly, and closed at the right layer. Task 1 now carries an explicit paragraph mandating that the two resolutions be written as **independent**: the ordered primary/fallback rule governs `$STACK` only, and a separate sentence states the manifest is still consulted for `$TEST_CMD` regardless of which source `$STACK` came from. It also carries the *reason* (the template has a Tech-stack field and no test-command field; Layer 7 consumes `$TEST_CMD` at `:260` and `:316`), which matters — an implementer who understands why the nesting is forbidden will not reintroduce it while rewording. This is the fix the finding asked for, not a restatement of the symptom.
- **Finding 2 (wrong Layer 5 line range)** — corrected to `:155-234` with the verdict grammar pinned at `:230-234` and `$STACK`'s pass-site at `:158`. Verified against the file; all three now match.

### Critical Issues

None. The one issue below is minor and does not threaten the change's correctness.

### Issues

**1. Task 2's fixture count contradicts its own enumeration (`plan:32`)**

The behavior-baseline bullet opens "Behavior-baseline, **two** scratch fixtures outside the repo tree (discard **both** afterwards; commit neither)" and then enumerates **three** — (1), (2), and the newly added (3) both-present case. The count and the disposal instruction were carried over from the spec's two-fixture Verification section (`spec 79:33`) without being updated when fixture (3) was added in response to round 1.

The enumeration is unambiguous enough that an implementer will run all three, so the practical risk is low — but "discard both afterwards" leaves fixture (3)'s disposal formally unstated, and the sentence's own numbers disagree inside a file being handed to an implementer. Change "two scratch fixtures" → "three scratch fixtures" and "discard both afterwards" → "discard all three afterwards".

While making that edit, it is worth marking fixture (3) as a deliberate addition beyond the spec's two-run Verification (a `DEVIATION:` note, or one clause naming review round 1 as its origin). The spec at `:33` says "two live runs"; a later reader diffing plan against spec will otherwise read the third fixture as unexplained scope creep rather than the guard that catches the exact regression round 1 identified.

### Positive Notes

- **The round-1 fix was made at the correct altitude.** The tempting cheap fix — "also read the manifest" bolted on — would have left the ordering ambiguous. Instead Task 1 restructures the instruction so `$STACK` resolution and `$TEST_CMD` resolution are stated as two independent rules, which is what actually prevents the nesting. The distinction between "same block" and "same branch" is the whole finding, and the plan now names it explicitly.
- **Fixture (3) is the right test, and the plan says why.** "Fixture (3) is the combination the other two never exercise and the one that regresses if the manifest read is nested under the `$STACK` branch" states the failure mode the fixture exists to catch, not just the setup. That sentence is what keeps the fixture from being dropped as redundant by a later editor.
- **The reframing survives intact.** Spec 79's central insight — that "Layer 1 has no Python detector" is itself the wrong framing, and the fix is to consult the project's declared stack rather than grow a hard-coded list — carries through into Task 1 including the explicit never-extend sentence. This closes a class of gap rather than one instance, exactly as the contract line promises.
- **The placeholder guard is pinned, not remembered.** Naming the literal `[language, framework]` as a fall-through condition and grounding it at `architecture-template.md:11` leaves no room for an implementer to guess the template's actual text.
- **Guards stay grep-checkable.** "Four items only, unreordered, unextended" with the exact grep that verifies it, plus the Layers 2–8 byte-identical check, leaves no interpretive drift.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md` — `$TEST_CMD` has never had a first-class derivation rule anywhere in `roadmap-test-coverage/SKILL.md`; it is stored at `:34` and consumed at `:260`/`:316`, but its only source is the stack-inference line's incidental manifest read. This plan now correctly guards against *worsening* that within Layer 1's boundary, but the underlying gap remains: a project with a filled `ARCHITECTURE.md` Tech-stack line and no sniffable manifest — precisely fixture (1)'s Python-with-pytest shape, and precisely the projects this task exists to serve — still reaches Layer 7 with an empty `$TEST_CMD` in front of a hard gate ("All tests must be green before Layer 8"), which is undefined behavior. Giving `$TEST_CMD` its own resolution rule, and defining what Layer 7 does when a project has no runnable test command at all, is a change to the skill's contract that task 20.1's Layer-1-only boundary does not admit; it belongs in its own task.

One minor finding above, fixable inside the task's existing file boundary, so no PLAN_REVIEW_PASS.

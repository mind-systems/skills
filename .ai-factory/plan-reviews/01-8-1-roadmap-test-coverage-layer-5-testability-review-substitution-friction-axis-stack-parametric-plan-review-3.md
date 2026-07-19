# Plan review 3: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** plan + spec `61-test-coverage-l5-substitution-friction-axis.md` + contract line 8.1 + target `src/skills/roadmap-test-coverage/SKILL.md` + fixtures `ui-ux-pro-max/scripts/core.py`, `design_system.py` + plan-reviews 1 and 2
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — WARN(none). Unchanged from rounds 1–2: the change stays inside one skill body, adds no `loads:` edge (`SKILL.md:14` verified still `test-philosophy roadmap-engine`), and leaves the silent-failure axis with `test-philosophy` at Layer 3. No boundary violation.
- **Rules** — WARN. No `.ai-factory/RULES.md`, no `.ai-factory/skill-context/aif-review/SKILL.md`. Nothing to enforce.
- **Roadmap** — OK. Contract line 8.1 (`.ai-factory/ROADMAP.md:11`) present, unchecked, `Spec:` tag resolves to the spec read here. Contract line, spec and plan agree on the parameter criterion, the friction framing, the `$STACK` → `<stack>` binding, and the three-fixture baseline. The 17.3 coupling guard holds: the plan constrains only *new* prose to registry vocabulary and leaves the file's 3 pre-existing `milestone` occurrences (`:35`, `:50`, `:51` — all outside Layer 5) to 17.3.

**All three findings from plan-review 2 are resolved, each at the level it was raised.**

1. **`singleton` acceptance condition** — Task 2 now splits the seven grep terms into two acceptance conditions (`:54-57`), gives `singleton` its own rule ("must not appear on a universal checklist line and must not define a band; may appear only in a clause subordinating the construct to the parameter criterion, or in a stack-conditional illustration"), names the concrete regression it hunts (`SKILL.md:170-171`), and states outright that applying the TS/Node-illustration rule to `singleton` would fail a correct implementation and burn a tightening round. The collision with the Task 1 `:34` mandated clause is gone.
2. **Stale spec citations** — all nine re-derived and now exact. Verified individually: `:22`→spec `:56` (Files & types, scopes to `:158-187`) ✓; `:38`→spec `:61` (two orthogonal axes) ✓; `:52`→spec `:81` (grep pattern) and spec `:62` (rejected half-fix) ✓; `:73`→spec `:69-71` (origin file unavailable, three in-repo fixtures, report must say so) ✓; `:83`→spec `:65` (load-bearing guard) ✓; `:90`→spec Verification `:78-80` and Guard `:65` ✓; `:92`→spec `:15` (the two naive reframes) ✓. Not one stale coordinate remains.
3. **The phantom `DEVIATION`** — `:73` now opens "The origin file is unavailable — this is not a deviation", states that spec and plan agree and there is nothing to reconcile, and keeps the surviving obligation (the report must state the origin defect was not re-run). Correct demotion: the framing is dropped, the instruction retained.

**Ground truth re-verified independently this round — every pin is exact.** `SKILL.md`: fence `:165-185`, `Collect all verdicts.` `:187`, orchestrator lines `:160-161`, `$STACK` sole occurrence `:37`, `<$TEST_CMD>` `:211`, `loads:` `:14`, DI-presence line `:170-171`, `setTimeout` check `:174`, length 330 (headroom against the 500-line cap). `core.py`: `CSV_CONFIG` `:17`, `_load_csv` `:159`, `_search_csv` `:165` with docstring `:166` and guard `:167-168`, `_load_csv` call `:170`, `search()` `:212`, `DATA_DIR / config["file"]` `:218`, guard `:220-221`, `search_stack()` `:234`. `design_system.py`: `from core import search` `:21`, class `:37`, `__init__` `:40`, `_load_reasoning` `:43-49` with guard `:46-47`, `_multi_domain_search` `:51-62`, `_find_reasoning_rule` `:64-86` with terminal `return {}` `:86`, `datetime.now()` `:552`/`:808` inside the module-level formatters `format_master_md` (`:542`) / `format_page_override_md` (`:805`).

**Grep-pattern interaction checked.** Task 2's pattern is case-sensitive `Date.now`; the Task 1 `:34` mandated clause writes `datetime.now()` in lowercase, so it produces no hit and no second `singleton`-shaped collision. The other five TS/Node terms appear nowhere in mandated new prose. The two acceptance conditions are jointly exhaustive over the seven terms and neither can fire on correctly-implemented text.

### Critical Issues

None.

### Positive Notes

- The finding-1 fix was made at the right depth: rather than dropping `singleton` from the grep to dodge the collision, Task 2 keeps the term and states *what regression it hunts* — the surviving "are all dependencies injected (constructor params, not module-level singletons or static imports)" line. A gate that names its target is testable; one that names a forbidden token is not.
- The citation re-derivation is complete rather than sampled. The blast-radius argument at `:22` now walks: an implementer opening spec `:56` finds the `:158-187` scope statement that makes the `:160-161` amendment in-scope, so the conservative "skip it as out of scope" failure — which would strand `<stack>` unbound and degrade silently — is foreclosed.
- The criterion is now stated three times consistently and each time from the same discriminator: plan `:7` (Context), Task 1 `:29-34` (the prompt's own bands), spec `:23-33` (ratified table). The helper-vs-collaborator clause (`:33`, spec `:39-47`) is present in all of them, and case 3's expectation (`:88`) explicitly names it as the clause under test with the correct diagnosis if it fails ("the defect is the missing clause in Task 1, not the fixture").
- The replay protocol (`:77-83`) remains contamination-proof — verbatim fence text, one fresh agent per case with the reasoning for why not one, withheld expectations, exact prompt recorded — and Task 3's Files line ("read-only replay targets, nothing written") resolves where the evidence lands without ambiguity.
- The fixture triple still holds up against the four cheap heuristics: all three read a CSV whose contents drive the result, all three guard with `.exists()` and return a benign default, and case 2 takes arguments yet must flag. Verified against the source — nothing surface-level separates them.
- The `datetime.now()` decoy warning in case 1 (`:86`) is correct and non-obvious: both calls sit in module-level formatters outside the class and outside anything it reaches.
- Task 2's `git diff HEAD --` with the explicit non-empty assertion, and its full re-run after each tightening round with named regression modes, remain the right shape for the bounded loop.

## Deferred observations

- Affects: roadmap task 17.3 — `SKILL.md` carries 3 pre-existing `milestone` occurrences (`:35`, `:50`, `:51`) outside the Layer 5 fence. This plan correctly constrains only *new* prose to registry vocabulary and leaves the sweep to 17.3, which the contract line schedules strictly after Phase 8 to avoid the same-file collision. Noted only so a reviewer seeing `milestone` in the post-change file does not read it as introduced by this task. [dismissed — already handled: 17.3 landed and swept milestone→task across roadmap-test-coverage; verified zero "milestone" occurrences remain in SKILL.md]

PLAN_REVIEW_PASS

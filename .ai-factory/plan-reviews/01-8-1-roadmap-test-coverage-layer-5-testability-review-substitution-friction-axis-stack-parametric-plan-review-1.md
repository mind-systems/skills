# Plan review: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** plan + spec `61-test-coverage-l5-substitution-friction-axis.md` + contract line 8.1 + target `src/skills/roadmap-test-coverage/SKILL.md` + replay fixtures `ui-ux-pro-max/scripts/core.py`, `design_system.py`
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — WARN(none). `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is untouched by this task: the change stays inside one skill body, adds no `loads:` edge (`SKILL.md:14` stays `test-philosophy roadmap-engine`), and the plan explicitly keeps the silent-failure axis with `test-philosophy` (Layer 3). No boundary violation.
- **Rules** — WARN. No `.ai-factory/RULES.md` in this repo; no `.ai-factory/skill-context/aif-review/SKILL.md`. Nothing to enforce.
- **Roadmap** — OK. Contract line 8.1 (`.ai-factory/ROADMAP.md:11`) is present, unchecked, and its `Spec:` tag resolves to the spec read here. Contract line, spec, and plan were updated in lockstep this session and now agree on the parameter criterion and the three-fixture baseline. The 17.3 coupling guard ("runs strictly after Phase 8 lands — same-file collision") is respected: this plan only constrains *new* prose to registry vocabulary and does not sweep the file's existing `milestone` occurrences.

**Line references — all verified against ground truth.** `SKILL.md` fence `:165-185`, `Collect all verdicts.` `:187`, orchestrator lines `:160-161`, `$STACK` sole occurrence `:37`, `<$TEST_CMD>` `:211`, `loads:` `:14`, file length 330. `design_system.py`: class `:37`, `__init__` `:40`, `_load_reasoning` `:43-49`, `.exists()` guard `:46-47`, `_find_reasoning_rule` `:64-86` with terminal `return {}` at `:86`, `datetime.now()` at `:552`/`:808` inside the module-level formatters `format_master_md` (`:542`) / `format_page_override_md` (`:805`) — outside the class, exactly as the plan warns. `core.py`: `CSV_CONFIG` `:17`, `_load_csv` `:159`, `_search_csv` `:165` with guard `:167-168` and `_load_csv` call `:170`, `search()` `:212`, `DATA_DIR / config["file"]` `:218`, guard `:220-221`, `search_stack()` `:234`. Every pin is exact. This is unusually well-grounded.

**Deviation, checked and accepted.** Task 3 records the spec `:49` replay target (the live-run Python file) as unavailable in this repo and substitutes three in-repo fixtures; and it records that `search()`, pinned `clean` in an earlier spec draft, contradicted the spec's own ratified table row `:32`. I verified the ground truth: `search()` receives `query`/`domain`/`max_results` by argument, but `CSV_CONFIG` resolves only a filename and the rows the behavior varies on sit behind `DATA_DIR / config["file"]` (`:218`) with no parameter. The spec was corrected rather than worked around, and the contract line follows. This is conformance, not a defect.

### Critical Issues

**1. The band criterion does not separate a *collaborator* from a *helper*, and case 3 fails its own criterion as written.**
Plan `:31` defines the middle band as "the code acquires varying data **or a collaborator** … at construction or inside the call, and the API offers no parameter to supply it instead". The `clean` band (`:30`) exempts only "module-level names it reads are **static lookup data**".

Apply that literally to case 3, `_search_csv()` (`core.py:165`): it reaches the module-level function `_load_csv` (`:159`) inside the call, and `open()` inside that — collaborators, not static lookup data, with no parameter to supply either. A replay agent reading the criterion strictly returns `needs-refactor` for case 3, contradicting the expected `clean` at plan `:74`. Meanwhile case 1 legitimately flags partly *because* `_multi_domain_search` reaches the imported `search()` (`design_system.py:21`) with no parameter — so the plan needs the collaborator clause to fire in case 1 and not in case 3, and gives the agent nothing to tell them apart.

Failure scenario: replay round 1 returns `needs-refactor` on all three. Task 3's bounded loop spends both tightening rounds on wording, then reports "the fixtures are not separable on the friction axis and the set needs replacing" (`:78`) — a false conclusion, since the fixtures are fine and the criterion is under-specified. The task lands with no baseline.

Fix, inside Task 1's block: add the missing clause to the criterion — *a helper whose behavior is fully determined by the parameters the caller passes it is not a substitution point; a collaborator counts only when it supplies varying data or an effect the test must control and the API offers no parameter for it.* That is precisely what distinguishes `_load_csv(filepath)` (filepath is the caller's parameter → `clean`) from `search(query, domain, …)` reached inside `DesignSystemGenerator` (nothing in the class's API supplies it → flag). Task 2's assertion 4 should then also check this clause is present.

**2. The replay protocol is unpinned, so the only verification this task has can be contaminated.**
Task 3 (`:71`) says "Launch the rewritten prompt as a real `general-purpose` agent three times, with `Stack: Python/pytest`" — but never states that the prompt must be the fence text **verbatim** with only `<area name>` / `<stack>` / `<file path>` substituted, that each replay runs in a **fresh** agent with no other context, and that the expected band is **not** disclosed to it. The implementing agent has all three expected verdicts written in front of it at `:72-74`. Nothing in the plan stops it from adding a clarifying sentence, pasting the plan's own rationale, or running all three in one agent that then reads the triple as a puzzle to split.

Failure scenario: the implementer passes a lightly-expanded prompt ("note that taking arguments is not the criterion"), all three verdicts land, Task 3 reports a clean baseline — and the shipped fence, which the orchestrator will actually run cold, was never exercised. This defeats the whole point of a behavior baseline, and it is the one guard spec `:55` calls load-bearing.

Fix: state the replay protocol explicitly in Task 3 — verbatim fence text, placeholders substituted and nothing else added, one fresh agent per case, expected band withheld, and the exact prompt sent recorded alongside each verdict line in the report.

**3. The blast-radius grep misses the DI-idiom residue it most needs to catch.**
Task 2's grep (`:50`) covers `process.env`, `(req as any)`, `(metadata as any)`, `observable pipes`, `Date.now` — inherited verbatim from spec `:71`. But the checks being made stack-conditional also include `setTimeout without returned handle` (`SKILL.md:174`) and the DI-presence line itself, `module-level singletons or static imports` (`:170-171`), which is the *primary* thing this task removes. Neither term is in the pattern.

Failure scenario: the rewrite keeps "module-level singletons" as a universal line (an easy regression under a tightening round, since it reads like the criterion), Task 2's grep passes clean, and the shipped prompt still encodes the DI-presence axis the task exists to remove — the exact failure spec `:52` names as the rejected half-fix. Add `setTimeout` and `singleton` to the pattern.

### Positive Notes

- Every line reference in the plan — 20+ across three files — is exact. That is the difference between a plan an implementer can execute and one it has to re-derive.
- The fixture triple is genuinely well-designed: all three read a CSV whose contents drive the result, all three guard with `.exists()` and return a benign default, and case 2 takes arguments yet must still flag. The four cheap heuristics the plan names (`module singleton? touches disk? fails loudly? takes arguments?`) really do each fail to split them, so only the criterion can. The reasoning at `:69` is sound.
- The `<stack>` binding gap (plan `:22`) is caught correctly and scoped correctly: the placeholder genuinely has no source today (`$STACK` occurs once, at `:37`), and an unbound placeholder degrades silently — the subagent still returns a well-formed verdict line, so nothing downstream catches it.
- The placeholder-form pin (`:24`) is grounded in observed file convention rather than invented: no `$VAR` appears inside any agent fence, and the one `$TEST_CMD` is angle-wrapped as `<$TEST_CMD>` at `:211`. Verified.
- Task 2's insistence on `git diff HEAD --` over bare `git diff`, with an explicit non-empty assertion, closes a real vacuous-pass hole.
- Re-running Task 2 in full after every tightening round (`:60`), with the named regression modes, is the right shape for a bounded loop.
- The `datetime.now()` decoy warning in case 1 (`:72`) is correct and non-obvious — those calls really do sit in module-level formatters outside the class and outside anything it calls.

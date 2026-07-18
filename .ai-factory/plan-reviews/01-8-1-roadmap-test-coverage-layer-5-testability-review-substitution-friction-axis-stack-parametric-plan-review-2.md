# Plan review 2: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** plan + spec `61-test-coverage-l5-substitution-friction-axis.md` + contract line 8.1 + target `src/skills/roadmap-test-coverage/SKILL.md` + fixtures `ui-ux-pro-max/scripts/core.py`, `design_system.py` + prior plan-review 1
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — WARN(none). Unchanged from review 1: the change stays inside one skill body, adds no `loads:` edge (`SKILL.md:14` verified still `test-philosophy roadmap-engine`), and keeps the silent-failure axis with `test-philosophy` at Layer 3. No boundary violation.
- **Rules** — WARN. No `.ai-factory/RULES.md`, no `.ai-factory/skill-context/aif-review/SKILL.md`. Nothing to enforce.
- **Roadmap** — OK. Contract line 8.1 (`.ai-factory/ROADMAP.md:11`) present, unchecked, `Spec:` tag resolves to the spec read here. Contract line reads "three pinned in-repo fixtures" — verified verbatim, matching plan and spec. The 17.3 coupling guard is respected: the plan constrains only *new* prose to registry vocabulary and does not sweep the file's existing `milestone` occurrences (3 today, confirmed).

**All three findings from plan-review 1 are resolved.** The helper-vs-collaborator clause is now in Task 1 (`:33`) *and* ratified in the spec (`:39-47`); the replay protocol is pinned in Task 3 (`:72-76`) with verbatim fence text, one fresh agent per case, withheld expectations, and recorded prompts; `setTimeout` and `singleton` are added to Task 2's grep (`:51`) with the reasoning made explicit. Good, complete closure.

**Ground truth re-verified — every pin against the target and fixtures is exact.** `SKILL.md`: fence `:165-185`, `Collect all verdicts.` `:187`, orchestrator lines `:160-161`, `$STACK` sole occurrence `:37`, `<$TEST_CMD>` `:211`, `loads:` `:14`, Layer 6 `:191-203`, length 330. `design_system.py`: `search` import `:21`, class `:37`, `__init__` `:40`, `_load_reasoning` `:43-49` with guard `:46-47`, `_multi_domain_search` `:51-62`, `_find_reasoning_rule` `:64-86` with terminal `return {}` `:86`, `datetime.now()` `:552`/`:808` inside module-level `format_master_md` (`:542`) / `format_page_override_md` (`:805`). `core.py`: `CSV_CONFIG` `:17`, `_load_csv` `:159`, `_search_csv` `:165` with docstring `:166`, guard `:167-168`, `_load_csv` call `:170`, `search()` `:212`, `DATA_DIR / config["file"]` `:218`, guard `:220-221`, `search_stack()` `:234`. Not one miss.

### Critical Issues

**1. Task 2's `singleton` assertion contradicts prose Task 1 mandates — a correct implementation fails the gate and burns a tightening round.**

Task 2 (`:51-52`) adds `singleton` to the grep pattern and then asserts: "every hit must sit inside a stack-conditional TS/Node illustration, never on a universal checklist line."

But Task 1 (`:34`) *requires* this sentence in the new prompt: "reading a module singleton, `os.environ`, `get_config()`, or `datetime.now()` is by itself **not** the middle band; it lands there when it is data the behavior varies on and the API offers no parameter to supply it instead." That is a **Python-side, criterion-scoped clause** — deliberately not a TS/Node illustration. Plan `:34` in fact frames these as the stack-conditional illustrations for a *non-TS* stack, and `:7` names "module singleton, `os.environ`, `datetime.now()`" as the general construct set.

So the `singleton` hit that a correct rewrite produces sits in neither category the assertion allows: it is not inside a TS/Node illustration, and it is not a universal checklist line either — it is a negative clause explicitly subordinating the construct to the criterion.

Failure scenario: Task 1 is implemented exactly as written. Task 2 greps, finds `singleton` in the `:34`-mandated sentence, and the assertion "every hit must sit inside a stack-conditional TS/Node illustration" evaluates false. The implementer treats it as a regression, moves or deletes the clause to satisfy the gate — weakening the very sentence that keeps construct names from re-becoming the band definition (Task 2's own assertion 4) — and consumes one of only two tightening rounds on a phantom failure. The two rounds are the plan's hard budget; spending one here can push Task 3 to the "fixtures are not separable, stop and report" exit at `:87` on a plan defect rather than a fixture defect.

Note the asymmetry is real and intended for the other terms: `process.env`, `(req as any)`, `(metadata as any)`, `observable pipes`, `Date.now` genuinely are TS/Node-only per Task 1 `:35`. Only `singleton` straddles both stacks — which is exactly why review 1 asked for it, and why it needs its own acceptance condition.

Fix: split the assertion. For `process.env` / `(req as any)` / `(metadata as any)` / `observable pipes` / `Date.now`, keep "must sit inside a stack-conditional TS/Node illustration". For `singleton`, the condition is different: it must **not** appear on a universal checklist line and must **not** define a band — it may appear only in a clause subordinating the construct to the parameter criterion (the `:34` sentence) or in a stack-conditional illustration. Stating the DI-presence regression it is actually hunting — a surviving "are all dependencies injected (constructor params, not module-level singletons or static imports)" line, `SKILL.md:170-171` — makes the check testable without colliding with mandated prose.

**2. Nine of the plan's ten spec citations point at the wrong lines; the spec was edited this session and the references were not re-derived.**

The plan repeatedly instructs the implementer to check its claims against numbered spec lines. Verified against the spec as it stands:

| Plan says | Actual spec line at that number | Correct target |
|---|---|---|
| `:22` — "spec `:36` scopes the change to `:158-187`" | mid-sentence, "…guard returning a default keeps construction from crashing…" | `:56` |
| `:38` — "spec `:41` — two orthogonal axes, two owners" | mid-sentence, "…test already controls it by controlling those parameters…" | `:61` |
| `:52` — "spec `:71`'s pattern" (the grep) | mid-sentence, "…fixtures that reproduce the bands…" | `:81` |
| `:52` — "the rejected half-fix (spec `:52`)" | "**Explicit scope boundary**" bullet | `:62` |
| `:70`, `:78` — "the one guard spec `:55` calls load-bearing" | blank line | `:65` |
| `:81` — "spec `:49` asks for a replay on…" | "The verdict vocabulary stays…" bullet | `:69-71` |
| `:85` — "Verification `:68`" / "Verification `:68-70` now carries these three bullets" | blank line | `:78-80` |
| `:85` — "Guard `:55` names three fixtures" | blank line | `:65` |
| `:87` — "the two naive reframes the origin analysis rejected (spec `:15`)" | correct — DI-presence/`patchable? → clean` paragraph | ✓ only correct one |

The **substance** of every claim is true against the spec — I checked each one. The spec really does scope the change to `:158-187`, really does hold the two-axes guard, really does carry the three Verification bullets and the three-fixture guard. Only the coordinates are stale, drifted by the criterion preamble (`:23-27`) and helper-vs-collaborator clause (`:39-47`) inserted during this planning session.

Failure scenario: Task 2's blast-radius argument at plan `:22` rests on "spec `:36` scopes the change to `:158-187`, and `:160-161` sit inside it" — the plan's justification for amending the orchestrator line being in scope. An implementer told to verify scope opens spec `:36`, lands mid-sentence in the defensive-acquisition paragraph, and finds nothing about `:158-187`. The in-scope claim now looks unsupported. The conservative response is to skip the `:160-161` amendment as out of scope — which strands `<stack>` unbound, the precise silent degradation plan `:22` exists to prevent (the subagent judges friction with no stack and still returns a well-formed verdict line, so nothing downstream catches it). The same failure shape applies at `:52`, where a stale pointer undercuts the grep-extension rationale.

Fix: re-derive all nine citations against the current spec. They are cheap to correct and the plan's grounding discipline is otherwise its strongest property — this is the one place a reader cannot walk the reference.

**3. The `DEVIATION` at Task 3 `:68` is no longer a deviation; the spec already says what it claims to depart from.**

Task 3 opens: "**Deviation, recorded deliberately:** spec `:49` asks for a replay on 'the Python class that misfired this session'. That file lives in the live orchestrator run's project … It stands replaced by the in-repo fixtures below."

The spec no longer asks for that. Spec `:69-71` reads: "The origin misfire file lives in the live orchestrator run's project and is named nowhere — it is unavailable in this repo. The baseline runs on three pinned in-repo fixtures that reproduce the bands; the origin defect itself is not re-run, and the report must say so." Plan `:85` itself records that the spec was corrected in this session and concludes "Plan and spec now agree; there is no unannotated divergence to carry" — which is right, and directly contradicts the `DEVIATION` header still standing at `:68`.

A `DEVIATION` annotation is a signal to a reviewer: *the plan followed ground truth where the plan-layer disagreed — go verify against the cited authority*. Here there is no disagreement. The instruction it carries ("the origin defect is not re-run; say so when reporting") is correct and matches spec `:71` — only the framing is wrong.

Failure scenario: a reviewer or rescue pass takes the `DEVIATION` at face value, opens spec `:49` to check what the plan departed from, finds the unrelated verdict-vocabulary bullet, and cannot reconcile the annotation with the spec. Worse, on a `milestone-rescue` read the standing `DEVIATION` reads as an unresolved plan/spec conflict and invites re-litigating a question already settled — the spec was corrected precisely so this would not recur.

Fix: demote `:68` from a `DEVIATION` to a plain statement of fact — the origin file is unavailable in this repo, the spec (`:69-71`) records this and pins the three in-repo fixtures, and the report must state the origin defect was not re-run. Keep the reporting instruction; drop the deviation framing.

### Positive Notes

- All three review-1 findings are closed properly — at the *criterion* level, not patched around. The helper-vs-collaborator clause was added to the plan **and** ratified into the spec's Change section (`:39-47`) with the `_load_csv` / `search()` contrast spelled out, so the criterion is now authoritative rather than plan-local. That is the right depth of fix.
- The replay protocol (`:72-76`) is now genuinely contamination-proof: verbatim fence text, placeholders and nothing else, one fresh agent per case with the reasoning for *why* not one agent ("reads it as a puzzle to split and reasons from the contrast"), withheld expectations, and the exact prompt recorded next to each verdict. The named failure mode at `:78` shows the author understood what the guard is for.
- Task 2's grep rationale (`:52`) is unusually good: it names `module-level singletons or static imports` (`SKILL.md:170-171`) as "the likeliest regression under a tightening round, because it reads like the criterion while encoding the rejected half-fix". Correct diagnosis — that line is the axis the task removes. (Finding 1 is about the acceptance condition attached to it, not the instinct to grep for it.)
- Every line pin against `SKILL.md`, `design_system.py`, and `core.py` — 25+ of them — is exact, including the non-obvious ones (`_search_csv` docstring at `:166` so the guard is `:167-168`; `search_stack()` at `:234`, with the plan explicitly noting an earlier draft's wrong `:236`). The *code*-side grounding is exemplary; finding 2 is confined to the spec-side coordinates.
- The `datetime.now()` decoy warning in case 1 (`:81`) remains correct and non-obvious: both calls sit in module-level formatters outside the class and outside anything it calls, so an agent citing them as the class's friction is wrong for a reason the plan anticipates.
- Case 2 (`search()`) as the load-bearing fixture is exactly right, and the reconciliation at `:85` — treating a spec that disagreed with its own ratified table as a defect to fix rather than route around — is the correct handling of a governing-spec conflict.
- Task 2's `git diff HEAD --` with an explicit non-empty assertion, and its full re-run after every tightening round with named regression modes, remain the right shape.

## Deferred observations

- Affects: roadmap task 17.3 — `SKILL.md` carries 3 pre-existing `milestone` occurrences outside the Layer 5 fence. This plan correctly constrains only *new* prose to registry vocabulary and leaves the sweep to 17.3, which the contract line schedules strictly after Phase 8 to avoid the same-file collision. Nothing to do here; noted only so a reviewer seeing `milestone` in the post-change file does not read it as introduced by this task.

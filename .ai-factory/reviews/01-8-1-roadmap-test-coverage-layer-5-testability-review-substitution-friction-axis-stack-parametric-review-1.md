# Code review: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** `src/skills/roadmap-test-coverage/SKILL.md` (the only product change, read in full) + `.ai-factory/specs/61-test-coverage-l5-substitution-friction-axis.md`, contract line 8.1, the plan, and the three replay fixtures (`ui-ux-pro-max/scripts/core.py`, `design_system.py`)
**Risk Level:** 🟠 Medium-High — one shipped sentence licenses the exact reframe the task exists to reject

`git status` shows eight paths staged. Seven are planning artifacts (plan, plan-reviews, plan JSON, spec, ROADMAP contract line). Exactly one is product: `src/skills/roadmap-test-coverage/SKILL.md`. This review targets the product change; the artifacts are checked only where the product must conform to them.

### What the change does

The Layer 5 agent prompt is rewritten from four TS/NestJS checks on a binary DI-presence axis to a graded substitution-friction axis governed by one criterion — *does the API offer a parameter for the thing a test must vary?* — with TS/Node constructs demoted to a stack-conditional illustration block. The orchestrator line now binds `$STACK` from Layer 1 to the prompt's `<stack>` placeholder.

### Mechanical checks — all pass

| Check | Result |
|---|---|
| Blast radius | **1 hunk**, `@@ -157,26 +157,75 @@` — Layer 5 only. Frontmatter, Layers 1–4, 6–8, Critical Rules untouched. |
| Verdict grammar (Layer 6/8 contract) | `diff` of `HEAD:181-185` against `230-234` → **byte-identical**. |
| `loads:` edge | `:14` unchanged (`test-philosophy roadmap-engine`); no new edge. |
| DI-presence line removed | `module-level singletons or static imports` is **gone**; the only `singleton` hit (`:199`) is the subordinating clause, which is the acceptance condition the plan pins. |
| `$STACK` sourced, not stranded | `:37` (Layer 1) and `:161` (orchestrator line). **No hit inside the fence.** |
| Registry vocabulary in new prose | No `milestone` / `spec note` added. The three pre-existing `milestone` hits (`:35`, `:50-51`) are outside Layer 5 and correctly left to task 17.3. |
| Body length | 379 lines, well under 500. |
| Silent-failure axis | `:226-228` *forbids* weighing failure-loudness rather than asking about it — correct direction. |

The helper-vs-collaborator clause (`:191-195`) is present and correctly worded. The stack-conditional block (`:208-214`) is explicitly scoped "TS/Node only".

### Critical Issues

**1. The scope-fence sentence contradicts the criterion in the same prompt, and re-admits the rejected "patchable → clean" reframe.** (`SKILL.md:221-222`)

The shipped fence reads:

> Flag coupling only to the degree it taxes test setup: **a self-acquired dependency that is near-zero-friction to substitute is `clean`**, and pure design-smell coupling with no test-setup cost is out of scope…

Twelve lines earlier the criterion says the opposite (`:183-187`):

> **no parameter for what varies** — varying data or a collaborator is acquired at construction or reached inside the call, and the API offers no parameter to supply it instead; the only way to vary it in a test is to patch the acquisition site, **however cheap that patch** → friction → `needs-refactor`

"Self-acquired" means no parameter — the middle band by definition. "Near-zero-friction to substitute" means the patch is cheap — which `:186` says explicitly does *not* clear the flag. The fence therefore names a set that the criterion assigns to `needs-refactor` and assigns it to `clean`. The two rules cover the same case and disagree.

This is the precise failure the governing spec forbids. Spec `:52`:

> The fence clears *nothing-to-substitute* cases; it never clears a patchable acquisition of varying data — **"the patch is easy" is not the fence.**

And spec `:15` records "patchable? → `clean`" as one of the two rejected reframes the whole task exists to prevent — the one under which the origin finding "would vanish entirely".

**Failure scenario, concrete against the pinned baseline.** Replay case 2 is `core.py:search()` (`:212`), expected `needs-refactor`. Its corpus sits behind `DATA_DIR / config["file"]` (`:218`) with no parameter — middle band under `:183-187`. But patching `DATA_DIR` with `monkeypatch` is a one-liner, so it is unambiguously "a self-acquired dependency that is near-zero-friction to substitute" — and `:221-222` says that is `clean`. A cold agent applying the fence returns `clean`, the baseline misses, and the plan's bounded loop (two rounds) gets spent chasing prompt wording. Worse, the loop's own guard says "do not let case 2 come out `clean` on 'it takes arguments'" — it does not anticipate case 2 coming out `clean` on *the fence sentence*, so the implementer has no instruction pointing at the real culprit. The same sentence puts case 1 at risk: `DesignSystemGenerator`'s reasoning CSV is equally monkeypatchable.

**Origin.** This is not implementer drift — the plan's Task 1 mandates the sentence nearly verbatim ("a self-acquired dependency that is near-zero-friction to substitute is `clean`"), carried forward from a pre-criterion draft and never reconciled when the parameter criterion was ratified. The implementation faithfully shipped a defective instruction. The spec is the artifact that got this right.

**Fix** — restate the fence in nothing-to-substitute terms, so it clears the case the spec intends and no more. Something like: *Flag coupling only to the degree it taxes test setup. What the fence clears is code with nothing to substitute — varying inputs arrive as parameters and module-level names are read only as static reference data. It never clears a patchable acquisition of varying data: cheapness of the patch is not the fence.* Then correct the plan's Task 1 bullet to match, so a re-run does not reintroduce it.

### Minor Issues

**2. Two new angle-bracket tokens sit in instructional prose inside the fence.** (`:205`, `:216`)

`` `<sentence>` `` (`:205`) and `` `<one sentence>` `` (`:216`) refer to the verdict's third field, but the file's convention — the one the plan leaned on to justify `Stack: <stack>` over `Stack: $STACK` — is that angle brackets inside a fence mark a substitution slot. The replay protocol substitutes only `<area name>`, `<stack>`, `<file path>`, so these are non-substitutable lookalikes. The pre-existing `<one sentence: what to refactor and why>` in the return block is the same shape, so there is precedent and the orchestrator is unlikely to touch them; risk is low. Worth a rename to plain prose ("the one-sentence verdict field") if the fence is edited again for finding 1.

**3. "belongs to code review, not this review" reads oddly.** (`:224`)

Layer 5 *is* a review — the prompt's own header is "Testability review for:". The spec phrases it "belongs to a code-review lens, not a test-coverage planner", which distinguishes the two without self-contradiction. Cosmetic; fold into the finding-1 edit if convenient.

### Positive Notes

- The verdict grammar survived byte-identical, verified by diff rather than by eye. This is the one hard contract Layers 6/8 depend on, and it is intact.
- The DI-presence line is genuinely gone, not softened — the plan's widened grep (`singleton`) confirms the only surviving hit is the clause that subordinates the construct to the criterion. That was the single highest-value regression check and it passes.
- The stack-conditional block is well-formed: the three TS/Node checks are grouped under one explicit "TS/Node only" heading rather than scattered as universal lines, which is materially harder to misread than the original four-item checklist.
- The helper-vs-collaborator clause (`:191-195`) is present and correctly reasoned. Without it, case 3 (`_search_csv`, which reaches `_load_csv`) would flag; with it, the "path is the caller's parameter" reasoning is available to the agent.
- The orchestrator-line binding (`:160-161`) closes the unbound-`<stack>` hole exactly as planned, and `$STACK` correctly does not appear inside the fence.
- Blast radius is a single hunk. For a change of this size in a 379-line file, that is disciplined.

## Deferred observations

- Affects: `roadmap-test-coverage` Layer 1 (`SKILL.md:40`) — the axis is now stack-parametric, but Layer 1 infers `$STACK` only from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`. **There is no Python detection** (no `pyproject.toml`, `requirements.txt`, `setup.py`), and Python is the stack that motivated this entire task. On a Python repo `$STACK` is guessed or empty, so `<stack>` arrives unfilled and the agent judges friction with no stack idiom — the same silent degradation the `<stack>` binding was added to prevent, one step upstream. Out of scope here: spec `:56` requires Layers 1–4 byte-identical, so the implementation was right not to touch it. Needs its own task before the Python baseline is meaningful in a real run.
- Affects: task 17.3 — three pre-existing `milestone` occurrences remain at `:35`, `:50-51`, outside Layer 5. Correctly left alone; 17.3 is sequenced after Phase 8 for this file. Noted so a reader does not attribute them to this change.

# Code re-review: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** `src/skills/roadmap-test-coverage/SKILL.md` (re-read in full at current state), `.ai-factory/specs/61-test-coverage-l5-substitution-friction-axis.md`, the plan, contract line 8.1, reviews 1–2
**Risk Level:** 🟢 Low — both prior findings fixed at product and plan level; no new defects

Product change remains confined to one file: `src/skills/roadmap-test-coverage/SKILL.md`. The other nine staged paths are planning artifacts.

## Verdicts on review-2 findings

### Finding 1 (new in review-2) — fence's second sentence attached the wrong predicate, saying *clean* code is "out of scope". **FIXED.**

Current `SKILL.md:221-227`, quoted verbatim:

> Flag coupling only to the degree it taxes test setup. What the fence
> clears is code with nothing to substitute — varying inputs arrive as
> parameters and module-level names are read only as static reference data;
> **that is `clean`. Coupling that is merely ugly and costs test setup nothing
> is out of scope — it belongs to a code-review lens, not a test-coverage
> planner.** The fence never clears a patchable acquisition of varying data:
> cheapness of the patch is not the fence.

The merged sentence is split back into four distinct propositions, and each predicate now attaches to its own subject:

1. the scope rule — flag only to the degree it taxes test setup;
2. nothing-to-substitute code → **`clean`** (no longer mislabelled "out of scope");
3. design-smell coupling with no test-setup cost → **out of scope, code-review's**, restored as its own proposition;
4. patchable acquisition of varying data is never cleared — cheapness is not the fence.

This matches spec `:52`'s structure clause for clause, and satisfies spec Guard `:63` explicitly rather than by implication.

Fixed at the plan level too. Plan `:37` now carries the corrected wording plus a directive naming the exact referential trap:

> **Keep this as a distinct proposition from the design-smell exclusion** — coupling that is merely ugly and costs test setup nothing is a separate, second case that is out of scope and belongs to a code-review lens, not a test-coverage planner; do not merge the two into one sentence where "that" ends up referring back to the parameter-receiving (`clean`) case instead of the design-smell case.

That is the right depth: the plan was the origin of the defect both times, and it now forecloses the specific failure rather than just restating the desired text.

### Review-1 findings — re-verified, still fixed

- **Finding 1 (fence contradicted the criterion).** `:226-227` reads "The fence never clears a patchable acquisition of varying data: cheapness of the patch is not the fence" — consistent with the criterion at `:186` ("however cheap that patch → friction → `needs-refactor`"). The banned phrasing does not appear anywhere in the file.
- **Finding 2 (angle-bracket lookalikes).** `:205` "one-sentence verdict field's register" and `:216-217` "the one-sentence verdict field". Mechanically confirmed: scanning the fence (`:166-237`) for angle tokens returns only `<area name>`, `<stack>`, `<file path>` in the header plus the pre-existing pair in the return block. No lookalikes.
- **Finding 3 (self-undermining "not this review").** `:225-226` reads "belongs to a code-review lens, not a test-coverage planner" — spec `:52`'s phrasing.

## Mechanical checks — re-run at current state

| Check | Result |
|---|---|
| Blast radius | **1 hunk**, `@@ -157,26 +157,78 @@`. Verified by direct diff: lines `1-157` byte-identical to `HEAD`, and everything from `Collect all verdicts.` (old `:187` → new `:239`) through end of file byte-identical. Frontmatter, Layers 1–4, Layers 6–8, Critical Rules untouched. |
| Verdict grammar (Layer 6/8 contract) | `diff` of `HEAD:181-185` vs current `233-237` → **byte-identical**. |
| `loads:` | `:14` still `test-philosophy roadmap-engine`; no new edge. |
| DI-presence line | Gone. Sole `singleton` hit is `:199`, the subordinating clause — the acceptance condition plan Task 2 pins for that term. |
| `$STACK` | `:37` (Layer 1) and `:161` (orchestrator binding) only; **no hit inside the fence**. |
| Stack-conditional block | `:208-214`, grouped under an explicit "TS/Node only" heading; no TS construct on a universal line. |
| Registry vocabulary | No `milestone` / `spec note` in new prose; the three pre-existing hits (`:35`, `:50-51`) sit outside Layer 5 and are left to task 17.3. |
| Markdown integrity | 18 fence delimiters file-wide (even); Layer 5's fence opens `:166`, closes `:237`; no stray delimiter inside the prompt. |
| Body length | 382 lines, under the 500 limit. |

## New Issues

None. Reading the prompt end to end as a cold agent would, the instructions are internally consistent: the criterion (`:176-189`), the helper-vs-collaborator clause (`:191-195`), the construct-subordination paragraph (`:197-206`), the fence (`:221-227`), and the silent-failure exclusion (`:229-231`) agree with one another and with the return grammar. The redundancy between band 1 (`:179-182`) and fence proposition 2 (`:222-224`) is reinforcement of the same rule, not a conflict.

## Positive Notes

- Both defects found in this review cycle originated in the plan and were fixed in the plan as well as the product, each time with an explicit prohibition against the specific wording that failed. A re-run of Task 1 from the current plan produces the correct text.
- The verdict grammar survived three rounds of edits to the surrounding prose byte-identical. That is the single hard contract Layers 6/8 depend on.
- Blast radius held at one hunk across all three rounds — confirmed here by byte-comparing the head and tail of the file against `HEAD`, not merely by reading the diff.
- The final fence reads as four short propositions rather than one compound sentence, which is what made the referential error possible in the first place. The structure now resists the failure rather than just avoiding it.

## Deferred observations

- Affects: `roadmap-test-coverage` Layer 1 (`SKILL.md:40`) — carried unchanged from reviews 1 and 2, and the one item here with real downstream consequence. The axis is now stack-parametric and `<stack>` is bound, but Layer 1 infers `$STACK` only from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`. **There is no Python detection** (`pyproject.toml`, `requirements.txt`, `setup.py`) — and Python is the stack that motivated this task. On a Python repo `<stack>` arrives unfilled and the agent judges friction with no stack idiom, which is the same silent degradation the `<stack>` binding exists to prevent, one layer upstream. Correctly out of scope for 8.1 (spec `:56` freezes Layers 1–4); needs its own task before the Python baseline is meaningful in a live run. [routed → .ai-factory/specs/79-test-coverage-layer1-python-stack-detection.md — new Phase 20 task 20.1 opened: Layer 1 now reads $STACK from ARCHITECTURE.md's declared Tech-stack field first, generic across any language, manifest-sniffing demoted to a fallback rather than growing a per-language list]
- Affects: plan Task 2, assertion 1 — worded as "no question about failure-loudness, silent failure, or test-worthiness anywhere in the block". The shipped prompt necessarily *contains* those words at `:229-231` as a prohibition ("Do not weigh failure-loudness, silent failure…"), which Task 1 mandates. A careful reader distinguishes asking from forbidding and passes, but a keyword-driven pass could read a correct implementation as contamination — structurally the same trap plan-review-2 caught in the `singleton` grep condition. Phrasing the assertion as "does not *ask the agent to weigh*" would close it. Plan-artifact nit; no effect on the shipped skill. [dismissed — cosmetic nit on a transient plan artifact, no effect on the shipped skill]
- Affects: task 17.3 — three pre-existing `milestone` occurrences at `:35`, `:50-51`, outside Layer 5, correctly untouched. Noted so they are not attributed to this change. [dismissed — already handled: 17.3 landed and swept milestone→task across roadmap-test-coverage; verified zero "milestone" occurrences remain in SKILL.md]

REVIEW_PASS

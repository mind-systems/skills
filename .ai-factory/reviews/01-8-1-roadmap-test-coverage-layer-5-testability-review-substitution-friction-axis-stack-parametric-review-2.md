# Code re-review: 8.1 — roadmap-test-coverage Layer 5, substitution-friction axis

## Code Review Summary

**Files Reviewed:** `src/skills/roadmap-test-coverage/SKILL.md` (re-read in full at current state), `.ai-factory/specs/61-test-coverage-l5-substitution-friction-axis.md`, the plan, contract line 8.1, review-1
**Risk Level:** 🟡 Low-Medium — the blocking contradiction is genuinely resolved; one referential defect remains in the same paragraph

Product change is still confined to one file: `src/skills/roadmap-test-coverage/SKILL.md`. Everything else staged is planning artifacts.

## Verdicts on review-1 findings

### Finding 1 — scope fence contradicted the criterion, re-admitting "patchable → clean". **FIXED.**

Current `SKILL.md:221-226`, quoted verbatim:

> Flag coupling only to the degree it taxes test setup. What the fence
> clears is code with nothing to substitute — varying inputs arrive as
> parameters and module-level names are read only as static reference data;
> that is out of scope, and belongs to a code-review lens, not a
> test-coverage planner. **It never clears a patchable acquisition of varying
> data: cheapness of the patch is not the fence.**

The offending sentence — "a self-acquired dependency that is near-zero-friction to substitute is `clean`" — is gone, and its replacement states the opposite disposition explicitly. This now agrees with the criterion at `:183-187` ("the only way to vary it in a test is to patch the acquisition site, **however cheap that patch** → friction → `needs-refactor`") and with spec `:52` ("'the patch is easy' is not the fence").

The concrete failure scenario is closed: replay case 2 (`core.py:search()`) can no longer be routed to `clean` via the fence on the grounds that patching `DATA_DIR` is a one-liner.

Fixed on both sides, as recommended. Plan Task 1 `:37` now carries the corrected wording and adds an explicit ban:

> Do not phrase this as "a self-acquired dependency that is near-zero-friction to substitute is `clean`" — that sentence contradicts the parameter criterion's own "however cheap the patch" clause and re-admits the rejected "patchable → clean" reframe (spec `:15`).

So a re-run cannot reintroduce it. This is the right depth of fix.

### Finding 2 — non-substitutable angle-bracket lookalikes in fence prose. **FIXED.**

Current `:204-206` and `:216-217`:

> The stack's patchability sets the
> **one-sentence verdict field's** register (friction to drop, never
> "untestable"), never the verdict.

> For the middle band, name the friction and the fix in **the one-sentence
> verdict field** (e.g. "self-acquires its config at construction; …

Both `<sentence>` and `<one sentence>` are replaced with plain prose. Verified mechanically — scanning the fence (`:166-236`) for angle tokens returns only `<area name>`, `<stack>`, `<file path>` in the header and the pre-existing `<area name>` / `<one sentence: what to refactor and why>` in the return block. No lookalikes remain.

### Finding 3 — "belongs to code review, not this review". **FIXED.**

Current `:224-225`: "belongs to a code-review lens, not a **test-coverage planner**" — matches spec `:52`'s phrasing and removes the self-contradiction of a review telling itself it is not a review.

## Mechanical checks — re-run at current state, all pass

| Check | Result |
|---|---|
| Blast radius | **1 hunk**, `@@ -157,26 +157,77 @@`. Layers 1–4, 6–8, Critical Rules, frontmatter untouched. |
| Verdict grammar (Layer 6/8 contract) | `diff` of `HEAD:181-185` vs current `232-236` → **byte-identical**. |
| `loads:` | `:14` still `test-philosophy roadmap-engine`; no new edge. |
| DI-presence line | Gone. Sole `singleton` hit is `:199`, the subordinating clause — the acceptance condition the plan pins. |
| `$STACK` | `:37` and `:161` only; **no hit inside the fence**. |
| Registry vocabulary | No `milestone` / `spec note` in new prose; the three pre-existing hits (`:35`, `:50-51`) are outside Layer 5, left to 17.3. |
| Body length | 381 lines, under 500. |

## New Issues

**1. The fence's second sentence attaches the wrong predicate — it now says *clean* code is "out of scope".** (`SKILL.md:221-226`, mirrored in plan `:37`)

> What the fence clears is code with nothing to substitute — varying inputs arrive as parameters and module-level names are read only as static reference data; **that is out of scope, and belongs to a code-review lens, not a test-coverage planner.**

The referent of "that" is the immediately preceding clause: code whose varying inputs arrive as parameters. But such code is *not* out of scope — it is squarely in scope and receives the verdict `clean`. What genuinely belongs to a code-review lens is the other thing: coupling that is ugly but carries **no test-setup cost** ("design-smell for its own sake").

Spec `:52` keeps these as two distinct clauses and the implementation merged them, grafting the second's predicate onto the first:

> Code that receives its varying inputs as arguments and touches module-level names only as static reference data is **not flagged**, whatever those names are — **pure design-smell "coupling for its own sake"** is out of scope and belongs to a code-review lens, not a test-coverage planner.

Two consequences, both real but bounded:

- *Muddled disposition.* An agent is told that parameter-receiving code is "out of scope". The return grammar offers only `clean | needs-refactor`, so in practice it will still emit `clean` — there is no third option to escape to. Blast radius is therefore limited to confusion, not a wrong verdict.
- *The design-smell exclusion is no longer stated as its own proposition.* Spec Guard `:63` requires the prompt to say Layer 5 "ignores coupling that carries no test-setup cost", warning that omitting it "re-smuggles design review in". Sentence 1 — "Flag coupling only to the degree it taxes test setup" — does carry that requirement in positive form, so the guard is **not violated**; but the explicit negative case that made it concrete has been absorbed into a clause about a different subject.

Severity is lower than review-1's finding: no verdict flips, and the load-bearing "cheapness is not the fence" half is correct. It is worth one more edit because this is the paragraph the spec singles out as load-bearing, and a reader of the shipped prompt currently cannot recover the design-smell exclusion from it.

**Fix** — split the merged sentence back into the spec's two propositions, e.g.: *What the fence clears is code with nothing to substitute — varying inputs arrive as parameters and module-level names are read only as static reference data; that is `clean`. Coupling that is merely ugly and costs test setup nothing is out of scope — it belongs to a code-review lens, not a test-coverage planner. The fence never clears a patchable acquisition of varying data: cheapness of the patch is not the fence.* Correct plan `:37` in the same pass, since the implementation copied it faithfully and the plan is where the defect originates.

## Positive Notes

- Review-1's blocking finding was fixed at the criterion level and in both artifacts, with an explicit ban on the old phrasing added to the plan so the regression cannot recur on a re-run. That is the correct handling — the alternative (patching only the skill body) would have left the plan mandating the defect.
- The verdict grammar remains byte-identical across two rounds of edits to the surrounding prose. This is the one hard contract Layers 6/8 depend on and it has survived intact.
- The angle-token cleanup was done thoroughly rather than minimally — both occurrences replaced with prose that reads better than the originals, and the fence now contains exactly the three substitution slots the replay protocol names.
- Blast radius held at a single hunk through the fix round; no incidental edits crept into Layers 1–4 or 6–8.

## Deferred observations

- Affects: `roadmap-test-coverage` Layer 1 (`SKILL.md:40`) — unchanged from review-1 and still worth its own task. The axis is stack-parametric and `<stack>` is now bound, but Layer 1 infers `$STACK` only from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`. **No Python detection** (`pyproject.toml`, `requirements.txt`, `setup.py`) — and Python is the stack that motivated this task. On a Python repo `<stack>` arrives unfilled and the agent judges friction with no stack idiom. Correctly out of scope here (spec `:56` freezes Layers 1–4). [routed → .ai-factory/specs/79-test-coverage-layer1-python-stack-detection.md — new Phase 20 task 20.1 opened: Layer 1 now reads $STACK from ARCHITECTURE.md's declared Tech-stack field first, generic across any language, manifest-sniffing demoted to a fallback rather than growing a per-language list]
- Affects: task 17.3 — three pre-existing `milestone` occurrences at `:35`, `:50-51`, outside Layer 5, correctly untouched. Noted so they are not attributed to this change. [dismissed — already handled: 17.3 landed and swept milestone→task across roadmap-test-coverage; verified zero "milestone" occurrences remain in SKILL.md]

# Review — 25.2: task-rescue, close three non-blocking edges left by 25.1's escalation branch

**Scope:** `src/skills/task-rescue/SKILL.md` (one file, 31 insertions / 10 deletions). Skill-body documentation change — no executable code, no runtime/data-flow surface, no security surface.

## What changed vs. the spec (`89-task-rescue-escalation-branch-polish.md`)

All four spec-mandated edits landed exactly as specified:

1. **Step 3 root-cause list exemption** (`:140-141`) — added after the four-bullet list, before the governing-spec paragraph. Text matches spec item 3 verbatim.
2. **Step 3 "Attach the root-cause category" parenthetical** (`:189-191`) — the `— not applicable to an escalation classification, which has none` exemption inserted inside the existing parenthetical; the four category names and surrounding sentence otherwise unchanged.
3. **Step 4 router rewrite** (`:238-243`) — the "reuse … verbatim" summary is gone (grep confirms zero occurrences); replaced by a per-option router naming three distinct Step 5 targets. The `AskUserQuestion` block above it (`:211-233`) is untouched.
4. **Step 5 three escalation blocks** (`:334-349`) — inserted between the non-convergence block and "Depth: spec", each `---`-delimited. Option 1 → steps 1–4; option 2 → steps 3–4, explicitly "Do NOT run steps 1–2"; option 3 → no procedure, mirroring the non-convergence no-op shape and routing to Step 5.5.
5. **Always-valid guard** (`:452`) — now names `"escalated"` alongside `"planned:N"`/`"implemented:N"`, matching the closed-set table (`:422`) and its closing note (`:459-463`).

## Correctness checks

- **Step 4 → Step 5 routing is now coherent.** The router sends the agent to Step 5, where each labeled escalation block redirects into the "Depth: spec" procedure by step number. Option 2's "steps 3–4" correctly maps to the procedure's delete-plan/-plan-reviews/-reviews (step 3) + delete-sidecar (step 4); "Do NOT run steps 1–2" correctly skips the spec + contract-line edit — resolving the original contradiction with option 2's own body (`:226`, "Do not edit this task's spec").
- **Option 3 no-op matches non-convergence.** Structurally identical (`Do NOT delete anything. Do NOT touch the sidecar. Proceed directly to Step 5.5.`) and Step 5.5 already treats such routings as a propagation no-op — an escalation carries no defect to propagate, so the existing Step 5.5 logic needs no change.
- **Step-number coupling is fragile but flagged.** Options 1/2 reference "Depth: spec" by step number; if that procedure is ever renumbered these two blocks silently go stale. The spec's Guards already call this out as a maintenance note for a future editor. No action now.
- **Guards honored:** Step 2's four classifications, the Diagnosis Report narrative form, the stale-implementer short form, the closed-set table, and its closing note are all byte-identical. Domain-language discipline holds — the new Step 5 blocks use skill-body routing vocabulary (sidecar, plan-review), the same register as the "Depth: spec"/"Non-convergence" blocks they sit beside, not user-facing report text. `git diff --stat` confirms exactly one file changed.

## Deferred observations

- The Always-valid guard rewrite (`:452`) dropped the former trailing sentence `Never write "planned:1" after deleting the plan .md.` This is exactly what spec item 4 prescribes (its replacement text omits it), and the clause is logically redundant with the retained positive rule — a deleted plan `.md` is "not present", which the `write "planned:1" only when the plan .md is present` condition already forbids. No behavioral loss; recorded only for traceability. Not blocking.

No bugs, security issues, or correctness problems found.

REVIEW_PASS

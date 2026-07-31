# Plan: task-rescue: close three non-blocking edges left by 25.1's escalation branch

## Context
Close the three non-blocking internal-consistency edges 25.1's review left in `src/skills/task-rescue/SKILL.md`: Step 4's over-claimed "verbatim" routing for escalation options 1/2, Step 3's root-cause machinery that never exempted escalation, and the Always-valid guard that omits `escalated`. One file, one feature, one reason to revert.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Route Step 4 escalation options explicitly

- [x] **Task 1: Replace Step 4's post-`AskUserQuestion` summary sentence with a per-option router**
  Files: `src/skills/task-rescue/SKILL.md`
  Replace the paragraph currently at lines 235–240 (the sentence beginning "Options 1 and 2 both **reuse the existing spec-depth full reset verbatim**…" through "Proceed to Step 5 with the user's choice.") with the spec's per-option router text (spec § "The change", item 1):
  > Each option routes to its own labeled procedure under Step 5 (below) — no new rollback mechanism, no fifth depth-menu entry: option 1 runs the existing "Depth: spec" procedure unmodified (including its spec/contract-line edit); option 2 runs only that procedure's deletion steps, never its spec/contract-line edit; option 3 runs no Step 5 procedure at all. Proceed to Step 5.
  Do NOT touch the `AskUserQuestion` block above it (lines 211–233) — the three user-facing options stay byte-identical. Only the routing instruction after them changes.

- [x] **Task 2: Insert three labeled escalation-option blocks into Step 5** (depends on Task 1)
  Files: `src/skills/task-rescue/SKILL.md`
  Insert three new `---`-delimited labeled blocks immediately after the "**Non-convergence (terminal — no rollback):**" block (currently lines 325–328) and before "**Depth: spec**" (currently line 332), grouping the escalation routing-only outcomes alongside non-convergence, ahead of the depth-keyed repair procedures. Use the exact text from the spec § "The change", item 2 — three blocks:
  - **Escalated — option 1 (decision recorded here):** run the "Depth: spec" procedure below exactly as written, steps 1–4 — the spec edit is the point of this option.
  - **Escalated — option 2 (decision belongs elsewhere):** run only steps 3–4 of the "Depth: spec" procedure below (delete the plan, all plan-reviews, all reviews, and the sidecar). Do NOT run steps 1–2 — do not edit the task spec or the contract line; the decision was reported as belonging elsewhere, not resolved here.
  - **Escalated — option 3 (not resolved yet):** no Step 5 procedure runs. Leave every artifact in place exactly as the orchestrator left it — plan, sidecar, and any plan-review/review files. Do NOT delete anything. Do NOT touch the sidecar. Proceed directly to Step 5.5.
  Each block is separated by `---` on its own line, matching the surrounding block style. Option 3's block must read structurally identical to the non-convergence no-op block (no-delete / no-sidecar-touch / proceed to 5.5) — deliberately, so a reader recognizes the same pattern. Do NOT restate or duplicate "Depth: spec"'s step bodies; reference by step number only.

### Phase 2: Exempt escalation from Step 3's root-cause machinery

- [x] **Task 3: Add escalation exemptions to Step 3's root-cause list and the "Attach" sentence**
  Files: `src/skills/task-rescue/SKILL.md`
  Two one-clause additions, no restructuring (spec § "The change", item 3):
  - After the "Root-cause categories" bullet list (currently ending at line 138, the "Stale implementer session" bullet), add a sentence: "Escalation is not in this list — it carries no root cause; see its own short-form branch below and skip the 'Attach the root-cause category' step for it."
  - In the "Attach the root-cause category" sentence (currently lines 186–189), add the parenthetical exemption inside the existing parenthetical: "…(specification gap / scope overload / mechanical error / stale implementer session — **not applicable to an escalation classification, which has none**)…".
  Leave the four existing bullets, the Diagnosis Report narrative form, and the stale-implementer short form byte-identical — only these two clauses are new text.

### Phase 3: Sync the Always-valid guard with the closed-set table

- [x] **Task 4: Extend the "Always-valid guard" line to name `escalated`**
  Files: `src/skills/task-rescue/SKILL.md`
  Rewrite the "**Always-valid guard:**" line (currently line 431) per the spec § "The change", item 4, so it names `"escalated"` alongside `"planned:N"` / `"implemented:N"`:
  > **Always-valid guard:** `"planned:N"`, `"implemented:N"`, and `"escalated"` carry no artifact reference and always validate — write `"planned:1"` only when the plan `.md` is present; write `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists. `task-rescue` never writes `"escalated"` itself (see the closed-set table's closing note) — it is always-valid for the orchestrator to accept, not for this skill to produce.
  Leave the closed-set table (lines ~415–422) and its closing note (lines ~433–442) untouched — this line only catches up to what they already say.

### Phase 4: Verify

- [x] **Task 5: Confirm the diff matches the spec's verification checklist** (depends on Tasks 1–4)
  Files: `src/skills/task-rescue/SKILL.md`
  Manual read + grep against the spec's Verification section:
  - Step 4's post-`AskUserQuestion` sentence no longer says "verbatim" for both options 1 and 2; it names three distinct routing targets.
  - Step 5 contains three new blocks, each naming exactly one escalation option, positioned between "Non-convergence (terminal — no rollback)" and "Depth: spec"; the option 2 block says steps 1–2 do NOT run and option 1 says all four do; option 3 matches the non-convergence no-op shape.
  - `grep -n "Root-cause categories\|Attach the root-cause category" src/skills/task-rescue/SKILL.md` → both lines now carry an escalation exemption.
  - `grep -n "Always-valid guard" src/skills/task-rescue/SKILL.md` → the line now names `"escalated"`.
  - `git diff --stat` shows exactly one file changed: `src/skills/task-rescue/SKILL.md`.

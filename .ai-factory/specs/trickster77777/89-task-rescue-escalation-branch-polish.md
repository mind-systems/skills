# task-rescue: close three non-blocking edges left by 25.1's escalation branch

Task 25.1 landed the escalation branch clean — reviewed 🟢 Low risk, `REVIEW_PASS`, no blocking findings (`.ai-factory/reviews/trickster77777/10-…-review-1.md`). Its own `## Deferred observations` and the reconciled code review that followed it surfaced three non-blocking edges, all confined to `src/skills/task-rescue/SKILL.md`, all about the escalation branch's own internal consistency, none about a missing capability. This task closes all three in one pass — same file, same feature, one concern ("finish what 25.1 started"), one reason to revert.

## Current state (grounded, verified live)

**1. Step 4 → Step 5 routing over-claim** (`src/skills/task-rescue/SKILL.md:235-240`):

```
Options 1 and 2 both **reuse the existing spec-depth full reset verbatim**
(Step 5's "Depth: spec" procedure) — do not introduce a new rollback procedure or a
fifth depth-menu entry. The only new thing here is the routing decision (which of
the three options) and, for option 2, the pointer report in place of an in-place spec
edit. Option 3 performs no file changes at all. Proceed to Step 5 with the user's
choice.
```

The "Depth: spec" procedure it points at (`:332-344`) is four steps: (1) edit the task spec, (2) edit the contract line to match, (3) delete plan/plan-reviews/reviews, (4) delete the sidecar. Option 2's own body (`:224-229`) explicitly says "Do not edit this task's spec" — directly contradicting steps 1–2 of the procedure the summary sentence says option 2 "reuses … verbatim." A reader who follows "verbatim" literally for option 2 edits the task's own spec despite being told not to. Option 3 (`:230-232`, "No reset. The escalated sidecar stays exactly as the orchestrator left it") performs no file changes, yet the same summary sentence says "Proceed to Step 5 with the user's choice" for all three — Step 5 has no labeled block matching a true no-op the way it does for non-convergence (`:325-328`: "Do NOT delete any artifact. Do NOT touch the sidecar. Proceed directly to Step 5.5.").

**2. Step 3 root-cause-category machinery doesn't exempt escalation:**
- The "Root-cause categories" bullet list (`:131-136`) enumerates four: Specification gap, Scope overload, Mechanical error, Stale implementer session — the same four that get a Step 3 short-form-vs-full-narrative branch. Escalation's own short-form branch (`:171-177`) was added, but escalation was never added to this list.
- "Attach the root-cause category (specification gap / scope overload / mechanical error / stale implementer session) and the recurring-issue signal to the report as a classification" (`:186-189`) — same four, no escalation exemption. Taken literally, this instructs attaching a "root-cause category" to an escalation report, which has no root cause at all (per the escalation short-form branch's own closing line, "there is no root cause here, only a decision still to make").

**3. "Always-valid guard" omits `escalated`** (`:431`): "`"planned:N"` and `"implemented:N"` carry no artifact reference and always validate — write `"planned:1"` only when the plan `.md` is present; write `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists." The closed-set table (`:359-422`) marks `"escalated"` "none — always valid" too, and the closing note (`:436-442`) already explains task-rescue never writes it, only clears it — but this guard paragraph, which is the table's own write-precondition summary, doesn't mention `escalated` at all, leaving the table and this paragraph slightly out of sync.

## The change

**1. Step 4 — replace the summary sentence (`:235-240`) with an explicit per-option router, no other text in the `AskUserQuestion` block (`:211-233`) changes:**

> Each option routes to its own labeled procedure under Step 5 (below) — no new rollback mechanism, no fifth depth-menu entry: option 1 runs the existing "Depth: spec" procedure unmodified (including its spec/contract-line edit); option 2 runs only that procedure's deletion steps, never its spec/contract-line edit; option 3 runs no Step 5 procedure at all. Proceed to Step 5.

**2. Step 5 — insert three new labeled blocks**, positioned immediately after "**Non-convergence (terminal — no rollback):**" (`:325-328`) and before "**Depth: spec**" (`:332`) — grouping escalation's routing-only outcomes alongside non-convergence's, ahead of the depth-keyed repair procedures:

```
---

**Escalated — option 1 (decision recorded here):** run the "Depth: spec" procedure
below exactly as written, steps 1–4 — the spec edit is the point of this option.

---

**Escalated — option 2 (decision belongs elsewhere):** run only steps 3–4 of the
"Depth: spec" procedure below (delete the plan, all plan-reviews, all reviews, and
the sidecar). Do NOT run steps 1–2 — do not edit the task spec or the contract line;
the decision was reported as belonging elsewhere, not resolved here.

---

**Escalated — option 3 (not resolved yet):** no Step 5 procedure runs. Leave every
artifact in place exactly as the orchestrator left it — plan, sidecar, and any
plan-review/review files. Do NOT delete anything. Do NOT touch the sidecar.
Proceed directly to Step 5.5.

---
```

**3. Step 3 — two additions, both one clause, no restructuring:**
- After the "Root-cause categories" bullet list (`:131-136`), add: "Escalation is not in this list — it carries no root cause; see its own short-form branch below and skip the 'Attach the root-cause category' step for it."
- At the "Attach the root-cause category" sentence (`:186-189`), add a parenthetical exemption: "Attach the root-cause category (specification gap / scope overload / mechanical error / stale implementer session — **not applicable to an escalation classification, which has none**) and the recurring-issue signal…"

**4. Line `:431` — extend the "Always-valid guard" to name `escalated`, consistent with the closed-set table and its closing note:** "`"planned:N"`, `"implemented:N"`, and `"escalated"` carry no artifact reference and always validate — write `"planned:1"` only when the plan `.md` is present; write `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists. `task-rescue` never writes `"escalated"` itself (see the closed-set table's closing note) — it is always-valid for the orchestrator to accept, not for this skill to produce."

## Files & types

- edit: `src/skills/task-rescue/SKILL.md` — Step 3 (two one-clause additions), Step 4 (one summary sentence rewritten), Step 5 (three new labeled blocks inserted), the "Always-valid guard" line. One file, as scoped.

## Guards

- **The four pre-existing Step 2 classifications, their conditions, and their relative order (including escalation now checked first, from 25.1) stay byte-identical** — this task touches Step 3/4/5 text and one guard line only, never Step 2.
- **The Diagnosis Report's full narrative form (Plan/Implement-phase) and the stale-implementer-session short form stay byte-identical** — only the two Step 3 additions named above are new text; nothing existing is reworded.
- **Domain-language discipline holds**: none of the three new Step 5 blocks, the Step 3 additions, or the Step 4 rewrite introduce any orchestrator-mechanics language into user-facing report text — they are skill-body routing instructions, the same register as the existing "Depth: spec" / "Non-convergence" blocks they sit beside.
- **No new rollback mechanism.** The two new escalation-option blocks in Step 5 (options 1 and 2) do not duplicate or restate "Depth: spec"'s steps — they reference it by step number ("steps 1–4" / "steps 3–4"). If "Depth: spec"'s own step numbering ever changes, these two blocks' references must be updated in the same commit — flagged here so a future editor of "Depth: spec" greps for "Depth: spec" mentions before renumbering it.
- **Option 3's new block matches non-convergence's exact shape** ("Leave every artifact in place… Do NOT delete anything. Do NOT touch the sidecar. Proceed directly to Step 5.5.") — deliberately, so a reader recognizes the same no-op pattern rather than a new one.
- **The `AskUserQuestion` block's own text (`:211-233`) is untouched** — only the sentence after it (`:235-240`) changes. The user-facing options the rescuer presents do not change; only the internal routing instruction that follows them does.
- **`orchestrator-artifacts`, `reserved-words.md`, `task-rescue-audit` are untouched** — this task is scoped to `task-rescue/SKILL.md` only, per the review's own attribution of all three edges to that one file.
- **The closed-set table (`:359-422`) and its closing note (`:436-442`) are untouched** — only the "Always-valid guard" line changes, to stay consistent with what the table and note already say.

## Verification

- Manual read: Step 4's post-`AskUserQuestion` sentence no longer says "verbatim" for both options 1 and 2; it names three distinct routing targets.
- Manual read: Step 5 contains three new blocks, each naming exactly one escalation option, positioned between "Non-convergence (terminal — no rollback)" and "Depth: spec."
- Manual read: the "option 2" block explicitly says steps 1–2 of "Depth: spec" do NOT run; the "option 1" block explicitly says all four steps do.
- Manual read: the "option 3" block reads structurally identical to the non-convergence no-op block (no-delete, no-sidecar-touch, proceed to 5.5).
- `grep -n "Root-cause categories\|Attach the root-cause category" src/skills/task-rescue/SKILL.md` → both lines now carry an escalation exemption.
- `grep -n "Always-valid guard" src/skills/task-rescue/SKILL.md` → the line now names `"escalated"` alongside `"planned:N"`/`"implemented:N"`.
- `git diff --stat` shows exactly one file changed: `src/skills/task-rescue/SKILL.md`.

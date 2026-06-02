# Code Review: roadmap-decompose — always emit two-tier output by invoking aif-note

**Reviewed change:** `.claude/skills/roadmap-decompose/SKILL.md` (the only functional change in the diff).
**Other diff entries** — `ROADMAP.md`, `notes/15-…`, the `plan-reviews/*`, `plans/03-*.{md,json}` — are process artifacts (roadmap checkbox, plan + review records), not code under review.

**Verdict:** The plan was implemented faithfully and the load-bearing fixes from the plan reviews all landed (Task 0–4). `Skill` is in `allowed-tools` (line 10), the `description` is refreshed (lines 3–8, keywords preserved, well under 1024 chars), the shared **Two-Tier Output** block exists (lines 280–294), both modes reference it, the Format section and Critical Rules are updated. However, there are **two medium correctness issues** in the runtime behavior the new instructions produce, plus minor nits.

---

## Findings

### 1. (Medium) Mode 1 persists spec notes to disk *before* the user confirms the roadmap — rejected tasks leave orphaned notes

In Mode 1, Step **1.3** now runs the Two-Tier Output procedure per milestone, which **invokes `aif-note`** (line 105, lines 286–287) — writing a real note file to `.ai-factory/notes/<NN>-…md` and consuming an `<NN>` number. Only afterward does Step **1.4** ask the user to confirm, offering "Remove/modify some tasks" and "Rewrite — let me give better input" (lines 124–132).

Consequence: if the user removes a task or chooses Rewrite, the spec notes for the discarded tasks have **already been written to disk** and there is no cleanup step. The result is orphaned note files that no roadmap contract line points to, plus burned `<NN>` numbers. The previous skill drafted specs in-memory and only persisted on save, so this is a behavioral regression introduced by the change. It also works against the determinism/clean-output goal the milestone is chasing.

**Recommendation:** invoke `aif-note` *after* the 1.4 confirmation rather than during 1.3 generation — i.e. draft full specs + run the Atomicity Gate in 1.3, present the proposed roadmap (with placeholder `Spec:` targets) in 1.4, and only after "Looks good — save it" run the note invocations and finalize the contract-line `Spec:` paths. Alternatively, add an explicit cleanup step for notes belonging to rejected/removed tasks. The same ordering risk is much milder in Mode 2.4 (the user supplied the tasks before notes are written), so the fix is mainly a Mode 1 concern.

### 2. (Medium) Mode 2.5 "update … if the milestone already has a `Spec:` note" conflicts with aif-note's create-by-default contract

Step 2.5 instructs: "invoke `aif-note` to write **(or update, if the milestone already has a `Spec:` note)** the spec note" (line 206). But `aif-note`'s own contract (`.claude/skills/aif-note/SKILL.md`) is create-by-default:

- Step 3 allocates a **new** `<NN>` by scanning for the highest existing prefix and incrementing.
- Important Rule 5: *"By default, always create a new file. Update an existing note only if the user explicitly asks to."*

So a bare invocation will **create a second note** with a new number, not update the existing one — leaving a stale note plus a duplicate, and the old `<NN>` orphaned. Because the plan/skill also mandate "do not override or alter aif-note's behavior," the "update" path is only reachable if decompose **explicitly tells aif-note to update note `<NN>-<slug>.md`** (which is within aif-note's documented behavior — an explicit caller instruction, not a behavior override).

**Recommendation:** make the update path explicit — when the selected milestone already carries a `Spec:` tag, the invocation must name that exact note path and instruct aif-note to update it in place; otherwise expect (and accept) a brand-new note and update the contract line's `Spec:` tag to the new path. As written, the instruction is ambiguous and will most likely yield duplicate notes.

### 3. (Low) Malformed `Spec:` tag example in the Two-Tier Output block (line 288)

Step 5 specifies "ending with the exact tag" but the example itself is mis-nested:

```
ending with the exact tag: `Spec: `.ai-factory/notes/<NN>-<slug>.md`.`
```

The backticks pair as code-span `"Spec: "` + plain text + a stray `` `.` `` — it does not render as the intended `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``. The canonical, correctly-rendered form already appears at lines 99, 307–309, and 317. Since this step is literally defining "the exact tag," the example should match those. Cosmetic, but it's the authoritative spec for the output format, so worth correcting.

### 4. (Low / nit) Wording in the Two-Tier block

- Line 292: "A gate split two invocations also run one after another." reads as a dropped possessive/verb — intended "A gate split's two invocations also run one after another."
- Line 286: "pass the task name as aif-note `$1` slug argument" — missing article ("as aif-note's `$1` slug argument"). Same minor drop on line 292 ("aif-note `NN` scan").

### 5. (Low / informational) Out-of-scope cosmetic edits

The diff also de-contracts prose throughout ("what's" → "what is", etc.) and **removes the ✅ / 🔨 / ⏳ status emoji** from the Mode 3 progress report (lines 255–262). These weren't called for by the plan ("small, surgical change"). Harmless, but the emoji removal slightly reduces the scannability of the Mode 3 report for no stated reason. Not a blocker — flag only so it's a conscious choice rather than incidental drift.

---

## Verified — correct and as-planned

- `Skill` added to `allowed-tools` (line 10); `aif-note` is model-invocable (`disable-model-invocation: false`), so the invocation will resolve. `roadmap-decompose`'s own `disable-model-invocation: true` is unchanged and correct (user-invoked entry point).
- Capturing the path aif-note **reports back** (Step 4, line 287) is the right mechanism — it keeps the `Spec:` tag accurate regardless of the `<NN>`/slug aif-note picks, and correctly drops note 09's `task-` prefix since aif-note owns naming.
- Sequential-invocation requirement (line 292) correctly prevents `<NN>` collisions from aif-note's highest-prefix scan.
- Atomicity Gate logic preserved in both modes (1.3.1, 2.4.1) and correctly relocated to run on the full spec before note/contract-line emission; splits documented as two notes + two lines.
- Mode 3 (`check`) logic untouched apart from the emoji nit — only flips `[ ]`→`[x]`, unaffected by the two-tier shape.
- Format section + Critical Rule 6 consistently encode the contract-line + spec-note model; per-task scoping (pass task name as `$1`, delimit the spec text) is present (line 286), addressing plan-review-2 finding 2.

---

## Recommended actions before implementation is considered done

1. **Fix #1** — move the Mode 1 `aif-note` invocations to after 1.4 confirmation (or add cleanup for rejected tasks) to avoid orphaned notes.
2. **Fix #2** — make the Mode 2.5 "update existing note" path explicit so it doesn't silently create duplicates.
3. **Fix #3/#4** — correct the malformed tag example (line 288) and the two wording drops.
4. **#5** is optional — restore the Mode 3 emoji if their removal was unintentional.

Findings #1 and #2 are behavioral and should be addressed; #3–#5 are low-cost polish.

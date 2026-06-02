# Plan Review — roadmap-decompose: ensure aif-note is loaded once, then write spec notes manually

## Summary

**Plan:** `.ai-factory/plans/07-roadmap-decompose-ensure-aif-note-is-loaded-once-then-write-spec-notes-manually.md`
**Target:** `src/skills/roadmap-decompose/SKILL.md`
**Risk Level:** 🟡 Medium — the plan's approach is correct and its line references are accurate, but its enumerated edit list is **incomplete** and contains one **self-contradiction**. An implementer following the bullets literally will leave stale per-task-invocation wording in the skill, which defeats the task's whole purpose (remove all per-task `aif-note` invocation language).

The intent (load `aif-note` once, then `Write` each note manually; keep two-tier shape, contract line, `Spec:` tag, char budget, Atomicity Gate) is well understood and faithfully matches the spec note `16-task-decompose-inline-notes-aif-note-format.md`.

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`): PASS. The change is a doc-only edit to one skill's `SKILL.md`; no module-boundary or dependency-model impact. Skill-invokes-skill coupling stays runtime-text only, consistent with the documented dependency model.
- **Rules** (`.ai-factory/RULES.md`): not present — WARN (optional file absent, no action).
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS. The work maps to the open milestone "roadmap-decompose: ensure aif-note is loaded once, then write spec notes manually" and links its spec note. Good linkage.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project overrides to apply.

## Critical Issues

None that block — this is a documentation edit to a skill, not runtime code. No security, migration, or API-correctness issues. The findings below are correctness-of-intent gaps that should be fixed before implementing, because leaving them re-introduces the exact confusion the task exists to remove.

## Findings

### 1. (Medium) Task 1 says "keep step 2 as-is" but step 2 contains the cruft being removed

Task 1 instructs: *"Keep step 1 (Draft the full spec) and step 2 (Apply the Atomicity Gate) as-is."* But step 2 of the Two-Tier Output procedure (SKILL.md line 289) currently reads:

> "…split into two tasks and run this whole procedure independently for each **(two note invocations + two contract lines, sequentially)**."

That parenthetical embeds exactly the per-task-invocation + "sequentially" model the task is deleting. Keeping it verbatim contradicts the goal and leaves "note invocations" / "sequentially" wording inside the very procedure being rewritten. **Fix:** step 2 must be reworded to "two notes + two contract lines" (drop "invocations" and "sequentially") rather than kept as-is.

### 2. (Medium) Task 2's enumerated list omits several remaining `aif-note` / "note invocation" mentions

Task 2's preamble says "Update every remaining mention," but its explicit bullet list reads as exhaustive and misses these live references (confirmed via grep of the current file):

- **Line 16** — the intro sentence under `# Decompose`: *"…a contract line in the roadmap and a full spec note written by `aif-note`."* Not in the list; should be reworded like the frontmatter and Critical Rule 6.
- **Line 105** — Mode 1 Step 1.3 rules: *"do **not** invoke `aif-note` yet; **note invocations** happen after the user confirms in Step 1.4."* Under the new model there is no per-task invocation; this should become "do not write the notes yet; notes are written after confirmation in Step 1.4."
- **Line 115** — Step 1.3.1 Atomicity Gate: *"both receive **note invocations** at Step 1.4 after confirmation."* → "both receive notes at Step 1.4."
- **Lines 193, 197** — Step 2.4.1 Atomicity Gate: *"before the **note invocation** — apply the gate"* and *"A split produces **two note invocations** + two contract lines."* → "before writing the note" / "two notes + two contract lines."

An implementer working the bullets literally will leave all of these. Recommend converting Task 2's preamble promise into explicit bullets for lines 16, 105, 115, and 193/197, so nothing is left to interpretation.

### 3. (Minor / observation) aif-note's in-context template is a research-summary shape, not a task-spec shape

The plan correctly states decompose must carry **no** note format of its own and rely on aif-note's in-context instructions. Worth noting for the implementer: aif-note's template is `Key Findings / Details / Open Questions` ("research summary"), not the `Current state / Target / Guards / Verify` shape seen in existing spec notes. This is a pre-existing design choice inherited from commit `0bfa177` (decompose "tells aif-note the content is a task spec; does not override its template"), and the spec note for this task explicitly puts the format out of scope. So this is **not** a defect in the plan — it faithfully preserves prior behavior — but the implementer should not be surprised that the manually-written notes follow aif-note's research template, and should not "improve" the format (doing so would violate the "no note-format of its own" guard).

## Things the plan gets right

- **Accurate line references** — every cited location matches the current file: Two-Tier Output ~284–298, Step 1.4 line 136, Step 2.4 line 187, Step 2.5 lines 208–210, contract-line rule line 321, Critical Rule 6 line 332.
- **Correct rejection of literal `git revert 0bfa177`** — the "Notes for the implementer" section rightly flags that the file moved from `.claude/skills/` to `src/skills/`, so a literal revert would touch wrong paths; targeted in-place edits reach the same end state. Good catch.
- **`allowed-tools` reasoning is sound** — keeping both `Skill` (one-time aif-note load) and `Write` (manual note authoring) is correct; the skill already has `Glob` to scan `.ai-factory/notes/` for the next `<NN>`.
- **Guards faithfully mirror the spec note** — at-most-once invocation, no per-task invocation, no self-described format, unchanged two-tier shape / contract line / `Spec:` tag / char budget / Atomicity Gate, and "do not modify aif-note."

## Recommendation

Address findings 1 and 2 (reword step 2 of the Two-Tier procedure; add explicit bullets for lines 16, 105, 115, 193/197) before implementing. The approach is otherwise sound and ready.

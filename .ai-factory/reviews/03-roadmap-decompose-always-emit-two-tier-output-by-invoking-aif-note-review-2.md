# Code Review 2: roadmap-decompose — always emit two-tier output by invoking aif-note

**Reviewed change:** `.claude/skills/roadmap-decompose/SKILL.md` (only functional change in the diff; `ROADMAP.md`, `notes/15-…`, `plan-reviews/*`, `plans/03-*`, `reviews/review-1` are process artifacts).

**Verdict:** The two medium findings from review-1 are both **properly resolved**, along with the low-severity nits. The change is essentially ready. One minor wording ambiguity remains (low, non-blocking).

---

## Review-1 findings — all addressed

### ✅ 1. Mode 1 no longer persists notes before confirmation (was Medium)
Step 1.3 is renamed "Generate **draft** roadmap" and now emits placeholder `` Spec: `<note pending>`. `` lines with an explicit instruction: *"do **not** invoke `aif-note` yet; note invocations happen after the user confirms in Step 1.4"* (line 105). Step 1.4 adds a finalization block that runs the Two-Tier Output procedure (steps 3–5) per **confirmed** milestone after "Looks good — save it", and states *"Milestones removed or rewritten during options 2–4 receive no note invocation; only the confirmed set gets notes"* (line 136). The Atomicity Gate (1.3.1) is consistently re-scoped to produce draft contract lines, deferring note invocation to 1.4. This fully removes the orphaned-note / burned-`<NN>` regression. Good fix — and using `<note pending>` placeholders also sidesteps the `<NN>` collision entirely until the sequential finalization pass.

### ✅ 2. Mode 2.5 "update existing note" is now explicit (was Medium)
Step 2.5 now splits the note-handling rule (lines 208–210): if the milestone already carries a `Spec:` tag, *"instruct `aif-note` to **update** the named note file in place (pass the exact existing note path as an explicit instruction to update rather than create)"*; if it has no tag (legacy inline), create a new note and add the tag. This is consistent with `aif-note`'s contract (Important Rule 5 — "update an existing note only if the user explicitly asks to") and resolves the duplicate-note risk without altering `aif-note`.

### ✅ 3. Malformed `Spec:` tag example corrected
Two-Tier Output step 5 (line 292) now renders the canonical form `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``, matching lines 99/311–313/321.

### ✅ 4. Wording drops fixed
Line 296 "A gate split's two invocations also run one after another"; line 290 "aif-note's `$1` slug argument". Both corrected.

---

## Remaining findings

### 1. (Low) "Create a draft of `$TARGET_FILE`" can be misread as writing the file with `<note pending>` placeholders
Step 1.3 says *"Create a draft of `$TARGET_FILE`"* (line 90), while the actual file write is deferred to the 1.4 finalization (*"then write the final `$TARGET_FILE`"*, line 136). The surrounding cues ("Show the **draft** roadmap", "do not invoke `aif-note` yet") make the intent clear enough that a careful agent will keep the draft in-memory, but the phrase "Create a draft of `$TARGET_FILE`" still reads ambiguously as a disk write. If an agent does write it, the on-disk roadmap would briefly contain `` Spec: `<note pending>`. `` placeholders, and an abandoned run (user never reaches "save it") would leave them behind.

**Recommendation (optional polish):** tighten 1.3 to "Draft the roadmap **in memory (do not write `$TARGET_FILE` yet)**" so the only disk write is the 1.4 finalization. One-line clarification; not blocking.

### 2. (Informational) Mode 2.5 update path depends on `aif-note` honoring an explicit "update" instruction
`aif-note`'s documented workflow (its Step 3 / "Note File Handling") is create-oriented — its update behavior is only stated as a permission in Rule 5, not described mechanically. The 2.5 instruction is the correct way to reach it without modifying `aif-note`, but the actual update fidelity rests on `aif-note` interpreting "update note `<path>` in place" correctly at runtime. Acceptable as-is given the "do not alter aif-note" constraint — flagged only so it's a known dependency, not a defect.

### 3. (Informational) Mode 3 status emoji (✅/🔨/⏳) remain removed
Carried over from review-1 finding #5 — out-of-scope cosmetic drift, not reinstated. Harmless; noting only for awareness in case the removal was unintentional.

---

## Verified — correct and as-planned
- `Skill` in `allowed-tools` (line 10); `aif-note` model-invocable; `roadmap-decompose`'s own `disable-model-invocation: true` unchanged and correct.
- Two-Tier Output block (lines 284–298) is coherent; Mode 1 correctly references "steps 3–5" (draft + gate already done in 1.3/1.3.1), Mode 2 references the full procedure.
- Sequential-invocation requirement preserved (line 296) and reinforced by the `<note pending>` → finalization flow.
- Format section + Critical Rule 6 consistently encode the two-tier model; per-task scoping (task name as `$1`, delimited spec text) present (line 290).
- Mode 3 logic unchanged apart from the emoji nit.

---

The substantive issues are resolved. Remaining item #1 is a one-line wording polish; #2–#3 are informational. No blocking findings.

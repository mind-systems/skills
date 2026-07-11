# Plan: aif-docs: pyramid pass (second diet)

## Context
Continue the established `references/` progressive-disclosure pattern on `src/skills/aif-docs/SKILL.md` (454 lines): move the remaining long per-state procedures (State A generation, State B split, State C audit) behind branch pointers so the body drops materially under 300 lines while staying byte-identical in behavior — the skill remains the ТЗ-writer, sharpened not blurred.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Constraints (apply to every task)
- **Behavior-identical.** A State A / B / C run must produce the same dialogs, same files, same index rows as today. All moved text lands **byte-identical** — same wording, headers, code fences, `<resolved docs dir>` placeholders.
- **Verbatim-protected, never compressed:** every `AskUserQuestion` dialog (contract text); the Core Principles wording, above all the governing-spec **genre sentence** at `SKILL.md:19` (present tense whether the code exists yet or not) and Principle 6 **state-not-process**. These are never touched.
- **Closure rule:** any sentence stating a contract is protected verbatim whether or not named here — a contract-bearing sentence found mid-edit joins the protected set on the spot.
- **Re-basing rule (per spec 30 — the one documented exception to byte-identical):** inside every moved block, a relative reference is rewritten for its new base — a `references/<X>` pointer becomes the sibling form `<X>` once the text lives inside `references/`; a pointer to a step number/label that ceases to exist is re-pointed to its new home. Applied symmetrically to every occurrence (grep, never enumeration); all other bytes identical. An occurrence found mid-edit is fixed on the spot.
- **Extend the existing mechanism, don't invent a second one.** New files go under the existing `src/skills/aif-docs/references/` dir; each is reached by a one-line "→ read `references/<file>` when …" pointer in the same style as the already-established `topic-guides.md` / `html-generation.md` / `consolidation.md` / `REVIEW-CHECKLISTS.md` pointers.
- **Frontmatter unchanged.**
- **Body kept first-class:** state detection (Step 1 A/B/C), Core Principles, the CLAUDE.md `## Documentation` index contract + the key-artifact updating duty, when-to-read pointers.

## Tasks

### Phase 1: Carve the per-state procedures into references (byte-identical moves)

- [x] **Task 1: Move the State A generation procedure to a reference**
  Files: `src/skills/aif-docs/references/generate-state-a.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/generate-state-a.md` and move into it, **byte-identical**, the body of "Step 2 (State A): Generate from Scratch" — subsections **2.1** (topic analysis + its `AskUserQuestion` dialog and "Based on choice" branches), **2.2** (README structure template + "Key rules for README"), and **2.3** (doc-file generation, which already points to `references/topic-guides.md`).
  **Do NOT move 2.2b** — the "Update the CLAUDE.md Documentation Index" block is the key-artifact contract; it is lifted into the body in Task 4. In the moved 2.1/2.2/2.3 text, where the original flow reached 2.2b, leave a one-line pointer back to the body's CLAUDE.md-index contract section.
  The `AskUserQuestion` topic-selection dialog lands byte-identical.
  **Controlled deviation (sibling-path fix):** 2.3's line *"Content guidelines per topic → read `references/topic-guides.md` when generating State A pages"* now lives *inside* a `references/` file, making `references/topic-guides.md` a broken reference-to-reference path. Rewrite that one pointer to the sibling form **`topic-guides.md`** (the target sits beside it in the same dir) — a documented exception to byte-identical, in the same spirit as the 2.2b-pointer and State-B-2.3-redirect deviations. This is the only path rewrite in the moved State A text; all other bytes are identical.

- [x] **Task 2: Move the State B split procedure to a reference**
  Files: `src/skills/aif-docs/references/split-state-b.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/split-state-b.md` and move into it, **byte-identical**, the body of "Step 2 (State B): Split Existing README into the resolved docs directory" — subsections 2.1 (analyze / stays-vs-moves lists), 2.2 (the split-proposal dialog block), and 2.3 (execute the split). Where 2.3 references creating/updating the CLAUDE.md `## Documentation` section, point to the body's CLAUDE.md-index contract section.

- [x] **Task 3: Move the State C audit procedure to a reference**
  Files: `src/skills/aif-docs/references/audit-state-c.md` (new), `src/skills/aif-docs/SKILL.md`
  Create `references/audit-state-c.md` and move into it, **byte-identical**, the body of "Step 2 (State C): Improve Existing Docs" — subsection 2.1 (the audit checks, including the referent-conditional stale-content rule, legacy-README-table check, and coordination-trio staleness), 2.1.1 (standards-compliance, which already points to `references/REVIEW-CHECKLISTS.md`), and 2.2 (the audit-results proposal block). This is the "audit checklists" the spec calls out for moving.
  **Controlled deviation (sibling-path fix, symmetric to Task 1's):** 2.1.1's line *"For the full compliance table and auto-fix rules → read `references/REVIEW-CHECKLISTS.md` (Standards Compliance section)"* (`SKILL.md:327`) moves inside a `references/` file, so per the re-basing rule rewrite that one pointer to the sibling form **`REVIEW-CHECKLISTS.md`**. This is the only path rewrite in the moved State C text; all other bytes are identical. (Grep confirms `:253` and `:327` are the only two moved-into-`references/` pointers of this shape; `:102`, `:355`, `:363` stay in the body untouched.)

### Phase 2: Slim the body and wire the pointers

- [x] **Task 4: Rewire the body to pointers + lift the CLAUDE.md-index contract** (depends on Tasks 1-3)
  Files: `src/skills/aif-docs/SKILL.md`
  - Lift the former **2.2b "Update the CLAUDE.md Documentation Index"** block out of the State A branch into a first-class body section (byte-identical content) — the single home for the index contract, since States A and B both reach it. Keep it adjacent to the state-routing flow so its first-class status is visible.
  - Replace the three now-moved procedure bodies with short branch pointers in the established style, each naming the triggering state, e.g.:
    - State A → "→ read `references/generate-state-a.md`"
    - State B → "→ read `references/split-state-b.md`"
    - State C (without `--web`, and the Audit paths of the `--web` routing) → "→ read `references/audit-state-c.md`"
  - **Keep in the body, byte-identical:** Step 1 state-detection table; the State-C-`--web` `AskUserQuestion` routing dialog (Step 1); the Step 1.1 consolidation `AskUserQuestion` dialog + its routing; Step 4 review flow (already points to `REVIEW-CHECKLISTS.md`); the Step 4.1 cleanup `AskUserQuestion` dialog; Step 5 AGENTS.md; Artifact Ownership; Important Rules.
  - **Required internal-pointer fix (the one allowed edit to Step 5):** lifting 2.2b drops the `#### 2.2b` numbered heading, so the label `2.2b` ceases to exist. `SKILL.md:434` reads *"the CLAUDE.md `## Documentation` section (Step 2.2b) is the single source…"* — re-point that `(Step 2.2b)` to the new first-class section's title. This is the sole content change to Step 5; everything else in Step 5 stays byte-identical. (Cross-refs internal to the moved State C block — `(see 2.1.1)` at `:323`, `(Step 2.2)` at `:329` — stay coherent because 2.1.1 and 2.2 travel together into `audit-state-c.md`; no fix needed there.)
  - Verify the State-C-`--web` routing still resolves: "Generate HTML only" / "Audit & improve" / "Audit only" branches must land on the correct references (`audit-state-c.md` for the audit paths, `html-generation.md` for HTML) with no step-number dangling.
  - **Result gate:** body materially under 300 lines; every moved procedure reachable behind exactly one pointer; every `AskUserQuestion` dialog and the genre sentence at `:19` byte-identical to the pre-diet file. A State C run must yield an identical proposal set to the pre-diet baseline.

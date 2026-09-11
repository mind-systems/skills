## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/41-38-1-the-numbering-scan-sees-past-ninety-nine.md`
**Files Reviewed:** 2 target files (`src/skills/note/SKILL.md`, `src/skills/task-rescue/SKILL.md`) plus the task spec, the contract line, and every caller in `note`'s reverse graph
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present. `note` is a load-once engine; the plan honors the engine contract by (a) enumerating the reverse graph (`roadmap-engine`, `roadmap-outline-deep`, `task-rescue`, `command-handoff` — verified with `grep -ln '^loads:.*\bnote\b'`), (b) keeping the `<NN>` symbol callers resolve by name, and (c) fixing the one caller that copied the engine's pattern instead of pointing at it. No boundary violation. OK.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (missing optional file; nothing to check against).
- **Roadmap** — Task is `38.1` in the named roadmap `.ai-factory/roadmaps/trickster77777.md` under Phase 38 "one numbering rule, not three"; `Spec:` tag resolves to `.ai-factory/specs/trickster77777/125-note-numbering-sees-past-ninety-nine.md`, read in full. The phase header carries no `Governing spec:`; the task spec is the leaf of the chain. Plan aligns with the contract line and the spec on every requirement: any-length read, numeric comparison, four-digit write, `0001` default, `9999` bound with the destination named, no renames, `roadmap-test-coverage`/`aif-plan` untouched. OK.

### Ground-truth verification of the plan's claims

Every factual claim in the plan was checked against the files, not the plan's own description of them:

- The five sites in `src/skills/note/SKILL.md` exist exactly as quoted (Destination directory bullet; the `<NN>` width bullet; the determination sentence; the Folder style paragraph; the Note File Handling bullet). `grep -n '\[0-9\]\[0-9\]'` on the file returns four hits, matching the plan's statement that site 2 carries the width claim without the glob — so task 1's intermediate check ("hits only sites 3, 4, 5") is correct.
- `grep -rn '\[0-9\]\[0-9\]' src/skills src/commands` today hits `note` (×4), `aif-plan` (×2), `roadmap-test-coverage` (×1), `task-rescue` (×1). After the plan's edits the residual set is exactly `aif-plan` + `roadmap-test-coverage`, as the final task asserts. Correct.
- `task-rescue` line "its per-directory `[0-9][0-9]-*.md` numbering scan" sits in the paragraph opening "**All three of `note`'s hooks are supplied**", and the sentence "`note`'s own mechanics — numbering, `mkdir -p`, folder style — are not restated here" follows it. The plan's reading is accurate and the one-home-per-fact correction is the right call.
- `<NN>` is referenced by name in `roadmap-engine`, `roadmap-outline-deep`, `roadmap-test-coverage`, `architect-editor-engine`, and `docs/philosophy/multiuser-roadmaps.md`; none of them state a width. Keeping the placeholder name is correct and the plan's justification holds.
- `allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob` — listing the directory is already granted; no frontmatter change needed. Correct.
- `active/skills/note → ../../src/skills/note`; there is no upstream `note` to reconcile. The edit lands in the file that is actually loaded.
- `.ai-factory/specs/trickster77777/` holds 45 files with real top `126-…` — the collision the spec describes is real.

### Findings

1. **Task 4's suggested wording contradicts task 5's whole-file verification.** Task 4 instructs the Folder style paragraph to say "a three- or four-digit name outranks any **two-digit** one", while task 5's verification requires `grep -n '\[0-9\]\[0-9\]\|two-digit\|start at `01`' src/skills/note/SKILL.md` to return nothing. An implementer who follows task 4 as written fails task 5's check and has to guess which of the two to honor. Resolve one way: either narrow the verification pattern to the phrases that actually carry the old rule (`zero-padded two-digit` / `two-digit sequence`), or reword task 4's example so it does not use the phrase (e.g. "outranks any shorter-prefixed one"). Either is fine; the plan should pick.

2. **The bound predicate is stated two ways.** The Context section pins "when the highest number found is `9999` (or greater)", but task 3's instruction text says "when the highest number the scan finds is already `9999`". The spec says "at a destination already holding `9999`". The "(or greater)" form is a sensible defensive extension (a hand-made five-digit name should also stop the writer rather than produce `10000`), but the plan should state one predicate in the task that the implementer will actually transcribe, so the written rule is not left to chance.

3. **Task 5's `9999` verification list is incomplete.** Task 3 also appends a bound clause to Important Rules Rule 5 ("a destination at `9999` produces no file"), so `grep -n '9999'` will hit Step 3, Step 4, Important Rules, and Note File Handling — four sites, not the three the verification names. As written ("hits …") it does not fail, but an implementer reading it as an exhaustive list may treat the Rule 5 hit as stray and strip it. List all four.

### Positive Notes

- The plan reads ground truth by the text that opens each site, never by line number, and states each edit as a change to a named passage — exactly the reference discipline the repo asks for.
- Reading and writing are kept as two rules and worded as two rules; this is the one place a careless rewrite would silently reintroduce the defect (a four-digit *glob*), and the plan forecloses it explicitly.
- Collapsing site 5 into a pointer instead of a fourth copy of the rule, and correcting `task-rescue`'s copied glob, both move the file toward one home per fact rather than just patching the pattern in place.
- The bound is placed before `mkdir -p`, `Write`, and the sibling reads — so nothing is created for a note that is not written — and surfaced in Step 4 as its own report form rather than overloading "Note saved:".
- Intermediate grep checkpoints after each task make the sequence self-verifying and the dependency order between tasks is right (the scan definition lands first; every later site points at it).

## Deferred observations

- Affects: Phase 38 / `src/commands/command-handoff.md` (a caller outside this task's file boundary) — `command-handoff` § "Step 2 — Delegate to `note`" states "Its own Step 4 report is **not** surfaced — once `note` completes, emit only the minimal paste-back pointer below," and Step 3 always emits a pointer to the new handoff file. Once `note` gains the `9999` bound, this caller will suppress the "Numbering bound reached" report and emit a paste-back pointer to a file that was never written. `.ai-factory/handoffs/` sits at `22` today, so nothing is exposed now, but the caller's contract with the engine no longer covers every outcome the engine can produce. Whoever owns the callers' side of Phase 38 (or a follow-up task) should let the bound report through — or have the command stop — when `note` writes nothing.

# Review — 57.3 the skeleton takes the bead

## Code Review Summary

**Files Reviewed:** 1 changed product file (`src/skills/roadmap-decompose-skeleton/SKILL.md`, 3 hunks) + 1 unrelated staged planning artifact + 12 context surfaces
**Risk Level:** 🟢 Low — three text edits in one skill body, all mechanically checked against the pinned spec text; nothing executes, nothing is imported, no interface changes shape.

**Read:** `git status`, `git diff HEAD` in full; `src/skills/roadmap-decompose-skeleton/SKILL.md` (the whole file, before and after); the plan (iteration 2, all four tasks); plan-review-1 and plan-review-2; `.ai-factory/specs/trickster77777/158-…md` (the pinned block, extracted and diffed mechanically); `.ai-factory/specs/trickster77777/151-…md` (phase note); contract line 57.3 in `.ai-factory/roadmaps/trickster77777.md`; `src/skills/polymorphism-philosophy/SKILL.md` and its `active/skills/` symlink; `src/skills/test-philosophy/SKILL.md` (the precedent the load phrasing mirrors); `CLAUDE.md` § "Dependencies and the skill graph", § "SKILL.md frontmatter (required fields)", § "Key constraints"; `docs/counts-go-stale.md`; `docs/sakshi-harness/skill-cycle.md` § "Спецификация до кода"; `docs/sakshi-harness/skill-graph.md` § "Домены — по стволам"; `src/skills/orchestrator-artifacts/SKILL.md` § 5; the whole `loads:` graph at HEAD and at the working tree.

## What was verified, and how

**The replacement Lens 1 is word-for-word the spec's pinned text.** Extracted the two quoted lines from spec 158 § "The change" and compared them to lines 65–71 of the file programmatically, normalising whitespace only: paragraph match `True`, restraint bullet match `True`. No word added, dropped, or reordered.

**The re-wrap the plan ordered was performed, and to the measured convention.** The new block runs 65–86 columns (paragraph 86/78/83/65, bullet 84/84/17), inside the plan's `≤ ~90`; the restraint bullet continues at a two-space indent, matching the form it replaced. The file's longest line is still 96 and sits outside this block, so the file's own wrapping ceiling did not move. No trailing whitespace anywhere in the file; UTF-8, no BOM, no CRLF, ends in exactly one newline.

**The old justification is gone in substance, not just in phrasing.** The testability clause ("where an interface / abstract-class skeleton genuinely makes the surface testable") and the restraint sentence that restated it ("Only extract a skeleton where it makes a shared or non-obvious surface testable") are both removed, and the seam is now cut on the loaded unit's event. This is the contract line's actual subject — the *reason* a seam is cut, not its wording — and it changed.

**Lens 1 restates nothing of the loaded unit.** The new text names `polymorphism-philosophy` and nothing else about it: no copy of the question, the trigger, the exemption, or the vocabulary. It matches Lens 2's construction against `test-philosophy` clause for clause ("Load `X` once via the `Skill` tool, then apply its … to …"), so Critical Rule 2's standard is met and the question keeps exactly one home.

**The `loads:` edge resolves on both sides.** `loads: roadmap-engine test-philosophy polymorphism-philosophy` — existing two names and their order unchanged, third appended, space-separated. Each name resolves to a real `src/skills/<name>/SKILL.md` **and** to an `active/skills/<name>` symlink; `polymorphism-philosophy`'s own `name:` field is byte-identical to its directory name, so the identifier the caller writes is the one the loader resolves. The engine side needed nothing: its load-once sentence, its reverse-graph grep line, and its naming of this caller were already in place from 57.2, and that reverse grep now returns a real caller for the first time. `allowed-tools` already carried `Skill`; no tool was added, and none was needed.

**Frontmatter is intact apart from that one line.** `name`, `description`, `argument-hint` (still quoted), `disable-model-invocation`, `allowed-tools` all byte-identical. The `description:` field was deliberately left alone, as the plan argued — "shares a type surface" is not falsified by a lens that fires when a kind gains a second member, and rewriting always-loaded text is its own decision.

**The count repair is exactly the deletion the plan ordered.** "delegated to two shared skills" → "delegated to shared skills". The two bullets, the paragraph below them, and the rest of the section are byte-identical; no `polymorphism-philosophy` bullet was added, honouring the spec's ruling. No `DEVIATION` annotation was emitted, correctly — the plan ordered the edit, so there was no plan/file contradiction to record.

**Nothing else in the file moved.** The diff is three hunks and no more: Lens 2, Lens 3 with both their restraint clauses and canon citations, Steps 2–4, and the whole Critical Rules list (including items 5 and 6) are untouched, as the spec enumerates.

**The spec's sweep invariant holds.** Re-run from the repo root, `grep -rln "genuinely makes the surface testable\|loads: roadmap-engine test-philosophy$" .` now returns three paths — spec 158, phase note 151, and the plan file. The target dropped out on both alternatives, which is the invariant. All three survivors pass the plan's rule rather than a count: the spec and the note quote the old wording as the moment they describe, and the plan matches on the grep command quoted inside its own fenced block, not on either passage. No path outside that set appeared, so the spec's blast-radius claim still holds.

## One thing outside the change, for the operator

`.ai-factory/notes/07-architect-buffer.md` is staged alongside this task's edit. Its change — a correction to the bullet about phase notes and what a planner walks — was already in the working tree before this run began and has nothing to do with 57.3. It is not a defect in the implementation, and I have not touched it; but as staged, a commit made now would carry it under this task's message. Unstage it, or commit it separately, before closing the task.

## Findings

None. Every edit matches the pinned spec text mechanically, the re-wrap holds to the measured convention, both sides of the new `loads:` edge resolve, and the sweep invariant the plan set is satisfied.

The two deferred observations plan-review-2 raised — the unit's time-entry evidence clause reading for a landed diff while its only consumer runs at planning time, and the two-entry bullet list inheriting the role the deleted number vacated — remain open and are not re-homed here; they are recorded in that artifact and route to spec `157-…md` and `158-…md` respectively.

## Deferred observations

- Affects: `docs/sakshi-harness/skill-graph.md` § "Домены — по стволам" (phase 57 / task 57.3) — the sentence "Стволов у пакета четыре" names four trunks and derives them from a rule this task's edge feeds: "Границы доменов не назначаются — они **выводятся** из графа `loads:` … истина всегда во frontmatter". Run that derivation and the distinct `loads:` targets are seven, not four: the four named plus `architect-editor-engine`, `architect-pairing-engine` (both already there at HEAD, so the census was false by two *before* this task) and now `polymorphism-philosophy`. This task is therefore not the defect's cause and correctly did not touch it — the plan's `Docs: no` and the spec's blast radius both scope it out, and repairing a doc census already false at HEAD is outside a task's own file boundary. But the count is the same census class `docs/counts-go-stale.md` rules out, sitting in a doc whose own paragraph says the frontmatter is the truth, and it now misses three members. The repair belongs in that doc: either the number and the enumeration give way to the derivation command the paragraph already carries, or the sentence says which trunks it is naming and why the rest are out.

REVIEW_PASS

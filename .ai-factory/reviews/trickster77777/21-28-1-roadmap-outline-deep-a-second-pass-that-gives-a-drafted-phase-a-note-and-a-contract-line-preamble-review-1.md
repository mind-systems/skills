# Review — 28.1 `roadmap-outline-deep`: a second pass that gives a drafted phase a note and a contract-line preamble

**Plan:** `.ai-factory/plans/trickster77777/21-28-1-…preamble.md`
**Task spec:** `.ai-factory/specs/trickster77777/102-roadmap-outline-deep.md`
**In scope (the task's four paths):** `src/skills/roadmap-outline-deep/SKILL.md` (new, 131 lines), `active/skills/roadmap-outline-deep` (new symlink), `CLAUDE.md`, `src/skills/roadmap-prune/SKILL.md`
**Risk level:** 🟢 Low — the wiring is correct, the prune capture is complete and consistent, and the skill now reads both the docs and the code; one sentence in Step 2 survives from before the note was cut down to a short distillation and contradicts the size the note is now given.

The working tree also carries planning-side edits outside the task's file boundary (`.ai-factory/roadmaps/trickster77777.md` contract line, `.ai-factory/specs/…/102`, `.ai-factory/notes/05`, `06`, `.ai-factory/handoffs/13`). They are consistent with the implementation and are not reviewed as code changes; the roadmap now carries exactly one `Governing spec:` line (`:11`, Phase 19's), so the two lines added to phases 28 and 29 during an earlier repair are confirmed reverted.

## Mechanical verification (all pass)

Counts taken against a whitespace-normalized read with `**` and backticks stripped from both sides, never a line-oriented `grep`:

- `name: roadmap-outline-deep` → 1; `loads: roadmap-engine note` → 1; `allowed-tools: Read Write Edit Glob Grep AskUserQuestion Skill` → 1; `argument-hint: "[phase or slug]"` bracket-quoted; `disable-model-invocation: true`; `name` equals the directory name; body 131 lines (≤ 500); `description` 529 chars (≤ 1024).
- `](.ai-factory/specs/` → 1; `.ai-factory/specs/<slug>/` → 2; `.ai-factory/specs/` → 4; `Phase note:` byte-exact → present; `200` → 1; `500` → 1.
- `roadmap-prune`, seven sites read individually: `:272` heads Step 5 with both tokens; item 1's capture at `:281-290` keys on the literal token and carries the existing carve-outs by reference; item 3 `:315` folds the note paths into the same `rm -f` and root join; `:317` and `:444` each name both captured tokens with the directory-scan prohibition intact; `:339` ("only after Step 5's capture of tags and pointers has run"); `:349-350` points the emptied-phase sweep back at the capture; `:411` reports "the task specs and phase notes deleted in Step 5". Negative span `only through the pruned [x] lines' Spec: tags` → **2 pre-edit, 0 post-edit**.
- `CLAUDE.md` `:74` and `:189` both carry the skill; `:33` (doc-index prose) untouched. `roadmap-outline-deep` in `docs/sakshi-harness/skill-cycle.md` → 2, unchanged and committed.
- `active/skills/roadmap-outline-deep` → `../../src/skills/roadmap-outline-deep`, resolves to a readable `SKILL.md`.
- `git diff HEAD -- src/skills/note src/skills/roadmap-engine src/skills/roadmap-outline src/skills/task-rescue docs/` → empty. `git status --short -uall -- src/ active/ CLAUDE.md` → exactly the four expected paths.

The rework since the last implementation is coherent across all three layers: skill, spec item 1, and plan all now say the pass reads the docs the phase's header and preamble link (`a Governing spec:` line being one such link and nothing more) plus the code the phase is about, and that the note is short and in words. No trace of the withdrawn concepts survives anywhere — grep for `governing-spec hole`, `phase-header gap` and `owned by` returns nothing in skill, spec or plan.

## Findings

### 1. Step 2 still promises the note holds the preamble's overflow, which the note's own size rule makes impossible (`src/skills/roadmap-outline-deep/SKILL.md:97-98` vs `:71-73`)

Step 2's budget bullet:

> - **Budget** — rewrite the phase preamble down to **~200–500 characters**. What overflows that budget belongs in the note, not in the preamble.

The verbosity directive the note is written under:

> - **Verbosity directive** — short: a few sentences more than the preamble, grounded in the docs and code read at Step 0, a `file:line` where a claim needs one, never a transcript of the conversation.

These two cannot both hold. The task exists because preambles absorb note-sized prose — spec 102 § "Current state" measures the observed ones at 1200–1900 characters against 475–498 in a direction that keeps them short. Compressing an 1800-character preamble to 500 leaves ~1300 characters of overflow that Step 2 assigns to the note, while the note is capped at "a few sentences more than the preamble". The container is smaller than what it is told to receive.

This is a leftover, not a design choice: the sentence dates from before the note was cut down to a short distillation, and the current spec no longer supports it. Spec 102 item 1 now frames the note as *"short and in words: it states what is not yet as the docs say — this and this — with links to those docs, and that is the essence of the phase, what decomposition cuts tasks from"* — a distillation of one specific thing, not a home for whatever the preamble sheds.

*Failure scenario:* the pass runs over a phase with a 1700-character preamble. Step 2 rewrites that preamble in place, down to 500 characters. The agent then reads two contradictory instructions and resolves them one of two ways. Either it honors Step 2 and writes a 1400-character note — restoring exactly the note-sized prose the direction set out to shrink, one file further from the roadmap, and against the spec's "short" — or it honors the verbosity directive, writes the short note, and the remaining ~1200 characters of pinned decisions and gating context are gone from both surfaces in one edit. Nothing warns the user which happened; the roadmap is recoverable only through git.

*Fix, one sentence, inside this file:* drop the overflow clause and say what the compression actually does — the preamble keeps the phase's gate and its pointer, the note states what is not yet as the docs say, and prose that is neither is dropped deliberately, not relocated. That matches the spec, keeps the note short as the user ruled, and stops the pass from promising a home it does not have.

### 2. Minor — the in-place rewrite branch bypasses `note`, and the note's content contract is stated only as `note`'s hooks (`src/skills/roadmap-outline-deep/SKILL.md:58-73` vs `:85-88`)

Step 1 introduces the template and verbosity rules as *"`note` with all three of its caller hooks supplied"*, and the re-run rule then routes the common case away from `note` entirely:

> - **Where a phase preamble already carries a `Phase note:` pointer, rewrite the note in place at the path that pointer names** — with `Write`/`Edit` directly, never through `note` — and leave the pointer byte-identical.

On that path no hook is passed to anything, so the two rules that define what a phase note *is* — short, in words, what is not yet as the docs say, `file:line` where a claim needs one — are formally attached to a mechanism the branch does not use. Every re-run after the first deepening pass takes this branch, so it governs most writes over a roadmap's life. The risk is low (the whole skill is in context when the branch runs), but one clause closes it: the in-place rewrite produces the same note the hooks describe — same template, same verbosity — only through `Write`/`Edit` instead of through `note`.

## Deferred observations

Recovered from `.ai-factory/handoffs/13-phase-note-plain-behavior-no-ceremony.md` § 3, where they were parked when the previous run's review files were deleted; re-verified against the files this pass. All are outside this task's four-path boundary — for a ruling, not tasks.

- `docs/sakshi-harness/skill-cycle.md:55` says prune deletes completed tasks *"вместе с отработавшими артефактами и их task-spec"*; after this task it also deletes phase notes.
- `docs/philosophy/multiuser-roadmaps.md:47` describes `.ai-factory/specs/<имя>/` as the home of task specs resolved *"всегда … через `Spec:`-тег contract-line"*; it now also holds phase notes resolved through `Phase note:` on a phase preamble, sharing the same per-directory `<NN>` counter.
- `docs/sakshi-harness/skill-graph.md` § "Воронка в один дистиллятор" names only `command-handoff` as a direct caller of `note`; `roadmap-outline-deep` is now a second, and § "Домены — по стволам" derives domain boundaries from the `loads:` graph.
- Nothing preserves a `Phase note:` pointer through a `roadmap-outline` / `roadmap-engine` rewrite of a preamble: prune keys on the literal token, so a rewrite that drops it orphans the note in a directory nothing scans. The in-place re-run rule closes this for re-runs of this pass only.
- `note`'s folder-style layer (`src/skills/note/SKILL.md:35`, `:59`) now style-matches across two genres in one directory — phase notes and task specs. Caller hooks outrank folder style, so structure is safe; only unstated register can drift.

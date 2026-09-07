# Re-review — 28.1 `roadmap-outline-deep`: a second pass that gives a drafted phase a note and a contract-line preamble

**Previous review:** `…-review-1.md` (two findings).
**Changed since:** `src/skills/roadmap-outline-deep/SKILL.md` only — 131 → 136 lines, sha1 `2460e660…` → `c2fd339a…`. `src/skills/roadmap-prune/SKILL.md` (`3c40dda3…`), `CLAUDE.md` (`2f4f5481…`) and the symlink are byte-identical to the previous pass.
**Risk level:** 🟢 Low — both findings are fixed at the source, no new issue found in the changed file or anywhere in the task's four paths.

## Verdicts on previous findings

### Finding 1 — Step 2 promised the note holds the preamble's overflow, which the note's size rule made impossible → **Fixed**

`src/skills/roadmap-outline-deep/SKILL.md:99-103`, current content:

> - **Budget** — rewrite the phase preamble down to **~200–500 characters**, keeping the phase's gate and its `Phase note:` pointer. The note states what is not yet as the docs say, per Step 1's template — it is a short distillation, not a home for whatever the preamble sheds. Prose that is neither the gate nor that distillation is dropped deliberately, not relocated.

The contradicting sentence ("What overflows that budget belongs in the note, not in the preamble") is gone. What the compression keeps is now named — the gate and the pointer — the note is explicitly a distillation rather than a container, and the remainder is dropped as a stated decision rather than silently. The verbosity directive it conflicted with is unchanged at `:71-73`:

> - **Verbosity directive** — short: a few sentences more than the preamble, grounded in the docs and code read at Step 0, a `file:line` where a claim needs one, never a transcript of the conversation.

The two now agree: a short note, a short preamble, and no promise that either absorbs the other. This also puts the skill in step with spec 102 item 1, which frames the note as *"short and in words … that is the essence of the phase, what decomposition cuts tasks from"*.

### Finding 2 — the in-place rewrite branch bypassed `note`, leaving the rewritten note with no stated content contract → **Fixed**

`:85-89`, current content:

> - **Where a phase preamble already carries a `Phase note:` pointer, rewrite the note in place at the path that pointer names** — with `Write`/`Edit` directly, never through `note` — and leave the pointer byte-identical. The in-place rewrite produces the same note the template and verbosity directive above describe — same content contract — only written through `Write`/`Edit` instead of through `note`.

The added sentence binds the branch to the same template and verbosity rules, so the path every re-run takes after the first deepening pass is no longer governed only by hooks it does not pass.

## Full re-review — no new findings

The whole skill was re-read (136 lines), plus the current `roadmap-prune`, `CLAUDE.md` and the symlink. Counts taken against a whitespace-normalized read with `**` and backticks stripped from both sides, never a line-oriented `grep`:

- Frontmatter: `name: roadmap-outline-deep` → 1 and equal to the directory name; `loads: roadmap-engine note` → 1; `allowed-tools: Read Write Edit Glob Grep AskUserQuestion Skill` → 1; `argument-hint: "[phase or slug]"` bracket-quoted; `disable-model-invocation: true`; `description` 529 chars (≤ 1024); body 136 lines (≤ 500).
- Body: `](.ai-factory/specs/` → 1; `.ai-factory/specs/<slug>/` → 2; `Phase note:` byte-exact → present; `200` → 1; `500` → 1. Step 0 (`:49-54`) reads the docs the phase's header and preamble link — *"a `Governing spec:` line is one such link and nothing more"* — and the code the phase is about, down to the leaf, for every phase. The eight closing rules are internally consistent with the workflow: rule 4 matches the template's one-line no-doc branch, rule 6 matches the re-run rule as amended.
- `roadmap-prune`, seven sites re-read individually and unchanged: `:272`, item 1's capture `:281-290`, item 3 `:315`, `:317`, `:339`, `:349-350`, `:411`, `:444`. Negative span `only through the pruned [x] lines' Spec: tags` → 2 pre-edit, 0 post-edit.
- `CLAUDE.md` `:74` and `:189` both carry the skill; `:33` (doc-index prose) untouched. `roadmap-outline-deep` in `docs/sakshi-harness/skill-cycle.md` → 2, committed ahead of the task.
- `active/skills/roadmap-outline-deep` → `../../src/skills/roadmap-outline-deep`, resolves.
- `git diff HEAD -- src/skills/note src/skills/roadmap-engine src/skills/roadmap-outline src/skills/task-rescue docs/` → empty. `git status --short -uall -- src/ active/ CLAUDE.md` → exactly the four expected paths.

One artifact-hygiene note, not a finding: the plan's budget bullet (`.ai-factory/plans/trickster77777/21-28-1-…preamble.md:44`) still reads *"What overflows that budget belongs in the note, not in the preamble"* — the sentence finding 1 removed from the skill. The skill is the corrected side and the plan is a run artifact that `roadmap-prune` sweeps, so nothing ships from it; worth one edit only if the plan is re-read before the task closes.

## Deferred observations

Carried forward from `…-review-1.md` and handoff 13 § 3, re-verified this pass; all outside this task's four-path boundary — for a ruling, not tasks.

- `roadmap-engine`'s phase-intro format (`src/skills/roadmap-engine/SKILL.md:90-91`) describes the intro as carrying *"gate ("blocked on X"), the problem today, key contracts / pinned decisions the phase rests on"*. After this pass a compressed preamble keeps the gate and the pointer; the note holds what is not yet as the docs say. Pinned decisions a phase rests on are therefore named in the format but have no stated home after compression. The engine is excluded by this task's Guards, and enlarging the note would re-add the bulk this direction removes — so this is a ruling for the planning side (adjust the engine's sentence, or accept the drop), not a change here.
- `docs/sakshi-harness/skill-cycle.md:55` says prune deletes completed tasks *"вместе с отработавшими артефактами и их task-spec"*; it now also deletes phase notes.
- `docs/philosophy/multiuser-roadmaps.md:47` describes `.ai-factory/specs/<имя>/` as the home of task specs resolved *"всегда … через `Spec:`-тег contract-line"*; it now also holds phase notes resolved through `Phase note:`, sharing the per-directory `<NN>` counter.
- `docs/sakshi-harness/skill-graph.md` § "Воронка в один дистиллятор" names only `command-handoff` as a direct caller of `note`; `roadmap-outline-deep` is now a second, and § "Домены — по стволам" derives domain boundaries from the `loads:` graph.
- Nothing preserves a `Phase note:` pointer through a `roadmap-outline` / `roadmap-engine` rewrite of a preamble: prune keys on the literal token, so a rewrite that drops it orphans the note in a directory nothing scans. The in-place re-run rule closes this for re-runs of this pass only.
- `note`'s folder-style layer (`src/skills/note/SKILL.md:35`, `:59`) now style-matches across two genres in one directory. Caller hooks outrank folder style, so structure is safe; only unstated register can drift.

REVIEW_PASS

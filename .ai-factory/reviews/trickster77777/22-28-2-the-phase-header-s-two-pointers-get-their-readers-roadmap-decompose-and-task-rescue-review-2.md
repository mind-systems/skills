## Re-review Summary (round 2)

**Task:** 28.2 — the phase header's two pointers get their readers: `roadmap-decompose` and `task-rescue`
**Previous review:** `.ai-factory/reviews/trickster77777/22-28-2-…-review-1.md` (2 findings)
**Changed:** `src/skills/roadmap-decompose/SKILL.md` (+13), `src/skills/task-rescue/SKILL.md` (+29/−17)

Both findings from round 1 are fixed, verified against the current file contents. No new issues.

### Verdicts on round-1 findings

**Finding 1 — the governing-spec report duty fired when only a phase note was read (`src/skills/task-rescue/SKILL.md:150-151`). — Fixed.**

Current content, `:144-157`:

> When a governing spec or phase note was read in Step 1, judge the recurring findings
> against them: … The phase note stands beside the governing spec as a second
> baseline a finding is judged against: the governing spec states how the phase must
> become, the note what diverges now. **Where a governing spec was read, the Diagnosis
> Report must state whether the failure violates it and quote the relevant clause;**
> where a finding instead matches a divergence the phase note already records, the
> report says so and names it as already-recorded divergence. Such a finding is not by
> itself a "specification gap" — the divergence is known and ratified at the phase
> tier — so it does not on its own drive Step 4's depth choice toward inventing a new
> decision; …

The duty is now scoped to the pointer that was actually read ("Where a governing spec was read … whether the failure violates **it**"), so a note-only phase — reachable because `roadmap-outline-deep/SKILL.md:114` makes the `Governing spec:` line conditional — no longer instructs the agent to quote a clause from a document it never read. The paragraph's widened gate at `:144` and the note's own reporting branch both survive; nothing else in the paragraph changed.

**Finding 2 — plan-layer instruction transcribed into the skill body (`src/skills/roadmap-decompose/SKILL.md:42-43`). — Fixed.**

Current content, `:40-44`:

> Before a phase's first entry is drafted, read that phase's preamble; where the phase
> header or preamble names `Governing spec:` documents or a `Phase note:`, read those
> files in full before drafting continues — **unconditional, never suspicion-gated. The
> two pointers are not interchangeable:** the governing spec states how the phase must
> become, the phase note what diverges now.

The clause "the same register `task-rescue`'s own governing-spec read uses" is gone; the sentence now ends at "never suspicion-gated", which carries the whole meaning without pointing at a skill this reader does not load. No cross-skill reference remains in the added paragraph, and the file's only skill references are the pre-existing `roadmap-engine` ones.

### Full re-review — spec verification re-run

Counts taken on a whitespace-normalized read of each file, not a line-oriented `grep`:

- `Phase note:` byte-exact — `roadmap-decompose/SKILL.md` = 1 (spec: ≥1), `task-rescue/SKILL.md` = 2 (spec: ≥2); both were 0 at HEAD.
- `Governing spec:` byte-exact — `task-rescue/SKILL.md` = 2, one at the Step 1 read (`:60-61`) and one at the `## What NOT to do` rule (`:551`); the second pointer joined at both, replaced neither.
- By reading: the Step 1 title at `:58` names both pointers; `:63-64` keeps the exit ("under no phase, or neither pointer is named, proceed as today") and the load-bearing additive-to-Step-4 sentence; the absent-file branch is stated in both skills with a destination (`task-rescue:65-66` → told at Step 1 and carried into the Diagnosis Report; `roadmap-decompose:50-51` → reported to the user); the Step 5 copy rule at `:365` covers both files; `roadmap-decompose` states the unit ("once per phase … in every mode — never once per entry"), names Rewrite / Add / hook (d) "Decompose existing", and names no first-run create site.
- `:236` ("Decision belongs elsewhere (a neighboring task / the governing spec) — point there and reset") is byte-identical to HEAD, as the plan's deliberate exclusion required — it names the governing spec as an authority a decision belongs to, not a file the Step 1 read fetched.
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` → exactly `src/skills/roadmap-decompose/SKILL.md` and `src/skills/task-rescue/SKILL.md`. No `active/` symlink change (both are directory symlinks), no frontmatter or `loads:` edge touched, and `roadmap-outline-deep`, `note`, `roadmap-engine`, `roadmap-outline`, `roadmap-prune` are untouched.

### New-issue scan

Both files read in full. `roadmap-decompose`'s hooks (b), (c), (d) and its Critical Rules make no claim the new paragraph contradicts — hook (d)'s action name is quoted exactly as `:86` spells it. In `task-rescue`, every remaining mention of the governing spec or the Step 1 read (`:128`, `:217`, `:236`, `:365`, `:551`) is consistent with the widened read, and no step-title index elsewhere repeats `:58`'s bolded title, so widening it stranded nothing. No new findings.

## Deferred observations

- Affects: a future task on `src/skills/task-rescue/` — the file is 581 lines against the ≤ 500-line body constraint in `.ai-factory/ARCHITECTURE.md` § "Skill anatomy" and the repo CLAUDE.md § "Key constraints" (569 before this task). Pre-existing and structural — the remedy is moving the depth procedures or the `## What NOT to do` inventory into `references/`, which no widening edit can carry.
- Affects: a future task on `roadmap-outline` / `roadmap-engine` — nothing preserves a `Phase note:` pointer or a `Governing spec:` line across `roadmap-engine:248-250`'s Rewrite, which re-drafts an existing `$TARGET_FILE` and replaces its contents on confirmation. This change makes that gap load-bearing: `roadmap-decompose:46-49` now names Rewrite as a site where the pointers are read, so a rewrite that drops one leaves the new readers seeing a phase with no note and `roadmap-prune:281-286` capturing nothing for a file that still exists. The writer-side preservation rule still has no owner.
- Affects: the `orchestrator/` repo's roadmap — `docs/sakshi-harness/skill-cycle.md:21` names four readers of the two pointers; this task delivers the two in-repo ones, and the orchestrator's planner and reviewer remain committed doc with no task behind them.

REVIEW_PASS

## Review Summary

**Task:** 28.2 — the phase header's two pointers get their readers: `roadmap-decompose` and `task-rescue`
**Spec:** `.ai-factory/specs/trickster77777/104-phase-note-readers.md`
**Plan:** `.ai-factory/plans/trickster77777/22-28-2-the-phase-header-s-two-pointers-get-their-readers-roadmap-decompose-and-task-rescue.md`
**Changed:** `src/skills/roadmap-decompose/SKILL.md` (+14), `src/skills/task-rescue/SKILL.md` (+29/−17)

The cut is right: both edits land at the anchors the plan named, the two pointers are kept apart in wording everywhere, `Governing spec:` is joined and never replaced at either `task-rescue` site, the Step 1 exit survives in substance, and `:236` (the escalation option that names the governing spec as an *authority*, formerly `:227`) is byte-identical as the plan decided. Two issues below — one instruction is now unsatisfiable in a case the change itself makes reachable, and one sentence in `roadmap-decompose` is plan-layer text transcribed into the product.

### Spec verification (re-run, whitespace-normalized read, not line-oriented `grep`)

- `Phase note:` byte-exact — `roadmap-decompose/SKILL.md` = 1 (spec: ≥1), `task-rescue/SKILL.md` = 2 (spec: ≥2). Both were 0 at HEAD, so neither count is satisfied by accident.
- `Governing spec:` byte-exact — still present at both `task-rescue` sites (`:60-61` the Step 1 read, `:551` the `## What NOT to do` rule); `roadmap-decompose` = 1 (new).
- By reading: `roadmap-decompose` states the unit ("once per phase, at the moment that phase's first entry is drafted, in every mode — never once per entry"), names Rewrite / Add / hook (d) "Decompose existing", names no first-run create site, and states the flat-fallback and neither-pointer exits. `task-rescue`'s Step 1 title names both pointers, Step 3 carries the note into the judgment, `:365` covers both files in the copy rule, and the absent-file branch is stated in both skills with a destination.
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` → exactly the two `SKILL.md` files. No `active/` change (both are directory symlinks, unaffected), no `loads:` edge added, no frontmatter touched, and `roadmap-outline-deep`, `note`, `roadmap-engine`, `roadmap-outline`, `roadmap-prune` are all untouched.

### Issues

**1. The governing-spec report duty now fires when only a phase note was read — `src/skills/task-rescue/SKILL.md:144, 150-151`.** *Should fix.*

The paragraph's gate widened from "When a governing spec was read in Step 1" to "When a governing spec **or phase note** was read in Step 1", but the sentence it governs did not scope down with it:

> The Diagnosis Report must state whether the failure violates the governing spec and quote the relevant clause; where a finding instead matches a divergence the phase note already records, …

A phase can carry a `Phase note:` and no `Governing spec:` — `roadmap-outline-deep/SKILL.md:114` is conditional ("where a phase header **already** carries `Governing spec:`, that line stays first"), `:51` treats the governing-spec line as one optional link among the phase's links, and the note is written for every drafted phase regardless. Phase 28 in `.ai-factory/roadmaps/trickster77777.md:118-120` is itself a phase with neither. Before this change that combination could not reach the sentence, because the gate was governing-spec-only; now it does, and the rescue agent is told it *must* state whether the failure violates a document it never read and quote a clause that does not exist. The likely outputs are both bad: a fabricated violation verdict, or a report paragraph explaining the absence of a governing spec — orchestrator-adjacent noise in a report `:190-192` restricts to domain language.

Fix is one clause: scope the duty to the pointer that was actually read — e.g. "Where a governing spec was read, the Diagnosis Report must state whether the failure violates it and quote the relevant clause; where a finding instead matches a divergence the phase note already records, …". Everything else in the paragraph is already disjunction-safe (`:365`'s copy rule reads correctly either way).

**2. A plan-layer instruction was transcribed into the skill body — `src/skills/roadmap-decompose/SKILL.md:42-43`.** *Minor.*

> …unconditional, never suspicion-gated, the same register `task-rescue`'s own governing-spec read uses.

"State it … in the same register `task-rescue/SKILL.md:61-63` already uses" was the plan's instruction *to the implementer* about how to word the paragraph; it is not content for the runtime reader. An agent running `roadmap-decompose` has `roadmap-engine` loaded and nothing else — it cannot see `task-rescue`'s read, so the clause either carries no information or invites opening a skill this task's Guards deliberately keep off the graph ("No new `loads:` edge"). The meaning the clause gestures at is already fully stated three words earlier ("unconditional, never suspicion-gated"), so deleting it loses nothing.

This is distinct from the repo's ordinary cross-skill prose references (`roadmap-outline-deep:135` "that is `roadmap-decompose`'s tier", `roadmap-decompose-skeleton:39` "does not call `roadmap-decompose` at runtime"), which state a boundary the reader can act on without opening the named skill.

### Positive Notes

- **The unit statement landed where the risk is.** Hook (a) is the shape `roadmap-engine` applies per entry (`:189`, `:242`); the paragraph names its own unit in the same breath as the read, so it cannot be executed once per entry.
- **The site enumeration follows ground truth over the spec's prose.** Naming the create-mode draft cycle only "as re-run by the update menu's Rewrite action over an existing `$TARGET_FILE`" is correct — `roadmap-engine:152-154` enters create mode only when the file does not exist, and `roadmap-decompose:35-38` forbids minting a phase header — and the mode-independent "in every mode" still honors the contract line without an enumeration that would have to lie.
- **The Step 1 rewrite kept the load-bearing tail.** The additive-to-Step-4 sentence survives verbatim in substance, and the exit reads "under no phase, or neither pointer is named" — the widening that was easiest to lose.
- **The two pointers never merge.** Every site restates the distinction in the governing surface's own terms (`docs/sakshi-harness/skill-cycle.md:21`): the governing spec states how the phase must become, the note what diverges now.
- **The Step 3 routing effect is stated, not implied** — an already-recorded divergence is explicitly not a "specification gap" on its own, mirroring the root-cause/repair-target distinction already in that paragraph rather than inventing a category.

## Deferred observations

- Affects: a future task on `src/skills/task-rescue/` — the file is now 581 lines against the ≤ 500-line body constraint in `.ai-factory/ARCHITECTURE.md` § "Skill anatomy" and the repo CLAUDE.md § "Key constraints" (569 before this task; +12 here). Pre-existing and structural — the remedy is moving the depth procedures or the `## What NOT to do` inventory into `references/`, which no widening edit can carry. Carried forward from both plan-reviews.
- Affects: a future task on `roadmap-outline` / `roadmap-engine` — nothing preserves a `Phase note:` pointer or a `Governing spec:` line across `roadmap-engine:248-250`'s Rewrite, which re-drafts an existing `$TARGET_FILE` and replaces its contents on confirmation. This change makes that gap load-bearing: `roadmap-decompose:44-46` now names Rewrite as a site where the pointers are read, so a rewrite that silently drops one leaves the new readers seeing a phase with no note and `roadmap-prune:281-286` capturing nothing for a file that still exists. The writer-side preservation rule still has no owner.
- Affects: the `orchestrator/` repo's roadmap — `docs/sakshi-harness/skill-cycle.md:21` names four readers of the two pointers; this task delivers the two in-repo ones, and the orchestrator's planner and reviewer remain committed doc with no task behind them.

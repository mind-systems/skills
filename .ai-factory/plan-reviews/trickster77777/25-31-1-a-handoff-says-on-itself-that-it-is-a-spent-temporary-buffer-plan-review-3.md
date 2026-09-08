## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/25-31-1-a-handoff-says-on-itself-that-it-is-a-spent-temporary-buffer.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" holds that a skill restates nothing the always-loaded layer guarantees, and that where a skill leans on such a guarantee it names it in one sentence at the point of reliance. The plan's body-rule edit conforms: it forbids a citation rule outright and bounds the reliance on the global CLAUDE.md § "Grounding claims" guarantee at one sentence. Re-verified against that section — a handoff is indeed named among the descriptions ground truth overrides. No boundary issue: one command file, `loads: note` unchanged, no engine touched, no new `loads:` edge. **OK.**
- **Rules** — `.ai-factory/RULES.md` is absent in this repo (`ls` confirms). **WARN** (missing optional file; no convention source to check against).
- **Roadmap** — `.ai-factory/roadmaps/trickster77777.md:154` carries `31.1` under `### Phase 31` as the first unchecked line — the seam. Its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md`, which exists and matches the plan item-for-item. The file's only `Governing spec:` line (`:11`) belongs to Phase 19, under a different direction (`## Skills generate to today's norm…`); Phase 31 sits under `## A spent handoff looks exactly like a live one` and names neither a `Governing spec:` nor a `Phase note:`. The reference chain therefore ends at the task spec, and it was walked to the leaf. **OK.**

### Prior-round findings

Both findings of plan-review-2 are closed in this revision:

- **Heading pinned.** Edit 5 now reads "Head it as a non-numbered section addressed to the holder of a handoff file — e.g. `## Holding a handoff` — never `## Step 4` or any other numbered heading", and states why: the file's existing `## Step N — …` headings are the stages of this command's own write path, so numbering the rule into that sequence would frame it as a fourth step — the framing the spec's guard forbids. The Verification step carries the check (`under a non-numbered heading (no ## Step 4)`). The constraint is now carried by the heading, not only by the paragraph beneath it.
- **Prose-shape literal pinned, and the count scoped.** Edit 3 now says "**Reproduce the unprocessed literal verbatim here** rather than pointing at the line fenced in the grid skeleton", gives the reason (a cross-position reference would put one shape's byte-exactness at the mercy of the other), and states the resulting occurrence count explicitly — the literal and the reader-flips sentence occur twice file-wide, with the spec's `→ each 1` read position-scoped, one per shape. Verification repeats it as a do-not-delete instruction. The ambiguity that could have collapsed the one-form guarantee at verification time is gone.

### Ground-truth checks performed

Re-taken fresh against the files this round, never against the spec's or a prior review's description of them:

- `active/commands/command-handoff.md` is a symlink — `git ls-files -s` returns mode `120000`, target `../../src/commands/command-handoff.md`. Editing the target changes no second tracked blob, so "no symlink work" holds and the Verification `--stat` check will legitimately list one path.
- The `description:` block is lines 2–7 of a `>-` folded scalar, three sentences, with `durable note` on line 6. Exactly the two-keep / one-rewrite split the plan describes, and rewriting the closing sentence does not disturb the YAML.
- The grid skeleton opens `# Handoff — <semantic slug derived from the session subject>` (`:30`), a blank line (`:31`), then `## 1. Frame` (`:32`). The insertion point is real and unambiguous, and the blank-line spacing the plan prescribes reproduces the corpus exactly (handoff `17`: title line 1, blank line 2, mark line 3).
- The mark literal exists byte-for-byte in the corpus in both states: `[ ]` in handoff `17`, `[x]` in `15`, `16`, `18`. Nothing is invented, and the plan's insistence that the backticks are part of the literal matches what is actually on disk.
- Step 2's **Template** bullet (`:98`) does carry the "passed **blank**" / "do NOT pre-fill it" rule the exemption attaches to, and `note`'s Template hook does pass a caller directive through unchanged (`src/skills/note/SKILL.md:32`, `:66` — "the note body follows the caller's directive verbatim"; hooks outrank folder style, `:35`). A literal line inside the skeleton therefore survives into the written file with `note` untouched — the exemption is the only thing needed, and it is edit 4.
- The prose shape reaches `note` through that same hook as "a free-form body directive" (`:98`), so edit 4's "the exemption applies to both shapes" is mechanically true, not aspirational.
- Forbidden-token baseline in the target file today: `cite`/`cited`/`citation` case-insensitive = 0, `**Date:**` = 0, `**Source:**` = 0, `roadmap-prune` = 0. Every Verification count is therefore a check against this task's own diff, not pre-existing debt.
- `durable` in the target file: `:6` (the occurrence being removed) and `:87` ("the durable next step" — a different sense inside the prose-shape paragraph). The plan scopes its check to the `description:` block and preserves the rest of that paragraph, so the second occurrence correctly survives. Repo-wide, no doc calls a handoff durable (`docs/sakshi-harness/skill-graph.md:27` and `CLAUDE.md:164` name the genre without a durability claim), so `Docs: no` is right and nothing drifts out of sync with the rewrite.
- Blast radius outside the file: every other `handoff` mention lives under `src/skills/` or `docs/`. Phase 33.1 owns four of those surfaces by name (`roadmap-engine`, `roadmap-outline`, `roadmap-prune`, `orchestrator-artifacts`) and this plan touches none of them; `roadmap-prune`'s "Do not touch `handoffs/` — it is never swept" stays as-is, matching the contract line's guard.
- Position-address fragility: only edit 1 addresses by line range, and it is the topmost edit, so no later edit's anchor shifts under it. Edits 2–5 address by name (`**Prose shape.**` paragraph, the **Template** bullet of Step 2, after Step 3) — the discipline `docs/reference-by-name.md` asks for.
- Working tree on entry holds only untracked plan artifacts under `.ai-factory/` — nothing under `src/`, `active/`, `docs/` or `CLAUDE.md`. The Verification `--stat` check starts from a clean surface, and its dirty-tree caveat is carried anyway.

### Findings

None. Every load-bearing claim in the plan was checked against the files and holds; both prior rounds' findings are closed without introducing a new gap.

### Positive Notes

- The revision closes both prior findings by pinning the *reason* alongside the constraint, not just the constraint: the heading item says why a numbered heading would contradict the spec's guard, and the prose item says why a cross-position reference would be worse than a second copy. An implementer who reads only the rationale still lands on the right edit.
- The deliberate duplication of the literal is safe for a reason the plan states and the corpus confirms: both copies are anchored to the same external form in `.ai-factory/handoffs/`, not to each other, and the spec is explicit that nothing scans the mark — so the two positions cannot mechanically drift apart under a reader.
- The blast radius is stated and true on every limb: one file, a symlink already in place, `note` and every skill under `src/skills/` untouched, existing handoffs not backfilled, Phase 33's four surfaces left alone. Each was re-verified here rather than carried over.
- The plan carries the spec's negative constraints as first-class items with matching counts — no citation rule, no claim about `note`'s internals, no third state, no date, no author, no scanning step anywhere. These are exactly the constraints an implementer improvises past, and each has a check.
- Dependencies between edits are declared where they exist (prose after grid, Template hook after both template edits, body rule after the mark exists in both shapes), and Verification depends on all five.
- The plan follows the spec rather than handoff `15` (itself already marked `[x]`, spent), which asked the `description:` to also state that nothing references a handoff — a rule the spec later routed to `33.1`. That is the buffer's own rule being applied to the buffer that proposed it.

PLAN_REVIEW_PASS

## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/25-31-1-a-handoff-says-on-itself-that-it-is-a-spent-temporary-buffer.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md:41` holds that a skill restates nothing the always-loaded layer guarantees, and names such a guarantee in one sentence at the point of reliance. The plan's body-rule edit follows this: it forbids a citation rule outright and permits at most one sentence naming the global CLAUDE.md § "Grounding claims" guarantee. Re-verified against that section — a handoff is indeed named among the descriptions ground truth overrides. No boundary issue: one command file, `loads: note` unchanged, no engine touched. **OK.**
- **Rules** — `.ai-factory/RULES.md` is absent in this repo (confirmed). **WARN** (missing optional file; no convention source to check against).
- **Roadmap** — `.ai-factory/roadmaps/trickster77777.md:154` carries `31.1` under `### Phase 31` as the first unchecked line (the seam). Its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md`, which exists and matches the plan item-for-item. Phase 31's header names no `Governing spec:` and no `Phase note:` (checked against every `Governing spec:` line in the file — the only one, `:11`, belongs to Phase 19), so the reference chain ends at the task spec. **OK.**

### Prior-round findings

Both findings of plan-review-1 are closed in this revision:

- The edit count now reads "All five edits below land in `src/commands/command-handoff.md`", matching the five task items and the spec's five-item "The change".
- Case-insensitivity is carried through on the citation count in both places it is stated — the body-rule item (`cite`, `cited` or `citation`, case-insensitive, must not appear in the file) and the Verification bullet.

### Ground-truth checks performed

Re-taken fresh against the files, not against the spec's description of them:

- `active/commands/command-handoff.md` is a symlink (`git ls-files -s` → mode `120000` → `../../src/commands/command-handoff.md`). Editing the target changes no tracked blob under `active/`, so the plan's "no symlink work" holds and the Verification `--stat` check will not see a second path.
- The `description:` block is lines 2–7, three sentences, with `durable note` on line 6 — exactly the two-keep/one-rewrite split the plan describes.
- The grid skeleton opens `# Handoff — <semantic slug derived from the session subject>` (`:30`), a blank line, then `## 1. Frame` (`:32`). The insertion point is real and unambiguous, and the blank-line spacing the plan describes matches the corpus (`.ai-factory/handoffs/17` has the mark on line 3 under a line-1 title).
- The mark literal exists byte-for-byte in the corpus in both states: `[ ]` in handoff `17`, `[x]` in `15`, `16`, `18`. Nothing is invented.
- Step 2's **Template** bullet (`:98`) does carry the "passed **blank**" / "do NOT pre-fill it" rule the exemption attaches to, and `note`'s Template hook does pass a caller directive verbatim (`src/skills/note/SKILL.md` § Hooks: "the note body follows the caller's directive verbatim"). A literal line in the template therefore survives into the written file with `note` untouched.
- Forbidden-token baseline in the target file today: `cite`/`cited`/`citation` (case-insensitive) = 0, `**Date:**`/`**Source:**` = 0, `roadmap-prune` = 0. Every Verification count is a check against this task's diff, not pre-existing debt.
- `durable` in the repo outside handoffs: `src/commands/command-handoff.md:6` (the one being removed) and `:87` ("the durable next step" — a different sense inside the prose-shape paragraph, correctly preserved by the plan's "the rest of that paragraph stays as written"), plus `src/skills/task-rescue/SKILL.md:561-563` (unrelated). No doc anywhere calls a handoff durable — `docs/sakshi-harness/skill-graph.md:27` and `CLAUDE.md:164` name the genre without a durability claim — so `Docs: no` is correct.
- Blast radius outside the file: every other `handoff` mention lives in `src/skills/` (`roadmap-prune:61-63,447`, `roadmap-engine:86`, `roadmap-outline:40`, `orchestrator-artifacts:69`, `agent-architect:47-48,253`, `roadmap-test-coverage:293,401`). Phase 33.1 owns four of those surfaces by name and the plan touches none of them; `roadmap-prune:447` ("Do not touch `handoffs/` — it is never swept") stays as-is, matching the contract line's guard.
- Working tree on entry holds only untracked plan artifacts under `.ai-factory/` — nothing under `src/`, `active/`, `docs/` or `CLAUDE.md`. The Verification `--stat` check starts from a clean surface.

### Findings

1. **LOW — the new body section's heading is unpinned, and the file's own heading habit pulls it toward `## Step 4`.** Edit 5 says only "add a short section at the end of the file, after Step 3". Every top-level heading in the shipped file today is a step of the write path (`## Step 1 — Shape the mining lens`, `## Step 2 — Delegate to note`, `## Step 3 — Paste-back pointer`), so folder-and-file style pushes an implementer to name the new one `## Step 4 — …`. That numbering would frame the rule as a fourth step of this command's own procedure — precisely the framing the same edit forbids two lines earlier ("never as a permission granted to this command's own write path, which always produces a new numbered file through `note`") and the framing the spec's guard rules out ("nothing scans the mark … no skill gains a step that reads a handoff"). Pin the heading as a non-numbered section addressed to the holder of a handoff file, so the constraint is carried by the heading rather than only by the paragraph beneath it.

2. **LOW — the prose-shape edit does not pin whether the literal is reproduced or referenced, which leaves the spec's "→ each 1" counts ambiguous.** Edit 3 reads "state that the file opens with the `# Handoff — <slug>` title and the mark line directly beneath it … — the same literal line as the grid shape". That admits two implementations: the prose paragraph reproduces the 74-character literal verbatim (making the sentence "whoever reads this marks it; a marked handoff is spent" occur twice in the shipped file), or it references the line already fenced in the grid skeleton (occurring once). The spec's Verification pins "the emitted template carries the mark … and the sentence naming the reader as the one who flips it → each 1" and "the prose-shape directive names both … → each 1"; under the reproduce reading, an implementer who takes those counts file-wide rather than position-scoped reads 2 and "fixes" it by deleting one of the two — collapsing exactly the one-form guarantee edit 3 exists to protect ("so the corpus does not split into two forms"). The plan's own Verification bullet already softens the counts to presence, which is the right resolution, but it never says why. Pin the choice (reproduce verbatim, or reference the fenced line) and state the resulting occurrence count, so the spec's counts are read position-scoped and no correct edit is undone at verification time.

### Positive Notes

- The blast radius is stated and true on every limb: one file, a symlink already in place, `note` and every skill under `src/skills/` untouched, existing handoffs not backfilled. Each was re-verified here rather than carried over from the previous round.
- The plan carries the spec's negative constraints as first-class items with matching counts — no citation rule, no claim about `note`'s internals, no third state, no date, no author, no scanning step. These are exactly the constraints an implementer improvises past, and each has a check.
- The mark's literal is pinned to the corpus rather than reinvented, with the backticks named as part of the literal — the one detail a "reproduce byte-for-byte" instruction usually loses.
- Dependencies between edits are declared where they exist (prose after grid, Template hook after both, body rule after the mark line exists in both shapes), and Verification depends on all five.
- The dirty-tree caveat on the `git diff --stat` check is carried from the spec and matters here, since the tree already holds untracked plan artifacts on entry.
- The plan follows the spec rather than handoff `15` (itself already marked spent), which asked the `description:` to also state that nothing references a handoff — a rule the spec later routed to `33.1`. That is the buffer's own rule being applied to itself.

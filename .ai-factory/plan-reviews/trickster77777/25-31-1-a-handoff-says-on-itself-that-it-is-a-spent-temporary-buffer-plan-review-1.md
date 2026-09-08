## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/25-31-1-a-handoff-says-on-itself-that-it-is-a-spent-temporary-buffer.md`
**Target file:** `src/commands/command-handoff.md` (single file)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" holds that a skill restates nothing the always-loaded layer guarantees, and names such a guarantee in one sentence at the point of reliance. The plan's body-rule edit follows this exactly: it forbids a citation rule and permits, at most, one sentence naming the global CLAUDE.md § "Grounding claims" guarantee. Verified against that section — it does name a handoff among the descriptions ground truth overrides. No boundary or dependency issue: the edit lands in one command file, `loads: note` is unchanged, no engine is touched. **OK.**
- **Rules** — `.ai-factory/RULES.md` is absent in this repo. **WARN** (missing optional file; no convention source to check against).
- **Roadmap** — `.ai-factory/roadmaps/trickster77777.md` carries `31.1` under `### Phase 31` as the first unchecked line (the seam), and its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md`, which exists and matches the plan item-for-item. Phase 31 names no `Governing spec:`, so the spec tree ends at the task spec. **OK.**

### Ground-truth checks performed

Every load-bearing claim in the plan was checked against the files, not against the spec's description of them:

- `active/commands/command-handoff.md` → `../../src/commands/command-handoff.md` — a symlink, confirmed. The plan's "no symlink work" holds.
- The frontmatter `description:` block is lines 2–7, with `durable note` on line 6 and exactly two preceding sentences — matching the plan's description of what to keep and what to rewrite. (A line range in a plan is legitimate: `docs/reference-by-name.md` § "The check" confines position addresses to a work-order, which is what a plan is.)
- The mark's literal, `**Processed:** \`[ ]\` — whoever reads this marks it; a marked handoff is spent.`, exists byte-for-byte in `.ai-factory/handoffs/17`; the `[x]` state exists in `15`, `16`, `18`. Both states are in the corpus as the plan claims, so "reproduce byte-for-byte" is realizable and no wording is invented.
- The grid skeleton does open `# Handoff — <semantic slug derived from the session subject>` followed directly by `## 1. Frame`, so the insertion point is real and unambiguous.
- The Step 2 **Template** bullet does carry the "passed **blank** / do NOT pre-fill it" rule the exemption attaches to, and `note`'s Template hook does pass a caller directive verbatim (`src/skills/note/SKILL.md` § Hooks) — so a literal line in the template survives into the written file without touching `note`. `note`'s own default template does carry a fully literal `**Source:** conversation context`, which is exactly why the plan bars that fact from the shipped file: it would be a one-sided cross-file assertion.
- Forbidden-token baseline in the target file today: `cite`/`cited`/`citation` = 0, `**Date:**`/`**Source:**` = 0, `roadmap-prune` = 0. The verification counts are therefore checks against the diff, not pre-existing debt.
- `durable` elsewhere in the repo: `src/commands/command-handoff.md:87` ("the durable next step" — a different sense, correctly preserved by the plan's "the rest of that paragraph stays as written") and `src/skills/task-rescue/SKILL.md` (unrelated). No doc anywhere states the handoff is durable, so `Docs: no` is correct — nothing drifts out of sync with the description rewrite.
- Phase 33's guard (`33.1` clears handoff references from durable surfaces) does not overlap: the plan touches none of the four surfaces that task owns.

### Findings

1. **LOW — the plan's own edit count contradicts its task list.** "The single file" opens "All four edits land in `src/commands/command-handoff.md` and nowhere else", but five edit tasks follow: the `description:`, the grid skeleton, the prose-shape directive, Step 2's Template bullet, and the body rule (the spec's "The change" likewise enumerates five). The load-bearing half of that sentence — "and nowhere else" — is right; the numeral is not, and an implementer who takes the count as the checklist size can merge the grid and prose edits into one or drop the Template-hook bullet. Say five, or drop the numeral.

2. **LOW — the Verification step drops the spec's case-insensitivity on the citation count.** The spec pins "`cite`, `cited` or `citation`, **case-insensitive**, in `src/commands/command-handoff.md` → 0"; the plan's Verification bullet reads only "`cite`/`cited`/`citation` at 0", and the body-rule edit likewise says "must not appear". A spec's verification wording is contract text in this repo; carry the qualifier through so a sentence-initial `Cited` cannot pass a case-sensitive check.

### Positive Notes

- The blast radius is stated and true: one file, one symlink already in place, `note` and every skill under `src/skills/` untouched, existing handoffs not backfilled. Each of those was verified rather than assumed.
- The plan carries the spec's negative constraints, not just its positive ones — no citation rule, no claim about `note`'s internals, no third state, no date, no author, no scanning step anywhere. These are precisely the constraints an implementer improvises past, and each has a matching count in Verification.
- The one place where the plan diverges from an earlier artifact is correct: handoff `15` (itself already marked spent) says the `description:` should also state that nothing references a handoff; the spec's guard later moved that to `33.1`, and the plan follows the spec, not the spent buffer. That is the buffer's own rule being applied to itself.
- Dependencies between edits are declared where they exist (prose after grid, Template hook after both, body rule after the mark line), and Verification depends on all of them.
- The dirty-tree caveat on the `git diff --stat` check is carried from the spec, which matters here: the working tree already holds untracked plan artifacts on entry.

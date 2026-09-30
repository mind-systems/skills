## Code Review Summary

**Files Reviewed:** 1 plan, its task spec (`.ai-factory/specs/trickster77777/182-…`), the contract line 65.3 in `.ai-factory/roadmaps/trickster77777.md`, the target `src/skills/roadmap-prune/SKILL.md`, and every file the plan's sweep hits
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap — OK.** Plan title matches contract line 65.3 in `.ai-factory/roadmaps/trickster77777.md`, which sits at the seam: 65.1 and 65.2 are `[x]`, 65.3 is the first `[ ]`. The spec named by the contract line was read. The governing docs (`docs/reference-by-name.md`, `docs/counts-go-stale.md`) are cited correctly and left unedited.
- **Architecture — OK.** The change is prose inside one skill body. No `loads:` edge, protocol token, or engine contract changes. `orchestrator-artifacts` and `command-handoff` are correctly left alone: neither reads a line from the handoff.
- **Rules — WARN (not applicable).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.

### Critical Issues

**1. The verification step's expected hit list does not match what the sweep returns now** (plan § "Confirm the blast radius", the "Re-run the spec's sweep" task)

The plan tells the implementer to treat any hit outside its list as a sign that "the sweep has changed since the spec was written" and to report it. I ran both searches against the current tree. The list does not match what they return, so a correct implementation would raise false alarms at this step:

- **Real hits the plan does not list:**
  - `docs/test-coverage-pass.md` — the heading "Grouping is left unpinned, on purpose".
  - `CLAUDE.md` — the documentation-index row that describes that doc.
  - `docs/sakshi-harness/skill-graph.md` — "`command-handoff` зовёт `note` напрямую".

  None of these is related to this change, and none needs an edit. They are still real matches of the listed commands.
- **A listed hit that does not occur:** "`command-handoff` itself". `src/commands/command-handoff.md` never contains the string `command-handoff`, so neither search reaches it. The spec's **Finding** makes the same claim. The plan copied it without re-running the sweep.
- **Wrong item number in `roadmap-prune`:** the plan says the "unpinned" hits outside the target are in "item 3 of the same step". In the file, the other hits are in item 2 ("developer's unpinned observation blocks it…") and item 5 ("If none are unpinned → proceed…"). Item 3 says "**not pinned**", which the search does not match.

**Fix:** rewrite the "Expected" bullets as the actual current hit set, each with a one-line reason why no edit is needed. Suggested list:
- Search 1 (`unpinned`):
  - `roadmap-prune` Step 0: items 2, 4 and 5.
  - `docs/reserved-words.md`.
  - `command-pin-gaps` (two lines, about value holes).
  - `docs/test-coverage-pass.md` and the `CLAUDE.md` index row (grouping, unrelated).
- Search 2 (`command-handoff`):
  - `roadmap-prune` Step 0 item 4.
  - `agent-architect` (the genre passage).
  - `docs/sakshi-harness/skill-cycle.md` (two lines, gate description).
  - `docs/sakshi-harness/skill-graph.md` (the note funnel, unrelated).

As an alternative, keep the stop condition on its real criterion: "a hit that names what the handoff carries per entry, or reads an entry's line from a handoff". That is the spec's **Rule**. It would replace the membership test against a list. None of the extra hits meets that rule, so the edit itself is unaffected. Only the check step is wrong.

### Verified correct (no action)
- The quoted "before" text matches `src/skills/roadmap-prune/SKILL.md` Step 0 item 4, part `1.`, exactly: same three wrapped lines, same indentation (3 spaces, then 6).
- The replacement sentence matches the spec's **What must be true after** word for word. The new middle line is 85 characters, inside the file's wrap width: the neighbouring lines run 83–88.
- After the edit, `grep -n "file:line"` on the skill returns nothing. Its only current hit is the line being replaced. The `<file>:<line>` chat forms in item 4, Step 7.5 and Step 8 don't match that pattern and are correctly kept.
- The plan's scope is right: one sentence in one file, with the chat line, parts `2.`/`3.`, the other Step 0 items, and the Step 7.5/Step 8 echoes all explicitly left alone.

### Positive Notes
- The "before" text is quoted in full, with its indentation and wrapping, so the edit can't be applied to the wrong place.
- The things that must stay unchanged are named one by one. That includes the easy-to-confuse `<file>:<line>` chat echoes, each with a reason.
- Adding a read-only check of what else the change could break is the right idea. It only needs its expected output to match the tree as it is now.

# Review — 35.1 the global CLAUDE.md says a reference addresses by name (round 1)

## Code Review Summary

**Files Reviewed:** the full working-tree change — `src/global/CLAUDE.md` (the one modified tracked file) read in full, and the new `tradeoxy_core/.ai-factory/handoffs/46-the-naming-rule-is-now-always-loaded.md` read in full; against the task spec `.ai-factory/specs/trickster77777/111-…`, the 35.1 contract line under `### Phase 35` in `.ai-factory/roadmaps/trickster77777.md`, the plan and its three plan-reviews, `src/commands/command-handoff.md`, `docs/reference-by-name.md`, and in `tradeoxy_core`: `.ai-factory/RULES.md`, handoffs 43/44/45 and the working tree.
**Risk Level:** 🟢 Low — a Markdown-only change: one paragraph inserted into an instruction file and one new prose file in a sibling repository. No executable surface, no schema, no protocol token, no symlink. Every one of the spec's five verification bullets holds, checked by equality rather than presence.

### Findings

None.

### Verified against ground truth

- **The inserted paragraph is byte-identical to the spec's pinned string.** Read whole and compared character-for-character against the paragraph under the spec's § "The change": **556 characters, equal**, em dashes, the backticks around `file:line` and the bold `**name**` intact. It occurs exactly once in the file, as a plain paragraph — no `> ` prefix, no indentation, no fence, which is the defect plan-review round 1 predicted and the plan's equality check was built to catch.
- **The placement is the one the spec pins.** § "Grounding claims" now holds eight paragraphs with the new one at index 4: the paragraph above ends `…("per the spec…") — never invent.`, the one below begins `The opening task statement is the first artifact`. `git diff HEAD -- src/global/CLAUDE.md` is a single hunk, one added line plus its blank line, no other change anywhere in the file.
- **The guard against linking the deep home holds.** `reference-by-name` appears 0 times in `src/global/CLAUDE.md`, and the paragraph carries no path — correct for a file that loads in projects that do not have `docs/reference-by-name.md`.
- **The file does not contradict the rule it now states.** A sweep of `src/global/CLAUDE.md` for a `file:line` form returns nothing: the file prescribes name-addressing and cites nothing by position.
- **The edit reaches every session without symlink work.** `active/CLAUDE.md → ../src/global/CLAUDE.md` and `~/.claude/CLAUDE.md → …/skills/active/CLAUDE.md` are unchanged; the tracked symlink's blob is a path, which is why `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists `src/global/CLAUDE.md` **alone**, exactly as the spec's third bullet requires.
- **The handoff is the next free number in its folder.** `46-the-naming-rule-is-now-always-loaded.md`, unpadded like its neighbours, with nothing else holding 46; the folder previously ran to 45.
- **The mark line is verbatim and unprocessed.** `**Processed:** \`[ ]\` — whoever reads this marks it; a marked handoff is spent.` is byte-identical to `src/commands/command-handoff.md` and to file 45 modulo the marker, and the marker is `[ ]`. This is the specific trap plan-review round 2 named — 44 and 45 both carry `[x]` because both are spent, and the marker rides along with the form — and it was not sprung.
- **The handoff names both halves the spec requires, and reproduces the paragraph nowhere.** It addresses the global rule by name — the global CLAUDE.md § "Grounding claims", the paragraph opening "A reference addresses by **name**, never by position" — and names the local duplicate by its `RULES.md` heading, quoted exactly as that file writes it. The paragraph's own text does not appear in the file (`defect report against its target` is absent), so the fact keeps one home, which is what the task exists to give it. It also carries no path into the skills repository and no link to `docs/reference-by-name.md`, holding the spec's Guards in the direction where the pull is strongest.
- **Its third claim is exact.** All four position addresses it quotes from `tradeoxy_core`'s `RULES.md` — `package.json:13-14`, `src/indicators/runtime/indicator-protocol.ts:58-79`, `src/replay/__tests__/replay-indicator-replayer.spec.ts:288` and `:298` — are present verbatim in that file, and they are named as exhibits and framed as an observation, not an instruction.
- **`tradeoxy_core` is otherwise untouched.** `git -C tradeoxy_core status --short` shows the new handoff as the **only** entry added by this run: the eight pre-existing entries the plan enumerated (six modified files under `notes/` and `specs/`, two untracked handoffs 44 and 45) are unchanged, `git diff HEAD -- .ai-factory/RULES.md` is empty (byte-identical to HEAD), and nothing there is committed. The plan's documented deviation — the spec's literal "shows the new handoff and nothing else" being unsatisfiable against a tree that was already dirty — was handled as a delta check, which is the honest reading and the one that actually verifies the invariant.
- **Nothing else in this repo moved.** The only modified tracked file is `src/global/CLAUDE.md`; the rest of the staged set is this task's own planning artifacts under `.ai-factory/`. No roadmap checkbox flip and no commit, which the orchestrator owns.
- **No test is owed.** Under `test-philosophy` there is no silent-failure surface here: a Markdown instruction file and a prose handoff, both verified by direct read. `Testing: no` in the plan is correct.

### Positive Notes

- The one thing this task could most easily have gotten wrong — pasting the paragraph into the handoff to be helpful — did not happen. The handoff addresses the rule by section and opening clause, which is both the one-home discipline and a live demonstration of the very rule being installed.
- The `[ ]` marker survived a copy from two exemplars that both carry `[x]`. That is the failure the plan warned about in the write step and checked in the read-back, and both halves did their job.
- The insertion is exactly two lines. Nothing was tidied, reworded, or "improved" in the seven neighbouring paragraphs of a file every session of every project loads.

## Deferred observations

- Affects: Phase 35 / task spec `.ai-factory/specs/trickster77777/111-the-global-claude-md-says-a-reference-addresses-by-name.md` — carried unchanged from the plan-review rounds and unaffected by the landing: the naming rule now has two homes in this repository and neither names the other. `docs/reference-by-name.md` § "Where things are normed" cites the global CLAUDE.md § "Grounding claims" only as the home of the one-home-per-fact rule it rests on; `docs/always-loaded-discipline.md` enumerates what § "Grounding claims" prescribes and that enumeration now omits its newest rule; and this repo's `CLAUDE.md` doc table gives the "Reference by name" row no equivalent of the clause its Context tree neighbour carries ("the normative rule lives in the global CLAUDE.md § 'Grounding claims'"). The spec's Files list pins one edit and the implementation correctly did not exceed it, so this belongs to the next task on this phase: one clause in each of the three.

REVIEW_PASS

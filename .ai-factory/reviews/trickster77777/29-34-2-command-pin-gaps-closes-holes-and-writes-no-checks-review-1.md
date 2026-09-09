# Review — 34.2 `command-pin-gaps` closes holes and writes no checks

## Code Review Summary

**Files Reviewed:** `src/commands/command-pin-gaps.md` (the only modified file, read in full at 49 lines); plus the plan and both plan-review rounds, the task spec `110-pin-gaps-closes-holes-and-writes-no-checks.md`, the contract line at `.ai-factory/roadmaps/trickster77777.md:185`, `src/skills/roadmap-engine/SKILL.md` § "What a task spec holds", `src/skills/test-philosophy/SKILL.md`, `docs/reference-by-name.md`, and the downstream describers (`docs/sakshi-harness/skill-cycle.md`, `docs/sakshi-harness/skill-graph.md`, `docs/skill-description-field.md`, `CLAUDE.md`).
**Risk Level:** 🟢 Low — three prose edits in one command file, no executable code, no schema, no runtime surface. Every pinned string landed byte-exact and every guard held.

### What landed

`git status --short` lists one modified file, `src/commands/command-pin-gaps.md`, plus this task's own four `.ai-factory/` artifacts. The diff is exactly three hunks in one contiguous region:

1. **Two new paragraphs at the pinned seam.** Inserted after the "A task spec that repeats a paragraph from a document…" paragraph and before `**Value holes:**`, with a blank line on each side (lines 35, 37, 39 are blank; the paragraphs are lines 36 and 38). Both open with a bold lead-in, so each is addressable by name — the form `docs/reference-by-name.md:13` cites as the reason this file's classes are cited by name.
2. **The value-hole repair clause replaced.** The `file:line` citation instruction is gone; the value is now pinned with its source named as the file and the name of the thing inside it that holds the value, "never a line number, because the spec outlives the numbering it was written against". The `never invent` ending survives.

### Verified against ground truth

- **Byte-exactness of all three pinned strings.** Both new paragraphs match the plan's pinned text as whole lines (`grep -Fxq`, exact match). The value-hole clause matches as an exact substring of line 40, with the prefix before it — `**Value holes:** TODO/TBD/«решим по ходу», … a missing file or call site. ` — byte-identical to the pre-change enumeration and nothing at all after it. The plan's "the enumeration of what a value hole *is* is untouched" holds literally.
- **The reference the new paragraph makes resolves by name.** `src/skills/roadmap-engine/SKILL.md:46` opens `**What a task spec holds:**` and italicizes the three parts in exactly the wording the command reuses, so the citation `` `roadmap-engine`'s "What a task spec holds" paragraph `` addresses a name, not a position — the edit obeys the rule it installs. The citation form also matches the file's own existing habit at line 20 (`see the engine's "Named roadmaps" section`), same straight quotes.
- **No restatement of the engine's fact.** The new paragraph carries only the three part-names; none of the engine's three elaborations ("read from the code with exact values", "in the code's own terms: which file, which text, which value", "enumerated rather than hedged") appears anywhere in the command. One home per fact holds.
- **The round-1 classification collision is genuinely closed in the landed bytes, not just in the plan.** Line 36 carries the principle verbatim — "A class is named by the part its repair supplies, never by the part that went unread" — with the worked case inline. Checked against the file's own routing: line 32 (`an existing shape nobody looked at, or work already half-done, is a meaning hole`) and the last two members of line 42's meaning-hole enumeration now follow from the stated principle instead of contradicting it. Lines 32 and 42 are byte-identical to their pre-change text.
- **The `file:line` guards held exhaustively.** The file contained three occurrences (old lines 26, 36, 44) and now contains two: line 26 (the walk's landing, described while reasoning) and line 48 (the scan-mode report format, printed to chat). Both are byte-identical to their pre-change text — the most likely failure mode here, a `grep file:line` sweep, did not happen.
- **Every negative guard held.** Frontmatter is unchanged in all five fields — `description:`, `argument-hint:`, `allowed-tools:`, and `loads: roadmap-engine` with no `test-philosophy` edge added, so the grep-based reverse graph reads as it did. Line 22's mandate is unrewritten. Line 46 ("A task that cannot be planned coherently belongs to `roadmap-decompose`… and loads none of the four") is untouched, and the new paragraph names `test-philosophy` as a discriminator only, matching that line's existing treatment. No heading was added at any level (`grep -c '^#'` → 0), which keeps `docs/reference-by-name.md:13` true. `docs/reference-by-name.md` is not cited in the command — correct for a command that executes in arbitrary projects where that path does not exist. Neither sibling 34.3 nor 34.4 was anticipated: `agent-architect`, `architect-pairing-engine`, `src/agents/editor.md` and `docs/reserved-words.md` are all unmodified.
- **The `test-philosophy` step is inherited, not invented.** `src/skills/test-philosophy/SKILL.md` holds the signal-immediately / run-on-silently discriminator and the skip rule; the landed sentence's step from "a check that can only fail where the instruction was ignored" to "loud failure" is the contract line's and task spec's own wording, carried through unchanged.
- **The register paragraph does not cancel the test routing.** Its closing sentence ("A surface that fails silently still owes a test, routed to its owner as below") points at line 46 rather than re-deriving it, which is what stops the absolute "never authors a check" from being read as "never mentions a test". "as below" is a direction inside one file, not a position address of the kind `docs/reference-by-name.md` § "The check" forbids, and it matches the file's existing habit ("referenced below" at line 18, "above" at line 36).
- **Nothing downstream is invalidated.** `grep -rn "pin-gaps"` outside `.ai-factory/` returns `docs/skill-description-field.md:13`, `docs/sakshi-harness/skill-cycle.md:37,39,74`, `docs/sakshi-harness/skill-graph.md:49`, `docs/reference-by-name.md:13` and the `CLAUDE.md` index row — all describe the pass's job, none quotes the value-hole repair or claims the pass writes checks. All remain correct, and none was edited, as the plan required.
- **Delivery and hygiene.** `active/commands/command-pin-gaps.md → ../../src/commands/command-pin-gaps.md` is a live symlink and was not replaced by a copy, so the edit goes live; `upstream/ai-factory/` ships skills only, so a re-sync cannot clobber a command. No trailing whitespace, no CR bytes, file ends in a single newline, the three edited/added lines are unwrapped single lines (798, 435 and 494 columns) matching the 120–887 range of the surrounding body, and the body is 49 lines against the 500-line cap.

### Critical Issues

None.

### Minor Issues

None.

### Positive Notes

- The round-1 finding was closed at its root in the landed text: the file now states *why* line 32 routes an existing shape nobody looked at to the meaning class, which is strictly more than it carried before this task — a correctness gain beyond the contract line's own ask.
- The two surviving `file:line` occurrences are the sharpest evidence the change was executed rather than pattern-matched: an implementer sweeping the token would have taken both, and both are exempt for stated reasons (a landing described while reasoning; a chat report thrown away, which is the exemption `docs/reference-by-name.md` itself grants a work-order).
- The replacement clause teaches the naming rule at the granularity `docs/reference-by-name.md` § "Granularity, not size" defines it — a symbol, a heading, a bold lead-in — without citing the doc, so the instruction travels into projects that do not have it.
- Both new paragraphs carry bold lead-ins, so the two facts this task adds are themselves addressable by name in a file that has no headings — the same discipline the task installs, applied to its own output.

REVIEW_PASS

## Code Review Summary

**Files Reviewed:** 1 plan, 1 task spec, 1 phase note, 1 target file (`src/skills/roadmap-test-coverage/SKILL.md`), governing spec checked by sweep
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. The change edits only one skill body's text. It moves no module boundary and adds no `loads:` edge.
- **Rules** — WARN. `.ai-factory/RULES.md` is absent, so there was nothing to check against.
- **Roadmap** — OK. The plan heading matches contract line 52.1 in `.ai-factory/roadmaps/trickster77777.md`, under Phase 52 (`Governing spec: docs/test-coverage-pass.md`). I read the chain: contract line → task spec `specs/trickster77777/0204-…md` → phase note `specs/trickster77777/146-roadmap-test-coverage-leftovers.md` → target file. The plan's three replacement texts match the spec's § "What must be true after" word for word.
- **Governing spec** — OK. I re-ran the spec's sweep. `docs/` and `CLAUDE.md` name neither `Explore` nor `general-purpose`, and they don't contain "Test Plan" or "Area Name". `docs/test-coverage-pass.md` needs no edit, as the plan says.

The plan's blast-radius statements hold against ground truth:
- `Explore` appears only at Layer 4's launch sentence (current line 144).
- `general-purpose` appears only at Layer 5 and Layer 7.
- `# <Area Name> — Test Plan` is the only title-line hit.
- Every `<area name>` occurrence is an orchestrator label: the input line, Layer 5's prompt and return lines, the Layer 6 and Layer 7 hand-off lists, and the Layer 8 report.
- Critical Rule 3 ("Layer 4 and 5 agents return one line") and the frontmatter (`allowed-tools` includes `Agent`) are unaffected.

### Critical Issues

None.

### Minor Issues

1. **The plan's re-wrap instruction allows a layout that makes its own Verify step fail.**
   - **What the plan says.** It asks the implementer to re-wrap the slug paragraph "at a fixed column of about 80 characters". Its Verify step then expects `grep -n "in words"` to find "the new prompt sentence and the new title line".
   - **Why that conflicts.** After re-wrapping, the paragraph's natural last line, `not for the Area label above. The note's title carries that same name, in words.`, is exactly 80 characters. The file holds prose lines at 80 and 81 characters (lines 6, 20, 41, 367), so 80 fits. But many lines top out at 79 (for example Layer 5's launch line). An implementer who wraps at 79 or below gets `…carries that same name, in` (73 characters) and then `words.` on the next line. That wrap follows the instruction, yet `grep -n "in words"` would then match only the title line, and the Verify step fails on a correct edit. In the orchestrator, that can cost a needless re-loop or an unnatural re-wrap made just to satisfy the grep.
   - **Fix.** Make the check independent of where the line breaks. Either grep for a phrase that cannot straddle a break, such as `grep -n "carries that same name"` plus `grep -n "# <the name you chose, in words> — Test Plan"`, or pin the paragraph's last line in the plan: `not for the Area label above. The note's title carries that same name, in words.` (80 characters, within the file's existing column).

### Positive Notes

- The plan pins all three replacement texts verbatim from the spec, with the exact current text to replace.
- It explicitly fences off the lines that must not change: the `Area:` input line, the "Write the document below to …" paragraph, `saved:`, and Layers 5–8.
- It re-ran all three spec sweeps and reports results that match the repo.
- The new launch line, "Launch one `general-purpose` agent per area in a **single message** (parallel).", is 79 characters, so it fits the column with no re-flow, consistent with Layer 5's identical launch line.

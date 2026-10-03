## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-test-coverage/SKILL.md`). The other staged files are pipeline artifacts: the plan, its sidecar, and the plan reviews.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. The change edits text inside one skill body. It adds no `loads:` edge and moves no module boundary.
- **Rules** — WARN. `.ai-factory/RULES.md` is absent, so there was nothing to check.
- **Roadmap** — OK. The plan heading matches contract line 52.1 in `.ai-factory/roadmaps/trickster77777.md`, under Phase 52, which names `docs/test-coverage-pass.md` as its governing spec. I walked the chain: contract line → task spec `specs/trickster77777/0204-…md` → phase note `specs/trickster77777/146-roadmap-test-coverage-leftovers.md` → the target file.
- **Governing spec** — OK. `docs/` and `CLAUDE.md` mention neither `Explore` nor `Area Name`. `docs/test-coverage-pass.md` says only "one throwaway agent per area", and in § "A number is fixed before research; a name is not" it says the name is pinned late enough to be true after research. The new title follows that.

### Conformance to the spec

The diff has three hunks, all in § "Layer 4 — Deep Research (parallel agents)". Each one matches the spec's § "What must be true after" word for word:

1. **Launch sentence.** It now reads "Launch one `general-purpose` agent per area in a **single message** (parallel)." The line is 79 characters. The next sentence is unchanged, and the wording matches the existing Layer 5 launch line.
2. **Slug paragraph.** It now ends "not for the Area label above. The note's title carries that same name, in words." The line is 80 characters, inside the file's existing column, and is the layout the plan pinned. The first two lines of the paragraph are unchanged.
3. **Template title.** It now reads `# <the name you chose, in words> — Test Plan`.

### Blast radius

I re-checked the spec's sweep against the edited file:
- `Explore` and `Area Name` no longer appear in the skill, its directory, `docs/`, or `CLAUDE.md`.
- `general-purpose` now appears at Layers 4, 5 and 7, so all three agent launches use one type.
- Every `<area name>` placeholder is the orchestrator's own label for the area. That covers the Layer 4 `Area:` input, the Layer 5 prompt and return lines, the Layer 6 and Layer 7 hand-off entries, and the Layer 8 report. None of them read the note's title, and Layer 6 opens the note by its path. The title change therefore cannot desynchronise them.
- The `saved:` return line is unchanged. It now reports a write the agent can actually perform.
- The frontmatter `allowed-tools` already includes `Agent`, and Critical Rule 3 ("Layer 4 and 5 agents return one line") still holds.
- `git diff HEAD --stat -- src` shows one file, with 3 insertions and 3 deletions.

### Critical Issues

None.

### Positive Notes

- The edit is minimal: three lines changed, all reflowed in place without touching the surrounding lines.
- The writer now has the `Write` tool its prompt relies on. This removes the observed failure where researchers refused to write and the main agent wrote their notes for them.
- The note's slug and title now come from the same post-research name. A note no longer names itself one way in its path and another way in its heading.

REVIEW_PASS

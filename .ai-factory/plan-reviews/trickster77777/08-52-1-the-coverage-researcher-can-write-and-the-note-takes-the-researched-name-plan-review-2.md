## Code Review Summary

**Files Reviewed:** 1 plan, 1 task spec, 1 phase note, 1 target file (`src/skills/roadmap-test-coverage/SKILL.md`), governing spec and `CLAUDE.md` checked by sweep
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. The change edits text in one skill body. It moves no module boundary and adds no `loads:` edge. `.ai-factory/ARCHITECTURE.md`, `README.md` and `AGENTS.md` mention neither `Explore` nor `Area Name`.
- **Rules** — WARN. `.ai-factory/RULES.md` does not exist, so there was nothing to check against.
- **Roadmap** — OK. The plan heading matches contract line 52.1 in `.ai-factory/roadmaps/trickster77777.md`, under Phase 52 (`Governing spec: docs/test-coverage-pass.md`). I read the chain: contract line → task spec `specs/trickster77777/0204-…md` → phase note `specs/trickster77777/146-roadmap-test-coverage-leftovers.md` → target file. The plan's three replacement texts match the spec's § "What must be true after" word for word.
- **Governing spec** — OK. I re-ran all three of the spec's sweeps against the current tree:
  - `Explore` appears only at the Layer 4 launch sentence.
  - `general-purpose` appears only at the Layer 5 launch and the Layer 7 failing-test agent.
  - `# <Area Name> — Test Plan` is the only title hit across `src/`, `docs/` and `CLAUDE.md`.
  - Every `<area name>` occurrence is one of the orchestrator's own labels: the input line, Layer 5's prompt and returns, the Layer 6 and Layer 7 hand-off lists, and the Layer 8 report.
  - `docs/test-coverage-pass.md` names neither the agent type nor the title, so it needs no edit.

### Previous review (plan-review-1)

The one minor issue is resolved. The plan now pins the slug paragraph's on-disk layout. The new last line, `not for the Area label above. The note's title carries that same name, in words.`, is 80 characters, which fits the file's existing column (other prose lines run to 80 and 81). The Verify step now greps `carries that same name` and the full title line, and neither phrase can be split by a line break. I confirmed the other numbers:
- The new launch line is 79 characters.
- `grep -n "Launch one \`general-purpose\` agent per area"` will match both Layer 4 (line 144 today) and Layer 5's existing line 210.
- After the edit, `grep -n "Explore"` and `grep -n "Area Name"` will return nothing.

### Critical Issues

None.

### Positive Notes

- The plan quotes each current text it replaces and pins each replacement verbatim from the spec. That leaves the implementer nothing to guess.
- It lists the lines that must not change: the `Area:` input line, the "Write the document below to …" paragraph, the `saved:` return line, the "Each agent writes its note to disk …" sentence, and Layers 5–8. Its final `git diff` check enforces that.
- It re-ran the spec's sweeps instead of copying them, and its findings match the repo.
- Frontmatter needs no change. `allowed-tools` already includes `Agent`, and Critical Rule 3 ("Layer 4 and 5 agents return one line") is unaffected.

PLAN_REVIEW_PASS

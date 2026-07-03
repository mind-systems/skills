# Code Review (round 2) — Engines carry a reverse-graph marker

**Scope:** `git diff HEAD` + `git status`
**Files changed:** `CLAUDE.md`, `src/skills/note/SKILL.md`, `src/skills/roadmap-engine/SKILL.md`, `src/skills/test-philosophy/SKILL.md` (milestone substance); plan/plan-review/review/sidecar artifacts.
**Risk level:** 🟢 Low — clean.

## Changes since round 1

- **Finding 1 (out-of-scope ROADMAP.md `---STOP---` move) — resolved.** `git diff HEAD -- .ai-factory/ROADMAP.md` is now empty; the STOP marker is back above `observe-logs` and the roadmap is untouched by this milestone.
- **Finding 2 (dangling modifier) — resolved.** All three markers now open "This is a load-once engine: its callers depend on its exact behavior …", matching the spec's suggested wording verbatim and removing the mis-attached introductory phrase.
- **Finding 3 (`grep -l "note"` noise) — informational only, inherent to the required convention; nothing to change.**

## Verification against the spec

Checked the current text of all four target files against `.ai-factory/specs/01-engine-reverse-graph-marker.md`:

- **Declarative, not imperative** — every marker states a property of edits and how the reverse graph is *computed* ("the reverse graph resolves via `grep …`"); no "before editing, run grep" imperative. A using agent finds nothing executable. ✓
- **No caller names** — grep literals are generic per engine; no caller enumerated. ✓
- **No new section, no frontmatter field** — prose appended to existing intro paragraphs only. ✓
- **Anchors** — `roadmap-engine` and `test-philosophy` extend their existing "Load this skill once per chat" sentences; `note` places the marker after its intro, before `## Workflow`, leaving `### Hooks (caller inputs)`, the default template, and default behavior untouched. ✓
- **Per-engine grep literals** — `"roadmap-engine"`, `"test-philosophy"`, `"note"` respectively; match the CLAUDE.md reverse-graph form. ✓
- **CLAUDE.md convention** — the added line completes the both-ends coupling rule (caller declares *whom* it loads; engine declares *that it is loaded* and how to find by whom) and specifies a new engine gets the marker with its first `loads:` edge. Matches spec Edit 2. ✓
- **Markdown** — double-backtick code spans render correctly and protect the `*` glob characters from emphasis parsing. ✓

No bugs, security issues, or correctness problems.

REVIEW_PASS

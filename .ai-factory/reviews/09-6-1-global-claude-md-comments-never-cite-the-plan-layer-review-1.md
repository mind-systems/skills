# Review: 6.1 — global CLAUDE.md: comments never cite the plan layer

## Scope
Single change: one bullet appended to `src/global/CLAUDE.md` § "Documentation style". No code, no tests, no runtime surface — this is a change to user-level instructions text.

## Verification against spec `.ai-factory/specs/58-global-comments-never-cite-plan-layer.md`
- **Exact text** — the added bullet matches the spec verbatim, including the `**Comments never cite the plan layer.**` bold lead, the phase/note-number / `ROADMAP`/`Plan` / `.ai-factory/` path enumeration. ✓
- **Placement** — line 16, immediately after "Describe behavior, not code." (line 15) and before "No file/directory trees." (line 17), inside § "Documentation style". Matches the spec's required position. ✓
- **Pure prohibition** — no positive "link `docs/` instead" limb, no second sentence, no provenance sentence. ✓
- **Additions only** — `git diff --numstat` reports `1 0` (one line added, zero removed); every pre-existing line is byte-identical. ✓
- `grep -n "Comments never cite the plan layer" src/global/CLAUDE.md` → exactly one hit (line 16). ✓

## Runtime / correctness
No executable code, migrations, types, or concurrency involved. Nothing to break at runtime.

## Findings
None.

REVIEW_PASS

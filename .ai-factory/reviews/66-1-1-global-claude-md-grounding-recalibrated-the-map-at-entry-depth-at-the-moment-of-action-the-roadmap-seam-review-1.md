# Code review: 1.1 — global CLAUDE.md grounding recalibrated

## Scope
Single changed source file: `src/global/CLAUDE.md` (the plan's `.md`/`.json`/plan-review artifacts are process files, not code). This is a user-level instructions document — no runtime, so the review is a fidelity check against the contract in `.ai-factory/specs/22-global-grounding-to-the-leaf.md`, whose guard states: "the four quoted blocks land verbatim; no rewording; existing section text byte-identical outside the insertions."

## What was verified

1. **Verbatim fidelity — all four blocks match the spec exactly.**
   - Block 1 (map / leaf at moment of action) → `src/global/CLAUDE.md:11`, character-for-character with spec §Change block 1, including em-dashes, bold `**map**`, and the "Never the whole tree" close.
   - Block 2 (held context decays) → `:13`, matches spec block 2 including the quoted `"already know it"`.
   - Block 3 (ROADMAP/ARCHITECTURE entry maps) → `:15`, matches spec block 3 including backticked paths and `## Features`.
   - Walkable-tree bullet → `:26`, matches the spec's Documentation-style bullet verbatim.

2. **Additions-only, existing text untouched.** `git diff HEAD` shows only inserted lines; every context line (the original Grounding-claims paragraph, the Documentation-style bullets) is unchanged. No pre-existing byte was modified.

3. **Correct placement.** The three grounding blocks land inside § "Grounding claims" after the original paragraph and before `## Documentation style`; the bullet lands at the end of the Documentation-style list. Rendered as plain paragraphs matching the section's existing formatting (not blockquotes), per the plan's Task 1 note.

4. **Spec verification checks pass.**
   - `grep -n "first artifact\|decays\|entry map\|walkable tree"` → four hits, one per inserted block, in the right sections.
   - `grep -ic "however much context"` → `0` (the deliberately-dropped eager-load phrasing is absent).
   - No eager/bulk-loading mandate introduced; "never the whole tree" constraint is carried inside the added text as required.
   - Content is project-agnostic (user-level instructions), no project-specific leakage.

## Findings
None. The change is a faithful, additions-only application of the contract; no correctness, security, or runtime concerns apply to an instructions document, and the verbatim-text and byte-identity guards both hold.

REVIEW_PASS

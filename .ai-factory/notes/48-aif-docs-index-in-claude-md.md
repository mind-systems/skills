# aif-docs: documentation index lives in CLAUDE.md, not in README

**Date:** 2026-07-02
**Source:** conversation context (orchestrator docs session)

## Key Findings

- `src/skills/aif-docs/SKILL.md` mandates a `## Documentation` table in README (Step 2.2 template, "Key rules for README", State B split rules, Step 1.1 "Add the new doc page to README's Documentation table", audit checks) — this contradicts the user's standing convention: **no README documentation table; the documentation index belongs in the project's CLAUDE.md**.
- The convention has a functional reason beyond taste: CLAUDE.md is the only channel loaded unconditionally into every agent run (including orchestrator agents working on the repo itself), so pages listed there become reachable edges of the agent's perception tree. A README table serves only human browsing, which the docs directory itself already covers.
- README stays a landing page (title, tagline, quick start, features, example, license) and may carry **one line** pointing at the docs directory and CLAUDE.md — never a table.

## Details

Edits to `src/skills/aif-docs/SKILL.md` — every place the README documentation table is created, updated, or audited is retargeted to CLAUDE.md:

1. **Core Principle 3 ("No duplication")** — reword: detailed info lives in the docs directory; the **documentation index lives in the project's CLAUDE.md** (`## Documentation` table: `| Doc | What it covers |`); README carries at most one pointer line to the docs directory, never an index table.
2. **Step 2.2 README template** — remove the `## Documentation` table section from the template and from "Key rules for README"; add the single pointer line in its place.
3. **New index step** (natural home: right after Step 2.2, or folded into Step 5) — create or update the `## Documentation` section in the project's `CLAUDE.md`: one row per doc page, README not listed, descriptions under ~12 words, same order as the docs directory's logical reading order. If CLAUDE.md does not exist, create it with only this section and a one-line header.
4. **Step 1.1 (consolidation)** — "Add the new doc page to README's Documentation table" → "Add the new doc page to CLAUDE.md's Documentation section".
5. **State B split (2.1/2.2) and State C audit (2.1)** — "Documentation links table" in the stays-in-README list → the pointer line; audit checks that verify the README table (existence, link validity) retarget to the CLAUDE.md section; add an audit check flagging a README that still carries a documentation table (legacy layout → propose moving it to CLAUDE.md).
6. **Step 5 (AGENTS.md)** — keep the existing AGENTS.md handling as is (skip silently when no section), but when AGENTS.md is a one-line redirect to CLAUDE.md, the CLAUDE.md section from item 3 is the single source and AGENTS.md is left untouched.

### Constraints

- All other aif-docs behavior unchanged: landing-page rules, docs-directory structure, 3D mode, `--web`, review checklists, no-motivation pass, language matching.
- The skill body is already over the 500-line guideline (known, accepted) — these edits must not grow it materially; prefer rewording existing lines over adding new blocks.
- Frontmatter unchanged.

## What NOT to do

- Do not remove the README entirely from the skill's ownership — it stays the landing page; only the index table moves.
- Do not generate the index into both README and CLAUDE.md "for compatibility" — single home, CLAUDE.md.
- Do not touch the upstream mirror copy (`upstream/ai-factory/aif-docs`) — only our `src/skills/aif-docs`.

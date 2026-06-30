# aif-roadmap: render milestones via roadmap-engine (two-tier)

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- Refactor `aif-roadmap` to **call `roadmap-engine` for output**. This is a deliberate **behavior change**: high-level milestones become two-tier (contract line + spec note) instead of inline short descriptions / verbose preambles.
- Keep aif-roadmap's **sole philosophy: granularity** — high-level major goals, 5–15 milestones, not granular tasks. The only thing that distinguishes aif-roadmap's output from decompose's is the coarseness of each task; the engine renders both identically.

## Details

### The change

aif-roadmap currently writes its own milestone lines (`- [ ] **Name** — short description`) with no spec note. After the refactor, each confirmed milestone is handed to `roadmap-engine`, which renders it as a contract line + a spec note at **coarse** (strategic) granularity.

### Concrete edits to `src/skills/aif-roadmap/SKILL.md`

- **Step 1.3 (Generate ROADMAP.md)** and **Step 2.4 (Add New Milestones)** — replace the inline "short description" rendering with: "Ensure `roadmap-engine` is loaded once in this chat, then hand each confirmed milestone to it to render note + contract line + save."
- **"ROADMAP.md Format" section** — delete the local short-description format; the format is the engine's.
- **Keep:** modes (create/update/check), Step 0 context loading, Step 1.2 exploration, all `AskUserQuestion` blocks, and Critical Rule 1 ("Milestones are high-level — each a major feature/capability, not a task"), which is the granularity philosophy.
- **Frontmatter `allowed-tools`** — add `Skill` (to load `roadmap-engine`).

### Files

- Edit `src/skills/aif-roadmap/SKILL.md`.
- `CLAUDE.md` Upstream Sync: `aif-roadmap` is currently under "Intentionally diverged from upstream". After this refactor it depends on a local-only engine and can no longer take upstream diffs — **move it to "Custom skills — never overwrite from upstream"**.

### Regression guard (static diff)

After the edit, `git diff src/skills/aif-roadmap/SKILL.md` must contain **only**: the removed inline render (Step 1.3 / Step 2.4 short-description output + the "ROADMAP.md Format" section) and the added "load `roadmap-engine` once, hand each milestone to it" glue. Any change to the preserved granularity philosophy — Critical Rule 1, the 5–15-milestones rules, modes, exploration, `AskUserQuestion` blocks — is a regression; revert it.

### What NOT to do

- **Preserve verbatim, do not paraphrase.** The granularity philosophy that stays — Critical Rule 1, the "5–15 milestones, high-level goal not task" rules, Step 0 context loading, Step 1.2 exploration, and every `AskUserQuestion` block — is kept **byte-identical** (copy the exact existing lines from the current `aif-roadmap/SKILL.md`). Do not reword, summarize, or reorder it; only the output lines change. A refactor here is a move, not a rewrite.
- Do not change the granularity philosophy — milestones stay high-level (5–15, major goals not tasks).
- Do not add the Atomicity Gate or the skeleton lenses — those belong to `roadmap-decompose` / `roadmap-decompose-skeleton`.
- Do not restate the roadmap/contract-line format locally — it is the engine's.

# Retire DESCRIPTION.md across our skills — CLAUDE.md is the single project-context source

**Date:** 2026-07-02
**Source:** conversation context (artifact-usefulness review)

## Key Findings

- DESCRIPTION.md duplicates the project CLAUDE.md almost entirely (stack, purpose, conventions) — a second home for the same facts, and every duplicated artifact in this ecosystem has demonstrably drifted. Every agent that reads DESCRIPTION.md runs via the claude CLI in the project cwd and therefore already receives CLAUDE.md unconditionally and for free.
- Its only unique tier — product vision — already lives elsewhere: the roadmap's `> vision` line (roadmap-engine format) and the CLAUDE.md `## Purpose` section.
- Decision: **retire it everywhere in the toolchain.** Our skills stop reading and mentioning it; `aif` stops generating it (note 50); `aif-architecture` sources from CLAUDE.md instead (note 51); the orchestrator's prompts drop it (separate task in the orchestrator's own roadmap). The DESCRIPTION.md files themselves have already been removed from all maintained projects (unique load-bearing facts salvaged into the respective CLAUDE.mds first) — this task retires the *reads*.

## Details

### The edit — grep-driven, not file-listed

The skills that reference DESCRIPTION.md are in flux (maintenance-flow and slim-down tasks may have landed); locate every live reference at implementation time:

```bash
grep -rn "DESCRIPTION" src/skills/ src/commands/
```

For each hit in **our** skills (expected: `roadmap-engine` (flow Step 0), `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage` (Layer 1), `aif-docs` (Step 0), plus whatever else the grep finds):

- Delete the "Read `.ai-factory/DESCRIPTION.md`" instruction. Do **not** replace it with a CLAUDE.md read — CLAUDE.md is loaded into every session automatically; instructing the read would be noise.
- Where DESCRIPTION.md was a listed fallback/source (e.g. roadmap vision line "from DESCRIPTION.md or user input", test-coverage's "if no DESCRIPTION.md, infer stack from package.json") — drop the DESCRIPTION branch and keep the remaining source(s): user input / conversation context / package-manager files.
- `ARCHITECTURE.md` and `RULES.md` reads stay untouched everywhere.

### Bookkeeping

- Skills-repo `CLAUDE.md`/docs: remove DESCRIPTION.md from any artifact lists (grep the repo docs too).
- Upstream mirror untouched — upstream skills keep their DESCRIPTION.md references; only `src/` copies change.

## What NOT to do

- Do not go hunting for DESCRIPTION.md files in projects — they are already removed; this task edits skill bodies only.
- Do not add explicit "read CLAUDE.md" instructions in place of the removed reads.
- Do not touch ARCHITECTURE.md / RULES.md handling.
- Do not edit the orchestrator from this task — its prompts are covered by its own roadmap task.

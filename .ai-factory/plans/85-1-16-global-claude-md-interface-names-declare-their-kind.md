# Plan: global CLAUDE.md: interface names declare their kind

## Context
Append one verbatim bullet to the global CLAUDE.md § "Planning workflow" so every planning tier (chat, decompose, skeleton lens, architect work-orders, orchestrator planners) inherits a rule that a newly named abstraction carries the language's interface marker — the kind readable from the name alone, a project's pinned form mandatory.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Append the rule

- [x] **Task 1: Append the "Interface names declare their kind" bullet**
  Files: `src/global/CLAUDE.md`
  In § "Planning workflow" (heading at line 50), append the bullet below as a **new last item**, after the existing "Deferred questions mean unfinished planning." bullet (currently the last in the section, before the next `## ` heading). Insert verbatim — no rewording, no project-specific example (`IPLRService`/tradeoxy stay out of the global file). Every existing line in the section and the rest of the file must remain byte-identical; this is an addition only.

  Exact text to append:

  ```
  - **Interface names declare their kind.** When a planning artifact — a roadmap line, a spec, a skeleton, a work-order, a plan — names a new abstraction, the name carries the language's own interface marker (`I` prefix, `Protocol` suffix, or whatever form the language's convention uses), so a reader tells a contract from a class by the name alone. Where the project's rules pin a specific form, that form is mandatory.
  ```

  Do **not** edit any skill body (`roadmap-decompose`, `roadmap-decompose-skeleton`, `agent-architect`, etc.) — the global file already loads into their sessions; this is the single home. Do not touch any project `RULES.md`.

  Verify: `grep -n "declare their kind" src/global/CLAUDE.md` returns exactly one hit inside § "Planning workflow", and `git diff src/global/CLAUDE.md` shows only the single added bullet.

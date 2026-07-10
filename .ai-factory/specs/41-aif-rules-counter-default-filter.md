# aif: rules generation gets the counter-default entry filter

## Current state

`src/skills/aif/SKILL.md` generates the project's rules artifact (`rules/base.md`) with no admission criterion, so it emits generic style conventions. Live evidence: `~/projects/tradeoxy/tradeoxy_analyst/.ai-factory/rules/base.md` — "Variables & functions: `snake_case`; Classes & Protocols: `PascalCase`; Constants: `UPPER_SNAKE_CASE`" — defaults the executor follows unprompted. The rules layer is the costliest instruction surface per line: the orchestrator reads it mandatorily at Step 0 of all four agents with override authority ("treat every rule as mandatory… they override general patterns"). By the composition model, a line there earns its place only as a **counter-default** — something the executor would naturally do otherwise — that **code alone cannot teach** (ground truth shows what *is*, never what must *never* change). Contrast the hand-grown `tradeoxy_core/.ai-factory/RULES.md`: proto-numerics-as-strings, branded UUIDs, no hand-written migrations — every rule counter-default, every rule with its why.

## Change

The rules-generation step of `aif` gains the **entry filter**, stated in the skill as the criterion the generated file must satisfy:

- A rule earns its line iff **(a)** the executor would do otherwise by default, and **(b)** the code alone cannot teach it; every rule carries its **why** (the incident or invariant behind it).
- Generic language/style conventions the agent already follows (case styles, formatting, idiomatic naming) are **explicitly excluded** — named in the skill as the anti-pattern, so generation stops producing them.
- The generation template's examples are rewritten to the passing genre (a counter-default with a why), so the template itself no longer seeds boilerplate.

## Files & types

- edit `src/skills/aif/SKILL.md` — the rules-generation step (and its template examples)

## Guards

- **Generation policy only** — the config.yaml machinery, mode skeleton, CLAUDE.md-first ordering are untouched (1.9.2's diet handles disclosure; this task changes what the rules artifact says, not where the instructions live).
- **Existing projects' rules files are not touched** — hygiene of already-generated files belongs to the Phase 2 alignment tasks (2.1/2.2).
- Runs **before** 1.9.2, so the diet moves the already-filtered template.

## Verification

- The skill states the two-part criterion and the why-requirement; the anti-pattern (style conventions) is named.
- Scratch run of `/aif`: the generated rules file contains only counter-default rules, each with a why; `grep -i "PascalCase\|snake_case\|UPPER_SNAKE"` over the generated file → zero.

# rules-generation.md: drop the dangling spec citation

Phase 19. `src/skills/aif/references/rules-generation.md` cites a task-spec file that does not exist — a pre-existing rotted reference that task 19.1 correctly left byte-identical (everything outside its four named edits stayed untouched), so it survives as its own cleanup. Surfaced as a deferred observation across 19.1's plan-review and code-review rounds.

## Current state (grounded, verified live)

- `src/skills/aif/references/rules-generation.md`, the "carries its why" paragraph, contains the parenthetical: `(see the composition-model reasoning in `.ai-factory/specs/41-aif-rules-counter-default-filter.md`)`.
- No such file exists: `grep -rl '41-aif-rules-counter-default-filter'` finds only this citation, and nothing named `41-*` or `*counter-default*` exists under `.ai-factory/specs/` or `.ai-factory/notes/` (the trickster77777 specs run 78/79/80/81). The path is a leftover from an earlier numbering scheme; the artifact it named is gone.
- The sentence around the parenthetical is self-contained without it: "This is the costliest instruction surface per line in the whole system: the orchestrator reads this file mandatorily at Step 0 of all four agents with override authority, treating every line as mandatory." It states the reasoning directly; the parenthetical only promised a deeper "composition-model" deep-dive that no longer exists.

## Change

- Drop the `(see the composition-model reasoning in `.ai-factory/specs/41-aif-rules-counter-default-filter.md`)` parenthetical, leaving the surrounding sentence intact. No repoint: no live artifact carries the referenced *composition-model reasoning*. The RULES.md contract itself (the (a)/(b) counter-default gate, carries-its-why, mandatory-at-Step-0) is stated in `docs/sakshi-harness/sakshi-harness.md`'s RULES.md wiring-contract bullet, but that is the contract, not the composition-model deep-dive the citation promised — so linking there would misdescribe the reference. Dropping the dead citation is the correct fix.

## Files & types

- edit: `src/skills/aif/references/rules-generation.md` (the one parenthetical only)

## Guards

- **Touch only the parenthetical.** The (a)/(b) counter-default gate, the carries-its-why requirement, the excluded-anti-pattern list, the near-empty-file default, and the `# Project Base Rules` scaffold stay byte-identical. No behavior of rules generation changes — this is a dead-link removal.
- **Preserve register** — the sentence keeps its existing voice; only the parenthetical is excised, with surrounding punctuation left reading cleanly.

## Verification

- `grep -rn '41-aif-rules-counter-default-filter' src/skills/` → zero hits.
- The "carries its why" sentence reads cleanly without the parenthetical and still states the costliest-surface / mandatory-at-Step-0 reasoning.
- `git diff --stat` touches only `src/skills/aif/references/rules-generation.md`.

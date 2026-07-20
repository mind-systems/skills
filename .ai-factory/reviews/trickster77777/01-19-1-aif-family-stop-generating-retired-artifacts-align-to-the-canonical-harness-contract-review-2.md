# Code Review 2 (re-review after fixes): 19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract

**Previous review:** `.ai-factory/reviews/trickster77777/01-19-1-…-review-1.md`
**Files re-read in full this pass:** `src/skills/aif/SKILL.md`, `src/skills/aif-architecture/SKILL.md`, `src/skills/aif-docs/SKILL.md`, `src/skills/aif/references/rules-generation.md`, plus spec, roadmap contract line, and plan.
**Risk level:** 🟢 Low — all three prior findings fixed; no new findings.

A note on method, because it nearly misled me: `git diff --stat` showed `aif-docs/SKILL.md` and `aif/SKILL.md` with **identical changed-line counts** to the previous pass (24 and 121), which reads as "untouched". Both had in fact changed — the fixes were one-for-one line substitutions, so the count held steady. The verdicts below come from reading the current bytes, not from the diffstat.

## Verdicts on previous findings

### Finding 1 — `aif-architecture/SKILL.md:135`, unswept `[resolved-architecture-path]` placeholder → **Fixed**

Current content, L133–136:

```markdown
## Architecture
See `.ai-factory/ARCHITECTURE.md` for module boundaries, folder structure, and dependency rules.
```

The placeholder is gone and the template now matches the prose above it (L128: "carries one `## Architecture` pointer line at `.ai-factory/ARCHITECTURE.md`"). Consumer projects will no longer receive an unsubstituted placeholder in their `CLAUDE.md`.

I re-ran the sweep with the **widened** pattern that catches the hyphenated form the original check could not — `grep -rn 'resolved[- ]architecture\|resolved[- ]docs\|resolved[- ]path'` across all four target files. `aif-architecture` returns **exactly one survivor**, L67:

> `- Use the resolved architecture directly, skip the recommendation step and proceed to Step 1.5`

That is the `$ARGUMENTS` architecture-*pattern* sense — the one named exclusion, correctly byte-identical. No hyphenated residue remains anywhere in the family.

### Finding 2 — `aif-docs/SKILL.md:32`, definition site scoped "below" its own referents → **Fixed**

Current content, L32:

> **Docs directory:** resolves to `docs/` by default, or the project's existing docs directory when one is already in use — detailed docs are written there. Every "resolved docs directory" reference **in this file** resolves against this definition. ARCHITECTURE.md is read from `.ai-factory/ARCHITECTURE.md`.

"below" → "in this file". The definition now governs the three `## Core Principles` uses at L19, L22, L24 that precede it, closing the forward-reference gap. The ~20 surviving "resolved docs directory" phrasings are the plan's deliberate ruling and now all resolve against a definition that claims them.

### Finding 3 — de-bracketed placeholders reading as literal output text → **Fixed** (all four sites)

`aif-architecture/SKILL.md` L143, L148, L153:

```
[success heading]

Pattern: [chosen pattern]
File: `.ai-factory/ARCHITECTURE.md`

[key rules heading]:
- [rule 1]

[closing sentence about workflow skills following these architecture guidelines]
```

`aif/SKILL.md` L192:

```
[completion heading]

- Project description: `CLAUDE.md`
```

Bracket notation is restored on every instruction-shaped slot, so each block is now internally consistent — `[success heading]` reads the same way as its sibling `[chosen pattern]`. None carries a `language.ui` reference, which is what the spec actually required removed. A sweep for the old unbracketed forms (`^Success heading$`, `^Completion heading$`, `^Closing sentence`, `^Key rules:$`) returns zero.

## New issues

None.

## Re-verified this pass (not carried from the previous review)

- **Residue sweep clean.** The narrow grep (`config.yaml`, `rules/base.md`, `.ai-factory/rules/`, `language.ui`, `language.artifacts`, `update-config`, `paths.docs`, `paths.architecture`) returns zero across all four target files. `references/` holds exactly `mcp-configuration.md`, `rules-generation.md`, `stack-analysis.md`.
- **The fixed-English invariant survived, with its discriminator intact.** `aif/SKILL.md:41` names all four artifacts *including `AGENTS.md`* — so it is provably the folded invariant, not the narrower pre-existing L37 statement. `aif-architecture:19` covers `ARCHITECTURE.md` and scopes prompts/confirmation to ambient. `aif-docs:34` carries both halves of the split.
- **Scope held.** No source file outside the three `aif*` skill directories is modified; the `upstream/ai-factory/` mirror is untouched.
- **`aif-docs` Step 5 symlink guard intact** (L246): when `AGENTS.md` is a symlink to `CLAUDE.md`, the CLAUDE.md section is the single source and AGENTS.md is left untouched. This matters because `aif` creates `AGENTS.md` as exactly that symlink — without the guard, Step 5's table write would write through to `CLAUDE.md`.
- **Spec and implementation agree** on the amended `aif-docs` ruling: the spec bullet rules `splits`, and its residual "fully ambient" occurrence is inside the sentence explaining why a blanket ruling was rejected — confirmed by content, not by grepping the phrase.

## Considered and cleared

`aif-architecture/SKILL.md` L120 and L122 instruct generating the artifact "**adapted to the project's tech stack and language**", which on its face sits oddly beside L19's fixed-English rule — and L120 was edited by this change, so it was in the implementer's hands. Cleared: "language" here means *programming* language, disambiguated at the point of use by `references/architecture-template.md:69` ("Adapt ALL examples to the project's language and framework — don't use TypeScript examples for a Go project"), a file L97 marks as a **CRITICAL** mandatory read before generation. No contradiction with the English invariant.

## Outstanding non-blocking item

The plan's **Task 10 live run** still shows no evidence of having been executed — no scratch artifacts, nothing in the working tree. All static checks now pass, but the runtime behaviors remain unexercised: the CLAUDE.md/RULES.md/ARCHITECTURE.md language split under a **non-English** session, and Modes 2/3 writing `.ai-factory/RULES.md` without an explicit `mkdir -p` step (Mode 1 has one at Step 5 item 2; the `Write` tool creates parent directories, so this is expected to work, but only a run confirms it). Both fixed placeholder sites from finding 3 are also user-facing output paths that only a live run exercises. This is a verification gap, not a defect in the code as written.

## Deferred observations

- Affects: `src/skills/aif/references/rules-generation.md:11` — cites `.ai-factory/specs/41-aif-rules-counter-default-filter.md`; no such file exists under `.ai-factory/specs/` or `.ai-factory/notes/`. Correctly left byte-identical by this task. Pre-existing rot; wants its own contract line to repoint or drop the parenthetical. [fixed]
- Affects: `orchestrator/.ai-factory/` — `orchestrator/docs/configuration.md:87` disambiguates the orchestrator's own overlay against `.ai-factory/config.yaml`, which this task retires; the sentence now disambiguates against nothing. Outside this repo's scope guard. [fixed]
- Affects: `src/skills/aif/SKILL.md:5` — no `Bash(ln *)` grant while `## AGENTS.md Generation` runs `ln -sfn CLAUDE.md AGENTS.md`. Carried by contract line 19.2 with a matching guard on the shared L5 edit; correctly untouched here. [fixed]

REVIEW_PASS

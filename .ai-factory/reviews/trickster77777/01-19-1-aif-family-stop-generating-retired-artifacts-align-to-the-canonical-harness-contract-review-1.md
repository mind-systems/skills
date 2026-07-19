# Code Review: 19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract

**Files reviewed in full:** `src/skills/aif/SKILL.md`, `src/skills/aif-architecture/SKILL.md`, `src/skills/aif-docs/SKILL.md`, `src/skills/aif/references/rules-generation.md`, plus the three deleted reference files, the spec, the roadmap contract line, and the plan.
**Risk level:** 🟡 Medium — one residue that ships an unsubstituted placeholder into every consumer project's `CLAUDE.md`, and that every automated check in the plan and spec passes green on.

## What the change does correctly

Verified live rather than taken from the plan:

- **The retirement is complete and strands nothing.** `references/` now holds exactly `mcp-configuration.md`, `rules-generation.md`, `stack-analysis.md`. The `Bash(node *update-config.mjs*)` grant is gone from `allowed-tools` while every other grant survives for 19.2 to extend. No repo doc, `CLAUDE.md`, `README.md`, or `ARCHITECTURE.md` references the retired artifacts. `active/skills/{aif,aif-architecture,aif-docs}` are directory-level symlinks and still resolve.
- **The narrow residue grep returns zero** across all four target files for `config.yaml`, `rules/base.md`, `.ai-factory/rules/`, `language.ui`, `language.artifacts`, `update-config`, `paths.docs`, `paths.architecture`. Every hit in the wider bare-`config` net is a legitimate survivor (MCP configuration; the documented *project's* config files).
- **The fixed-English invariant survived both deletion ranges.** `aif/SKILL.md:41` names all four generated artifacts including `AGENTS.md` — so it is the folded invariant, not the pre-existing narrow L37 statement. `aif-architecture/SKILL.md:19` restates it for `ARCHITECTURE.md` and correctly scopes prompts/confirmation to ambient. This was the plan's designated must-not-fail and it landed.
- **`aif-docs`' split ruling landed as amended** (`aif-docs/SKILL.md:34`): docs content ambient, the `## Documentation` index sections written into `CLAUDE.md`/`AGENTS.md` fixed English. This closes the cross-skill contradiction against `aif/SKILL.md:37`, which declares that same table a fixed English heading.
- **Step renumbering is contiguous and every cross-reference was updated with it** — Mode 1 "generated in Step 2", Mode 2 "once Step 2's dialog answers land", Mode 3 "once Step 3's dialog answers land" all resolve to the right steps. No `#language-resolution` anchor survives; the remaining `#claudemd-generation` / `#agentsmd-generation` / `#critical-do-not-implement` anchors all have live targets.
- **All three modes now write `.ai-factory/RULES.md`** (Mode 1 Step 5 item 3; Modes 2/3 Step 4), closing the pre-existing gap that would have made the spec's scratch-project check unsatisfiable via Mode 3.
- **`rules-generation.md`** renames the emission target in all three places and leaves the counter-default gate, excluded-anti-pattern list, near-empty-file default, and `# Project Base Rules` scaffold byte-identical, as required.

## Findings

### 1. `aif-architecture/SKILL.md:135` — unswept `[resolved-architecture-path]` placeholder ships into every consumer project's CLAUDE.md

Step 3 emits this literal block into the project's `CLAUDE.md`:

```markdown
## Architecture
See `[resolved-architecture-path]` for module boundaries, folder structure, and dependency rules.
```

Every other "resolved architecture path" phrasing in the file was correctly settled on the literal — including, two lines above this block, the prose that now reads "carries one `## Architecture` pointer line at `.ai-factory/ARCHITECTURE.md`". The template the prose introduces still carries the retired vocabulary, so Step 3 instructs writing a concrete path and then shows a template that does not contain one.

**Failure scenario.** `/aif-architecture` runs against any project. Step 3 emits the block into `CLAUDE.md`. Unlike its siblings in the Step 4 confirmation block, this placeholder has no adjacent instruction naming what to substitute — the surrounding bullets now say `.ai-factory/ARCHITECTURE.md` literally, so the placeholder reads as a leftover rather than a fill-in. The likely output is a project `CLAUDE.md` carrying a literal `See \`[resolved-architecture-path]\` for module boundaries…` — a broken pointer line in the trunk document of the context tree, in the one artifact `aif-architecture` is allowed to touch outside its own. Worst case it is emitted verbatim into every project the family sets up.

**Why every check passed it.** This is the plan's own false-green taxonomy on a fifth axis it did not enumerate — **the hyphenated form**. The plan's sweep and its verification both key on `grep -n 'resolved architecture'` (space-separated); the live string is `resolved-architecture-path` (hyphens), which that pattern structurally cannot match. The spec's Verification bullet — "complete when `grep -n 'resolved architecture'` returns exactly one survivor" — returns exactly one survivor (L67, the `$ARGUMENTS` pattern sense) and reads green. The plan additionally enumerated this exact line (as L141, pre-shift) in Task 5's sweep list, so it was named and still missed; the grep that was meant to backstop the enumeration shares the enumeration's blind spot.

**Fix:** settle L135 on `.ai-factory/ARCHITECTURE.md`, matching the prose above it. Then widen the verification pattern to `resolved[- ]architecture` so the check can see the form it just missed.

### 2. `aif-docs/SKILL.md:32` — the docs-directory definition site sits below three of its own referents

Step 0 establishes the definition and scopes it explicitly: "Every 'resolved docs directory' reference **below** resolves against this definition." But `## Core Principles` uses the term at L19, L22, and L24 — all above L32. Those three lines previously carried their own self-contained `(paths.docs, default: docs/)` parenthetical, which the sweep correctly removed as retired vocabulary; nothing replaced the standalone readability it provided.

**Failure scenario.** A reader (or an executor loading the body top-down) reaches L19's "Everything written under the resolved docs directory is governing-spec genre" with no definition of the term in scope, and the only definition present disclaims coverage of that position. Low severity — Step 0 is read within the same file on any real run, and the default `docs/` is inferable from L24's example — but the definition's own "below" makes the gap explicit rather than merely implicit.

**Fix:** drop the word "below" from L32 so the definition governs the file, or add a short pointer at L19's first use.

### 3. `aif/SKILL.md:192`, `aif-architecture/SKILL.md:143,148,153` — de-bracketed placeholders now read as literal output text

Converting `[Localized … in \`language.ui\`]` to plain prose conforms to the spec, but it landed as bare unbracketed lines *inside fenced example blocks whose sibling fill-ins kept bracket notation*:

```
Success heading            ← L143, no brackets

Pattern: [chosen pattern]  ← L145, bracketed fill-in
File: `.ai-factory/ARCHITECTURE.md`

Key rules:                 ← L148
- [rule 1]
```

Same shape at `aif/SKILL.md:192` ("Completion heading" above `- MCP configured: [list]`), and `aif-architecture:153` ("Closing sentence about workflow skills following these architecture guidelines.").

**Failure scenario.** Within one block, `[chosen pattern]` signals "substitute me" and `Success heading` does not. An executor renders the block and emits the literal string `Success heading` — or the literal sentence "Closing sentence about workflow skills following these architecture guidelines." — as user-facing output, instead of writing an actual heading in the ambient language. The prose above each block ("Present the confirmation in the ambient language") is the only thing preventing it.

**Fix:** restore bracket notation for the instruction-shaped slots — `[success heading]`, `[key rules heading]`, `[closing sentence about workflow skills following these architecture guidelines]`, `[completion heading]` — keeping them free of `language.ui`, which is what the spec actually required removed.

## Note on verification status

The plan's Task 10 (live `/aif` scratch-project run, then `/aif-architecture` + `/aif-docs`, in a **non-English session**) does not appear to have been run — no scratch artifacts and nothing in the working tree indicates one. That run is the only check that can distinguish a live language rule from a dead letter, and it is also the check most likely to have surfaced finding 1: a non-English `/aif-architecture` run writes the Step 3 pointer line into `CLAUDE.md`, where an unsubstituted `[resolved-architecture-path]` is visible immediately. Findings 1 and 3 are both in code paths that only a live run exercises.

## Deferred observations

- Affects: `src/skills/aif/references/rules-generation.md:11` — cites `.ai-factory/specs/41-aif-rules-counter-default-filter.md` as the home of its composition-model reasoning; no such file exists under `.ai-factory/specs/` or `.ai-factory/notes/` (verified). Correctly left byte-identical by this task, which required everything outside its four named edits unchanged. Pre-existing rot; wants its own contract line to repoint or drop the parenthetical.
- Affects: `orchestrator/.ai-factory/` — `orchestrator/docs/configuration.md:87` disambiguates the orchestrator's own overlay against `.ai-factory/config.yaml`; now that this task retires that artifact, the sentence disambiguates against nothing. Outside this repo's scope guard; recorded so the sibling-repo follow-up is not lost.
- Affects: `src/skills/aif/SKILL.md:5` — `allowed-tools` still grants no `Bash(ln *)` while `## AGENTS.md Generation` runs `ln -sfn CLAUDE.md AGENTS.md`. Already carried by contract line 19.2 with a matching guard about the shared L5 edit; correctly untouched here.

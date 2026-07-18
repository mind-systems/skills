# Plan Review: 17.2 — The "new work" coupling: one dictionary in the authoring skills (round 2)

## Code Review Summary

**Files Reviewed:** 1 plan + 7 target files + spec 63 + reserved-words + ROADMAP + round-1 review
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is untouched: no `loads:` edge, no engine/lens boundary, no reverse-graph marker in scope. Naming-only conformance does not move the graph.
- **Rules** — WARN (non-blocking). No `.ai-factory/RULES.md` in this repo; conventions live in CLAUDE.md and `docs/reserved-words.md`, both cited correctly by the plan.
- **Roadmap** — OK. `ROADMAP.md:28` is the contract line for 17.2, naming `Spec: .ai-factory/specs/63-new-work-coupling-reserved-words-conformance.md`; its governing spec is [reserved-words](../../docs/reserved-words.md). Walked both. The plan conforms on every pinned decision: `milestone`→**phase** in outline's `description:` product, `milestone`→**task** in decompose/skeleton, outline's `Use when` trigger word retained, `aif-docs:70` `ROADMAP milestone`→`ROADMAP phase`, detection-list "this milestone" left. No drift.
- **Skill-context** — no `.ai-factory/skill-context/aif-review/SKILL.md` present; no project overrides to apply.

### Round-1 findings — all five resolved, verified against the live files

1. **Length-preservation claim** — fixed. Assumption 1 now states the substitutions are *not* uniformly length-preserving and tabulates the six lengthening sites. I re-measured each against the live files and the arithmetic is now correct: `roadmap-decompose:6` 93→100 (`spec`→`detail` +2, `note`→`task spec` +5), `:79` 85→90, `:81` 87→92, `roadmap-decompose-skeleton:122` 89→96 (+12 for `` `Spec:` note ``→`` `Spec:`-tagged task spec ``, −5 from Task 6, net +7), `:123` 84→94, `:126` 90→95. The "leave long, do not rewrap" directive is grounded precedent, not invention — post-17.1 `roadmap-engine` carries lines at 95, 100, 114, and 145 chars.
2. **Gate arithmetic** — fixed. Task 10 now reads "exactly 3 matching lines, falling into 2 exempt categories", with the per-line/per-category distinction spelled out. The stated baseline of 18 matching lines is correct (re-run: 18).
3. **Straddling quote at decompose:6** — fixed. Task 3 now quotes the line-6 text alone and explicitly flags that `with` is the last word of line 5. Verified: line 5 ends `…types, and guards, with`, line 6 begins `the full spec persisted as a note`. The quoted string is now an exact-match target.
4. **Skeleton 122/124 collision** — fixed. Both lines now carry "apply both" on both sides (Task 6 and Task 7), Task 7 adds the general instruction to match against post-Task-6 state, and the net length-neutrality of line 124 is stated.
5. **Loose `\bnotes?\b` residue categories** — fixed. The gate is now sharpened to the single expected survivor `aif-docs:41`, with the phantom categories retired and the justification recorded in Assumption 4. Verified: none of the four files contains a backticked `` `note` `` skill reference, and all three roadmap skills declare `loads: roadmap-engine` / `roadmap-engine test-philosophy`.

### Findings

**1. Assumption 1's "unconditional" no-rewrap directive is contradicted by Task 2 — a regression introduced by the round-1 fix.** (`plans/04-17-2…md:21`, `:38`)

Assumption 1 closes with: "This directive is unconditional: **no task in this plan rewraps a paragraph or a folded block.**" Task 2 then does exactly that on `roadmap-outline:40–41`. The live pair reads:

```
40: Links to handoff/spec notes are allowed as plain markdown links inside the intro/
41: preamble prose — no formal `Spec:` tag, no invented notes.
```

Task 2's pinned result moves `intro/` from the end of line 40 to the start of line 41 — a word crossing a line boundary, which is what Assumption 1 forbids. Task 2 acknowledges it ("the wrap point moves within the pair but the line count does not change"), so the two statements are in direct opposition on the word "unconditional".

This is not the round-1 defect returning — the outcome here is fully deterministic, because Task 2 pins both replacement lines byte-for-byte and an implementer applying them cannot go wrong (new line 40 is 78 chars, line 41 ~69 — both within the file's ~85 wrap, so no long line results either). The defect is in the plan's own consistency: round 1's finding 1 was fixed by hardening Assumption 1 to "unconditional", and that hardening overshot into a claim the plan's own Task 2 violates. An implementer who reads Assumption 1 as governing may hesitate on Task 2, or worse, "correct" Task 2 back to a two-line split that preserves the original wrap point and silently changes the pinned bytes.

Fix within the plan, one clause: scope the directive to what it actually protects — no rewrap of a *folded frontmatter block or a multi-line paragraph whose line count or downstream numbering would shift* — and note Task 2's two-line pair as the one pinned, count-preserving exception. Both wordings yield the same edits; only one of them is self-consistent.

### Positive Notes

- **Site coverage is complete and independently re-verified.** I re-ran all three greps against the live files. Every one of the 20 `\bnotes?\b` hits and all 9 `spec\s+notes?` hits maps to a task: decompose 6/18/30/78/79/81/83/93, skeleton 35/117/122/123/124/126/127/132, outline 40/41, aif-docs 41/70. **Zero missed sites, zero over-reach.**
- **Every quoted pre-edit string matches the live file byte-for-byte.** I diffed all ~25 quoted fragments against the actual lines — including the two genuinely tricky wrapped sites (`decompose:29–30`, the `decompose:6` straddle). Each is now an exact-match `Edit` target.
- **The certification is real, not assumed.** `rg -U -in 'spec\s+notes?|milestones?' src/skills/agent-architect/SKILL.md src/agents/editor.md` returns exit 1 (zero hits), confirming Task 9 before the work starts. `command-pin-gaps:17`'s `contract line` and quoted `"Named roadmaps"` section title, and `:21`'s generic `field types`, are all confirmed conformant as stated.
- **The `decompose:6` `spec`→`detail` call is the right one and is properly justified.** The bare-note guard alone would yield "the full spec persisted as a task spec" — redundant nonsense. The plan instead mirrors the engine's own landed description, and I confirmed `roadmap-engine:5` reads "contract line plus a full task spec written via note". The mirror claim is accurate.
- **All five `wc -l` baselines verified**: outline 75, decompose 97, skeleton 148, aif-docs 271, plus the three certified files.
- **Cross-file coupling handled in lockstep.** `skeleton:126`'s reference to `roadmap-decompose`'s "in-place note-update discipline" is renamed alongside Task 5's rename of the discipline itself — I grepped for `Note-handling|note-update` repo-wide and these are the only two sites, both covered. A per-file sweep would have broken this.
- **Mention-vs-use reasoning at `aif-docs:26/182` is correct and load-bearing.** Both lines are forbidden-phrase detection lists; rewriting `"this milestone"` there would make the detector miss the phrase it exists to catch — behavior, not naming. Correctly protected.
- **`Spec:` tag vs artifact is pinned per site**, including the subtle `skeleton:132` call where `note tag` means the tag and the noun is dropped rather than substituted.
- **Scope restraint surfaced, not silently expanded** — `command-pin-gaps:17`'s bare artifact-`note` is left alone per spec 63 § Guards and reported rather than swept.

## Deferred observations

- Affects: Phase 17 (task 17.4, or a new standalone) — `src/commands/command-pin-gaps.md:17` carries **two** bare artifact-`note` sites, not the one the plan surfaces: `` scanning each contract line and its `Spec:` note file `` and, earlier on the same line, `the scope under discussion in chat (a named task, phase, or note)`. Both are correctly out of scope for 17.2, whose bare-note sweep is scoped to edited files and which certifies `command-pin-gaps` as no-change. The forward-looking concern is that no remaining task appears to claim them: 17.3 covers `roadmap-test-coverage`/`roadmap-prune`/the rescue pair, and 17.4 enumerates `detangle`, `temporal-tree`, `aif`, `aif-architecture`, `observe-logs`, `command-handoff`, `command-commit-roadmap-update` — `command-pin-gaps` is named in neither. Unless it is folded into 17.4's standalone sweep, the One-dictionary direction will close with two retired synonyms alive in a command file. Worth a line in 17.4's spec rather than a change here.

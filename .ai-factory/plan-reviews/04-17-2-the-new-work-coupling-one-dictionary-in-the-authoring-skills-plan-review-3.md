# Plan Review: 17.2 — The "new work" coupling: one dictionary in the authoring skills (round 3)

## Code Review Summary

**Files Reviewed:** 1 plan + 7 target files + spec 63 + reserved-words + ROADMAP + rounds 1–2 reviews
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is untouched: no `loads:` edge, no engine/lens boundary, no reverse-graph marker in scope. Naming-only conformance does not move the skill graph.
- **Rules** — WARN (non-blocking). No `.ai-factory/RULES.md` in this repo; conventions live in CLAUDE.md and the governing spec [reserved-words](../../docs/reserved-words.md), both cited correctly by the plan.
- **Roadmap** — OK. `ROADMAP.md:28` is the contract line for 17.2 and names `Spec: .ai-factory/specs/63-new-work-coupling-reserved-words-conformance.md`; that spec names its own governing spec, [reserved-words](../../docs/reserved-words.md). Walked the full chain. The plan conforms on every pinned decision: `milestone`→**phase** in outline's `description:` product, `milestone`→**task** in decompose/skeleton, outline's `Use when` trigger word retained, `aif-docs:70` `ROADMAP milestone`→`ROADMAP phase`, detection-list `"this milestone"` left. No drift from the contract line, no over-reach beyond it.
- **Skill-context** — no `.ai-factory/skill-context/aif-review/SKILL.md` present; no project overrides to apply.

### Round-2 finding — resolved, verified against the live files

**Assumption 1's "unconditional" no-rewrap directive vs. Task 2.** Fixed correctly, and fixed the way round 2 recommended: Assumption 1 now scopes the directive to what it actually protects — "no task rewraps a folded frontmatter block, and no task reflows a multi-line paragraph in a way that shifts its line count or moves downstream line numbers" — and names Task 2 as "the one **pinned, count-preserving exception**", with the explicit instruction not to "restore" the original wrap point. Task 2 and Assumption 1 now say the same thing. The two replacement lines remain pinned byte-for-byte, so the edit is deterministic regardless of which statement an implementer reads first.

Rounds 1 and 2's earlier findings remain closed — I re-verified each rather than inheriting the verdict: the length table in Assumption 1 (finding 1), the "3 matching lines / 2 exempt categories" gate arithmetic (2), the `decompose:6` straddle requote (3), the skeleton 122/124 "apply both" cross-references (4), and the sharpened single-survivor `\bnotes?\b` expectation (5).

### Critical Issues

None.

### Verification performed

- **Site coverage is complete — re-derived, not inherited.** I re-ran all three greps against the live files and mapped every hit to a task.
  - `[^-]milestones?` → 18 matching lines (the plan's stated baseline is correct): decompose 4/8/17/41/75/83/92 (Tasks 3, 4), skeleton 96/98/102/122/124/125/130 (Task 6), aif-docs 26/70/182 (Task 8 edits 70, exempts 26/182), outline 3 (Task 1, trigger retained). Post-edit residue is exactly the 3 protected lines.
  - `spec\s+notes?` → 9 hits: outline 40 (Task 2), decompose 18/29–30/93 (Task 5), skeleton 35/117/127 (Task 7), aif-docs 70 (Task 8). `command-pin-gaps` carries zero. Post-edit: zero.
  - `\bnotes?\b` → 20 hits, all covered; the only post-edit survivor is `aif-docs:41`'s ordinary-English `**Note:**`, matching the gate exactly. **Zero missed sites, zero over-reach.**
- **Every quoted pre-edit string is an exact-match `Edit` target.** I diffed all ~25 fragments against the live bytes, including the three that previously tripped rounds 1–2: the `decompose:6` straddle (line 5 does end `…types, and guards, with`), the `decompose:29–30` wrap, and the `outline:40–41` pair.
- **All six lengthening sites re-measured and correct**: `decompose:6` 93→100 (+7), `:79` 85→90, `:81` 87→92, `skeleton:122` 89→96 (+12 from Task 7, −5 from Task 6), `:123` 84→94, `:126` 90→95. Line *counts* are unaffected — every edit is within-line except Task 2's pinned two-line pair, which stays two lines.
- **`wc -l` baselines confirmed**: outline 75, decompose 97, skeleton 148, aif-docs 271.
- **The certification is real, not assumed.** `rg -U -in 'spec\s+notes?|milestones?' src/skills/agent-architect/SKILL.md src/agents/editor.md` returns exit 1 (zero hits). `command-pin-gaps:17`'s `contract line` and quoted `"Named roadmaps"` section title, and `:21`'s generic `field types`, are conformant as stated.
- **Cross-file coupling verified repo-wide.** `rg -uu -i 'Note-handling|note-update|Milestones are atomic|invented notes'` across the whole grove returns only the four sites inside the edited files — every one claimed by a task, and no external consumer references the renamed `Note-handling rule:` heading or the "in-place note-update discipline" phrase. The `decompose` ↔ `skeleton:126` pair is the sole lockstep coupling and both halves move together.

One measurement is off by a character: Task 2 annotates its new line 40 as 78 chars; the pinned bytes are 79. This changes no instruction and no output byte — the parenthetical's actual claim ("neither is long", both inside the file's ~85 wrap) holds at 79 — so it is recorded here rather than raised as a finding.

### Positive Notes

- **The `decompose:6` `spec`→`detail` call is right and properly grounded.** The bare-note guard alone would produce "the full spec persisted as a task spec"; the plan instead mirrors the engine's own landed description, and `roadmap-engine:5` does read "contract line plus a full task spec written via note".
- **Mention-vs-use at `aif-docs:26/182` is load-bearing and correctly protected.** Both are forbidden-phrase detection lists; rewriting `"this milestone"` there would make the detector miss the phrase it exists to catch — behavior, not naming.
- **`Spec:` tag vs. artifact is pinned per site**, including the subtle `skeleton:132` call where `note tag` means the tag and the noun is dropped rather than substituted, and `skeleton:122` where the artifact reading yields `` `Spec:`-tagged task spec ``.
- **Every protocol literal is held byte-identical** — `` `Spec:` ``, `Governing spec:`, `.ai-factory/specs/` paths, `loads:` values, frontmatter names — exactly the axis [using-the-language](../../docs/using-the-language.md) § "Protocol tokens are a different axis" separates from vocabulary.
- **Scope restraint is surfaced, not silently expanded.** `command-pin-gaps` is certified no-change and its bare artifact-`note` is reported rather than swept, per spec 63 § Guards.
- **The behavior gate is honest about its limit** — static byte-identity of the artifact-shape instructions (`### Phase N`, `**N.M — Name**`, aif-docs' governing-spec genre), with the reason a headless live render is impossible stated rather than glossed.
- **Three rounds of findings have each been fixed at the root** rather than patched around, and the round-2 fix did not re-introduce the round-1 defect.

## Deferred observations

- Affects: Phase 17 (task 17.4, or a new standalone) — `src/commands/command-pin-gaps.md:17` carries **two** bare artifact-`note` sites, not the one the plan surfaces in Assumption 3 and Task 9: `` scanning each contract line and its `Spec:` note file `` and, earlier on the same line, `the scope under discussion in chat (a named task, phase, or note)`. Both are correctly out of scope for 17.2, whose bare-note sweep is scoped to edited files and which certifies `command-pin-gaps` as no-change. The forward-looking concern is that no remaining task appears to claim them: 17.3 covers `roadmap-test-coverage`/`roadmap-prune`/the rescue pair, and 17.4 enumerates `detangle`, `temporal-tree`, `aif`, `aif-architecture`, `observe-logs`, `command-handoff`, `command-commit-roadmap-update` — `command-pin-gaps` is named in neither. Unless it is folded into 17.4's sweep, the One-dictionary direction will close with two retired synonyms alive in a command file. Worth a line in 17.4's spec rather than a change here. [fixed — command-pin-gaps.md:17 now reads "task spec" at both bare-note sites]

PLAN_REVIEW_PASS

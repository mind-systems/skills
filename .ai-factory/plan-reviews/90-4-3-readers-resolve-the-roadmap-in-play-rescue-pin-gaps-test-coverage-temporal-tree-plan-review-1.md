## Code Review Summary

**Files Reviewed:** 1 plan (targets 4 skill/command files)
**Risk Level:** 🟡 Medium

Plan under review: `4.3 — readers resolve the roadmap in play`. Root recovered: ROADMAP.md line 211 (Phase 4 — "Named roadmaps across the skill family"), governing spec `.ai-factory/specs/45-readers-resolve-roadmap-in-play.md`, whose own governing spec is `docs/multiuser-roadmaps.md`; the resolution's one home is roadmap-engine's "Named roadmaps" section (spec 43). Sibling `[x]` milestone 4.2 (`specs/44`, the writers) is the precedent for the same wiring and was read as the baseline.

The four wording edits themselves are correctly scoped and line-accurate: rescue `SKILL.md:177-180`, pin-gaps `:13`, test-coverage `:29`, temporal-tree `:67-70`. All four literals verified present. The problem is not what the plan changes but the integration wiring it omits.

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy") — **WARN.** The plan makes four skills newly depend on roadmap-engine's resolution content without establishing the engine-load edge the composition model requires (see Critical Issue 2).
- **Rules** (global CLAUDE.md → "Dependencies and the skill graph") — **ERROR.** "Every skill that loads another declares it in its own frontmatter `loads:` field." The plan adds no `loads: roadmap-engine` edge to any of the four readers, diverging from how sibling 4.2 wired the identical dependency.
- **Roadmap** — aligned. The plan traces cleanly to ROADMAP.md line 211 and spec 45; scope (four sites, resolution referenced-not-restated, defaults byte-stable) matches the contract line.

### Critical Issues

**1. Task 1 leaves milestone-rescue Step 1's inline restatement stale — it will contradict the widened Step 4.**
`milestone-rescue/SKILL.md:57-58` (Step 1, "Read the phase's governing spec") restates the resolution and explicitly claims parity: *"Determine `$TARGET_FILE` (the same resolution Step 4 uses: argument-named file if given, else `.ai-factory/ROADMAP_TESTS.md` for test slugs, else `.ai-factory/ROADMAP.md`)"*. Task 1 only rewrites Step 4's list at lines 177-180. After the edit, Step 4 will read *argument → my → default* with a named-roadmap test-sibling mapping, while Step 1 still lists the old three literal branches under the words "the same resolution Step 4 uses" — a direct internal contradiction, introduced by this milestone in a file it touches. This is a finding, not a deferred observation: it sits inside the target file and is fixable within the milestone boundary. Task 1 must also reconcile line 57-58 — either collapse the parenthetical to a pure pointer ("the same resolution Step 4 determines") or update it to the widened order. (Note the sentence at lines 62-64, "additive to Step 4's own `$TARGET_FILE` resolution", stays correct and needs no change.)

**2. The engine-load edge is unaddressed for all four readers — and two of them cannot load the engine as-is.**
The plan instructs each task to "Reference roadmap-engine's 'Named roadmaps' resolution … rather than restating it," but says nothing about *how* each reader obtains that section at runtime. The ratified pattern is visible in the sibling 4.2 writers (`roadmap-decompose`, `roadmap-outline`): they (a) declare `loads: roadmap-engine` in frontmatter, (b) instruct "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool…)", then (c) reference "see the engine's 'Named roadmaps' section for the slug/owner mechanics." The plan does only (c). Without (a)/(b) the pointer dangles: the agent needs the exact slug algorithm (local-part → lowercase → non-alnum runs to single hyphen) and the `> Owner:` verification/hard-stop to actually resolve "my roadmap", and the plan's own Task 1 parenthetical ("slug derivation, owner-line verification, hard-stop on mismatch") only names those mechanics without supplying them.

This splits by tool access:
- **rescue** (`allowed-tools` has `Skill`) and **test-coverage** (`allowed-tools` has `Skill`) — add `roadmap-engine` to `loads:` and a load-once instruction, matching their existing dependency pattern (rescue already does this for `orchestrator-artifacts`; test-coverage for `test-philosophy`).
- **command-pin-gaps** (`allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *)`) and **temporal-tree** (`allowed-tools: Read Bash(git *) Glob Grep`) — **have no `Skill` tool**, so they cannot load the engine via Skill at all. The plan must decide this explicitly: add `Skill` to their `allowed-tools`, or accept a Read-of-the-engine-file pointer, or state the minimal resolution inline (which collides with spec 45's "referenced, never restated" guard). As written, these two skills would carry a pointer to content they have no mechanism to reach.

This is the plan's central gap: it treats a cross-skill dependency as a pure wording change and never wires the dependency.

**3. temporal-tree's "my" tier is semantically questionable for historic, integration-branch reconstruction.**
Task 4 applies *argument → my → default* to temporal-tree per spec 45. But temporal-tree reconstructs the roadmap **snapshot at a feature's birth hash** (`git show <first-hash>:<roadmap path>`), and its entry point is the `## Features` table built by `roadmap-prune` — which milestone 4.4 (spec 46) and `docs/multiuser-roadmaps.md` define as an **integration-branch, repo-wide** operation. The feature timeline being reconstructed is therefore the integration roadmap's history, not a developer's personal `.ai-factory/roadmaps/<slug>.md`. If a user explicitly requests "my roadmap", `git show <hash>:.ai-factory/roadmaps/<slug>.md` will likely resolve to a path that did not exist at the historic hash (named roadmaps are a new feature) or to unmerged personal work — the wrong timeline. Practical risk is bounded because the engine activates "my" only on explicit user request (it "never infers multiuser mode"), so the default path stays `ROADMAP.md` as today. Still, the plan/spec should confirm whether temporal-tree genuinely wants the "my" tier or whether *argument → default* is the correct resolution for a skill whose subject is repo-wide pruned history. Because the tier is spec-dictated (spec 45), resolving this may route back to spec 45 rather than being fixed in the plan alone.

### Positive Notes
- Line citations are accurate and current; every `ROADMAP.md`/`ROADMAP_TESTS.md` literal the plan names was verified against the live files, including Task 4's instruction to grep at execution time (temporal-tree's only literals are `:67` and `:70`, both covered).
- The byte-identical guards are correctly enumerated per file and match spec 45's guard list (rescue depth/rollback/sidecar table, coverage's 8 layers + Class A/B, pin-gaps' hole taxonomy + `## Blocking decisions`, temporal-tree's walk order).
- Task 1 correctly preserves the test-keyword branch's *behavior* while widening it — mapping a named roadmap to its `-tests` sibling and the default to `.ai-factory/ROADMAP_TESTS.md` — which matches spec 45's Change bullet exactly.
- The "no `roadmaps/` → identical to today" invariant is stated in the plan's task-level preamble and holds for all four edits.

Findings 1 and 2 are blocking: as written the plan produces an internally contradictory rescue skill and four dangling engine references (two of them unreachable). Not writing PLAN_REVIEW_PASS.

## Plan Review Summary

**Plan:** `.ai-factory/plans/84-1-15-detangle-pyramid-revision.md` (milestone 1.15 — detangle pyramid revision)
**Governing spec:** `.ai-factory/specs/35-detangle-pyramid-revision.md`
**Direction:** "Pyramid rewrite — the skill package on the written philosophy"
**Files Reviewed:** 1 plan + spec 35 + `src/skills/detangle/SKILL.md` + the four standards (`docs/context-tree.md`, `docs/skill-pyramid.md`, `docs/skill-composition-model.md`, global § "Grounding claims") + revised siblings `temporal-tree` (1.13) / `roadmap-decompose-skeleton` (1.14)
**Risk Level:** 🟡 Medium

### Context Gates
- **Roadmap linkage** — WARN→OK: the plan's `# Plan: detangle — pyramid revision` heading resolves to ROADMAP.md line 187 (`- [ ] 1.15 — detangle: pyramid revision`), whose `Spec:` tag points at `specs/35-detangle-pyramid-revision.md`. Plan intent (audit-first, "no change" legal, protect the multi-tree raise) matches the spec's Change/Guards faithfully. Aligned.
- **ARCHITECTURE.md** — no boundary/dependency issue: the change is skill-body-internal, no module boundaries crossed, no `loads:` edge introduced (a doc reference is not a Skill-tool load — correctly not adding `loads:`).
- **RULES.md** — n/a (no project RULES.md governs this skills repo edit beyond CLAUDE.md conventions, which the plan honors).
- **Direction hard rule** — the pyramid direction states "the repo docs stay the philosophy's single home — skills link to them, never restate them." This rule is the source of the one finding below: it collides with the fact that detangle is a *globally-shipped* skill.

### Critical Issues

**1. The plan's proposed relink target `docs/context-tree.md "Две карты входа"` dangles for a globally-shipped skill.**
Task 1 and Task 2 instruct that restated shared ownership "becomes a link to its owner," naming as the example `docs/context-tree.md "Две карты входа" / global § "Grounding claims"` and treating the two as interchangeable (the `/`). They are **not** interchangeable:
- `detangle` is a generic skill exposed to every project via `~/.claude/skills → active/skills`. It executes inside *foreign* project roots (mind, tradeoxy, …), where `docs/context-tree.md` **does not exist**. A markdown link to it is a walkable edge only inside this skills repo and a dead 404 everywhere else — the opposite of the context-tree doctrine that links are "рёбра, по которым ходят."
- The global CLAUDE.md § "Grounding claims" is loaded into *every* session of *every* project (it is the user-global instruction file). It carries the two-entry-maps content verbatim ("`ROADMAP.md` … entry map of time … its counterpart `ARCHITECTURE.md` … entry map of space"). It is the only safe, always-available owner to point at — and `docs/context-tree.md` itself references it by name rather than by path ("живёт в глобальном CLAUDE.md, § «Grounding claims»").
- Ground truth confirms the pattern: `grep` over `src/skills/` + `src/commands/` for `context-tree`, `skill-pyramid`, `Grounding claims`, `global CLAUDE` returns **zero** hits. The two directly-revised siblings of this same genre — `temporal-tree` (1.13) and `roadmap-decompose-skeleton` (1.14) — carry **no** repo-doc link; `temporal-tree` kept a lean, self-contained "Before you start" instead. The direction's "skills link to them" rule was, in practice, satisfied for shipped skills by pointing at the always-loaded global rule and/or slimming in place — never by embedding a `docs/…` path.

**Fix:** amend Task 1/Task 2 so any relink points at **global § "Grounding claims"** (referenced by name, as context-tree.md does), and explicitly forbid inserting a `docs/context-tree.md` (or `docs/skill-pyramid.md`) path link into detangle's shipped body. Where the two-entry-maps / roadmap-seam material is a genuine restatement, prefer **slimming it in place** (leaning on the always-loaded global rule) over emitting a dangling link. Note `docs/context-tree.md` / the pyramid docs remain valid as **audit standards Task 1 reads** — the constraint is only on what lands *in the shipped SKILL.md*.

### Secondary Issues

**2. Relinking the executor imperatives in "Before you start" can silently drop behavior — state the safety condition.**
Lines 28–37 are executor-facing **imperatives** ("If `ARCHITECTURE.md` exists — read it. If `ROADMAP.md` exists — read it."). Per `skill-composition-model.md` § "У каждой строки два читателя," an imperative executes and a declaration/link does not. Converting these imperatives to a mere pointer is behavior-identical **only because** the global grounding rule already commands raising both maps at session entry — that is the load-bearing precondition. The plan's two-reader lens and "behavior-identical" guard imply this, but the plan never states it, so an executor could relink the imperative without confirming the owner still *commands* the read for the executor. Add one sentence to Task 2: a restated **imperative** may be relinked only if its owner (the always-loaded global rule) already issues the same executor command; otherwise slim, do not delink.

**3. Task 1's fourth lens over-points at protected content in "Depth rules" / "What NOT to do" (113–126).**
The plan asks the auditor to judge whether these restate "the grounding rule's decay/depth-at-action clauses." But detangle has no decay clause, and most of this block is detangle's own executor-facing climbing discipline — line 117 ("Read all consumers") is explicitly protected forest content, and line 118 ("If you cannot name the trunk-level invariant, you have not climbed high enough") is detangle's own climb test, not a grounding restatement. Note that spec 22 (milestone 1.1) *deliberately dropped* "however much it takes" from the global rule, so detangle's "Go as deep as the flow requires — not as deep as is easy" (line 116) may be a nuance the global rule intentionally does **not** carry — relinking it would lose content. The plan hedges ("Judge whether…"), so this is not fatal, but Task 1 should caution the auditor that this block skews toward detangle's own contribution and default to protection absent a clear one-to-one restatement.

### Positive Notes
- **Structure is correct for the genre.** Audit-first (read-only Task 1) → conditional apply (Task 2, skipped on conformance) → conditional live baseline (Task 3, only if body changed) maps cleanly onto spec 35's "revision, not a mandated rewrite" and "'no change' + a one-paragraph audit report is a legal, complete outcome."
- **Line references are all accurate** against the current 125-line SKILL.md: fractal model 14–24, Step 2 climb 47–66, Step 3 forest 68–80, synthesis/ASCII-map 84–103, intent split 105–108, depth rules / what-not-to-do 113–126, "Before you start" 28–37. No stale offsets.
- **The spec's hard guard is honored.** Both Task 1 and Task 2 protect the multi-tree shared-contract raise (Step 3 + line 117) and the leaf→trunk climb as detangle's own content, "never reduced to a doc link" — verbatim to spec 35's Guards.
- **Frontmatter assumption verified:** the current frontmatter is `name` / `description` / `argument-hint` only — no `loads:` / `allowed-tools`. Task 2's guard "none added" is correct, and correctly declines to add a `loads:` edge for a doc reference.
- **Task 3's baseline analogue is sound:** with no proto/DTO in this repo, using an engine consumed by multiple callers (`note`, reached via the canonical reverse-graph grep `grep -l "note" src/skills/*/SKILL.md src/commands/*.md`) is a legitimate in-repo stand-in for a cross-project forest raise; the grep syntax matches the CLAUDE.md convention.
- **No missing migrations / security surface:** the change is skill-text-only; no data, config, or executable path is touched.

## Deferred observations
- Affects: the pyramid direction's hard rule ("skills link to them, never restate them") vs. globally-shipped skills — The tension surfaced in finding 1 is broader than milestone 1.15: every top-level skill that ships via `~/.claude/skills` (detangle, temporal-tree, the roadmap family, command-handoff) cannot host a walkable link to `docs/*.md`, because those docs live only in the skills repo. The de-facto reconciliation across the completed 1.x tasks has been "point at the always-loaded global rule, or slim in place" — but the direction text still literally says "link to them." Reconciling the direction's wording with the shipped-skill reality (e.g. distinguishing "audit against the docs" from "link into the body") is a direction-level edit outside this milestone's file boundary; noting it here so a future pass can align the rule with observed practice. [fixed]

(No PLAN_REVIEW_PASS — finding 1 requires the plan to correct its relink-target guidance before implementation.)

# repo-stats-herald: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/repo-stats-herald` is a **single git repository, not a project family** — confirmed live: `find` for nested `.git` directories under it returns none. One `CLAUDE.md` (91 lines) at the root; no subproject `CLAUDE.md`s exist because no subprojects exist. One rules file: `.ai-factory/rules/base.md` (29 lines). One `AGENTS.md` (1 line): `See [CLAUDE.md](CLAUDE.md) as the single source of truth for this project.` — already the retired one-line-pointer form, never converted. No `DESCRIPTION.md` anywhere in the tree.

The pre-philosophy state 2.1/2.2 addressed at family scale shows up here at file scale: nobody has driven the context-tree philosophy over this repo's instruction layer, and its rules file has already drifted from the code it's meant to govern — `rules/base.md`'s "Module Structure" section describes `src/routes/`, `src/services/` (naming `ollama, github, telegram, changelog`), `src/models/`, and `src/config.py`; the actual tree (`find src -maxdepth 1 -type d`) is `src/core/`, `src/llm/`, `src/commits/`, `src/summarization/`, matching CLAUDE.md's own Architecture table exactly. The rules file describes a structure that was never built or was superseded before this pass — ground truth (code + CLAUDE.md) settles it.

**Stratigraphy note:** the line counts above are as-of-planning measurements, not execution inputs — re-measure on entry (see Grove entry checks) and budget against that measurement.

## Read first — the philosophy source (mandatory, before touching anything)

Raise the same context the authoring chat held, in this order:

1. `~/projects/sakshi/skills/docs/philosophy/context-tree.md` — the tree model: trunk/crown/roots, input-to-leaf raising, links as edges.
2. `~/projects/sakshi/skills/docs/philosophy/skill-pyramid.md` — tiny authoritative top, expanding depth, authority by reading order.
3. `~/projects/sakshi/skills/docs/philosophy/skill-composition-model.md` — one home per fact's deeper ground: duplication drifts; what to pin vs. what to trust.
4. `~/projects/sakshi/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring" — the normative rules (one home per fact, points-not-copies, present tense not change history, monorepo root routes by ownership; read the live file, it supersedes this summary).

Then raise the target's tree per that philosophy: the one root `CLAUDE.md`, its rules file, and — down the named edges — the `src/` layout and `docs/` tree it names, deeper wherever a claim must be verified (the Module Structure conflict above is exactly this kind of claim).

## Grove entry checks (run before the pass)

A project family is a **grove**; this target is **not one** — confirmed topology: `~/projects/repo-stats-herald` is a single git repository with no nested subproject repos and no plain subdirectory standing in for one either (per spec 24's "if some are plain subdirectories of one repo, the grove constraints apply only to the true-repo leaves" clause, taken to its limit: here there are zero true-repo leaves, so **none** of the grove-specific checks apply):

- **Topology:** single repo, confirmed — no grove premise to verify, no harness parent-load concern (there is only one `CLAUDE.md`; it is the session's own repo file, not a parent-loaded one), no README § Setup layout-guarantee to check (nothing is checked out separately — there is nothing to clone but this one repo).
- **What the three operations degrade to on a single file:** **dedupe** is intra-file only (the one `CLAUDE.md` must not repeat itself) and cross-genre-aware (the rules file and `CLAUDE.md` may describe the same fact from different registers — see Guards); **hoist** has no target — there is no leaf to move a meaning up from, so this operation is void for this task; **resolve conflicts** becomes CLAUDE.md/rules-file-vs-ground-truth resolution — the Module Structure conflict in Current state is exactly this operation's material.
- **Metric re-baseline:** re-measure `CLAUDE.md`'s line count on entry and budget "no growth" against that measurement, never against the 91 in Current state.

## Change

One pass over the single `CLAUDE.md` file, two of the three operations degrade as noted above; all still apply where they have material:

- **Dedupe** — check `CLAUDE.md` does not restate a fact in two of its own sections (spot-check on entry: its "Architecture" table and "Documentation" section both describe `src/` layout from different angles — verify they agree and neither drifts into restating the other's full detail).
- **Hoist** — void; no leaves exist.
- **Resolve conflicts** — never silently: ground truth from the code decides. The known conflict: `rules/base.md`'s "Module Structure" section names `src/routes/`, `src/services/` (`ollama, github, telegram, changelog`), `src/models/`, `src/config.py` — none of which exist; the real tree is `src/core/`, `src/llm/`, `src/commits/`, `src/summarization/`, matching CLAUDE.md's own Architecture table. Rewrite or drop the rules file's section to match ground truth (it is not stated confidently enough to be a forward-looking governing spec — nothing in CLAUDE.md or the roadmap names `routes/services/models` as a target shape). Every conflict found — resolved or escalated — is listed explicitly in the implementation report.

Also enforce while passing: **no skill or command names as routing** in the file; present tense, no change-history narration; `AGENTS.md` is a symlink to `CLAUDE.md`, not a one-line pointer file — content dropped, no salvage (the current one-line content is the exact retired template text, safe to discard unread); strip both the `# CLAUDE.md` H1 title and the boilerplate `This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.` intro line, plus the blank lines among/after them — contentless noise — so the file starts directly at its first real `## section`. **Adaptation for this file:** the title strips cleanly as its own standalone line, but the boilerplate is not its own line — line 3 reads `This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. What the service does and how each part behaves is specified under [docs/spec/](docs/spec-overview.md); this file is how to work in the code.` Strip only the boilerplate clause and its trailing space; the second sentence is real content (a pointer to the spec) and must survive intact on the same line.

**Fourth operation — rules hygiene.** `.ai-factory/rules/base.md` (29 lines) passes the counter-default filter: a rule survives iff the executor would do otherwise by default AND code alone cannot teach it, and it carries its why. Live noise-target preview: the "Naming Conventions" section (`snake_case.py` files/variables/functions, `PascalCase` classes) is standard Python convention an agent already follows by default — the same class of block spec 39 dropped from `tradeoxy_analyst`. The "Module Structure" section is the ground-truth conflict above, not a counter-default rule at all (it's a stale directory map, not a behavioral instruction) — correct or drop it, don't merely re-word it. "Error Handling" and "Logging" are more plausibly hand-grown and worth a real look (the Logging bullet overlaps CLAUDE.md's own "## Logging" section near-verbatim — note this at the coupling point; cross-genre overlap between `CLAUDE.md` and the rules file is not itself a violation, per the grove tasks' own precedent, but is worth a decision, not a silent pass). The file stays in place — the orchestrator's dedicated mandatory-read channel — only its content is filtered; every dropped rule is listed in the report.

**Fifth operation — orchestrator rules-path convergence.** The orchestrator reads a hardcoded `.ai-factory/RULES.md` in every prompt (`planner`/`implementer`/`reviewer`/`test-planner`) and never reads `rules/base.md` or `.ai-factory/config.yaml` at all (its own config is `orchestrator.json`) — `rules/base.md` sits at a path the orchestrator never opens. Convert it to the canonical `.ai-factory/RULES.md`: given the rules-hygiene operation above finds no surviving counter-default in this repo — Error Handling and Logging are both boilerplate error/logging idioms the excluded-anti-pattern rule forbids emitting, Logging additionally duplicating `CLAUDE.md`'s own "## Logging," which stays untouched as the fact's one home — the new `RULES.md` is header-only: its note states the exclusion rule and that an empty body below it is the correct result, not a gap to fill. The now-empty `rules/` directory is removed. The vestigial `.ai-factory/config.yaml` is removed outright — the orchestrator never reads it, and it is an artifact of aif skills outside our active set.

## Files & types

- edit (as needed): `~/projects/repo-stats-herald/CLAUDE.md`; `~/projects/repo-stats-herald/AGENTS.md` (convert to a symlink — it is not already one); `~/projects/repo-stats-herald/.ai-factory/rules/base.md` → `.ai-factory/RULES.md` (rules hygiene applied, then converted to the orchestrator's canonical path; `rules/` removed once empty); `~/projects/repo-stats-herald/.ai-factory/config.yaml` (removed outright — the orchestrator never reads it)
- read-only: everything else in `~/projects/repo-stats-herald` (code and `docs/` are ground truth for verification, never edit targets here); no README carve-out — there is no multi-repo layout to guarantee

## Guards

- **Scope is the instruction layer** — `CLAUDE.md`, `AGENTS.md`, and the one rules file; no edits to code, `docs/`, or anything else under `.ai-factory/`. The rules file is filtered in place, never deleted, never folded into `CLAUDE.md` — it is the orchestrator's imperative-genre channel with override authority.
- **Grounding over preference** — every kept, moved, or rewritten claim is verified against the actual code (read down the named edges: `src/`, `docs/spec-overview.md`, `docs/spec/`); no claim is invented or "improved" beyond what ground truth supports.
- **Preserve the file's language and register** — match what's there; this is alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/repo-stats-herald` by absolute path; nothing in the skills repo changes in this task.
- The read-first list above is a hard precondition — the experiment is void if the pass runs on chat-free context without those four sources loaded.

## Verification

- Spot-check: no meaning stated verbatim in two of `CLAUDE.md`'s own sections.
- The implementation report lists every conflict found (the Module Structure staleness at minimum), each with its ground-truth resolution or its escalation.
- `grep` the file for skill/command-name routing → zero; for history phrasing ("was replaced", "now uses instead") → zero.
- `AGENTS.md` is a symlink to `CLAUDE.md`.
- `CLAUDE.md`'s line count does not grow **vs the entry measurement** (the 91 in Current state is stratigraphy, not the baseline).
- The grove entry checks are recorded in the report as void-with-reason (single repo, no grove premise), not silently skipped.
- After editing the file's body, its header/intro/summary lines are re-scanned for now-superseded claims — same-file self-contradiction is the cheapest drift to create and the hardest for its author to see.
- `.ai-factory/RULES.md` exists at the orchestrator's canonical path, header-only (its note plus no surviving rule); `.ai-factory/rules/` no longer exists; `CLAUDE.md`'s own "## Logging" section is untouched — it remains the one home for that fact.
- `.ai-factory/config.yaml` no longer exists — removed outright as an aif-artifact the orchestrator never reads.

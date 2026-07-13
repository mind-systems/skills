# tradeoxy: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/tradeoxy` is a project family: a root `CLAUDE.md` (66 lines) over four subrepos with their own `CLAUDE.md`s — `tradeoxy_broker` (142), `tradeoxy_gui` (102), `tradeoxy_core` (91), `tradeoxy_analyst` (57); 458 lines total, grown independently. The same pre-philosophy state task 2.1 addresses in mind: likely duplication between root and leaves, shared meaning sitting repeated in leaves instead of hoisted, and possible root↔leaf contradictions. The root also carries its own `.ai-factory/` (ROADMAP, specs) — the monorepo-routing rules apply.

**Like 2.1, this is an experiment**: the philosophy must transfer through the written documentation alone.

**Stratigraphy note:** the line counts above are as-of-planning measurements, not execution inputs — re-measure on entry (see Grove entry checks). The 2026-07-11 ratification session (commits `d2aa9a9` root, `4ee7361` broker, `6f7c2d2` core, `2fdece6` analyst) has since grown the tree: root `docs/` now holds only `architecture.md` (the cross-project map), vendor references moved to their owner repos, root CLAUDE.md gained a "Documentation routing" section. That session's output is **fresh ground truth the pass must not treat as drift** — and partly its own dedupe input (see Change).

## Read first — the philosophy source (mandatory, before touching anything)

1. `~/projects/skills/docs/philosophy/context-tree.md`
2. `~/projects/skills/docs/philosophy/skill-pyramid.md`
3. `~/projects/skills/docs/philosophy/skill-composition-model.md`
4. `~/projects/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring"

Then raise the target's tree per that philosophy: the tradeoxy root `CLAUDE.md`, every subrepo `CLAUDE.md`, and — down the named edges — the first layer of docs/code each names, deeper wherever a claim must be verified.

## Grove entry checks (run before the pass)

A project family is a **grove**, not a tree: separate git repos, each leaf CLAUDE.md committed and published with its own repo, under a coordination root (`~/projects/skills/docs/philosophy/context-grove.md` is the model's home). The four operations below are defined on a tree; the grove adds entry checks:

- **Topology:** confirm the family shape — separate git repos under the root directory (true for tradeoxy).
- **Hoist premise — the layout guarantee.** Hoist, and deleting leaf-side duplicates of root facts, is licensed only because the root trunk reaches every leaf session *mechanically*: (a) the harness parent-loads CLAUDE.mds up the directory tree across git-repo boundaries — verify live once (open a session under a leaf; the root CLAUDE.md must be in context); (b) the family layout is **guaranteed** — the root `README` § Setup carries the agent-facing instruction: check out the exact directory structure and switch every repo to its freshest branch automatically (tradeoxy's README already mandates the tree; relative proto/build paths depend on it). This guarantee is a universal invariant of our multi-repo families; **if the README instruction is missing or incomplete, establish it during the pass** — the root README is an edit target for exactly this one section, mirroring the structure the other families use.
- **No upward-edge lines in leaves — ever.** Directory nesting plus harness traversal *is* the upward edge; a written back-pointer is a second home for a mechanically-delivered fact (noise while the layout holds, a dead path in a standalone checkout). A back-pointer found in a leaf is **dedupe input** — removed like any duplicate. Symmetrically, the root CLAUDE.md never enumerates its consumer projects — the harness carries the upward edge; the ownership routing tables are a different genre (they answer "where does a task go", not "who reads me") and stay.
- **Metric re-baseline:** re-measure the instruction-layer sizes on entry and budget "no growth" against that measurement, never against the stratigraphy in Current state.

## Change

One pass over the five `CLAUDE.md` files (root + four leaves), three operations — identical contract to spec 24:

- **Dedupe** — one home per fact; the second occurrence becomes a pointer (or is deleted where the home is auto-loaded anyway).
- **Hoist** — a meaning repeated across 2+ leaves moves to the root; leaf-specific facts stay in leaves; the root holds shared meaning and ownership routing (the sub-repo prefix/keyword tables stay intact).
- **Resolve root↔leaf conflicts** — never silently: ground truth from the code/config decides; a conflict ground truth cannot settle is escalated in the report, not invented; every conflict found — resolved or escalated — is listed explicitly in the implementation report. **Calibration: conflicts are the expected case, not the edge case** — budget this operation as primary (one prior sweep alone surfaced three instruction-layer lies: a "no roadmap yet" claim with a roadmap on disk, a pointer to a nonexistent `docs/concepts/`, a wrong gRPC default port); the report contract will have real material.

**Known dedupe inputs from the 2026-07-11 session:** the root CLAUDE.md "Documentation routing" section is itself a hoist-artifact the pass may compress; the root CLAUDE.md "Cross-project invariants" section partially duplicates root `docs/architecture.md` (§ Auth model / § Service identity) — CLAUDE.md keeps the one-line invariant + pointer, the doc keeps the mass. **Caution — two same-named layers:** root `docs/architecture.md` (cross-project map, English) and `tradeoxy_core/docs/architecture.md` (core's own, Russian) are different documents, both cited as "architecture.md § …" from different places; never merge or confuse them.

Also enforce while passing: **no skill or command names as routing** in any of the files — names rot when skills are renamed or retired, leaving dead routing paid on every run; routing is described in task terms (this rule is the task's own, not a loaded global — apply it from here); current-state-only; root `AGENTS.md` stays a one-line pointer.

**Fourth operation — rules hygiene.** The family's rules files (`tradeoxy_core/.ai-factory/RULES.md`, `tradeoxy_gui/.ai-factory/RULES.md`, `tradeoxy_broker/.ai-factory/RULES.md`, `tradeoxy_analyst/.ai-factory/rules/base.md`) pass the counter-default filter: a rule survives iff the executor would do otherwise by default AND code alone cannot teach it, and it carries its why; generic style conventions are deleted as noise — live target: analyst's `snake_case`/`PascalCase`/`UPPER_SNAKE_CASE` block. The hand-grown core rules (proto-strings, branded UUIDs, no hand migrations, protocol naming) are the passing genre — expected to survive intact. Files stay in place (the orchestrator's mandatory-read channel); every dropped rule is listed in the report.

## Files & types

- edit (as needed): `~/projects/tradeoxy/CLAUDE.md` + the four subrepo `CLAUDE.md`s; `~/projects/tradeoxy/AGENTS.md` only if it violates the one-line-pointer rule
- edit (grove-guarantee carve-out only): `~/projects/tradeoxy/README.md` — solely the § Setup layout-guarantee instruction (checkout structure + freshest-branch switch), only if absent or incomplete; nothing else in README
- read-only: everything else in `~/projects/tradeoxy` — docs, code, `RULES.md` files, `.ai-factory/` trees are ground truth for verification, never edit targets here

## Guards

- **Scope is the instruction layer** — the five CLAUDE.mds plus the rules files named above; no edits to code, docs/, or anything else under `.ai-factory/`; README only per the grove-guarantee carve-out in Files & types. Rules files are filtered in place, never deleted, never folded into CLAUDE.md — RULES.md is the imperative-genre channel the orchestrator reads with override authority.
- **Grounding over preference** — every kept, moved, or rewritten claim verified against the actual code/docs down the named edges.
- **Preserve each file's language and register** — alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/tradeoxy` by absolute path; nothing in the skills repo changes.
- The read-first list is a hard precondition — the experiment is void without those four sources loaded.

## Verification

- No meaning stated verbatim in two of the five files; shared meanings in the root; leaves carry leaf-specific content plus pointers.
- The implementation report lists every root↔leaf conflict with its ground-truth resolution or escalation.
- `grep` the five files for skill/command-name routing → zero; for history phrasing → zero.
- The root still routes by ownership; `AGENTS.md` is one line.
- The instruction-layer total does not grow **vs the entry measurement** (the counts in Current state are stratigraphy, not the baseline).
- The grove entry checks are recorded in the report: parent-load verified live, README § Setup guarantee present (or established under the carve-out), sizes re-measured.
- After editing any file's body, its header/intro/summary lines are re-scanned for now-superseded claims — same-file self-contradiction is the cheapest drift to create and the hardest for its author to see.

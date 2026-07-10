# tradeoxy: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/tradeoxy` is a project family: a root `CLAUDE.md` (66 lines) over four subrepos with their own `CLAUDE.md`s — `tradeoxy_broker` (142), `tradeoxy_gui` (102), `tradeoxy_core` (91), `tradeoxy_analyst` (57); 458 lines total, grown independently. The same pre-philosophy state task 2.1 addresses in mind: likely duplication between root and leaves, shared meaning sitting repeated in leaves instead of hoisted, and possible root↔leaf contradictions. The root also carries its own `.ai-factory/` (ROADMAP, specs) — the monorepo-routing rules apply.

**Like 2.1, this is an experiment**: the philosophy must transfer through the written documentation alone.

## Read first — the philosophy source (mandatory, before touching anything)

1. `~/projects/skills/docs/context-tree.md`
2. `~/projects/skills/docs/skill-pyramid.md`
3. `~/projects/skills/docs/skill-composition-model.md`
4. `~/projects/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring"

Then raise the target's tree per that philosophy: the tradeoxy root `CLAUDE.md`, every subrepo `CLAUDE.md`, and — down the named edges — the first layer of docs/code each names, deeper wherever a claim must be verified.

## Change

One pass over the five `CLAUDE.md` files (root + four leaves), three operations — identical contract to spec 24:

- **Dedupe** — one home per fact; the second occurrence becomes a pointer (or is deleted where the home is auto-loaded anyway).
- **Hoist** — a meaning repeated across 2+ leaves moves to the root; leaf-specific facts stay in leaves; the root holds shared meaning and ownership routing (the sub-repo prefix/keyword tables stay intact).
- **Resolve root↔leaf conflicts** — never silently: ground truth from the code/config decides; a conflict ground truth cannot settle is escalated in the report, not invented; every conflict found — resolved or escalated — is listed explicitly in the implementation report.

Also enforce while passing: **no skill or command names as routing** in any of the files — names rot when skills are renamed or retired, leaving dead routing paid on every run; routing is described in task terms (this rule is the task's own, not a loaded global — apply it from here); current-state-only; root `AGENTS.md` stays a one-line pointer.

**Fourth operation — rules hygiene.** The family's rules files (`tradeoxy_core/.ai-factory/RULES.md`, `tradeoxy_gui/.ai-factory/RULES.md`, `tradeoxy_broker/.ai-factory/RULES.md`, `tradeoxy_analyst/.ai-factory/rules/base.md`) pass the counter-default filter: a rule survives iff the executor would do otherwise by default AND code alone cannot teach it, and it carries its why; generic style conventions are deleted as noise — live target: analyst's `snake_case`/`PascalCase`/`UPPER_SNAKE_CASE` block. The hand-grown core rules (proto-strings, branded UUIDs, no hand migrations, protocol naming) are the passing genre — expected to survive intact. Files stay in place (the orchestrator's mandatory-read channel); every dropped rule is listed in the report.

## Files & types

- edit (as needed): `~/projects/tradeoxy/CLAUDE.md` + the four subrepo `CLAUDE.md`s; `~/projects/tradeoxy/AGENTS.md` only if it violates the one-line-pointer rule
- read-only: everything else in `~/projects/tradeoxy` — docs, code, `RULES.md` files, `.ai-factory/` trees are ground truth for verification, never edit targets here

## Guards

- **Scope is the instruction layer** — the five CLAUDE.mds plus the rules files named above; no edits to code, docs/, README, or anything else under `.ai-factory/`. Rules files are filtered in place, never deleted, never folded into CLAUDE.md — RULES.md is the imperative-genre channel the orchestrator reads with override authority.
- **Grounding over preference** — every kept, moved, or rewritten claim verified against the actual code/docs down the named edges.
- **Preserve each file's language and register** — alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/tradeoxy` by absolute path; nothing in the skills repo changes.
- The read-first list is a hard precondition — the experiment is void without those four sources loaded.

## Verification

- No meaning stated verbatim in two of the five files; shared meanings in the root; leaves carry leaf-specific content plus pointers.
- The implementation report lists every root↔leaf conflict with its ground-truth resolution or escalation.
- `grep` the five files for skill/command-name routing → zero; for history phrasing → zero.
- The root still routes by ownership; `AGENTS.md` is one line.
- The 458-line total does not grow.

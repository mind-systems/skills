# mind: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/mind` is a project family: a root `CLAUDE.md` (88 lines) over seven subprojects with their own `CLAUDE.md`s — `mind_mobile` (198), `mind_api` (115), `neiry_kit` (115), `mind_web` (72), `camera_ppg_kit` (66), `mind_mcp` (43), `mind_landing` (33); 730 lines total, grown independently over time. The skills repo has since articulated the philosophy these files predate: the context tree (session input → CLAUDE.md → docs → code, links as walked edges), one home per fact, CLAUDE.md points — it does not copy, root routes by ownership. Nobody has driven that philosophy over the mind tree: meanings are likely duplicated between root and leaves, shared meaning likely sits repeated in several leaves instead of hoisted to the root, and — the worst case — the root may contradict its leaves.

**This task is also an experiment**: the philosophy must transfer through the written documentation alone, not through the chat that produced it.

## Read first — the philosophy source (mandatory, before touching anything)

Raise the same context the authoring chat held, in this order:

1. `~/projects/skills/docs/context-tree.md` — the tree model: trunk/crown/roots, input-to-leaf raising, links as edges.
2. `~/projects/skills/docs/skill-pyramid.md` — tiny authoritative top, expanding depth, authority by reading order.
3. `~/projects/skills/docs/skill-composition-model.md` — one home per fact's deeper ground: duplication drifts; what to pin vs. what to trust.
4. `~/projects/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring" — the normative rules (one home per fact, points-not-copies, no skill-name routing, current-state only, monorepo root routes by ownership).

Then raise the target's tree per that philosophy: the mind root `CLAUDE.md`, every subproject `CLAUDE.md`, and — down the named edges — at least the first layer of docs/code each one names, deeper wherever a claim must be verified.

## Change

One pass over the eight `CLAUDE.md` files (root + seven leaves), three operations:

- **Dedupe** — a fact stated in two files keeps one home; the second occurrence becomes a pointer to the first (or is deleted when the home is already reachable). One home per fact, points-not-copies.
- **Hoist** — a meaning repeated across 2+ leaves belongs to the root: move it up, leave pointers (or nothing, where the root is auto-loaded context anyway). The root holds shared meaning and ownership routing; leaf-specific facts stay in leaves.
- **Resolve root↔leaf conflicts** — where the root claims X and a leaf claims Y: never pick silently. Read down to ground truth (the code/config the claim describes); the file that matches ground truth wins; rewrite the loser. A conflict that ground truth cannot settle (a genuine product decision) is escalated in the report, not invented. Every conflict found — resolved or escalated — is listed explicitly in the implementation report.

Also enforce while passing: **no skill or command names as routing** in any of the files — names rot when skills are renamed or retired, leaving dead routing paid on every run; routing is described in task terms (this rule is the task's own, not a loaded global — apply it from here); current-state-only (no "was changed/replaced" history); root `AGENTS.md` stays a one-line pointer.

**Fourth operation — rules hygiene.** The family's rules files (`mind_api/.ai-factory/RULES.md` — 57 lines, `mind_mobile/.ai-factory/RULES.md` — 9, plus any `rules/` dirs in `camera_ppg_kit`/`mind_web`) pass the counter-default filter: a rule survives iff the executor would do otherwise by default AND code alone cannot teach it, and it carries its why; generic style conventions the agent follows unprompted are deleted as noise. The files stay in place — they are the orchestrator's dedicated mandatory-read channel — only their content is filtered; every dropped rule is listed in the report.

## Files & types

- edit (as needed): `~/projects/mind/CLAUDE.md` + the seven subproject `CLAUDE.md`s; `~/projects/mind/AGENTS.md` only if it violates the one-line-pointer rule
- read-only: everything else in `~/projects/mind` (docs and code are ground truth for verification, never edit targets here)

## Guards

- **Scope is the instruction layer** — the eight CLAUDE.mds plus the rules files named above; no edits to mind's code, docs/, README, or anything else under `.ai-factory/`. Rules files are filtered in place, never deleted, never folded into CLAUDE.md — RULES.md is the imperative-genre channel the orchestrator reads with override authority.
- **Grounding over preference** — every kept, moved, or rewritten claim is verified against the leaf's actual code/docs (read down the named edges); no claim is invented or "improved" beyond what ground truth supports.
- **Preserve each file's language and register** — match what's there; this is alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/mind` by absolute path; nothing in the skills repo changes in this task.
- The read-first list above is a hard precondition — the experiment is void if the pass runs on chat-free context without those four sources loaded.

## Verification

- Spot-check: no meaning stated verbatim in two of the eight files; shared meanings live in the root; leaf files carry only leaf-specific content plus pointers.
- The implementation report lists every root↔leaf conflict found, each with its ground-truth resolution or its escalation.
- `grep` the eight files for skill/command-name routing → zero; for history phrasing ("was replaced", "now uses instead") → zero.
- The root still routes by ownership (prefix/keyword tables intact); `AGENTS.md` is one line.
- Total instruction-layer size does not grow: dedupe+hoist should shrink or hold the 730-line total, not inflate it.

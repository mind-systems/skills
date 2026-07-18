# mind: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/mind` is a project family: a root `CLAUDE.md` (88 lines) over seven subprojects with their own `CLAUDE.md`s — `mind_mobile` (198), `mind_api` (115), `neiry_kit` (115), `mind_web` (72), `camera_ppg_kit` (66), `mind_mcp` (43), `mind_landing` (33); 730 lines total, grown independently over time. The skills repo has since articulated the philosophy these files predate: the context tree (session input → CLAUDE.md → docs → code, links as walked edges), one home per fact, CLAUDE.md points — it does not copy, root routes by ownership. Nobody has driven that philosophy over the mind tree: meanings are likely duplicated between root and leaves, shared meaning likely sits repeated in several leaves instead of hoisted to the root, and — the worst case — the root may contradict its leaves.

**This task is also an experiment**: the philosophy must transfer through the written documentation alone, not through the chat that produced it.

**Stratigraphy note:** the line counts above are as-of-planning measurements, not execution inputs — re-measure on entry (see Grove entry checks) and budget against that measurement.

## Read first — the philosophy source (mandatory, before touching anything)

Raise the same context the authoring chat held, in this order:

1. `~/projects/sakshi/skills/docs/philosophy/context-tree.md` — the tree model: trunk/crown/roots, input-to-leaf raising, links as edges.
2. `~/projects/sakshi/skills/docs/philosophy/skill-pyramid.md` — tiny authoritative top, expanding depth, authority by reading order.
3. `~/projects/sakshi/skills/docs/philosophy/skill-composition-model.md` — one home per fact's deeper ground: duplication drifts; what to pin vs. what to trust.
4. `~/projects/sakshi/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring" — the normative rules (one home per fact, points-not-copies, present tense not change history — with the governing-spec/description mode split from the recalibrated Grounding claims — monorepo root routes by ownership; read the live file, it supersedes this summary).

Then raise the target's tree per that philosophy: the mind root `CLAUDE.md`, every subproject `CLAUDE.md`, and — down the named edges — at least the first layer of docs/code each one names, deeper wherever a claim must be verified.

## Grove entry checks (run before the pass)

A project family is a **grove**, not a tree: separate git repos, each leaf CLAUDE.md committed and published with its own repo, under a coordination root (`~/projects/sakshi/skills/docs/philosophy/context-grove.md` is the model's home). The four operations below are defined on a tree; the grove adds entry checks:

- **Topology:** determine mind's actual shape first — whether the seven subprojects are separate git repos under `~/projects/mind`. If some are plain subdirectories of one repo, the grove constraints apply only to the true-repo leaves; the rest are ordinary tree branches.
- **Hoist premise — the layout guarantee.** Hoist, and deleting leaf-side duplicates of root facts, is licensed only because the root trunk reaches every leaf session *mechanically*: (a) the harness parent-loads CLAUDE.mds up the directory tree across git-repo boundaries — verify live once (open a session under a leaf; the root CLAUDE.md must be in context); (b) the family layout is **guaranteed** — the root `README` § Setup carries the agent-facing instruction: check out the exact directory structure and switch every repo to its freshest branch automatically. This guarantee is a universal invariant of our multi-repo families; **if mind's README lacks the instruction, establish it during the pass** — the root README is an edit target for exactly this one section, mirroring the § Setup structure tradeoxy's README uses. **Entry audit (2026-07-13):** mind's README carries the layout under `## Repository layout`, not `## Setup`, with the checkout guidance but **no freshest-branch instruction**, and its subproject table/tree lists only **6 of 7** — `camera_ppg_kit` is absent. So this is a rename+augment of the existing section (add the freshest-branch switch, add the missing `camera_ppg_kit` row), not a from-scratch add.
- **No upward-edge lines in leaves — ever.** Directory nesting plus harness traversal *is* the upward edge; a written back-pointer is a second home for a mechanically-delivered fact (noise while the layout holds, a dead path in a standalone checkout). A back-pointer found in a leaf is **dedupe input** — removed like any duplicate. Symmetrically, the root CLAUDE.md never enumerates its consumer projects — the harness carries the upward edge; ownership routing tables are a different genre (they answer "where does a task go", not "who reads me") and stay.
- **Metric re-baseline:** re-measure the instruction-layer sizes on entry and budget "no growth" against that measurement, never against the stratigraphy in Current state.

## Change

One pass over the eight `CLAUDE.md` files (root + seven leaves), three operations:

- **Dedupe** — a fact stated in two files keeps one home; the second occurrence becomes a pointer to the first (or is deleted when the home is already reachable). One home per fact, points-not-copies.
- **Hoist** — a meaning repeated across 2+ leaves belongs to the root: move it up, leave pointers (or nothing, where the root is auto-loaded context anyway). The root holds shared meaning and ownership routing; leaf-specific facts stay in leaves.
- **Resolve root↔leaf conflicts** — where the root claims X and a leaf claims Y: never pick silently. Read down to ground truth (the code/config the claim describes); the file that matches ground truth wins; rewrite the loser. A conflict that ground truth cannot settle (a genuine product decision) is escalated in the report, not invented. Every conflict found — resolved or escalated — is listed explicitly in the implementation report. **Calibration: conflicts are the expected case, not the edge case** — budget this operation as primary (the tradeoxy family's equivalent sweep surfaced three instruction-layer lies in one session); the report contract will have real material.

Also enforce while passing: **no skill or command names as routing** in any of the files — names rot when skills are renamed or retired, leaving dead routing paid on every run; routing is described in task terms (this rule is the task's own, not a loaded global — apply it from here); present tense, no change-history narration (no "was changed/replaced" — a CLAUDE.md is a description of existing behavior); root `AGENTS.md` stays a one-line pointer.

**Fourth operation — rules hygiene.** The family's rules files (`mind_api/.ai-factory/RULES.md` — 57 lines, `mind_mobile/.ai-factory/RULES.md` — 9, plus any `rules/` dirs in `camera_ppg_kit`/`mind_web`) pass the counter-default filter: a rule survives iff the executor would do otherwise by default AND code alone cannot teach it, and it carries its why; generic style conventions the agent follows unprompted are deleted as noise. The files stay in place — they are the orchestrator's dedicated mandatory-read channel — only their content is filtered; every dropped rule is listed in the report.

## Files & types

- edit (as needed): `~/projects/mind/CLAUDE.md` + the seven subproject `CLAUDE.md`s; `~/projects/mind/AGENTS.md` only if it violates the one-line-pointer rule
- edit (grove-guarantee carve-out only): `~/projects/mind/README.md` — solely the § Setup layout-guarantee instruction (checkout structure + freshest-branch switch), only if absent or incomplete; nothing else in README
- read-only: everything else in `~/projects/mind` (docs and code are ground truth for verification, never edit targets here)

## Guards

- **Scope is the instruction layer** — the eight CLAUDE.mds plus the rules files named above; no edits to mind's code, docs/, or anything else under `.ai-factory/`; README only per the grove-guarantee carve-out in Files & types. Rules files are filtered in place, never deleted, never folded into CLAUDE.md — RULES.md is the imperative-genre channel the orchestrator reads with override authority.
- **Grounding over preference** — every kept, moved, or rewritten claim is verified against the leaf's actual code/docs (read down the named edges); no claim is invented or "improved" beyond what ground truth supports.
- **Preserve each file's language and register** — match what's there; this is alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/mind` by absolute path; nothing in the skills repo changes in this task.
- The read-first list above is a hard precondition — the experiment is void if the pass runs on chat-free context without those four sources loaded.

## Verification

- Spot-check: no meaning stated verbatim in two of the eight files; shared meanings live in the root; leaf files carry only leaf-specific content plus pointers.
- The implementation report lists every root↔leaf conflict found, each with its ground-truth resolution or its escalation.
- `grep` the eight files for skill/command-name routing → zero; for history phrasing ("was replaced", "now uses instead") → zero.
- The root still routes by ownership (prefix/keyword tables intact); `AGENTS.md` is one line.
- Total instruction-layer size does not grow **vs the entry measurement**: dedupe+hoist should shrink or hold it, not inflate it (the 730 in Current state is stratigraphy, not the baseline).
- The grove entry checks are recorded in the report: topology determined, parent-load verified live, README § Setup guarantee present (or established under the carve-out), sizes re-measured.
- After editing any file's body, its header/intro/summary lines are re-scanned for now-superseded claims — same-file self-contradiction is the cheapest drift to create and the hardest for its author to see.

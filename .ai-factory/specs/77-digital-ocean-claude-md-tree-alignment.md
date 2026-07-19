# digital_ocean: align the CLAUDE.md tree with the context-tree philosophy — dedupe, hoist, resolve root↔leaf conflicts

## Current state

`~/projects/digital_ocean` is a **single git repository, not a project family** — confirmed live: `find` for nested `.git` directories under it returns none; it is a server-management workspace for one remote host (`compmaster`, `185.138.186.243`), not a monorepo over sibling code repos. One `CLAUDE.md` (131 lines) at the root; no subproject `CLAUDE.md`s exist because no subprojects exist. **No rules files exist at all** (`.ai-factory/rules/base.md` and `RULES.md` both absent) — the rules-hygiene operation has nothing to filter this time, unlike 75/76.

One `AGENTS.md` (69 lines) — not the one-line-pointer form, a full stale project-map document: its own "Hosted Sites" table has 6 rows where `CLAUDE.md`'s "Nginx Virtual Hosts" table has 12 (verified against the real vhost configs in `configs/nginx/` — 10 live `server_name` entries plus the 2 CLAUDE.md itself marks "pending, not deployed"; `AGENTS.md`'s 6 rows are a strict subset, missing `admin`, `broker`, and both observability-stack domains entirely). It gets discarded with no salvage per the standing convention, so this staleness needs no separate fix — just confirms discarding it loses nothing worth keeping.

One `.ai-factory/DESCRIPTION.md` (85 lines) — the retired genre, to be dropped, but **not by blind deletion**: it carries facts absent from `CLAUDE.md` entirely — CPU (`Intel i5-4460, 4 cores, 3.2 GHz`), RAM (`15 GB`), GPU (`NVIDIA GeForce RTX 3090, 24 GB VRAM, CUDA`), disk (`228 GB, ~193 GB free`), the OS **version** (`Ubuntu 24.04` — `CLAUDE.md` never states an OS at all), and a "Non-Functional Requirements" pair (all server commands over SSH with explicit key/host/port; destructive operations require explicit user confirmation before execution) that `CLAUDE.md`'s own "Working with the Server" section only half-states (it prefers explicit SSH but never states the destructive-op confirmation rule). Unlike the mind family's DESCRIPTION.md retirements, these facts do **not** all salvage into `CLAUDE.md`: the CPU/RAM/GPU/disk/OS-version quintet is per-server hardware detail — not needed in every always-loaded session, and this workspace may hold more than one server over time — so it salvages into a new doc under `docs/` (a server-facts reference, structured to hold more than one server entry), consulted on demand rather than always-loaded. The one exception is the destructive-op confirmation rule: a behavioral working rule relevant to every session, not a per-server fact — it folds into `CLAUDE.md`'s own "Working with the Server" section instead. **Do not** salvage its Nginx/services tables — they are the same stale-subset pattern as `AGENTS.md`'s (8 rows vs. `CLAUDE.md`'s 12, verified against `configs/nginx/` the same way); `CLAUDE.md`'s own tables are already the freshest copy and must not be overwritten by the older ones during salvage.

**Intra-file staleness in `CLAUDE.md` itself:** the "Working with the Server" section still reads as a forward-looking placeholder — "Document the server's IP/hostname and key path here once known" — but the very next section, "Server Connection," already documents exactly that. The instruction is self-superseded and present-tense cleanup is due (this is not a two-file conflict, it is the single-file case the "re-scan header/intro for now-superseded claims" verification step exists for).

**README is out of scope, with one narrow exception.** `README.md`'s own "## Setup" is single-machine dev setup (clone this one repo, install an SSH key, verify the connection, start Claude Code) — not a multi-repo checkout guarantee, so the grove-guarantee carve-out this family's other specs use does not apply here (no clone-layout to fix). Its "## Config sync rule" section is a near-verbatim duplicate of `CLAUDE.md`'s own "## Config Sync" section — flagged for awareness, **not** an edit target (README stays read-only by default, same as spec 75's precedent). The one exception: README's "Workspace structure" tree lists `.ai-factory/DESCRIPTION.md — Detailed project spec`; once `DESCRIPTION.md` is retired per this task, that line becomes a dead reference purely as a side effect of this task's own edit — fix that one line (delete it or repoint it), nothing else in README.

**Stratigraphy note:** the line counts above are as-of-planning measurements, not execution inputs — re-measure on entry (see Grove entry checks) and budget against that measurement.

## Read first — the philosophy source (mandatory, before touching anything)

Raise the same context the authoring chat held, in this order:

1. `~/projects/sakshi/skills/docs/philosophy/context-tree.md` — the tree model: trunk/crown/roots, input-to-leaf raising, links as edges.
2. `~/projects/sakshi/skills/docs/philosophy/skill-pyramid.md` — tiny authoritative top, expanding depth, authority by reading order.
3. `~/projects/sakshi/skills/docs/philosophy/skill-composition-model.md` — one home per fact's deeper ground: duplication drifts; what to pin vs. what to trust.
4. `~/projects/sakshi/skills/src/global/CLAUDE.md` — §§ "Grounding claims", "Documentation style", "Project CLAUDE.md authoring" — the normative rules (one home per fact, points-not-copies, present tense not change history, monorepo root routes by ownership; read the live file, it supersedes this summary).

Then raise the target's tree per that philosophy: the one root `CLAUDE.md`, `AGENTS.md`, `DESCRIPTION.md`, and — down the named edges — `configs/nginx/` (ground truth for the vhost tables) and `docs/`, deeper wherever a claim must be verified.

## Grove entry checks (run before the pass)

A project family is a **grove**; this target is **not one** — confirmed topology: `~/projects/digital_ocean` is a single git repository with no nested subproject repos (per spec 24's "if some are plain subdirectories of one repo, the grove constraints apply only to the true-repo leaves" clause, taken to its limit: here there are zero true-repo leaves, so **none** of the grove-specific checks apply, exactly as spec 75 found for `repo-stats-herald`):

- **Topology:** single repo, confirmed — no grove premise to verify, no harness parent-load concern (there is only one `CLAUDE.md`), no README § Setup layout-guarantee to check (nothing is checked out separately beyond this one repo and an SSH key).
- **What the three operations degrade to on a single file:** **dedupe** is intra-file (the now-superseded "Working with the Server" placeholder) plus cross-file-vs-a-retiring-file (the DESCRIPTION.md salvage, which must not duplicate what `CLAUDE.md` already states more currently); **hoist** has no target — there is no leaf to move a meaning up from, void for this task; **resolve conflicts** becomes CLAUDE.md-vs-AGENTS.md-vs-DESCRIPTION.md-vs-ground-truth resolution — the three-way Nginx-table drift, verified against `configs/nginx/`, is this operation's material, and it resolves itself once the two stale copies are retired/discarded rather than requiring a separate edit to `CLAUDE.md`'s own (already-correct) table.
- **Metric re-baseline:** re-measure `CLAUDE.md`'s line count on entry and budget "no growth" against that measurement, never against the 131 in Current state — note `CLAUDE.md` itself grows only by the one destructive-op confirmation sentence from the DESCRIPTION.md salvage (the CPU/RAM/GPU/disk/OS-version quintet lands in a new `docs/` file instead, outside the instruction layer) and this modest growth should be weighed against the AGENTS.md/DESCRIPTION.md content leaving entirely; the net across the whole instruction layer (not `CLAUDE.md` alone) is what must not grow.

## Change

One pass over the single `CLAUDE.md` file (plus retiring `DESCRIPTION.md` and converting `AGENTS.md`), two of the three operations degrade as noted above; all still apply where they have material:

- **Dedupe** — fix the now-superseded "Working with the Server" placeholder once "Server Connection" states the same facts; check no other section of `CLAUDE.md` restates another's full detail.
- **Hoist** — void; no leaves exist.
- **Resolve conflicts** — never silently: ground truth (the real `configs/nginx/*.conf` files) decides. Verified: 10 live `server_name` entries plus 2 CLAUDE.md itself already marks pending/undeployed — `CLAUDE.md`'s own 12-row table is already the freshest and needs no rewrite for this fact; `AGENTS.md` (6 rows) and `DESCRIPTION.md` (8 rows) are the stale copies, handled by discard/retirement, not by editing `CLAUDE.md`. Every conflict found — resolved or escalated — is listed explicitly in the implementation report.

Also enforce while passing: **no skill or command names as routing** in the file; present tense, no change-history narration; `AGENTS.md` is a symlink to `CLAUDE.md`, not a rich stand-alone file — content dropped, no salvage (69 lines discarded unread, same class as mind's `neiry_kit`/tradeoxy's `tradeoxy_gui` precedent); `DESCRIPTION.md` is a retired genre — salvage its six unique facts first, then drop the file: CPU, RAM, GPU, disk, and OS version go into a new `docs/` file (per-server hardware facts, not always-loaded, structured to allow more than one server), while the destructive-op confirmation rule — a behavioral working rule, always relevant — folds into `CLAUDE.md`'s "Working with the Server" section; this is a variant of the "Retire DESCRIPTION.md; salvage unique facts" commit pattern already landed across the mind family, adapted here because the bulk of the salvage is per-server hardware detail rather than always-loaded instruction; strip both the `# CLAUDE.md` H1 title and the boilerplate `This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.` intro line, plus the blank lines among/after them — contentless noise, confirmed present as their own standalone lines here — so the file starts directly at its first real `## section`.

**Fourth operation — rules hygiene.** Void — no `RULES.md` or `rules/base.md` exists anywhere in this repo (confirmed by `find`). Record this in the report as void-with-reason, not silently skipped.

## Files & types

- edit (as needed): `~/projects/digital_ocean/CLAUDE.md` (gains only the destructive-op confirmation rule from the salvage); `~/projects/digital_ocean/AGENTS.md` (convert to a symlink — discard its 69-line content, no salvage); `~/projects/digital_ocean/.ai-factory/DESCRIPTION.md` (delete, after salvaging its six unique facts — five into the new `docs/` file, one into `CLAUDE.md`)
- create: a new `docs/` file holding the per-server hardware quintet (CPU, RAM, GPU, disk, OS version), structured to allow more than one server entry — this is the one place this alignment pass creates a `docs/` file rather than staying instruction-layer-only; name and exact structure are the implementing pass's call, grounded in the facts above
- edit (narrow carve-out only): `~/projects/digital_ocean/README.md` — solely the one "Workspace structure" line naming `.ai-factory/DESCRIPTION.md`, fixed or removed once that file is retired; nothing else in README (its Config-sync-rule overlap with `CLAUDE.md` is flagged, not an edit target)
- read-only: everything else in `~/projects/digital_ocean` (`configs/`, `scripts/` are ground truth for verification, never edit targets here; the rest of `docs/`, beyond the one new hardware-facts file above, is likewise read-only ground truth)

## Guards

- **Scope is otherwise the instruction layer** — `CLAUDE.md`, `AGENTS.md`, `DESCRIPTION.md`, and the one narrow README line named above; no edits to `configs/`, `scripts/`, or anything else under `.ai-factory/`. The one named exception: the DESCRIPTION.md hardware-facts salvage makes a new file under `docs/` a create/edit target for exactly that content — nothing else in `docs/` is touched.
- **Grounding over preference** — every kept, moved, or rewritten claim is verified against the actual configs (`configs/nginx/*.conf` for the vhost tables) or is a plain fact carried over from `DESCRIPTION.md` unchanged; no claim is invented or "improved" beyond what ground truth supports.
- **Preserve the file's language and register** — match what's there; this is alignment, not restyling.
- **Cross-repo anchoring** — the target is `~/projects/digital_ocean` by absolute path; nothing in the skills repo changes in this task.
- The read-first list above is a hard precondition — the experiment is void if the pass runs on chat-free context without those four sources loaded.

## Verification

- Spot-check: no meaning stated verbatim in two of `CLAUDE.md`'s own sections; the "Working with the Server" placeholder no longer contradicts "Server Connection."
- The implementation report lists every conflict found (the three-way Nginx-table drift at minimum), each with its ground-truth resolution or its escalation.
- `grep` the file for skill/command-name routing → zero; for history phrasing ("was replaced", "now uses instead") → zero.
- `AGENTS.md` is a symlink to `CLAUDE.md`; `DESCRIPTION.md` no longer exists; the one README line naming it is fixed; the new `docs/` file exists and holds the per-server hardware quintet (CPU, RAM, GPU, disk, OS version).
- The instruction-layer total (CLAUDE.md + the now-gone AGENTS.md/DESCRIPTION.md content) does not grow **vs the entry measurement** (the 131 in Current state is stratigraphy, not the baseline) — `CLAUDE.md` itself grows only by the one destructive-op confirmation sentence; the bulk of the DESCRIPTION.md salvage lands in the new `docs/` file, outside the instruction-layer count; the whole-layer net must not grow.
- The grove entry checks and the rules-hygiene operation are both recorded in the report as void-with-reason, not silently skipped.
- After editing the file's body, its header/intro/summary lines are re-scanned for now-superseded claims — same-file self-contradiction is the cheapest drift to create and the hardest for its author to see.

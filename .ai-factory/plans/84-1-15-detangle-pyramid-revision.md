# Plan: detangle — pyramid revision

## Context
Reconcile `src/skills/detangle/SKILL.md` (125 lines) with `docs/context-tree.md` and the global "Grounding claims" rule into one model: detangle climbs from a leaf up through branch and trunk to the forest; the context-tree doc raises from the session input down to the leaf — the same motion, two ends. Where detangle restates what the global rule now owns, slim it — pointing at global § "Grounding claims" by name, never at a repo-doc path. "No change" plus a one-paragraph audit report is a complete, legal outcome.

**Shipped-skill constraint (from plan review, finding 1).** `detangle` is a generic skill exposed to every project via `~/.claude/skills → active/skills`; it runs inside foreign project roots where `docs/context-tree.md` and `docs/skill-pyramid.md` **do not exist**. A markdown link to those paths is walkable only inside this repo and a dead 404 everywhere else — the opposite of the "рёбра, по которым ходят" doctrine. The two revised siblings of this genre (`temporal-tree` 1.13, `roadmap-decompose-skeleton` 1.14) carry **no** repo-doc link. Therefore: the repo docs are **audit standards Task 1 reads**, never a link that lands in the shipped body. The only safe, always-available owner to point at is the global CLAUDE.md § "Grounding claims" — loaded into every session of every project, and referenced **by name** (as `docs/context-tree.md` itself references it), never by path. Where two-entry-maps / roadmap-seam material is a genuine restatement, prefer **slimming it in place** over emitting any link.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Audit

- [x] **Task 1: Audit the skill against the context tree, the global grounding rule, and the pyramid; write the report**
  Files: `src/skills/detangle/SKILL.md` (read-only in this task); read as standards: `docs/context-tree.md`, `docs/skill-pyramid.md`, `docs/skill-composition-model.md`, and `src/global/CLAUDE.md` § "Grounding claims"
  Read the body in full against four lenses:
  - **Restated shared ownership → slim in place.** The global grounding rule (and, as a read-only standard, `docs/context-tree.md`) now owns: the two entry maps (`ARCHITECTURE.md` = space, `ROADMAP.md` = time) and the roadmap `[x]`/`[ ]` seam; that held context decays and the leaf must be re-read fresh; that the chain must reach code, never stop at a doc; depth walked at the moment of action. Judge whether detangle's "Before you start — load project context" (lines 28–37) restates the two-entry-maps / roadmap-seam contract. The owner to point at (if any pointer is warranted) is **global § "Grounding claims", referenced by name** — never a `docs/…` path, which dangles in the foreign roots detangle ships into (see Context). Because the global rule is always loaded, the default fix for a genuine restatement is to **slim in place**, not to emit a link.
  - **Caution on the depth block.** "Depth rules" / "What NOT to do" (lines 113–126) skews toward detangle's **own** executor-facing climbing discipline, not the grounding rule: line 117 ("read all consumers") is protected forest content, line 118 ("if you cannot name the trunk-level invariant, you have not climbed high enough") is detangle's own climb test, and line 116 ("go as deep as the flow requires — not as deep as is easy") is a nuance the global rule **deliberately dropped** ("however much it takes" was cut in milestone 1.1 / spec 22). Detangle has no decay clause. Default this block to **protection**; flag a line here only on a clear one-to-one restatement, never on family resemblance.
  - **Detangle's own contribution — protected, never a link.** The fractal model (leaf/branch/trunk/forest, lines 14–24), the leaf→trunk climb (Step 2, lines 47–66), and above all the **cross-project forest raise / multi-tree shared-contract read** (Step 3, lines 68–80, and the depth rule "read all consumers", line 117) are detangle's own content. The spec Guard is explicit: the multi-tree shared-contract raise is **never reduced to a doc link**. These stay.
  - **Procedural ceremony** (`docs/skill-composition-model.md`) — flag narration the executor performs unprompted and obvious step-sequencing padding; distinguish it from pinned contract (the synthesis output block / ASCII-tree + context-map format, lines 84–103, and the explain-vs-act intent split, lines 105–108 — these are detangle's deliverable contract and stay verbatim).
  - **Two-reader register** — verify each line addresses the right reader (executor imperatives vs editor-facing knowledge); flag misaddressed lines.
  Produce a one-paragraph audit report naming **each finding with its concrete fix** (slim-in-place, name-referenced pointer to global § "Grounding claims", or cut), or stating conformance. This report is the task's primary deliverable and gates Task 2. If a restatement is found, the fix keeps only detangle's angle on it (climbing, not the map itself) and never lands a `docs/…` path in the body.

### Phase 2: Apply findings (only if the audit finds any)

- [x] **Task 2: Apply only the audit-confirmed fixes** (depends on Task 1)
  Files: `src/skills/detangle/SKILL.md`
  Apply **only** what Task 1's report names — restated shared ownership is slimmed in place (or, where a pointer is warranted, name-references global § "Grounding claims"), ceremony is cut, misaddressed lines are re-registered. Skip this task entirely if the audit reported conformance.
  Guards (from the spec's Guards + plan review):
  - Behavior-identical whatever the outcome; **frontmatter unchanged** (name, description, argument-hint — no `loads:`/`allowed-tools` present, none added).
  - **No `docs/…` path link in the shipped body.** detangle runs in foreign roots where the repo docs do not exist; any pointer references global § "Grounding claims" **by name**, and slimming-in-place is preferred over pointing.
  - **Imperative-safety condition.** Lines 28–37 are executor **imperatives** ("if `ARCHITECTURE.md` exists — read it"); an imperative executes, a link does not. A restated imperative may be delinked/slimmed **only** if its owner (the always-loaded global rule) already issues the same executor command to raise both maps at entry — which it does. If that command were absent, slim without removing the imperative; do not convert a live command into an inert pointer.
  - The multi-tree shared-contract raise (Step 3 forest detection + "read all consumers") and the leaf→trunk climb are **never reduced to a doc link** — they stay as detangle's own content.
  - Pinned contract stays byte-identical — the synthesis context-map / ASCII-tree format and the explain-vs-act intent split.
  - A revision only removes / relinks / re-registers; do not add or expand content, and do not invent a `references/` split (the file is 125 lines and has no subfolders).

- [x] **Task 3: Live baseline verification (only if the body changed)** (depends on Task 2)
  Files: none (verification only)
  If and only if Task 2 changed the body, confirm behavior is identical: run detangle once on a real shared-contract element pre/post and compare the raised context set — per the spec, the forest-level multi-tree raise must produce the same set of consuming trees. This repo has no proto/shared-DTO contract to exercise a true cross-project raise; use the nearest in-repo shared-contract analogue — an engine skill consumed by multiple callers (e.g. `note`, reached via `grep -l "note" src/skills/*/SKILL.md src/commands/*.md`) — and confirm the pre/post runs surface the same caller set and the same leaf→trunk→forest map shape. If Task 2 was skipped (conformance), no baseline is needed.

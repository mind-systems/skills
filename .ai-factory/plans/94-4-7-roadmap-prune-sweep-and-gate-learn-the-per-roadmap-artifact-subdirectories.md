# Plan: 4.7 — roadmap-prune: sweep and gate learn the per-roadmap artifact subdirectories

## Context
Teach `roadmap-prune`'s artifact sweep (Step 5) and deferred-observations gate scan (Step 0) the per-roadmap subdirectory layout that 4.6 landed in `orchestrator-artifacts` §1: the default pair keeps flat behavior byte-stable, a named roadmap sweeps only its own stem's subdirectories, `patches/` leaves the sweep list, and the gate scan covers nested `.md` files repo-wide.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Per-roadmap sweep and gate

- [x] **Task 1: Scope Step 5's artifact sweep to the pruned roadmap and drop `patches/`**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In `## Step 5 — Sweep completed artifacts and specs`, rewrite item 2 (currently `rm -rf` of the four flat dirs `plans/`, `plan-reviews/`, `reviews/`, `patches/`). New behavior, per spec `.ai-factory/specs/49-prune-sweep-per-roadmap-subdirs.md` and the layout owned by `orchestrator-artifacts` §1 (do not restate the layout in detail — the `loads:` edge already exists):
  - Determine whether the target roadmap is the **default pair** or a **named roadmap** from the skill argument path already anchored in this step: a roadmap at `.ai-factory/ROADMAP.md` or `.ai-factory/ROADMAP_TESTS.md` is the default pair; a roadmap under `.ai-factory/roadmaps/…` is named.
  - **Stem derivation (a named roadmap and its `-tests` partner share one stem).** For a named main roadmap `roadmaps/<name>.md`, `<stem>` = `<name>`. For a named **test** roadmap `roadmaps/<name>-tests.md`, `<stem>` is also `<name>` (strip the `-tests` suffix) — **not** the raw basename `<name>-tests`. This mirrors the layout owner: `orchestrator-artifacts` §1 keys all four dirs (`plans/`, `plan-reviews/`, `reviews/`, `test-runs/`) to a **single** stem segment per roadmap pair (`roadmaps/kg-wmservice.md` → `plans/kg-wmservice/…`, and the test partner's runs go to `test-runs/kg-wmservice/`, not `…-tests/`). Prune must delete exactly the segment the orchestrator wrote, so the `-tests` partner resolves to the main partner's stem — the symmetric named-side rule to the default pair's shared flat dirs. Pin this explicitly; the implementer must not derive the stem from the raw basename.
  - **Default pair** → `rm -rf` the three flat dirs directly under `<target repo root>/.ai-factory/`: `plans/`, `plan-reviews/`, `reviews/` — exactly today's dirs minus `patches/`, byte-stable for a solo repo.
  - **Named roadmap** → `rm -rf` only that stem's subdirectories: `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` — never the flat dirs, and never a sibling stem's subdirectories (another developer's completed artifacts are not this prune's to delete).
  - Remove `patches/` from the sweep list entirely — the dir is retired (4.6).
  - Update the `ROADMAP_TESTS.md` / tests-mode sentence (currently "`test-runs/` joins the swept dirs in that mode only"). **Keep the tests-mode gate explicit and unchanged in meaning:** `test-runs/` is swept **only when the pruned target is the test roadmap** (`ROADMAP_TESTS.md` for the default pair, `roadmaps/<name>-tests.md` for a named pair) — a main-roadmap prune (`ROADMAP.md` or `roadmaps/<name>.md`) never touches `test-runs/`. The stem change is **path resolution only**, not a change to which prune triggers the sweep: in that tests mode, the swept dir is flat `test-runs/` for the default pair and `test-runs/<stem>/` for a named test roadmap, where `<stem>` is the same `-tests`-stripped `<name>` derived above (so the subdir is unambiguously `test-runs/<name>/`). Do not broaden the sweep to the main-roadmap prune.
  Leave item 1 (spec-tag capture) and item 3 (`rm -f` captured spec paths — subdir-agnostic; `Spec:` tags carry exact paths) unchanged, and keep the target-repo-root anchoring rule intact.

- [x] **Task 2: Make Step 0's gate scan cover nested `.md` at any depth, repo-wide** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In `## Step 0 — Deferred-observations gate`, update item 2 so the scan of `<target repo root>/.ai-factory/plan-reviews/` and `.../reviews/` explicitly includes files nested in subdirectories — "every `.md` file under … at any depth", not just the flat top level. State that the gate stays **repo-wide** by design: prune is an integration-branch act, so any developer's unpinned observation blocks it regardless of author (do not scope the gate scan to the pruned roadmap's stem). Keep the pinned-definition citation to the engine, the stop/refuse flow, and the resolution steps unchanged. Update the `ROADMAP_TESTS.md` parity sentence at the end of Step 0 so it still reads correctly against the nested scan (the gate scans the shared `plan-reviews/`/`reviews/` trees identically in both modes; `test-runs/` still carries no review sections and is not scanned).

  **Item 6 (margin capture) — scope it to what Step 5 will actually sweep, not repo-wide (review finding #2, decided).** The item-2 gate is repo-wide, but item 6 exists only to salvage margins "before Step 5 deletes the file". Since Step 5 in a named prune now deletes only the pruned stem's subtree, capturing sibling stems' margins would make Step 8 echo "possible unharvested margins" for files that still exist and belong to another developer. So: item 6 also applies the "at any depth" nesting fix, but its capture is limited to the files Step 5 will delete — the flat `plan-reviews/`/`reviews/` files in the default-pair case, the pruned stem's `plan-reviews/<stem>/` and `reviews/<stem>/` files in the named case. Add one sentence making this scope divergence explicit (gate scan repo-wide; margin capture follows the sweep scope) so the implementer neither leaves item 6 repo-wide nor "fixes" the gate scope to match.

  **Reconcile the two "Step 5 deletes these files" clauses that feed item 6 (review-2 finding #1).** The premise that the scanned files get deleted by Step 5 appears in two spots that become false for a repo-wide scan in a named prune — bring both in line with the new sweep-scoped capture so the hand-off and the capture agree:
  - **Item 2's hand-off clause** — currently "A file with no such section contributes nothing to this step — but capture it for step 6 below before moving on, since Step 5 deletes these files…": qualify the hand-off so only files within the Step-5 sweep scope are handed to item 6 (repo-wide files outside the pruned stem are scanned for the gate but not handed off for margin capture).
  - **Item 6's own rationale** — currently "Capture the matching paragraph(s) … now, before Step 5 deletes the file": restate so the "before Step 5 deletes the file" premise holds only for the swept-scope files it now captures.
  Both edits are instructions only (no rationale prose beyond the one divergence sentence), consistent with the skill's mandate.

- [x] **Task 3: Align Step 8 report wording and any residual flat-dir references** (depends on Task 1, Task 2)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In `## Step 8 — Summary report`, ensure "List the dirs swept in Step 5" reads correctly for both branches (flat dirs vs. the named roadmap's stem subdirectories) without restating the layout. **Reconcile the third "Step 5 deletes" premise (review-3 finding #1)** — Step 8's parenthetical *"Do not re-scan `plan-reviews/`/`reviews/` here — Step 5 already deleted them"* (file line 327): the instruction itself stands (after Task 2's scoping, the item-6 captured set equals the swept set, so everything Step 8 echoes was in fact deleted), but restate the justification to name the swept scope instead of the blanket dirs — e.g. "Step 5 already deleted the swept files". A `grep -n "Step 5 delet\|deleted them\|before Step 5"` after all edits must show every remaining premise consistent with the scoped sweep — three sites total (lines 43, 67, 327), none left blanket. Grep the whole file for `patches` and confirm zero remaining hits; grep for any other lingering flat-only assumption in prose (e.g. `## What NOT to do`, the Step-5 preamble) and reconcile it with the per-roadmap sweep. Do not touch 3.1's landed ledger text (versioned Features header, self-heal, drop-history semantics) or 4.4's two integration-branch policy sentences — instructions only, no rationale prose, commit policy untouched.

## Verification (per spec)
- `grep -n "patches" src/skills/roadmap-prune/SKILL.md` → zero hits.
- Dry-read both Step 5 branches: default prune → flat three-dir sweep; named prune → only `<stem>/` subdirs named, sibling stems explicitly excluded.
- Dry-read the `-tests` case: pruning `roadmaps/<name>-tests.md` resolves `<stem>` to `<name>` (suffix stripped) and sweeps `test-runs/<name>/` — the segment the orchestrator wrote — not a `…-tests/` subdir.
- Step 0 gate scan reads "at any depth" and stays repo-wide; item 6 margin capture reads "at any depth" but is scoped to the Step-5 sweep set.

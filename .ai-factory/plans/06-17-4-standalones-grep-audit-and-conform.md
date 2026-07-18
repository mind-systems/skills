# Plan: 17.4 — Standalones: grep-audit and conform

## Context

The last conformance pass of Phase 17: the skills that sit outside the three couplings (`detangle`, `temporal-tree`, `aif`, `aif-architecture`, `observe-logs`, `command-handoff`, `command-commit-roadmap-update`). Naming-only conformance to the governing spec [reserved-words](../../docs/reserved-words.md).

**This is an audit, not a rewrite.** The expected total diff is **one line in one file** — `roadmap milestone` → `task` in `detangle:33`. Every other file in scope is certified clean and edited not at all. Per the spec's own guard, *"the audit certifies, it does not manufacture work"*: a task that produces one changed line and six unchanged files has succeeded, not underperformed. Resist the pull to find something to do in the six clean files — a discretionary "improvement" there is out of scope and is a review finding.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Context notes — read before editing

**The spec's line numbers are from a 2026-07-13 grep; the grep governs.** Re-derived against the working tree while planning this file, the spec's inventory holds exactly:

- `rg -U -in '[^-]milestones?' src/skills/detangle/SKILL.md` → **one hit, line 33**, matching the spec.
- `rg -U -in 'spec\s+notes?|[^-]milestones?'` over the other six files → **zero hits** (exit 1). The six are clean as certified.

Re-derive both before editing anyway — held context decays, and this plan is a description of the files, not the files.

**`detangle` has no `loads:` field.** Its frontmatter is `name` / `description` / `argument-hint` only (verified in place). The task's `loads:`-byte-stability guard is therefore vacuously satisfied here — there is no edge to preserve and nothing to hunt for. The guard still binds `temporal-tree`, which keeps `loads: roadmap-engine` untouched because that file is not edited at all.

**`aif-skill-generator` is out of scope — do not open it to "check".** `active/skills/aif-skill-generator` symlinks into `upstream/ai-factory/`, the pristine mirror that makes the sync conflict-free. Editing it breaks that split. It is excluded by the spec, not merely clean.

**`src/commands/command-pin-gaps.md` is not in this task.** It belongs to 17.2 and has already landed. The command half of this task is exactly two files: `command-handoff.md` and `command-commit-roadmap-update.md`.

**Byte-frozen throughout:** every `loads:` line, `name:`, `description:`, `argument-hint`, `allowed-tools`, the `` Spec: `` and `Governing spec:` tags, the `.ai-factory/specs/` path, and every protocol literal. None of these sit on the one line this task edits; the freeze is stated so a wandering edit is recognized as one.

## Tasks

### Phase 1: The one edit

- [x] **Task 1: `detangle` — `roadmap milestone` → `task` (line 33)**
  Files: `src/skills/detangle/SKILL.md`
  Re-derive the site by grep, then make the single substitution. The sentence currently reads:

  > is the element you're looking at part of an
  > in-progress or planned roadmap milestone? That changes the impact analysis in Step 4.

  and becomes:

  > is the element you're looking at part of an
  > in-progress or planned task? That changes the impact analysis in Step 4.

  **The whole two-word phrase collapses to `task`** — not "roadmap task". The qualifier does no work here: the enclosing paragraph names `.ai-factory/ROADMAP.md` at line 30, three lines above the edit site, so the roadmap context is already established, and [reserved-words](../../docs/reserved-words.md) takes a qualifier only where it disambiguates. `task` is also the correct registry word rather than `phase` — the unit whose in-progress/planned state changes an impact analysis is the `N.M` entry.

  Nothing else on the line or in the paragraph changes; preserve the existing line wrapping.

  **Expected no-change sites in this same file — certify, do not edit.** Both are listed with their reason so certification does not depend on rediscovering it:
  - `field` at ~15 ("a field — exists at a specific level of the tree") — a generic code element, not the skill description field.
  - `field` at ~42 ("file, function, class, field, endpoint") — same, inside a list of code elements.

### Phase 2: The certifications

- [x] **Task 2: Certify the six audit-clean files — read-only** (independent of Task 1)
  Files: none (read-only)
  Run the certification grep and confirm zero hits across all six:
  ```
  rg -U -in 'spec\s+notes?|milestones?' \
    src/skills/{temporal-tree,aif,aif-architecture,observe-logs}/SKILL.md \
    src/commands/{command-handoff,command-commit-roadmap-update}.md
  ```
  Zero hits (rg exits 1) is the pass. **Make no edits in these files** — the outcome of this task is a certification, and its deliverable is the confirmed-zero result recorded in the commit rationale.

  **Two deliberate strengthenings of the spec's gate expression**, both recorded rather than silently applied:
  - The spec writes `[^-]milestones?`; this plan uses the **bare** form. The `[^-]` anchor cannot match a line-initial occurrence, so a synonym wrapped to the start of a line hides from it — exactly the blind spot task 17.3 hit twice in its own files. The bare form is strictly stronger and, on files expected to return zero, costs nothing.
  - Add a hyphenated pass the `\s`-based expression is structurally blind to:
    ```
    rg -in 'spec-note' src/skills/{temporal-tree,aif,aif-architecture,observe-logs}/SKILL.md \
      src/commands/{command-handoff,command-commit-roadmap-update}.md
    ```
    → zero. Same lesson from 17.3, where the attributive `spec-note` survived the primary grep.

  If any hit appears in these six files, **stop and report rather than improvising an edit** — the spec certifies them clean, so a hit means the inventory is wrong and the spec needs amending before the file is touched.

  Leave untouched and expect to see: `temporal-tree`'s `named roadmap` (~73, 87, 89) and attributive `named-roadmap resolution` (~24, 71) — ordinary English under the plain-form contract, explicitly re-audited to no change; `observe-logs`'s generic "fields" (~24); `command-handoff`'s generic "field" (~81); `temporal-tree`'s `loads: roadmap-engine`.

### Phase 3: Verification

- [x] **Task 3: Run the spec's verification gates** (depends on Tasks 1–2)
  Files: none (read-only)
  From the repo root, expect the stated result on each:
  - `rg -U -in 'milestones?' src/skills/detangle/SKILL.md` → **zero**. (Bare form, per the strengthening in Task 2.)
  - The two Task 2 certification greps → zero, re-run post-edit to confirm the edit did not stray outside `detangle`.
  - `git status --short -- src/ active/ upstream/` → **exactly one line**, `M src/skills/detangle/SKILL.md`. This is the gate that catches both a stray edit in a certified-clean file and any touch of the excluded `aif-skill-generator`. **The path scope is load-bearing, not cosmetic:** an unscoped `git status` also lists the pipeline's own untracked artifacts for this task (this plan, its `.json`, the plan-review, the review, the sidecar), which are expected and none of the implementer's doing. Scoping to the three source trees keeps the gate true at run time, so an unexpected line is unambiguously a stray edit rather than pipeline bookkeeping to be waved through.
  - `git diff --stat` → `1 file changed, 1 insertion(+), 1 deletion(-)`. A larger diff means an edit was manufactured somewhere; reconcile before proceeding.
  - `git diff` filtered to `loads:`, `name:`, `description:`, `argument-hint`, `allowed-tools` lines → empty.

- [x] **Task 4: Behavior baseline check — read the diff** (depends on Task 3)
  Files: none (read-only)

  **Recorded deviation from the spec's implied live check, on the same grounds 17.3 recorded.** No pre-conformance baseline of a `/detangle` run exists to diff against, and `detangle` produces free-form analytical prose whose output is not byte-comparable between runs even on identical input — a live run would yield an unanchored smoke test, not a baseline comparison. The static read below is the stronger feasible check for a one-line prose substitution.

  Read the one-line diff and confirm it is a noun substitution inside prose: no changed control flow, no changed grep needle, no changed scanned literal, no changed step reference. Specifically confirm the trailing clause still reads "That changes the impact analysis in **Step 4**" — the step pointer is a live internal reference and must survive the edit intact. Then read the surrounding "Before you start — load project context" section in full and confirm it still reads coherently: one name for the roadmap unit, no leftover synonym, and the sentence's instruction to re-read the entry map unchanged.

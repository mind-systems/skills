# Code Review — 1.8.3 roadmap-prune: pyramid pass (review 1)

**Change under review:** `src/skills/roadmap-prune/SKILL.md` — the milestone's only code file (a skill instruction file). Reviewed the full `git diff HEAD`, read the rewritten file in full (302 lines, was 330), and cross-checked every removed hunk against the plan's verbatim-protected inventory (Task 1, items 1–10) and spec 28's behavior-identical guard.

**Also present in the staged tree (out of scope for 1.8.3's file boundary, checked for coherence only):** `ROADMAP.md` (+task 1.17, "315"→"330" and closure-rule note on line 171), `specs/28`, `specs/29` (closure-rule additions), new `specs/42-skill-tool-grant-alignment.md`, and specs 30–32. These are planning artifacts from the resolution session that routed the plan-reviews' recurring deferred observation (`allowed-tools` omits `Skill`) into a new open task 1.17 with governing spec 42 — the correct disposal per the deferred-observations gate. They are internally consistent and touch no code. Nothing broken.

## What the change does

A compression pass: removes narration, rationale glosses, and one restated-protocol fragment. No procedure, gate, sweep, anchor, or commit contract is altered.

## Behavior-identity audit (the spec's central guard)

Every removed hunk classified; all are narration / rationale / restated-protocol, never a contract sentence:

1. **Opening blurb** (old 16–20, "Cleans up a roadmap… GPS-accurate…") — pure narration. Cut.
2. **Step 0.3** — removed the inline `(- Affects: <target> — <observation>)` entry-line example. This is the `## Deferred observations` entry-line *format*, which `orchestrator-artifacts` owns and Step 0's preamble (line 20–22) explicitly defers to the loaded engine for. Authorized "link, never restate" cut; the unpinned-entry *test* ("pinned = ≥1 bracketed status marker") is preserved verbatim, and the refusal message still names `Affects:` (line 39). Behavior-preserving.
3. **Step 2.1** — removed "The Features table is the answer to 'what does this system know how to do?'…" — rationale gloss the plan flagged cuttable. The discriminator question, the New/Extended/Internal outcome table, and all four classification rules ("never copy a phase or section header," "internal-only never gets a named row," etc.) are byte-identical.
4. **Step 2.2** — removed "The name becomes a row in ARCHITECTURE.md — meaningful enough to navigate…" — gloss. The 2–5-word operator-perspective naming rule and the domain-grouping/section-header rules survive.
5. **Step 3** — removed "That commit is the GPS coordinate…" — gloss. The rule ("find the commit where its last task was closed") and the decisive "Pick the commit where the **last task of the feature** was marked `[x]`" are intact.
6. **Step 4.1** — removed "Anyone can run `git show <hash>:…` to restore the full picture." — usage narration. The `git rev-parse --short HEAD` capture and its meaning are intact.
7. **Step 6** — removed "Their history lives in ARCHITECTURE.md." and compressed the retain-last-phase-header rationale to "always retain the last phase header, even when it is emptied of all its tasks." The rule is preserved; the emptied-phase / emptied-direction sweeps and the **never renumber** clauses are byte-identical.
8. **"Reading the history later" section** (old 312–331) — removed wholesale. Pure how-to/rationale, flagged cuttable in the plan. No other file or step in the skill references it (grep-checked within the file); it is not load-bearing.

## Protected contracts — confirmed byte-identical

- **Step 0 gate:** the three-part 1.8.1 refusal chain (`/command-handoff` → dedicated resolution session → `[fixed]`/`[routed → <path>]`/`[dismissed]` → re-run when pinned, "never manufactured"), the "make no edits, no sweep, no partial prune" line, the Step 0.6 pre-standardization marker-phrase capture, and the `ROADMAP_TESTS.md` parity sentence — all present and unchanged (lines 34–59).
- **Step 5 sweep:** scoped `Spec:`-tag capture, "no `Spec:` tag… skip it, never synthesize a path," the four-dir `rm -rf` set (`plans/`, `plan-reviews/`, `reviews/`, `patches/`), `rm -f` per captured spec, the no-scan invariant, target-repo-root anchoring, `test-runs/` addition — all intact (lines 203–220).
- **Step 4.2 `## Features` anchor**, the example table, **Step 8 echo contract** ("possible unharvested margins," report-only/never-gates, omit-if-empty), **commit policy** (`git add -A` scoped, one commit, exactly `Roadmap prune`), and the **What NOT to do** list (plain `rm` not `git rm`; no spec-dir scan; no `handoffs/` touch) — all byte-identical.
- **Frontmatter:** `name`, `description`, `argument-hint`, `allowed-tools`, `loads: orchestrator-artifacts` unchanged. (The known `allowed-tools`-lacks-`Skill` gap is deliberately untouched here — it is task 1.17's territory, correctly deferred.)

## Runtime / correctness / security

- No executable runtime surface changed. The destructive sweep commands (`rm -rf`, `rm -f`, `git add -A`) are byte-identical to HEAD — no new deletion path, no widened scope, no `git rm` introduced.
- Markdown structure remains valid; the H1 now sits directly above a `---` rule (the intro was between them) — cosmetically bare but harmless, no rendering or parsing issue.
- No missing migration, type, race, or dependency concern applies to a skill instruction file.

## Conclusion

Behavior-identical compression. Every protected contract survives verbatim; every removed hunk is narration, rationale, or engine-owned protocol legitimately delegated to the load pointer. Frontmatter and `loads:` unchanged. No bugs, no security issues, no correctness problems.

REVIEW_PASS

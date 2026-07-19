# Review 1: 17.3 — The "roadmap cleanup" coupling: one dictionary in test-coverage, prune, and the rescue pair

## Code Review Summary

**Files Reviewed:** `git diff HEAD` in full (9 files) + all four target `SKILL.md` files read in full + spec 72 + contract line + `roadmap-engine` + cross-repo sweep of `orchestrator/`
**Risk Level:** 🟢 Low
**Verdict:** Correct. All eight verification gates pass with the exact expected values. No correctness, security, or behavior defect found.

## What changed

Four skill bodies conformed to the reserved-words vocabulary (`milestone`→`task`, `spec note`→`task spec`), plus a ground-truth sync of one cross-repo citation. Two planning artifacts (spec 72, contract line 17.3) amended to record the ratified carve-outs.

Line counts are **identical pre/post in all four files** (382/436/476/221) — every edit is an in-place substitution, no structural change. `git diff --check` is clean.

## Verification gates — all pass

Run from `src/skills/`:

| Gate | Expected | Actual |
|---|---|---|
| `rg -U -in 'spec\s+notes?'` ×4 | zero | **zero** ✓ |
| `rg -in 'spec-note'` ×4 | zero | **zero** ✓ |
| `rg -U -in 'milestones?'` ×4 | exactly 3 | **exactly 3** — prune 75, prune 326, task-rescue 10 ✓ |
| `rg -in 'roadmap lines?'` prune | exactly 1 | **exactly 1** — line 155 ✓ |
| `rg -n 'task line\|task-line'` rescue pair | zero | **zero** ✓ |
| `grep -n 'Silent-Failure'` test-coverage | heading only | **only line 64** (Layer-3 `##` heading) ✓ |
| `grep -c '## Deferred observations'` | prune 3 / audit 1 | **3 / 1** ✓ |
| frontmatter diff (`name:`/`loads:`/`allowed-tools:`/`argument-hint:`) | empty | **empty** ✓ |

## Carve-outs — all three honored

Each was the failure mode this task most risked; all three survived correctly.

- **§1 `roadmap-prune:75`** — the Step-4.6 pre-standardization marker-phrase list is byte-identical; `out of scope for this milestone` intact. The grep needle over target projects' historical review files still matches its corpus.
- **§3 `roadmap-prune:325–326`** — dual form applied as specified: ``a flat `## Tasks` (or legacy `## Milestones`) list``. Read Step 6 in full: the legacy literal survives, the registry name leads, and nothing downstream in Step 6 (emptied-phase sweep, emptied-direction sweep) depends on the heading name, so the change is contained. Behavior is additive — no roadmap prune recognized before is lost.
- **§4 `task-rescue:10`** — the quoted trigger phrase `"rescue", "milestone failed", "pipeline stopped"` is verbatim, while the surrounding description prose at line 8 conforms (`checks downstream tasks`). The boundary landed exactly at the quotation marks, as the plan drew it.

## Correctness checks beyond the gates

- **§2 cross-repo sync verified against ground truth.** `task-rescue:356–357` now reads `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py`. Confirmed in the orchestrator repo: `resume.py:11` and `resume.py:169`; `main.py` holds neither. Both halves synced — no verified identifier left beside a stale path.
- **`milestone line` → `contract line`, not `task line`.** Both sites correct: `:65` "contract-line locate" (attributive hyphen preserved), `:189` "locate the contract line matching the slug". The `task line|task-line` gate confirms no third synonym was minted. This was the plan's highest-value catch and it survived implementation.
- **No `milestone`→`phase` mistranslation.** Spot-checked the sites where the two tiers sit adjacent: `task-rescue:60–63` reads "locate the phase section the task belongs to … If the task is under no phase" — the unit and its container stay correctly distinguished.
- **`task-rescue:448`** ("Do not add implementation details to the task or task spec") is correct rather than a missed contract-line site: per the registry, **task** *is* the `N.M` entry, so the pairing with "task spec" names the two tiers accurately.
- **No cross-file breakage.** Swept `src/`, `docs/`, `CLAUDE.md` for the renamed H1s (`# Milestone Rescue`, `# Milestone Rescue Audit`) and the renamed Step-5.5 heading — zero external references. Swept the **orchestrator repo** for `Milestone Rescue|open milestones|milestone slug|milestone-rescue` outside its frozen `.ai-factory/` — zero hits, so no cross-repo scan depends on any string this task changed.
- **Protocol literals untouched.** `## Deferred observations` counts unchanged; no `- Affects:` line exists in these four files to disturb; PASS literals not in any diff hunk.

## Nits (non-blocking, not findings)

1. **`roadmap-prune:326` breaks the paragraph's hard wrap.** The inserted text left the line at 113 chars where the surrounding Step-6 paragraph wraps at ~86 (325 is 86, 327 is 87, 330 is 83). Cosmetic only — markdown renders identically and no gate is affected — but re-wrapping the two lines would keep the file's local style consistent. The other long lines in this file (128–153) are list/table rows, not wrapped prose, so this one is a genuine local outlier.

2. **Contract line 17.3 grew 876 → 1107 chars**, against `roadmap-engine`'s "~600-char contract line" norm. Not an outlier *in practice* — sibling 17.1 is 1120 and 17.2 is 834 — so this is in-family rather than newly introduced drift, and the added text (external-corpus rule, `milestone line`→`contract line`) is load-bearing for anyone reading the line cold. Noted only so the phase's collective drift from the engine's norm is visible.

## Positive notes

- **The spec and contract line were reconciled with the ratified decisions rather than left contradicting them.** Spec 72 originally instructed "`milestone` (75) → `task`" — the instruction the plan correctly overruled as a behavior regression. Leaving that text in place would have left a live landmine for a future re-run or reader; amending it is the right call and matches the global discipline that a governing spec disagreeing with reality is a defect to reconcile. The spec's Verification section was updated in step (now expecting three `milestone` hits, with the two new gates added), so the artifact is internally consistent.
- Worth noting the amendment sits slightly outside the spec's own § "Files & types" ("The four `SKILL.md` files") — correct in substance, and flagged only so the scope statement's narrowness is not read as having been violated carelessly.
- **The external-corpus rule was generalized into the spec's Guards** rather than left as three ad-hoc exceptions, so the next conformance task (17.4) inherits the reasoning instead of rediscovering it.
- **Every edit is a pure substitution** — identical line counts, no whitespace damage, no structural drift in any of the four files.

## Deferred observations

- Affects: 17.4 (`.ai-factory/specs/65-standalone-skills-conformance.md`) — residual `milestone` hits remain elsewhere in `src/skills/`: `detangle` (1), `roadmap-outline` (1, 17.2's deliberate user-input exemption), `aif-docs` (2). All owned by landed or planned tasks; nothing unowned. Noted so 17.4 reconciles against the current count rather than the spec's historical one. [dismissed — verified live: detangle's hit is 17.4's own landed scope, roadmap-outline's is the exempt user-trigger word, aif-docs's two hits sit inside its own banned-motivation-word example list (SKILL.md:26,182) illustrating a retired word, not naming an artifact — already conformant]
- Affects: `roadmap-prune` (`.ai-factory/specs/72-cleanup-coupling-one-dictionary.md`) — the spec's live-verification item ("a `roadmap-prune` pass and a `/task-rescue` diagnosis run produce the same artifact shapes as their pre-conformance baselines") was deliberately substituted by static gates plus a full post-edit read, recorded in the plan's Task 6 with its grounds (no pre-conformance baseline exists to diff against; prune is destructive against a real target project). No action — recorded so a later reader sees the substitution was judged, not lost. [dismissed — the deviation was already judged correct by this same review; no action requested]

REVIEW_PASS

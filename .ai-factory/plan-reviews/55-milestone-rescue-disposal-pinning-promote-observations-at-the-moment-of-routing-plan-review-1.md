## Code Review Summary

**Files Reviewed:** 1 plan (targets `orchestrator-artifacts/SKILL.md`, `milestone-rescue/SKILL.md`; guards over `milestone-rescue-audit/SKILL.md`, `roadmap-prune/SKILL.md`)
**Risk Level:** 🟡 Low–Medium

Reviewed against spec `.ai-factory/specs/09-rescue-disposal-pinning.md`, ROADMAP.md line 121 (the milestone contract), and the four target/guard skill files in full.

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy")** — PASS. The plan keeps the marker grammar in the engine (`orchestrator-artifacts`) and has `milestone-rescue` *cite* it (§6) rather than redefine it. This is exactly the engine/philosophy split the architecture mandates: mechanism stays in the load-once engine, the caller holds policy and cites the mechanism. Task 2 explicitly forbids redefining the grammar/pinned/dedup in the caller — correct.
- **Rules (`.ai-factory/RULES.md`)** — WARN (non-blocking): file present but empty; no explicit conventions to check against.
- **Roadmap linkage** — PASS. The plan heading matches ROADMAP.md:121 (`- [ ] milestone-rescue: disposal-pinning — promote observations at the moment of routing`), the contract line names `Spec: .ai-factory/specs/09-rescue-disposal-pinning.md`, and that spec exists and matches the plan's two-file, one-contract change. No governing-spec reference on the phase; no further tree to follow.
- **Writer-set drift check** — PASS. `grep` confirms the sole-writer claim exists at exactly **one** site (`orchestrator-artifacts/SKILL.md:63`). No other skill duplicates the "written by `milestone-rescue-audit` only" assertion, so the single-sentence edit cannot leave a stale duplicate. The audit body's `## Write contract` scopes "the only writes *either one* ever performs" to itself (audit's own writes), not to a global marker monopoly — so Task 3's expectation that `git diff milestone-rescue-audit` and `roadmap-prune` stay empty holds.

### Critical Issues

None. The plan is faithful to the spec, the line anchors resolve, the ≤500-line guard is satisfied (446 today + ~12 lines ≈ 458), and `allowed-tools` already grants `Edit`.

### Issues

**1. Step 5.6 pins "across that milestone's review files" — but Step 5 has already deleted some of those files at real-defect depths. The instruction text needs one clause to stay unambiguous. (Medium — instruction precision)**

In this repo the skill body *is* the executable; ambiguous prose is a defect class, not a nit. Step 5.6 is numbered after Step 5, and Step 5 deletes review files for the rescued slug at every real-defect depth:
- **spec** (`:288`) and **spec + plan** (`:302`) delete *all* plan-review and review files for the slug.
- **spec + plan + code** (`:322`) deletes reviews, keeps plan-reviews.
- **plan-ratified** (`:338`) deletes reviews, keeps plan-reviews.

Deferred observations live in both review genres. So by the time Step 5.6 runs, an entry the session routed into a task may sit in a file that Step 5 just deleted, while a sibling survives in a kept plan-review. The behavior is *logically* correct in every path (a deleted file has nothing left to pin and nothing for `roadmap-prune`'s gate to later flag), but the plan's literal wording — "append … to the entry and to **every sibling occurrence** across that milestone's review files" — invites an agent that captured occurrences during Step 1's read to attempt an `Edit` on a now-deleted file, which fails.

Recommendation: add one clause to Task 2's Step 5.6 bullet scoping the pin to **surviving** review files on disk at pin time (e.g. "…across every review file still present on disk for that milestone — Step 5 may already have deleted the rescued slug's review files"). One phrase closes the ordering ambiguity without adding rationale prose or threatening the ≤500-line guard.

### Minor / Non-blocking

- **Line-anchor drift in Task 1.** The plan cites the marker list as `:58-59` and the dedup rule as `:61-63`; in the current file the marker list spans `:58-60` and the dedup rule `:61-63`. This does not affect correctness — Task 1 replaces a unique verbatim sentence ("All four markers are written by `milestone-rescue-audit` only."), so the `Edit` matches by exact string regardless of the approximate line hints. Worth tightening only if the anchors are re-used mechanically.
- **"disposal tools" framing.** The writer-set sentence labels all marker-writers "downstream **disposal** tools," but `[audit-corroborated]`/`[audit-dismissed]` are written by audit *rescue* mode, which is evaluative rather than disposal. The sentence immediately carves those out per-marker, so the meaning is unambiguous, and the framing is copied verbatim from spec 09 §2 — the plan faithfully implements the ratified spec, so this is not a plan defect. Noting only for awareness.

### Positive Notes

- **Correct single edit point.** The plan correctly identifies that the exclusivity claim lives at one site and that removing it requires touching only that closing sentence — the guard "leave everything else in §6 byte-identical" is the right contract for an engine other skills cite.
- **Guard discipline.** Task 3's verification set (grep for the writer-set split, empty diffs on audit + prune, `wc -l ≤500`, and the milestone-52 behavior baseline) is a genuine regression fence, not ceremony — the milestone-52 baseline (hand-pinned entries → specs 07/08, every sibling marked) gives the implementer a concrete oracle for "what Step 5.6 should now produce."
- **What-NOT-to-do symmetry.** Adding the ban clause (rescue writes only `[promoted → <path>]`; evaluating/dismissing/sweeping stay audit's) mirrors the existing audit-side prohibition and keeps the two skills' contracts legible from either file.
- **Faithful to the composition model.** No grammar is inlined into the caller; the caller cites `orchestrator-artifacts §6`. This respects the load-once engine boundary and the "never inline an engine's content into a philosophy skill" rule.

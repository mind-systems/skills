## Plan Review Summary

**Plan:** `59-milestone-rescue-dismiss-disposed-observations-in-session-not-just-promote.md`
**Files Reviewed:** 1 plan + full spec/loader chain (spec 13, spec 09, engine §6, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune`, ROADMAP line 129, ARCHITECTURE.md)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`ARCHITECTURE.md` → "Composition: mechanism vs policy"): PASS. The change widens the *writer-set statement* (a format/grammar — mechanism) in the engine `orchestrator-artifacts` §6, while the disposal *decision* (evaluate-and-moot → dismiss) is added as policy inside the philosophy skill `milestone-rescue`. This respects the engine-holds-mechanism / philosophy-holds-policy boundary exactly as spec 09 did before it. No dependency-direction violation: `milestone-rescue` already declares `loads: orchestrator-artifacts`; no new edge is introduced.
- **Rules** (`.ai-factory/RULES.md`): WARN — file absent (optional). No convention source to check against.
- **Roadmap** (`ROADMAP.md:129`): PASS. Milestone line matches the plan title and names `Spec: .ai-factory/specs/13-rescue-dismiss-disposed-observations.md`. Followed the reference tree: contract line → spec 13 → spec 09 (predecessor invariant) → engine §6 and `milestone-rescue` Step 5.6 / What-NOT-to-do. Findings judged against this tree.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): absent — not applicable.

### Verification of the plan against ground truth

Every line anchor and quoted string in the plan was checked against the actual files:

- **Task 1** — engine §6 writer-set sentence. Confirmed: the marker-name list is at `:58-60`, the writer-set sentence is at the tail of §6, and the marker names / append-only / "entry text & `Affects:` never rewritten" / **Pinned** definition / sibling dedup rule are all present and correctly identified as byte-identical-preserved. The rewrite target matches spec 13 §1 verbatim in intent (both `[promoted → <path>]` and `[audit-dismissed]` written by the disposing skill; only `[audit-corroborated]` / `[unrouted-reported]` remain audit's). The `[audit-dismissed]` token is preserved (no rename), honoring the spec's ripple guard.
- **Task 2** — Step 5.6 lives at `:419-432`; the on-disk scoping the plan says to preserve verbatim in intent is at `:426-430`. Confirmed accurate. Both disposal branches, the dedup citation to `orchestrator-artifacts` §6, and the moment-of-disposal rule match spec 13 §2.
- **Task 3** — the What-NOT-to-do clause to replace is at `:464-468` and currently says exactly what the plan claims (bans `[audit-dismissed]`, "Rescue's only marker is `[promoted → <path>]`", "evaluating, dismissing, and sweeping stay `milestone-rescue-audit`'s"). The replacement text is quoted **verbatim** from spec 13 §2. Confirmed.
- **Task 4** — reverse-graph grep confirmed the three loaders are exactly `milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune`. The verify checks reproduce spec 13's "How to verify" list.

**Coherence risk checked and cleared:** the plan's guard "leave `milestone-rescue-audit`'s body untouched" is only safe if the audit body does not claim *exclusive* ownership of `[audit-dismissed]`. I read the audit Write contract (`:294-303`) and its What-NOT-to-do (`:313-338`): it describes what *it* writes ("the only writes **either one** ever performs"), scoped to its own two modes — never a cross-skill monopoly claim. Widening §6 therefore leaves the audit body coherent, and the remaining `[audit-dismissed]` references in the audit (`:145,272,288,300-301,335`) all stay valid because the audit still writes the marker. No stale reference is introduced anywhere in `src/`.

**Line-budget guard:** `milestone-rescue` is 468 lines today; the dismiss branch (Task 2) plus the same-length clause swap (Task 3) land it well under the ≤500 ceiling. Confirmed.

**Frontmatter / tooling:** `milestone-rescue` `allowed-tools` already includes `Edit` (`:13`); no frontmatter change needed and the plan correctly omits one. No new skill, so no `active/` symlink or CLAUDE.md active-set edit is required — correctly out of scope.

**Settings sanity:** Testing "no" is correct — these are markdown skill files with no silently-failing runtime surface (per `test-philosophy`). Docs "no" is correct — internal marker-grammar change, no user-facing doc.

### Critical Issues
None.

### Positive Notes
- The plan is a faithful, minimal extension of spec 09's ratified shape — "whoever disposes pins, at the moment of disposal" — by exactly one marker, with every grammar/pinned/dedup invariant explicitly frozen byte-identical.
- Dependency ordering (Task 1 → 2 → 3 → 4) is correct: the engine writer-set must widen before the caller's What-NOT-to-do can legally drop the ban.
- Task 4 is a genuine coherence gate (empty `git diff` on audit + prune, plus the three-loader grep), not a rubber stamp — it catches accidental collateral edits.
- The on-disk scoping caveat (deleted review files have nothing to pin / nothing for prune's gate) is carried forward verbatim, so the dismiss path inherits the same rollback-interaction safety the promote path already has.

### Minor observation (non-blocking, no change required)
- Task 1 cites the writer-set sentence as `:63-67`; the sentence's first two words ("Markers are") actually begin on line 62 ("…`Affects:` target + gist). Markers are written by downstream **disposal** tools,"). This is a one-line-early anchor, not a content error — the plan additionally identifies the sentence by content ("the writer-set sentence at the tail of §6") and explicitly instructs preserving the "reviewer-never-writes-markers point" that sits on line 62–63, so an implementer editing by content cannot be misled. Advisory anchor only; no correction needed.

PLAN_REVIEW_PASS

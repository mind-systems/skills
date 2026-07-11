## Code Review Summary

**Files Reviewed:** 1 plan (`75-1-8-2-…md`) against its governing spec `.ai-factory/specs/38-prune-sweep-scoped-keep-rule-removed.md`, the roadmap contract line (`ROADMAP.md:169`), and the target `src/skills/roadmap-prune/SKILL.md`
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap linkage:** OK. The plan heading matches milestone `1.8.2` (`ROADMAP.md:169`); its `Spec:` tag resolves to `specs/38-prune-sweep-scoped-keep-rule-removed.md`. The milestone sits under Phase 1 "Pyramid rewrite"; its phase intro (`ROADMAP.md:143-149`) names no explicit `Governing spec:`, so the spec note is the authoritative tree — the plan is judged against it.
- **Spec fidelity:** OK. All three spec changes are covered: both automatic task retentions deleted (Task 1 = Step 1 slice; Task 2 = Step 6 "2 most recent"), last-phase-header anchor preserved (Task 2), spec sweep scoped to pruned lines only (Task 3). Verified guards honored: capture-before-delete ordering and "no tag → skip, never synthesize" kept verbatim (Task 3); four-dir artifact sweep left unchanged (Task 3); gate untouched (1.8.1 territory, not mentioned — correct).
- **Line-reference accuracy:** OK. Every cited range matches the current file — Step 1 `74-82`, Step 5 item 1 `214`, Step 6 `232-234`, Step 7 `262-263`. Approximate (`~`) prefixes are used, which is safe against drift.
- **Scope discipline:** OK. The plan does not compress rationale prose — that is 1.8.3's pyramid pass. Task 1 explicitly keeps the step "instructions-only," consistent with the skill's own mandate and not overstepping the downstream milestone.
- **ARCHITECTURE.md / RULES.md:** No boundary or convention impact — this is a self-contained edit to one skill body.

### Critical Issues
None.

### Issues

1. **Two trailing spec-scope statements in the edited sections are left unreconciled (low severity).** Task 3 scopes the Step 5 capture to *pruned* lines only, but the plan does not mention two sentences that assert the deletion mechanism in terms of "every `[x]` line":
   - `SKILL.md:218` — "Spec deletion goes only through `[x]` lines' `Spec:` tags — no spec directory is ever scanned or swept, so open `[ ]` tasks' specs are never touched." This is inside the very step Task 3 edits. Its open-`[ ]` reassurance stays true, but after scoping, a **user-kept `[x]` line's** spec is also never deleted — the phrase "`[x]` lines' `Spec:` tags" now reads as *all* `[x]` lines and no longer distinguishes pruned from kept.
   - `SKILL.md:295-296` (What NOT to do) — "spec deletion goes only through `[x]` lines' `Spec:` tags; never touch a path an open `[ ]` line's tag names." Same phrasing, same imprecision.

   Task 3's own verification says "capture speaks only of pruned lines," so the surrounding guard prose should say the same (e.g. "the **pruned** `[x]` lines' `Spec:` tags"). Recommend adding a note to Task 3 to reconcile lines 218 and 295-296 so the changed step reads coherently. This is a wording-coherence item, not a logic defect — the sweep behavior is correct either way.

### Positive Notes
- Task 2 correctly anticipates the ripple: the emptied-phase (`:240-241`) and emptied-direction (`:247-249`) sweep caveats reference "a phase that still holds a kept `[x]` task" / "the retain rule above," which pointed at the now-deleted auto-retention. The plan explicitly instructs adjusting that wording so it reads as *user-kept*, not auto-retained — a non-obvious dependency that a narrower plan would have missed.
- The dependency edges (Task 3 → Task 1, Task 4 → Task 2) are logical and the two-phase split (remove retentions, then scope the sweep) is clean.
- The verification section faithfully mirrors the spec's three dry-runs (one named keep; no keeps; grep for surviving auto-retention language), and correctly reads the grep as "no automatic-retention language" rather than "zero matches" — avoiding a false expectation, since legitimate words like "keeps its header" and "user-kept" survive.
- Task 4 correctly targets the stale Step 7 verify phrase ("kept as recent context") that would otherwise describe a removed mechanism.

## Deferred observations
- Affects: the milestone's governing spec (`specs/38`) / the skill's own flow — Both the spec and the plan (Task 1) state a retained `[x]` line is named "at invocation or at the confirmation step," but `roadmap-prune/SKILL.md` has no discrete confirmation step (its flow runs Step 0→8 then a commit-on-request block; it does not load `roadmap-engine`'s draft→confirm flow). In practice the only reliable retention channel is "at invocation," with the pre-commit working-tree review as an informal second chance. This wording is inherited verbatim from the ratified spec, so it is not a plan defect; flagging it because if a future task ever wants the "confirmation step" to be real, it would need to add one — outside this milestone's boundary. [routed → .ai-factory/specs/52-prune-prose-reconciliation.md]

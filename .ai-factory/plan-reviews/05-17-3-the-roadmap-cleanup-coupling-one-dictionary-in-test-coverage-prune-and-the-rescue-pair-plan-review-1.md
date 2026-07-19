# Plan review — 17.3 The "roadmap cleanup" coupling: one dictionary in test-coverage, prune, and the rescue pair

## Code Review Summary

**Files Reviewed:** 1 plan + 4 target `SKILL.md` files + spec 72 + contract line 17.3 + `roadmap-engine`, `roadmap-outline`, ARCHITECTURE.md, and the orchestrator's `resume.py`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — PASS.** The plan touches only four `SKILL.md` bodies under `src/skills/`, which is exactly where "skills we authored" live per ARCHITECTURE.md § three zones. No `references/` directories exist for any of the four (verified), so the spec's "no `references/` touched" is vacuously satisfied. `active/skills/{roadmap-prune,roadmap-test-coverage,task-rescue,task-rescue-audit}` are all **directory-level** symlinks into `src/skills/`, so edits propagate with no symlink work — the plan correctly lists no such step. No `upstream/` file is in scope.
- **Rules — WARN (non-blocking).** No `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md` in this repo; the governing constraints come from `docs/reserved-words.md` and `docs/using-the-language.md`, both loaded, and the plan conforms to them.
- **Roadmap — PASS.** Contract line 17.3 is present at `ROADMAP.md:29`, unchecked, and names `Spec: .ai-factory/specs/72-cleanup-coupling-one-dictionary.md`. The plan's `# Plan:` heading matches the contract line's title verbatim. Every element the contract line mandates — `milestone`→`task` never `phase`, `spec note`→`task spec`, the prune 325 dual form, external-corpus strings unconformed, `milestone line`→`contract line` never `task line`, protocol literals byte-identical — is carried into a task in the plan.
- **Spec chain — PASS.** Spec 72 is modified-uncommitted; the plan states this and declares the working-tree version governing. Confirmed: the working-tree spec already absorbs all four carve-outs (prune 75, prune 325 dual form, task-rescue 10 trigger, 65/189 contract-line), so the plan is verifying against the amended file, not the older HEAD inventory.

### Critical Issues

None.

### Verification of the plan's own ground-truth claims

Every load-bearing claim was independently re-derived. All hold:

| Plan claim | Verified |
|---|---|
| `rg -U -in -c 'milestones?'` → tc 3, prune 2, rescue 25, audit 6 | ✅ exact |
| `spec note` → 16 lines in `task-rescue` at 21, 28, 29, 49, 133, 134, 162, 206, 209, 238, 281, 283, 284, 299, 318, 448 | ✅ exact — 16 occurrences on 16 distinct lines, no double-per-line |
| Hyphenated `spec-note` at `task-rescue:269` and `task-rescue-audit:206` | ✅ both present, invisible to the `\s` form as stated |
| `_validate_sidecar_step` / `_detect_task_step` live in `orchestrator/resume.py` at `:11` and `:169` | ✅ exact — the milestone-named function is already renamed upstream |
| `roadmap-engine:120` flat fallback names no heading | ✅ verbatim; no `## Tasks` or `## Milestones` heading exists anywhere in `roadmap-engine` |
| 17.2 precedent — `roadmap-outline:3` still reads `"milestones"` in `Use when` | ✅ verbatim |
| Phase 14.2 targets these four descriptions as the "exhaustive pole" | ✅ `ROADMAP.md:46` |
| Bare-unit arithmetic: 25 − 2 − 1 − 1 = 21 | ✅ and independently enumerable to exactly 21 sites (8, 17, 28, 50, 55, 57, 61, 63, 183, 270, 385, 389, 391, 395, 404, 406, 407, 415, 422, 448, 450) |

**Gate baselines check out.** `rg -n 'task line\|task-line'` over the rescue pair returns zero today, so that gate is a real guard rather than a tautology. `rg -in 'roadmap lines?'` over `roadmap-prune` returns exactly three (155, 231, 276) pre-edit and will return one post-edit, exactly as the plan states. `roadmap line` appears in **no** file other than `roadmap-prune`, so scoping that gate to prune alone is sufficient — no fourth site hides in the rescue pair.

**The `argument-hint` gate is consistent.** `task-rescue`'s hint is `"[path/to/ROADMAP.md | ROADMAP_TESTS.md]"` — it carries no `milestone`, so Task 5's "diff filtered to `argument-hint` → empty" cannot collide with the `milestone slug` → `task slug` sweep. The plan's parenthetical that the audit's `"[task-slug]"` is already conformed is also correct.

### Positive Notes

- **The three carve-outs are each verified in place, not asserted.** I read `roadmap-prune:75` (genuinely inside the Step-4.6 pre-standardization marker-phrase list), `:325` (genuinely a recognition alternative over a *target project's* roadmap), and `task-rescue:10` (genuinely a quoted user utterance) — all three classifications are correct, and the external-corpus reasoning is the right frame for all three.
- **The 155 / 231 / 276 discrimination is the sharpest thing in the plan, and it is right.** Read in place, `:231`'s enclosing `git log … -- .ai-factory/ROADMAP.md` filter does already guarantee the file was touched, which makes the literal file-line reading vacuous exactly as the plan argues — only the concept reading states a real test. `:155` genuinely describes lines removed from a file at a snapshot boundary. `:276` genuinely denotes the concept. The plan's own warning that the Task 5 gate *mechanically requires* the 231 edit and therefore would enforce a misclassification rather than catch it is exactly the right reason to demand a read instead of a counter.
- **`milestone line` → `contract line`, never `task line`, is correctly reasoned and correctly gated.** Minting a third synonym for a concept the file already names right in 10 places would be a one-word-two-meanings violation introduced by the conformance fix itself — and the plan notices that the `milestone` gate returns zero either way, so it adds a dedicated `task line` gate to cover the blind spot.
- **The §2 self-correction is the right call.** Syncing the identifier while knowingly leaving `orchestrator/main.py` stale would indeed raise the sentence's apparent authority while preserving the misdirection. Both halves fail against the same ground truth and both are on a line the task already edits — fixing both is conformance, not scope creep.
- **The §4 resolution correctly prefers landed precedent over a dual form**, and the "the boundary is the quotation marks" distinction — quoted trigger frozen at `:10`, surrounding prose conformed at `:8` — is precisely where `using-the-language` draws it.
- **The behavior framing in Context is honest.** Declaring the one additive gain outright rather than repeating "zero behavior change" verbatim respects what the guard is actually for.

## Deferred observations

- Affects: Phase 14.2 / `.ai-factory/specs/68-descfield-altitude-cleanup-flow.md` — Task 6's recorded deviation replaces the spec's live-run check with static gates, and that substitution is the correct call for *this* task: no pre-conformance baseline was ever captured, so a live run would have nothing to diff against, and `roadmap-prune` is destructive against a real target project (it deletes `[x]` lines, sweeps artifact dirs, rewrites ARCHITECTURE.md), so exercising it to prove a noun rename would mean damaging a repo. The plan explicitly hands this call to the reviewer, and I am making it: the static gates plus the full post-edit read are the stronger feasible check here, and the deviation needs no repair. What outlives this task is the underlying gap it exposes — this skill family has no captured behavior baseline of any kind, so every conformance task in the direction lands on static byte-checks alone (17.1 already hit the same wall and recorded "a headless live render is impossible"). Capturing baselines is not fixable inside 17.3's four-file boundary: it would have to happen *before* the first edit of any such task, and it belongs to whoever owns the family's verification story — a natural fit for the phase that next revisits these four skills. [dismissed — stale: Phase 14.2 and spec 68 were retired/superseded before this task ran; Phase 14 landed as the single pass 14.1, the container this observation was filed against no longer exists]

PLAN_REVIEW_PASS

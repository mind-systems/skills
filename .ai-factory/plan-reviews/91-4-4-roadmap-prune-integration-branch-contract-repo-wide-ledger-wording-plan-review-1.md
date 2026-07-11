## Code Review Summary

**Files Reviewed:** 1 plan (`91-4-4-roadmap-prune-integration-branch-contract-repo-wide-ledger-wording.md`), targeting `src/skills/roadmap-prune/SKILL.md`
**Risk Level:** 🟢 Low

Wording-only, two-sentence policy amendment to a single skill file. No mechanism, gate, sweep, or commit change. Grounded against the governing spec (`docs/multiuser-roadmaps.md` § «Интеграционные поверхности»), spec note `46-prune-integration-branch-contract.md`, and the live target file.

### Context Gates
- **Roadmap linkage:** the plan heading matches ROADMAP.md line 213 (`4.4 — roadmap-prune: integration-branch contract + repo-wide ledger wording`), whose `Spec:` tag resolves to `.ai-factory/specs/46-prune-integration-branch-contract.md`. Chain intact. — OK
- **Governing spec:** spec 46 names `docs/multiuser-roadmaps.md` § «Интеграционные поверхности» as its governing spec. Both sentences the plan prescribes are faithful paraphrases of that section's lines 51 (integration-branch, one actor, after merges; Features are project features; single-actor keeps both surfaces single-writer) and 53 (repo-wide ledger; snapshot holds all files; `git show <снапшот>:<путь роадмапа>` reconstructs any roadmap), plus spec 46 line 14's "no per-roadmap ledger rows". — OK
- **Dependency ordering:** the plan and spec both state this runs strictly after task 3.1 lands (same-file collision; 3.1's ledger text is the amended base). The target file already shows 3.1's landed artifacts (versioned `## Features (roadmap-prune v2)` header, 4.2a self-heal, snapshot semantics), confirming 3.1 is in place. — OK
- **Architecture / Rules:** no ARCHITECTURE/RULES boundary touched — this is skill-body wording within the skill's own mandate ("instructions only, no rationale prose"), which the plan explicitly preserves. — OK

### Critical Issues
None.

### Positive Notes
- **Accurate line anchors.** Every line reference in the plan is correct against the live file: Step 4.2 "Write Features and drop history" (line 198), the Step 2.2 drop-history bullet carrying the `git show <hash>:.ai-factory/ROADMAP.md` reconstruction wording (line 143), and the Step 4.2 drop-history write (lines 240/247). The plan's disambiguating qualifier — "pick the drop-history instruction site so it sits beside the existing `git show <hash>:.ai-factory/ROADMAP.md` reconstruction wording" — resolves cleanly to line 143, the only drop-history site adjacent to that reconstruction text (line 173 is a Step 3 bash example, line 340 is a What-NOT-to-do bullet).
- **Solo-project invariance preserved.** Both sentences are made conditional on `.ai-factory/roadmaps/` existing, and Task 2 explicitly requires the existing single-roadmap `git show <hash>:.ai-factory/ROADMAP.md` text to stay byte-identical (additive clause). This matches spec 46's verification: "Solo-project reading of the skill is unchanged in behavior."
- **Guards mirror the spec.** The plan's "do not touch Step 0 gate, Step 5 sweep, commit policy, or 3.1's self-heal/versioned-header/snapshot text" is a precise restatement of spec 46's Guards section.
- **Verification-aware placement.** Task 1 places the integration sentence at Step 4.2 specifically so `grep -n "integration"` hits it next to the Features write step — matching spec 46's verification clause.
- **Implementer awareness (not a defect):** line 142 already contains the token "integration" ("a new protocol integration"). The spec's `grep -n "integration"` verification will therefore return that pre-existing hit *plus* the new Step-4.2 hit; the verification ("hits the policy sentence next to the Features write step") remains satisfied because the new sentence is the one adjacent to the Features write. No plan change needed — noted only so the verifier reads the multi-line grep output correctly.

The plan is atomic, correctly ordered behind its dependency, faithful to the governing spec's wording, and scoped to leave every other behavior byte-identical. It is ready to implement.

PLAN_REVIEW_PASS

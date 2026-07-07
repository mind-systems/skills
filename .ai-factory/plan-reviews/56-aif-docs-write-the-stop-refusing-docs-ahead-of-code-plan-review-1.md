## Plan Review — aif-docs: write the ТЗ, stop refusing docs-ahead-of-code

**Plan:** `.ai-factory/plans/56-aif-docs-write-the-stop-refusing-docs-ahead-of-code.md`
**Spec:** `.ai-factory/specs/10-aif-docs-rewrite-tz.md`
**Target files:** `src/skills/aif-docs/SKILL.md`, `references/REVIEW-CHECKLISTS.md`, `references/topic-guides.md`
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): No aif-docs-specific boundary or composition rule; the plan touches no `loads:` edge and no engine contract. **PASS.**
- **Rules** (`.ai-factory/RULES.md`): absent. **WARN** (optional file missing) — no convention source to check against.
- **Roadmap** (`.ai-factory/ROADMAP.md`): the milestone line ("aif-docs: write the ТЗ — stop refusing docs-ahead-of-code", `Spec: .ai-factory/specs/10-aif-docs-rewrite-tz.md`) exists and is unchecked; the plan's `# Plan:` heading matches it; the spec note resolves. **PASS.**
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project override to apply.

### Verification performed
- Ran both spec greps against current `src/skills/aif-docs/`. **Every** `3d`/`3д`/`MODE = 3D`/`Document-Driven` hit and every nav-residue hit the plan enumerates is real and correctly line-numbered (SKILL.md:4, 64, 67-70, 72-92, 95, 345, 395-400; REVIEW-CHECKLISTS.md:11, 12, 15, 43; topic-guides.md:8). No un-enumerated `3d` occurrence exists — Task 2/3/4/5 coverage is complete for the token-based deletions.
- Confirmed line citations `:13-15`, `:93-97`, `:345`, `:395-400`, and the reference-file citations all point at exactly the text the plan describes. Task dependency chain (1→2→3→4→5→6) and the two-commit split are coherent and match the repo's git conventions (imperative, no type prefix, no period).

The plan is faithful and mechanically accurate. Three gaps remain.

### Findings

**1. Residual "mode" vocabulary survives the single-mode collapse — and the Task 6 greps won't catch it.**
The plan collapses two modes into one but leaves stale "mode" wording that the reframe orphans:
- `SKILL.md:24` — Principle 6 ends "…applies to **every run, every mode, no exceptions**." Task 1 instructs "Keep Principle 6 intact," which literally preserves "every mode" — a reference to a concept the plan is deleting.
- `SKILL.md:391` — "**No-motivation pass (mandatory, all modes):**" retains "all modes."

Once `3D`/`normal` no longer exist, "every mode" / "all modes" read as dangling references to a deleted distinction. The Task 6 verification greps only match `3d|3д|MODE = 3D|Document-Driven` and the nav tokens — none of them match the bare word `mode`, so these survive the guard. Recommend: (a) reconcile the "keep Principle 6 intact" instruction — keep the *rule* intact but drop/rephrase its "every mode" clause (e.g. "every run, no exceptions"); (b) sweep `SKILL.md:391`'s "(mandatory, all modes)" to "(mandatory)"; (c) add `mode` (or `all modes`/`every mode`) to the Task 6 verify sweep so orphaned mode language is caught. This is in-scope, in-boundary, and introduced by the diff — a finding, not a deferral.

**2. Spec Change item 4's "coordination-trio staleness check" is not landed in any task.**
Spec §Change item 4 requires: "On each run, check the coordination trio — README, the CLAUDE.md index, ARCHITECTURE.md — for staleness; refresh what aif-docs owns; for ARCHITECTURE.md just **check for staleness, don't clobber** its structural info — no descriptive-vs-structural boundary, no aif-architecture edit." Task 1 captures the *first half* of item 4 (point Principle 3 at the existing CLAUDE.md index; one-home-per-fact role split) but is silent on the trio-staleness behavior and the ARCHITECTURE.md check-don't-clobber clause. It is partly covered by existing behavior (State C audit already checks README length and CLAUDE.md-index staleness; ARCHITECTURE.md is read-only in Step 0), so this is a completeness gap rather than a contradiction — but the plan should either add a sub-step wiring the on-each-run trio check (especially the explicit "check ARCHITECTURE.md for staleness without clobbering" stance) or state explicitly that existing State C / Step 0 behavior already satisfies item 4. As written, an implementer following only the tasks would not produce the trio-staleness check the spec calls for.

**3. Frontmatter `description` (SKILL.md:3) is left README-centric while the body is reframed ТЗ-first.**
The router-facing `description` still reads "Generate and maintain project documentation. Creates a lean README as a landing page…" — the most load-bearing self-description for skill invocation. The spec's Verify says "**Skill identity** + Core Principles state that docs are ТЗ," and its doctrine says "Rephrase the skill's self-description." The concrete instruction quotes "Project Documentation Generator," which is the H1 (line 13) the plan does target — so strictly the plan matches the literal citation. But the frontmatter is arguably part of "skill identity." Recommend the plan state explicitly whether the frontmatter `description` is in or out of scope. Caveat worth pinning either way: the `description` also carries the invocation trigger phrases ("create docs", "update docs", "generate readme"…) — rewording it risks changing when the skill is auto-selected, so if touched it should keep those triggers intact.

### Positive Notes
- Line citations are exact and were independently reproduced by grep — no drift between plan and code.
- The plan correctly anticipates numbering drift and pins Principle 6 **by name** rather than by number.
- The "no lead/lag meta-commentary" guard is repeated at every task that could reintroduce it (Tasks 1, 3, 6) — the exact insight (that spelling out the duality is what spawned `3d`) is preserved, matching the spec's strongest guard.
- Scope discipline is good: the plan explicitly keeps the README/onboarding genre, the A/B/C state machine, `--web`, and the review ceremony, matching the spec's "no fork this pass" boundary. It does not touch `upstream/` or `aif-architecture`.
- Task 4 correctly handles `:44` (linear-path reading-order) via manual reframe even though it contains none of the grep tokens — a subtlety the verify greps alone would miss.

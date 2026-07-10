## Plan Review Summary

**Plan:** `70-1-5-milestone-rescue-pyramid-pass.md`
**Milestone:** ROADMAP.md § "Pyramid rewrite" → Phase 1 → `1.5 — milestone-rescue: pyramid pass` (the next `[ ]` after committed 1.1–1.4)
**Spec:** `.ai-factory/specs/25-milestone-rescue-pyramid-pass.md`
**Files Reviewed:** 1 plan against SKILL.md (477 lines), spec 25, `orchestrator-artifacts` engine, ROADMAP.md, ARCHITECTURE.md
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): OK. The plan's composition reference — "a top loads the engine, never inlines it (`.ai-factory/ARCHITECTURE.md` → 'Composition: mechanism vs policy')" — resolves to a real section (line 30). The compression respects the mechanism-vs-policy boundary: `milestone-rescue` stays a philosophy top loading `orchestrator-artifacts`, no engine mass is absorbed. WARN (non-blocking): none.
- **Rules** (`.ai-factory/RULES.md`): absent — gate skipped (WARN: optional file missing, expected for this repo).
- **Roadmap**: OK. Plan heading matches ROADMAP.md line 159 exactly. Governing-spec gate: Phase 1's header/intro (lines 147–149) names **no** `Governing spec:`, so the phase-governing-spec read is n/a for this milestone; the plan correctly grounds itself on spec 25 alone. The phase's hard rule "each rewrite passes its live baseline before the next starts" is honored — Task 3 flags the baseline replay as user-run, not orchestrator-fabricated (matches spec 25 § Guards / § Verification).
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): absent — no project overrides to apply.

### Critical Issues

**1. The `$TARGET_FILE` dedup instruction is infeasible as written — it collides with a byte-identical-protected block and would create a circular reference.** (`70-1-5-...md` Task 1 cut-candidates, Task 2 bullet 3)

The plan lists as a cut candidate: *"the twice-stated `$TARGET_FILE` resolution — keep one authoritative statement, reference it from the other site,"* and Task 2 restates it: *"de-duplicate the `$TARGET_FILE` resolution … to a single authoritative home referenced elsewhere."* But the two sites are not symmetric restatements that can be freely collapsed:

- **Step 1 (SKILL.md:57–59)** — inside the governing-spec block that Task 1 item (2) protects **byte-identical** — reads: *"Determine `$TARGET_FILE` (the same resolution Step 4 uses: argument-named file if given, else `.ai-factory/ROADMAP_TESTS.md` for test slugs, else `.ai-factory/ROADMAP.md`)"*. This text is a gloss **plus a cross-reference naming Step 4 as the authority**.
- **Step 4 (SKILL.md:183–186)** is the canonical full statement, under the heading "Determine `$TARGET_FILE`", where the repair actually reads the file.

Because Step 1's text is protected and it names Step 4 as canonical, the dedup has no legal move:
- Trimming Step 1 → forbidden (protected block).
- Trimming Step 4 to "resolve as in Step 1" → creates a **circular reference** (Step 1 points to Step 4, Step 4 points to Step 1) with no canonical statement left.

Moreover, SKILL.md:63–65 explicitly marks the two resolutions as **deliberately additive**: *"This read is additive to Step 4's own `$TARGET_FILE` resolution and milestone-line locate — it does not replace it."* The Step 1 resolution exists to locate the phase/governing-spec early; Step 4's exists to locate the milestone line for the repair. This is load-bearing structure, not ceremony.

**Impact:** an over-eager implementer follows the cut-candidate nudge, edits Step 4 (unprotected) to reference Step 1, and either breaks the reference chain or trips the reviewer; a cautious implementer leaves it and the reviewer flags "dedup not done." Either path risks a plan-review/implement loop — the exact failure mode this pyramid pass exists to avoid.

**Fix:** drop `$TARGET_FILE` from the cut list, or replace the instruction with an explicit ruling: *"`$TARGET_FILE` is already deduped — Step 1 is a protected gloss+reference, Step 4 is canonical and stays in place; do not touch it."* Contrast this with the **"read all rounds" dedup, which is genuinely available**: Step 1's mandate (SKILL.md:67) is the protected canonical home, and Step 3 (SKILL.md:120) carries a bare restatement ahead of its recurring-issues logic that can be trimmed to a reference without collision. Keep that one; the plan should distinguish the two cases rather than pairing them as equivalent.

### Non-critical Issues

**2. Task 1 produces no durable on-disk deliverable.** (Task 1) Its output is "an in-session checklist for Task 2." That is fine *if* Task 1 and Task 2 run in one implement session (the inventory is fully re-derivable from SKILL.md + spec 25 + the engine, all readable at Task 2 time anyway). It is worth stating explicitly in the plan that Task 1 is preparatory reading with no diff, so a reviewer does not read the empty diff as a stale/no-op implementation. Low severity — structural clarity, not a defect.

### Positive Notes

- The **seven verbatim-protected blocks** in Task 1 are catalogued accurately against the live file — each maps to real content (artifact-discovery Step 1; governing-spec read 57–65 + its What-NOT-to-do bullet 454–457; Diagnosis Report register 149–172 incl. the "shared with `milestone-rescue-audit` — change in both or neither" clause; the four depth deleted-file sets 280–348; the `step` closed-set table 352–376 with its `_validate_sidecar_step()`/`_detect_milestone_step()` mirror invariant; the whole What-NOT-to-do list; Step 5.6 disposal grammar 419–441). No phantom block, no mislocated one.
- **Frontmatter contract is correct**: `loads: orchestrator-artifacts`, `allowed-tools`, `description`, `argument-hint` all present and correctly marked byte-identical (SKILL.md:1–15).
- Task 3's guards are well-chosen — the `grep -n` spot-check for surviving layout-restatement hits, the protected-block diff check, and the routing-preservation checklist together give the reviewer a concrete pass/fail.
- The plan correctly refuses to invent the live baseline (Task 3 final note) and correctly treats ≤500 as trivially-held, not a target to pad toward — matching spec 25 § Guards.
- Composition discipline is right: cut = link to the engine, never inline; the top stays a lens.

### Recommendation
Resolve Issue 1 (drop or re-rule the `$TARGET_FILE` dedup) before implementation; optionally address Issue 2. With Issue 1 clarified, the plan is sound and faithfully executes spec 25.

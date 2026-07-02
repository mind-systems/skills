## Code Review Summary

**Files Reviewed:** 1 plan + target `src/skills/aif-docs/SKILL.md` + `references/REVIEW-CHECKLISTS.md` + spec note 48 + ROADMAP milestone
**Risk Level:** 🔴 High

### Context Gates

- **Roadmap (WARN→ERROR feeder):** Plan title matches ROADMAP.md line 85 milestone; governing spec is `.ai-factory/notes/48-aif-docs-index-in-claude-md.md`. Linkage OK. **However, the spec itself carries an internal contradiction that the plan inherited** — see Critical Issue 1.
- **Architecture:** `.ai-factory/ARCHITECTURE.md` has no boundary/dependency rule touching README/CLAUDE.md doc-index placement. No conflict.
- **Rules:** No `.ai-factory/RULES.md` present. Skipped.
- **Line-number accuracy:** All cited lines verified against the current file — Task 1 (line 21, Principle 3), Task 2 (template 291–298, rule 311), Task 4 (line 208), Task 5 (374/395/410), Task 6 (State C 417–425), Task 7 (Step 5 531–554). All correct. Good.

### Critical Issues

**1. The review-checklist file still requires, audits, and AUTO-RE-ADDS the README documentation table — and the plan (per spec) refuses to touch it. This self-reverts the feature.**

The plan scopes all edits to `SKILL.md` ("All edits are confined to a single file"), echoing spec note 48 line 25 ("review checklists … unchanged"). But `references/REVIEW-CHECKLISTS.md` — which the skill **actively reads and enforces** — hard-codes the old convention in three places:

- Line 8 (Technical Checklist): `README has: title, tagline, quick start, example, documentation table, license`
- Line 44 (Readability): `Is the Documentation table in README ordered by the path a new user would follow?`
- Line 57 (Standards Compliance, **auto-fix**): `Missing Documentation table in README | README has no table linking to docs/ pages | Add table`

These are not dormant text. `SKILL.md` wires them in:
- Step 2.1.1 (line 429): "read `references/REVIEW-CHECKLISTS.md` (Standards Compliance section)" — auto-fix rules.
- Step 4 (line 484): "evaluate it against both checklists from `references/REVIEW-CHECKLISTS.md`".

Consequences after the plan lands:
- **Self-reverting:** On the next State C audit run, the Standards-Compliance auto-fix (line 57) detects the now-tableless README as a gap and **re-adds the README documentation table** — directly undoing Tasks 1–2. The feature is unstable across runs.
- **False failure:** Step 4's mandatory review flags every correctly-produced tableless README as failing the Technical Checklist (line 8).

This is a wrong-scope assumption, not a stylistic nit. The plan must either (a) add a task retargeting REVIEW-CHECKLISTS.md lines 8/44/57 to the CLAUDE.md `## Documentation` section (retiring the README-table auto-fix, and optionally adding a legacy-README-table detector there — this is where the real audit lives, see Issue 5), or (b) escalate the spec-note contradiction (line 14 "every place the README table is audited is retargeted" vs. line 25 "review checklists unchanged") to `milestone-rescue` before implementing. As written, Task 6's "retarget any audit check that verifies the README documentation table" cannot succeed because the actual audit lives in the file the plan excludes.

### Issues (should fix)

**2. Dangling reference in Step 5 after Task 2 removes the README table.**
`SKILL.md` line 549 instructs: "…all doc files … **in the same order as the README Documentation table**". Task 2 deletes that table; Task 7 edits Step 5 but only adds the redirect sentence and leaves line 549 intact. The ordering source now points at a table that no longer exists. Retarget it to the CLAUDE.md `## Documentation` section (or the docs directory's logical reading order, matching Task 3's ordering rule). This edit is inside SKILL.md — fully in scope — but no task covers it.

**3. Dual index home (AGENTS.md + CLAUDE.md) for non-redirect projects.**
After Task 3, CLAUDE.md gains a `## Documentation` section; Step 5 still maintains a `## Documentation` table in AGENTS.md (Task 7 keeps it "as-is" except the one redirect sentence). In this repo AGENTS.md is a one-line redirect to CLAUDE.md, so Task 7's carve-out applies cleanly. But for a general project where AGENTS.md is a full standalone file, the index is then duplicated across two agent-context files — drift risk, and it contradicts the single-home intent (spec "What NOT to do" line 32 forbids the README+CLAUDE.md double, but is silent on AGENTS.md+CLAUDE.md). This traces to spec item 6 covering only the redirect case; flag for the author to confirm the intended behavior (e.g., when both a full AGENTS.md section and CLAUDE.md exist, which is canonical?) rather than shipping an ambiguous double.

### Minor / Notes

**4. CLAUDE.md not added to the skill's ownership declarations.** The skill will now create/write the project's `CLAUDE.md` `## Documentation` section, but "Artifact Ownership" (lines 560–564) and Important Rule #7 (line 574) list only README / docs dir / AGENTS.md. Add CLAUDE.md's Documentation section to both for consistency; otherwise the skill writes an artifact it does not declare it owns. Small, but it's the write-scope contract.

**5. Task 6's SKILL.md-only retarget is largely vacuous.** State C 2.1 in SKILL.md has no explicit README-table check — only a generic broken-links check (line 421). The real README-table existence/auto-fix logic is in REVIEW-CHECKLISTS.md line 57 (see Issue 1). Adding the legacy-table flag in SKILL.md State C is fine, but the substantive audit retarget belongs in the references file.

### Positive Notes

- Line-number citations are accurate throughout — implementer can navigate directly.
- Correct discipline on the upstream mirror (`upstream/ai-factory/aif-docs` untouched) and frontmatter.
- Task dependencies and the two-commit split are logically ordered.
- The CLAUDE.md `## Documentation | Doc | What it covers |` shape matches this repo's own existing CLAUDE.md convention — the target format is grounded, not invented.
- Body-growth restraint (reword, don't add blocks) correctly respects the known >500-line constraint and the follow-on diet milestone (ROADMAP line 87).

### Verdict

The plan is faithful to spec note 48 and its line references are exact, but it inherits the spec's blind spot: the enforced review checklists (`references/REVIEW-CHECKLISTS.md`) still mandate and **auto-restore** the README documentation table, which makes the change self-reverting and produces false review failures (Critical Issue 1). Plus a dangling ordering reference (Issue 2) and an unresolved dual-index case (Issue 3). These must be addressed — by widening scope to the checklist file (and Step 5 line 549) or by escalating the spec contradiction — before implementation.

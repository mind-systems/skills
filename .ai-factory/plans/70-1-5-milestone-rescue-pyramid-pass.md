# Plan: 1.5 — milestone-rescue: pyramid pass

## Context
Compress `src/skills/milestone-rescue/SKILL.md` (477 lines) — the heaviest philosophy top — by cutting procedural ceremony and protocol restated from the loaded `orchestrator-artifacts` engine, while landing every contract block byte-identical. A compression, not a redesign: behavior-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Compress milestone-rescue to a lens

- [x] **Task 1: Pin the verbatim-protected inventory + cut list**
  Files: (read-only) `src/skills/milestone-rescue/SKILL.md`, `.ai-factory/specs/25-milestone-rescue-pyramid-pass.md`, `src/skills/orchestrator-artifacts/SKILL.md`
  Do not edit yet — this is preparatory reading with **no diff**; Task 1 and Task 2 run in one implement session, and the checklist is fully re-derivable from SKILL.md + spec 25 + the engine (all readable at Task 2 time). An empty diff here is expected, not a stale/no-op implementation. Read the current skill, the spec, and the engine, and record as an in-session checklist for Task 2 — the contract Task 2 must not break. Two lists:
  - **Verbatim-protected (must land byte-identical):**
    (1) the artifact-discovery block — Step 1's `git status --short -- .ai-factory/` scan, the artifact-directory filter, the "nothing to rescue" stop, the milestone-slug identification, the multi-slug ask, and the "read every artifact file / all rounds" mandate;
    (2) the governing-spec mandatory read — Step 1's `$TARGET_FILE` resolution + phase-section locate + `Governing spec:` unconditional-read paragraph, and its paired "What NOT to do" bullet;
    (3) the Diagnosis Report register — Step 3's Form paragraph (chronological narrative, one paragraph per round, length scales with rounds), the "shared with `milestone-rescue-audit` — change in both files or neither" clause, the no-tables/no-bullets rule, the stale-implementer variant, the domain-language / zero-orchestrator-vocabulary rule, and the standalone set-off root-cause sentence;
    (4) the per-variant deleted-file sets — Step 5's four depth blocks (spec / spec+plan / spec+plan+code / plan-ratified) with their exact delete lists, sidecar `step` values, `implementer`-key handling, and the `Emit:` lines;
    (5) the sidecar `step` closed-set table — the 5-row table, the "mirrors `_validate_sidecar_step()` / `_detect_milestone_step()`" invariant, the Silent-failure / Test-mode / Always-valid guards, and the "`plan_reviewed` IS written by this skill" note;
    (6) the entire "What NOT to do" list;
    (7) Step 5.6's disposal grammar — the `[promoted → <spec path>]` / `[audit-dismissed]` branches, the "scope to review files present on disk" rule, and the "rescue never writes `[audit-corroborated]` / `[unrouted-reported]`" clause (grammar owned by `orchestrator-artifacts` §6, byte-identical).
  - **Cut candidates (ceremony / restated protocol):** any sentence restating what `orchestrator-artifacts` already carries (directory layout, `<seq>-<slug>` naming mechanics, PASS-signal semantics, sidecar-field list) — replace with a link/reference to the engine, never a restatement; transitional prose between contract blocks; step-narration an executor performs unprompted; duplicated rationale prose. **One genuine dedup only — the "read all rounds" mandate:** Step 1 (SKILL.md:67) is the protected canonical home; Step 3 (SKILL.md:120) carries a bare restatement ahead of its recurring-issues logic that may be trimmed to a reference to Step 1 without collision. Frontmatter (`loads: orchestrator-artifacts`, `allowed-tools`, description) is unchanged.
  - **`$TARGET_FILE` resolution is NOT a dedup target — do not touch it.** The two sites are deliberately additive, not symmetric restatements: Step 1 (SKILL.md:57–59) is a protected gloss that *already* names Step 4 as canonical and exists to locate the phase/governing-spec early (SKILL.md:63–65 pins this as "additive to Step 4's own resolution — it does not replace it"); Step 4 (SKILL.md:183–186) is the canonical full statement where the repair reads the file. Trimming Step 1 is forbidden (protected block); trimming Step 4 to point back at Step 1 creates a circular reference with no canonical statement left. Leave both in place verbatim.

- [x] **Task 2: Compress the file** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Rewrite for compression, not redesign — the step structure (Step 1 → 5.6 + What NOT to do) and every routing decision stay identical; only ceremony and restated protocol shrink. Requirements:
  - **Land every verbatim-protected block from Task 1 byte-identical.** Do not paraphrase, re-order clauses within, or "improve" a protected block — copy it through untouched.
  - **Cut protocol the engine owns:** anything `orchestrator-artifacts` states (layout, naming, PASS signals, sidecar fields) becomes a link to the engine (as Step 1 already does with "layout and naming conventions are described in `orchestrator-artifacts`"), never a restatement. Follow the composition rule: a top loads the engine, never inlines it (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy").
  - **Cut procedural narration and duplicated rationale:** collapse transitional prose and remove step-narration of obvious executor actions. The only permitted dedup is the "read all rounds" mandate — trim Step 3's bare restatement to a reference to Step 1's canonical statement. **Do not touch `$TARGET_FILE`** — Step 1 and Step 4 are deliberately additive (see Task 1); leave both verbatim.
  - **Two-reader register throughout:** rules stated as intent for the executing agent; contracts pinned exact for the editor. (Spec: "rules as intent, contracts pinned exact.")
  - **Frontmatter unchanged:** `loads: orchestrator-artifacts`, `allowed-tools`, `description`, `argument-hint` all byte-identical. `≤ 500` holds trivially — the target is meaningful ceremony shrinkage, not the limit; do not pad or clamp to a line number.
  - Write in English.

- [x] **Task 3: Verify against guards** (depends on Task 2)
  Files: (read-only) `src/skills/milestone-rescue/SKILL.md`
  Confirm each spec guard before declaring done:
  - **Protected blocks byte-identical:** `git diff src/skills/milestone-rescue/SKILL.md` shows the seven Task-1 protected blocks unchanged — no hunk touches their text. Removed hunks are ceremony / protocol-restatement only. Report any protected-block edit as a failure.
  - **Protocol-restatement reduced:** the body no longer restates directory layout, `<seq>-<slug>` naming, PASS-signal semantics, or the sidecar-field list as its own prose — each such fact is either gone or a link to `orchestrator-artifacts`. Spot-check with `grep -n "plan-reviews/\|reviews/\|patches/\|PLAN_REVIEW_PASS\|REVIEW_PASS" src/skills/milestone-rescue/SKILL.md` and confirm remaining hits are load-bearing (the `step` table's artifact column, the depth-classification signal application, the plan-ratified validation contract) rather than layout restatement.
  - **Frontmatter intact:** `loads: orchestrator-artifacts` and `allowed-tools` unchanged.
  - **Every routing decision preserved:** the four depth branches, the non-convergence path, the stale-implementer path, the scope-overload flag, Step 5.5 propagation, and Step 5.6 pinning all still present and unchanged in behavior.
  - **`$TARGET_FILE` untouched:** both resolutions survive — Step 1's protected gloss (SKILL.md:57–59, incl. the "additive … does not replace it" clause) and Step 4's canonical statement (SKILL.md:183–186). Confirm no circular reference was introduced. The only permitted dedup is Step 3's "read all rounds" restatement trimmed to a Step 1 reference.
  - **Line count:** report actual; meaningful shrinkage from 477 expected, but skeleton/table mass is legal — do not pad or clamp.
  - Note for the reviewer: the spec's live baseline replay (re-run the skill on a preserved failed-milestone artifact set — or the most recent real rescue — and compare the Diagnosis Report register and rollback file set to pre-rewrite behavior) requires real failed artifacts and is user-run, not orchestrator-fabricated. Flag it as user-run; do not invent a baseline.

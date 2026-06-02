# Plan Review 3: roadmap-decompose — always emit two-tier output by invoking aif-note

**Plan:** `.ai-factory/plans/03-roadmap-decompose-always-emit-two-tier-output-by-invoking-aif-note.md`
**Risk Level:** 🟢 Low
**Verdict:** READY. Every blocking item from reviews 1 and 2 is now resolved. The single load-bearing blocker — `Skill` missing from `allowed-tools` — is fixed by the new **Task 0**, which also refreshes the stale frontmatter `description`. The per-task scoping risk (review 2 finding 2) and sequential-numbering risk (finding 4) are both folded explicitly into Task 1 step 3 and step 28. Remaining notes below are non-blocking refinements, not gates.

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): WARN — non-blocking. ARCHITECTURE.md frames skill-to-skill invocation as "runtime text instructions," and this plan introduces the first domain-skill→aif-skill *programmatic* invocation via the Skill tool. This stays consistent with the `aif` precedent (which already declares `Skill`), is confined to one skill file, and violates no module boundary. No `## Features` anchor references either skill, so no anchor conflict.
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (WARN, non-blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md` present): PASS — work is explicitly linked. The milestone "roadmap-decompose: always emit two-tier output by invoking aif-note" carries `Spec: .ai-factory/notes/13-task-decompose-two-tier-via-aif-note.md` and matches the plan's intent (contract line + per-task note via aif-note, no behavior override, no mode restructure). Plan, roadmap entry, and the referenced spec note are mutually consistent.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project-specific review overrides to apply.

## Critical Issues

None. All review-1/review-2 blockers are resolved:

- **`Skill` in `allowed-tools` (the load-bearing blocker)** — now an explicit, first-landing step: **Task 0** changes the frontmatter to add `Skill`, citing the correct precedent (`.claude/skills/aif/SKILL.md`, which I verified does declare `Skill` in its allowlist). Without this the central mechanism could be blocked or prompt mid-run; the plan now closes it.

## Other Findings (non-blocking — address during implementation)

### 1. aif-note's fixed research-note template will shape the spec, not a spec template (WARN — accepted tradeoff)

The plan (correctly, per the roadmap entry) forbids overriding aif-note's behavior. The consequence: each per-task note is forced into aif-note's research template — `# Topic` / `## Key Findings` / `## Details` / `## Open Questions` — plus aif-note's "be concise, capture findings not process" rules. That is *not* a clean implementation-spec shape (current-state → target → files/types → guards → verify). The same tension is documented elsewhere in this very repo: the `command-handoff` roadmap entry explicitly chose **not** to route through aif-note precisely because "it would reshape the handoff into its own note template and lose the skeleton." Here the opposite choice is made deliberately and is roadmap-sanctioned ("do not constrain or alter its behavior"), so it is an accepted tradeoff, not a defect — but implementers should expect the notes to read as research summaries, and the invocation prompt (Task 1 step 3) should front-load the spec fields into the content so they survive aif-note's `## Details` section. Worth one sentence in the procedure block.

### 2. Mode 2 Step 2.5 "update that note" collides with aif-note's default-create behavior (WARN)

Task 3 says: for Decompose-Existing, "if the selected milestone is already a contract line with a note, update that note rather than the line." But aif-note Rule 5 is explicit: it **always creates a new file by default** and "update an existing note only if the user explicitly asks to." So a decompose invocation that wants an update must *explicitly* instruct aif-note to update the named existing note path — otherwise aif-note will mint a fresh `<NN>` note and the old one is orphaned. The fallout is mild (aif-note declares duplicates OK, and the captured-path mechanism keeps the `Spec:` tag accurate to whichever note was written), so this is not blocking — but Task 3 should state that the update path passes an explicit "update this existing note" instruction to aif-note, or it should accept that decompose-existing always creates a new note and supersedes the old tag.

### 3. `$1` slug argument: task names need slugifying (minor)

Task 1 step 3 says "pass its task name as aif-note's `$1` slug argument." aif-note's `argument-hint` is `[topic-slug]` and Step 2 treats `$1` as a slug (lowercase, hyphens). A raw task name like "Wire Mode 1 into the two-tier procedure" is not a slug. aif-note will still derive a usable slug, but to keep the reported path predictable the invocation should pass an already-slugified task name. One word ("slugified") in the procedure removes the ambiguity. Non-blocking.

## Verified — assumptions that hold

- **`Skill` precedent confirmed.** `.claude/skills/aif/SKILL.md` `allowed-tools` includes `Skill` — Task 0's cited precedent is real.
- **The Skill tool runs aif-note in the same conversation**, so the drafted spec text is visible to aif-note — the mechanism works, and this is exactly why the per-task delimiting in step 3 matters (aif-note also sees sibling drafts). Plan mitigates correctly.
- **aif-note is invocable** — `disable-model-invocation: false`, `user-invocable: true`; `disable-model-invocation: true` on roadmap-decompose does not impair its ability to call the Skill tool.
- **aif-note writes `<NN>-<slug>.md` (no `task-` prefix) and reports the path** in Step 4 (`Note saved: …`), so "capture the reported path verbatim" is achievable and the `Spec:` tag form matches reality.
- **Sequential numbering is safe** — aif-note allocates `<NN>` by scanning for the highest `[0-9][0-9]-*.md`; Task 1 step 28 now mandates strictly sequential invocation (incl. a gate split's two notes one-after-another), preventing collisions.
- **All touchpoints accurate** — Step 1.3 + inline `# Project Roadmap` example, Steps 2.4/2.5, "Roadmap File Format", and "Critical Rules" all exist and currently carry the inline-spec instructions the plan replaces; Atomicity Gates 1.3.1/2.4.1 are correctly left intact and run before notes/contract lines.
- **File path correct** — `.claude/skills/roadmap-decompose/SKILL.md` exists; all five tasks target it; the skill is on CLAUDE.md's never-overwrite-from-upstream list, so editing it is allowed.
- **Mode 3 (`check`) correctly untouched** — it only flips `[ ]`→`[x]`, unaffected by the two-tier shape.
- **No migration** — plan correctly avoids bulk-migrating pre-existing legacy inline tasks, limiting roadmap diff churn.

## Positive Notes

- Correct dependency ordering: Task 0 (frontmatter, load-bearing) → Task 1 (shared procedure block) → Tasks 2–4 reference it, avoiding four drifting copies of the procedure.
- Review history is tracked in the plan itself, and each prior finding is mapped to a concrete task step — strong traceability.
- Char budget framed as guidance (400–1000, target ~600) rather than a hard clamp — avoids brittle output rules.
- Rationale encoded inline in the procedure block (why ~600 chars, note-is-implementation / line-is-header) — gives the implementing agent the intent, not just the mechanics.

## Recommended Action

Proceed to implementation. Optionally tighten three non-blocking points during the edit: (1) front-load spec fields in the aif-note invocation so they survive its template; (2) make Task 3's "update existing note" path pass an explicit update instruction to aif-note; (3) pass an already-slugified task name as `$1`.

PLAN_REVIEW_PASS

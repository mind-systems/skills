# The "roadmap cleanup" coupling: one dictionary in test-coverage, prune, and the rescue pair

Task 17.3 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Naming-only conformance of the maintenance flow: `roadmap-test-coverage`, `roadmap-prune`, and the two rescue skills `task-rescue` / `task-rescue-audit` (Phase 16's rename and Phase 8's Layer-5 rewrite have both landed — the ordering guards below are satisfied and this task runs freely). In all four files `milestone`/`milestones` denote the orchestrator's processed unit → **`task`(s)** (never `phase` — the orchestrator marks `[x]` at the task tier). Zero behavior change.

## Current state — per-file inventory (line numbers from the 2026-07-13 grep — **historical**: Phase 8.1 rewrote `roadmap-test-coverage`'s Layer 5 and Phase 16.1 renamed the rescue pair after that sweep, so the lists below have drifted; the grep governs, the lists orient. Re-derive with a multiline-tolerant, case-insensitive grep (`rg -U -in`) before editing — a single-line form is blind to occurrences wrapped across a line break)

**`roadmap-test-coverage` (382 lines post-Phase-8)** — prose casing `Silent-Failure` (64) → per grammatical position; note 64 is the Layer-3 `##` heading, and heading capitals are legal — judged by position the expected outcome is **no change**; do not manufacture an edit to satisfy the inventory. `milestone`/`milestones` (35, 50, 51) → `task`(s). **Leave**: `Named roadmap` (34 — casing per position, otherwise plain-conformant), "fields" (148, generic), and Layer 5's rewritten prompt (Phase 8 wrote it in registry vocabulary — certify, don't re-edit).

**`roadmap-prune` (436 lines)** — `milestone` (75) → `task`; `Milestones` heading (325) → `Tasks`; `roadmap line(s)` for the **contract line** concept (231, 276) → `contract line(s)` — 17.1 retired this variant in the two engine files (`roadmap-engine`, `orchestrator-artifacts`) and deliberately did not reach into this file; it lands here so the synonym does not outlive the direction. **Carve-out: line 155 is not the concept** — "the commit before which the prune deleted roadmap lines" means literal lines removed from the roadmap *file* at a snapshot boundary; substituting "contract lines" there would corrupt the drop-history description. Edit 231 and 276, leave 155 alone. **Leave**: `Named roadmap` (295 — casing per position), the three `## Deferred observations` occurrences (35, 42, 71 — the literal protocol heading; see Guards).

**`task-rescue` (476 lines)** — the heavy one: `spec note` → **`task spec`** (21, 28, 29, 49, 133, 134, 162, 206, 209, 238, 281, 283, 284, 299, 318, 448); every bare `milestone`/`milestones`/`Milestone` denoting the unit → **`task`(s)** — ~25 sites today, re-derive by grep; none is a `phase`. Known drift from the 2026-07-13 list: the former name self-references (2, 151, 439, 440, 476) now carry the new names and are out of this class; the `description:` field carries "checks downstream milestones" (line 8) — the always-loaded surface, in scope; the Step-5.5 template lines `→ MilestoneA:` / `→ MilestoneB:` (406–407) are illustrative placeholders, in scope; the `# Milestone Rescue` H1 (17) is prose, in scope. Also in scope: the **hyphenated attributive** `spec-note` at 269 ("the deliberate spec-note repair" → "task-spec repair") — invisible to the `spec\s+notes?` grep form (hyphen ≠ `\s`), so it needs the dedicated hyphen check in Verification. **Leave**: `contract line` (already plain-conformant, 10 places), `governing spec`/`Governing spec` prose (plain-conformant; the `Governing spec:` header tag is byte-frozen), `named roadmap` (181, 184 — casing per position), `two-tier` (27).

**`task-rescue-audit` (221 lines)** — `spec note` (192) → **`task spec`**; every bare `milestone` denoting the unit → **`task`** — ~6 sites today (4, 19, 22, 167, 193, 210), re-derive by grep; the former name self-references (2, 9, 32) now carry the new names and are out of this class; the `# Milestone Rescue Audit` H1 (19) is prose, in scope. Also in scope: the hyphenated attributive `spec-note` at 206 ("no spec-note edits" → "no task-spec edits") — same hyphen-blindness as the rescue occurrence. **Leave**: prose `deferred observation(s)` (57, 100, 217, 219 — plain-conformant), the literal `## Deferred observations` heading (58), `PASS signal` prose (40 — plain-conformant; the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals stay).

## Change

Retire the synonyms (`milestone`→`task`, `spec note`→`task spec`) and normalize the odd prose casing. Behavior byte-identical.

## Files & types

The four `SKILL.md` files. Frontmatter `name` / `loads:` / `allowed-tools` untouched; no `references/` touched. The skill renames themselves (dirs, `name:`, symlinks, cross-references) are Phase 16 (`.ai-factory/specs/71-rescue-skills-rename.md`), not this task.

## Guards

- **Ordering — satisfied.** Phase 8 (the Layer-5 friction rewrite) and Phase 16 (the rescue rename) have both landed; the same-file collisions this guard fenced are gone.
- **`milestone` → `task`, never `phase`, in all four files** — the unit is the `[x]`-marked task the orchestrator processes.
- **Protocol literals stay (cross-repo shared surface).** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` **emits** and these skills **scan** — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals. Byte-identical; a one-sided rewrite silently breaks the scan (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).
- **Tags stay legacy.** `` Spec: `` / `Governing spec:` header tags and the `.ai-factory/specs/` directory are structural — never renamed.
- **Spelling is ordinary English.** Attributive hyphens ("named-roadmap resolution order", "deferred-observations section format") and sentence-start/heading capitals stay; only mid-prose oddities (`Silent-Failure`) are normalized.
- **Generic `field`/`fields` left.**
- **Behavior baseline:** each skill runs identically pre/post — a rename that changes behavior is a bug.

## Verification

- `rg -U -in 'spec\s+notes?' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero (multiline-tolerant — a single-line grep is blind to a synonym wrapped across a line break).
- `rg -in 'spec-note' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero — the hyphenated attributive form is invisible to the `\s`-based check above; the one legitimately frozen `spec-note` lives in `orchestrator-artifacts` (17.1's file, retired by 17.5's paired change), not in these four.
- `rg -U -in '[^-]milestones?' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero.
- `grep -n 'Silent-Failure' src/skills/roadmap-test-coverage/SKILL.md` → zero mid-prose (the Layer-3 heading hit is legal — heading capitals stay).
- `grep -c '## Deferred observations' src/skills/{roadmap-prune,task-rescue-audit}/SKILL.md` → unchanged pre/post (protocol literal preserved).
- Diff each file's `loads:` line pre/post → byte-identical.
- Live: a `roadmap-prune` pass and a `/task-rescue` diagnosis run produce the same artifact shapes as their pre-conformance baselines.

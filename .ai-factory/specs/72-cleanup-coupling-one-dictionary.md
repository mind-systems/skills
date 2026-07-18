# The "roadmap cleanup" coupling: one dictionary in test-coverage, prune, and the rescue pair

Task 17.3 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Naming-only conformance of the maintenance flow: `roadmap-test-coverage`, `roadmap-prune`, and the two rescue skills (named `task-rescue` / `task-rescue-audit` once Phase 16 lands — this task runs strictly after that rename, or folds into it, to avoid a same-file collision). In all four files `milestone`/`milestones` denote the orchestrator's processed unit → **`task`(s)** (never `phase` — the orchestrator marks `[x]` at the task tier). Zero behavior change.

## Current state — per-file inventory (line numbers from the 2026-07-13 grep; re-verify by grep before editing)

**`roadmap-test-coverage` (330 lines)** — prose casing `Silent-Failure` (64) → per grammatical position (`silent-failure` attributive / `silent failure` noun); `milestone`/`milestones` (35, 50, 51) → `task`(s). **Leave**: `Named roadmap` (34 — casing per position, otherwise plain-conformant), "fields" (148, generic). **Guard: this file is also the target of Phase 8 (Layer-5 friction axis) — this pass runs strictly after Phase 8 lands, or folds into it.**

**`roadmap-prune` (436 lines)** — `milestone` (75) → `task`; `Milestones` heading (325) → `Tasks`. **Leave**: `Named roadmap` (295 — casing per position), the three `## Deferred observations` occurrences (35, 42, 71 — the literal protocol heading; see Guards).

**`task-rescue` (476 lines; `milestone-rescue` pre-Phase-16)** — the heavy one: `spec note` → **`task spec`** (21, 28, 29, 49, 133, 134, 162, 206, 209, 238, 281, 283, 284, 299, 318, 448); every bare `milestone`/`milestones`/`Milestone` denoting the unit → **`task`(s)** (2, 10, 17, 28, 50, 55, 57, 61, 63, 65, 151, 183, 189, 270, 356, 385, 389, 391, 395, 404, 407, 415, 422, 439, 440, 448, 450, 476 — verify by grep, none is a `phase`; self-references to the skill's own *name* belong to Phase 16, not here). **Leave**: `contract line` (already plain-conformant, 10 places), `governing spec`/`Governing spec` prose (plain-conformant; the `Governing spec:` header tag is byte-frozen), `named roadmap` (181, 184 — casing per position), `two-tier` (27).

**`task-rescue-audit` (221 lines; `milestone-rescue-audit` pre-Phase-16)** — `spec note` (192) → **`task spec`**; every bare `milestone` denoting the unit → **`task`** (2, 4, 9, 19, 22, 32, 167, 193, 210 — name self-references are Phase 16's). **Leave**: prose `deferred observation(s)` (57, 100, 217, 219 — plain-conformant), the literal `## Deferred observations` heading (58), `PASS signal` prose (40 — plain-conformant; the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals stay).

## Change

Retire the synonyms (`milestone`→`task`, `spec note`→`task spec`) and normalize the odd prose casing. Behavior byte-identical.

## Files & types

The four `SKILL.md` files. Frontmatter `name` / `loads:` / `allowed-tools` untouched; no `references/` touched. The skill renames themselves (dirs, `name:`, symlinks, cross-references) are Phase 16 (`.ai-factory/specs/71-rescue-skills-rename.md`), not this task.

## Guards

- **Ordering.** After Phase 8 for `roadmap-test-coverage` (same-file collision with the Layer-5 friction rewrite); after or folded into Phase 16 for the rescue pair (same files as the rename).
- **`milestone` → `task`, never `phase`, in all four files** — the unit is the `[x]`-marked task the orchestrator processes.
- **Protocol literals stay (cross-repo shared surface).** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` **emits** and these skills **scan** — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals. Byte-identical; a one-sided rewrite silently breaks the scan (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).
- **Tags stay legacy.** `` Spec: `` / `Governing spec:` header tags and the `.ai-factory/specs/` directory are structural — never renamed.
- **Spelling is ordinary English.** Attributive hyphens ("named-roadmap resolution order", "deferred-observations section format") and sentence-start/heading capitals stay; only mid-prose oddities (`Silent-Failure`) are normalized.
- **Generic `field`/`fields` left.**
- **Behavior baseline:** each skill runs identically pre/post — a rename that changes behavior is a bug.

## Verification

- `grep -in 'spec note' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero.
- `grep -inE '[^-]milestones?' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero.
- `grep -in 'Silent-Failure' src/skills/roadmap-test-coverage/SKILL.md` → zero mid-prose.
- `grep -c '## Deferred observations' src/skills/{roadmap-prune,task-rescue-audit}/SKILL.md` → unchanged pre/post (protocol literal preserved).
- Diff each file's `loads:` line pre/post → byte-identical.
- Live: a `roadmap-prune` pass and a `/task-rescue` diagnosis run produce the same artifact shapes as their pre-conformance baselines.

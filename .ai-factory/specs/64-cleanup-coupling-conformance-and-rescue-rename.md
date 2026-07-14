# The "roadmap cleanup" coupling: conform to reserved-words + rename the rescue skills

Phase 11 of the Language-integration direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Two moves in one task (one context): the vocabulary conformance of the cleanup family, and the structural rename of the two rescue skills whose names carry the retired word `milestone`.

## Part 1 — Vocabulary conformance (four files)

Rename every reserved-word token to canonical form. In all four files `milestone` / `milestones` denote the orchestrator's processed unit → **`task`(s)** (never `phase` — the orchestrator marks `[x]` at the task tier); the skill-name variants `milestone-rescue` / `milestone-rescue-audit` are handled by Part 2, not here.

**`roadmap-test-coverage` (330 lines)** — casing `Silent-Failure` (64) → `silent-failure`; `Named roadmap` (34) → `named-roadmap`; `milestone`/`milestones` (35, 50, 51) → `task`(s). `silent-failure`/`loud-failure` elsewhere already lowercase. **Leave** "fields" (148, generic). **Guard: this file is also the target of Phase 8 (Layer-5 friction axis) — this pass runs strictly after Phase 8 lands, or folds into it.**

**`roadmap-prune` (436 lines)** — `Named roadmap` (295) → `named-roadmap`; `milestone` (75) → `task`; `Milestones` heading (325) → `Tasks`. The three `## Deferred observations` occurrences (35, 42, 71) are the literal protocol heading — **leave** (see Guards); no prose occurrence to conform.

**`milestone-rescue` (476 lines → renamed dir, see Part 2)** — the heavy one: `spec note` → `task-spec` (21, 28, 29, 49, 133, 134, 162, 206, 209, 238, 281, 283, 284, 299, 318, 448); `contract line` → `contract-line` (21, 27, 30, 162, 238, 281, 283, 286, 299, 318); `two-tier` (27) already ok; `governing spec` / `Governing spec` → `governing-spec` (59, 62, 64, 131, 284, 454, 456); `named roadmap` / `Named roadmap` (181, 184) → `named-roadmap`; every bare `milestone`/`milestones`/`Milestone` denoting the unit → `task`(s) (2, 10, 17, 28, 50, 55, 57, 61, 63, 65, 151, 183, 189, 270, 356, 385, 389, 391, 395, 404, 407, 415, 422, 439, 440, 448, 450, 476 — verify by grep, none is a `phase`).

**`milestone-rescue-audit` (221 lines → renamed dir, see Part 2)** — `spec note` (192) → `task-spec`; prose `deferred observation(s)` (57, 100, 217, 219) → `deferred-observations` — **58 excluded** (the literal `## Deferred observations` protocol heading; see Guards); `PASS signal` (40) → `PASS-signal` (prose; the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals stay); every bare `milestone` denoting the unit → `task` (2, 4, 9, 19, 22, 32, 167, 193, 210).

## Part 2 — Rename the two rescue skills

`milestone` sits in two skill names; retire it there too. **`milestone-rescue` → `task-rescue`**, **`milestone-rescue-audit` → `task-rescue-audit`**. This is structural — it changes each skill's identity — so it stays inside this task by explicit decision, but its scope is deliberate.

**Live surfaces to update (skills repo only):**
- `git mv src/skills/milestone-rescue src/skills/task-rescue`; `git mv src/skills/milestone-rescue-audit src/skills/task-rescue-audit`.
- The `name:` frontmatter in each renamed `SKILL.md` → `task-rescue` / `task-rescue-audit`; all in-body self-references to the old name → the new name (5 refs in the first, 4 in the second — includes any reverse-graph / trigger prose).
- Repoint the `active/skills/` symlinks: `active/skills/milestone-rescue` → `../../src/skills/task-rescue`; `active/skills/milestone-rescue-audit` → `../../src/skills/task-rescue-audit` (rename the symlink files to match).
- `src/skills/orchestrator-artifacts/SKILL.md` — the reverse-graph marker "Loaded by milestone-rescue, milestone-rescue-audit, and roadmap-prune" → "…task-rescue, task-rescue-audit, and roadmap-prune" (2 occurrences). (roadmap-engine's reverse marker is grep-based, not a hardcoded list — it needs no edit; the grep will find `task-rescue`.)
- `docs/philosophy/skill-cycle.md` — 4 references → the new names.
- `CLAUDE.md` — 4 references (the active-set enumeration and the upstream-sync "ours, never overwritten" list) → the new names.
- `.ai-factory/ROADMAP.md` — only the **live** Phase 11 lines carry the new names (this spec and its contract line already do); the historical `[x]` task lines (1.5, 1.6.x, 5.1, …) keep `milestone-rescue` as the record of what the skill was called then.

## Files & types

The four `SKILL.md` above (two renamed); `active/skills/{milestone-rescue,milestone-rescue-audit}` symlinks; `src/skills/orchestrator-artifacts/SKILL.md`; `docs/philosophy/skill-cycle.md`; `CLAUDE.md`. `loads:` fields byte-identical (no `loads:` edge names either rescue skill — nothing loads them; they are tops).

## Guards

- **Frozen history left untouched.** Every reference under `.ai-factory/{handoffs,plans,plan-reviews,reviews,notes}` and the historical specs (25, 26, 36, 37, 45, 48, 50, 57) — and historical `[x]` ROADMAP lines — keep `milestone-rescue` / `milestone-rescue-audit`: they are archival records of a skill that was named that at the time (~130 of the 142 occurrences). Do not rewrite history.
- **The orchestrator repo is a separate handoff.** The orchestrator invokes these skills by name and consumes the whole reserved-words convention; that cross-repo work is out of this task's scope and is carried by the handoff written alongside this phase — see `.ai-factory/handoffs/` (orchestrator side).
- **`milestone` → `task`, never `phase`, in all four files** — the unit is the `[x]`-marked task the orchestrator processes.
- **Spec 62's guard is superseded for these two names.** Phase 9 (engines) leaves the `milestone-rescue` reference in `orchestrator-artifacts` as-is; Phase 11 updates it in the same pass as the rename. Order: Phase 11's rename touches `orchestrator-artifacts` after Phase 9's vocabulary pass, or the two folds are done together.
- **Tags legacy** (`` Spec: `` / `Governing spec:` / `.ai-factory/specs/`); casing lowercase kebab; behavior byte-identical (the skills invoke and run identically under the new names); generic `field`/`fields` left.
- **Protocol literals stay legacy (cross-repo shared surface).** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` **emits** and these two skills **scan** — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` PASS-signal literals. Leave them byte-identical; conform only prose that names the `deferred-observations` reserved word. A one-sided rewrite silently breaks the scan (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).

## Verification

- `grep -rIn 'milestone-rescue' src active docs/philosophy/skill-cycle.md CLAUDE.md` → zero (all live surfaces renamed; only frozen `.ai-factory` history retains it).
- `ls -l active/skills/task-rescue active/skills/task-rescue-audit` → symlinks resolve to the renamed dirs; the old symlink names are gone.
- `grep -inE '[^-]milestones?' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero.
- `grep -inE 'spec note|contract line|PASS signal|governing spec|named roadmap|Silent-Failure' src/skills/{roadmap-test-coverage,roadmap-prune,task-rescue,task-rescue-audit}/SKILL.md` → zero (`deferred observ` excluded — the literal `## Deferred observations` heading is a preserved protocol token; prose `deferred observation(s)` is caught by reading, not this grep).
- `grep -c '## Deferred observations' src/skills/{roadmap-prune,task-rescue-audit}/SKILL.md` → unchanged pre/post (protocol literal preserved).
- Invoke `/task-rescue` and `/task-rescue-audit` — they load and run identically to the pre-rename behavior; `orchestrator-artifacts`' reverse marker names the new callers.

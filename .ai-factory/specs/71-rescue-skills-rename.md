# Rename the rescue skills: milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

Phase 16. `milestone` is retired from the vocabulary ([reserved-words](../../docs/reserved-words.md) — the unit is task); skill names are machine-resolved identifiers on the fixed-form axis, so the fix is structural: the identity changes, the behavior does not. Prose inside the two bodies is **not** part of this task — the contract binds naming, not spelling, and legacy wording is corrected opportunistically at the next touch of each file; only references to the *identifier* (the skill name itself) move here.

## Scope — live surfaces to update (skills repo only)

- `git mv src/skills/milestone-rescue src/skills/task-rescue`; `git mv src/skills/milestone-rescue-audit src/skills/task-rescue-audit`.
- The `name:` frontmatter in each renamed `SKILL.md` → `task-rescue` / `task-rescue-audit`; all in-body self-references to the old name → the new name (5 refs in the first, 4 in the second — includes any reverse-graph / trigger prose).
- Repoint the `active/skills/` symlinks: `active/skills/milestone-rescue` → `../../src/skills/task-rescue`; `active/skills/milestone-rescue-audit` → `../../src/skills/task-rescue-audit` (rename the symlink files to match).
- `src/skills/orchestrator-artifacts/SKILL.md` — the reverse-graph marker "Loaded by milestone-rescue, milestone-rescue-audit, and roadmap-prune" → "…task-rescue, task-rescue-audit, and roadmap-prune" (2 occurrences). (roadmap-engine's reverse marker is grep-based, not a hardcoded list — it needs no edit; the grep will find `task-rescue`.)
- `docs/philosophy/skill-cycle.md` — 4 references → the new names.
- `CLAUDE.md` — 4 references (the active-set enumeration and the upstream-sync "ours, never overwritten" list) → the new names.
- `.ai-factory/ROADMAP.md` — only the live Phase 16 lines carry the new names (this spec and its contract line already do); historical `[x]` task lines keep `milestone-rescue` as the record of what the skill was called then.

## Files & types

The two renamed `SKILL.md` dirs; `active/skills/{milestone-rescue,milestone-rescue-audit}` symlinks; `src/skills/orchestrator-artifacts/SKILL.md`; `docs/philosophy/skill-cycle.md`; `CLAUDE.md`. `loads:` fields byte-identical (no `loads:` edge names either rescue skill — nothing loads them; they are tops).

## Guards

- **Frozen history left untouched.** Every reference under `.ai-factory/{handoffs,plans,plan-reviews,reviews,notes}` and the historical specs — and historical `[x]` ROADMAP lines — keep `milestone-rescue` / `milestone-rescue-audit`: they are archival records of a skill that was named that at the time. Do not rewrite history.
- **The orchestrator repo is a separate handoff.** The orchestrator invokes these skills by name; that cross-repo work is out of this task's scope and is carried by a handoff written alongside this task (orchestrator side).
- **Behavior identical.** The skills invoke and run identically under the new names; body prose beyond identifier self-references is untouched.
- **Protocol literals stay.** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` emits and these two skills scan — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals. This task does not touch them (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).

## Verification

- `grep -rIn 'milestone-rescue' src active docs/philosophy/skill-cycle.md CLAUDE.md` → zero (all live surfaces renamed; only frozen `.ai-factory` history retains it).
- `ls -l active/skills/task-rescue active/skills/task-rescue-audit` → symlinks resolve to the renamed dirs; the old symlink names are gone.
- Invoke `/task-rescue` and `/task-rescue-audit` — they load and run identically to the pre-rename behavior; `orchestrator-artifacts`' reverse marker names the new callers.

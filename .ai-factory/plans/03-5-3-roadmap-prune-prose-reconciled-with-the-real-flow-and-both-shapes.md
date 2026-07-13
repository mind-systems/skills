# Plan: 5.3 — roadmap-prune: prose reconciled with the real flow and both shapes

## Context
Two sentences in `src/skills/roadmap-prune/SKILL.md` describe things that don't exist — a `## Milestones` section a direction-grammar roadmap never has, and a "confirmation step" the Step 0→8 + commit-on-request flow never contains. Reword both so the prose matches the real flow and both roadmap shapes; doc-only, behavior-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Reconcile the two drifted sentences

- [x] **Task 1: Fix the Step 7 verify bullet to speak both roadmap shapes**
  Files: `src/skills/roadmap-prune/SKILL.md`
  On line 360, the last verify bullet reads `- The Milestones section still reads coherently without the pruned tasks`. Reword it to `- The task-holding sections still read coherently without the pruned tasks`. This matches Step 6 (line 323), which already enumerates both shapes ("the task-holding sections — a flat `## Milestones` list, or direction sections …"). Do not touch Step 6's flat-shape enumeration; the literal `## Milestones` there is correct and stays. The other three verify bullets are unchanged.

- [x] **Task 2: Fix the Step 1 retention sentence to name only invocation**
  Files: `src/skills/roadmap-prune/SKILL.md`
  On lines 98–99, the retention exception reads `The only exception is a `[x]` line the user explicitly names for retention — at invocation or at the confirmation step.` The flow (Step 0→8 plus the "Commit (on request only, never automatic)" section) has no discrete confirmation step. Reword so retention is named **at invocation only**, and name the pre-commit working-tree review (the run ends with all changes in the working tree before the on-request commit — Commit section, lines 380–385) explicitly as the informal second chance — never as a "confirmation step". Keep the following sentence ("Absent such an explicit instruction, prune every `[x]` task; the history is preserved in git and ARCHITECTURE.md.") intact.

### Phase 2: Verify

- [x] **Task 3: Confirm the reconciliation (depends on Tasks 1–2)**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Run `grep -n "Milestones" src/skills/roadmap-prune/SKILL.md` → only Step 6's shape enumeration remains. Run `grep -n "confirmation step" src/skills/roadmap-prune/SKILL.md` → zero results. Confirm exactly two sentences changed and behavior is otherwise byte-identical.

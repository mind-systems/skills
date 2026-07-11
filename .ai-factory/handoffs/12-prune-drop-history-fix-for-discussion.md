# Handoff — roadmap-prune drop-history fix (discuss before implementing)

## 1. Frame
`.ai-factory/notes/59-prune-drop-history-snapshot-ledger-versioned-selfheal.md` specifies a fix to `roadmap-prune`'s drop-history handling. **The user wants to discuss the design with you before it is implemented** — the fix works but has acknowledged rough edges (below). This handoff carries the what/why, the worked example that surfaced it, and the open tensions. The originating session's context isn't here — trust these files.

## 2. What note 59 asks for (the task, in brief)
Full spec is note 59; the shape:
- **Drop-history is a prune-snapshot ledger, not a bin for every dropped hash.** One hash per prune run: the **snapshot** = the last commit before that prune deletes roadmap lines. Walking the snapshots reconstructs a flat roadmap across the whole project history (`git show <snapshot>:.ai-factory/ROADMAP.md`).
- **Bug to remove:** Step 2.1's *"Internal only → hash goes to drop history"*. Internal-only tasks (refactors, proto-locks, cleanups, tests with no feature row) must write **no** hash anywhere — they already live inside the nearest prune snapshot.
- **Versioned Features header** `## Features (roadmap-prune v2)` — stamps the skill version that last built the table; doubles as the "already migrated" flag.
- **Legacy self-heal on invocation:** if the header marker is absent/older, rebuild the drop-history row from git ground truth (real prune commits by message → each commit's parent = snapshot), discard the polluting internal hashes, stamp the current version. Idempotent; touches only the drop-history row + the header.
- **Retirement:** once every consuming repo carries the current marker, the self-heal block is dead code.

## 3. Worked example — why this surfaced (the first legacy case)
A live prune on the **`tradeoxy_core`** repo produced a drop-history row of 11 hashes where only 2 relate to prunes (`20d2a0e`, `0bee791`); the other 9 are internal-task hashes the old rule dumped in. The user read the row as "11 prunes" — exactly the misreading the ledger should prevent. That repo's **real** prune commits are six: `9025621` (Remove complete plans, 03-18), `bc85388` (03-19), `20d2a0e` (Rmove complete plans, 03-20), `42f29ec` (Roadmap prune, 05-13), `2c7cc67` (05-18), `0be0279` (Roadmap prune, 07-11). Self-heal would replace the row with those six commits' parents and stamp `(roadmap-prune v2)`. **It was left un-fixed on purpose** so its next prune exercises the migration — a ready real-world test case for the implementation.

## 4. Open tensions the user wants to talk through
1. **The snapshot hash is off-by-one, by construction.** The recorded hash is the commit *before* the prune (the parent/snapshot), because the prune commit's own hash isn't knowable when `ARCHITECTURE.md` is written — the ARCHITECTURE edit and the roadmap deletion are committed **together** as one "Roadmap prune" commit. For flat-roadmap reconstruction the snapshot is exactly the right anchor, but it points one commit shy of the prune *event*, which reads like a workaround. The user sees no clean fix (recording the prune commit's own hash would need a post-commit amend — circular). Worth deciding together whether the snapshot anchor is simply accepted as correct-for-purpose, or whether a two-step (commit prune, then amend ARCHITECTURE with the now-known prune hash) is worth the ugliness.
2. **Force-push rots the whole ledger at once.** Any shared-history rewrite invalidates every hash. The user's stance: that's a repo-behavior rule (don't rewrite shared history), **out of scope** for the skill to defend against. Confirm that stance so it's a documented decision, not a silent gap.
3. **Prune detection is message-heuristic.** Self-heal finds prunes by commit message (`Roadmap prune`, `Remove complete plans`, `Rmove complete plans`). Discuss whether that set is sufficient, how to extend it, and what to do with a prune commit that used some other wording.
4. **Version scheme.** Note 59 suggests starting at **v2** (unmarked legacy = v1). Confirm the numbering and where the version constant lives in the skill.

## 5. Pointers
- Task spec: `.ai-factory/notes/59-prune-drop-history-snapshot-ledger-versioned-selfheal.md`
- Sibling fix in the same skill family (context): `.ai-factory/notes/58-prune-audit-hands-off-not-promotes.md`
- Skill to change: `src/skills/roadmap-prune/SKILL.md` — Step 2.1 (internal-only routing), Step 4.2 (Features header + drop-history write). `orchestrator-artifacts` § marker-grammar is unrelated here.

## 6. Next
Discuss the four tensions in §4 with the user; then implement note 59 (revise the note first if the discussion moves the design). `tradeoxy_core` is the standing integration test for the legacy self-heal.

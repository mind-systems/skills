# Review: agent-architect — the architect's own state survives the compact

**Plan:** `.ai-factory/plans/trickster77777/13-26-1-agent-architect-the-architect-s-own-state-survives-the-compact.md`
**Governing spec:** `.ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md`
**Changed:** `src/skills/agent-architect/SKILL.md` (one file, +76/−17; 184 → 226 lines)
**Risk Level:** 🟢 Low
**Round:** 1

## Scope of the diff

`git status` shows five staged entries: four under `.ai-factory/` (the plan, its sidecar, and the two plan-reviews — orchestrator artifacts, not reviewable code) and one source file. `git status --porcelain -- ':!.ai-factory'` returns exactly ` M src/skills/agent-architect/SKILL.md`, so the spec's one-file boundary holds with nothing extra riding along. `active/skills/agent-architect` is a symlink into `src/`, so the edit produces no second working-tree entry.

This is an instruction file, not executable code: its "runtime" is an architect rehydrating into it. There is no build, no type system, no migration surface — the failure mode is an agent reading a rule and acting on it, so contradictions between two sentences in this file are the analogue of a logic bug.

## Ground truth re-checked

Every assertion below was read off the file and the tree, not off the plan or the plan-reviews:

- **Spec verification, all five checks pass.** `grep -n "name:"` → `:2` (frontmatter) and `:57` (the `Agent` `name:` clause) — the paragraph hit exists separately from the frontmatter false positive, as required. `grep -n "ListAgents"` → `:70`, in a sentence that rules it out. `grep -n "subagents/agent-"` → `:79`, carrying the full `~/.claude/projects/<project-key>/<session-id>/` root, not the bare form. `grep -n "architect-buffer.md"` → `:207`, the path unchanged at `.ai-factory/notes/<NN>-architect-buffer.md`. `git diff --stat` shows one source file.
- **The spec's mandated order is honored** in the rewritten region: addressee (`:47-53`) → recording at spawn and at role assignment (`:55-65`) → liveness test with `ListAgents` ruled out and the meta.json fallback (`:67-83`) → the "dead" consequence (`:85-92`).
- **The "dead" consequence carries forward intact.** Report before anything is sent onward (`:85-86`), no auto-replay of an undelivered payload (`:86-87`), respawn is the next channel-message and never eager with authored prose (`:87-89`), self-contained per round (`:90-91`), losing the editor is never fatal / silently is the defect (`:91-92`). The retired two-branch definition ("a stale handle discovered at recovery, or a failed send") is gone — `grep -rn "stale handle" src/ docs/` returns nothing — and the failed send now stands alone as the signal at `:85`.
- **Round-1 plan-review issues all landed in the file.** The fallback trigger is the recovery-time state in the two-branch form (`:75-78`), not the spec's narrower "never recorded". The pairing role has its own recording moment (`:61-65`), explicitly allowed to be mid-session. `:226` names the buffer's path, not the editor's handle, with the "if one exists" hedge preserved.
- **Every guard held.** Frontmatter byte-identical — `allowed-tools` (`:13`) unchanged and still without `ListAgents`, `loads:` (`:14`) unchanged. "Spawn once, message thereafter" `:32-45`, the `::` mechanics, the two-format statement, and every other section are untouched in the diff. No second spawn path and no change to when a spawn happens — `:55` hangs the handle write on the existing spawn moment via "(see above)". No third channel-message kind is introduced as a probe. None of the retired machinery reappears: `<session-id>` occurs only inside the meta.json path and never in the buffer path, there is no directory scan to locate the buffer, no slug key, no echo-the-path step.
- **Nothing outside this file is falsified.** `grep -rn "editor's handle\|architect-buffer\|pre-compact handoff" src/ docs/ CLAUDE.md` returns hits only inside `agent-architect/SKILL.md` itself, confirming the spec's "this knowledge lives entirely in the architect's own skill and nowhere else" is still true on disk.
- **`behavior` at `:61` matches the repo's dominant spelling** (58 occurrences vs 3 of `behaviour`), so no convention drift.

## Findings

### 1. `:199-200` states the handoff carries the buffer's path "alone", contradicting `:50` where it also carries the digest — Low

`:50` says the handoff "records your buffer's path (below) **and a digest of what the editor has accumulated**". `:51-53` then scopes the exclusivity precisely: "**Of the recorded state**, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role."

The buffer section drops that scoping. `:199-200` reads, unqualified: "The handoff continuing you across a compact carries this buffer's path alone."

Read literally, the two sentences cannot both be true. The plan's Context call 1 is explicit that "alone" is scoped to buffer-held state — the handoff points at the buffer instead of copying what is in it — and the rewritten paragraph implements exactly that scoping. The buffer section was told to *mirror* that sentence and instead states the unrestricted form, so the scoping survives in one of the two places it was supposed to appear.

**Failure scenario, concrete:** an architect maintaining its buffer reads `## Your buffer is yours alone` — the section about the buffer, the natural entry point when recording the handle or a deferral entry — and writes a pre-compact handoff containing the buffer's path and nothing else, dropping the digest of what the editor has accumulated. The digest is, by `:50-51`, the architect's own recovery note; losing it costs exactly the accumulated-context recovery the paragraph exists to preserve. The dash clause at `:200-202` does point back to "Spawn once, message thereafter", which mitigates this for a reader who follows the pointer — but the sentence it qualifies is false as written, and this phase exists precisely because rules in this file that had to be inferred rather than read got filled in wrongly.

**Fix, one clause, inside the region the task already rewrites:** qualify the exclusivity the same way `:51-53` does — e.g. "…carries this buffer's path alone: of the state recorded here, the pointer, never a copy" — or drop "alone" and let the paragraph above remain the single home of the exclusivity rule. No other sentence needs to move, and every spec verification check keeps passing.

## Positive notes

- The four-paragraph split of the rewritten region reads as four distinct rules — what the handoff carries, when state is recorded, how liveness is tested, what a dead editor costs — rather than the single dense paragraph it replaced, and each is independently quotable. That is the shape a rule wants in an instruction file.
- The `ListAgents` exclusion at `:70-75` writes down the *mechanism*, not just the prohibition: the task registry, the ~minute drop-out, and the fact that a compact never touches the editor and only erases the address from the architect's own context. That is what makes the rule survive an architect who wants to reason around it, and it directly answers the incident in the spec's Defect C.
- The fallback trigger at `:75-78` closes the state the spec itself left uncovered (recorded into a buffer whose path did not reach you) without reopening the retired scan — it recovers the handle, never the buffer path. The boundary is held exactly where the plan drew it.
- The role's recording moment at `:61-65` is stated with its own timing ("which may be mid-session and need not coincide with the spawn") instead of being folded into the spawn sentence, which is the difference between a home and a mechanism.
- One-home discipline is clean elsewhere: the buffer section points at "Spawn once, message thereafter" rather than restating the liveness test, the `name:` convenience, or the fallback, and `:226` names the carrier without re-explaining it.
- `:57-61` phrases the `name:` parameter exactly as the build requires — conditional, an addressing convenience layered on the recorded handle, never the carrier and never a required step. The `Agent` schema in this build exposes no `name:`, so any stronger phrasing would have shipped an instruction that cannot be followed.

## Deferred observations

- Affects: Phase 26 / `.ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md` — `<session-id>` at `:81` is glossed as "the running session's own id" with no derivation, while `<project-key>` on the line above gets a full one and the same spec guards against resting on undocumented harness behavior. It degrades gracefully (newest-first by mtime across the project key's session directories), so it blocks nothing; it is the one placeholder in the shipped paragraph a recovering architect must resolve unaided. Carried unchanged from plan-review rounds 1 and 2.
- Affects: Phase 26 / `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — `agent-architect/SKILL.md:62` is now the second skill body naming "the deciding half" / "the applying half", and `docs/reserved-words.md` § "Paired loop" still registers only *architect* and *editor*. The same section is the natural home for *buffer* as the architect's private state file; `docs/reserved-words.md:84` currently spends the word on a named roadmap's gloss. Both are out of reach here (`docs/` is guarded untouched). Carried from plan-review round 2.
- Affects: Phase 26 / the architect's recovery route — the meta.json fallback recovers the handle but, by the retired-scan guard, never the buffer's path, so an architect recovering that way still cannot reach the buffer holding its pairing role and deferral entries and will number a fresh one. The deliberate cost of the reduced fix; the residue a later phase would price if per-session buffer identity is revisited. Carried from plan-review round 2.

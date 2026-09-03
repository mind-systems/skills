# Plan Review: agent-architect — pairing roles for two architects working together

**Plan reviewed:** `.ai-factory/plans/trickster77777/12-26-4-agent-architect-pairing-roles-for-two-architects-working-together.md`
**Governing spec:** `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md`
**Target files:** new `src/skills/architect-pairing-engine/SKILL.md`; `src/skills/agent-architect/SKILL.md` (frontmatter only); new symlink `active/skills/architect-pairing-engine`; `CLAUDE.md`
**Risk Level:** 🟡 Medium

## Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): § "Composition: mechanism vs policy" (`:30-39`) requires shared content used by two or more callers before a capability is factored out. `architect-pairing-engine` has exactly one declaring caller file (`agent-architect`), unlike its precedent `architect-editor-engine`, which has two (`agent-architect` + `src/agents/editor.md`). The spec argues the extraction on a different axis — a deployment-specific, per-session role must not be baked into the generic skill — and the two callers are the two *runtime* architects. That reasoning is sound and settled upstream of the plan; recorded as WARN, not a blocker. The plan itself introduces no boundary violation. **WARN**
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (optional file). No `.ai-factory/skill-context/aif-review/SKILL.md` either.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md:86`): task 26.4 is a live `[ ]` contract line under Phase 26 (no `Governing spec:` on the phase header), and its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md`, which exists. The plan's scope matches the contract line's four edges exactly, and the plan honours the phase's stated ordering (26.4 first, because 26.1 only gains a role to record once the roles exist). Linkage intact. **OK**

## Verification against the governing spec

Every code anchor the plan cites was checked against the live files and resolves:

- `src/skills/architect-editor-engine/SKILL.md:1-13` — the frontmatter block; `:17` — the reverse-graph sentence with the `grep -l` command. Both correct, and the precedent genuinely has no `argument-hint` and no `loads:`.
- `src/skills/agent-architect/SKILL.md:14` — `loads: architect-editor-engine`. Correct.
- `:19-28` / `:25-26` (the unpaired default and the "that hand is always the editor's" sentence), `:71-91` (the `REPORT-ONLY` before-mark relay), `:120-126` (the `APPLY-EDIT` work-order), `:128-131` (the two-format statement), `:60-140` (the `::` mechanics). All correct.
- `CLAUDE.md:74` — the `**The active set**` paragraph; `agent-architect` is the last item in the "our skills —" enumeration, directly before the "— plus one upstream original" clause, so the plan's insertion point is unambiguous. Correct.
- `active/skills/architect-editor-engine -> ../../src/skills/architect-editor-engine` — the relative symlink form the plan mirrors. Correct, and `git ls-files` confirms these symlinks are tracked.
- The pre-existing gap the plan carries forward as an explicit non-fix (`architect-editor-engine` symlinked but unnamed in the active-set paragraph) is real. `AGENTS.md` is a symlink to `CLAUDE.md`, so no second file needs the same edit.

The three-part decomposition of the new file (frontmatter + load-trigger, reverse-graph marker, the two role halves) maps cleanly onto the spec, and the plan is right that the always-loaded skill description is the *sole* load trigger given the spec pins `agent-architect` to a frontmatter-only edit — with `disable-model-invocation: false` as the enabling field. The instruction to keep deployment facts out of the file, invent no third format or marker, and write only departures from the generic discipline all match the spec's guards.

## Critical Issues

### 1. The verification step's git assertions are wrong about how git reports this change set — `Verify the four edges and the diff boundary`

The plan orders: "Then `git status` and `git diff --stat` must show exactly four things and nothing else … Anything beyond that set is out of scope and must be reverted."

Both halves misdescribe reality, and the second half is actively dangerous:

- Two of the four artifacts are **new, untracked** paths (`src/skills/architect-pairing-engine/SKILL.md` and the `active/skills/architect-pairing-engine` symlink). `git diff --stat` reports only tracked modifications, so it will show **two** entries — `CLAUDE.md` and `src/skills/agent-architect/SKILL.md` — never four. An implementer taking the assertion literally reads a correct implementation as a failed one and starts hunting for two missing files that are in fact on disk.
- `git status` shows every untracked path in the tree, which already includes the orchestrator's own artifacts. Verified on the current tree, before any implementation work: `git status` lists `.ai-factory/plans/trickster77777/12-26-4-…md` and `…json` as untracked, and by the time this step runs the plan-review and review files will be there too. Combined with "Anything beyond that set … must be reverted", the step instructs the implementer to delete the orchestrator's own plan file and sidecar.

Fix: state the check in a form that matches git's actual behaviour and excludes the orchestrator's artifact tree, e.g. `git status --porcelain -- ':!.ai-factory'` expected to be exactly `?? active/skills/architect-pairing-engine`, `?? src/skills/architect-pairing-engine/`, ` M CLAUDE.md`, ` M src/skills/agent-architect/SKILL.md` — and drop the "revert anything else" order, or narrow it explicitly to paths outside `.ai-factory/`.

### 2. The deciding half leaves the editor-spawn trigger self-contradictory — `The two role halves`

`src/skills/agent-architect/SKILL.md:34-36` defines the spawn: *"The first channel-message is the spawn — the first `::` relay or, where none has arrived, the first authored apply work-order — and its content* is *the spawn prompt."* The plan's preamble rule says anything the new skill does not name "stays exactly as the generic skill has it", and its deciding-half section is told to name only work-order **addressing** and **origination**.

So the second spawn alternative survives untouched while the pairing half removes the very message it depends on. Concrete failure: a deciding architect is assigned its role, the session runs without a single `::` relay, the user confirms an edit, and the architect authors the apply work-order. Generic `:34-36` tells it that work-order is the spawn prompt for its own editor; the pairing half tells it no `APPLY-EDIT` work-order goes to that editor and this one is addressed to the paired architect. The architect must either spawn an editor with a message it is forbidden to send, or leave the generic clause visibly unsatisfied — a fork the file does not resolve, hit on the most ordinary deciding-half session shape.

This is not a decision outside the task's authority; it is a direct consequence of the rule the spec already pins ("no `APPLY-EDIT` work-order does"), so naming it is clarification, not new policy. Fix: add one sentence to the deciding-half section stating the departure — for this half the spawn trigger is the first `::` relay alone, since the apply work-order no longer travels to the editor.

## Positive Notes
- Every line anchor in the plan resolves against the live files; the plan can be executed by anchor without re-deriving positions.
- The plan correctly identifies the non-obvious mechanism point that the spec leaves implicit: because `agent-architect` gets a frontmatter-only edit, the skill `description:` is the only thing that can ever trigger the load, which makes the description load-bearing rather than decorative — and it pins `disable-model-invocation: false` accordingly.
- Carrying the spec's `architect-editor-engine` / `CLAUDE.md` gap forward as an explicit "do not fix, do not repeat by omission" instruction is exactly right: it keeps the diff boundary clean without silently reproducing the defect for the new skill.
- The instruction to say nothing about whether the applying half relays `REPORT-ONLY` or spawns an editor at all — resolving the silence through the preamble's interpretive rule instead of inventing a rule — is disciplined and checks out: the applying half can still receive `::` relays, so generic spawn behaviour stays coherent for that half.

## Deferred observations
- Affects: Phase 26 / `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — `CLAUDE.md:189` ("**Everything else in `src/skills/` is ours** … sync never touches it: …") carries a second enumeration of our skills, parallel to the active-set paragraph at `:74`. It omits `architect-editor-engine` today and will omit `architect-pairing-engine` after this task, so the spec's flagged gap has a twin one paragraph-family over that the spec did not notice. The omission is descriptive only — `scripts/sync-upstream.sh` overwrites `upstream/ai-factory/` and never reads this list — so nothing breaks; but whoever picks up the flagged active-set gap should close both enumerations in one pass rather than leaving the second to drift further. [routed → .ai-factory/specs/trickster77777/98-claude-md-enumerations-and-engine-self-description.md]


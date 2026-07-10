# roadmap-prune: the refused gate parks into a handoff, not into the audit

## Current state

`src/skills/roadmap-prune/SKILL.md:41-42`: when the deferred-observations gate refuses, the named resolution is "run `milestone-rescue-audit` in prune mode first". That mode is removed (task 1.6.1 / spec 36): resolution now happens in a **dedicated session** the user opens from a handoff, and the parked, still-blocked prune is the deliberate waiting state — not a failure to engineer around.

## Change

Rewrite the gate-refusal message only. On refusal the prune: makes no edits, no sweep (unchanged), and names the new resolution path —

1. the user runs `/command-handoff` on this session: the handoff carries every unpinned observation (gist, original reviewer text, `Affects:`, file:line of the entry) plus the gate context into `.ai-factory/handoffs/`;
2. a **dedicated resolution session** works through the findings — fixing, routing into an **open** task's spec, or dismissing — and sets the pins per `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`);
3. `roadmap-prune` is re-run when every entry is pinned; the gate passing is the resolution's proof, never manufactured.

The prune itself never invokes the handoff and never sets pins — it reports, hints, and halts.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` — the gate-refusal message (`:41-42` region) only

## Guards

- Gate **logic** byte-identical — same scan, same refusal condition (any unpinned entry), same no-edits/no-sweep behavior; only the named resolution changes.
- Depends on 1.6.1 (spec 36): the vocabulary the message names must already exist in `orchestrator-artifacts` § 6.
- No new machinery: the prune does not call `command-handoff` itself — the hint is addressed to the user.

## Verification

- `grep -n "milestone-rescue-audit" src/skills/roadmap-prune/SKILL.md` → zero.
- The refusal message names: `/command-handoff` → resolution session → pins per `orchestrator-artifacts` → re-run.
- A gate refusal still makes zero edits (dry run on a repo with one unpinned observation).

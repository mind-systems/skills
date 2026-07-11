# Plan: 1.8.1 — roadmap-prune: the refused gate parks into a handoff

## Context
When the deferred-observations gate refuses, `roadmap-prune` currently names the removed `milestone-rescue-audit` prune mode as the resolution; rewrite that one refusal message to instead park the blocked prune and hint the user toward a `/command-handoff` → dedicated-resolution-session → re-run path. Gate logic stays byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite the refusal message

- [x] **Task 1: Replace the audit-prune-mode resolution with the handoff parking path**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 0 item 4 (the `:39-43` region), the refusal branch keeps everything it already does — print one line per unpinned entry as `<file>:<line> — <entry text>`, state that pruning is blocked until every entry is pinned, make no edits/no sweep/no ARCHITECTURE/ROADMAP changes/no partial prune. Only the *named resolution* changes: replace "run `milestone-rescue-audit` in prune mode (`milestone-rescue-audit prune`) first" with the three-step park-and-hint path from spec `.ai-factory/specs/37-prune-gate-parks-into-handoff.md`:
  1. the user runs `/command-handoff` on this session — the handoff carries every unpinned observation (gist, original reviewer text, `Affects:`, `file:line` of the entry) plus the gate context into `.ai-factory/handoffs/`;
  2. a **dedicated resolution session** works through the findings — fixing, routing into an **open** task's spec, or dismissing — and sets pins per `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`);
  3. `roadmap-prune` is re-run when every entry is pinned; the gate passing is the resolution's proof, never manufactured.
  Keep the tone as an instruction/hint addressed to the user. Do not touch items 1–3, 5, 6, the `ROADMAP_TESTS.md` parity paragraph, or any other step — the scan, the refusal condition (any unpinned entry), and the no-edits/no-sweep behavior are all unchanged.

- [x] **Task 2: Verify the guards hold** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Confirm against spec Verification: `grep -n "milestone-rescue-audit" src/skills/roadmap-prune/SKILL.md` returns zero hits; the new message explicitly names `/command-handoff` → resolution session → pins per `orchestrator-artifacts` → re-run; the prune never invokes the handoff itself and never sets pins (the hint is addressed to the user). No other region of the file changed.

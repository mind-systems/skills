# Review — 1.8.1 roadmap-prune: the refused gate parks into a handoff

## Scope
Single code change: `src/skills/roadmap-prune/SKILL.md`, Step 0 item 4 (the gate-refusal branch). The other staged files (`plans/*.json`, `plans/*.md`, `plan-reviews/*.md`) are orchestrator planning artifacts, not code.

## What changed
The named resolution in the refusal branch was replaced. Previously: "run `milestone-rescue-audit` in prune mode (`milestone-rescue-audit prune`) first". Now: a three-step park-and-hint path — (1) user runs `/command-handoff` carrying unpinned observations + gate context into `.ai-factory/handoffs/`; (2) a dedicated resolution session fixes/routes-into-an-open-task's-spec/dismisses and sets pins per `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`); (3) prune re-runs once every entry is pinned, the passing gate being the resolution's proof.

## Verification against spec `37-prune-gate-parks-into-handoff.md`

- **Gate logic byte-identical** — items 1–3 (scan + collect unpinned entries), the refusal condition ("If any unpinned entry exists → stop the skill entirely"), the per-entry print format, item 5, item 6, and the `ROADMAP_TESTS.md` parity paragraph are all untouched. Confirmed by reading the full Step 0 (lines 23–64). ✓
- **No-edits/no-sweep preserved** — "Make no edits, no sweep, no ARCHITECTURE/ROADMAP changes, no partial prune." survives verbatim, correctly relocated to the end of item 4 so it still governs the whole refusal branch. ✓
- **`grep -n "milestone-rescue-audit"` → zero hits** (exit 1). ✓
- **Message names the full path** — `/command-handoff` → resolution session → pins per `orchestrator-artifacts` § 6 → re-run. Marker vocabulary matches `orchestrator-artifacts` § 6 exactly. ✓
- **Prune invokes nothing / sets no pins** — the three steps are addressed to the user ("the user runs `/command-handoff`"; "a dedicated resolution session … sets pins"); the prune itself only reports, hints, and halts. ✓

## Runtime / correctness
This is an agent-instruction file, not executable code — no migrations, types, or races apply. The only "runtime" concern is markdown/interpretation clarity: item 4 now nests a `1./2./3.` ordered list under the parent's `1.–6.` numbering. The nesting is unambiguous — the sub-list is indented three spaces under item 4 and the trailing "Make no edits…" line closes the branch at item-4 indentation, so an agent reading it will not conflate the nested steps with the parent items. No defect.

## Findings
None. The change is faithful to the spec, minimal, and leaves gate logic intact.

REVIEW_PASS

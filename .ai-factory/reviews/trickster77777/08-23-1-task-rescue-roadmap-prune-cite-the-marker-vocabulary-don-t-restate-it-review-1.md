# Review — 23.1: task-rescue & roadmap-prune: cite the marker vocabulary, don't restate it

Scope: two skill-doc files, `src/skills/task-rescue/SKILL.md` (Step 5.6 + tail + "What NOT to do") and `src/skills/roadmap-prune/SKILL.md:65`. No code, no runtime surface — the review is against spec fidelity, the guards, and internal consistency of the marker vocabulary.

## What changed (verified against the diff)

- **task-rescue Step 5.6 disposal branches** — `[promoted → <spec path>]` → `[routed → <spec path>]`; `[audit-dismissed]` → `[dismissed]`. Both now name §6's current forms, framed as "each pinned in §6's current form," and the intro line now cites §6 for the grammar as well as the dedup rule.
- **task-rescue Step 5.6 tail (`:441-444`)** — the false attribution of `[audit-corroborated]` / `[unrouted-reported]` to `task-rescue-audit`, and "left for `task-rescue-audit` prune mode," are gone. Undisposed entries now "stay unmarked, left for the resolution session (`orchestrator-artifacts` §6) to pin later." The genuine scope limit (rescue disposes only of what it evaluates; does not corroborate against a root-cause chain or sweep the unrouted corpus) is preserved as behavior, without naming the retired literals.
- **task-rescue "What NOT to do" (`:476-479`)** — retired literals and the audit attribution dropped; rewritten to "pins only what it disposed of this session, in §6's current form — an entry it did not evaluate stays unmarked, left for the resolution session to pin."
- **roadmap-prune (`:65`)** — the inline `(`[fixed]` / `[routed → <path>]` / `[dismissed]`)` parenthetical dropped; the sub-item now cites `orchestrator-artifacts` § 6 alone, matching the citation-only posture of Step 0 item 3 (`:53-55`).

## Correctness

- **Vocabulary is now consistent with the one home.** `[routed → <spec path>]` matches §6's `[routed → <path>]`; §6 constrains `<path>` to an editable open task spec, and both of task-rescue's routed sources — a newly written task spec, or a spec repaired at Step 5 (an open, re-validated task) — satisfy that. `[dismissed]` matches §6 exactly. No stale or invented marker survives.
- **No attribution tension introduced.** §6's dedup rule already reads "whoever pins an entry pins every occurrence," so §6 admits writers beyond the resolution session; task-rescue pinning `[routed]`/`[dismissed]` at disposal time is consistent, not a contradiction. roadmap-prune's gate is purely structural (≥1 bracketed marker), so it counts task-rescue's pins identically.
- **The surviving `task-rescue-audit` reference (`:149`)** is about a shared *narrative register*, not marker-writing — correctly left in place. The verification criterion (no surviving reference attributes marker-writing to the audit skill) holds.

## Guards — all honored

- `orchestrator-artifacts/SKILL.md` and `task-rescue-audit/SKILL.md` are byte-identical to pre-task state (`git diff --stat` empty for both).
- Sidecar `step` markers (`"planned:1"` / `"implemented:1"`, `:468-471`) untouched — the different grammar was not conflated.
- roadmap-prune Step 0 item 3 gate logic (`:53-55`) untouched; only the item-4 parenthetical two paragraphs later changed.
- Register preserved in both files — targeted citation rewrites in the existing voice, no wholesale rewrite.

## Verification results

- `grep -nE "\[audit-dismissed\]|\[promoted →|\[audit-corroborated\]|\[unrouted-reported\]" src/skills/task-rescue/SKILL.md` → zero hits. ✓
- Every surviving disposal literal in task-rescue is limited to `[routed → <path>]` / `[dismissed]`. ✓
- `grep -n "task-rescue-audit" src/skills/task-rescue/SKILL.md` → one hit (`:149`), narrative-register only, no marker attribution. ✓
- roadmap-prune `:65` cites §6 without inline literals. ✓
- Guarded files unchanged. ✓

The change is faithful to the spec, complete across all three call sites, and consistent with the one home in §6. No bugs, security issues, or correctness problems.

REVIEW_PASS

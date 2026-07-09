# Plan: milestone-rescue: dismiss disposed observations in-session — not just promote

## Context
Extend spec 09's "whoever disposes pins, at the moment of disposal" invariant by one marker: let `milestone-rescue` pin `[audit-dismissed]` on observations it evaluates and finds moot/already-handled, instead of forcing a ceremonial `milestone-rescue-audit` run or a hand-written marker.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Widen the engine writer set

- [x] **Task 1: Move `[audit-dismissed]` into the disposal-tool writer set in engine §6**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Edit only the writer-set sentence at the tail of §6 (`:63-67`). Rewrite so both `[promoted → <path>]` and `[audit-dismissed]` are written by whichever disposal skill actually disposes of the observation at the moment of disposal — routing it into a task (promote) or evaluating it and finding it moot/already-handled (dismiss). Only `[audit-corroborated]` (root-cause corroboration, an audit rescue-mode judgment) and `[unrouted-reported]` (audit prune-mode sweep) remain named as `milestone-rescue-audit`'s. Keep the reviewer-never-writes-markers point. Everything else in §6 — the marker-name list (`:58-60`), append-only accumulation, "entry text and `Affects:` never rewritten", the **Pinned** definition, and the sibling dedup rule — stays **byte-identical**. Keep the `[audit-dismissed]` token verbatim (no rename). Do not touch §1–§5 or §7.

### Phase 2: Add the dismiss path to rescue

- [x] **Task 2: Broaden Step 5.6 from routing-only to disposal** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Step 5.6 (`:419-432`), generalize the routing-only wording into two disposal branches on entries encountered in the artifacts read this session: (a) **routed** into a task/spec → append `[promoted → <spec path>]` (existing); (b) **evaluated and found moot / already handled in code** (nothing to route — fix already exists, or the observation is stale/wrong) → append `[audit-dismissed]`. Both branches pin the entry **and every sibling occurrence** across that milestone's review files, citing the engine's dedup rule (`orchestrator-artifacts` §6) — do not redefine grammar / pinned-ness / dedup. **Preserve the existing on-disk scoping verbatim in intent** (`:426-430`): pin only review files still present on disk at pin time; pin at the moment of the judgment, not session end. State that rescue still does not corroborate against a root-cause chain (`[audit-corroborated]`) or sweep unrouted entries (`[unrouted-reported]`) — those stay audit's — and entries rescue never evaluated stay unmarked for audit prune mode. Keep Step 5.6 lean; rescue stays ≤500 lines.

- [x] **Task 3: Rewrite the matching "What NOT to do" clause whole** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Replace the final clause (`:464-468`) entirely — it currently bans `[audit-dismissed]`, asserts "Rescue's only marker is `[promoted → <path>]`", "do not dismiss an observation by marker", and "evaluating, dismissing, and sweeping stay `milestone-rescue-audit`'s", all now false. Use the spec's target replacement (spec 13 §2):
  > Do not write `[audit-corroborated]` or `[unrouted-reported]`, and do not mark any observation rescue did not actually evaluate this session. Rescue pins only what it disposed of — `[promoted → <path>]` for what it routes, `[audit-dismissed]` for what it evaluates and finds moot; corroborating against a root-cause chain and sweeping unrouted entries stay `milestone-rescue-audit`'s.
  Leave every other What-NOT-to-do bullet untouched.

### Phase 3: Verify caller coherence

- [x] **Task 4: Confirm audit and prune are untouched and all loaders stay coherent** (depends on Task 3)
  Files: (verification only — no edits expected)
  Re-run the engine's reverse-graph grep `grep -l "orchestrator-artifacts" src/skills/*/SKILL.md src/commands/*.md` (loaders: `milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune`) and confirm the new §6 sentence stays coherent with all three: audit still writes all four markers across its two modes; prune's pinned check is writer-agnostic so a rescue-dismissed entry counts as pinned. Run the spec's verify checks: (1) `grep -n "written by\|remain" src/skills/orchestrator-artifacts/SKILL.md` shows `[audit-dismissed]` beside `[promoted]` in the disposal writer set, only `[audit-corroborated]`/`[unrouted-reported]` named as audit's; (2) Step 5.6 has both disposal paths + dedup citation + moment-of-disposal rule, and the What-NOT-to-do clause bans only `[audit-corroborated]`/`[unrouted-reported]` (and marking unevaluated entries); (3) `git diff src/skills/milestone-rescue-audit/SKILL.md src/skills/roadmap-prune/SKILL.md` is **empty**. If any check fails, fix in the owning file (Task 1–3 scope); do not touch the audit body or prune gate.

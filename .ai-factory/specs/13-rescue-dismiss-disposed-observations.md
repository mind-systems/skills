# milestone-rescue: dismiss disposed observations in-session — not just promote

**Date:** 2026-07-09
**Source:** conversation context — live incident this session: a `/milestone-rescue` investigation of milestone 23 (`BrokerGRPCServer` / `fetchOrders`) evaluated the `Affects: note 37` deferred observation, found it **moot** (the Makefile stub-split fix already lives in code), and had to hand-write `[audit-dismissed]` on all three sibling occurrences — outside the writer set `milestone-rescue` is permitted.

## Problem today

Spec 09 legalized the invariant *"whoever disposes of an observation pins it, at the moment of disposal"* — but only for **routing**: `milestone-rescue` Step 5.6 may pin `[promoted → <path>]` when it routes an observation into a task/spec, and its "What NOT to do" clause bans the other three markers. The engine keeps the rest audit-only — `orchestrator-artifacts/SKILL.md` §6: *"the evaluative markers `[audit-corroborated]` / `[audit-dismissed]` and the sweep marker `[unrouted-reported]` remain `milestone-rescue-audit`'s."*

That leaves a real disposal that rescue performs constantly with **no legal marker**: evaluating an observation and finding it **moot / already handled in code** — nothing to route, so `[promoted]` is wrong; but it is disposed of, so leaving it unpinned is also wrong. The orchestrator is deliberately nitpicky and flags even complete tasks; the common rescue flow ends in *"commit the task, this observation needs nothing"* — the user does **not** run `milestone-rescue-audit` in that flow. Today rescue's only options are a ceremonial audit-prune run purely to stamp a dismissal, or hand-writing `[audit-dismissed]` outside the ratified writer set (which is exactly what happened with note 37). Unpinned entries left behind re-surface later and force a second investigator to re-derive the same "nothing to do" conclusion — and they block `roadmap-prune`'s gate.

The correct generalization: rescue may **dismiss** what it evaluated in-session, the same way spec 09 let it **promote** what it routes.

## The change (two files, one contract)

### 1. `src/skills/orchestrator-artifacts/SKILL.md` §6 (the writer-set statement)

Move `[audit-dismissed]` out of the audit-only clause into the disposal-tool writer set beside `[promoted → <path>]`: **`[promoted → <path>]` and `[audit-dismissed]` are written by whichever disposal skill actually disposes of the observation — at the moment of disposal (routing it into a task, or evaluating it and finding it moot/already-handled).** `[audit-corroborated]` (root-cause corroboration — a `milestone-rescue-audit` rescue-mode judgment) and `[unrouted-reported]` (the prune-mode sweep) **remain `milestone-rescue-audit`'s**. Everything else in §6 — marker names, append-only accumulation, entry text / `Affects:` never rewritten, the **pinned** definition, the sibling dedup rule — stays byte-identical.

### 2. `src/skills/milestone-rescue/SKILL.md` — Step 5.6 gains the dismiss path

Broaden Step 5.6 from routing-only to **disposal**: when a deferred-observation entry encountered in the artifacts read this session is disposed of —
- **routed** into a task/spec (existing) → append `[promoted → <spec path>]`;
- **evaluated and found moot / already handled in code** (nothing to route — the fix already exists, or the observation is stale/wrong) → append `[audit-dismissed]`;

— to the entry and to **every sibling occurrence** across that milestone's review files, per the engine's dedup rule (cite the engine; do not redefine grammar / pinned-ness / dedup). **Preserve the existing on-disk scoping** (current Step 5.6, `milestone-rescue:426-430`): pin only review files still present at pin time — a rollback may already have deleted the slug's review files, and a deleted file has nothing to pin. Pin at the moment of the judgment, not at session end. Rescue still does **not** corroborate against a root-cause chain (`[audit-corroborated]`) or sweep unrouted entries (`[unrouted-reported]`) — those stay `milestone-rescue-audit`'s. Entries rescue never evaluated stay unmarked, for audit prune mode.

Rewrite the matching "What NOT to do" clause **whole** — it is not merely a banned list; it also asserts *"Rescue's only marker is `[promoted → <path>]`"*, *"do not dismiss an observation by marker"*, and *"evaluating, dismissing, and sweeping stay `milestone-rescue-audit`'s"* (current `milestone-rescue:464-468`), all now false. Target replacement:
> Do not write `[audit-corroborated]` or `[unrouted-reported]`, and do not mark any observation rescue did not actually evaluate this session. Rescue pins only what it disposed of — `[promoted → <path>]` for what it routes, `[audit-dismissed]` for what it evaluates and finds moot; corroborating against a root-cause chain and sweeping unrouted entries stay `milestone-rescue-audit`'s.

## Guards

- **Writer-set change only** — the marker grammar (names, append-only, pinned definition, dedup) is untouched in the engine; callers cite it, never redefine it. This is spec 09's shape, extended by one marker.
- **Keep the `[audit-dismissed]` token as-is** — do not rename to `[dismissed]`: the token is a disposal verdict, not an audit-exclusive one, and "audit" is now vestigial; renaming ripples across the engine, the audit skill, and **every already-pinned entry on disk** (including live pins already committed elsewhere), invalidating them. Cheaper and safer to leave the name.
- **`milestone-rescue-audit`'s body is untouched** — loosening §6 removes no capability from the audit; it still writes all four markers in its two modes. Its prune sweep still treats any marker as pinned, so rescue-dismissed entries are skipped naturally.
- **`roadmap-prune`'s gate is untouched** — the pinned check is writer-agnostic; a rescue-dismissed entry counts as pinned and no longer blocks the gate (this is the point).
- `milestone-rescue`'s `allowed-tools` already includes `Edit` — no frontmatter change.
- The engine is load-once with three loaders (`grep -l "orchestrator-artifacts" src/skills/*/SKILL.md src/commands/*.md` → rescue, audit, prune) — re-run at implementation time and keep all three coherent with the new sentence.
- Keep Step 5.6 lean; rescue stays ≤500 lines.

## How to verify

1. `grep -n "written by\|remain" src/skills/orchestrator-artifacts/SKILL.md` → `[audit-dismissed]` sits in the disposal-tool writer set with `[promoted]`; only `[audit-corroborated]` and `[unrouted-reported]` remain named as the audit's.
2. `src/skills/milestone-rescue/SKILL.md` Step 5.6 has both disposal paths (promote-on-route, dismiss-on-moot) with the sibling-dedup citation and the moment-of-disposal rule; "What NOT to do" bans only `[audit-corroborated]` / `[unrouted-reported]` (and marking unevaluated entries), not `[audit-dismissed]`.
3. `git diff src/skills/milestone-rescue-audit/SKILL.md src/skills/roadmap-prune/SKILL.md` → empty.
4. Behavior baseline (output shape): this session's note-37 disposal — three sibling occurrences marked `[audit-dismissed]`, committed from a rescue with no audit run — is exactly the marker output Step 5.6 now produces. Caveat: that incident probed a *passed* outlier (audit-flavored territory, which `milestone-rescue-audit` already covers); the capability's primary target is the ordinary case — a rescue of a **failed** task that reads the review artifacts, routes some observations, and finds others moot. The verify holds on output shape — identical whichever disposal skill pins it (mirrors spec 09's milestone-52 baseline).

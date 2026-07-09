## Code Review — 59-milestone-rescue-dismiss-disposed-observations-in-session-not-just-promote

**Scope:** `git diff HEAD` — two skill files changed (`src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/milestone-rescue/SKILL.md`) plus new planning artifacts. These are markdown skill-instruction files (agent runtime behavior, no executable/runtime surface).

### What the change does
Extends spec 09's disposal-pinning invariant by one marker: `[audit-dismissed]` moves from audit-only into the disposal-tool writer set, and `milestone-rescue` Step 5.6 gains a dismiss branch (evaluate-and-moot → pin `[audit-dismissed]` across siblings). The What-NOT-to-do clause is rewritten to drop the `[audit-dismissed]` ban.

### Verification against spec 13 and the loader graph

**Engine §6 (`orchestrator-artifacts/SKILL.md:63-68`)** — Only the trailing writer-set sentence changed. Confirmed byte-identical (unchanged) for everything the spec freezes: the marker-name list (`:58-60`, all four markers still listed), append-only accumulation, "Entry text and `Affects:` are never rewritten", the **Pinned** = ≥1 marker definition, and the sibling dedup rule. The new sentence correctly places `[promoted → <path>]` **and** `[audit-dismissed]` in the disposal-writer set ("whichever disposal skill actually disposes…at the moment of disposal"), leaving only `[audit-corroborated]` and `[unrouted-reported]` named as `milestone-rescue-audit`'s. Matches spec 13 §1. `[audit-dismissed]` token preserved (no rename) — the ripple guard holds. §1–§5 and §7 untouched.

**Step 5.6 (`milestone-rescue/SKILL.md:419-441`)** — Generalized from routing-only to two disposal branches (Routed → `[promoted → <spec path>]`; Evaluated-and-moot → `[audit-dismissed]`). The engine dedup citation, the on-disk scoping (pin only review files present at pin time; the spec/spec+plan vs spec+plan+code/plan-ratified deletion caveat), and the moment-of-disposal rule are all preserved. It correctly reaffirms that rescue still does not write `[audit-corroborated]` / `[unrouted-reported]`, and unevaluated entries stay unmarked for audit prune mode. Matches spec 13 §2.

**What-NOT-to-do (`milestone-rescue/SKILL.md:473-477`)** — Rewritten whole; text matches spec 13 §2's target replacement verbatim (bar the trailing period, consistent with the surrounding bullet style). The now-false assertions ("Rescue's only marker is `[promoted]`", "do not dismiss an observation by marker", "evaluating, dismissing…stay audit's") are gone. Every other bullet is untouched.

### Coherence across the three loaders (`grep -l "orchestrator-artifacts"` → rescue, audit, prune)

- **`milestone-rescue-audit` untouched and still valid** — not in the changed-file set. Its `[audit-dismissed]` references (`:145,272,288,300-301,335`) describe what the audit itself writes in its two modes ("the only writes *either one* ever performs are these two", scoped to that skill) — never a claim that *only* the audit may write the marker. Widening §6 introduces no stale or contradicted reference; the audit still writes all four markers in its two modes.
- **`roadmap-prune` untouched and writer-agnostic** — its gate defines pinned as "the entry line carries ≥1 bracketed status marker" (`:37-38`), so a rescue-dismissed entry counts as pinned and no longer blocks the prune gate. This is the intended effect, achieved without editing prune.

### Runtime / breakage analysis
No executable code, no migrations, no types, no config. The only "runtime" is agent instruction-following. Risks considered and cleared:
- **Contradictory instructions across the load-once engine and its callers** — none; the three loaders are mutually consistent (checked above).
- **Line budget** — `milestone-rescue` is 477 lines, under the ≤500 ceiling.
- **Frontmatter/tooling** — `milestone-rescue` `allowed-tools` already includes `Edit`; no new skill, so no `active/` symlink or CLAUDE.md active-set change needed. Correctly untouched.
- **Byte-identical guards** — Task 4's `git diff` on audit + prune is empty (neither file modified).

No findings.

REVIEW_PASS

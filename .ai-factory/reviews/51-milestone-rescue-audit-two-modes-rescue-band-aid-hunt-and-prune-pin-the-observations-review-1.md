## Code Review — milestone-rescue-audit: two modes (rescue / prune)

**Files reviewed:** `src/skills/milestone-rescue-audit/SKILL.md` (only code/behavior change in the diff; the rest of `git status` is planning artifacts — plan, plan-reviews, sidecar).

The edit is a prose behavior spec for an agent skill, so "runtime bugs" here are internal contradictions and instructions that steer the model wrong. The spec mapping (Edits 1–4 + Constraints + What-NOT-to-do) is faithful and complete; the two findings below are inconsistencies the plan did not cover.

---

### Findings

**1. (Medium) Frontmatter `description` still says "to chat only (no file writes)" — now false, and it omits prune mode entirely.**
Lines 8–9: *"Emits a diagnosis plus one upstream recommendation to chat only (no file writes, no ROADMAP edits). Run right after `milestone-rescue` while artifacts are warm, or cold on any looped/outlier task."*

The whole point of this milestone is that the skill now **does** write: rescue mode appends `[audit-corroborated]`/`[audit-dismissed]` markers (lines 134–140), and prune mode appends markers plus promotion blocks into `Affects:`-target files (Prune mode + Write contract, lines 246–299). The body was correctly updated — Step 6 line 197 now reads *"Beyond the status-suffix marks in the Write contract below, no files are written"* — but the frontmatter `description` was left with the old "no file writes" claim, directly contradicting the body.

This matters more than a stale comment: the `description` is the text the agent loads to decide *when and how* to invoke the skill. It advertises a chat-only, single-mode audit and says nothing about the new `prune` mode or that the skill is now the resolver for `roadmap-prune`'s refused gate. A model routing on the description will never reach for prune mode, and may believe writes are out of contract.
*Fix:* reword the parenthetical to reflect the real write contract (append-only status marks + prune-mode promotion appends; no ROADMAP edits, no content rewrites) and add a clause naming the two modes / the prune-gate trigger, so skill selection can route to it. Spec Edit 1 changes the frontmatter (argument-hint, loads) but the description's accuracy is a direct consequence of Edit 4 granting writes.

**2. (Low) `$1` dispatch has no defined behavior when the argument is present but is neither `rescue` nor `prune`.**
Line 28: *"`$1` selects the mode: `rescue` (default when `$1` is absent) or `prune`."* Only two cases are defined — `$1` absent → rescue, `$1` == `prune` → prune. Nothing covers `$1` holding some other token.

This is a live path, not hypothetical: the historic cold invocation passed the **task slug** as the first argument, and the trigger phrases ("audit", "band-aid check") plus the description's "cold on any looped/outlier task" invite natural-language invocation where `$1` arrives as free text (e.g. `audit the foo-task`). Under the current wording that value is neither "absent" nor `prune`, so mode selection is undefined — and the new cold-rescue slug channel is `$2` (lines 48–51), leaving a bare-slug-in-`$1` invocation unhandled.
*Fix:* make the dispatch total — e.g. "`$1` == `prune` → prune; anything else (absent, `rescue`, or a bare slug) → rescue, and a non-`rescue` first token is taken as the cold-rescue slug (the `$2` role)." That preserves spec Edit 1's `$1 ∈ rescue|prune` while gracefully absorbing the historic and natural-language forms.

---

### Verified correct
- Frontmatter mechanics: `argument-hint` → `"[rescue|prune]"`, `loads: orchestrator-artifacts` added, `allowed-tools` gains `Edit` and does **not** add `Write` (append-only markers + appends into existing files are expressible via `Edit`) — matches spec Edit 4.
- Inputs rewrite states each mode's inputs directly and the "see `milestone-rescue` for layout" pointer is deleted, replaced by the engine reference (Edit 1). Cold-rescue `$2` slug affordance present.
- Rescue mode: deferred observations excluded from chain / round count / severity trend, captured separately, `audit-*`-marked entries skipped as pre-evaluated (Step 1). Corroboration is explicitly non-decisive and never replaces the one-sentence test; absence of a match carries no weight (Step 3). Marking only on actually-evaluated entries, siblings marked via the engine dedup rule.
- Prune mode: full-dir scan of both review genres, dedup by `Affects:`+gist, evaluate → dismiss/promote/unroute, no route-guessing, every sibling marked, exit at zero unpinned, summary with per-marker counts + unrouted list. Matches Edit 3.
- Write contract and What-NOT-to-do enumerate exactly the two permitted append writes and forbid content rewrites / roadmap touches / marking un-evaluated entries. The engine's marker grammar and dedup rule are referenced, never redefined.
- Rescue pipeline (Steps 2–6), one-sentence test, discriminators, and "default is NOT band-aid" are unchanged.

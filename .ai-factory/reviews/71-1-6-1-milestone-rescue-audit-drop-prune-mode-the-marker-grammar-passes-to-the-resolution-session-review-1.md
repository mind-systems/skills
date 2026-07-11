# Review — 1.6.1 milestone-rescue-audit: drop prune mode; grammar to the resolution session

## Scope
Two files changed: `src/skills/milestone-rescue-audit/SKILL.md` and `src/skills/orchestrator-artifacts/SKILL.md`. Reviewed both in full against spec 36 and the plan. (The other tracked changes — `CLAUDE.md`, `docs/skill-pyramid.md`, `.ai-factory/plans/*`, `plan-reviews/*` — are prior-work/plan artifacts, not this task's code surface.)

## Verification against the spec's acceptance criteria

1. **Body grep clean.** `grep -n -i "prune\|promote\|marker\|\[audit-" src/skills/milestone-rescue-audit/SKILL.md` → **zero matches over the whole file** (body *and* frontmatter). Frontmatter description names the invoke-on-smell trigger ("or in any session, on smell, when you suspect the orchestrator stuck crutches around crooked architecture or spaghetti code"). ✓
2. **No write path in the audit.** `allowed-tools` dropped `Edit` → `Read Glob Grep Bash(git *)` (read-only). The only `Write`/`Edit` tokens left in the body are prose ("write **one sentence**", "Write no file, ever") — not tool invocations. Prune mode, the Write contract, and Step 3's marking paragraph are all deleted; Step 3's chat-only corroboration paragraph is preserved. ✓
3. **§ 6 repointed.** Lists `[fixed]` / `[routed → <path>]` (path must be an open task's spec, editable surface) / `[dismissed]`, names the resolution session as the writer, and keeps the legacy-markers-count-as-pinned sentence. Append-only, the dedup rule, and "**Pinned** = the entry line carries ≥1 marker" are preserved verbatim. ✓
4. **Engine edit confined to § 6.** The single diff hunk touches only § 6 body; §§ 1–5, 7 are byte-identical (the `@@ -55,18` context line is § 5's unchanged trailing line). ✓
5. **`roadmap-prune`'s gate still computes "pinned" correctly.** The gate cites the engine's "≥1 marker" definition (`roadmap-prune/SKILL.md:37`), which is unchanged, and legacy markers still count — so blocked/unblocked behavior is preserved for both new and legacy pins. ✓

No orphaned references remain in the audit: greps for `$2`, "Run mode", "Write contract", "both modes / either mode", "rescue mode", "prune mode" all return zero. The analysis pipeline (Steps 1–6, discriminators, verdict spectrum, narrative register) is untouched, as the spec required.

## Findings
None blocking. The code changes are correct and complete for the task's two-file scope.

## Deferred observations
- Affects: `src/skills/milestone-rescue/SKILL.md` (Step 5.6, lines ~412–433, 465–469) — `milestone-rescue` still writes `[promoted → <spec path>]` / `[audit-dismissed]` at in-session disposal and, at line ~431–433, still points readers to "`milestone-rescue-audit` prune mode" for `[audit-corroborated]`/`[unrouted-reported]` and unrouted entries — a mode this change deletes. After the § 6 rewrite those tokens are *legacy/retired*, and the referenced prune mode no longer exists, so `milestone-rescue`'s § 6 citation and its Step 5.6 writer-set now drift from the engine. This is **not a runtime break** — legacy markers still satisfy "pinned = ≥1 marker", so the prune gate is unaffected — and it is **explicitly out of scope** per the plan's Context ("reconciling `milestone-rescue`'s writer set to the new vocabulary belongs to a later milestone") and spec 36's two-file boundary. Flagging so the reconciliation is tracked, not lost.

REVIEW_PASS

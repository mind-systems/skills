# task-rescue & roadmap-prune: cite the marker vocabulary, don't restate it

A session investigation (triggered while pinning a deferred observation on task 22.1) found the deferred-observation status-marker grammar — defined once, correctly, in `orchestrator-artifacts` §6 — is restated instead of cited at two call sites, and one of those restatements is actively wrong: `task-rescue/SKILL.md` hardcodes the RETIRED marker forms as live write-instructions, and separately attributes marker-writing responsibility to `task-rescue-audit` for a capability that skill doesn't have. This is the same "restate instead of cite" drift shape as the triplicated `APPLY-EDIT` mechanics the paired-loop cleanup (Phase 22, 22.2) just removed from the channel-message engine — a shared fact copied into a caller instead of referenced, going stale the moment its one home changes.

This task touches **two files** — `src/skills/task-rescue/SKILL.md` and `src/skills/roadmap-prune/SKILL.md` — as one task: both fixes are the identical underlying defect (a caller restating §6's literal markers instead of citing them), recurring at two call sites, one of them incidental and low-severity. `orchestrator-artifacts/SKILL.md` and `task-rescue-audit/SKILL.md` are untouched.

## Current state (grounded, verified live today)

**`src/skills/orchestrator-artifacts/SKILL.md` §6 (`:59-77`)** — the one home, unchanged by this task. Current active vocabulary: `[fixed]` (`:65`), `[routed → <path>]` (`:66-67`), `[dismissed]` (`:68`). Legacy/retired: `[promoted → <path>]`, `[audit-corroborated]`, `[audit-dismissed]`, `[unrouted-reported]` (`:75-77`) — "retired from the active vocabulary; encountered in old repos they still count as pinned (lazy migration — history is never rewritten)." "Pinned" is defined structurally (`:71`, "the entry line carries ≥1 marker"), not by a literal whitelist — this is why `roadmap-prune`'s actual gate logic (below) is not itself broken by the drift.

**`src/skills/task-rescue/SKILL.md`** — two defects, both inside the file, no dependency on `roadmap-prune`:
- **Step 5.6 (`:422-443`)** — the two disposal branches: `:429-430` "Routed — ... append `[promoted → <spec path>]`"; `:431-432` "Evaluated and found moot / already handled in code — ... append `[audit-dismissed]`." Both are retired forms, written as the live instruction. `:440-443` further states: "Rescue still does not corroborate a finding against a root-cause chain (`[audit-corroborated]`) or sweep unrouted entries (`[unrouted-reported]`) — those stay `task-rescue-audit`'s. Entries rescue never evaluated this session stay unmarked, left for `task-rescue-audit` prune mode."
- **"What NOT to do" (`:447-479`)** — `:475-479`: "Do not write `[audit-corroborated]` or `[unrouted-reported]`, and do not mark any observation rescue did not actually evaluate this session. Rescue pins only what it disposed of — `[promoted → <path>]` for what it routes, `[audit-dismissed]` for what it evaluates and finds moot; corroborating against a root-cause chain and sweeping unrouted entries stay `task-rescue-audit`'s." Restates both retired forms again and repeats the audit attribution.
- The attribution is dead: `src/skills/task-rescue-audit/SKILL.md` is chat-only by its own explicit design — `:204-205` "Write no file, ever — no patches, no task-spec edits, no ROADMAP changes, no rewriting plan or review file content"; `:161` "## Step 6 — Output (to chat only)". Verified live: `grep` for every marker literal (`audit-dismissed`, `audit-corroborated`, `unrouted-reported`, `promoted →`, `[fixed]`, `[routed`, `[dismissed]`) across `task-rescue-audit/SKILL.md` returns zero hits — it neither writes, cites, nor mentions any of them.
- The only entity currently shown setting pins is the **resolution session** — `src/skills/roadmap-prune/SKILL.md:63-66`: "a dedicated resolution session works through the findings — fixing, routing into an open task's spec, or dismissing — and sets pins per `orchestrator-artifacts` § 6."

**`src/skills/roadmap-prune/SKILL.md`** — one low-severity echo, in prose only, not in gate logic:
- Step 0 item 3 (`:53-55`) — the actual gate logic, already correct: "Collect every entry line that is **not pinned** per the engine's grammar (pinned = the entry line carries ≥1 bracketed status marker — do not redefine, cite the engine)." No literal markers named here; this is the pattern to match.
- Step 0 item 4, sub-item 2 (`:63-66`) — the resolution-session description: "...and sets pins per `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`)." The parenthetical restates the three current literals inline — harmless today, but the same shape of duplication that would go stale if §6's vocabulary changes again.

## The change

**1. `task-rescue/SKILL.md` — cite §6 instead of listing literals; drop the false audit attribution.**
Rewrite Step 5.6's two disposal branches (`:429-432`) to describe "routed" and "dismissed" generically against `orchestrator-artifacts` §6's current vocabulary, by citation, the same way Step 0 item 3 in `roadmap-prune` already does for its gate ("do not redefine, cite the engine") — do not name the literal bracket strings as the instruction itself. Rewrite `:440-443` and the "What NOT to do" entry `:475-479` to drop the attribution of `[audit-corroborated]` / `[unrouted-reported]` to `task-rescue-audit` entirely (user-ruled resolution: option 2, no new capability for the audit skill) — describe entries `task-rescue` does not itself dispose of this session as simply **left unmarked**, for the resolution session to pin later (the only entity `roadmap-prune` shows doing this today). Do not invent or reference any marker-writing role for `task-rescue-audit`.

**2. `roadmap-prune/SKILL.md:65-66` — cite instead of listing literals.**
Rewrite the resolution-session parenthetical to cite `orchestrator-artifacts` §6 without re-listing the three literal markers inline — matching the citation-only posture Step 0 item 3 (`:53-55`) already uses two paragraphs earlier in the same file. This is the minor, low-severity half of the fix, folded in to complete "one protocol": every caller that mentions the vocabulary cites it, none restate it.

## Files & types

- edit: `src/skills/task-rescue/SKILL.md` — Step 5.6 and "What NOT to do."
- edit: `src/skills/roadmap-prune/SKILL.md:65-66` only.

## Guards

- `src/skills/orchestrator-artifacts/SKILL.md` §6 is **untouched** — it stays the one home and **keeps both the current and the legacy/retired marker lists**. The legacy list is deliberate, not dead weight: current roadmaps may carry mixed pins from before this fix, and `roadmap-prune`'s generic "≥1 bracketed marker" gate must keep counting them as pinned. Removable only once every roadmap has re-iterated through the new vocabulary — not this task, not now.
- `src/skills/task-rescue-audit/SKILL.md` is **untouched** — it is chat-only and correctly holds no marker vocabulary of its own; this task gives it no new surface, no marker-writing capability, nothing.
- The sidecar `step` markers (`planned:N` / `implemented:N`, `orchestrator-artifacts` §3, fixed separately in Phase 21) are a **different grammar** — out of scope, not to be touched or conflated with the deferred-observation status markers (§6) this task fixes.
- `roadmap-prune`'s actual gate logic (Step 0 item 3, `:53-55`) is not touched beyond this citation cleanup — it was already correct and vocabulary-agnostic; this task does not change its behavior, only removes a stale-prone echo two items later in the same Step.
- Preserve register in both files — targeted citation-based rewrites of the existing voice, not a wholesale rewrite of either skill.

## Verification

- `grep -nE "\[audit-dismissed\]|\[promoted →|\[audit-corroborated\]|\[unrouted-reported\]" src/skills/task-rescue/SKILL.md` → zero hits (the retired forms no longer appear as write-instructions anywhere in the file).
- `task-rescue/SKILL.md` cites `orchestrator-artifacts` §6 for its disposal markers; any literal it still names is limited to the current `[routed → <path>]` / `[dismissed]`.
- `grep -n "task-rescue-audit" src/skills/task-rescue/SKILL.md` — if any reference survives, it no longer attributes marker-writing responsibility to it.
- `roadmap-prune/SKILL.md:65-66` no longer lists the three literals inline; it cites §6 the same way `:53-55` already does.
- `src/skills/orchestrator-artifacts/SKILL.md` and `src/skills/task-rescue-audit/SKILL.md` are byte-identical to their pre-task state (`git diff` shows no changes to either).

# Plan: task-rescue & roadmap-prune: cite the marker vocabulary, don't restate it

## Context
`task-rescue` and `roadmap-prune` restate the deferred-observation status-marker vocabulary whose one home is `orchestrator-artifacts` §6 — one restatement (`task-rescue` Step 5.6) is actively wrong, naming retired markers as live write-instructions and falsely attributing marker-writing to the chat-only `task-rescue-audit`. This task rewrites the three call sites to cite §6 instead of listing literals, leaving §6 and `task-rescue-audit` untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: task-rescue — cite §6, drop the false audit attribution

- [x] **Task 1: Rewrite Step 5.6's two disposal branches to cite §6's current vocabulary**
  Files: `src/skills/task-rescue/SKILL.md` (Step 5.6, `:429-432`)
  The two disposal branches currently name retired literals as the instruction: "Routed — ... append `[promoted → <spec path>]`" and "Evaluated and found moot / already handled in code — ... append `[audit-dismissed]`." Rewrite both to describe the "routed" and "dismissed" dispositions generically and pin per `orchestrator-artifacts` §6's current vocabulary **by citation** — mirroring the posture Step 0 item 3 in `roadmap-prune/SKILL.md:53-55` already uses ("do not redefine, cite the engine"). Do not name the retired bracket strings as the instruction. Any literal that survives must be limited to §6's current forms `[routed → <path>]` / `[dismissed]`. The disposal-branch semantics (routed = new task+spec or fold into a Step-5-repaired spec; dismissed = fix already exists / observation stale or wrong) are preserved — only the marker naming changes to citation.

- [x] **Task 2: Rewrite the `:440-443` tail — drop the retired-marker + audit attribution**
  Files: `src/skills/task-rescue/SKILL.md` (Step 5.6 tail, `:440-443`)
  The current paragraph attributes `[audit-corroborated]` / `[unrouted-reported]` to `task-rescue-audit` as its responsibility to write, and says undisposed entries are "left for `task-rescue-audit` prune mode." Per spec (user-ruled resolution option 2: no new capability for the audit skill), remove the audit attribution entirely — `task-rescue-audit` is chat-only and writes no files. Rewrite so that entries `task-rescue` does not itself dispose of this session are simply **left unmarked**, for the resolution session to pin later (the only entity `roadmap-prune` shows setting pins). Do not invent or reference any marker-writing role for `task-rescue-audit`. Preserve the surrounding register — a targeted rewrite of this paragraph, not a rewrite of Step 5.6.

- [x] **Task 3: Rewrite the "What NOT to do" entry `:475-479` the same way** (depends on Task 2)
  Files: `src/skills/task-rescue/SKILL.md` ("What NOT to do", `:475-479`)
  This entry restates the retired forms again ("Do not write `[audit-corroborated]` or `[unrouted-reported]` ... Rescue pins only what it disposed of — `[promoted → <path>]` ..., `[audit-dismissed]` ...; corroborating ... stay `task-rescue-audit`'s"). Rewrite it consistently with Task 1 and Task 2: express the "do not mark what rescue did not evaluate this session" constraint without naming retired literals, and without attributing any marker to `task-rescue-audit`. Describe rescue as pinning only what it disposed of (per §6, by citation) and undisposed entries as left unmarked for the resolution session. Keep it phrased as a single "What NOT to do" bullet in the existing voice.

### Phase 2: roadmap-prune — cite instead of listing literals

- [x] **Task 4: Rewrite the resolution-session parenthetical to cite §6**
  Files: `src/skills/roadmap-prune/SKILL.md` (Step 0 item 4, sub-item 2, `:65-66`)
  The sub-item currently reads "...and sets pins per `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`)." Remove the inline re-listing of the three literals so it cites §6 only — matching the citation-only posture Step 0 item 3 (`:53-55`) already uses two paragraphs earlier in the same file. The reference to `orchestrator-artifacts` § 6 stays; only the parenthetical literal list is dropped. Gate logic (item 3) is not touched.

## Guards (apply to every task)

- `src/skills/orchestrator-artifacts/SKILL.md` §6 stays **byte-identical** — it is the one home and deliberately keeps both the current and the legacy/retired marker lists (mixed-vocabulary roadmaps still need the retired forms recognized as pinned).
- `src/skills/task-rescue-audit/SKILL.md` stays **byte-identical** — it is chat-only and holds no marker vocabulary; give it no new surface.
- The sidecar `step` markers (`planned:N` / `implemented:N`, §3) are a different grammar and out of scope — do not touch or conflate them with the §6 deferred-observation markers.
- `roadmap-prune` Step 0 item 3 gate logic (`:53-55`) is not changed beyond leaving it as the citation template — its behavior is already correct and vocabulary-agnostic.
- Preserve register in both files: targeted citation-based rewrites of the existing voice, not a wholesale rewrite of either skill.

## Verification

- `grep -nE "\[audit-dismissed\]|\[promoted →|\[audit-corroborated\]|\[unrouted-reported\]" src/skills/task-rescue/SKILL.md` → zero hits.
- `task-rescue/SKILL.md` cites `orchestrator-artifacts` §6 for its disposal markers; any surviving literal is limited to `[routed → <path>]` / `[dismissed]`.
- `grep -n "task-rescue-audit" src/skills/task-rescue/SKILL.md` → any surviving reference no longer attributes marker-writing responsibility to it.
- `roadmap-prune/SKILL.md:65-66` no longer lists the three literals inline; it cites §6 the way `:53-55` does.
- `git diff` shows no changes to `orchestrator-artifacts/SKILL.md` or `task-rescue-audit/SKILL.md`.

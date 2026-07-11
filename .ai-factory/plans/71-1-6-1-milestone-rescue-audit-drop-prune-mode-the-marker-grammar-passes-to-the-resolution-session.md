# Plan: 1.6.1 — milestone-rescue-audit: drop prune mode; the marker grammar passes to the resolution session

## Context
Delete `milestone-rescue-audit`'s `prune` mode whole (dispatch, disposal, promote, and every file-writing step — including `rescue` mode's status-mark appends) so the audit becomes a single-mode, chat-only band-aid hunter that writes nothing, ever; and rewrite `orchestrator-artifacts` § 6 so the disposal actor is the resolution session with the vocabulary `[fixed]` / `[routed → <path>]` / `[dismissed]`, legacy markers still counting as pinned.

Assumptions / out-of-scope seams (per the spec's explicit two-file boundary):
- **`milestone-rescue` is NOT touched.** It still writes `[promoted → <spec path>]` / `[audit-dismissed]` at in-session disposal (specs 09/13). After this task those tokens are *retired-but-still-pinned* legacy markers per the new § 6; reconciling `milestone-rescue`'s writer set to the new vocabulary belongs to a later milestone, not here.
- **`roadmap-prune/SKILL.md:41-42` still names "`milestone-rescue-audit` in prune mode" as the gate's resolution.** That stale pointer is task **1.8.1**'s explicit subject (spec 37) — leave it; do not fix it here.
- The audit's analysis pipeline (one-sentence root-cause test decisive, discriminators corroborative-only, "default is NOT band-aid", healthy-convergence early-exit, prose-narrative register) is **not** compressed here — that is task 1.6.2. This task only removes the prune half, removes all writes, and adjusts frontmatter.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Slim the audit and repoint the grammar

- [x] **Task 1: Delete prune mode + all writes from `milestone-rescue-audit`; rewrite frontmatter**
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Make the skill single-mode and read-only. Do NOT compress or reword the surviving analysis pipeline beyond what the removals below force.

  Frontmatter:
  - `description`: rewrite to describe one mode only — the outside-view band-aid/convergence audit. Drop all prune wording and the two prune trigger phrases (`"prune gate blocked"`, `"pin deferred observations"`). Add the **invoke-on-smell** trigger: runnable after `milestone-rescue` on a looped/outlier milestone **or in any session** when the user suspects the orchestrator stuck crutches around crooked architecture / spaghetti code. Ensure the description text itself contains none of the substrings `prune`, `promote`, `marker`, `[audit-`.
  - `allowed-tools`: make read-only — drop `Edit`. Result: `Read Glob Grep Bash(git *)`.
  - `argument-hint`: change from `"[rescue|prune]"` to `"[task-slug]"` (only the optional cold-run slug remains).
  - Keep `loads: orchestrator-artifacts`.

  Body — remove the prune half and every write path so the file body contains **zero** occurrences (case-insensitive) of the substrings `prune`, `promote`, `marker`, `[audit-` (this also forbids naming the skill `roadmap-prune` in prose — reword any such reference to not name it):
  - `## Run mode` (the `$1` mode-dispatch block): delete the two-mode dispatch and the per-mode bullets. Keep the "Ensure `orchestrator-artifacts` is loaded once this chat" instruction (relocate it), reworded to drop "status-marker grammar both modes rely on" — say it defines the artifact layout, naming, rounds, signals, and the deferred-observations section format this audit relies on.
  - `## Inputs`: delete the `prune` mode input paragraph and the `$1`/`$2` two-mode dispatch complexity. Keep the single-task input description (plan, all plan-reviews, implementation diffs/patches, code-reviews, final state) and the cold-run path (optional slug as `$1`; else identify from prose + `Glob` over `plan-reviews/`/`reviews/`).
  - Step 1 deferred-observations capture (currently the paragraph referencing skipping entries that already carry an `audit-*` marker): keep the capture-as-scratch behavior (round, `Affects:` target, one-line gist; excluded from the finding→fix chain/round count/severity trend as non-findings), but reword to remove the words `marker`/`audit-*`. Drop the "skip already-marked" optimization (the audit no longer writes marks, so there is nothing of its own to skip).
  - Step 3: delete the entire marking paragraph (the one instructing to append `[audit-corroborated]`/`[audit-dismissed]` via `Edit` to every sibling occurrence). **Keep** the preceding corroboration paragraph ("Corroboration from captured deferred observations" — check captured observations against the root-cause sentence, name matches in the narrative, corroborative-only) — it is chat-only and contains no banned substrings.
  - Step 6: keep the chat-only narrative deliverable intact. Reword its opening ("Beyond the status-suffix marks in the Write contract below, no files are written…") to simply state no files are written and the ROADMAP is never edited.
  - `## Prune mode — pin every deferred observation`: delete the whole section.
  - `## Write contract`: delete the whole section (the audit now writes nothing).
  - `## What NOT to do`: delete the prune/marker/promote bullets (route-guessing, "do not redefine the marker grammar", "do not mark an observation `[audit-*]`", the prune-mode qualifiers). Reword the "do not write any file beyond the Write contract" bullet to "produce only a chat diagnosis, write no file"; reword the "do not touch the roadmap … that is `roadmap-prune`'s job" bullet to drop the skill name (e.g. "sweeping/deleting the roadmap is not this skill's job"). Keep every analysis-discipline bullet (single-sentence-test gate, judge the sequence not the fix, both outcomes valid, deferred obs are non-findings, corroboration never replaces the test).

  Verify: `grep -n -i "prune\|promote\|marker\|\[audit-" src/skills/milestone-rescue-audit/SKILL.md` returns matches only inside the frontmatter? No — target zero in the body; the `description` must also avoid these substrings. Confirm no `Write`/`Edit` verb remains anywhere in the body.

- [x] **Task 2: Repoint `orchestrator-artifacts` § 6 to the resolution session's vocabulary** (depends on Task 1)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Engine edit — edit **only** `## 6. Status-marker grammar`; every other byte of the file stays identical. Before editing, confirm (already grepped) the three callers — `milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune` — and that this edit preserves their expectations: `roadmap-prune`'s gate reads "pinned = ≥1 marker" (kept verbatim, legacy markers count), and `milestone-rescue`'s disposal writes now land as legacy-but-pinned tokens (out-of-scope reconciliation, per Context).

  Rewrite § 6 to state:
  - Append-only, space-separated bracketed suffix at the end of the entry line (keep verbatim).
  - **Active markers, written by the resolution session** (the dedicated session the user opens from the parked prune's handoff): `[fixed]`, `[routed → <path>]` — where `<path>` must resolve to an **open** task's spec, an editable surface, never a completed/frozen one — and `[dismissed]`.
  - The reviewer never writes or imitates markers.
  - Entry text and `Affects:` are never rewritten — markers only accumulate (keep verbatim).
  - **Pinned = the entry line carries ≥1 marker** (keep verbatim).
  - Dedup rule: whoever pins an entry pins every occurrence across that milestone's review files, dedup by `Affects:` target + gist (keep verbatim).
  - **Legacy markers** `[promoted → <path>]`, `[audit-corroborated]`, `[audit-dismissed]`, `[unrouted-reported]` are retired from the active vocabulary; encountered in old repos they still count as pinned (lazy migration — history is never rewritten).

  Verify: § 6 lists `[fixed]` / `[routed → <path>]` / `[dismissed]`, names the resolution session as the writer, keeps the legacy-markers-count-as-pinned sentence, and keeps append-only + dedup + "pinned = ≥1 marker" verbatim; `git diff src/skills/orchestrator-artifacts/SKILL.md` touches only lines inside § 6.

## Code Re-Review (round 2) — roadmap-prune deferred-observations gate

Re-verified each finding from review-1 against the **current** `src/skills/roadmap-prune/SKILL.md`, then ran a fresh full pass.

---

### Prior findings — verdicts

**Finding 1 (Low) — Step 8 marker-phrase report read files that Step 5 already deleted.** → **Fixed.**

The marker-phrase scan was moved into the pre-sweep gate and Step 8 now only echoes what was captured. Current content:

- `SKILL.md:31-35` (Step 0.2): "Scan every `.md` file … A file with no such section contributes nothing to this step — but capture it for step 6 below before moving on, since Step 5 deletes these files and Step 8 runs after the sweep."
- `SKILL.md:46-51` (Step 0.6): "While scanning, for every file that has **no** `## Deferred observations` section, also check it for any pre-standardization marker phrase … Capture the matching paragraph(s) with their source file now, before Step 5 deletes the file — Step 8 only echoes what is captured here, it never re-reads these dirs."
- `SKILL.md:247-251` (Step 8): "echo the paragraph(s) captured by Step 0.6 under a "possible unharvested margins" heading … Do not re-scan `plan-reviews/`/`reviews/` here — Step 5 already deleted them; this step only reports what Step 0 captured before the sweep. … If Step 0 captured nothing, omit the heading."

The capture now happens while the files exist (Step 0, before the Step 5 sweep), and Step 8 is a pure echo of captured data with an explicit "do not re-read" instruction. The runtime gap (report drawing from deleted files) is closed. `Glob`/`Grep`/`Read` in `allowed-tools` cover the capture. Spec Edit 2's intent — the summary-report step surfaces the margins — is preserved; only the read moment moved earlier, which is the correct fix.

**Finding 2 (Informational, non-blocking) — abort resolution names `milestone-rescue-audit prune`, a mode not yet implemented.** → **Not fixed — by design, as expected.**

Current content `SKILL.md:39-43` still reads: "name the resolution — run `milestone-rescue-audit` in prune mode (`milestone-rescue-audit prune`) first." This text is spec-mandated (spec 03 step 3), correct for this milestone's boundary, and the cross-milestone sequencing risk is already captured as a deferred observation in the plan-review. No code change was requested or appropriate here; the fix is roadmap ordering (land `ROADMAP.md:113` first or add an explicit dependency). Remains tracked, not a defect in this change.

---

### Fresh full pass — new issues

No new correctness, security, or runtime defects. Verified:

- Frontmatter `loads: orchestrator-artifacts` + `Glob Grep` added; no write-capable tool added; sweep/commit grants untouched (`SKILL.md:10-11`).
- Gate sits above `## Before you start`/Step 1 (`SKILL.md:23`), grammar and **pinned** definition are cited from the engine, never restated (`SKILL.md:25-27`, `36-38`).
- Step 0.6 correctly partitions the population: only files **without** a `## Deferred observations` section are margin-scanned; files with the section flow through the entry gate. No double-counting.
- Abort path makes no edits/sweep/ROADMAP changes; proceed path is unchanged. Sweep (Step 5), commit policy, and `What NOT to do` are untouched.
- Marker-phrase list (`SKILL.md:47-49`) matches spec Edit 2 word-for-word.

### Non-blocking note (not a finding)

Step 0.6 ("While scanning …") is numbered *after* the terminal branch steps 0.4 (abort) and 0.5 (proceed), so a linear reader meets the "capture margins" instruction after the "proceed to the normal flow" decision. This is functionally safe — the scan is a single pass, step 0.2 forward-references "capture it for step 6 below before moving on," and step 0.6 opens with "While scanning" — so the agent gathers everything during the one scan regardless of list position. Purely a readability nit (e.g. it could be a sub-bullet of 0.2); no runtime consequence. Optional polish, not required.

REVIEW_PASS

## Code Review — roadmap-prune deferred-observations gate

**Change under review:** `src/skills/roadmap-prune/SKILL.md` (frontmatter `loads:`/`allowed-tools`, new Step 0 gate, Step 8 report clause). The other diffed files are orchestrator artifacts (plan, sidecar, plan-review), not product code.

**Verdict:** Faithful to spec `03-prune-harvest-deferred-observations.md`. The frontmatter edge, gate procedure, engine-referencing (no grammar redefinition), and report-only marker scan all match the spec and the `orchestrator-artifacts` engine (§5/§6). Two correctness notes below; neither blocks, but the first is a genuine runtime gap.

---

### Findings

**1. (Low) Step 8's marker-phrase report reads files that Step 5 already deleted.**
`SKILL.md:239-244` — the report-only clause says: "for files scanned in Step 0 that have no `## Deferred observations` section but contain any pre-standardization marker phrase … quote the matching paragraph(s)." But Step 5 (`SKILL.md:199`) `rm -rf`s `plan-reviews/` and `reviews/` **before** Step 8 runs, so the files are gone by report time. The data can only come from context captured earlier. Step 0's stated job (`SKILL.md:31-36`) is to find `## Deferred observations` sections and check pinning — an agent that Greps for the section header (the natural implementation) never loads the *body* of files that **lack** the section, which is exactly the population Step 8 must quote from. Net effect at runtime: the marker-phrase report silently produces nothing, because its source files are both unread and deleted.
This is a report-only, non-gating feature, so the failure mode is a missing report, not a bad prune or data loss — hence Low. The spec itself places this quoting in the summary step, so the tension is partly spec-inherited; the implementer's "files scanned in Step 0" anchor is the right instinct but Step 0 doesn't actually mandate reading those bodies. A robust phrasing would have Step 0 (or a pre-sweep step) capture the marker-phrase paragraphs while the files still exist, then Step 8 merely echoes them.

**2. (Informational, non-blocking — already captured) Resolution names a mode that does not exist yet.**
`SKILL.md:39-40` — the abort instruction tells the user to "run `milestone-rescue-audit` in prune mode (`milestone-rescue-audit prune`) first." Per engine §6, all status markers are written by `milestone-rescue-audit` only, and that prune mode is milestone `ROADMAP.md:113`, still `[ ]`. If this gate ships before 113, a repo holding any unpinned `## Deferred observations` entry becomes un-prunable with no working pinning path. The gate text is spec-mandated (spec 03 step 3) and correct for this milestone's boundary — the fix is roadmap sequencing (land 113 first, or add an explicit dependency). This is already recorded as a deferred observation in the plan-review for this milestone, so it is tracked, not lost. No code change requested here.

---

### Verified correct
- Frontmatter: `loads: orchestrator-artifacts` mirrors `milestone-rescue/SKILL.md:14`; `Glob Grep` added to `allowed-tools` cover the read-only scan (Read for line numbers, Glob to enumerate, Grep to locate sections). No write-capable tool added. ✓
- Gate placed above Step 1, before `## Before you start` — matches "gate at the very top." ✓
- **Pinned** definition and marker grammar are cited from the engine, never restated (`SKILL.md:34-36`, engine §6). ✓
- Abort format `<file>:<line> — <entry text>` matches spec step 3. ✓
- Missing review dirs (first-ever prune) degrade gracefully — empty scan → proceed. ✓
- `ROADMAP_TESTS.md` parity and the "read-and-refuse only, never marks" constraint are stated (`SKILL.md:45-48`). ✓
- Marker-phrase list (`SKILL.md:240-242`) matches spec Edit 2 word-for-word; the "no `## Deferred observations` section" exclusion prevents structured entries from being double-reported as free-form margins. ✓
- Sweep, spec-deletion, commit policy, and `What NOT to do` are untouched. ✓

The change is safe to ship as-is for this milestone; finding 1 is a quality gap worth a follow-up tweak, finding 2 is roadmap ordering already tracked.

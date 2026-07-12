## Code Review — 5.2 roadmap-prune: default-pair sweep never deletes stem subdirectories

**Files reviewed (code change):** `src/skills/roadmap-prune/SKILL.md` (the only product-code change in the diff)
**Also inspected:** plan `02-5-2-…`, spec 51, spec 49, roadmap line 5.2, `orchestrator-artifacts` §1 layout it cites.
**Out of scope of this milestone (pre-existing staged changes, not reviewed):** `.ai-factory/ROADMAP.md` line 7.1, `.ai-factory/specs/60-…` — both belong to milestone 7.1, unrelated to 5.2.

**Risk level:** 🟢 Low. The change is instruction text for the prune skill; the core behavior matches spec 51 exactly. No data-loss or wrong-deletion path introduced. Two low-severity internal-consistency notes below.

### Correctness — the change does what the spec requires

- **Default-pair split (SKILL.md:279–291)** is correct. `roadmaps/` absent → whole-dir `rm -rf` of `plans/`/`plan-reviews/`/`reviews/`, byte-stable with prior behavior. `roadmaps/` present → `find <dir> -maxdepth 1 -type f -delete`, which removes exactly the flat regular files (the default pair's own artifacts, per `orchestrator-artifacts` §1 — named artifacts always live under `<stem>/`) and leaves every `<stem>/` subdirectory intact. This closes the exact cross-developer hazard 4.7 closed on the named side. `-maxdepth 1` bounds deletion to the dir's own entries; `-type f` spares the subdirs that must survive. Dotfiles are included (find does not skip them), matching the whole-dir sweep's coverage of flat contents.
- **Existence probe** reuses the same `.ai-factory/roadmaps/` signal the skill already relies on at Step 4.1/4.2 — no new detection mechanism, consistent multiuser signal.
- **`test-runs/` split (SKILL.md:310–315)** mirrors the same rule for the default pair, byte-stable when absent, flat-file-only when present; the `<name>-tests`→`<stem>` derivation and the named-test-roadmap case are left untouched, as required.
- **Named-roadmap branch (292–299)** is unchanged — it already swept only its own stem, correct.
- **`allowed-tools` (line 10)** gains `Bash(find *)` and retains `Bash(rm *)` — right call, since the implementer emitted a literal `find … -delete` and the solo branch still uses `rm -rf`. This is the coupling Task 3 required.
- **Lead-in verb (line 278)** softened `rm -rf:` → `then delete:` — resolves plan-review F1; the stem no longer hard-asserts a verb that contradicts the nested `find`.
- **Step 8 (362–367)** left byte-stable. Defensible: the swept *dirs* are unchanged (still the three flat dirs + flat `test-runs/`); only what is deleted within them narrows, and Step 8 enumerates dirs, not files. No drift.
- **Step 0.2 margin-capture scope** ("the flat `plan-reviews/`/`reviews/` files for a default-pair prune") was already flat-scoped, so the narrowed sweep now *aligns* with it — correctly left untouched, no scope expansion.

### Findings (non-blocking)

**N1 — "deletion is plain `rm`" (SKILL.md:399) is now inaccurate on the multiuser branch.**
The "What NOT to do" bullet reads: *"Do not use `git rm` — deletion is plain `rm`; staging happens once, at commit time, via `git add -A`."* The `roadmaps/`-present branch now deletes via `find … -delete`, not `rm`, so the justification clause has an unstated exception. The bullet's operative intent — *don't stage deletions with `git rm`; leave them for `git add -A`* — still holds (`find -delete` likewise leaves nothing staged), so behavior is unaffected; this is purely a wording drift of the same class as F1 that the plan-review chain cared about. Minimal fix: broaden the clause to e.g. "deletion is plain `rm`/`find -delete`" or "deletion is unstaged (`rm`/`find`), never `git rm`". Low severity — instruction consistency, not runtime behavior.

**N2 — `find <dir> -maxdepth 1 -type f -delete` errors on a missing dir where `rm -rf` did not.**
`rm -rf plans/` succeeds silently if `plans/` was never created; `find plans -maxdepth 1 -type f -delete` exits non-zero with "No such file or directory". On a multiuser repo where the default pair never produced one of the flat dirs (or flat `test-runs/`), the present-branch command emits a benign stderr error. It causes **no** data loss and does not touch the preserved subdirs, and the spec explicitly sanctioned this exact command form ("`find <dir> -maxdepth 1 -type f -delete` or equivalent"), so this is essentially by-design. Noting only because the solo branch tolerates missing dirs and the multiuser branch no longer does; if the implementer wants parity, guarding on directory existence (or `find <dir> … 2>/dev/null`, or `[ -d <dir> ] &&`) would restore it. Very low severity.

### Verdict

Core logic correct and spec-faithful; both findings are cosmetic/robustness notes with no behavioral impact on the intended cases. Safe to proceed; N1 is a one-line wording fix worth folding in for consistency.

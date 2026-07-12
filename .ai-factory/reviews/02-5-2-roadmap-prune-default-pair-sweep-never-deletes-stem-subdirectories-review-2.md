## Code Review (re-review) — 5.2 roadmap-prune: default-pair sweep never deletes stem subdirectories

**Files reviewed (code change):** `src/skills/roadmap-prune/SKILL.md` (only product-code change in the diff).
**Also inspected:** plan `02-5-2-…`, spec 51, `orchestrator-artifacts` §1 layout, prior review-1.
**Out of scope (pre-existing staged changes, not this milestone):** `.ai-factory/ROADMAP.md` line 7.1, `.ai-factory/specs/60-…` — milestone 7.1.

**Risk level:** 🟢 Low.

### Verdicts on prior review (review-1)

**N1 — "deletion is plain `rm`" (SKILL.md:399) inaccurate on the `find` branch → FIXED.**
Current content (SKILL.md:401):
> - Do not use `git rm` — deletion is unstaged (`rm`/`find -delete`), never `git rm`; staging happens once, at commit time, via `git add -A`

The justification clause now names both deletion mechanisms (`rm`/`find -delete`) and reframes the guard around its actual intent (deletion is *unstaged*, never `git rm`). The wording drift is gone and the guard's meaning is preserved. Fixed.

**N2 — `find … -delete` errors on a missing dir where `rm -rf` did not → FIXED.**
Current content (SKILL.md:285–288, and 314–316 for `test-runs/`):
> - **`roadmaps/` present** — delete only the regular files directly under each of those three flat dirs (`[ -d <dir> ] && find <dir> -maxdepth 1 -type f -delete`, guarding the way `rm -rf` tolerates a dir that was never created), preserving every developer's per-roadmap stem subdirectories …

and for tests mode:
> `roadmaps/` present → delete only the regular files directly under flat `test-runs/` (`[ -d test-runs ] && find test-runs -maxdepth 1 -type f -delete`), preserving every `test-runs/<stem>/` subdirectory.

Both `find` invocations are now guarded by `[ -d <dir> ]`, restoring the missing-dir tolerance the solo-repo `rm -rf` branch has, and the inline comment states exactly that intent. This is the parity fix review-1 suggested, applied to both the three flat dirs and flat `test-runs/`. Fixed.

### Full re-review — current state

Re-read Step 5 and the surrounding steps in full. The change remains spec-faithful and is now internally consistent end to end:

- **Default-pair split (279–292)** — `roadmaps/` absent → whole-dir `rm -rf`, byte-stable; present → guarded `find -maxdepth 1 -type f -delete`, deleting only the default pair's flat artifacts and sparing every `<stem>/` subdir (named artifacts live only under `<stem>/` per `orchestrator-artifacts` §1). Correct closure of the cross-developer hazard on the default side.
- **`test-runs/` split (311–317)** — mirrors the same guarded rule for the default pair; `<name>-tests`→`<stem>` derivation and the named-test case left untouched.
- **Named-roadmap branch (293–300)** — unchanged, already stem-scoped.
- **Lead-in verb (278)** — `then delete:` no longer contradicts the nested `find` (review-1 F1 / plan-review F1 both resolved).
- **`allowed-tools` (line 10)** — `Bash(find *)` added, `Bash(rm *)` retained for the solo branch and the `rm -f` spec deletion; grant now covers every command the body emits.
- **Step 8 (365–370)** — byte-stable; the swept *dirs* are unchanged and it enumerates dirs, not files. No drift.
- **Step 0.2 margin-capture** — already flat-scoped, now aligned with the narrowed sweep; correctly untouched.

The `[ -d <dir> ] && find …` compound returns a non-zero status when the dir is absent (the `&&` short-circuit), but this is per-dir agent instruction text run interactively, not a `set -e` script, so the benign non-zero is inconsequential — no data-loss or wrong-deletion path exists on either branch.

No new issues found.

REVIEW_PASS

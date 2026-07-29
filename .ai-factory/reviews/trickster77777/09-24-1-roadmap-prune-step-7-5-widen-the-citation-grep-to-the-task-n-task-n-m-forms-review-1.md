## Code Review — roadmap-prune Step 7.5: widen the citation grep to the `Task N` / `task N.M` forms

**Change reviewed:** `git diff HEAD` — one code change in `src/skills/roadmap-prune/SKILL.md` (the other staged files are the plan, its JSON sidecar, and two plan-reviews — planning artifacts, not code).
**Risk Level:** 🟢 Low

### What the change does
Step 7.5 item 3 (the report-only plan-layer citation scan) gains two ERE alternations in both the prose shape list and the fenced `grep -rInE` invocation: `Task [0-9]` (the capitalized `# Task N:` section-comment form) and `task [0-9]+\.[0-9]+` (the lowercase decimal-coordinate form). Diff spans SKILL.md:375–381 only.

### Verified correct
- **Matches the spec byte-for-byte.** The resulting command on SKILL.md:381 is identical to the pattern stated in `.ai-factory/specs/trickster77777/87-prune-scan-task-citation-shapes.md`: `grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]|Task [0-9]|task [0-9]+\.[0-9]+"`. Prose list (375–376) and invocation (381) carry the same two additions, in lockstep.
- **ERE validity, verified live.** Ran the widened pattern against `/Users/max/projects/sakshi/orchestrator`: `grep -E` exits 0 with no stderr — `\.` literal dot and `+` quantifier are valid POSIX ERE.
- **No regression, verified live.** Old pattern → 60 hits; widened pattern → 111 hits; all 60 old lines present in the new set (`comm -23` missing count = 0). The widening is strictly additive.
- **Surfaces the real leak, verified live.** Both anchors the plan's Task 3 cites resolve to genuine matches: `tests/test_main.py:260` (`# Task 1: Fresh start and sidecar-driven steps…`) and `tests/test_agents.py:17` (`# Task 1: match within the last-5-line window`). The pre-change pattern nets zero `# Task N:` comment lines.
- **Case-sensitivity is correct.** The scan runs without `-i`, so capital `Task [0-9]` (for `# Task N:`) and lowercase-decimal `task [0-9]+\.[0-9]+` (for inline `task 2.2` cites) are both required; the lowercase form's mandatory decimal avoids flooding on the bare word "task".

### Guards honored
- `--exclude-dir=.ai-factory --exclude-dir=.git` preserved exactly (SKILL.md:382).
- Scan stays report-only, whole-repo, repo-root-anchored; placement in the step sequence unchanged; the surrounding "guidance, not contract" sentence and item 4 unchanged.
- Steps 0–7 (outside 7.5 item 3), Step 8, and the Commit section are untouched (diff confirms — only lines 375–381 changed).
- The five pre-existing alternations are left in original order; the two new forms are appended.
- `src/global/CLAUDE.md:18` (the home rule) is untouched — consistent with the spec's cross-artifact-coupling decision that the scan is a deliberate, permanent report-only superset of the home rule, not a divergence.

### Runtime failure modes considered
- No migration, type, or concurrency surface — the change is a static grep pattern inside a skill body. The only runtime risk (an invalid ERE that would make the whole scan error out) was checked live: pattern is valid.

No findings.

REVIEW_PASS

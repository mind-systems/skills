# Code Review (Re-review) — 4.3 readers resolve the roadmap in play

Re-review after fixes for `review-1.md`. Each prior finding re-checked against the **current** file via Read, then a full fresh pass for new issues.

---

## Prior finding verdicts

### Finding 1 — pin-gaps cannot execute the "my roadmap" tier it points to (grant gap) · **FIXED**

`src/commands/command-pin-gaps.md:10` now reads:

```
allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill
```

The grant changed from `Bash(git grep *)` to `Bash(git *)`. `Bash(git *)` matches the engine's identity read `git config user.email` (engine `SKILL.md:56`), so the "my roadmap" tier the fallback references (`command-pin-gaps.md:17`) is now executable — including in a headless orchestrator run. The `Skill` grant and `loads: roadmap-engine` (`:10-11`) plus the load-once line (`:14-15`) remain in place, so the full dependency (load *and* execute) is wired. The implementer chose `Bash(git *)` over the minimal `Bash(git config *)` I suggested; this is the better call — it matches the family norm (rescue, test-coverage, temporal-tree all carry `Bash(git *)`) and pin-gaps is a user-invoked planning command, not a grant-sensitive surface. Verdict: **Fixed**.

---

## Full re-review — new issues

Ran `git diff HEAD` and read all four changed files in full. The only delta versus the previous pass is the one-token pin-gaps grant fix above; the rescue, test-coverage, and temporal-tree diffs are unchanged and were verified correct in review-1. Re-confirmed on this pass:

- **rescue** — Step 4 (`:178-187`) resolution-order widen intact (argument branch byte-unchanged, test-keyword → `-tests` sibling of the roadmap in play, else the roadmap in play); Step 1 (`:56-57`) collapsed to the pure pointer "(the same resolution Step 4 determines)", no contradiction; `loads: orchestrator-artifacts roadmap-engine` + mirrored load-once line correct. No stray old literals.
- **test-coverage** — Layer 1 (`:29-35`) names the resolution feeding `$ROADMAP_PATH`; `loads: test-philosophy roadmap-engine`; `Bash(git *)` already covered the identity read.
- **temporal-tree** — Step-3 path resolved (`git show <first-hash>:<resolved-roadmap-path>`), both literals replaced, integration-branch caveat (`:83-88`) present; `loads: roadmap-engine` + `Skill` added; `Bash(git *)` present.
- **Engine coupling** — the four new `loads: roadmap-engine` callers resolve via the engine's live reverse-graph grep marker (`roadmap-engine SKILL.md:22-23`); the named anchor `## Named roadmaps` (`:49`) exists. No engine-side edit needed.
- **Spec-45 guards** — "referenced, never restated" and "defaults byte-stable" hold at all four sites; with no `roadmaps/` present, every reader resolves exactly as today.

No new correctness, security, or runtime issues found. The prior finding is resolved and no regression was introduced.

REVIEW_PASS

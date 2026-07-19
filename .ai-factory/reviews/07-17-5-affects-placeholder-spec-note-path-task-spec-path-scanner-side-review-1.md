# Review 1 — 17.5 `- Affects:` placeholder: `spec-note path` → `task-spec path` (scanner side)

## Code Review Summary

**Files Reviewed:** `src/skills/orchestrator-artifacts/SKILL.md` (in full, 84 lines), plus the cross-repo emitter `orchestrator/orchestrator/prompts/reviewer.md:108`, the callers surfaced by the engine-caller grep (`roadmap-prune`, `task-rescue-audit`, `docs/using-the-language.md`), the task spec `73-affects-placeholder-task-spec-path.md`, and `ROADMAP.md:31`.
**Risk Level:** 🟢 Low
**Verdict:** the change is correct, minimal, and complete.

### What changed

Exactly one line, one field:

```
-Present in both review genres. Entry: `- Affects: <phase / spec-note path /
+Present in both review genres. Entry: `- Affects: <phase / task-spec path /
```

`git diff --numstat` reports `1 1` for the file — one insertion, one deletion, no collateral edit anywhere else in the 84 lines. The other four staged files are pipeline artifacts (plan, sidecar, two plan-reviews), not product.

### Verification — all four plan checks executed, all pass

| Check | Expected | Actual |
|---|---|---|
| `grep -n 'task-spec path' …/SKILL.md` | line 55 only | `55:` only ✅ |
| `rg -in 'spec-note' …/SKILL.md` | zero | zero ✅ |
| `grep -c '## Deferred observations' …/SKILL.md` | 2, unchanged | 2 ✅ |
| `git diff` shape | one line, `spec-note`→`task-spec` only | `1 1` numstat ✅ |

### Guards — each one checked against ground truth, not assumed

- **Scanned literals byte-identical.** `grep -c '- Affects: '` returns `1` both at `HEAD` and in the working tree — the prefix is untouched. The `## Deferred observations` heading count is unchanged at 2 (frontmatter `description:` line 5 and section header line 53); neither was edited.
- **Tail preserved.** Line 56 still reads `"unknown"> — <observation>`. The emitter's `— <one-paragraph observation>` was correctly *not* harmonized — the per-side difference both specs record survives intact.
- **Wrap not reflowed.** The two strings are both 14 bytes, and line 55 ends at the same column as before; the placeholder still wraps between `/` and `"unknown">`. No reflow, exactly as instructed.
- **Protocol tokens untouched.** Frontmatter (`description:`, `allowed-tools:`, `user-invocable:`, `disable-model-invocation:`), the reverse-graph marker at lines 17–19, the `[fixed]` / `[routed → <path>]` / `[dismissed]` literals, the legacy-marker list, and the PASS-signal literals (`PLAN_REVIEW_PASS` / `REVIEW_PASS` / `TEST_PASS`) are all identical to `HEAD`. File ends with a single trailing newline — no whitespace damage.

### Engine contract — no caller breaks

`grep -rn 'Affects:' src/skills/ src/commands/ docs/` returns only: `roadmap-prune:61` and `task-rescue-audit:60` (both naming `Affects:` as a target *field name*), `docs/using-the-language.md:35` (naming the token `- Affects: …` with the placeholder elided), and the two in-file self-references at `SKILL.md:71,74`. None reads the placeholder's inner field text, so no consumer's expectation is disturbed. This is a documentation placeholder, not a parsed literal — there is no scanner regex, migration, or type surface to break at runtime.

### Cross-repo lockstep — now closed

`reviewer.md:108` (emitter) reads `- Affects: <phase / task-spec path / "unknown"> — <one-paragraph observation>`; `SKILL.md:55` (scanner) now reads `<phase / task-spec path /`. The pinned field matches on both sides, and `rg -in 'spec-note'` across `src/` and `docs/` returns zero. The only remaining repo occurrence is the roadmap contract line naming the task itself — correctly left alone.

`active/skills/orchestrator-artifacts` is a symlink to `../../src/skills/orchestrator-artifacts`, so the working set that `~/.claude` loads picks the change up with no second write. Editing under `src/` was the right path.

### Critical Issues

None.

### Findings

None.

### Positive Notes

- The edit is genuinely surgical on a file a prior task certified conformant — the scope fence held, and nothing adjacent was "tidied up" along the way.
- The tail divergence survived, which is the outcome that required active restraint: a conformance pass over this section invites collapsing `— <observation>` and `— <one-paragraph observation>` into one form, which would have broken a deliberate per-side difference.

## Deferred observations

- Affects: `.ai-factory/ROADMAP.md` — contract line 17.5 is still `[ ]` while the sidecar reads `step: implemented`. Prior task commits in this repo (e.g. `abbc811` for 17.4) carry the `ROADMAP.md | 2 +-` flip in the same commit as the product change, so the flip is expected at the commit stage, after review passes — not a defect at this point in the pipeline. Recorded so the commit stage is checked to include it rather than assumed. [dismissed — verified live: ROADMAP.md's 17.5 contract line is now [x], the commit-stage flip happened as expected]

REVIEW_PASS

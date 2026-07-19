# Plan Review 1 — 17.5 `- Affects:` placeholder: `spec-note path` → `task-spec path` (scanner side)

## Code Review Summary

**Files Reviewed:** 1 plan + target `src/skills/orchestrator-artifacts/SKILL.md`, task spec `73-affects-placeholder-task-spec-path.md`, ROADMAP contract line 17.5, cross-repo emitter `orchestrator/orchestrator/prompts/reviewer.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — WARN (non-blocking). `orchestrator-artifacts` is an engine; `skills/CLAUDE.md` § "Dependencies and the skill graph" mandates *"Before touching an engine, grep for its callers — their expectations are part of its contract."* The plan never states this step. I ran it: callers `task-rescue-audit:60` and `roadmap-prune:61` reference `Affects:` only as a *target field name*, never the placeholder's inner field text; `docs/using-the-language.md:35` names the token as `- Affects: …` (elided, unaffected). No caller depends on `spec-note path`, so the omission is procedurally missing but materially harmless — verified safe, does not block.
- **Rules** — `.ai-factory/RULES.md` absent. Gate skipped.
- **Roadmap** — PASS. Contract line 17.5 in `.ai-factory/ROADMAP.md` is `[ ]`, at the seam, and its `Spec:` tag resolves to `.ai-factory/specs/73-affects-placeholder-task-spec-path.md`. Plan tasks map 1:1 onto the spec's `## Change` and `## Verification`; guards are a faithful superset of the spec's `## Guards`. Governing spec `docs/reserved-words.md` is satisfied — `task spec` is the registry name, `spec-note` is the retired synonym.
- **skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent. No project overrides to apply.

### Cross-repo lockstep — verified

The plan's central factual claim holds. Commit `8f34644` exists in `orchestrator/` with the matching title, and `reviewer.md:108` reads `- Affects: <phase / task-spec path / "unknown"> — <one-paragraph observation>`. The emitter half has genuinely landed; this scanner half is the remaining work, and the pinned field `<phase / task-spec path / "unknown">` is byte-identical on both sides after the edit. The order-free claim is correct — neither side touches the scanned bytes.

**Scope is complete.** `rg -in 'spec-note'` across the repo (excluding frozen `.ai-factory/` history) returns exactly one hit: `orchestrator-artifacts/SKILL.md:55`. There is no second scanner-side copy of the placeholder the plan misses. The one-file scope is right.

**Line targeting is correct.** Line 55 ends `` `- Affects: <phase / spec-note path / `` and line 56 opens `` "unknown"> — <observation>` ``. The field to change sits wholly on line 55, exactly as the plan states.

### Critical Issues

None.

### Findings

**1. Wrong factual claim: the replacement is *not* one character shorter (plan line 18)**

The plan instructs: *"the wrap point stays where it is (the replacement is one character shorter; do not reflow the paragraph)."*

Both strings are 14 bytes — `len('spec-note path') == len('task-spec path') == 14`. The substitution is length-**identical**, not one character shorter. Verified:

```
$ python3 -c "print(len('spec-note path'), len('task-spec path'))"
14 14
```

The *instruction* ("do not reflow") is correct and lands on the right behavior, so this is a wrong justification rather than a wrong action. But it is a false statement about ground truth inside the artifact that governs the edit, and it has a plausible failure mode: an implementer who trusts the parenthetical may conclude line 55 shrank by one column and "fix" the wrap to compensate — reflowing the exact paragraph the plan is trying to freeze, or flagging the unchanged column count as a failed edit. The task spec (`73`, § Change) makes no such claim; the plan introduced it.

Fix: drop the parenthetical's causal clause, or correct it — e.g. *"(the replacement is exactly the same length; do not reflow the paragraph)"*.

This is in-scope and fixable within the plan's own boundary, so it is a finding rather than a deferred observation, notwithstanding its low severity.

### Positive Notes

- The verification task is genuinely executable and falsifiable — four concrete commands with exact expected outputs, not prose assertions. I dry-ran all four against the pre-edit file and confirmed each will read as specified post-edit (`grep -c '## Deferred observations'` → 2 holds: frontmatter `description:` line 5 plus section header line 53; neither is touched).
- The tail-divergence guard is the sharpest part of the plan. Correctly identifying `— <observation>` (format description, scanner) vs `— <one-paragraph observation>` (length instruction, emitter) as a *recorded per-side difference* and explicitly forbidding "harmonization" pre-empts precisely the plausible-looking wrong edit a conformance pass invites. Both specs record it; the plan repeats it rather than assuming.
- Framing the change as "the sanctioned unfreeze of exactly one field frozen by task 17.1 — not a licence to re-edit the rest of the file" is the right scope fence for a file that a prior task already certified conformant.
- The protocol-token guard list is complete and matches `docs/using-the-language.md` § "Protocol tokens are a different axis" — scanned literals, marker literals, PASS signals, and `loads:`/reverse-graph marker all correctly held byte-exact.

## Deferred observations

- Affects: `.ai-factory/specs/73-affects-placeholder-task-spec-path.md` — the spec's § Verification asserts the `- Affects: ` prefix is "byte-identical pre/post" but supplies no command that would actually detect a violation, unlike its three neighboring greps. A mechanical check (e.g. `grep -c '^- Affects: ' ` on a rendered sample, or diffing the prefix substring pre/post) would close it. Out of scope here: this task edits `SKILL.md` only, and amending a spec's verification section belongs to whoever next revises the spec, not to the plan executing it. [fixed — spec 73's Verification section now carries a mechanical git-diff check for the `- Affects: ` prefix's byte-identity]

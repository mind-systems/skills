# Review: 4.4 — roadmap-prune integration-branch contract + repo-wide ledger wording

## Scope
Code change: `src/skills/roadmap-prune/SKILL.md` (two sentences added). The plan/spec govern the wording and placement; `roadmap-prune` is instruction text with no runtime, so correctness here means contract fidelity and byte-stability guards.

## What changed
1. **Line 200 (Step 4.2 head) — integration-branch policy sentence.** Added: in a multiuser project (`.ai-factory/roadmaps/` exists), prune runs on the integration branch, one actor, after merges — never per-developer; Features are project features (authorship in commit history), single-actor prune keeps drop-history + feature rows single-writer.
2. **Line 143 (Step 2.2 `Roadmap drop history` bullet) — repo-wide ledger sentence.** Inserted between the existing snapshot-semantics sentence and the maintenance-work sentence: the snapshot commit holds all files, one repo-wide ledger serves every roadmap, `git show <snapshot>:<roadmap path>` reconstructs any roadmap, no per-roadmap ledger rows.

## Verification against spec `46` and the plan
- **Placement:** sentence 1 sits at the Features write step; `grep -n "integration" src/skills/roadmap-prune/SKILL.md` hits line 200 (the policy sentence) — spec verification satisfied. Sentence 2 sits beside the existing `git show <hash>:.ai-factory/ROADMAP.md` reconstruction wording.
- **Conditionality:** both sentences are gated on `.ai-factory/roadmaps/` existing, so a solo project's reading is behavior-identical — the spec's "solo-project reading unchanged" guard holds.
- **Byte-stability of prior text:** the pre-existing single-roadmap snapshot sentence and the maintenance-work sentence on line 143 are preserved verbatim; the new clause is inserted between them. 3.1's landed text (versioned header, self-heal 4.2a, snapshot semantics) is untouched.
- **Untouched surfaces:** the diff touches only lines 143 and 200–204. Step 0 gate, Step 1, Step 3, Step 5 sweep, Step 6–8, and the commit policy are unmodified — matching "gate, sweep, commit policy untouched."
- **Instructions only:** both additions are directive, no rationale prose — consistent with the skill's own mandate.

## Observations (non-blocking, no action required)
- `grep "integration"` also matches the pre-existing "protocol integration" on line 142; the intended policy-sentence hit on line 200 is present, so the spec check is unambiguous. No issue.
- The parallel drop-history bullet in Step 4.2's write rules (line ~247) does not carry the `git show` reconstruction wording and so was correctly left without the repo-wide clause — no inconsistency introduced.

No correctness, security, or runtime concerns — the change is additive instruction text, correctly scoped and conditional.

REVIEW_PASS

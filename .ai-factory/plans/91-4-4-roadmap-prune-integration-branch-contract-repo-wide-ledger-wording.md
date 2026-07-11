# Plan: roadmap-prune: integration-branch contract + repo-wide ledger wording

## Context
State the multiuser policy in `roadmap-prune` so prune/Features are understood as integration-branch operations and the drop-history ledger reads repo-wide, without changing any mechanism, gate, sweep, or commit behavior.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Policy wording

- [x] **Task 1: Add the integration-branch policy sentence**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Place one contract sentence with the Features/drop-history write instructions — the natural home is Step 4.2 ("Write Features and drop history"), adjacent to the Features write step so `grep -n "integration" src/skills/roadmap-prune/SKILL.md` hits it there (per the spec's verification). Wording, per the governing spec (`docs/multiuser-roadmaps.md` § «Интеграционные поверхности» via spec `46`): in a multiuser project (`.ai-factory/roadmaps/` exists), prune runs on the integration branch, one actor, after merges — never per-developer; Features are project features (authorship lives in commit history, not the table), and single-actor prune keeps both the drop-history row and the feature rows single-writer. Make the sentence conditional on `.ai-factory/roadmaps/` existing so a solo project's reading is unchanged. Instructions only — no rationale prose (the skill's own mandate). Do not touch the Step 0 gate, Step 5 sweep, commit policy, or 3.1's landed self-heal/versioned-header/snapshot text beyond adding this sentence.

- [x] **Task 2: Add the repo-wide ledger sentence** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Add one contract sentence next to the drop-history snapshot semantics (Step 2.2's `Roadmap drop history` description at line ~143 and/or Step 4.2's drop-history write at line ~240/247 — pick the drop-history instruction site so it sits beside the existing `git show <hash>:.ai-factory/ROADMAP.md` reconstruction wording). Wording, per spec `46`: the snapshot commit holds all files, so one repo-wide ledger serves every roadmap — `git show <snapshot>:<roadmap path>` reconstructs any roadmap at that prune; no per-roadmap ledger rows. Add it as an additive clause conditional on `.ai-factory/roadmaps/` existing — leave the existing single-roadmap `git show <hash>:.ai-factory/ROADMAP.md` text byte-identical so solo-project behavior is unchanged. Instructions only, no rationale prose.

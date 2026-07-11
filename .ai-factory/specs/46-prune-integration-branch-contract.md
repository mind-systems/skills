# roadmap-prune: integration-branch contract + repo-wide ledger wording

Governing spec: `docs/multiuser-roadmaps.md` § «Интеграционные поверхности». Runs strictly after task 3.1 lands (same-file collision — 3.1 rewrites the drop-history/ledger text this task amends).

## Current state

`src/skills/roadmap-prune/SKILL.md` already takes the target roadmap as its argument, so a named roadmap prunes mechanically. But nothing states the multiuser policy: with per-developer roadmaps in per-developer branches, concurrent prunes would write the same `## Features` table and the same drop-history row — a guaranteed merge conflict and a broken single-writer surface. The ledger wording (post-3.1) also reads single-roadmap: the snapshot reconstructs "the" roadmap.

## Change

Two contract sentences, placed with the Features/drop-history instructions:

1. **Integration-branch policy:** in a multiuser project (`.ai-factory/roadmaps/` exists), prune runs on the integration branch, one actor, after merges — never per-developer. Features are project features; authorship lives in commit history, not in the table.
2. **Repo-wide ledger:** the snapshot commit holds all files, so `git show <snapshot>:<roadmap path>` reconstructs any roadmap at that prune — one ledger serves every roadmap; no per-roadmap ledger rows.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only.

## Guards

- Gate (Step 0), sweep, commit policy (`Roadmap prune`, on request only), and 3.1's landed text (versioned header, self-heal, snapshot semantics) untouched beyond the two sentences.
- No mechanism added — this is policy wording; the path argument already carries the file.
- Instructions only, no rationale prose (the skill's own mandate).

## Verification

- `grep -n "integration" src/skills/roadmap-prune/SKILL.md` hits the policy sentence next to the Features write step.
- Solo-project reading of the skill is unchanged in behavior — both sentences are conditional on `roadmaps/` existing.

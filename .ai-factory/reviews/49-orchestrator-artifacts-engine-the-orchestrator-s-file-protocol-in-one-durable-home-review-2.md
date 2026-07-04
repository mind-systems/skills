# Review — orchestrator-artifacts: engine (round 2, re-review)

## Verdicts on round-1 findings

### 1. (Medium) `milestone-rescue` never instructs the engine to be loaded — **Fixed**

Current content of `src/skills/milestone-rescue/SKILL.md` lines 34–36:

> Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if
> not already loaded) — it defines the artifact layout, naming, signals, sidecar
> fields, and marker grammar referenced below.

The explicit load-trigger is now present, placed before Step 1, and matches the roadmap-family idiom verbatim (`roadmap-outline` line 15 / `roadmap-decompose` line 21: "Ensure `X` is loaded once this chat (via the Skill tool, only if not already loaded)"). The three by-name references at lines 44–45, 53–54, and 77 (Step 2 signal semantics) now resolve against an engine that is guaranteed to be in context. The gap is closed.

## Full re-review for new issues

Changes since round 1 are limited to the three added lines above — `git status` and the diffs confirm the engine skill, the `active/skills/orchestrator-artifacts` symlink, and the `CLAUDE.md` active-set line are byte-identical to round 1, where they were verified clean:

- Engine content faithful to spec 05 Edit 1 (all seven items, correct frontmatter, reverse-graph marker in the `note`-engine idiom, 56-line body ≤ ~60 target, no procedure/policy leaked).
- Symlink resolves to `../../src/skills/orchestrator-artifacts` with target `SKILL.md` reachable.
- `CLAUDE.md` active-set updated correctly.
- `milestone-rescue` protected regions (sidecar step table, Step 5 rollbacks, Step 3 Diagnosis Report register) remain untouched — the diff stays confined to the frontmatter `loads:` field, the new load instruction, and the Step 1/Step 2 slimming.

The new lines introduce no correctness, security, or runtime problems: purely a load-once instruction consistent with the established engine-loading mechanism.

No outstanding findings.

REVIEW_PASS

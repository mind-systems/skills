# Review — orchestrator-artifacts: engine (round 1)

Scope: new engine skill `src/skills/orchestrator-artifacts/SKILL.md`, rewired `src/skills/milestone-rescue/SKILL.md`, `active/skills/orchestrator-artifacts` symlink, `CLAUDE.md` active-set line.

## What was verified clean

- **Engine content vs. spec 05 Edit 1** — all seven items present and faithful: layout (four dirs + `test-runs/`, `<seq>-<slug>` naming, rounds), PASS signals (`PLAN_REVIEW_PASS`/`REVIEW_PASS`/`TEST_PASS` on own last line), sidecar fields, committed⇔completed, `## Deferred observations` format + reserved status field, the four-marker grammar with pinned/dedup rules, and the mirrors-the-orchestrator coupling. Frontmatter correct (`user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`). Reverse-graph marker present in the `note`-engine idiom with the correct inline grep. Body is 56 lines — within the ≤~60 target. No procedure or policy leaked in.
- **Symlink** — `active/skills/orchestrator-artifacts → ../../src/skills/orchestrator-artifacts` resolves (target `SKILL.md` reachable), matching the relative-target form of sibling symlinks.
- **CLAUDE.md** — `orchestrator-artifacts` added to the active-set list before the "plus one upstream original" clause. Correct.
- **milestone-rescue byte-identical guarantee** — the diff touches only frontmatter + Step 1/Step 2 prose (21 lines, all in the top region). The `### Valid sidecar step states` table, all Step 5 rollback procedures, and the Step 3 Diagnosis Report register are untouched, as the spec required.

## Findings

### 1. (Medium) `milestone-rescue` never instructs the engine to be loaded — the delegated content may be absent at runtime

`src/skills/milestone-rescue/SKILL.md` now delegates layout, naming, and signal semantics to `orchestrator-artifacts` via three by-name references ("layout and naming conventions are described in `orchestrator-artifacts`" line 41; "see `orchestrator-artifacts` for the naming convention" line 50; "Signal semantics … are defined in `orchestrator-artifacts`" line 76). It adds `loads: orchestrator-artifacts` to frontmatter — but that field is only the dependency-graph declaration (per CLAUDE.md, the forward/reverse graph is *read* from `loads:`; nothing states it auto-loads at runtime).

The actual load-trigger in this codebase is an explicit body instruction. The roadmap family — the exact idiom spec 05 Edit 2 says to copy ("ensure loaded once per chat, same idiom as the roadmap family") — carries it verbatim: `roadmap-outline` line 15 and `roadmap-decompose` line 21 both say *"Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded)."* `milestone-rescue` has no equivalent line anywhere (`grep` for "Skill tool"/"loaded" in the body returns nothing but the frontmatter).

Failure scenario: an agent invoked directly on "rescue" runs Step 1, hits "layout and naming conventions are described in `orchestrator-artifacts`", and — having no instruction to load that engine and no engine content in context — proceeds with the slimmed prose that no longer defines the four directories, the `<seq>-<slug>` naming, or the PASS-signal last-line rule. The rewiring removed content on the assumption the engine is present, but nothing guarantees it is. The spec's parenthetical ("ensure loaded once per chat, same idiom as the roadmap family") was only half-applied: the `loads:` field landed, the load instruction did not.

Fix: add the roadmap-family line near the top of milestone-rescue's body (before Step 1), e.g. *"Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if not already loaded)."*

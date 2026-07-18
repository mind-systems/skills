# skill-description-field: compress descriptions to the routing contract

Phase 14, task 14.1. Governing spec: [skill-description-field](../../docs/skill-description-field.md). Supersedes the retired three-task altitude cut (specs 67–69): the levelling frame — a reference grain set by one task, a capstone converging the rest — is replaced by one **locally decidable rule**, so no task depends on another's output and the whole pass is a single edit set.

## The rule — one home per fact, applied to the manifest

A `description:` carries the routing contract: **what the skill does + when to invoke it + the concept, with every trigger phrase verbatim**. Any clause that restates what the body owns — procedure steps, enumerated stage pipelines, repair-depth lists, sidecar mechanics, wiring ("then hands off to X", caller lists, spawn protocol) — is a **second home for a body fact**: when the body changes, the always-loaded layer silently lies, and the trigger drowns in detail. Cut those clauses; their home is the body (`loads:`, the engine body's reverse-graph marker, the caller's skill). Never pad: a terse entry that routes cleanly is already at grain, and "no change" is a legal per-file outcome.

## Inventory (re-verified 2026-07-18 against the final post-13/16/17 field; re-read the manifest before editing — the handoff-19 checklist is satisfied and this section records its result)

**Compress — mini-manuals restating their body:**

- `task-rescue` — the parenthetical depth enumeration "(spec / spec+plan / spec+plan+code / plan-ratified-implementation-absent)" and the sidecar-rollback mechanics are Step 4/5's facts. Keep: diagnose → repair to depth → roll back concept, the PASS-literal quotes, and the trigger phrases byte-identical ("rescue", "milestone failed", "pipeline stopped" — user input, frozen per 17.3's ruling).
- `task-rescue-audit` — the manifest's heaviest entry. Keep: outside-view convergence audit of a looped/outlier task, chat-only output, when-to-run; compress the band-aid narrative and the "on smell" clause chain; trigger phrases byte-identical.
- `roadmap-test-coverage` — the nine-verb pipeline narration is the body's layer structure. Keep goal + when-to-use; drop "then hands off to /roadmap-decompose" (topology).
- `roadmap-decompose-skeleton` — "renders via roadmap-engine, sources the test rule from test-philosophy — copies neither" is the `loads:` line's fact. Keep the spec-before-code axis concept + when + trigger words.
- `editor` (`src/agents/editor.md`) — the spawn-protocol instructions ("Spawn once… never a fresh spawn per task") duplicate the discipline whose home is `agent-architect`'s body. Decide at plan time: keep only what the main loop genuinely routes on (that the architect is the sole caller may qualify; the operational protocol does not).

**Candidates — judge by the rule, likely light or no change:** `agent-architect`, `command-pin-gaps`, `orchestrator-artifacts` (its three-caller list is a reverse edge; the body's reverse-graph marker is the home).

**Untouched — already at grain, never padded:** `aif`, `aif-architecture`, `note`, `roadmap-engine`, `test-philosophy`, `detangle`, `temporal-tree`, `observe-logs`, `roadmap-outline`, `aif-docs`, `roadmap-decompose`, `roadmap-prune` (near-grain; likely no change). `aif-skill-generator` excluded (upstream-pristine symlink, never edited).

## Guards

- **Triggers, `Use when` lists, and keyword phrases byte-identical** — they match user input and are not part of the grain.
- **No vocabulary edits** (Phase 17 owns word choice) and **no topology added**; existing topology is cut, not protected.
- **Compression, not amputation:** keep any clause a caller genuinely routes on; every skill must still route from its description alone.
- Frontmatter beyond `description:` untouched (`name:`, `loads:`, `allowed-tools`, `argument-hint`).
- "No change" legal per file; no padding anywhere.

## Verification

- Read the full manifest end to end post-edit: no mini-manual outlier left; no description restates a body procedure; no wiring clause remains except one kept deliberately and recorded in the plan.
- `git diff` shows only `description:` blocks changed; every trigger phrase byte-identical pre/post.
- Each edited skill still routes: its description states what + when unambiguously.
- Total loaded size of the edited descriptions drops — record pre/post character counts in the plan.

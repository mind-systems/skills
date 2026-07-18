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

**Wiring clauses across the loaded field — the closed disposition list.** The grain inventory above does not cover topology, but the field sweep does — so every wiring clause in the loaded field (`active/skills/`, `active/commands/`, `active/agents/`) is disposed here, and the sweep checks against this list instead of discovering the gap one clause per round. The discriminator: a clause naming **which skill loads, is loaded by, or produces for which** is topology → cut (its home is the `loads:` line or the body's reverse-graph marker); a clause naming **what this skill itself does**, or **the user's moment of use**, is concept or when-signal → stays.

- **Cut** (each entry opened for its wiring clause only; grain untouched, nothing padded):
  - `test-philosophy` — `Loaded by roadmap-test-coverage and roadmap-decompose-skeleton for the discriminator;` (the rule clause is this entry's when — no `Use when` added to compensate);
  - `orchestrator-artifacts` — the three-caller list (the candidates line above);
  - `roadmap-decompose` — `rendered per roadmap-engine's format` (the contract-line + task-spec concept stays; the engine name goes);
  - `roadmap-engine` — `written via note` (the two-tier concept stays; the edge goes);
  - `temporal-tree` — `(produced by roadmap-prune)` (reading the `## Features` table from ARCHITECTURE.md routes on its own).
- **Keep** — the sweep's closed exception list:
  - `editor`'s sole-caller clause — a routing negative the main loop reads before spawning;
  - `agent-architect`'s drives-a-persistent-editor-subagent clause — a behavior of the skill itself, not a load edge;
  - the **when-anchor class** — a clause naming a sibling skill as the user's moment of use, not a load relation (the named skill is not on the carrier's `loads:` line): `task-rescue-audit`'s "Run right after `task-rescue` while artifacts are warm", `temporal-tree`'s "Invoke after detangle …", and `aif-architecture`'s "or after /aif setup" (the file carries no `loads:` field at all, so `aif` cannot be a load edge — the clearest case of the class; the entry stays unopened).
- **Non-matches** (wording that names no edge). Own parameterization: `note`'s "caller-supplied…", `roadmap-engine`'s "Caller-agnostic: holds no decomposition philosophy of its own." Artifact-genre word collisions: `command-handoff`'s "durable note under `.ai-factory/handoffs/`" and `command-pin-gaps`' "Scan a plan/note/task…" — "note" names the output's genre, not a mechanism edge (contrast `roadmap-engine`'s `written via note`, cut above, which names how the artifact is produced). Never raise findings on these four.

**Untouched — already at grain, never padded:** `aif`, `aif-architecture`, `note`, `detangle`, `observe-logs`, `roadmap-outline`, `aif-docs`, `roadmap-prune` (near-grain; likely no change). `roadmap-decompose`, `roadmap-engine`, `temporal-tree`, `test-philosophy` are at grain too — each is opened solely for its wiring clause from the disposition list, nothing else in its entry touched. `aif-skill-generator` excluded (upstream-pristine symlink, never edited).

## Guards

- **Triggers, `Use when` lists, and keyword phrases byte-identical** — they match user input and are not part of the grain.
- **No vocabulary edits** (Phase 17 owns word choice) and **no topology added**; existing topology is cut, not protected.
- **Compression, not amputation:** keep any clause a caller genuinely routes on; every skill must still route from its description alone.
- Frontmatter beyond `description:` untouched (`name:`, `loads:`, `allowed-tools`, `argument-hint`).
- "No change" legal per file; no padding anywhere.

## Verification

- Read the full manifest end to end post-edit: no mini-manual outlier left; no description restates a body procedure; no wiring clause remains except the keeps on the disposition list. The sweep is decidable against that closed list — a wiring clause found outside it is a defect in this spec's inventory to reconcile, never a finding to loop the stage on.
- `git diff` shows only `description:` blocks changed; every trigger phrase byte-identical pre/post.
- Each edited skill still routes: its description states what + when unambiguously.
- Total loaded size of the edited descriptions drops — record pre/post character counts in the plan.

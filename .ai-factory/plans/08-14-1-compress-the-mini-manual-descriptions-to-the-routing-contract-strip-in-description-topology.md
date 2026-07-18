# Plan: 14.1 — Compress the mini-manual descriptions to the routing contract; strip in-description topology

## Context
Five `description:` fields (`task-rescue`, `task-rescue-audit`, `roadmap-test-coverage`, `roadmap-decompose-skeleton`, `editor`) restate body mechanism — repair-depth enumerations, the nine-verb pipeline, engine-sourcing, spawn protocol — in the always-loaded manifest, a drift-prone second home that buries the trigger. Each is cut back to the routing contract (what + when + concept, triggers byte-identical); three further candidates are judged by the same rule.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Decisions taken at plan time

- **`editor`'s sole-caller clause is kept, the spawn protocol is cut.** The main loop reads this description to decide whether to spawn the agent at all, so "the architect is the only caller — you never originate either mode on your own" is what it genuinely routes on (a routing negative, not decorative topology). "Spawn once at the start of a paired-loop session and keep it — send every subsequent round to the same spawn via SendMessage, never a fresh spawn per task" is operational protocol whose home is `agent-architect`'s body → cut. The duplicate second naming of the two modes (stated once in the opening sentence, restated in the trailing clause) is redundancy → collapse to one.
- **The discriminator that makes the sweep decidable.** A clause naming **which skill loads, is loaded by, or produces for which** is topology and gets cut. A clause naming **what this skill itself does** — including that it drives a subagent, or that its inputs are caller-supplied — is concept and stays. Every keep and cut below is decided by this one rule, and Task 8 checks against it rather than against caller-shaped wording.

- **Deliberately-kept clauses — the closed list Task 8 checks against (mirrors spec 74's disposition list).** Two keeps plus one keep-class survive this edit set:
  1. `editor`'s sole-caller clause (Task 5, reasoned above) — a routing negative the main loop reads before spawning.
  2. `agent-architect`'s editor-subagent clause — `drives a persistent editor subagent that applies every change while the architect never touches shared artifacts itself`. Under the discriminator this is concept, not wiring: it names a behavior of `agent-architect` itself, not a load edge, and a user deciding whether to invoke it genuinely routes on "this drives a second agent that does the editing". Kept whole (Task 7).
  3. The **when-anchor class** — a clause naming a sibling skill as the user's moment of use, not a load relation (the named skill is not on the carrier's `loads:` line): `task-rescue-audit`'s "Run right after `task-rescue` while artifacts are warm" (Task 2 preserves it by name) `temporal-tree`'s "Invoke after detangle …" (Task 6c leaves it byte-identical), and `aif-architecture`'s "or after /aif setup" — same class, and the clearest case of it: `aif-architecture` carries no `loads:` field at all, so `aif` cannot be a load edge; the clause names only when the user reaches for the skill. No task opens the file (Guard below keeps it out of scope), so this is a disposition on the closed list, not an edit.

  Nothing else survives. Any other clause naming an edge is cut by Tasks 3, 4, 5, 6, 6b, 6c, or 7.

  Note on scope vs. disposition: an entry being out of scope as "already at grain" disposes of **grain only** and says nothing about wiring — the two are separate axes (the same reasoning the `test-philosophy` decision rests on). So a kept clause in an unopened file still needs its disposition recorded here, or Task 8's sweep has no cover for it.

- **`agent-architect`'s rehydration sentence is cut** (Task 7, pinned here rather than left to the implementer). `Invoked by the user, re-rehydrates the role fresh on every invocation — the body carries zero session state.` restates body mechanics, and its routing half is already encoded mechanically in frontmatter (`user-invocable: true`, `disable-model-invocation: true`) — the manifest reader never needs the prose. Cut entire; it is **not** a third recorded keep.

- **`test-philosophy` joins the edit set for its caller list only** (Task 6b), as spec 74's disposition list instructs; the reasoning here is the verification. The already-at-grain judgment covers *grain* — the entry is short and unpadded, and stays so — while the wiring rule is a separate axis: `Loaded by roadmap-test-coverage and roadmap-decompose-skeleton for the discriminator;` is a reverse edge structurally identical to the one Task 6 cuts from `orchestrator-artifacts`, and the governing spec names exactly this construct as the coarse edit to avoid ([skill-description-field](../../docs/skill-description-field.md) § "The boundary: vocabulary, not topology"). The fact keeps its home: the body's reverse-graph marker is present (`src/skills/test-philosophy/SKILL.md:22-23`). Both named callers are inside this edit set, making it the manifest's most drift-exposed clause. Per the same disposition list, `roadmap-decompose`, `roadmap-engine`, and `temporal-tree` are opened for their wiring clauses only (Task 6c); no already-at-grain entry is opened for anything else.

- **For `test-philosophy`, the rule clause *is* the when.** The deleted caller list is that entry's only when-signal, and the entry is model-invocable — so the routing check has to be discharged deliberately. It is discharged without adding anything: the discriminator names its own moment of use (you are deciding whether a surface is worth testing), so `what + concept` routes this engine on its own. No `Use when` clause is authorized, and the no-padding guard stands. Task 8 checks against this decided answer instead of re-litigating it.

### Verdicts recorded during execution

Task 7 writes its two per-file verdicts here (this plan file), under this heading — the same place Task 8 appends its post-edit character column. No other artifact is a legal destination for them.

- **`agent-architect`**: cut. Deleted `Invoked by the user, re-rehydrates the role fresh on every invocation — the body carries zero session state.` (body mechanics; its routing half already lives in the `user-invocable:`/`disable-model-invocation:` frontmatter). Kept the drives-a-persistent-editor-subagent clause whole and the `Use when …` clause byte-identical.
- **`command-pin-gaps`**: no change. Already a what + when + concept entry — no procedure enumeration, no wiring clause in the description body (`loads: roadmap-engine` is a frontmatter field, not restated in prose). The fantasy-holes concept and the value-hole/meaning-hole distinction are what it routes on; nothing to cut.


## Pre-edit baseline (description body, whitespace-normalized characters, measured 2026-07-18)

| Skill | Pre | Post |
|---|---|---|
| `task-rescue` | 542 | 435 |
| `task-rescue-audit` | 739 | 620 |
| `roadmap-test-coverage` | 420 | 225 |
| `roadmap-decompose-skeleton` | 619 | 484 |
| `editor` | 628 | 354 |
| `agent-architect` | 547 | 438 |
| `orchestrator-artifacts` | 432 | 325 |
| `command-pin-gaps` | 420 | 420 |
| `test-philosophy` | 360 | 274 |
| `roadmap-decompose` | 378 | 340 |
| `roadmap-engine` | 303 | 285 |
| `temporal-tree` | 393 | 365 |
| **Total** | **5781** | **4565** |

### Round-1 review fixes (2026-07-18)

Review 1 found two compressions that narrowed or inverted the body's actual claim:

- **`roadmap-decompose-skeleton`**: the trailing async-I/O + stateful-buffer + lifecycle qualifier had drifted to scope all three extraction kinds instead of only the contract-task kind, contradicting the byte-identical `Use when … or shares a type surface` clause right after it. Re-attached the qualifier to the contract-task kind only: `Extracts skeleton, tests-first (filtered by the silent-failure rule), and no-prod-code contract tasks for surfaces mixing async I/O + stateful buffer + lifecycle.`
- **`roadmap-test-coverage`**: "drafting a test plan" claimed work the body's Layer 8 explicitly hands off to `/roadmap-decompose` and its hard rules forbid ("Never write ROADMAP_TESTS.md — that is `/roadmap-decompose`'s job"). Reworded to what the skill actually produces: `Filters areas by silent-failure risk, then researches each and writes up the findings.`
- **Nit (applied)**: `roadmap-engine`'s back-to-back "plus…plus" cadence — changed the first to `and`: `a ~600-char contract line and a full task spec — plus the shared create/update/check…`. Meaning unchanged.

Both findings' fixes and the nit are reflected in the Post column above; both trigger/`Use when` clauses stayed byte-identical.

## Guards (apply to every task below)

- Only the `description:` block changes in each targeted skill/agent/command file (this plan file's own verdict/count records are the one carve-out; spec 74's disposition inventory is pre-existing working-tree state, not an edit of this plan). `name:`, `loads:`, `allowed-tools`, `argument-hint`, `tools:`, `model:`, `effort:`, `user-invocable`, `disable-model-invocation` untouched.
- Every trigger phrase, `Use when` phrase, and quoted PASS literal byte-identical pre/post.
- No vocabulary edits (Phase 17 owns word choice) and no topology added.
- Compression, not amputation: each skill must still route from its description alone.
- "No change" is a legal outcome per file; never pad a terse entry.
- `aif-skill-generator` and all skills listed as already-at-grain in the spec are out of scope — do not open them for editing. The recorded exceptions are the four entries spec 74's disposition list opens for their wiring clause only: `test-philosophy` (Task 6b), `roadmap-decompose`, `roadmap-engine`, `temporal-tree` (Task 6c).

## Tasks

### Phase 1: Compress the five mini-manuals

- [x] **Task 1: task-rescue — cut the depth enumeration and sidecar mechanics**
  Files: `src/skills/task-rescue/SKILL.md`
  Rewrite the `description:` body. Cut the parenthetical depth list `(spec / spec+plan / spec+plan+code / plan-ratified-implementation-absent)` and the sidecar-rollback mechanics — both are Step 4/5 facts owned by the body. Keep: reads failed orchestrator artifacts, diagnoses how deep the root cause reaches and repairs to that depth, rolls the task's state back so the orchestrator re-validates from there (concept only, no mechanics), checks downstream tasks for the same gaps. Keep byte-identical: `Use when the pipeline stops with "PLAN_REVIEW_PASS never achieved" or "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone failed", "pipeline stopped".`

- [x] **Task 2: task-rescue-audit — compress the band-aid narrative and the on-smell clause chain**
  Files: `src/skills/task-rescue-audit/SKILL.md`
  The manifest's heaviest entry. Keep: outside-view audit of a task that looped or is a wall-clock outlier even if it passed; the converged-vs-band-aid question as the concept; chat-only output (no files, no ROADMAP edits); when to run. Compress the "band-aid accretion around one structural/spec gap the implementation routed around" narrative to a single clause, and collapse the three-way when-to-run chain ("right after task-rescue while artifacts are warm, or cold…, or in any session, on smell, when you suspect…") to one when-clause that preserves the warm/cold/on-smell entry points without the crutches-around-crooked-architecture elaboration. The warm entry point survives **by name** — "Run right after `task-rescue` while artifacts are warm" is a when-anchor keep per Decisions (names the user's moment, not a load edge; `task-rescue` is not on this skill's `loads:` line). Keep byte-identical: `Trigger phrases: "audit", "convergence audit", "did it converge or band-aid", "band-aid check", "outside-view audit".`

- [x] **Task 3: roadmap-test-coverage — drop the nine-verb pipeline narration and the hand-off**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Cut the enumerated pipeline ("Reads the roadmap, scans existing specs, filters areas by silent-failure risk, runs parallel deep-research agents per area, reviews testability, collects refactor findings, runs existing tests and classifies failures (API drift vs silent bug)") — that is the body's layer structure. Cut `then hands off to /roadmap-decompose` entirely (topology). Keep the opening sentence byte-identical: `Orchestrates full test coverage planning for a project.` — unhyphenated in the source; do not respell it (Phase 17 owns word choice). Keep the silent-failure risk filter as the *concept* it selects on (one clause, not a pipeline step). Keep byte-identical: `Use when you want a complete test plan from a roadmap with no prior test strategy.`

- [x] **Task 4: roadmap-decompose-skeleton — cut the engine-sourcing clause**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Delete `Renders via roadmap-engine, sources the test rule from test-philosophy — copies neither.` — that fact's home is the `loads:` line. Keep the spec-before-code axis as the concept and its contrast with atomic deliverability; compress the three-kind extraction enumeration (interface/abstract skeleton tasks, tests-first tasks, no-prod-code contract-tasks with the async-I/O + stateful-buffer + lifecycle condition) so the axis and the heavy/hazardous applicability survive without restating the body's split procedure. **The compressed enumeration drops the `test-philosophy` name with it** — "filtered by test-philosophy's silent-failure rule" names the same `loads:` edge the deleted sentence names, and one edge cannot be cut in one sentence and kept in the previous one; the concept survives as the bare silent-failure rule (pin the intent, e.g. "tests-first tasks filtered by the silent-failure rule" — not exact wording). Keep byte-identical: `Use when a task is heavy/hazardous or shares a type surface and needs splitting before implementation. Trigger: "skeleton", "tdd tasks", "concurrency contract".`

- [x] **Task 5: editor — cut the spawn protocol, keep the sole-caller routing negative**
  Files: `src/agents/editor.md`
  Per the plan-time decision above: delete `Spawn once at the start of a paired-loop session and keep it — send every subsequent round to the same spawn via SendMessage, never a fresh spawn per task.` Collapse the duplicated two-mode statement to one occurrence. Keep: the editor half of the architect↔editor paired loop; the two modes (reason independently over a relayed analysis target / apply a decided work-order exactly as written); self-verifying and reporting back by fact; and the sole-caller clause naming `agent-architect` as the only caller with the editor never originating work on its own. Frontmatter beyond `description:` (`tools:`, `model:`, `effort:`) untouched.

### Phase 2: Judge the candidates by the same rule

- [x] **Task 6: orchestrator-artifacts — cut the caller list** (depends on Task 5)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Delete `Loaded by task-rescue, task-rescue-audit, and roadmap-prune so each stops re-describing the layout inline.` — a reverse edge whose home is the body's reverse-graph marker (already present in §"Orchestrator Artifacts — the File Protocol"). Keep the protocol inventory, `Pure protocol reference, no procedure.`, and the `Use when reading or writing plans, plan-reviews, reviews, or sidecars under `.ai-factory/`.` clause byte-identical. Do not touch the body's reverse-graph marker sentence.

- [x] **Task 6b: test-philosophy — cut the caller list, nothing else** (depends on Task 6)
  Files: `src/skills/test-philosophy/SKILL.md`
  Per the plan-time decision above and spec 74's disposition list, this entry is opened for its wiring clause only. Delete exactly `Loaded by roadmap-test-coverage and roadmap-decompose-skeleton for the discriminator;` — a reverse edge whose home is the body's reverse-graph marker. Keep byte-identical: the opening `Shared testing philosophy for the roadmap family.`, the full silent/loud rule sentence `Holds one rule — write tests only for surfaces that fail silently (wrong output, no crash), skip surfaces that fail loudly (compile error, exception, DI failure, 4xx/5xx).`, and the trailing `holds no test-generation or coverage-pipeline logic.` (re-capitalize its leading `h` only if it becomes the sentence opener after the cut — that is punctuation repair, not a word change). Do not touch the body's reverse-graph marker or the body sentence naming the two callers. Do not pad: the entry is short and stays short, and per the Decisions ruling the rule clause serves as this entry's when — do **not** add a `Use when` clause to compensate for the deleted caller list.

- [x] **Task 6c: roadmap-decompose, roadmap-engine, temporal-tree — cut the three remaining edges from the spec's disposition list** (depends on Task 6b)
  Files: `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-engine/SKILL.md`, `src/skills/temporal-tree/SKILL.md`
  Each entry is opened for its wiring clause only — grain untouched, nothing else edited, nothing padded.
  - `roadmap-decompose`: drop `rendered per roadmap-engine's format` — the contract-line + task-spec concept stays intact without the engine name (pin the intent: the clause ends at the task-spec concept, not exact wording). Home: `roadmap-engine` is on this skill's `loads:` line.
  - `roadmap-engine`: drop `written via note` from `a full task spec written via note` — the two-tier concept stays. Home: `note` is on this skill's `loads:` line.
  - `temporal-tree`: delete the parenthetical `(produced by roadmap-prune)` — `reads the ## Features table from ARCHITECTURE.md` routes on its own; the provenance fact's home is `roadmap-prune`'s own description and body. Keep `Invoke after detangle when the reason behind a pattern is non-obvious or a change touches something previously refactored.` **byte-identical** — a when-anchor keep per Decisions (`detangle` is not on this skill's `loads:` line).

- [x] **Task 7: agent-architect and command-pin-gaps — judge, expect light or no change** (depends on Task 6c)
  Files: `src/skills/agent-architect/SKILL.md`, `src/commands/command-pin-gaps.md`
  Apply the discriminator and record the verdict per file as two lines under this plan file's "Verdicts recorded during execution" heading — that is the destination; there is no other legal one. "No change" is a legal outcome for either file.
  - `agent-architect`: **one cut, pinned at plan time — no judgment left to make.** Delete `Invoked by the user, re-rehydrates the role fresh on every invocation — the body carries zero session state.` (body mechanics; its routing half already lives in the `user-invocable:`/`disable-model-invocation:` frontmatter). Keep the drives-a-persistent-editor-subagent clause whole — concept under the discriminator, and one of the recorded keeps. Keep the `Use when …` clause byte-identical. Repair the sentence join only as punctuation if the cut leaves one.
  - `command-pin-gaps`: already a what + when + concept entry with no procedure enumeration or wiring — expect no change; do not cut the fantasy-holes concept or the value-hole/meaning-hole distinction, which is what it routes on.

### Phase 3: Verify

- [x] **Task 8: Verify the edit set** (depends on Task 7)
  Files: this plan file (post-edit count column only)
  - Read the manifest end to end and confirm: no mini-manual outlier left, no description restates a body procedure, and **the only surviving wiring clauses are the keeps on spec 74's disposition list, mirrored in Decisions** — `editor`'s sole-caller clause, `agent-architect`'s editor-subagent clause, and the three when-anchors (`task-rescue-audit`'s "Run right after `task-rescue`…", `temporal-tree`'s "Invoke after detangle…", `aif-architecture`'s "or after /aif setup"). The last sits in a file no task opens — it is a recorded keep, not an omission; do not raise a finding on it.
    - **Judge every candidate by the Decisions discriminator, not by caller-shaped wording**: names which skill loads, is loaded by, or produces for which → topology, must be gone; names what the skill itself does → concept, stays. By this rule `note`'s `Destination directory and section template are caller-supplied…` and `roadmap-engine`'s `Caller-agnostic: holds no decomposition philosophy of its own.` are **non-matches** — both describe their own parameterization and name no edge. Two further bare-word `note` collisions are non-matches for a different reason, and are listed here so no sweeper has to adjudicate them live: `command-handoff`'s `Always persists the handoff as a durable note under `.ai-factory/handoffs/`.` and `command-pin-gaps`' `Scan a plan/note/task for "fantasy holes"…` — in both, "note" names the output artifact's genre, not a mechanism edge (`note` sits on `command-handoff`'s `loads:` line; `command-pin-gaps` loads `roadmap-engine`, making it an even clearer non-match). Contrast `roadmap-engine`'s `written via note`, which Task 6c *does* cut because it names how the artifact is produced. Do not raise findings on any of these four.
    - **Scope the sweep to what is actually loaded**: the field is `active/skills/`, `active/commands/`, `active/agents/`. An entry present under `src/` but not symlinked into `active/` (e.g. `src/skills/aif-plan`, `src/skills/ui-ux-pro-max`) is not in the field — out of scope, no findings.
    - If a wiring clause turns up that is in the field, is not on the disposition list's keep side, and is not covered by the edit set: report it as a defect in spec 74's inventory to reconcile — the list is the closed home of dispositions; do not edit outside the plan.
  - `git diff` shows only `description:` blocks changed in the touched skill files; spec 74's disposition inventory and this plan file's own records are pre-existing working-tree state, expected in the diff. Confirm every trigger phrase and `Use when` clause listed in the tasks above is byte-identical pre/post.
  - Confirm each edited skill still routes. For `test-philosophy` the answer is already decided in Decisions — its rule clause is its when; do not re-litigate it or add a `Use when`.
  - Recompute the whitespace-normalized character count of each edited description and append a post column to the baseline table in this plan file. **Carry the pre value forward for any file whose verdict is no change**, so both columns total all twelve rows and are directly comparable; the post total must drop below 5781.

# Handoff — prune blocked: unpinned deferred observations

## 1. Frame

`/roadmap-prune` on the skills ROADMAP is blocked at its Step-0 gate: 42 unpinned
`## Deferred observations` entries across the review artifacts must be resolved and
pinned before the prune can run. The originating session's context isn't available
here — trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- this handoff — the block, the ~16 unique observations, the resolution path.
- `~/.claude/skills/roadmap-prune/SKILL.md` § Step 0 — the read-and-refuse gate and its exact resolution steps (handoff → resolution session pins every entry → re-run prune). The gate is not engineered around; it is parked here.
- `~/.claude/skills/orchestrator-artifacts/SKILL.md` §§ 5–6 — the `- Affects:` deferred-observation entry format (§5) and the status-marker grammar the resolution session writes (§6): `[fixed]` / `[routed → <path>]` / `[dismissed]`; **pinned = the entry line carries ≥1 marker**; markers only append (entry text and `Affects:` are never rewritten); **dedup — pinning one entry pins every occurrence across that task's review files** (dedup by `Affects:` target + gist).

### Read on demand
- The specific review files at the `file:line`s in § 3 — each observation's full reviewer text lives there. The files are still on disk: the blocked prune swept nothing.
- `~/projects/sakshi/skills/.ai-factory/ROADMAP.md` — the `[x]` slice the prune removes once unblocked (16 `[x]` tasks across Phases 2, 8, 13, 14, 15, 16, 17, 18); one open `[ ]` task, 19.1.
- `~/projects/sakshi/skills/.ai-factory/specs/78-aif-generates-to-norm.md` — the only OPEN task's spec, and therefore the only valid `[routed → …]` target.

## 3. Current state

**Done:**
- `/roadmap-prune` was run on `.ai-factory/ROADMAP.md`. Its Step-0 gate scanned `.ai-factory/plan-reviews/` and `.ai-factory/reviews/` repo-wide → **42 `- Affects:` entries, every one unpinned** (zero status markers) → the gate refused. No edits, no sweep, no ARCHITECTURE/ROADMAP change.

**In-flight:**
- The prune is PARKED. Nothing else pending.

**The 42 unpinned entries collapse to ~16 unique observations** (each recurs across review rounds 1/2/3 of the same task; a representative `file:line` given — full reviewer text is at that location; pinning one pins all its occurrences):

- `task 17.3` — 3 pre-existing `milestone` occurrences in roadmap-test-coverage `SKILL.md` outside Layer 5 → `reviews/01-8-1-…-review-1.md:77` (recurs in 8.1 review-2/3, plan-review-2/3)
- `roadmap-test-coverage` Layer 1 (`SKILL.md:40`) wording → `reviews/01-8-1-…-review-1.md:76` (review-2/3)
- plan Task 2, assertion 1 — failure-loudness wording → `reviews/01-8-1-…-review-3.md:73`
- both rescue `SKILL.md` H1 titles still `# Milestone Rescue` (Phase 17.3) → `reviews/02-16-1-…-review-1.md:63` (review-2, plan-review-1/2/3)
- orchestrator repo — task 8.2 gate / handoff 07 → `reviews/02-16-1-…-review-1.md:64` (review-2, plan-review-1/2/3)
- reverted philosophy-doc paragraph (curators of philosophy docs) → `reviews/02-16-1-…-review-2.md:68`
- `agent-architect` `SKILL.md:3–9` description framing (Phase 14.1 / follow-up desc pass) → `reviews/09-15-1-…-review-1.md:63` (review-2, plan-review-1/2/3)
- paired-loop vocabulary absent from registry (relay, channel-message, work-order) → `reviews/09-15-1-…-review-1.md:64` (review-2)
- `command-pin-gaps.md:17` `milestone` (task 17.4 / spec 65) → `reviews/04-17-2-…-review-1.md:66` (plan-review-2/3)
- `docs/skill-description-field.md` Finding 1 (spec 72 / spec 65) → `reviews/04-17-2-…-review-1.md:67` (review-2)
- residual `milestone` heading (spec 65, 17.4) → `reviews/05-17-3-…-review-1.md:62`
- `roadmap-prune` spec detail (spec 72) → `reviews/05-17-3-…-review-1.md:63`
- 17.5 contract line `[ ]` vs sidecar state → `reviews/07-17-5-…-review-1.md:61`
- spec 62 § Guards → `plan-reviews/03-17-1-…-plan-review-1.md:71`
- spec 68 Task 6 record (Phase 14.2) → `plan-reviews/05-17-3-…-plan-review-1.md:49`
- `test-philosophy` description — two consecutive `Ho…` (Phase 17 word choice) → `plan-reviews/08-14-1-…-plan-review-1.md:63`

**Uncommitted working-tree state:**
- This handoff (new, untracked). Nothing else — the prune made zero edits. All prior session work (Phase 2 alignment across the project families, the `docs/sakshi-harness/` docs, Phase 19 + spec 78) is already committed and pushed.

## 4. Next step

A dedicated resolution session works through **each** unpinned observation and disposes of it one of three ways, then sets the pin per `orchestrator-artifacts` § 6:
- **`[fixed]`** — the gap is fixed directly in that session;
- **`[routed → <path>]`** — routed into an OPEN task's spec; the only open task is `19.1`, so the only valid path is `.ai-factory/specs/78-aif-generates-to-norm.md` — never a completed or frozen spec;
- **`[dismissed]`** — evaluated and found moot, stale, or already handled.

Pinning one entry pins every occurrence across that task's review files (dedup by `Affects:` target + gist). When **every** entry is pinned, **re-run `/roadmap-prune`** — the gate passing is the resolution's proof, never manufactured.

Likely a large share are already moot: Phases 16/17 landed, so the `milestone`-title and `milestone`-occurrence observations may already be corrected in the tasks themselves or the later alignment work — but each such entry is disposed explicitly with a `[dismissed]` pin (with a one-line reason), never silently assumed.

## 5. Working discipline

- The user drives this handoff-then-resolution flow directly; the paired-loop editor is bypassed for it ("делай сам, без редактора").
- Pins are `[fixed]` / `[routed → <path>]` / `[dismissed]` only. Entry text and `Affects:` are never rewritten — markers only append to the end of the entry line.
- A `[routed → <path>]` target must resolve to an OPEN task's spec (only 19.1 / spec 78); routing into a completed or frozen spec is invalid.
- The gate passing is the resolution's proof — never faked, never engineered around, no partial prune.

## 6. Error log

- The prune run itself made no mistakes — the Step-0 gate correctly refused with zero edits.
- Architect process-note worth carrying forward: contract-line length was mis-enforced earlier this session as a "~600 hard cap," and several already-valid lines were trimmed on that false premise. `roadmap-engine`'s actual rule is **"target ~600, range 400–1000"** (`SKILL.md:102`). Do not re-trim a contract line that already sits under 1000.

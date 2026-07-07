# Handoff — aif-docs rewrite: docs skill writes the ТЗ

## 1. Frame

The **aif-docs lean-rewrite task** just landed in this repo's roadmap (open `[ ]` above `---STOP---`) with spec `.ai-factory/specs/10-aif-docs-rewrite-tz.md`; it was derived from a tradeoxy_core docs session that is the working model. Not implemented — this is the context for whoever rewrites the skill. Chat compacted; knowledge is in files, don't trust memory.

## 2. Read-first map

### Must-read now (to implement the rewrite)
- `.ai-factory/specs/10-aif-docs-rewrite-tz.md` — the task: what to delete, what to reframe, what to add. ← start here
- `src/skills/aif-docs/SKILL.md` — the file to rewrite; locate and delete every `3d`/`3д` / `MODE = 3D` / "Document-Driven Development" branch (Step 0.1 flag, the DDD section, Step 1 content-source, Step 2.1 staleness, Step 4 accuracy-verify, `argument-hint`, the `implementation must conform to` pointer).
- `src/skills/aif-docs/references/` — `topic-guides.md`, `consolidation.md`, `html-generation.md`, `REVIEW-CHECKLISTS.md`; the diet (notes 48/49) moved rare branches here — preserve that structure, keep the body ≤500 lines.

### Read on demand (the model — a **different repo**, `~/projects/tradeoxy/tradeoxy_core/`)
- `docs/backtest-replay/` — the exemplar: governing-spec docs written as behavior + invariants (the ТЗ voice, present tense), cross-linked internally and out to `indicator-engine/spec-v2/`.
- `docs/architecture.md` (lean overview, links out) + `.ai-factory/ARCHITECTURE.md` (canonical structural map, module mentions → topic docs) — the dedup-by-role + module→doc-tree model the rewrite should teach.

## 3. Current state

**Done:**
- Task authored two-tier: contract line in `.ai-factory/ROADMAP.md` + spec `specs/10-aif-docs-rewrite-tz.md`.

**In-flight:**
- Implementation — not started (orchestrator's job, separate run).

**Uncommitted working-tree state (this repo):**
- `.ai-factory/ROADMAP.md` (new `[ ]` line), `.ai-factory/specs/10-aif-docs-rewrite-tz.md` (new). Not committed.

## 4. Next step

Implement the aif-docs rewrite per spec 10: delete `3d`/`3д` wholesale; reframe the one remaining mode so the skill **writes the ТЗ** (behavior + invariants, present tense — Principle 6 stays); add cross-doc linking (a feature mention → its expanding doc; in ARCHITECTURE.md, module/subsystem mentions → topic docs, so docs grow into trees + sub-trees); reference the existing CLAUDE.md `## Documentation` index rather than reinventing it; cut the bloat. Verify: zero `3d`/`MODE = 3D`/`Document-Driven` tokens remain, file materially shorter, a plain run yields a present-tense behavior doc with cross-links.

## 5. Working discipline

- Chat plans; the orchestrator implements (separate run). No auto-commit — the user reviews and asks.
- Keep the skill **terse** — bloat is the whole complaint; a padded rewrite fails the task.
- English artifacts.

## 6. Error log

- The insight that must not be undone: the current aif-docs bloat is *what forced inventing 3d mode* (note 14). The fix is **deletion + reframe to one ТЗ mode**, not another mode. Do **not** re-add lead/lag meta-commentary — the present-tense-behavior voice already works both ahead of and behind the code; explaining that is the meta-bloat to avoid.

## 8. Domain model spine

- **Governing-spec pattern** (don't re-litigate): a behavior+invariants doc *is* the ТЗ and the reader doc at once — present tense, no history/motivation (state-not-process). Model: `~/projects/tradeoxy/tradeoxy_core/docs/backtest-replay/`.

## 9. Hard rules

- Never edit `upstream/ai-factory/` (pristine mirror). aif-docs is registered as ours / never-overwrite-from-upstream in `CLAUDE.md` — keep it so.
- Skill body ≤500 lines (repo norm); rare branches live in `references/`.

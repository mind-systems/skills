# Handoff — Deferred-observations harvest: review margins as a first-class artifact

## 1. Frame
We diagnosed an orchestrator non-convergence (tradeoxy_gui milestone 48) whose false failure exposed a systemic gap — reviewer margin notes ("latent", "forward risk", "no action needed") are never delivered downstream and get deleted by `roadmap-prune` — and we designed a delivery channel for them that spans the orchestrator's reviewer prompt and this skills repo. The chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `/Users/max/projects/tradeoxy/tradeoxy_gui/.ai-factory/reviews/48-phase-2-layout-indicator-ws-lifecycle-w2-review-3.md` — the canonical specimen: Findings 4/5 and Notes A/B show exactly what a "deferred observation" looks like in the wild, including the reviewer's own addressing ("Flagging now so Phase 3a's design accounts for it") ← lead with this
- `/Users/max/projects/orchestrator/orchestrator/prompts/reviewer.md` — the shared reviewer prompt where the `## Deferred observations` section must be added; note it currently has an "Output Format" skeleton with no home for non-blocking notes
- `/Users/max/projects/orchestrator/orchestrator/agents.py` (lines ~234–401) — proves the one-prompt-two-agents fact (PlanReviewer uses `reviewer.md` alone; PlannerReviewer concatenates planner + reviewer) and contains the two pending bug fixes (`review()` re-review branch, `implement()` patches_dir pointer)
- `~/.claude/skills/roadmap-prune/SKILL.md` — the skill that must gain the harvest step; it currently sweeps completed-work artifact dirs, which is what destroys the margins

### Read on demand
- `/Users/max/projects/tradeoxy/tradeoxy_gui/.ai-factory/reviews/48-phase-2-layout-indicator-ws-lifecycle-w2-review-1.md` and `-review-2.md` — the other two passes; show Note B recurring verbatim and the reviewer's anchoring across a persistent session
- `/Users/max/projects/orchestrator/orchestrator/main.py` (lines ~355–399) — shows review-file content is read exactly once and only on failure (into `PipelineStopError`); after `REVIEW_PASS` it's `mark_done()` + commit, nothing reads the file
- `/Users/max/projects/orchestrator/docs/non-convergence.md` — where the reviewer-anchoring failure mode (stale-verdict re-review in a persistent session) should eventually be documented
- `~/.claude/skills/milestone-rescue-audit/SKILL.md` — candidate secondary consumer: could read the deferred-observations layer during audits

## 3. Current state

**Done:**
- Diagnosed milestone 48's stop: a FALSE failure. The implementer had applied both review fixes (verified directly in the working tree: `track()` idempotency guard at `layout-indicator-subscription.service.ts:101-105`, `!= null` exception guard at line 66), but the persistent-session reviewer claimed the code was "byte-identical to passes 1 & 2" — it anchored on its own earlier verdict instead of rereading the diff.
- Traced the root cause in orchestrator code: `PlannerReviewer.review()` (agents.py:283-309) sends the same generic prompt every pass — unlike `plan()`, it has no re-review branch referencing the previous review file.
- Found a second bug: `Implementer.implement()` continuing-prompt (agents.py:371-374) points to `patches_dir`, which is never populated in implement mode (reviews go to `reviews_dir`; patches only get written in test mode, main.py:638). The implementer found the reviews anyway by its own initiative.
- Identified the structural asymmetry (with the tradeoxy GUI agent's independent analysis converging on the same point): reviews are binarized to pass/fail; non-blocking notes evaporate on success and are deleted at prune. The better the milestone went, the more certainly its margins are lost. Meanwhile those margins (milestone 48's Finding 4, Note B) were verified-real problems addressed to Phase 3a — the cheapest source of genuine architectural gaps, because the reviewer already did the verification work and only deprioritized against the *current* milestone.
- Settled the design (see §8 for the decisions).

**In-flight:**
- Nothing is edited yet anywhere. All four work items below are designed but not implemented.

**Uncommitted working-tree state:**
- Orchestrator repo: clean (this handoff note is the only new file, in the skills repo).
- tradeoxy_gui: milestone 48's implementation + review artifacts staged but uncommitted (the pipeline stopped before `mark_done()`); the code there is correct and includes both fixes.

## 4. Next step
Add the `## Deferred observations` section to `/Users/max/projects/orchestrator/orchestrator/prompts/reviewer.md` (one edit covers both plan-reviews and code-reviews, since both agents share that prompt), then update the `roadmap-prune` skill in this repo with a harvest step that sweeps **both** `.ai-factory/plan-reviews/` and `.ai-factory/reviews/` for those sections before deleting artifacts, promoting only entries with a concrete `Affects:` target into the addressed phases' spec notes. The orchestrator agent (chat session in ~/projects/orchestrator) owns the prompt edit; this repo owns the skill edit.

## 5. Working discipline
- Chat plans; the orchestrator implements. Do not edit application code without an explicit, unambiguous user request — the user confirms each concrete change before it lands.
- The user was offered the two agents.py bug fixes twice and has not yet said "do it" — treat them as approved-in-principle but ask before writing.
- Proposals are discussed in Russian; all artifacts (notes, prompts, skill files) are written in English.

## 6. Error log
- Initial instinct was to route the diagnosis through the `milestone-rescue-audit` skill; the user stopped it — "разбери сам флоу" — this was orchestrator-internals debugging, not a convergence audit. Correction: read the pipeline code and artifacts directly.
- Near-miss to avoid: an early framing treated `reviewer.md` as belonging only to the plan reviewer. Wrong — `_load_prompt("reviewer")` feeds BOTH `PlanReviewer` (as its whole system prompt) and `PlannerReviewer` (concatenated after the planner prompt). One edit, two destinations; do not create a second reviewer prompt file.

## 7. Orientation
- **Two reviewers, easy to conflate:** `PlanReviewer` (fresh session per attempt, reviews the *plan*, writes to `plan-reviews/`, signal `PLAN_REVIEW_PASS`) vs `PlannerReviewer.review()` (the *planner's own persistent session* reused to review *code*, writes to `reviews/`, signal `REVIEW_PASS`). "The planner is the code reviewer" is the non-obvious fact.
- **Two feedback dirs, one dead:** in implement mode, review feedback lives in `reviews/`; `patches/` stays empty (it is only populated in test mode). The implementer prompt currently points at the dead one.
- **Marker phrases** that identify deferred observations in existing (pre-standardization) reviews: "latent", "forward risk", "no action needed", "this milestone", "out of scope", "downstream phase must…", "worth reconsidering when X lands", "flagging so Phase N accounts for it", "Surface this to the orchestrator".

## 8. Domain model spine
- **Do not raise severity of deferred observations.** The pass/fail binarization is what makes the review loop converge; milestone 48's Finding 4 was *correctly* a non-blocker for its own milestone. The fix is a delivery channel, not a gate. Don't re-litigate. (Context: reviews 1–3 of milestone 48.)
- **Harvest needs an addressee filter.** Only entries with a concrete `Affects: <phase/spec-note>` target get promoted into downstream spec notes; unaddressed INFO-noise stays in the review file and dies with it. Otherwise prune smears noise across every open spec.
- **Harvest must hook into `roadmap-prune`, not into the orchestrator pipeline.** The orchestrator is deliberately dumb (file protocol + PASS markers); a per-milestone LLM harvest step would cost tokens on every run. Prune is the last exit before artifact deletion, is batch, and is already in the user's skill chain.
- **Review tails are pre-verified findings.** The reviewer already passed them through the "is this real" filter; only the "does it block *this* milestone" filter cut them. That's why mining them is cheaper than fresh gap-hunting — the verification work is done.

## 9. Hard rules
- Never commit without explicit permission (global rule; tradeoxy_gui's staged state is the orchestrator's business, not ours).
- All notes/prompts/skill content in English; no "See Also" sections, no history references ("X was added") in docs — describe current state only.
- Skill names must not leak into project CLAUDE.md files (routing is described in task terms).

## 10. Cross-cutting contracts / invariants checklist
- The standardized section is `## Deferred observations` with entry shape `- Affects: <phase/spec-note or "unknown"> — <one-paragraph observation>`; the rule for the reviewer: "everything you noticed but consciously did not block goes here, with an addressee."
- The section must be worded role-neutrally in `reviewer.md` (no "code" or "plan" specifics) because the same text serves both review types.
- Harvest sweeps BOTH `plan-reviews/` and `reviews/` — plan reviews suffer the identical evaporation asymmetry (`PLAN_REVIEW_PASS` first-try → notes never read), and the plan reviewer sees forward risks *earliest*.
- Signals stay as-is: `PLAN_REVIEW_PASS` / `REVIEW_PASS` on their own line, detected by `_has_signal()`; the new section must never interfere with signal detection (it precedes the signal line).

## 11. Per-unit map with watch-points
- **`prompts/reviewer.md` (orchestrator)** — gets the `## Deferred observations` section spec. Watch-point: the existing "Final Output Rule" (output only `done`) and the REVIEW_PASS placement rules must survive the edit; the new section must be defined as coming *before* the signal line.
- **`agents.py` `PlannerReviewer.review()` (orchestrator)** — pending fix: add a re-review branch (mirror `plan()`'s `plan_review_path` pattern) passing the previous review path with an explicit "don't trust session memory — reread each finding's file via Read, quote current line content, then verdict Fixed/Not Fixed". Watch-point: the session stays persistent by design (reviewer keeps planner context) — fix the prompt, not the session model.
- **`agents.py` `Implementer.implement()` (orchestrator)** — pending fix: continuing-prompt must point to the real feedback location in implement mode (`reviews_dir`), not the never-populated `patches_dir`. Watch-point: test mode legitimately uses `patches_dir` (main.py:638 bridges test output there) — don't break that path.
- **`roadmap-prune` skill (this repo)** — gains the harvest step: before sweeping artifact dirs, extract Deferred observations from both review dirs and promote `Affects:`-targeted entries into the addressed spec notes. Watch-point: prune is the *last* reader before deletion; harvest must run before any file removal, and pre-standardization reviews need the §7 marker-phrase heuristic as a fallback.
- **Possible new skill (this repo)** — distill the general method: mining review tails as the cheapest source of real architectural gaps. Not designed yet; the user said "возможно сделаю скилл из этого случая". The §7 markers + §8 "pre-verified findings" rationale are its seed.
- **`milestone-rescue-audit` skill (this repo)** — candidate minor edit: teach it to read the deferred-observations layer during audits. Low priority, not committed to.
- **tradeoxy side (NOT this repo's work)** — the GUI agent's "gap classes into a permanent checklist" idea and the retro-sweep of Orders Surface reviews belong to the tradeoxy project; excluded from the skills-repo scope deliberately.

# Handoff — grove topology & upward edges: tradeoxy findings for the CLAUDE-tree alignment tasks

## 1. Frame

On 2026-07-11 the tradeoxy family went through a full protocol-ratification + doc-topology session (external-integration pins, root-docs redistribution, three per-repo consistency sweeps, all committed); its findings must upgrade specs 24/39 — the CLAUDE.md-tree alignment tasks — and the family-pass pattern itself before those tasks run. The originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `.ai-factory/specs/39-tradeoxy-claude-md-tree-alignment.md` — the spec to amend; every finding below lands here first ← lead here
- `.ai-factory/specs/24-mind-claude-md-tree-alignment.md` — the mirror; amendments that are family-generic (not tradeoxy-specific) propagate into it
- `docs/context-tree.md` — the philosophy the amendments extend; the findings sharpen its "tree" into "grove" for multi-repo families
- `~/projects/tradeoxy/CLAUDE.md` + `~/projects/tradeoxy/tradeoxy_broker/CLAUDE.md` — live evidence: root routes down via tables, the leaf never names the root (one-directional edges)

### Read on demand
- `~/projects/tradeoxy/docs/architecture.md` — the rewritten cross-project map (transport, three auth tiers, shared infra); new ground truth the alignment pass must not treat as drift
- tradeoxy commits `d2aa9a9` (root), `4ee7361` (broker), `6f7c2d2` (core), `2fdece6` (analyst) — the 2026-07-11 state the spec's "Current state" section now lags

## 3. Current state

**Done:**
- tradeoxy external-integration protocol ratified and decomposed (core Phases 12/16, broker Phase 17, specs/notes on both sides); analyst handoff layer refreshed (handoffs 06/07/10 corrected, 11 added).
- Root docs redistributed: root `docs/` now holds **only** `architecture.md` (cross-project map); vendor references moved to their owners (core: `docs/exchange/ccxt-reference.md`, `docs/exchange/ccxt-ws-lifecycle.md`, `docs/nestjs-grpc.md`; broker: `docs/grpc-swift-2.md`); README doc-table removed; root CLAUDE.md gained a "Documentation routing" section codifying ownership.
- Three read-only per-repo consistency sweeps ran; all findings fixed and committed in the four hashes above.

**In-flight:** nothing — the tradeoxy side is stable and committed; this handoff is the only transfer artifact.

**Uncommitted working-tree state:** none relevant (tradeoxy root `docker-compose.yml` and core handoff 19 are foreign changes, deliberately untouched).

## 4. Next step

Amend `specs/39` (and mirror the family-generic parts into `specs/24` and any future family-alignment task) with the findings in §8/§10 below: the layout-guarantee premise that licenses hoist (stated, verified per family — **no** upward-edge lines in leaves), metric re-baselining at execution time, and drift-expectation calibration. Then re-check task lines 2.1/2.2 in `ROADMAP.md` for stale metrics they carry inline.

## 5. Working discipline

- The user rules by ratification — "the platform defines the contract" — and reads diffs himself; present findings as pins with rationale, flag anything pinned unilaterally for veto.
- Chat plans; the orchestrator implements. Alignment-task specs are planning artifacts — amend freely; never touch the target family's code from the skills repo.

## 6. Error log

- **Same-file self-contradiction while updating specs.** In tradeoxy-core, specs 18/19 had their *bodies* updated to "ratified" while their *headers and acceptance lines* still said "pending 3-way ratification / set-of-ids MVP" — caught only by a fresh-eyes sweep agent, not by the editor. Correction applied in core commit `6f7c2d2`. Lesson for the alignment pass: after editing a file's body, re-scan its header/intro/acceptance for the superseded claim — self-contradiction inside one file is the cheapest drift to create and the hardest for the author to see.
- **Wrong topology diagnosis, corrected twice.** The session first argued "hoist is unsafe because leaves are standalone repos" — refuted by verifying harness behavior: Claude Code loads parent-directory CLAUDE.mds, so a leaf session *does* see the root. The fallback recommendation — "then every leaf needs a written upward-edge line" — was refuted by the user's ruling: the family layout is *guaranteed* (README § Setup mandates the exact directory tree; relative proto/build paths depend on it), so the physical nesting + harness traversal **is** the edge, and a written back-pointer would be a second home for a mechanically-delivered fact — exactly the noise the alignment pass exists to remove. Final form: §8.1 — hoist is licensed by the stated layout guarantee; nothing is added to leaves.

## 7. Orientation

- "Tree" vs **"grove"**: `context-tree.md` models one repo's knowledge as one tree. A project *family* (tradeoxy, mind) is a grove — separate git repos, each leaf-CLAUDE committed to and published with *its own* repo, under a coordination root. The four operations (dedupe/hoist/conflicts/rules) are defined on a tree; the grove adds constraints (§8) without changing the operations.
- Two same-named layers in tradeoxy that the pass must not confuse: root `docs/architecture.md` (cross-project map, the only root doc) vs `tradeoxy_core/docs/architecture.md` (core's own, Russian, § Транспорт). Both are referenced as "architecture.md § …" from different places.

## 8. Domain model spine

1. **Hoist is licensed by the layout guarantee — state the premise, add nothing to leaves.** Verified live: a session with cwd inside `tradeoxy_broker/` loads global + root `tradeoxy/CLAUDE.md` + the leaf CLAUDE.md (harness parent-traversal crosses the git-repo boundary). And the family layout is **guaranteed** — README § Setup mandates the exact directory tree; relative proto/build paths depend on it — so the root trunk is always in a leaf session's context, by mechanics, not by convention. Consequences (user-ruled, don't re-litigate): hoisting shared meaning to the family root is safe; **no upward-edge lines in leaves** — the directory nesting is the edge, and a written back-pointer would be a second home for a mechanically-delivered fact (the very noise the pass removes). The amendment to specs 24/39 is one sentence: *name the layout guarantee as hoist's precondition and verify it per family* — a family whose layout is not guaranteed (or whose harness does not parent-load) must reconsider hoist before running the pass.
2. **Metrics in task lines are stratigraphy.** Spec 39 and task line 2.2 carry line counts (root 66, total 458) measured before 2026-07-11; the session grew the tree (root "Documentation routing" section, core/broker doc-index entries, analyst corrections). Per `context-tree.md`'s own supersession rule, a `[ ]` line describes the moment of its planning — the executor must **re-measure at execution and re-baseline the no-growth budget**, not trust the inline numbers. Generic amendment: family-pass specs should say "re-measure on entry" instead of embedding counts.
3. **Conflicts with ground truth are the expected case, not the edge case.** One session's sweeps caught three instruction-layer lies: analyst CLAUDE claimed "no code and no roadmap yet" (roadmap existed), root CLAUDE pointed at nonexistent `tradeoxy_broker/docs/concepts/` (actual: `docs/design/`), broker api-doc claimed gRPC default `50052` (code: `50053`, `configure.swift:162`). All fixed in the four commits. Calibration for the pass: budget the conflict-resolution operation as primary, not residual; the report contract (every conflict listed) will have real material.
4. **The pass inherits fresh 2026-07-11 content as ground truth, and some of it is its own dedupe input.** The root CLAUDE "Documentation routing" section is a hoist-artifact the pass may compress; the root CLAUDE "Cross-project invariants" section now partially duplicates root `docs/architecture.md` (§ Auth model / § Service identity) — a dedupe candidate (CLAUDE keeps the one-line invariant + pointer; the doc keeps the mass).

## 9. Hard rules

- Skills repo: nothing in the target family changes from here; the amendment targets are specs 24/39 + ROADMAP task lines only.
- tradeoxy artifacts are English-only by its own rule; skills docs are Russian, specs English — preserve each file's language.
- Never commit without explicit permission (the tradeoxy commits above were explicitly requested).

## 10. Cross-cutting contracts / invariants checklist

- No upward-edge lines in leaves — the layout guarantee + harness parent-traversal deliver the trunk mechanically; a written back-pointer is dedupe *input*, not an operation.
- The four operations stay as specced (dedupe / hoist / conflicts / rules hygiene); the grove adds two entry checks: topology determination (single repo vs grove; does the harness parent-load; is the layout guaranteed) and metric re-baseline.
- Rules-hygiene targets in spec 39 remain valid post-session: analyst `snake_case`/`PascalCase` block is still the live noise target; broker/core RULES.md still the passing genre (verified by reading them this session — proto-strings, branded UUIDs, nested-Content DTOs, no-incremental-migrations all counter-default with their why).
- Root keeps its ownership routing tables (already pinned in spec 39) — unchanged by these findings.

## 11. Per-unit map with watch-points

- **Spec 39 amendment** — add grove constraints + upward-edge operation + re-measure clause. *Watch:* the spec's "Current state" paragraph and the 458 total are stale against commits `d2aa9a9`/`4ee7361`/`6f7c2d2`/`2fdece6`; rewrite from fresh measurement, don't patch numbers in place.
- **Spec 24 mirror** — propagate only the family-generic parts (topology determination + layout-guarantee premise, re-baseline, conflict calibration). *Watch:* mind's topology may differ — verify whether its subprojects are separate git repos and whether its layout carries the same written guarantee before licensing hoist there; if the guarantee is absent, the pass must establish it (a documented layout mandate) before hoisting, not invent leaf back-pointers.
- **ROADMAP task lines 2.1/2.2** — carry inline line-counts too. *Watch:* per the two-tier discipline, keep the contract line ~600 chars — fold the amendment as "re-measure on entry" rather than new numbers.

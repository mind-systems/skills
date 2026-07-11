# Code Review: 1.14 — roadmap-decompose-skeleton: pyramid revision

**Target:** `src/skills/roadmap-decompose-skeleton/SKILL.md`
**Spec:** `.ai-factory/specs/34-roadmap-decompose-skeleton-pyramid-revision.md`
**Plan:** `.ai-factory/plans/83-1-14-roadmap-decompose-skeleton-pyramid-revision.md`

## Scope of change

Three code edits to the skill body (the other diffed files are planning artifacts — plan `.md`/`.json`, plan-review — not code). The revision removed leaked engine content and ceremony, per the audit:

1. **Call-graph ASCII block removed** (old lines 42–45). It merely restated the `loads:` frontmatter — pure ceremony. Removal loses no contract.
2. **Lens 2 discriminator restatement collapsed to a load** (lines 74–79). The inline spell-out of `test-philosophy`'s silent-failure rule ("write tests only for surfaces that fail *silently* … skip … *loudly* (compile error, exception, DI failure, 4xx/5xx)") was replaced with "Load `test-philosophy` once via the `Skill` tool, then apply its silent-failure discriminator to that surface." This is exactly what Critical Rule 2 mandates (do not copy the discriminator; load it).
3. **Numbering block delegated to the engine** (lines 128–131). The inline `N.M.1 … N.M.(k-1)` numbering procedure was replaced with a delegation to "`roadmap-engine`'s split sub-numbering rule (and its flat fallback)."

## Verification performed

**The delegation target genuinely exists and is behavior-identical.** The central runtime risk in edit #3 is a dangling reference — delegating to an engine rule that doesn't exist would leave the executor with no numbering procedure. Confirmed against `src/skills/roadmap-engine/SKILL.md:83-89`:

- **Split sub-numbering** (engine `:83-87`): children `N.M.1 … N.M.k` in chain order; original impl line renumbered to the **last child** `N.M.k`; `N.M` becomes the family prefix, outside references stay valid; never cascade-renumber the rest of the phase. This matches the removed inline text exactly (inserted milestones `N.M.1 … N.M.(k-1)`, original → `N.M.k`).
- **Flat fallback** (engine `:88-89`): a file/region with no phase headers keeps the flat unnumbered format. Matches the removed "unnumbered target → insertions stay unnumbered."

The skill-specific residue that the engine does **not** own is correctly retained inline: the chain order (skeleton → TDD/contract → …) and "its contract-line text and `Spec:` note tag stay unchanged." No behavior lost, no dangling reference — `roadmap-engine` is an already-declared `loads:` dependency and is loaded via `Skill` in Step 4, so the rule is in context when needed.

**No dependency-graph change.** No new `loads:` edge is introduced (edit #3 references an already-loaded engine), so no reverse-graph marker or frontmatter update is required.

**Guards honored.**
- Frontmatter byte-identical — `name`, `description`, `argument-hint`, `disable-model-invocation`, `allowed-tools`, `loads: roadmap-engine test-philosophy` all unchanged (`:1-16`).
- The three pinned decision contracts survive verbatim: fuse-at-1:1 (`:95-99`), standalone-scaffold-at-2+ (`:100-101`), heavy ≥2-of-{async I/O, buffer, lifecycle} (`:81-85`). Both canon anchors — m36 `PassThroughIndicator` (`:76-79`) and m37 `clearHeap()`/`drainHeap()` (`:87-90`) — intact.
- Restraint-first-class wording intact: Lens 1 (`:70-72`), Lens 3 (`:86-90`), Critical Rule 5 (`:143-145`).
- No content added or expanded; no `references/` subdirectory invented. The revision only removes/relinks — matching the spec's "revision, not a mandated rewrite."

**Behavior-identity.** Removing the inline discriminator changes nothing at runtime because the skill mandates loading `test-philosophy` (Load-once section `:37-38`, Lens 2 `:75`, Critical Rule 2 `:137-139`) and grants `Skill` in `allowed-tools`. This mirrors the identical treatment applied in sibling milestone 1.7 (roadmap-test-coverage). No loud/silent-failure classification is lost.

## Findings

None. The change is a faithful, behavior-identical pyramid revision: two ceremony/leak removals and one delegation to an engine rule that provably exists and matches the removed text.

REVIEW_PASS

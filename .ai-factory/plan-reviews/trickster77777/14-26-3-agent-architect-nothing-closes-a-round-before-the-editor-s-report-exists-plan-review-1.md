# Plan Review: agent-architect — nothing closes a round before the editor's report exists

**Plan reviewed:** `.ai-factory/plans/trickster77777/14-26-3-agent-architect-nothing-closes-a-round-before-the-editor-s-report-exists.md`
**Governing spec:** `.ai-factory/specs/trickster77777/92-nothing-closes-a-round-before-the-report.md` (Phase 26's header carries no `Governing spec:` of its own)
**Target file:** `src/skills/agent-architect/SKILL.md` — one additive `##` section
**Risk Level:** 🟢 Low
**Round:** 1

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): § "Composition: mechanism vs policy" governs extraction; this plan extracts nothing, adds no `loads:` edge, touches no frontmatter, and does not move content between `agent-architect`, `architect-editor-engine`, or `architect-pairing-engine`. `:22` already places `agent-architect` in `src/skills/` opposite the `editor` definition in `src/agents/` — no boundary crossed. **OK**
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (optional). `.ai-factory/skill-context/aif-review/SKILL.md` also absent. **WARN** (missing optional files only; nothing to enforce)
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md:90`, owner `trickster77777@gmail.com`): 26.3 is a live `[ ]` line under Phase 26; its `Spec:` tag resolves to `92-nothing-closes-a-round-before-the-report.md`, which exists and is the spec the plan cites. The phase's stated order 26.4 → 26.1 → 26.3 holds — both predecessors are `[x]` and both are in this file's git history (`27ab9cb`, `451c6b3`). Linkage intact. **OK**

## Ground truth re-checked

Nothing was taken on the plan's or the spec's word; every anchor was re-read fresh against the file (227 lines today):

- `## Relay on the marker; author a prompt in exactly one case` opens at `:94`; its last paragraph ends at `:174` with "…and an unmarked answer is yours to hold, not to forward." `## Review in parallel, reconcile before the apply order` opens at `:176`. Both of the plan's insertion anchors are exact, and both heading strings are unique in the file — the insertion point resolves unambiguously.
- The two passages the spec quotes as "current state" are intact and byte-matching, so the spec's premise still holds: the reconcile sentence ("Once the editor's report returns, reconcile your independent read against it…") sits at `:110-113`, and "Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go." sits at `:183-184` inside `## Review in parallel…`.
- The spec's fenced block satisfies all four content checks the plan's verification step names: the three closing artifacts are named ("not a summary of the payload, not a verdict on it, not an apply work-order"); "as finally as a verdict" and "addressed to the editor rather than the user" are both present verbatim; the parallel-pass guard is present ("what waits is the announcement, never the work"); the reason is stated, not implied ("its agreement can no longer be told from an echo"). The section is copyable as-is — no authoring judgment is left open, exactly as the plan claims.
- **No contradiction with the sections the new text sits between.** `## Spawn once, message thereafter` (`:32-36`) makes the first channel-message the spawn — "the first `::` relay or, where none has arrived, the first authored apply work-order" — which is reachable only when no round is open, so the new rule never blocks the spawn. The dead-editor path ("If the send fails, the editor is dead: report to the user **before anything is sent onward**") releases a *failure report*, not a closing artifact, so it is untouched. The flag-back path (carry a scope question to the user verbatim) likewise releases no summary, verdict, or work-order.
- **No contradiction with the pairing roles 26.4 introduced.** `architect-pairing-engine`'s deciding half addresses its apply work-order to the paired architect through the user rather than to its own editor; the new section's own principle — "where the round is settled is what counts, not who reads it" — covers that case rather than colliding with it, and the engine's "anything it does not name stays exactly as the generic skill has it" carries the rule into the paired session unchanged.
- **No propagation debt.** `grep -rn "Relay on the marker\|Review in parallel"` over `src/`, `docs/` and `.ai-factory/` finds live references only inside `agent-architect/SKILL.md` itself; every other hit is a historical spec. Nothing outside the file cites its line numbers or section list, so a pure insertion falsifies nothing elsewhere. `active/skills/agent-architect` is a symlink into `src/`, so the edit yields one working-tree entry.
- The guarded surfaces are real and untouched by an insertion at this boundary: the `::` mechanics (`:96-107`), the before/after-mark split, the enrichment gating (`:117-128`), the skill-expansion rule (`:139-152`), and the two-format statement (`:161-165`).
- SKILL.md body budget: 227 lines today, ~247 after — well inside the 500-line ceiling.
- The verification commands run as written against this tree: `grep -n "^## "` returns the eight headings, and `git diff --stat` is empty today (both plan artifacts are untracked), so "exactly one file changed" is a real post-condition.

## Critical Issues

**1. Both line-number corrections in "Notes for the implementer" are wrong, and the second one silently re-points a guard.** (`plan.md` § "Notes for the implementer", first bullet)

The note declares the contract line's `:76-79` / `:149-150` stale — correct — and then supplies replacements that do not match the file:

- "the reconcile sentence now sits around `:78-80`" — it sits at `:110-113`. Lines `:78-80` are inside the meta.json handle-recovery paragraph of `## Spawn once, message thereafter` ("…fall back to reading `~/.claude/projects/<project-key>/…`"), which has nothing to do with reconciliation.
- "the work-order-authoring sentence around `:154-155`" — the sentence the spec cites at `:149-150` is explicitly attributed there to `## Review in parallel, reconcile before the apply order` and is "Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go.", now at `:183-184`. `:154-155` is a *different* sentence in a *different* section: "You author your own prompt in exactly one case: the **apply work-order**, once the user has confirmed the edits." inside `## Relay on the marker…`.

This is not only hygiene. The plan's own guard says "do not fold the rule into the reconcile paragraph or the work-order-authoring paragraph it constrains" — and the second correction moves that guard's referent from the paragraph the spec protects to a neighbouring one, while leaving the paragraph the spec actually named unmentioned. An implementer who orients on the numbers (the note presents them as a fresh verification, unlike the plan's task body, which correctly says "Verified fresh in the file" only for `:94` and `:176`) reads handle-recovery prose for the first and guards the wrong sentence for the second.

Fix without adding numbers that will go stale again: state both positions the way the plan states its insertion anchors — by section plus opening words. E.g. "the reconcile sentence — 'Once the editor's report returns, reconcile your independent read against it…' in `## Relay on the marker…`; the work-order-authoring sentence — 'Draft the apply work-order only for what survives reconciliation…' in `## Review in parallel…`. Both are intact; resolve them by text, never by number."

Minor, in the same bullet: the shift is attributed to 26.1 alone, but 26.4 (`27ab9cb`) also edited this file before 26.1 (`451c6b3`) — both moved the cited lines.

## Positive Notes

- Anchoring the insertion on the two heading strings rather than on line numbers is the right call for a file three sibling tasks have already shifted, and the plan states it as a rule ("Anchor the insertion on those two heading strings, not on line numbers") instead of leaving it to be inferred.
- The plan does not copy the section text into itself — it points at the spec's fenced block as the one home and forbids paraphrase. That keeps a verbatim-pinned artifact from acquiring a second, drift-prone home in a runtime plan.
- The verification task restates the spec's four content checks as things to read back from the *file*, not from the plan, and pairs them with `git diff` evidence that the change is insertion-only — the guards are checked where they can actually fail.
- The register note ("states behavior and its reason in the present tense — it narrates no incident and no history") carries the spec's fourth guard into the plan at the point where an implementer might otherwise be tempted to explain why the section is new.
- Scope is drawn tightly and explicitly: `src/agents/editor.md` and `src/skills/architect-editor-engine/` are named as untouched, matching the spec's reasoning that neither the editor's discriminator nor the two channel-message formats change.
- The placement rationale is carried over rather than dropped: before `## Review in parallel…`, so the rule reads as governing every `::` relay instead of scoping itself to a review-shaped target.

## Deferred observations

- Affects: Phase 26 / `.ai-factory/specs/trickster77777/92-nothing-closes-a-round-before-the-report.md` — after this insertion the "agreement is indistinguishable from an echo" rationale is stated twice in one file: at `:127-128` ("The editor still reasons over the payload independently, which is the only way its agreement is real signal rather than manufactured echo", where it justifies the no-self-initiated-enrichment rule) and again in the new section's third paragraph, where it justifies holding the announcement. The two applications differ, and the spec argues deliberately that the rule must ship with its own reason, so this is defensible reinforcement rather than plain duplication — but under the repo's one-home-per-fact discipline it is the kind of pair that drifts when one of the two is later reworded. Closing it would require amending an existing sentence, which the spec's guard forbids and the plan therefore cannot do; it belongs to whoever next opens the relay section's spec.

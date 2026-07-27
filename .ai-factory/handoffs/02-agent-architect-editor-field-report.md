# Handoff — agent-architect ↔ editor paired loop: field report + user feedback from a long planning session

## 1. Frame

A field report to the skills project on how the `agent-architect` ↔ `editor` paired loop actually ran across one long, heavy planning session (a `tradeoxy_core` backtest-replay effort: a governing-model correction, two roadmap-phase decompositions, two `roadmap-decompose-skeleton` passes, four cross-repo handoffs). This is the architect's half — the editor writes its own, independent report separately (handoff 03). Both what held up and, the load-bearing part, where practice diverged from the prescribed skill plus the **user's explicit feedback** on the friction. The originating session's context is not available here — trust this report.

## 2. What worked (keep)

- **Dual independent agents on hard cruxes.** For every consequential decision — a correlation-key wire shape, an owner-resolution auth question, an async-determinism race, a cross-context handoff — the architect launched the warm editor **plus a second, fresh, independent agent** on the same question, then reconciled and verified the load-bearing claims by fact. This repeatedly caught real things the architect's own reasoning had missed (a `has_order_axis` inference consequence; a `setImmediate`-not-microtask race; a handoff-buffer gap). **The independent-second-agent move is the strongest part of the loop** and is currently an architect improvisation, not a prescribed step.
- **Verify-by-fact after every editor report.** The architect re-grepped/re-read the real files rather than trusting the report. Right discipline; kept the chain honest.
- **The private buffer.** A durable architect buffer (`.ai-factory/notes/NN-architect-buffer.md`) carrying the resolved-decision record survived several compacts and kept a very long model coherent.

## 3. Where practice diverged + the user's feedback (the actionable part)

The user's model of `::` differs from the skill's, and the skill under-specifies several things. In substance, verbatim from the user:

### 3.1 `::` is "two entities," not just a trailing marker — and mid-message splits must be deterministic
- The skill mandates a **trailing** `::`. The user routinely puts `::` **mid-message** as a split: everything **before** the mark is a command to **both** architect and editor; everything **after** is for the architect alone. The user also uses an **enrich pattern**: `<content> :: <"enrich this for the editor">` — the architect enriches the before-part and relays it.
- This **worked in this session but failed with a different architect**, who refused: *"the message doesn't end with `::`, the mark is in the middle, I won't relay or enrich."* The user does **not** want this per-architect randomness they must police every time.
- The user's mental model, stated directly: **`::` = two colons = two entities. The first `:` is the architect, the second `:` is the editor. They stand together, and everything before the mark unambiguously concerns both.** Consequence: a `::` message is a command to **both** — **the architect must do its own part, not merely relay to the editor.** In practice the architect often relayed and skipped its own work.
- → **Ask:** formalize the `::` grammar so mid-message split, the enrich pattern, and "before-the-mark = both entities, architect included" are deterministic, not architect-interpreted.

### 3.2 A `::` relay to the editor = research + feedback, never execute
- The editor frequently **ran the skill / edited artifacts** instead of reporting, when a `::` relay reached it. The user's model: a `::` relay is **plainly a command for research + feedback**, not an apply.
- → **Ask:** on a relay, the editor defaults to research/report and **does not edit**.

### 3.3 The editor edits artifacts ONLY on an explicit architect apply-order — and can't reliably tell task from research
- The editor **struggles to distinguish an apply-order (→ edit) from a research/investigation message (→ report only)**. It over-edited more than once in spirit. The user named this the single thing the skills-project agent should reason about hardest.
- → **Ask:** give the editor a sharp discriminator for "this is an apply-order" vs "this is a research relay." Editing is permitted **only** on an explicit architect apply-order.

## 4. The architect's own self-critique (mine, not the user's)

Several times I offered a **"parallel view" that was a prediction, not analysis** — and presented it as an independent review. On the two `roadmap-decompose-skeleton` passes my prediction was directionally right once and outright wrong once (the editor found a real task-split I had predicted "passes through untouched"). The user caught this and it was fair. → **The skill's "run your own review concurrently, reach your own verdict independently" needs teeth:** the architect must actually read the artifacts and run the lens, or explicitly label the output a prediction — never dress a guess as a parallel review. The single-editor relay is weakest exactly where the architect coasts; the dual-independent-agent pattern (§2) is strong because it forces real independent work — which is an argument for promoting it from improvisation to a prescribed move on consequential decisions.

## 5. For the skills project to reason about

1. **The `::` grammar** — mid-message split, the enrich pattern, "before-the-mark = both entities (architect does its own part)" (§3.1). Highest user-visible friction.
2. **The editor's task-vs-research discriminator** (§3.3) — the user's flagged top-priority fix; a relay ⇒ report, an apply-order ⇒ edit, and the editor must tell them apart without the user spelling it out.
3. **Whether the architect's "parallel review" must be genuine-analysis or explicitly-labelled-prediction** (§4).
4. **Whether the dual-independent-agent pattern should be prescribed** for consequential decisions rather than left to architect initiative.

## 6. Pointers

- `src/skills/agent-architect/SKILL.md` — the architect skill (the `::` grammar, spawn-once, review-in-parallel, apply-work-order rules live here).
- `src/agents/editor.md` — the editor agent (the task-vs-research discriminator belongs here).
- `.ai-factory/handoffs/03-...` — the editor's own independent field report on the same session (its half of this pair).

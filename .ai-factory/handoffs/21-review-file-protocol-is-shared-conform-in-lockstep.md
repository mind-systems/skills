# Handoff — the review-file protocol is a shared contract; conform it across both repos in lockstep

> From the orchestrator side, mid language-conformance. This is the reverse-direction counterpart to handoff `orchestrator/.ai-factory/handoffs/06-*`: that one brought the reserved-words language *into* the orchestrator; this one flags a shared surface the orchestrator cannot conform alone, because the skills repo is conforming the same surface at the same time.

## The realization (and the mistake that surfaced it)

The orchestrator's `reviewer.md` prompt **produces** review files whose format the skills repo **consumes**: the literal heading `## Deferred observations` and the `- Affects: <phase / spec-note path / "unknown">` entry line are scanned in three skills — `orchestrator-artifacts/SKILL.md` (§5), `roadmap-prune/SKILL.md` (the section scan), and `milestone-rescue-audit/SKILL.md`. The orchestrator's own `CLAUDE.md` already says any change to the review-section format must be reflected in `orchestrator-artifacts`.

While decomposing the orchestrator's prompt-conformance phase, an analysis "verified" that these strings must stay fixed by grepping the **current** skills code. That check was against the skills repo's **pre-conformance** state — the very strings both repos are now bringing under the reserved-words language. Grounding a cross-repo decision on the other repo's in-flight planning, not its landed code, is the trap. Hence this handoff: the decision belongs to whichever side conforms the protocol, and it must be one decision, applied on both sides together.

## The shared surface

Every string the orchestrator emits into a review or plan-review file and the skills consume literally is joint protocol, not private vocabulary:

- `## Deferred observations` — the review-section heading (reserved word: `deferred-observations`).
- `- Affects: <phase / spec-note path / "unknown">` — the entry line and its placeholders.
- `PLAN_REVIEW_PASS` / `REVIEW_PASS` — the PASS-signal literals (reserved word: `PASS-signal`).
- Artifact directory layout and per-roadmap stem subdirectories; sidecar fields.

For each, the reserved word is the **prose vocabulary**; the literal string is a **protocol token**. `PASS-signal` already models the split correctly — the reserved word is used in prose, the literal `PLAN_REVIEW_PASS` token is unchanged on both sides. The open question is whether `## Deferred observations` follows the same rule (heading stays a literal token, like `PLAN_REVIEW_PASS`) or gets rewritten to a kebab form.

## What the orchestrator side is doing about it (so it can't break you)

The orchestrator's prompt-conformance task (`orchestrator/.ai-factory/roadmaps/trickster77777.md`, Phase 7 / task 7.1) treats the heading `## Deferred observations`, the `Affects:` line, and its placeholders as **legacy — unchanged** — conforming only the surrounding descriptive prose. So the orchestrator does **not** unilaterally touch the shared protocol; a review file it produces after 7.1 still carries the exact strings your skills scan today. 7.1 is therefore safe to land in any order relative to your work.

## The decision, and the ask

**Does the skills-side language conformance intend to change any of these protocol literals?**

- **If no** — the heading and `Affects:` stay literal protocol tokens (same class as `PLAN_REVIEW_PASS`), conforming only prose that mentions `deferred-observations`. Then the orchestrator's "leave legacy" is already correct and stable; nothing to coordinate — just confirm it, so a later orchestrator task doesn't reopen it.
- **If yes** — it is a **coordinated protocol change**, and it must land as one lockstep pair: identical before/after strings specified in both a skills task and an orchestrator task, either landing together or with the orchestrator's task explicitly ordered to run **after** the skills change lands (grounding on your finished code, not your plan). A one-sided rewrite silently breaks the other repo's scan — the orchestrator emits a heading `roadmap-prune`/`task-rescue-audit` no longer matches, or vice versa.

## The general rule this instance teaches

Any cross-repo surface — review-section format, PASS-signal literals, sidecar fields, artifact naming — that the language touches is a joint contract. The orchestrator's tasks that would change such a surface must either run after the skills equivalent lands, or carry a spec whose before/after strings exactly match the skills side's. Where the surface can stay a literal token (the `PASS-signal` pattern), the cheapest coordination is to agree it stays legacy on both sides.

## Related, already in motion

The skill rename `milestone-rescue` / `milestone-rescue-audit` → `task-rescue` / `task-rescue-audit` (per handoff 06) is the same shape from the other direction: the skills repo renames, and the orchestrator's Phase 8 updates its live references to the new names. Land order there is looser (doc references only), but it is the same lockstep principle — the orchestrator's Phase 8 should reference whatever names the skills side has actually landed.

# Handoff — our docs are the ТЗ; the global CLAUDE.md forbids them from leading code

> Discussion/design handoff, not a parked task. Surfaced from a live orchestrator session. The problem is process-level — it lives in the global agent discipline (`src/global/CLAUDE.md`), not in any one repo. The owner states it directly: **"наши доки — это тех задание. Тех задание всегда впереди кода."** They have been fighting this same resistance for months across sessions; this is one more thread of it.

## 1. Frame

In this shop `docs/` is the **technical specification (ТЗ)**. A ТЗ is written *ahead* of code; code is then built and verified *against* it. "Code written without a ТЗ" is, in the owner's words, worthless. So the correct default is **doc-ahead-of-code**: a planned capability lands in the doc first, and implementation follows it.

Two pieces of `src/global/CLAUDE.md` make agents actively **resist** that default — they push the agent to treat every doc as a lagging *description of existing code* that may not describe anything not yet built. That inverts the owner's process.

## 2. The offending text (quote exactly)

**a) `## Documentation style` →**
> **Describe current state only.** Never reference what was changed, removed, or added. No "X was replaced", "Y was added". History belongs in commit messages.

**b) `## Grounding claims` →**
> Ground truth (code, command output, the actual file) overrides any description of it (docs, CLAUDE.md, handoffs, memory) — descriptions drift.

and

> …the leaf is code, on both sides of the spec: docs are the crown, code is the root system, and a chain that stops at a doc has not reached ground truth.

## 3. The incident, concretely (this session)

Asked to reflect a **planned** per-project config capability in `orchestrator/docs/configuration.md`, the agent refused to write it into the live doc and instead shunted it into a `docs/future/` folder — citing (a) "describe current state only" and (b) "ground truth overrides descriptions." It treated `configuration.md` as a description that must *lag* the code, when the owner wanted it as a ТЗ that *leads* the code. The owner then had to override the agent and order the doc updated ahead of implementation, the future-file deleted, and the parallel roadmap task + spec note removed (the doc is the spec now).

## 4. Why each bit harms — and what to preserve

The rules are **tangled**: each carries a genuinely good intent fused to the harmful one. Do not blanket-delete; separate the strands.

- **(a) "Describe current state only."** Its *body* is an anti-history-narration rule — don't write "X was replaced / Y was added" into docs; that's for commits. **Keep that.** But the *label* "current state only" overreaches its own body: read literally it forbids documenting intended / not-yet-built behavior — i.e. it forbids a ТЗ. The fix is to keep the anti-history intent while dropping the "only describe what already exists" reading.

- **(b) Grounding-claims doc-subordination.** "Ground truth (code) overrides any description (docs)" and "a chain that stops at a doc has not reached ground truth" are **true for description docs** — a doc written to describe existing behavior does drift, and code wins. They are **false for ТЗ/spec docs** — there the doc is the *intent*, and code is the artifact verified against it. When code and a spec-doc disagree, that is a *defect to reconcile*, not automatically "the doc is stale." The framing needs to name *stale description docs* as the thing code overrides, not docs categorically.

**Preserve intact:** "Describe behavior, not code"; "Comments never cite the plan layer"; and the read-**down-the-reference-chain** discipline in Grounding claims (don't act on a leaf in isolation) — that mechanic is orthogonal to doc-vs-code primacy and is valuable.

## 5. The family already half-believes the owner's side

`aif-docs`'s own charter describes documentation as **"a present-tense governing spec of behavior, protocols, data flows, and connections."** A *governing spec* leads — that is the ТЗ stance. So the skill family is **internally contradictory**: `aif-docs` says docs govern, while `src/global/CLAUDE.md` says docs merely describe current code and are overridden by it. The owner's position is already partly encoded; the global discipline contradicts it. Resolving in favor of docs-as-governing-spec removes an existing self-contradiction rather than inventing a new stance.

## 6. Recommendation (exact wording for the skills session to decide)

1. **Recognize two doc modes** in `src/global/CLAUDE.md`:
   - **ТЗ / spec (governing):** states intended behavior, present tense, **leads code**; code is verified against it.
   - **Reference / description:** describes existing behavior, may drift, ground-truth (code) wins.
   The "current state only" and "ground truth overrides docs" rules apply to the *description* mode only — never to a governing spec.
2. **Reword "Describe current state only"** into a pure anti-history-narration rule that does **not** forbid forward-looking specs — e.g. *"Docs state intended behavior in the present tense; they don't narrate change history (what was added/removed/replaced) — that's for commits."*
3. **Qualify the Grounding-claims doc-subordination** so code overrides a *stale description*, not a governing spec written ahead of it. Keep the read-the-chain paragraph.
4. **Sweep the doc-authoring skills** for the same lagging framing: `grep -rn "current state only\|describe.*current\|overrides.*description" src/skills` — `aif-docs` and any doc-update skill must not re-inject the "docs only describe existing code" reading the global file is losing.

Open question for the discussion: does the ТЗ-leads-code stance live only in `src/global/CLAUDE.md`, or is it also a line in `aif-docs` so the doc *generator* is explicit that a governing spec may precede its implementation?

## 7. One-line statement

Our docs are ТЗ — they lead code, not lag it; the global CLAUDE.md's "describe current state only" and "code is the only ground truth" rules must stop forbidding doc-ahead-of-code, while keeping the anti-history-narration and read-the-reference-chain disciplines they are currently fused to.

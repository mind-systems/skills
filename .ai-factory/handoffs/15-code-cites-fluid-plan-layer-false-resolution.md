# Handoff — code (and docs) cite the fluid plan layer; pruning turns the refs into *false* resolution

> Discussion/design handoff, not a parked task. Surfaced from a live tradeoxy_core session (paired architect↔editor loop). The problem is process-level — it lives in how the skill family produces and prunes plans, not in any one repo. Trust the files named below over this prose.

## 1. Frame

The skill family treats `.ai-factory/` (ROADMAP + specs + notes) as the working plan, and two habits have grown around it:

- **Implementers stamp provenance into code**: `// Phase 9.3.1 — …`, `// note 39`, `Phase 8.2 REST endpoint`, `see ROADMAP Phase 25 / Plan 12`. The comment names the *plan step that produced the code* instead of describing behaviour.
- **`roadmap-prune` recycles phase numbers**: `roadmap-engine` fixes phase numbers as **globally sequential with legal gaps** ("gaps are legal and expected (pruning leaves holes)"), and `roadmap-prune` moves completed phases out of ROADMAP into `ARCHITECTURE.md ## Features` (feature → commit hash). The freed numbers are then reused by later, unrelated directions.

Individually each habit is defensible. **Together they are a latent corruption**: once a phase is pruned and its number reused, every code comment that cited it now points at a *different, live* phase. The reference does not dangle — it **resolves to the wrong thing**. That is strictly worse than a dead link: a dead link stops a reader; a false resolution misinforms one who trusts it.

## 2. The failure, concretely (from tradeoxy_core)

The indicator-engine v2 build was phases 1–11; it was pruned. Those numbers were reused by unrelated live directions. So today:

| Code comment says… | Reader resolves against current ROADMAP → | Reality |
|---|---|---|
| `alert-engine.service.ts:15` — `Phase 8.1.2` (output-handler split) | `Phase 8 — External timeline intake` | unrelated |
| `indicator-runtime.service.ts` — `Phase 9.3.1 / 9.4.2 / 9.5.1` | `Phase 9 — Analyst activation` | unrelated |
| `replay-engine.ts:44` — `Phase 10.1` (backtest harness) | `Phase 10 — Service identity` | unrelated |
| `:529` — `Phase 11.1` (forming bucket) | `Phase 11 — Shared env keys` | unrelated |

`ARCHITECTURE.md ## Features` cannot rescue the reference: it anchors pruned work only coarsely (a feature name → one commit hash), never at sub-phase grain. So `Phase 8.1.2` has **no** correct resolution path anywhere — only an incorrect one.

Some references *do* still resolve (e.g. `Phase 6.2`/`7.1.2` in the replay branch, whose phases are still live). That is luck, not safety — the number is one prune away from being reused.

**Scale in one repo:** ~81 production-code comments + ~140 test comments carrying `Phase N.M`, plus ~23 `note NN` / `.ai-factory/specs|notes` path citations. This is a convention, not an accident — so assume comparable density in every repo the family has driven (the skills repo itself, mind_api, the broker).

## 3. Why this is a *skills-ecosystem* problem, not a tradeoxy_core bug

Nothing in the flow prevents it, and one thing actively arms it:

- **The planning layer legitimately cites itself.** A spec note referencing `spec 44`, a roadmap line carrying a `Spec:` tag, a decompose-skeleton milestone pointing "before its impl line" — all fine: they live and die together inside `.ai-factory/`, versioned as one surface. The rule is *not* "never cite a phase." It is **"nothing outside `.ai-factory/` may cite into it."**
- **The implementer carries the plan label across that boundary.** When a task spec says "annotate this," or the implementer simply narrates which task they are doing, the phase number leaks into a code comment — crossing from the ephemeral layer into the durable one, coupling durable code to the single most-rewritten surface in the repo.
- **`roadmap-prune`'s number reuse weaponizes the leak.** Reuse is a deliberate design choice (globally-sequential numbering, holes from pruning). On its own it is harmless — the plan layer self-heals. But every external citation of a reused number silently flips from correct to wrong at the moment of reuse. Prune has no idea a code comment depended on the number it just freed.

So the corruption is emergent across three skills (`roadmap-decompose*` produces the numbered surface, the implementer stamps it into code, `roadmap-prune` recycles the number) and no single skill owns the seam. That is why it is large: it is invisible at every local step and only manifests as a reader, months later, trusting a comment that now lies.

The same hazard extends to **docs and handoffs** that cite spec/note numbers — any durable artifact pointing into the ephemeral layer inherits the rot. This handoff itself cites tradeoxy_core spec 49 *by number*; that is acceptable only because a handoff is itself ephemeral discussion, not a durable resolution target.

## 4. The principle (the fix at the level of the rule)

> **Durable artifacts (code, tests, docs) never reference the fluid plan layer.** A comment either (a) explains behaviour/why, self-contained, or (b) links to a durable `docs/…` file that owns that behaviour. The roadmap/specs/notes may reference *themselves*; nothing outside `.ai-factory/` may reference *into* them.

Provenance/archaeology is a real need — but its home is **git history + `ARCHITECTURE.md ## Features`** (commit-anchored, reachable via `temporal-tree`), not a bare phase number frozen into a source comment. "Which task built this" is answered by `git blame` → the commit → the Features row; it must not be answered by a string the next prune will invalidate.

## 5. Remediation candidates (for this repo to decide)

The tradeoxy_core instance is already being fixed (see §6). The *class* fix belongs here:

1. **A rules-level ban (highest leverage), at two grains.** State the invariant above as a hard rule so it can't rot back in. Two places it could live, not exclusive:
   - **Generator grain** — add it to the rules the `aif` family emits (`rules/base.md`), so every repo the family sets up forbids code→plan citations from day one.
   - **Per-repo grain** — the sweep task (or `aif` on an existing repo) writes the invariant into that repo's own `.ai-factory/RULES.md`. *This exact variant was considered for the concrete tradeoxy_core task 34.6 and deliberately pulled back out* — baking a per-repo rule write into one cleanup task pre-empts the ecosystem-level decision this handoff is for. Flagged here as an option to rule on, not to hard-code task by task.
2. **Implementer contract.** Where a spec says "annotate," bind it to behaviour/docs, never a phase label. Consider a line in the decompose specs' rendered guidance that generated code comments cite `docs/` or behaviour only.
3. **A grep gate.** `grep -rIE "Phase [0-9]|note [0-9]{2}|\\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]" src` → nonzero fails. Cheap, mechanical, catches regressions the rule alone won't.
4. **Prune-time awareness (weaker).** `roadmap-prune` could warn when it frees a phase number that appears in code — but this is downstream of the leak; forbidding the citation upstream (1–3) is strictly better than detecting it after the fact.

Recommendation: **1 + 3** as the durable pair (rule + enforcement) — with the rule's *home* (generator `rules/base.md` vs per-repo `RULES.md` vs both) the open question for the skills discussion; 2 to stop new leaks at the source.

## 6. Local fix already in flight (tradeoxy_core)

- Task **34.6 — Purge roadmap/spec references from code comments** (`.ai-factory/ROADMAP.md`, Phase 34) + its spec **`.ai-factory/specs/49-purge-roadmap-refs-from-code.md`** carry the invariant, the (a)/(b)/(c) sweep method, and the "absolute — convert even the still-resolving refs" clause. It is a **pure code-comment sweep** — the anti-rot enforcement (writing the invariant into that repo's `RULES.md`) was deliberately *removed* from the task and referred to this discussion (§5.1, per-repo grain). That is the *instance* remediation of the mess; this handoff is the *class* one — including where the anti-rot rule should live.

## 7. Pointers

- The number-reuse mechanism: `src/skills/roadmap-engine/SKILL.md` (globally-sequential phase numbers, legal gaps) + `src/skills/roadmap-prune/SKILL.md` (moves completed phases to `ARCHITECTURE.md ## Features`, freeing the number).
- The coarse-anchor limitation: `ARCHITECTURE.md ## Features` is feature→commit, not sub-phase — so it is not a resolution path for `Phase N.M` code citations.
- Instance spec (by number, because this file is itself ephemeral): tradeoxy_core `.ai-factory/specs/49-purge-roadmap-refs-from-code.md`.

## 8. One-line statement

A durable artifact that cites the plan layer is a time bomb: it is correct until the next prune reuses the number, then it silently points at the wrong thing — so code, tests, and docs must cite behaviour or `docs/`, never the roadmap/specs/notes.

# Handoff (to self) — we built "the language"; next: review Phase 14, mind the pre-flight

> Rehydration handoff after a long session. This session gave the skills family a **formal language** — a reserved-words contract — and planned its rollout across the codebase (roadmap Phases 9–14). No skill code was touched; everything is planning + docs. **Read `docs/reserved-words.md` first** (the root CLAUDE.md now mandates it); it is the single source of truth for the vocabulary below.

## The one mental model to load first

The skills family is written in a **language**. Its two docs are the top of `docs/`:
- **`docs/reserved-words.md`** — the semantic contract: the fixed reserved words, their single canonical forms (multi-word terms are kebab-case like Claude's own `allowed-tools`), one-word-one-meaning. Binds everything the system *produces* (skills, descriptions, roadmaps, specs, docs) — **not** the user's input (the agent maps that by context). Naming rule: a reserved word takes a qualifier only to resolve a collision or mark a ≥2-member family (`task-spec`/`governing-spec`, `skill-description`/`skill-description-field`); otherwise single (`leaf`, `map`, `walk`, `seam`).
- **`docs/skill-description-field.md`** — how the language loads: the always-loaded `description:` fields form the **skill-description-field** (part of the system prompt); coherent vocabulary at an even abstraction-level makes flows self-run — the agent does a skill's work without invoking it. This is the emergent effect this whole session chased.

Retired/renamed vocabulary you must respect: `milestone` → **phase** (outline's product) / **task** (decompose's product, the `N.M` unit); `spec note` → **task-spec**; `field` (the layer) → **skill-description-field**; multi-word terms hyphenate (`contract-line`, `named-roadmap`, `governing-spec`, `ground-truth`, `PASS-signal`, `deferred-observations`). On-disk tags (`` Spec: ``, `Governing spec:`) and the `.ai-factory/specs/` dir stay **legacy** — never renamed (tag ≠ reserved word).

## Primary target — review Phase 14

Phase 14 (`skill-description-field: even abstraction-level`, specs **67/68/69**) is the second coherence axis: 9–13 conform the *vocabulary*, 14 levels the *altitude* so the flat description manifest reads as one document. It was decomposed **provisionally, before 9–13 landed**. Do:
1. Read specs 67/68/69 and the Phase 14 preamble in ROADMAP — check the three flow-grouped tasks (14.1 new-work sets the reference; 14.2 cleanup = exhaustive pole; 14.3 engines+standalones+whole-field capstone) are right.
2. **Do not run any 14.x task** until its pre-flight passes — **[handoff 19](19-phase-14-preflight-reverify-against-final-descriptions.md)** is the blocker (9–13 landed, the Phase-11 rename in place, poles re-confirmed, reference set against the *final* manifest). "No change" is a legal per-task outcome — the plan may find the field already even.
3. Guard the doctrine: level altitude/register only; **never** wire the flows/topology into descriptions (that is the rejected "amp" — coherence must *emerge* from vocabulary + altitude). Triggers/routing and vocabulary are untouched (9–13 owns vocabulary).

## What this session did (retrospective)

- **Started** with Phase 8 / spec 61: `roadmap-test-coverage` Layer 5 testability review reframed from binary DI-presence to **substitution-friction**, graded in `$STACK`'s test idiom (misfired on Python). Open, not run.
- **Built the language**: wrote `reserved-words.md` (the contract) and `skill-description-field.md` (the runtime); iterated hard on it with the user (kebab-case, `task-spec`, `skill-description`, the naming rule).
- **Reorganized `docs/`**: language pair at `docs/` top; the six narrative explainers moved to **`docs/philosophy/`**; `summary-field.md` → `skill-description-field.md` (rewritten in English). Deleted three skill-internal `docs/overview.md` garbage files.
- **Wired the language into the roots**: root `CLAUDE.md` gained `## The language` (mandates `skills/docs/reserved-words.md`, governs both sub-repos); `skills/CLAUDE.md` promoted the language pair to a "read first" subheading.
- **Swept every doc** to the contract (Russian docs carry the English reserved words as bare keywords).
- **Decomposed the "Language integration" direction** (Phases 9–13): 9.1 engines (spec 62), 10.1 new-work coupling + flagship `milestone`→phase/task (63), 11.1 cleanup coupling **+ renamed `milestone-rescue`→`task-rescue`, `milestone-rescue-audit`→`task-rescue-audit`** (64), 12.1 standalones (65, `aif-skill-generator` excluded = upstream), 13.1 docs-as-ТЗ doctrine + global-file vocabulary (66). Model: **one task per family** (don't make the orchestrator re-raise the same context); detail lives in the spec, not in splitting.
- **Wrote orchestrator handoff 06** (in the *orchestrator* repo, `orchestrator/.ai-factory/handoffs/06-…`): the cross-repo half — the language convention + the rescue rename it must follow.
- **Phase 2 audit**: verified tasks 2.1 (mind) / 2.2 (tradeoxy) are **CURRENT** (structure/rules/noise-target all match); the language does **not** complement them (their CLAUDE.mds don't speak workflow vocabulary — mind 0 hits, tradeoxy only the legacy `Governing spec:` tag). Pinned the mind README gap (`camera_ppg_kit` absent; `## Repository layout` not `## Setup`; no freshest-branch) into spec 24.
- **Pruned** the roadmap (`7072633 Roadmap prune`): folded completed Phases 1/3/4/5/6/7. ARCHITECTURE now carries the **Reserved-words language as a Foundation feature** (hash `a379ac9` = where the contract landed; phases 9–14 extend the row). Cleaned all legacy `notes/` and handoffs 01–16.

## Open decisions / state (do not re-litigate; do resolve)

- **Phase 13 doctrine wording is RATIFIED** (user "да, всё верно", 2026-07-13). Spec 66 Edits A/B/C (the three surgical `src/global/CLAUDE.md` grounding-rule rewrites: two doc-modes, code-overrides-*stale-description*, governing-spec-of-unbuilt-code-ends-at-the-doc) are final contract text — the orchestrator lands them verbatim, no re-litigation. The spec's proposal hedging is removed.
- **Nothing in 9–14 has been implemented** — all planning. The orchestrator runs them; conformance is vocabulary-only, deepest-first (engines → callers). Phase 8 and Phase 2 are also ready-to-run and independent.
- **Tone note:** the user's core discipline is **"our artifacts are the source of truth; the ТЗ leads the code."** They are *triggered* by any wording that reads as if a committed artifact is unfinished — do not call a landed doc "pending" (a pending *hash* for in-flight code is fine; a pending *contract* is not).

## Artifact map — read in this order to rehydrate

1. `docs/reserved-words.md` — the language contract (read first; root CLAUDE.md mandates it).
2. `docs/skill-description-field.md` — how it loads (the field / system prompt; the self-running-flows effect).
3. `.ai-factory/ROADMAP.md` — current state: Phase 8 (friction axis), Language integration 9–14, Experiments/Phase 2. The `[x]`/`[ ]` seam is empty (all pruned) — everything left is `[ ]`.
4. `.ai-factory/ARCHITECTURE.md` — the language Foundation feature + the prune ledger.
5. Specs, by phase: **67/68/69** (Phase 14 — your target), **62–66** (Language 9–13), **61** (Phase 8), **24/39** (Phase 2).
6. Handoffs: **19** (Phase 14 pre-flight blocker), **17** (docs-are-ТЗ, drives Phase 13), **18** (example email, folded into Phase 9). Orchestrator side: `orchestrator/.ai-factory/handoffs/06-…`.
7. Root `CLAUDE.md` § "The language"; `skills/CLAUDE.md` § "The language" (Documentation) — the mandate + index.
8. Background model (only if a claim needs it): `docs/philosophy/{skill-pyramid,context-tree,skill-cycle,skill-composition-model,context-grove,multiuser-roadmaps}.md`.

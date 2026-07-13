# skill-description-field altitude — the "new work" flow (sets the field reference)

Phase 14, task 14.1. The altitude axis of skill-description-field coherence. Governing spec: [skill-description-field](../../docs/skill-description-field.md) — "coherence = one vocabulary at one abstraction-level". Phases 9–13 do the vocabulary; this does the altitude.

**Precondition — runs after phases 9–13.** Altitude is read off the *final* descriptions (post-vocabulary-conformance). This spec is drafted against the current field; **re-verify it against the post-9–13 descriptions before running** — the specific outliers may shift.

## Method — level the flow's descriptions as one sub-document

1. Read the `description:` of the seven skills below **in sequence, as one text** — that is how the manifest loads them.
2. Assess **altitude**: how much detail each "what it does" packs. The target grain is *enough to route and convey the concept in one register* — not so terse it is vague, not an exhaustive multi-clause mini-manual. Assess **register**: the same voice across all seven.
3. Level the outliers to that shared grain. Because this flow is the most central and most-invoked, its levelled altitude is the **field reference** — record it (one sentence in the plan output describing the target grain) so 14.2 and 14.3 match it rather than inventing their own.

## Group (the "new work" flow)

`roadmap-outline`, `aif-docs`, `roadmap-decompose`, `agent-architect`, `editor` (`src/agents/editor.md`), `roadmap-decompose-skeleton`, `command-pin-gaps`.

## Guards

- **Triggers and routing are untouched.** The `Use when user says "…"` lists and keyword triggers stay verbatim — they match user input and are not part of the altitude.
- **No vocabulary.** Reserved-word tokens are already conformed by phase 10; do not re-touch them.
- **No topology — this is the microamp, not the amp.** Never add "then X" / "hands off to Y" / the chain into a description. The coherent reading emerges from even altitude, it is not welded in.
- **No behavior change.** A description is still a router entry; levelling grain must not drop information a caller needs to decide when to invoke.
- **"No change" is a legal outcome.** The plan may find the flow already even — then the implementer edits nothing and the review confirms nothing was done.
- **Re-verify before running** (precondition above).

## Verification

- The seven descriptions read at one altitude and one register as a sequence; no terse-vs-mini-manual jump between neighbors.
- Every trigger/keyword phrase is byte-identical to before.
- The plan output states the target reference grain in one sentence, for 14.2/14.3 to match.
- Each skill still routes correctly (its description still says what it does and when to call it).

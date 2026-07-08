# command-handoff: boundary-neutral framing + first-class narrative register

**Date:** 2026-07-09
**Source:** conversation context — this session produced two live failures of `command-handoff`: (1) the handoff it wrote (`skills` handoff 07) opened with "the chat is compacted", and the receiving skills agent immediately announced *"we had a compact, rehydrating"* — but **no compact ever happened**; the handoff was a cross-project context transfer. (2) Getting a narrative instead of the 11-section skeleton required the user to say *"не делай этот дурацкий нумерованный ноут… сделай повествование"* by hand — the skill has no first-class narrative path.

## Problem today

`command-handoff.md` over-fits to a single shape: **a post-compact, skeleton-form state-transfer.** Two independent over-fits fall out of that:

1. **Compact is hard-coded as the trigger.** The description (`command-handoff.md:3-6`) says *"lets the next agent (or yourself after /compact) rehydrate… Run this BEFORE /compact — while context is still full. After compact there is nothing left to mine."* The Frame skeleton (`:54-55`) bakes *"the chat is compacted but the knowledge is durable in files"* into every emitted handoff, and the example pointer (`:136`) repeats *"chat compacted, knowledge is in files."* A handoff is a general **context-transfer** artifact — the boundary it crosses is irrelevant to its content (this session's was cross-project, not a compact; per the user, cross-project is the common case). Asserting a compact that did not occur makes the receiving agent narrate a false premise.

2. **Both modes force the 11-section skeleton.** The only mode axis today is *destination* — chat mode (emit to chat) vs note mode (persist via `note`). Both render the same rigid skeleton. But some sessions are **understanding-transfers** (a reasoning journey to one or two decisions, where *why* must land before *what*), and for those a flowing narrative — the causal thread top-to-bottom, references appearing inline where they are load-bearing — beats a grid the reader must reassemble. The skeleton is right for **state-transfer** (many mechanical work-units mid-flight); it is wrong for understanding-transfer. Today the user must override by hand every time.

## The change (one file, two facets)

`src/commands/command-handoff.md`.

### Facet A — boundary-neutral framing

- **Description (`:3-6`):** drop the compact-exclusivity; keep the one true constraint — mine while the originating session's context is still live, because that is the only time there is something to mine. State the trigger by the *act* — transferring context to a future agent/session — **not** by enumerating boundary kinds. No taxonomy of boundary types belongs in the skill: listing them re-introduces the same over-fit in longer form and invites the receiving agent to classify and narrate a boundary that may not apply.
- **Frame skeleton (`:54-55`):** replace *"the chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory"* with a boundary-neutral line that asserts no compact — e.g. *"the originating session's context isn't available here — trust these files, not memory."*
- **Example pointer (`:136`):** replace *"chat compacted, knowledge is in files"* with a boundary-neutral equivalent.
- No compact-specific claim survives anywhere in the emitted-handoff text or its examples, and no replacement boundary taxonomy is introduced anywhere; `/compact` is not singled out as the trigger.

### Facet B — a first-class narrative register (a second, orthogonal axis)

Add a **register** axis, orthogonal to the existing note/chat **destination** axis:

- **Skeleton register (state-transfer)** — today's 11-section skeleton, unchanged. For sessions of mechanical progress across many work-units; the successor needs *what's done / what's next / what to re-check*.
- **Narrative register (understanding-transfer)** — flowing prose that carries the causal thread (the path walked, the false turns, the decision and its rationale). References to files/specs/notes appear **inline at the moment they are load-bearing**, not catalogued in a read-map. Still ends by making the durable next step and the working discipline explicit — woven into the prose, not sectioned away.

Selection:
- An explicit user cue wins — *narrative / повествование / story*, or a rejection of the numbered form (*"not the numbered skeleton"*).
- Otherwise infer from session shape: many mechanical units mid-flight → skeleton; a reasoning journey to one or two decisions → narrative.
- When genuinely ambiguous, default to skeleton (safe for state-transfer) and name the choice.

Narrative × destination:
- **Narrative + note destination:** the agent **composes the prose itself and `Write`s it directly** to `.ai-factory/handoffs/<NN>-<slug>.md` (existing numbering/slug mechanics; slug ≠ the literal word "handoff"). It does **not** route through `note` — `note` distils, and distillation flattens the exact causal thread the narrative exists to carry (the blank-skeleton lens in Step 3 is skeleton-only by construction). This is precisely what was done by hand this session for handoff 07.
- **Skeleton + note destination:** unchanged — still delegates to `note` with the blank skeleton as the mining lens.
- Both registers may also emit to chat (chat destination) instead of a file.

## Guards

- **Skeleton register is byte-identical** — its section names/order, the proportionality guard (`:46`), the read-first-map-scoped-to-next-step rule (`:48`), and the self-check gate (`:110`) are untouched. Facet B *adds* a register; it does not rewrite the skeleton.
- **Keep the "mine while context is live" truth** — only its compact-exclusivity is removed, not the timing discipline (a handoff written after context is already gone has nothing to mine — still true, boundary-agnostic).
- **Narrative is not a licence to bloat** — the proportionality principle applies to both registers: a small session yields a short narrative; a trivial session padded to migration-guide length is still a failure.
- **Keep the note/chat destination axis** — register is a *second* axis, orthogonal to destination; do not collapse the two into one four-way enum that loses the distinction.
- `allowed-tools` already includes `Write`, `Skill`, and the `note` loader — no frontmatter change is needed for narrative-writes-directly.

## How to verify

1. `grep -ni "compact" src/commands/command-handoff.md` → `/compact` is not singled out as the trigger and no enumerated list of boundary kinds replaces it; compact is absent from the Frame skeleton (`:54-55`) and the example pointer (`:136`); no emitted-handoff text asserts a compact occurred.
2. The skill defines a **register** axis (skeleton | narrative) with a selection heuristic (explicit cue → else session shape → else default skeleton), described as orthogonal to the note/chat destination axis.
3. Narrative + note destination: the skill has the agent compose prose and `Write` directly to `.ai-factory/handoffs/`, **explicitly not** via `note`'s distiller; skeleton + note destination still delegates to `note`.
4. `git diff` shows the skeleton section (its 11 sections, proportionality/read-map/self-check paragraphs) unchanged apart from the Facet-A wording edits and the new register-axis prose.
5. Baseline: this session's handoff 07 — narrative, written directly to `.ai-factory/handoffs/`, boundary-neutral (no compact claim) — is exactly what the narrative register + Facet A would now produce without the user having to override by hand.

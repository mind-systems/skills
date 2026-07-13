# Doctrine + conformance: the global CLAUDE.md leads code with docs, and speaks reserved-words

Phase 13 of the Language-integration direction. Two moves on `src/global/CLAUDE.md`, one file, one context (make the most-loaded discipline file both *correct* and *current*): **Part 1** the docs-lead-code doctrine from [handoff 17](../handoffs/17-docs-are-tz-must-lead-code.md), **Part 2** the reserved-words vocabulary conformance the global file itself still lacks. The global file is the most authoritative always-loaded surface in the environment — it must speak the language it defines.

## Part 1 — the doctrine (wording ratified — land verbatim)

Two rules make agents treat every doc as a *lagging description of existing code*, so an agent refuses to write a **planned** capability into a live doc (the live incident). The fix recognizes **two doc modes** — a `governing-spec` that *leads* code, and a description that *lags* it — and scopes the "current state only" / "code overrides docs" rules to the description mode. This is not a retreat from grounding; it is the same two-axis scoping already in `reserved-words.md` (`governing-spec` = what must be, `ground-truth` = what is), raised into the global file. **These are the most load-bearing sentences in the environment — the wording below is ratified; land Edits A/B/C verbatim.**

**Current offending text:**
- § Documentation style: "**Describe current state only.** Never reference what was changed, removed, or added. No "X was replaced", "Y was added". History belongs in commit messages."
- § Grounding claims para 1, first sentence: "Ground truth (code, command output, the actual file) overrides any description of it (docs, CLAUDE.md, handoffs, memory) — descriptions drift."
- § Grounding claims para 2, last clause: "…and a chain that stops at a doc has not reached ground truth."

**Edit A** — § Documentation style bullet →
> **Present tense, not change history.** A doc states behavior in the present tense — a governing-spec states *intended* behavior whether the code exists yet or not, a description states *existing* behavior. Neither narrates change history: no "X was replaced", "Y was added" — that belongs in commit messages.

**Edit B** — § Grounding claims para 1, first sentence →
> ground-truth (code, command output, the actual file) overrides any **description** of it (a description doc, CLAUDE.md, handoff, memory) — descriptions drift. That subordination is the *description* mode: a doc written to record existing behavior lags its code, and code wins. A governing-spec (a ТЗ) is the other mode — it states intended behavior *ahead* of code, which is then built and verified against it; when a governing-spec and its code disagree, that is a defect to reconcile, not automatically a stale doc.

**Edit C** — § Grounding claims para 2, last clause →
> …a chain that stops at a doc has not reached ground-truth — *when the question is what the system does now*. A governing-spec answers a different question, what it must do, and legitimately terminates at the doc when the code it governs is not built yet; there the doc is the ground-truth of intent.

**Doc-skills sweep** — `aif-docs` already aligns: its no-motivation pass (line 182) says "describe the **current (or target)** state in present tense" — it already permits target (not-yet-built) behavior. `aif-architecture` carries no lagging framing. **Audit-clean, no change.**

## Part 2 — vocabulary conformance of the global file

The global CLAUDE.md still spells the old vocabulary; conform it (kebab reserved words, per the folded-in decision):
- `spec note` → **`task-spec`**: line 5 ("a task line names its spec note" and "its named spec note sits unread"), 26, 49, 51.
- `contract line` / "task line" / "roadmap line" (all denoting the ~600-char task line) → **`contract-line`**: line 5 ("a task line names…", "a task's roadmap line"), 26, 51 (×2), 53.
- `ground truth` / `Ground truth` → **`ground-truth`**: lines 5, 7 — these sit inside Edits B/C above and are already kebab there.
- `Named roadmap` → **`named-roadmap`**: line 11.
- `two-tier` (51) already canonical.
- **Leave**: "fields" (15, "not list methods, fields, event types" — generic).

## Files & types

`src/global/CLAUDE.md` only (surfaced to `~/.claude/CLAUDE.md` via symlink). No skill bodies edited — the doc-skills sweep is a verification, not a change.

## Guards

- **Preserve intact:** the read-down-the-reference-chain discipline (para 1), held-context-decays (para 3), the roadmap time-map / `[x]`-is-history paragraph (para 4), and the § Documentation style bullets "Describe behavior, not code", "Comments never cite the plan layer", "Docs form a walkable tree". The doctrine touches *doc-vs-code primacy* only; the walk mechanics are orthogonal and stay.
- **Not a retreat from grounding.** Code still wins over a *stale description*, and to know what the system *does now* you still reach the code leaf. The only thing added: a governing-spec of not-yet-built behavior is authoritative and legitimately terminates at the doc.
- **Vocabulary is mechanical, doctrine is ratified.** Part 2 renames tokens with zero meaning change; Part 1's wording is ratified — land Edits A/B/C verbatim, no re-litigation. Casing lowercase kebab even at a sentence start (`ground-truth (code…) overrides…`).
- **Named-roadmap doctrine sentence** (para 4, "Named roadmaps under `.ai-factory/roadmaps/`…") — the token `named-roadmap` conforms; the sentence's meaning is untouched.
- No skill behavior changes; verified by re-reading, not by a run.

## Verification

- § Grounding claims names two modes (description subordinate to code; governing-spec leads code and is verified against it); § Documentation style's bullet permits present-tense *intended* behavior while still forbidding change-history narration.
- `grep -inE "current state only|spec note|contract line|task line|roadmap line|[^-]ground truth|Named roadmap" src/global/CLAUDE.md` → zero.
- The read-the-chain, held-context-decays, and time-map paragraphs keep their meaning (only the tokens `task-spec` / `contract-line` / `named-roadmap` / `ground-truth` replace the old spellings).
- `grep -inE "current \(or target\)" src/skills/aif-docs/SKILL.md` → still present (aif-docs already aligned; no edit).
- Re-read § Grounding claims: an agent asked to write a *planned* capability into a live doc now writes it (doc leads code), while an agent verifying *what the system does* still walks to the code leaf.

# Code Review — command-handoff: boundary-neutral framing + first-class narrative register

**Plan:** `.ai-factory/plans/60-command-handoff-boundary-neutral-framing-first-class-narrative-register.md`
**Governing spec:** `.ai-factory/specs/14-handoff-narrative-register-boundary-neutral.md`
**Changed file:** `src/commands/command-handoff.md` (single file; the other staged files are planning artifacts)

## What was verified

- **Facet A — boundary-neutral framing:** `grep -ni "compact" src/commands/command-handoff.md` returns nothing (exit 1). The description (`:2-8`) triggers by the *act* ("transfers context to a future agent or session") and keeps the one true timing truth ("while the originating session's context is still live"), with no boundary taxonomy. The Frame skeleton line (`:63-64`) and the example pointer (`:161`) are both boundary-neutral and assert no compact. Matches spec Facet A and verification steps 1.
- **Facet B — register axis:** the register axis (`:19-23`) is defined as explicitly orthogonal to the destination axis ("do not collapse them into one four-way enum"), with the full selection heuristic (explicit cue → session shape → default skeleton, name the choice). Narrative + note routes to a direct `Write` and explicitly *not* through `note`, with the distiller-flattens-the-thread rationale stated (`:140`). Skeleton + note is unchanged (`:131-138`). Matches spec Facet B and verification steps 2–3.
- **All three destination-only note-mode paragraphs reconciled:** the original `:18` (now `:25`), `:108` (now `:121`), and `:118`/Step-3 (now `:129-131`) are each rewritten register-aware — the agent mines/composes itself for chat (either register) and for narrative+note; only skeleton+note delegates to `note`. No surviving text asserts "note ⇒ agent does not mine." This was the exact class review-1 and review-2 gated on; it is closed.
- **Guards intact (byte-identical):** the proportionality guard (spec `:46`, now `:55`), the read-first-map rule (spec `:48`, now `:57`), and the self-check gate (spec `:110`, now `:123`) are unchanged in the diff. The 11 section names and their order (`:60-114`) are untouched; only the Frame prose changed, exactly as Facet A mandates. The self-check gate's "chat mode / note mode" vocabulary stays valid because the destination axis is still literally named "Note mode / Chat mode" (`:16-17`).
- **Tooling:** the narrative direct-write path uses `Bash(ls *)`/`Glob` (scan), `Bash(mkdir *)` (mkdir), and `Write` — all already in `allowed-tools`; no frontmatter grant was needed, as the plan claimed.

## Findings

### 1. (Minor) Narrative direct-write numbering diverges from the `note` engine's contract — inconsistent width in an empty `handoffs/`

`src/commands/command-handoff.md:142` tells the agent: *"`<NN>` is the current max numeric prefix + 1, zero-padded to match the existing files' width."* But the `note` engine — which owns numbering for the *other* note-destination path writing into the **same** directory — specifies a fixed rule (`src/skills/note/SKILL.md:53-55`): *"`<NN>` is a zero-padded **two-digit** sequence number (`01`, `02`, `03` …). … If no numbered files exist yet, **start at `01`**."*

Both note-destination registers write into `.ai-factory/handoffs/`, so their numbering must be interchangeable. Two gaps:

- **Empty-directory start is undefined on the narrative path.** "match the existing files' width" has no defined width when there are no existing files, and the narrative branch never states the "start at 01" fallback that `note` does. An agent could reasonably emit `1-<slug>.md` (one digit) as the first file.
- **A one-digit first file desyncs the two paths.** If the narrative path writes `1-foo.md`, a later skeleton+note handoff invokes `note`, whose scan matches only `[0-9][0-9]-*.md` (`note` SKILL `:55`,`:113`) — it would not see `1-foo.md`, restart at `01`, and produce out-of-order/overlapping numbering.

**Failure scenario:** `.ai-factory/handoffs/` is empty → a narrative-shaped session runs `/command-handoff note` → agent follows `:142`, writes `1-<slug>.md` → next skeleton+note handoff calls `note`, which scans `[0-9][0-9]-*.md`, finds nothing matching, and writes `01-<slug>.md`, breaking sequential ordering.

**Impact is low in this repo** — `.ai-factory/handoffs/` already holds `01`…`08` (two-digit), so today the "match existing width" rule yields `09` and coincides with `note`'s behavior. The defect only surfaces from an empty directory. **Fix:** mirror `note`'s exact rule verbatim on the narrative path — "zero-padded **two-digit** sequence; start at `01` if no `[0-9][0-9]-*.md` files exist" — rather than the looser "match existing width," so the two note-destination paths stay interchangeable regardless of directory state.

## Non-blocking observations

- The guarded self-check gate (`:123`) is skeleton-framed ("avoid every mistake in the error log", "for each subsystem touched … what it became", "recurring contracts"). When applied to a narrative draft (the narrative guidance at `:117` precedes it) these criteria read as skeleton-shaped. This is *not* a defect: the spec mandates the self-check byte-identical, so the slight framing mismatch is an accepted consequence of that guard, not something to change here.

---

One minor, edge-case finding; no blocking correctness or security issues. The milestone's intent — boundary-neutral framing plus an orthogonal, first-class narrative register with the skeleton path preserved byte-identical — is faithfully implemented.

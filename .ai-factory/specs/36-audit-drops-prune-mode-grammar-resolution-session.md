# milestone-rescue-audit: drop prune mode; the marker grammar passes to the resolution session

## Current state

`src/skills/milestone-rescue-audit/SKILL.md` carries two modes; the `prune` mode's disposal **promotes** still-real deferred observations — appending them verbatim into the file their `Affects:` names — and its routing test is "the path resolves to an existing file". Live incident (tradeoxy_core, `.ai-factory/notes/58-prune-audit-hands-off-not-promotes.md`): promote grafted reviewer jargon into the specs of completed `[x]` tasks and into `ARCHITECTURE.md` — finished artifacts are records, not editable surfaces, and the existence test cannot tell an open spec from a frozen one. The "gate can pass" state it manufactures is illusory: observations get relocated, not resolved. The marker grammar lives in `orchestrator-artifacts` § 6 (`[promoted → <path>]`, `[unrouted-reported]`, `[audit-corroborated]`, `[audit-dismissed]`; written by "disposal tools").

## Change

The user's ruling: the audit exits the prune cycle **entirely** — resolution belongs to a dedicated session the user opens from a handoff; the audit slims to its core capability and writes nothing, ever. Two files, one concern (the disposal machinery), not independently deployable — hence one task:

- **`milestone-rescue-audit`**: delete the `prune` mode whole — mode dispatch, disposal procedure, promote, and every file-writing step including the status-mark appends of `rescue` mode. What remains is the single-mode **band-aid hunter**: the outside-view convergence analysis (chain reconstruction → one-sentence root-cause test → discriminators → verdict; prose-narrative deliverable; chat-only) — invocable after `milestone-rescue` on a looped/outlier milestone **or in any session, on smell**: when the user suspects the orchestrator has stuck crutches around crooked architecture or spaghetti code. Frontmatter: description rewritten (prune trigger phrases out; invoke-on-smell in); `allowed-tools` stays read-only.
- **`orchestrator-artifacts` § 6**: the disposal actor becomes the **resolution session** — the dedicated session the user opens from the parked prune's handoff. Vocabulary replaced: `[fixed]`, `[routed → <path>]` (the path must be an **open** task's spec — an editable surface, never a completed one), `[dismissed]`. Retired from the active vocabulary: `[promoted → <path>]`, `[audit-corroborated]`, `[audit-dismissed]`, `[unrouted-reported]` — encountered in old repos they still count as pinned (lazy migration; history is never rewritten). Append-only, the dedup rule, and "pinned = ≥1 marker" stay verbatim.

## Files & types

- edit `src/skills/milestone-rescue-audit/SKILL.md` (mode removal + frontmatter description)
- edit `src/skills/orchestrator-artifacts/SKILL.md` (§ 6 vocabulary + actor)

## Guards

- **Engine edit** — `orchestrator-artifacts` is load-once with three callers (`milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune`); grep them before touching § 6; everything outside § 6 byte-identical.
- The audit's analysis pipeline (one-sentence test decisive, discriminators corroborative-only, "default is NOT band-aid", healthy-convergence early-exit, narrative register) is **not** compressed here — that is task 1.6.2's subject; this task only removes the prune half and adjusts frontmatter.
- The audit writes nothing after this task — no Write/Edit path anywhere in the body.

## Verification

- `grep -n -i "prune\|promote\|marker\|\[audit-" src/skills/milestone-rescue-audit/SKILL.md` → zero (body); frontmatter description names invoke-on-smell.
- `orchestrator-artifacts` § 6 lists `[fixed]` / `[routed → <path>]` / `[dismissed]`, names the resolution session as the writer, and keeps the legacy-markers-count-as-pinned sentence.
- `roadmap-prune`'s gate still computes "pinned" correctly against both new and legacy markers.

# Review: 40.1 — the buffer section's heading and opening clause name what it now holds

**Files reviewed in full:** `src/skills/agent-architect/SKILL.md` (the only changed artifact), against the plan, task spec 128, `src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer", `docs/paired-loop.md`.

## What was checked and holds

- Heading renamed to `## Your buffer is shared; you alone write it` — drops the possession claim, names the buffer as shared, keeps the sole-writer fact. Meets all three properties the plan pinned.
- The rescoped-inventory reference (`(see "Your buffer is shared; you alone write it")`) is byte-identical to the new heading text. `grep -rn "yours alone" src/ docs/` now hits only the new opening clause's "yours alone to write" (see finding 1), not the old heading — no dangling reference anywhere.
- The remainder of the first paragraph, the second paragraph (occasion-and-form, announce-obligation), and the third paragraph (deferral format, engine pointer, closing sole-writer sentence) are untouched. No other section, no other file changed. Scope honored.
- The opening clause still lists handle, pairing role, and deferral entries, so "both already timed above" in the second paragraph still resolves.
- Body is 321 lines, under the 500-line cap.

## Findings

### 1. The new opening clause misplaces the live/settled distinction and contradicts the section's own "restates none of them" — `src/skills/agent-architect/SKILL.md`, section "Your buffer is shared; you alone write it", first sentence

The inserted parenthetical reads: "the editor holds and re-reads its settled zone per `architect-editor-engine`, the live zone is yours alone to write".

Two problems with the same clause:

- **Wrong axis for the live zone.** In the engine (and in `docs/paired-loop.md`), the two zones differ in who *holds/reads* them: the settled zone is held by both halves, the live zone is "the architect's alone" because a hand that reads the head's forming conclusion returns an echo. The *writer* is not what distinguishes them — the whole file has exactly one writer, as the section's own closing sentence says ("you are its only writer") and as the new heading itself says. Contrasting "the editor holds and re-reads the settled zone" with "the live zone is yours alone *to write*" reads as if the settled zone had some other writer, or as if the live zone were the only part the architect writes. A reader keying off this sentence gets the zone split wrong on exactly the property the engine calls load-bearing. Fix: either drop the zone parenthetical altogether (the heading already carries "shared" + "you alone write it", which is all this task requires) or phrase it on the correct axis, e.g. "— the editor holds and re-reads its settled zone, its live zone is held by you alone, both per `architect-editor-engine` —".

- **Self-contradiction within the section.** The third paragraph states that "its two zones and what each holds … are `architect-editor-engine`'s … this section points there and restates none of them." The new opening now restates what each zone holds (the editor's relation to the settled zone, the architect's to the live zone). The plan's guardrail was explicit: "refer to the engine by name … rather than redefining zones". Dropping the parenthetical (or reducing it to a bare pointer — "as `architect-editor-engine` defines") resolves this and finding 1a together.

Severity: medium — this is contract text in a skill body, read on every architect run; a wrong statement of the zone split is a behaviour defect, not a style nit.

### 2. Ragged hard-wrap in the edited paragraphs — `src/skills/agent-architect/SKILL.md`, section "Relay on the marker…" and the buffer section's first paragraph

The file is hard-wrapped at ~78 columns throughout. Two lines now break the convention as a side-effect of the edit:
- "needs no form of its own. A `REPORT-ONLY` message carries either the before-mark payload, worked" (96 cols) — the sentence following the reference was not re-flowed.
- "snapshot continuing you carries" followed by "this buffer's path alone: …" — an orphaned short line in the opening paragraph.

Cosmetic; re-flow both paragraphs to the file's wrap width. Low severity, but it is the folder's settled style and the edit introduced the break.

## Verdict

One medium finding (the zone parenthetical states the split on the wrong axis and contradicts the section's own "restates none of them"), one low formatting finding. Not a pass until finding 1 is resolved.

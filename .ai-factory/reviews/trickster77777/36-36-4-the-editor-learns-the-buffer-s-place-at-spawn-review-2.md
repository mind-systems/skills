## Re-review — 36.4 — the editor learns the buffer's place at spawn

Re-read fresh: `git diff HEAD -- src/` shows only `src/agents/editor.md` (+4 −1) and `src/skills/agent-architect/SKILL.md` (+13 −2); both files read in full again. `agent-architect` is 272 lines (≤ 500); no `loads:` or `description:` change; engine, pairing engine, and `docs/paired-loop.md` untouched.

### Previous findings

1. **"as widened above" — change-history phrasing.** **Fixed.** Current text of the handle-writing paragraph in `src/skills/agent-architect/SKILL.md`:
   > starts above you came through — and in that same act give the editor the buffer's path through the spawn prompt, **as defined above**, so each half holds the other's address from the spawn on; a later round sent via `SendMessage` never repeats it.

   `grep -n "widened" src/skills/agent-architect/SKILL.md src/agents/editor.md` returns nothing.

2. **Truncated `§ "Relay on the marker"` cross-reference.** **Fixed.** Current text of the widened spawn sentence:
   > … carrying no reading, no finding, no conclusion — not the enrichment **"Relay on the marker; author a prompt in exactly one case"** forecloses — while the format token still literally opens the message; there is no spawn before one exists.

   The full heading is now quoted in the file's own `"<full heading>"` form; `grep -n "§"` across both files returns nothing.

### Full pass for new issues

- The widened spawn sentence still carries every constraint the spec sets — path at the spawn and only there, the pointer never a copy, alongside not inside the before-mark payload, no reading carried, the format token still opening the message — and "there is no spawn before one exists" is preserved. The line wrap "opens the message; there is no spawn / before one exists." is uneven but renders as one paragraph; cosmetic only, not a finding.
- The handle-writing paragraph binds the path-giving to the same act as the handle write and confines it to the spawn (`SendMessage` rounds never repeat it), matching the governing spec's "the memory's place is given to the hand in turn". The respawn paragraph is unedited and remains consistent: a respawn is an `Agent` spawn on a channel-message and inherits the definition; "resent as-is" still holds for the work-order itself.
- `editor.md`'s opening paragraph states the receipt as something that happens to the editor ("the spawn prompt gives you the buffer's own path — held from birth"), keeps the path outside the message so the mode rule below is not contradicted, and imports neither the path's literal form, a re-read instruction, nor a recovery account.
- No plan-layer citation in either skill text; `active/` symlinks resolve into `src/`, so the change is live with no second copy.

No security or runtime surface is involved — prose instructions only. No new findings.

REVIEW_PASS

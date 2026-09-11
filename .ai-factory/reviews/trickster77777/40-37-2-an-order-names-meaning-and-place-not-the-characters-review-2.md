## Re-review — 37.2 an order names meaning and place, not the characters

**Diff:** `src/skills/agent-architect/SKILL.md` only, same paragraph as round 1 (§ "Relay on the marker; author the apply work-order and your own legwork"). Re-read fresh from disk; session memory not used.

### Previous findings

**1. Dangling pronoun — "It does not compose the sentence" with no antecedent.** — **Fixed.**
Current text (lines 190–193):
> Send the apply work-order as an `APPLY-EDIT` channel-message: the order names what a sentence must say and where it goes — the meaning and the place — and does not compose the sentence: the text is written by the editor, who has the file open.

"the order" is now the explicit subject of both "names" and "does not compose"; the pronoun is gone.

**2. Change-history phrasing — "stay pinned in the order exactly as before" / "still addressed by name".** — **Fixed.**
Current text (lines 199–201):
> these are the thing itself, not a description of it, and stay pinned in the order. An anchor is addressed by name — a heading, a bolded rule, a symbol, a unique string — never a position.

Both "exactly as before" and "still" are removed; `grep -n "as before\|still addressed"` returns nothing.

### Full pass for new issues

- Edit boundary unchanged: the 37.1 two-cases sentence (lines 184–190) and the following paragraph (line 207 on) are byte-identical to HEAD.
- `grep -n "exact string"` returns nothing; "pinning"/"pinned" remain in the passage with the four retained value kinds; the "pin nothing" reading is closed in one sentence (lines 196–200).
- Anchor rule restated as name-never-position with the governing spec's four name kinds; guardrails clause and the explicit **"do not commit."** retained; closing "leave the mechanical steps to the editor" sentence retained.
- Neighbouring files (`src/agents/editor.md` § "Apply mode", `architect-pairing-engine`, `architect-editor-engine`) untouched and still coherent with a pinned work-order.
- No heading, `loads:` edge, `description:`, doc link, or plan-layer citation added.
- Cosmetic only, not a finding: line 202 ("guardrails — what NOT to touch, a collision-safe method") is a short line left by the rewrap, and line 195 is 80 columns; the file already carries both kinds of irregularity elsewhere (e.g. "enrich the payload before sending only" in the same section; 81–99-column lines in the frontmatter).

No new issues.

REVIEW_PASS

## Review: 40.4 — the engine states the bound on what may ride beside the re-read rule, and its own limit beside the mode rule

**Scope reviewed:** `git diff HEAD` / `git status` — one file changed, `src/skills/architect-editor-engine/SKILL.md` (+3/−1, 45 → 47 lines). Read in full, alongside the plan, task spec 131, the contract line, `docs/paired-loop.md` § "What crosses the channel", and the untouched receiving-side files (`src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`).

### What changed, against the plan and the spec

**§ "The architect's buffer"** — one new paragraph, placed exactly where the plan pins it: after the widened re-read paragraph ("The editor re-reads the settled zone when it changes, not once at birth — …") and before the drain-rule paragraph ("A ruling recorded in the buffer is a debt…"). Both neighbours are byte-identical to `32db19f`. The paragraph carries both halves of the governing spec's sentence pair in the engine's register:
- the permission — a fact about where the shared memory sits (settled zone moved, or the buffer's path itself) or what the hand needs in order to work at all; opens no message of its own, takes no form of its own, rides inside a message that already opens with its own token;
- the bound, in the same breath — never a reading of the payload: no finding, no conclusion, no verdict; what crosses for an independent reading still reaches the hand undisturbed; a fact about where the memory sits carries no reading of it.
It restates neither the path/numbering, the two zones, nor the re-read rule's wording; names no marker, before-/after-mark, or enrich instruction (the `agent-architect` mechanism stays there); names no spawn, recovery, or metadata fallback (the caller's occasions); coins no token-like noun and no third format. Matches the plan's guardrails and the spec's "the engine states the limit, not the argument behind it".

**§ "The mode rule"** — one sentence inserted after "Ambiguity resolves to `REPORT-ONLY`." and before "The full authoring and execution mechanics…", both of which remain byte-exact. The sentence states only the rule's own limit — the fallback never reaches what keeps the hand current, because it opens no message of its own and travels inside a message already carrying its token — and points at § "The architect's buffer" by heading name. It names neither the permitted content nor the bound, so it is a pointer, not a second copy. This is the wording the spec allocates to the mode-rule site verbatim in meaning.

### Verifications run
- `grep -n "verdict"` → exactly one hit, on the new buffer-section paragraph (between the re-read paragraph and the drain paragraph).
- `grep -c "re-reads the settled zone"` → 1 (40.2's widened sentence untouched).
- `grep -n "^## "` → the same three headings as before; no new section.
- `grep -c 'Ambiguity resolves to \`REPORT-ONLY\`'` → 1, byte-exact.
- `grep -n "The architect's buffer"` → the heading plus the new pointer inside § "The mode rule", nothing else.
- Token census: only `REPORT-ONLY` and `APPLY-EDIT` occur; no third token introduced.
- "fallback" now occurs once in the body, in "That fallback never reaches…", where its antecedent is the immediately preceding "Ambiguity resolves to `REPORT-ONLY`" — the ambiguity fallback, not the metadata fallback; no confusion with the caller's recovery path.
- `git status` / `git diff --stat` → `agent-architect`, `editor.md`, `docs/paired-loop.md`, and the roadmap are untouched, as the contract line requires ("no change to either receiving-side file"). Frontmatter `description:` unchanged, per the plan's stated assumption (precedent: 40.2).
- 47 lines, well under the 500-line bound.

### Blast radius
Both callers of the engine (`agent-architect`, `editor.md`) key their behaviour off the two tokens and the ambiguity default; neither changes. The new text is a limit on what the mode rule classifies plus a bound on what may ride, both already true of how the architect sends things — nothing downstream gains a new obligation or a new branch.

### Findings
None.

REVIEW_PASS

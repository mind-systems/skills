## Code Review — 1.9.1 aif: rules generation gets the counter-default entry filter

**Files reviewed:** `src/skills/aif/SKILL.md` (only source change) against the plan, spec `41-aif-rules-counter-default-filter.md`, and ROADMAP:173. The other staged files are planning artifacts (plan, plan-reviews, sidecar JSON) — not application code.
**Change nature:** instruction-text edit to a skill (no runtime code, no automated test surface — Settings: Testing = no). "Breaks at runtime" reduces here to: does the generated `rules/base.md` still come out well-formed, and does any other reader of this skill depend on the removed structure?
**Risk level:** 🟢 Low

### What the change does

The rules-generation block (SKILL.md:144–178) is reframed from a style-inventory dump into the counter-default entry filter:
- The old detect-and-emit list (naming/module/error/control-flow/logging/test patterns) is replaced by the two-part gate `(a) executor would do otherwise ∧ (b) code alone cannot teach it`, each rule carrying its why (Task 1).
- The excluded anti-pattern is named with concrete case-style examples (Task 2).
- The fenced `# Project Base Rules` template is rewritten to the passing genre (Data Types / Identifiers / Migrations, each a counter-default + why), the header note renamed to the new genre, the `## Naming Conventions` and `## Control Flow` blocks removed, and an italic meta-note marks the examples illustrative-not-literal with the empty-file-is-valid rule (Task 3).
- The Mode 1 Step 7 item 6 mirror (SKILL.md:239) drops "detected conventions" → "the filtered counter-default rules in English."

### Verification performed

- **Plan grep gate** — `grep -i "PascalCase\|snake_case\|UPPER_SNAKE"` over the fenced template (lines 160–176) returns **zero**. The case-style tokens survive only in the instruction prose (line 154) as the named anti-pattern, exactly where Task 2 places them — so the *generated* file (which copies only the fenced block) is clean, satisfying the spec's verification (`grep over the generated file → zero`).
- **No stale references** — grep for `detected conventions | Control Flow | Naming Conventions | detected pattern` across `src/skills/aif/` returns no matches; both occurrences of "detected conventions" (instruction + mirror) are gone, and nothing else in the skill keyed off the removed section headings.
- **Structure intact** — the fenced block opens/closes cleanly (160–176), the italic note sits *outside* the fence (178) so it guides the generating agent without leaking into the emitted file, and the `---` section boundary and `### Mode 1` heading that follow are undisturbed.
- **Scope guards honored** — config.yaml machinery, MCP, CLAUDE.md-first ordering, other modes' skeletons untouched; no existing project's rules file is modified.

### Findings

None blocking. One non-defect observation for the record:

- **(Nit, non-blocking) "Use fixed English headings" reads slightly stale against now-variable sections.** Line 158 retains "Use fixed **English** headings and service text in this file." Under the old design the heading *set* was genuinely fixed (Naming Conventions / Module Structure / …, always emitted); now sections are project-specific and may be absent entirely. The word "fixed" here still correctly means *English regardless of `language.ui`* (consistent with the Language Resolution section's artifact rule), and the illustrative note (178) makes section variability explicit, so no executor is misled into a malformed file — this is a wording smell, not a correctness problem. If touched again, "Use English headings and service text (regardless of `language.ui`)" would remove the ambiguity. Not worth a round-trip on its own.

### Assessment

The implementation realizes the plan faithfully at every named locus, the spec's Change list and Guards are all satisfied, the spec's own verification (two-part criterion stated, anti-pattern named, template in passing genre, generated-file grep zero) passes, and no downstream reader depended on the removed structure. The lone observation is a documentation nicety with no runtime consequence.

REVIEW_PASS

## Code Review Summary

**Files Reviewed:** 1 plan (`77-1-9-1-…md`) against target `src/skills/aif/SKILL.md`, spec `41-aif-rules-counter-default-filter.md`, ROADMAP line 173.
**Risk Level:** 🟡 Medium

### Context Gates

- **Roadmap (ROADMAP.md:173)** — OK. The plan's `# Plan:` title matches the `1.9.1` milestone line; the milestone's `Spec:` tag resolves to `.ai-factory/specs/41-aif-rules-counter-default-filter.md`, which the plan follows faithfully (two-part filter + why-requirement, anti-pattern naming, template rewrite). Guards align: config machinery untouched, existing projects' rules files untouched, runs before 1.9.2.
- **Rules/composition-model** — OK. Task 1 correctly cites the "costliest instruction surface per line" motive from the spec. No `.ai-factory/RULES.md` in this repo to gate against.
- **Line-reference accuracy** — Verified against ground truth. The instruction block is at 144–183, the fenced template at 156–183, and the Mode 1 Step 7 item 6 mirror at 242–244. All plan line hints are correct. The mirror's actual text is "Write `.ai-factory/rules/base.md` with detected conventions **in English**" — Task 3 targets the "detected conventions" phrase; the trailing "in English" should be preserved (the filtered genre still emits English), which the plan's intent supports but does not state outright.

### Critical Issues

None that block, but one substantive gap:

**1. The `## Control Flow` block (SKILL.md:176–178) is unaddressed and would survive the rewrite as exactly the kind of rule the milestone exists to delete.**
Unlike every other section in the template, `## Control Flow` is not a `[detected pattern]` placeholder — it is a fully-written, always-emitted prose rule ("Prefer flat, readable control flow over deeply nested conditionals. Use guard clauses, early `return`/`continue`…"). Task 3 instructs the implementer to "Remove the `## Naming Conventions` … block and **any other placeholder** that invites style-inventory output." Because Control Flow is *not a placeholder*, an implementer following the plan literally would leave it in place. Yet it is a generic style convention that fails both gates of the new filter: (a) the executor prefers guard clauses/early returns by default, and (b) code alone teaches this style. Keeping it seeds precisely the boilerplate the milestone bans, inside the very template being reshaped to the "passing genre." This is inside the milestone's file boundary and introduced-by-nothing-external, so it is a finding, not a deferred observation. **The plan should state explicitly what happens to `## Control Flow`** — remove it, or (if it is a deliberate house rule worth keeping) reframe it as a counter-default-with-why so it doesn't read as a style inventory. Right now the plan is silent, and silence here defaults to leaving a gate-(b)-failing rule in the shipped template.

### Minor Issues

**2. Task 3's grep verification conflates two scopes.** The check is described as `grep -i "PascalCase\|snake_case\|UPPER_SNAKE"` "over the skill's **template block**" returning "only the anti-pattern mention from Task 2." But the anti-pattern examples are added by Task 2 to the *instruction block* (the `**Create …**` prose), not to the fenced `# Project Base Rules` template. A grep scoped strictly to the fenced template should return zero; a grep over the whole section returns the anti-pattern examples. The intent is clear, but the verification wording should pick one scope so the implementer can actually run it as a pass/fail gate.

**3. Header-note tension (non-blocking).** Task 3 keeps the note `> Auto-detected conventions from codebase analysis. Edit as needed.` The new genre is counter-defaults-with-why, not a raw "detected conventions" dump; the retained note mildly contradicts the reshaped body. Acceptable if intentional, but worth a one-line acknowledgment since Task 3 otherwise scrubs "detected conventions" language from the mirror.

### Positive Notes

- The plan is tightly scoped and correctly separates *what the rules artifact may say* from the config/mode/disclosure machinery it must not touch — matching the spec's Guards and the 1.9.2 hand-off.
- Task decomposition (criterion → anti-pattern → template) mirrors the spec's Change list and is properly dependency-ordered.
- Line references were checked against the live file and are all accurate — rare and appreciated.
- The grep verification (despite the scope wording nit) gives the implementer a concrete, mechanical pass condition, which is the right instinct for a "stop emitting boilerplate" change with no automated test surface.

Not writing PLAN_REVIEW_PASS: finding #1 (unaddressed `## Control Flow` block) needs a decision in the plan before implementation.

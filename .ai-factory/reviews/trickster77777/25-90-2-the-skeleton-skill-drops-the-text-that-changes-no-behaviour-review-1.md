## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-decompose-skeleton/SKILL.md`), read in full. The staged plan, its sidecar and the plan-review are orchestrator artifacts and were not judged as product.
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap: OK.** The plan heading matches line 90.2 in `.ai-factory/roadmaps/trickster77777.md`. The line's `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0259-the-skeleton-skill-drops-the-text-that-changes-no-behaviour.md`, and the diff was judged against that spec. 90.1 is `[x]`, so this task sits at the seam.
- **Governing spec: WARN (non-blocking).** The Phase 90 header says "Governing spec: none written yet". The task spec is the authority.
- **Architecture: OK.** Each engine is still loaded through the `Skill` tool at its point of use: `roadmap-engine` in Step 0 and Step 4, `polymorphism-philosophy` in Lens 1, `test-philosophy` in Lens 2. `loads:` stays as the one home of the edge declaration, which matches the mechanism-vs-policy model.
- **Rules: WARN (missing optional files).** Neither `.ai-factory/RULES.md` nor `.ai-factory/skill-context/aif-review/SKILL.md` exists.

### Verification against the spec

- **Every removal target is gone:**
  - § "Load-once / dependencies"
  - "Do not over-engineer targeting."
  - Step 0's "Never touch closed…"
  - Lens 1's "Restraint" bullet
  - the label "Canon (m36)"
  - Step 3's orchestrator sentence
  - § "Critical Rules / What NOT to do"
- **The spec's sweep comes back empty.** `grep -n -i -E "load-once|Critical Rules|What NOT|restraint|Canon|over-engineer|never touch|neither reads"` on the skill returns nothing.
- **Everything the spec keeps is unchanged:**
  - the opening's reach ("most open tasks pass through untouched")
  - Targeting's default and single-task reach
  - Step 0's open set
  - the lenses' questions and what each extracts
  - the three hazard classes
  - Lens 3's two paragraphs, as 90.1 left them
  - Step 2's order, fuse and exception
  - Step 3's account of what "deliverable" means
  - Step 4's render, disposition and numbering, including "Ensure `roadmap-engine` is loaded once this chat"
- **The frontmatter is byte-identical.**
- **Step 0 loads `roadmap-engine` before it uses the engine's named-roadmap resolution.** The phrasing ("Load `…` once via the `Skill` tool, then …") mirrors Lens 1 and Lens 2. "per its named-roadmap resolution order" now refers clearly back to `roadmap-engine` in the same sentence.
- **Lens 2's example is told whole and unlabeled.** It says what the stateless `PassThroughIndicator` double let pass (two test cases, although `loadHistory` omitted re-instantiation). It also says what a stateful double, forced by writing the test against the skeleton first, would have caught. The case numbers the reader cannot see are gone.
- **No dangling outside references.** Outside texts that name the skill still hold:
  - `docs/sakshi-harness/skill-cycle.md` says "Сдержанность первого класса: простые задачи проход не трогает". The opening's kept sentence still carries that.
  - `docs/philosophy/principles-at-their-moment.md` quotes Lens 1's "apply its question to the target task(s)", which is unchanged.
  - `test-philosophy` and `polymorphism-philosophy` name the skill only as a caller.
  - `roadmap-outline-deep`'s `## Load-once / dependencies` belongs to that skill.

### Critical Issues

None.

### Positive Notes

- Every removal is surgical, and the surrounding wrap is preserved. The diff touches only the sentences the spec names.
- The Step 0 rewrite turns a load the reader only met in the removed section into an instruction at the point of use. This closes the one behavioural gap the removal would otherwise have opened.

REVIEW_PASS

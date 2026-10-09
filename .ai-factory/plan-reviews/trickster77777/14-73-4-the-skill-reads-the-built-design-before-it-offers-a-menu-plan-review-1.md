## Code Review Summary

**Files Reviewed:** 1 plan, against its task spec (`.ai-factory/specs/trickster77777/0211-…`), the phase note (`0206-…`), the 73.3 spec (`0210-…`), and the target `src/skills/aif-architecture/SKILL.md` and its `references/architecture-template.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. The change stays inside one skill body. It adds no `loads:` edge and no new skill, so the mechanism/policy composition rule in `.ai-factory/ARCHITECTURE.md` is not touched.
- **Rules** — WARN (non-blocking): `.ai-factory/RULES.md` is absent, so there are no explicit conventions to check against.
- **Roadmap** — OK. Contract line 73.4 in `.ai-factory/roadmaps/trickster77777.md` is the first `[ ]` after the `[x]` 73.1–73.3, which are committed (`b09ed48`, `e09e147`, `c6870fa`). The plan's `Spec:` path matches the contract line. The phase has no `Governing spec:` header; the phase note states "No document governs this; a skill is its own documentation". The plan's after-text matches the phase note's "What should be true" (built design first, variation axes asked before the menu for a new project, migration target only on explicit choice).

**Ground truth checks performed:**
- Every replaced "before" line exists byte-for-byte in the current `SKILL.md`: the Step 0 scan lead, the Step 1 opening line, the Step 1.5 section through "Wait for their decision before proceeding to Step 2.", and the Step 3 pointer line.
- Every verbatim block in the plan was extracted and checked paragraph by paragraph against the spec's pinned after-text. All of them match exactly: the Step 0 paragraph, the three Step 1 paragraphs, the whole Step 1.5 block, the Step 0 lead and the Step 3 pointer line.
- The plan says `references/architecture-template.md` no longer names "Option 1"/"Option 2" and gates "Legacy vs New Code Policy" on "the user explicitly asked for a migration target in Step 1.5". The file confirms both.
- The second paragraph of the new Step 1 ends in ":". It leads straight into the untouched `**If `$ARGUMENTS` specifies an architecture**` block, so the structure stays coherent.

### Critical Issues

None.

### Findings

1. **The verify step's list of expected sweep hits is incomplete** (plan § "Verify the blast radius").
   The plan lists the hits that "stay as they are and are NOT edited": `aif`, `aif-docs`, `docs/reserved-words.md`, `CLAUDE.md`, and the `roadmap-test-coverage` line. Run against today's tree, the second sweep command (`grep -rn "aif-architecture" src docs CLAUDE.md --include="*.md"`) also returns `docs/philosophy/principles-at-their-moment.md` (section **"Dependency inversion, and where to invert."**). Its text reads: "`aif-architecture` writes it by reading the built design first: which interfaces have several implementations, where and by what key one is chosen…".

   The spec's own Finding misses this hit too, so the plan copied the gap. The hit is harmless: that doc describes the behaviour this task builds, and the change brings the skill into line with it. Nothing there needs editing. But an implementer checking the sweep output against the plan's "Expected:" list will find an unlisted hit. They then have to decide alone whether to edit a doc outside the task's one-file boundary.

   **Fix:** add `docs/philosophy/principles-at-their-moment.md` to the expected-and-untouched list, with the reason: it already states the behaviour the new Step 0/Step 1 implement, and stays.

### Positive Notes

- Each verbatim after-text is reproduced exactly. The plan also says outright that the spec wins on any disagreement, which is the right fallback for contract text.
- The plan names precisely what must stay byte-identical in Step 1: the `$ARGUMENTS` mappings, the "Consider: …" line, the recommendation template, the options list and the CRITICAL INSTRUCTION. It also cites "Nothing else in the file changes" as contract text. This guards against the most likely implementer drift.
- Before relying on 73.3's template gating, the plan checks it against the committed file.
- The read-only verify step includes `git diff --stat` and a check of the `description:` frontmatter. That catches accidental edits outside the boundary.

## Deferred observations
- Affects: Phase 73 / `.ai-factory/specs/trickster77777/0210-the-template-writes-the-built-design.md` (73.3's file, `src/skills/aif-architecture/references/architecture-template.md`). The template's **Rules for generation** still say "Base the generated folder structure on the user's decision in Step 1.5 (either adapted to reality or strict pure architecture)." The 73.4 spec's own breakage rule covers "a text … describ[ing] … what the two Step 1.5 options mean". After 73.4, option 2 reads "Also write a migration target: strict guidelines the application must be refactored toward later", and Step 1.5 says the built design "is documented as it is". The template line can be read as still consistent: the folder structure becomes the strict target, and the built design is recorded in "What varies" / "Composition root". It can also be read as asking the whole document to be "strict pure architecture". The 73.4 sweep patterns ("ideal architecture", "ideal folder structure", …) cannot catch this wording. The file sits outside this task's one-file boundary ("Nothing else in the file changes" concerns `SKILL.md`, and the template text is pinned by 73.3), so the planner should not fix it here. Whoever owns Phase 73 should decide whether the line needs rewording to match the new option 2. [fixed]

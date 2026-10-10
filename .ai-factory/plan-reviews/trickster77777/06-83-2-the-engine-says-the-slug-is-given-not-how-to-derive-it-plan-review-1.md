## Plan Review Summary

**Plan:** 83.2 — the engine says the slug is given, not how to derive it
**Files targeted:** 1 (`src/skills/roadmap-engine/SKILL.md`), plus a read-only sweep
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap gate — OK.** The plan's heading matches the open contract line 83.2 in `.ai-factory/roadmaps/trickster77777.md`, which sits right at the seam (83.1 `[x]`, 83.2 `[ ]`). The contract line's `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0234-the-engine-says-the-slug-is-given-not-how-to-derive-it.md`, and the plan cites that file and follows it.
- **Governing spec gate — OK.** Phase 83 names `docs/sakshi-harness/sakshi-harness.md` as its governing spec. The paragraph about what the harness puts in every session already says what this task's new paragraph says: the session gets a line with the user's slug, `user-slug.sh` of `roadmap-engine` prints that line, a `SessionStart` hook registers it, a session without the line runs the script itself, and the agent never computes the slug. The pinned after-text puts the engine in line with that doc. Docs come first, as they should.
- **Architecture gate — OK.** The plan changes only the engine's own mechanism text and adds no `loads:` edge. Under "Composition: mechanism vs policy", the engine still points to its own script for mechanism and holds no policy.
- **Rules gate — WARN (non-blocking).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`, so no project-specific rules apply.

### Verification against ground truth

- **Target paragraph.** In the current `SKILL.md` § "Named roadmaps", **Slug derivation** is three wrapped lines. It starts `**Slug derivation:** the local-part of \`git config user.email\`, lowercased, every` and ends `` `john-doe`); fallback — slugified `user.name` when email is unset. ``. The plan quotes exactly these start and end lines.
- **Replacement text.** The plan's code block matches the spec's "What must be true after" sentence character for character: the bold label, the comma after "session start", the semicolon, and `scripts/user-slug.sh`.
- **Script exists.** 83.1 created `src/skills/roadmap-engine/scripts/user-slug.sh`. It prints the bare slug and exits `2` when no slug can be derived, so the new paragraph points at a file that is really there.
- **Scope boundary.** Leaving **Resolution order**, **Owner line**, **Test sibling** and **Spec destination** alone is correct. The Owner line checks the full email, not the slug, and the spec says "the rest of the section stands."
- **Sweep is correct.** Today, `grep -rn "Slug derivation" src docs CLAUDE.md` matches only the engine's line. After the rewrite it still matches only that line, because the bold label stays. `grep -rn "slug/owner mechanics" …` matches exactly the six callers the plan lists (`roadmap-decompose`, `roadmap-outline`, `roadmap-test-coverage`, `task-rescue`, `temporal-tree`, `command-pin-gaps`). Each one points to the section as a whole, which still holds the resolution order, the owner line and the test sibling, so they stay true.
- **Removal check is correct.** Today, `local-part`, `john-doe` and `user.name` appear in the engine only on lines 68 and 70, both inside the target paragraph. So after the rewrite, the plan's check that the grep "returns nothing" is the right expectation and won't flag anything elsewhere.
- **Wrapping guidance is safe.** The text is about 200 characters, so it wraps to roughly three lines at about 85 columns. The longest backtick span, `` `The user's slug: <user-slug>` ``, is 30 characters, so keeping it on one line is easy.

### Critical Issues

None.

### Positive Notes

- The plan quotes the exact start and end of the old paragraph, so the implementer cannot cut too much or too little.
- It separates word changes from line wrapping and protects the backtick spans. That is the right way to honour "verbatim" text in a hard-wrapped Markdown file.
- The sweep is copied from the spec, and the plan says what result to expect from each command. It also adds a check that the old derivation text is gone and that the script exists. These checks close the task's contact surface.
- The out-of-scope items (the hook and its README walkthrough for 83.3, the governing-spec docs, and the frozen `reserved-words.md`) are named explicitly, so nobody will drift into them.
- A note for the implementer only, not a defect: the plan says to write `scripts/user-slug.sh` "the same way the skill's other relative references are written". The engine has no other relative file references today. The repository's rule that a skill's file references are relative (skills `CLAUDE.md` § "Key constraints") is the real basis. The text is pinned verbatim anyway, so the result is the same.

PLAN_REVIEW_PASS

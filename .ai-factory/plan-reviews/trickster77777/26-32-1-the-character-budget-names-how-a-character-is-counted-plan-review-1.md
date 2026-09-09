# Plan Review — 32.1 the character budget names how a character is counted

## Code Review Summary

**Files Reviewed:** plan (1) + targets (2): `src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-outline-deep/SKILL.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" holds that an engine carries the shared mechanism and a philosophy skill loads it rather than inlining it. The plan puts the counting method in `roadmap-engine` (the engine, eight callers) and has `roadmap-outline-deep` (policy) name the address and explicitly refuse the restatement. No new skill, no new `loads:` edge, no new tool grant — consistent with "a skill that only routes, with no content of its own, is negative value" and with the repo's one-home-per-fact rule.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist in this repo; nothing to check against. The repo's conventions live in `CLAUDE.md` and `ARCHITECTURE.md`, both checked below.
- **Roadmap** — PASS. `.ai-factory/roadmaps/trickster77777.md:164` is the first `[ ]` line in the file — the seam — and it is 32.1, the task this plan targets. The plan's title matches the contract line. The `Spec:` tag resolves to `.ai-factory/specs/trickster77777/107-character-budget-names-its-method.md`, which exists and was read in full, as was the Phase 32 header prose (`## A budget stated in characters is measured in bytes` / `### Phase 32 — the budget carries its own unit and method`). Phase 32 names no `Governing spec:`, so the chain ends at the task spec and the two target files.
- **CLAUDE.md conventions** — PASS. `active/skills/roadmap-engine` and `active/skills/roadmap-outline-deep` are both per-item symlinks into `src/skills/` (verified with `ls -l active/skills/`), so the plan's claim that both edits go live without touching `active/` is correct. Both skills are ours, in `src/`, with no upstream counterpart — a re-sync cannot clobber them.

### Verified against ground truth

Every positional and textual claim in the plan was checked against the files, not against the spec's description of them:

- `src/skills/roadmap-engine/SKILL.md:98` is `**Rules for writing a contract line:**`; its list runs `:99–105` — **seven** bullets, matching the plan's and the spec's count. `:105` is indeed `- Full current-state / target / guards / verify detail lives in the task spec, not the contract line`, `:106` is blank, `:107` is `**Numbering rules:**`. The insertion point and the "exactly one blank line on each side" instruction land correctly.
- The list sits **outside** the ```` ```markdown ```` fence (fence `:79–96`), so the new paragraph will not be swallowed by a code block — a real hazard on this file that the plan's anchor happens to avoid.
- `Target ~600 characters (range 400–1000)` occurs exactly once (`:102`), so the plan's "→ 1" verification is a valid post-condition and not already violated at HEAD.
- `family` occurs on exactly one line in the engine (`:117`, twice: `the family prefix`, `family references`). The plan's ban on that word in the new paragraph is well-founded. Its "ten lines below" is loosely twelve; harmless, since the anchor is the word, not the distance.
- The verbatim paragraph in the plan is **byte-identical to the task spec's** after stripping the plan's own outer quoting backticks (325 vs 324 chars, one trailing quote backtick). The nested-backtick quoting is ambiguous as markdown, and the plan pre-empts exactly that with its parenthetical and with the "quote the heredoc delimiter (`<<'EOF'`) or use `Edit`" instruction. The `\n` inside double quotes survives both `zsh` and `bash` unexpanded, so the pinned command lands literally.
- The addressing shape checks out end to end: `**Spec destination:**` is a bold lead-in inside `## Named roadmaps` (`:71`), addressed from `roadmap-outline-deep:63` as `` `roadmap-engine`'s "Named roadmaps" § "Spec destination" ``. `**Counting characters:**` will be a bold lead-in inside `## Roadmap File Format` (`:77`), addressed as `"Roadmap File Format" § "Counting characters"` — the same grammar, and a named anchor deep enough to be referenced, per `docs/reference-by-name.md`.
- `roadmap-outline-deep/SKILL.md:99` starts `- **Budget** — rewrite the phase preamble down to **~200–500 characters**, keeping` — the plan quotes it correctly. Its frontmatter already declares `loads: roadmap-engine note`, so the plan's "add no `loads:` edge" is correct rather than an oversight.
- The scope claim holds. A sweep of `src/`, `docs/`, `CLAUDE.md` finds the `~600` figure in three further places — `roadmap-engine`'s own `description:`, `roadmap-decompose/SKILL.md:5`, and `docs/reserved-words.md:24` — and each carries it as vocabulary, not as the rule; `roadmap-engine:43` ("The char budget below is guidance, not a hard clamp") is a forward pointer, not a second statement of the number. The plan leaves all of them alone, correctly. The only other "characters" hits are `ui-ux-pro-max`'s CSS line-length guidance and `roadmap-prune`'s 7-char hashes — neither a text-length budget, and the new paragraph's em-dash appositive closes its enumeration over the two that are.
- `**Why two tiers:**` at `:43` says the budget below "is guidance, not a hard clamp". The new paragraph adds a unit and a method without turning the budget into a clamp, so the two do not contradict.
- Both files are far under the 500-line body cap (315 and 136); one added paragraph and one added sentence change nothing there.
- Working tree is clean apart from the plan's own artifacts, so the plan's `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` post-condition will be a meaningful signal rather than noise.

### Spec coverage

All five of the task spec's Verification items appear in the plan's third task, including the load-bearing "no count is trusted until taken by the normalized method" and the whole-file (not `grep`-line) reading discipline. The spec's guards that the plan does not restate verbatim — the two untouched `description:` blocks beyond the engine's own, "no verification step anywhere gains a count", "no skill runs the pinned command" — are all enforced transitively by two constraints the plan does state: the paragraph text is pinned verbatim, and the diff must list exactly two files. Nothing in the spec is reachable that the plan leaves open.

### Critical Issues

None.

### Positive Notes

- The second task's failure mode is named rather than merely forbidden: "Naming the address and then explaining what it says would give the method a second home while still reading correctly" — this is precisely the leak that shape-only counts (`code point` → 0, command → 0) would otherwise pass, and the plan pairs the prose with the counts that catch it.
- Instructing the implementer to imitate an existing in-file passage for the pointer's shape, and quoting that passage, is the right level of pinning: the content is fixed, the sentence is not over-specified, and the result will match the file's settled folder style.
- The shell-quoting hazard on `'\n'` and `"` is anticipated with a concrete remedy, and verification is explicitly ordered to run against the file's own bytes rather than by eye — the exact discipline this task is about.
- Naming the new paragraph with a bold lead-in is what makes the cross-skill reference addressable by name instead of by position; the plan gets that right without being told.

PLAN_REVIEW_PASS

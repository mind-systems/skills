# Code Review: 17.2 — The "new work" coupling: one dictionary in the authoring skills

## Code Review Summary

**Files Reviewed:** `git diff HEAD` (4 modified skill files + 5 new planning artifacts), all 4 changed files read in full, 3 certified-unchanged files, spec 63, reserved-words, using-the-language, skill-description-field, ROADMAP, the plan and its two plan-reviews
**Risk Level:** 🟢 Low — one non-blocking documentation-correctness finding; zero behavior risk

### Scope check

`git status` shows exactly the expected set: `src/skills/{aif-docs,roadmap-decompose,roadmap-decompose-skeleton,roadmap-outline}/SKILL.md` modified, plus the task's own plan/plan-review artifacts. `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, and `src/commands/command-pin-gaps.md` are **unchanged** — `git diff HEAD --stat` over those three returns empty, which is Task 9's certification landing as an assertion rather than an assumption. No reach into `roadmap-prune`, `roadmap-test-coverage`, or the rescue pair (17.3's set).

### Verification gates — all pass, re-run independently

| Gate | Expected | Actual |
|---|---|---|
| `rg -U -in 'spec\s+notes?'` over the 4 edited + pin-gaps | zero | **exit 1, zero hits** ✓ |
| `rg -U -in '[^-]milestones?'` over the 4 edited | 3 lines / 2 exempt categories | **3**: `roadmap-outline:3` (trigger), `aif-docs:26` + `:182` (detection lists) ✓ |
| `rg -U -in '\bnotes?\b'` over the 4 edited | exactly `aif-docs:41` | **1 hit, `aif-docs:41`** (`**Note:**`) ✓ |
| `wc -l` per file | 75 / 271 / 97 / 148 | **75 / 271 / 97 / 148** ✓ |
| frontmatter `name:`/`loads:`/`allowed-tools`/`argument-hint` | untouched | **zero changed lines touch a key or its value** ✓ |
| `` `Spec:` `` literal count pre/post | stable | **outline 3→3, decompose 2→2, skeleton 2→2, aif-docs 0→0** ✓ |
| `.ai-factory/` path literals | intact | **`.ai-factory/ROADMAP.md` on `outline:3` survives the same-line edit** ✓ |
| certified trio | unchanged | **empty diff** ✓ |

The plan's six forecast line widths landed **exactly**: `decompose:6`=100, `:79`=90, `:81`=92; `skeleton:122`=96, `:123`=94, `:126`=95. The "leave long, do not rewrap" directive was honored — no paragraph reflowed, no line count moved, so no downstream line number shifted.

### Behavior gate

Static, per 17.1's precedent. Confirmed by reading:
- `roadmap-outline:23` still instructs `### Phase N — <Title>` headers; the 5–15 rule, numbering invariant, and the "no contract line, no `Spec:` tag" restraint are untouched. The description's `milestones`→`phases` now **agrees** with a body that already said "phase" throughout — the edit removes a description/body disagreement rather than creating one.
- `roadmap-decompose:34` still renders `**N.M — Name**` under `### Phase N`, flat fallback intact; the Atomicity Gate (46–57), target-file routing (59–71), and sub-numbering rule (84–87) are byte-untouched.
- `aif-docs`' single edited line changes two nouns inside one sentence of Step 1; the State A–D dispatch table below it and the governing-spec genre instructions are untouched.

No runtime scanner depends on the changed words: `orchestrator/roadmap.py` parses roadmap lines via `CHECKBOX_RE` and treats title/description as opaque text. Nothing greps for `spec note` or `milestone`.

### Findings

**1. `docs/skill-description-field.md:25` is made false by this diff — a bound doc now contradicts ground truth.** (Medium; not a defect in the skill edits themselves)

The doc reads, in the present tense:

> "A divergence **is live now**: `roadmap-outline`'s skill-description calls its product "major milestones / high-level goals" and never "phase"; `roadmap-decompose` calls its own "milestones" too. … Aligning the vocabulary … is **the first application of the doctrine**, not a rewrite of the skill-descriptions."

This diff *is* that alignment. As of these changes `roadmap-outline:3` reads "major phases" and `roadmap-decompose:4/8` read "tasks" — so the doc asserts a live divergence that no longer exists and quotes, verbatim, two strings the diff just deleted. Three things make this more than cosmetic:

- **The doc is inside the vocabulary contract's own scope.** `using-the-language.md` § "What conforms" binds "the docs that specify the system", and `skill-description-field.md` is named there and in the root CLAUDE.md as one of the trio. A doc in the bound set stating a false fact about the bound files is the exact drift the contract exists to prevent.
- **It is the governing spec for Phase 14.** `ROADMAP.md:43` names it as such, and 14.1 explicitly re-verifies "against the *final* (post-13/16/17) descriptions". A 14.1 implementer reading line 25 is told the milestone divergence is still open — the likeliest failure is a wasted cycle re-deriving that it is closed; the worse one is re-introducing the retired word to match the doc's quoted text.
- **Ground truth wins, per global CLAUDE.md § "Grounding claims".** Line 25 is a *description* of the skill files, not a governing spec of intended behavior, so the code is authoritative and the doc is now stale — a defect to reconcile, not a doc to leave.

I am **not** asking for any change to the four skill files; they are correct. The fix is one paragraph in `skill-description-field.md`, restating the doctrine without the "is live now" claim and without the two dead quotes (and in present tense — not "milestone was retired", which the doc-style rule forbids as change-history narration).

Scope note, stated honestly rather than assumed: spec 63 § "Files & types" fences the file set to the seven skill/command files and says "no `references/` touched" — it does not name `docs/`. So this is arguably outside the task boundary, and the plan's Task 5/Task 7 lockstep handling of the `skeleton:126` ↔ `decompose:78` coupling shows the plan was alert to this class and simply did not sweep `docs/` for it. Two defensible dispositions: fix the paragraph now as a sanctioned same-concern follow-on, or record it against 14.1 whose spec already mandates a re-verify pass. Either closes it; leaving it unrecorded does not.

### Positive Notes

- **The `Spec:` tag / artifact distinction landed correctly on every site**, including the two subtle calls: `skeleton:122` became `` a `Spec:`-tagged task spec `` (the artifact) while `skeleton:132` became `` its `Spec:` tag `` (the tag — noun dropped, not substituted). Both read naturally and neither disturbs the literal.
- **Cross-file coupling held in lockstep.** `decompose:78`'s heading became `Task-spec-handling rule:` and `skeleton:126`'s reference to it became `in-place task-spec-update discipline` in the same changeset. A per-file sweep breaks this silently; it didn't.
- **The `decompose:6` `spec`→`detail` rewrite is the right call.** A literal bare-note substitution would have produced "the full spec persisted as a task spec" — redundant. The chosen wording mirrors `roadmap-engine:5` ("contract line plus a full task spec written via note"), which I verified reads as claimed.
- **The mention-vs-use protection at `aif-docs:26/182` held.** Both forbidden-phrase detection lists still contain the literal `"this milestone"`. Rewriting them would have made the no-history detector miss the phrase it exists to catch — a behavior regression disguised as conformance. Correctly left alone.
- **`milestone` survives in `docs/reserved-words.md:5` and `docs/using-the-language.md:23`** — both are mentions *about user input* ("a user may type 'milestone'"), exempt by the contract's own text, and both correctly untouched.
- **`roadmap-outline:40–41`'s pinned two-line exception applied exactly**, wrap point moved as specified, pair still two lines at 78 and 69 chars. The plan's round-2 self-consistency fix was load-bearing and was honored.
- **`spec note` surviving in `task-rescue` (11 sites) and `task-rescue-audit`** is correct scope discipline — that is 17.3's declared set, not this task's.

## Deferred observations

- Affects: `.ai-factory/specs/65-standalone-skills-conformance.md` (task 17.4) — `src/commands/command-pin-gaps.md:17` carries **two** bare artifact-`note` sites: `` scanning each contract line and its `Spec:` note file `` and, earlier on the same line, `the scope under discussion in chat (a named task, phase, or note)`. Both are correctly out of scope for 17.2, which certifies `command-pin-gaps` as no-change and scopes its bare-note sweep to edited files. The forward concern is that no remaining task claims them: 17.3 covers `roadmap-test-coverage`/`roadmap-prune`/the rescue pair, and 17.4 enumerates `detangle`, `temporal-tree`, `aif`, `aif-architecture`, `observe-logs`, `command-handoff`, `command-commit-roadmap-update` — `command-pin-gaps` appears in neither. Unless folded into 17.4's sweep, the One-dictionary direction closes with two retired synonyms alive in a command file. Carried forward from plan-review-2.
- Affects: `docs/skill-description-field.md` — see Finding 1; if not fixed in this task, it must be pinned to 14.1, whose spec already mandates a re-verify against the post-17 descriptions.

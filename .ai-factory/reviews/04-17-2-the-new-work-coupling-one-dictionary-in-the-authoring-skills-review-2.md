# Code Review (round 2, re-review): 17.2 — The "new work" coupling: one dictionary in the authoring skills

## Code Review Summary

**Files Reviewed:** `git diff HEAD` + `git status`; all 5 modified files re-read from disk (not from session memory); the 3 certified-unchanged files; spec 63, reserved-words, using-the-language, skill-description-field, ROADMAP, the plan, and review-1
**Risk Level:** 🟢 Low — previous finding fixed; no new defects

Changed set is now 5 files: the 4 skill files (byte-identical to the round-1 pass — `git diff HEAD --stat -- src/skills/` still reports 2/26/30/6, 32 insertions / 32 deletions) plus `docs/skill-description-field.md`, the round-1 fix.

---

## Verdicts on review-1 findings

### Finding 1 — `docs/skill-description-field.md:25` made false by the diff → **FIXED**

Re-read from disk. The line cited in review-1 no longer exists in its old form. Current content of `docs/skill-description-field.md:25`:

> "Coherence requires every thing to be named by the artifact's own word. The artifact grammar (both bodies, `roadmap-engine`, [skill-cycle](philosophy/skill-cycle.md)) is `### Phase N` (outline's product) and `N.M — task` (decompose's), and the skill-description-field names each tier by that same word: `roadmap-outline`'s skill-description calls its product "phases", `roadmap-decompose`'s calls its own "tasks". "Milestone" is retired from the vocabulary; it survives only as a user-facing trigger word (a phrase the agent maps by context, per [using-the-language](using-the-language.md)), never as the artifact's name. Naming each tier by its artifact's own word — "phase" where outline makes phases, "task" where decompose makes tasks — is a vocabulary edit, not a fact or a topology edit."

Every element of the finding is addressed:

- **The false "divergence is live now" claim is gone.** No forward-looking-divergence assertion remains.
- **The two dead quotes are gone.** `"major milestones / high-level goals"` and `roadmap-decompose` calling its own `"milestones"` — both strings the diff deleted from the skill files — no longer appear anywhere in the doc (`rg -i 'spec note|milestone' docs/skill-description-field.md` returns only this line, and its sole `milestone` is the retirement statement itself, a **mention** of the retired word, which is correct and unavoidable in a paragraph about retiring it).
- **The two new descriptive claims are true.** Verified against live frontmatter: `roadmap-outline:3` reads `Create or update a project roadmap with major phases.`; `roadmap-decompose:4` reads `Create or update a project roadmap with atomic, granular tasks.` and `:8` reads `tasks that need to be implementation-ready.`
- **Present tense, no change-history narration.** The rewrite states the settled rule rather than "milestone was retired" — conforming to the global CLAUDE.md § Documentation style rule the finding explicitly warned about.
- **The trigger-word carve-out is correctly sourced.** The paragraph cites [using-the-language](using-the-language.md) for it; I confirmed `docs/using-the-language.md:23` genuinely carries that carve-out ("user input is mapped by context, never conformed. A user types 'milestone'; the agent understands"). The link target exists, as does `philosophy/skill-cycle.md`.
- **The edit is one-line-for-one-line** (`docs/skill-description-field.md | 2 +-`); file stays 33 lines; no surrounding section touched.

The fix also improves on what was asked: it explains *why* the trigger word survives, so a future reader does not re-open the question.

---

## Full re-review — verification gates

All re-run against the current tree, not carried over:

| Gate | Expected | Actual |
|---|---|---|
| `rg -U -in 'spec\s+notes?'` over 4 edited + pin-gaps | zero | **exit 1, zero hits** ✓ |
| `rg -U -in '[^-]milestones?'` over 4 edited | 3 lines / 2 exempt categories | **3** ✓ |
| `rg -U -in '\bnotes?\b'` over 4 edited | exactly `aif-docs:41` | **1 hit, `aif-docs:41`** ✓ |
| `wc -l` | 75 / 271 / 97 / 148 | **75 / 271 / 97 / 148** ✓ |
| `docs/skill-description-field.md` line count | unchanged | **33, one-for-one line swap** ✓ |
| certified trio (`agent-architect`, `editor.md`, `command-pin-gaps`) | unchanged | **empty diff** ✓ |
| frontmatter keys/values, `` `Spec:` `` literals, `.ai-factory/` paths | byte-stable | **unchanged** ✓ |

## Full re-review — files read in full

- **`roadmap-decompose/SKILL.md`** (97 lines, read whole). Description block conforms; body consistent throughout. `Task-spec-handling rule:` (78) and its three bullets read naturally; the `` `Spec:` `` tag survives at 79 and 82; the sub-numbering rule (84–87) and Atomicity Gate (46–57) are untouched. Line 30's "never a full spec inline" and line 75's "expand a vague task into a full spec" use "spec" generically — correct, not a missed substitution.
- **`roadmap-decompose-skeleton/SKILL.md`** (121–137 re-read). Line 122's `` a `Spec:`-tagged task spec `` (artifact) and line 132's `` its `Spec:` tag `` (the tag, noun dropped) are both right, and both were the plan's genuinely subtle calls. Line 126's "in-place task-spec-update discipline" names `roadmap-decompose`'s discipline **by concept**, so it stays consistent with the renamed heading at `decompose:78` without creating a byte-level coupling that a future edit could silently break.
- **`roadmap-outline/SKILL.md`** (18–47 re-read). Body already said "phase" throughout (23: "Each entry is a **phase**: a `### Phase N — <Title>` header"); the description edit closes a description/body disagreement rather than opening one. The pinned 40–41 two-line exception applied exactly as specified.
- **`aif-docs/SKILL.md`** (65–72 re-read). Single-sentence edit inside Step 1; the State A–D dispatch table immediately below is untouched. The protected detection lists at 26 and 182 still contain the literal `"this milestone"` — rewriting them would have made the no-history detector miss the phrase it exists to catch.

## Runtime-risk assessment

No runtime surface is touched. These are markdown instruction files, not executable code — no migrations, types, or concurrency involved. The two mechanisms that *could* break were checked directly:

- **The orchestrator's roadmap parser** reads contract lines via `CHECKBOX_RE` and treats title/description as opaque text; it never greps the vocabulary inside. Nothing in the orchestrator or `scripts/` matches `spec note` or `milestone`.
- **Skill resolution** depends on `name:`, directory names, and `loads:` edges — all byte-stable (`loads: roadmap-engine`, `roadmap-engine test-philosophy` unchanged). No `active/` symlink is affected.
- **`roadmap-outline`'s user trigger** still contains `"milestones"`, so users typing the old word still route correctly. This was the single highest-risk item in the whole task and it held.

## Deferred observations

- Affects: `.ai-factory/specs/72-cleanup-coupling-one-dictionary.md` (task 17.3) — `docs/skill-description-field.md:25` now states that "milestone" "survives only as a user-facing trigger word …, never as the artifact's name". Across the *live* always-loaded field that is not yet literally true: `task-rescue/SKILL.md:8` (`description:`) reads "Also checks downstream **milestones** for the same gaps" and `task-rescue-audit/SKILL.md:4` reads "Outside-view audit of a **milestone** that looped" — both name the artifact, neither is a trigger. (`task-rescue:10`'s "milestone failed" *is* a trigger phrase and is exempt.) I am **not** raising this as a defect: the sentence follows "is retired from the vocabulary" and cites the language docs, so it reads as the *rule* rather than a census of the current field, and 17.3 is the declared reconciliation for exactly these two skills. Worth pinning so 17.3's implementer knows a bound doc already asserts the end state, and so the claim is re-read once 17.3 lands. [dismissed — already handled: 17.3 landed, task-rescue/task-rescue-audit descriptions no longer name "milestone" as the artifact; docs/skill-description-field.md:25's claim is now literally true]
- Affects: `.ai-factory/specs/65-standalone-skills-conformance.md` (task 17.4) — carried forward unchanged from review-1 and plan-review-2: `src/commands/command-pin-gaps.md:17` holds **two** bare artifact-`note` sites (`` its `Spec:` note file `` and "a named task, phase, or note"). Correctly out of scope for 17.2, but claimed by no remaining task — 17.3 covers the cleanup four, 17.4 enumerates seven standalones without `command-pin-gaps`. Unless folded into 17.4, the direction closes with two retired synonyms alive in a command file. [fixed — command-pin-gaps.md:17 now reads "task spec" at both bare-note sites]

REVIEW_PASS

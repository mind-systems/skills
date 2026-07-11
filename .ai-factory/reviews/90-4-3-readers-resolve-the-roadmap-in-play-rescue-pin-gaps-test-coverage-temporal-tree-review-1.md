# Code Review — 4.3 readers resolve the roadmap in play

**Scope reviewed:** the four code changes only — `src/commands/command-pin-gaps.md`, `src/skills/milestone-rescue/SKILL.md`, `src/skills/roadmap-test-coverage/SKILL.md`, `src/skills/temporal-tree/SKILL.md`. (Roadmap/spec/handoff/plan files in the diff are planning artifacts, not code under review.)

**Method:** read all four files in full, cross-checked every `ROADMAP*.md`/`roadmaps/` literal, verified the engine anchor and reverse-graph marker, and compared each reader's `allowed-tools` against the runtime the engine's resolution requires. Baseline: spec 45, the engine's "Named roadmaps" section (spec 43), and the ratified sibling wiring from 4.2 (`roadmap-outline`, `roadmap-decompose`).

---

## Finding 1 — pin-gaps cannot execute the "my roadmap" tier it now points to (grant gap) · Medium

`src/commands/command-pin-gaps.md:10`

The diff correctly adds `Skill` + `loads: roadmap-engine` + the load-once line so pin-gaps can *load* the engine (the plan-review-1 / milestone-1.17 fix). But loading the section is only half the dependency. To actually resolve the **"my roadmap"** tier the fallback now references, the engine requires the developer identity:

> engine `SKILL.md:56` — "**Slug derivation:** the local-part of `git config user.email` … fallback — slugified `user.name`".

pin-gaps' grant is `Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *) Skill`. The pattern `Bash(git grep *)` does **not** match `git config user.email` (nor `git config user.name`). So when a user explicitly asks pin-gaps to operate on "my roadmap", the engine's slug derivation issues a `git config` call that pin-gaps has no permission for — a permission prompt interactively, an outright **denial in a headless orchestrator run**. The resolution then can't produce a slug, and the "my" tier is unreachable at this site.

This is the exact failure class milestone 1.17 exists to prevent (spec 42): *the body demands a tool the frontmatter doesn't grant, so a headless run denies it and the step silently degrades.* Here the plan closed the `Skill` half of that gap but not the `git config` half. The other three readers do not have this problem — rescue, test-coverage, and temporal-tree all carry `Bash(git *)`, which covers `git config`. pin-gaps is the sole outlier, and the 4.2 writers it was modeled on (`roadmap-outline`, `roadmap-decompose`) both hold `Bash(git *)` too.

**Impact is bounded:** the engine "never infers multiuser mode", so absent an explicit "my roadmap" request pin-gaps falls to `$ARGUMENTS` / chat scope / default `ROADMAP.md`, none of which need `git config` — those paths are unaffected and behavior with no `roadmaps/` is identical to today (spec 45 guard holds). The gap fires only on the new, explicitly-requested "my" tier, and it fails loudly (denial), not silently. But the milestone's stated intent is to make the resolution reachable at all four sites, and at this one it is not fully wired.

**Fix:** widen pin-gaps' git grant to cover the engine's identity read — minimally add `Bash(git config *)` (or align with the family on `Bash(git *)`). Alternatively, if pin-gaps is deliberately meant to support only argument→default (no autonomous "my" derivation), state that scope explicitly in the fallback wording so the pointer doesn't promise a tier the command can't serve. The former matches the family and the milestone intent; I recommend it.

---

## Verified correct (no action)

- **rescue** — Step 4 (`:178-187`) widens cleanly: argument branch first and byte-unchanged, test-keyword branch now maps the roadmap in play to its `-tests` sibling (named → `roadmaps/<slug>-tests.md`, default → `ROADMAP_TESTS.md` as today), else the roadmap in play. Matches spec 45's Change bullet exactly. The Step-1 restatement (`:56-58`) is collapsed to the pure pointer "(the same resolution Step 4 determines)", killing the contradiction plan-review-1 flagged; the `:65-67` "additive to Step 4's own resolution" sentence is correctly left intact. `loads: orchestrator-artifacts roadmap-engine` and the mirrored load-once line are correct. No stray old literals remain (grep clean; the only other `ROADMAP.md` mention is the argument-hint example).
- **test-coverage** — Layer-1 (`:29-35`) names the resolution order feeding `$ROADMAP_PATH`; no-`roadmaps/` behavior is identical to the prior "ROADMAP.md (or $ARGUMENTS)". `loads: test-philosophy roadmap-engine` correct; `Bash(git *)` already present, so no grant gap. The `:323` "Never write ROADMAP_TESTS.md" guard is unrelated and untouched.
- **temporal-tree** — Step-3 path is now the resolved roadmap (`git show <first-hash>:<resolved-roadmap-path>`); both old `.ai-factory/ROADMAP.md` literals replaced, none left. The added caveat paragraph (`:83-88`) correctly documents that "my" activates only on explicit request over integration-branch pruned history and that an explicitly-named historic path is the user's choice — resolving plan-review-1's Issue 3 in-file without reopening spec 45. Walk order (Steps 1–6), `## Features` prefix-match, and synthesis output are byte-identical. `Bash(git *)` covers the engine's `git config`.
- **Engine coupling** — the engine's reverse-graph marker (`roadmap-engine SKILL.md:22-23`, "the reverse graph resolves via `grep -l …`") is a live grep, so the four new `loads: roadmap-engine` callers are automatically discoverable; no engine-side edit needed, as the plan claimed. The anchor "Named roadmaps" section (`:49`) that all four pointers name exists.
- **Spec-45 guards** — "referenced, never restated" holds at every site (each cites the engine's section rather than inlining slug/owner mechanics); "defaults byte-stable" holds at all four.

---

One Medium finding blocks a clean pass: pin-gaps points to a resolution tier its tool grant cannot execute. The other three edits are correct and spec-faithful.

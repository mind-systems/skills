# Code review 1 — 16.1 Rename milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

## Code Review Summary

**Files Reviewed:** full `git diff HEAD` (17 files) + both renamed `SKILL.md` in full + all 5 cross-reference targets + plan + spec 71 + ROADMAP
**Risk Level:** 🟡 Medium — the rename itself is correct and complete; two unplanned prose additions landed outside the plan's file boundary

The mechanical task is **done correctly**. Every identifier moved, every column held, the symlinks are right, and the frozen-history guard passes. One finding, and it is about scope rather than correctness: two Russian philosophy docs received new doctrinal prose that no task authorized.

## Verified correct

| Check | Result |
|---|---|
| `grep -rIn 'milestone-rescue' src active docs CLAUDE.md` | ✅ zero hits |
| `name:` frontmatter matches directory | ✅ `task-rescue`, `task-rescue-audit` |
| `loads:` byte-identical | ✅ `orchestrator-artifacts roadmap-engine` (L14), `orchestrator-artifacts` (L16) |
| Symlinks: mode, depth, resolution | ✅ both `120000`, `../../src/skills/<name>`, `ls -L` resolves |
| Old symlink names gone | ✅ `ls active/skills/ \| grep -c milestone` → 0 |
| `git status` staging | ✅ 2 deleted + 2 added, both staged; `git mv` preserved rename detection on `SKILL.md` |
| `orchestrator-artifacts` both refs | ✅ L7 reverse marker and L44 sidecar prose — the ref spec 71 omitted was caught |
| `skill-cycle.md` arrow column | ✅ held at char 42 (rescue rows now L72–73 after insertion) |
| `CLAUDE.md` tree `#` column | ✅ held at char 35, matching L48–59 block |
| Frozen `.ai-factory` history | ✅ negative control passes — specs, handoffs, ROADMAP `[x]` lines all retain the old names |
| `ROADMAP.md:27` (17.1 scope note) | ✅ correctly left untouched |

**Both `SKILL.md` bodies are provably identifier-only changes.** Normalizing the old and new identifiers to a common placeholder and diffing the pre/post files returns *identical* for `task-rescue` and, for `task-rescue-audit`, only the three expected `milestone-rescue` → `task-rescue` cross-references (L9, L32, L167). No prose drifted into the skill bodies — the Phase-17.3 boundary held exactly.

**The behavioral check is discharged, with evidence.** The plan required a fresh session because the skills manifest is built at session start. This review session's manifest lists **`task-rescue`** and **`task-rescue-audit`** under their new names, carrying the updated description text (including audit's "Run right after `task-rescue`"). Both resolve and load — this is the wrong-relative-depth failure mode the plan singled out, and it did not occur.

## Issues

### 1. Two unplanned prose additions landed outside the plan's file boundary

Neither is a correctness defect. Both are scope violations, and the second involves a file the plan never names.

**a. `docs/philosophy/skill-cycle.md:45` — a new ~200-word doctrinal paragraph.**

Plan Task 7 is explicit: *"line `41` …, line `43` …, line `70` and `71` … The doc is in Russian; **only the identifiers change, no surrounding prose**."* Spec 71's Scope for this file is likewise "4 references → the new names." The diff instead adds an entire new paragraph theorizing about why prose tasks converge more slowly than code tasks.

**b. `docs/philosophy/skill-composition-model.md:49` — a new cross-reference sentence.**

This file appears **zero times** in the plan and zero times in spec 71. It is not in the seven-file live-surface set that three plan-reviews independently confirmed. It contains no `milestone-rescue` reference and needed no edit for this task.

**Why this matters beyond bookkeeping.** Three things, in descending order of consequence:

1. **It asserts an unverified empirical claim as settled doctrine.** The new paragraph states *"задачи над скилами не сходятся чаще кодовых при том же ревьюере"* — skill tasks fail to converge more often than code tasks at the same reviewer. That is a quantitative claim about pipeline behavior, presented in a governing philosophy doc as established fact, generalized from what appears to be this task's own three-round plan-review history. Nothing in the repo measures it. A doc that leads code should not encode an anecdote as a law.
2. **It reads as the implementing agent editorializing about its own difficulty.** The paragraph's subject is the planning process that produced it — grep-verifications, protocol literals, negative-control checks "in plans." Per the global CLAUDE.md, docs describe *behavior*, and the plan layer is not a thing docs cite. This sits close to that line, and the self-referential framing ("rescue on such tasks is routine manual finishing") risks normalizing non-convergence as expected rather than treating it as signal.
3. **It muddies task ownership.** Phase 17 owns vocabulary conformance across these very docs; 17.3 owns the rescue pair's prose. Landing unplanned doctrine in a rename commit makes it harder for those passes to tell authored-and-ratified content from drive-by additions.

**In its favour, and worth stating plainly:** the prose is well-crafted, it does not contradict existing doctrine, and the reciprocal cross-references are **well-formed and verified to resolve** — `skill-composition-model.md` § "У языка нет компилятора" exists at L43, and `skill-cycle.md` § "Когда task не сходится" exists at L41. Whoever wrote it did the linking discipline correctly. The objection is to *where it landed*, not to its quality.

**Recommended resolution.** Revert both additions from this commit, keeping 16.1 a pure rename — that is what its contract line, spec, and three ratified plan-reviews describe. If the content is wanted (it may well be), give it its own roadmap task so it gets the plan-review scrutiny every other doctrinal change in this repo receives; the empirical claim in particular deserves a reviewer. This is a judgement call for the owner, not a defect I can close unilaterally: the alternative — keeping it and amending the contract line to say the task also added convergence doctrine — is defensible, just less clean.

## Non-issues checked and cleared

- **`orchestrator-artifacts/SKILL.md:7` now wraps ~5 chars shorter** than its neighbours in the folded YAML `description:` block. Cosmetic only — YAML folded scalars are whitespace-insensitive at this level, and the skill-description field loads identically. No action.
- **`ROADMAP.md:21` still reads `[ ]`.** Expected — the orchestrator marks the contract line at commit, not at implement.
- **`docs/reserved-words.md:11` and `docs/using-the-language.md:35`** both took the Task 5 substitution correctly, identifier-only, surrounding sentences intact. The deviation the plan flagged as its one judgement call was executed as specified.
- **No `loads:` edge anywhere names either skill** — re-confirmed; both remain tops, so no caller's forward graph changed.

## Deferred observations

- Affects: Phase 17.3 (`ROADMAP.md:29`) — Both skill bodies still title themselves `# Milestone Rescue` and `# Milestone Rescue Audit`, and the bare word `milestone` remains throughout both (including in `task-rescue-audit`'s own `description:`, which is always-loaded context). Every grep in this task passes clean because none of it is the hyphenated identifier. 16.1's green verification is evidence about the **identifier only** — 17.3 should not read it as prose coverage.
- Affects: orchestrator repo — Orchestrator task `8.2` is `[x]` from the doc-first pass and its docs already publish `/task-rescue` and `/task-rescue-audit`; with 16.1 landing, the two repos are now consistent. Someone on that side should confirm any gate conditioned on "skills 16.1 is `[x]`" is genuinely discharged rather than left dangling on an already-completed task. Outside this repo's boundary.

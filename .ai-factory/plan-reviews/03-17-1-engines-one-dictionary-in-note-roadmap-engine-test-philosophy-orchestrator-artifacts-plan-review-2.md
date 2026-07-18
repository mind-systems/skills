# Plan review — 17.1 Engines: one dictionary in note, roadmap-engine, test-philosophy, orchestrator-artifacts (round 2)

## Code Review Summary

**Files Reviewed:** plan + 4 target `SKILL.md` files (`note`, `roadmap-engine`, `test-philosophy`, `orchestrator-artifacts`), spec 62, spec 72, `ROADMAP.md:27`, `roadmap-prune/SKILL.md`, `docs/philosophy/multiuser-roadmaps.md`, `orchestrator/orchestrator/prompts/reviewer.md`, plan-review-1
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` states the mechanism/policy contract (engine holds shared content, caller keeps control, load-once). This pass is naming-only, with explicit guards that `loads:` edges and both reverse-graph marker sentences stay byte-identical. No boundary touched.
- **Rules** — no `.ai-factory/RULES.md` in this repo. The binding rules are `docs/reserved-words.md` and `docs/using-the-language.md`; the plan conforms to both — it retires synonyms for registry concepts (`task spec`, `contract line`, `task`) while holding protocol tokens (`## Deferred observations`, `- Affects:`, `Spec:`, `` `<note pending>` ``) byte-exact, which is precisely the "protocol tokens are a different axis" discipline.
- **Roadmap** — PASS. `ROADMAP.md:27` carries the 17.1 contract line (verified at that exact line); its `Spec:` tag resolves to `.ai-factory/specs/62-engines-reserved-words-conformance.md`. Governing spec named at spec 62 line 3 is `docs/reserved-words.md` — walked. The plan's task bodies and the contract line agree site-for-site.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent. No project overrides.

### Round-1 issues — all three closed

| Round-1 issue | Status |
|---|---|
| #1 Deferred obs. on `skills/CLAUDE.md` factually false, would seed a phantom task | ✅ Rewritten as a closed observation ("checked, already conformant… **Do not seed a task from this**"), keeping the correct contrast note about the legitimate `milestone` mentions in the three docs |
| #2 Uncommitted-file caveat on `multiuser-roadmaps.md` stale | ✅ Dropped explicitly ("that is no longer true — the file is committed and clean"). Re-verified: `john.doe@example.com` at 15/24, `plans/john-doe/…` at 47, no `kg-` anywhere, and `git status --porcelain` shows no entry for it |
| #3 Stale spec-62 archival line numbers (`:12`/`:22`/`:47`) | ✅ Corrected to **14, 25, 52** — re-read against the amended spec 62; all three land exactly there |

### Verification performed against ground truth

Every citation in Assumptions 1–5 and Tasks 1–6 was re-grepped this session. All hold:

| Claim | Verified |
|---|---|
| `spec note` — 7 sites in `roadmap-engine` (5, 16–17, 28, 69, 103, 105, 209) | ✅ `rg -U -in 'spec\s+notes?'` returns exactly these; the 16–17 wrap confirmed (`spec` ends 16, `note` opens 17) — the one site whose *substitution* spans the break |
| Task 1's verbatim two-line target for 16–17 | ✅ byte-matches the live lines; length-preserving as claimed (`the spec`→`the task`, `note,`→`spec,`) |
| Bare artifact-`note` — 8 sites (33, 36, 43, 47, 75, 212, 213, 214) | ✅ confirmed; 32–33 and 74–75 wraps confirmed, substitutions falling on 33 and 75 alone |
| `roadmap line` at `re:105`, `oa:31` | ✅ exactly two; `oa:31` confirmed **not** wrapped (line 30 ends at `is not`) — the plan's correction of the earlier revision is right |
| `milestone` — `re:104`, `oa:49`, `oa:73`; nothing at `oa:7`/`44` | ✅ Assumption 3 holds; 16.1 landed |
| `oa:73–74` wrap, substitution wholly on 73 | ✅ |
| Legal `note` residue = 9 lines (5, 11, 36, 37, 39, 70, 73, 190, 210) | ✅ matches the four declared classes exactly; no artifact-noun hit among them |
| Guard counts: `<note pending>` / `` Spec: ` `` / `## Deferred observations` | ✅ **2 / 7 / 2**. The 7 resolves to lines 34, 93, 94, 95, 190, 210, 211 — none is an edit target (Task 2 edits 212, not 211), so the count is genuinely invariant |
| `Silent-Failure\|Loud-failure` → 3 at 14 (H1), 25 (H2), 41 (sentence-initial attributive) | ✅ all three exonerated by the rule; Assumption 4's no-edit expectation is correct |
| `note/SKILL.md` synonym-free | ✅ combined grep for `spec note`, `milestone`, `roadmap line`, casing tokens, `kg-*` → exit 1, zero hits. Certification is honest |
| Line widths (re 43: 85→90, re 213: 84→89; oa 68: 81→86 under 67's 89) | ✅ measured 85, 84, 81, 89 — the no-reflow band argument is sound. `oa:31` measured 85 → 86 after `roadmap`→`contract`, also within band |
| Emitter half landed (`reviewer.md:108` reads `task-spec path`) | ✅ re-read this session; `oa:55`'s `spec-note path` is the lagging half, correctly left to 17.5 |
| Out-of-boundary `spec note` survivors are 17.2/17.3's | ✅ `roadmap-outline:40`, `aif-docs:70` → 17.2; `roadmap-decompose`, `-skeleton` → 17.2; `task-rescue`, `-audit` → 17.3. Boundary is clean, nothing orphaned |

Two guard designs deserve explicit confirmation because they are the ones that could silently pass on a broken edit:

- **`git diff --stat` equal-insertions/deletions** holds by construction: every edit in Tasks 1–4 is an in-place line substitution, so each contributes exactly 1 insertion + 1 deletion. There is no edit in the plan that could legitimately change the line count.
- **`rg -U -in 'the\s+note\b'` → zero** is reachable after Task 2: line 33 becomes `task-spec and tag machinery` (killing the 32–33 wrap match), 36 becomes sentence-initial `The task spec`, and 43/47/75 are direct substitutions. The `-i` and `\s+` are both load-bearing exactly as the plan argues.

### Critical Issues

None. Tasks 1–6 are executable as written — no missing step, no wrong assumption about the codebase, no incorrect file path, no API misuse, no behavior risk, and nothing requiring a migration.

### Positive Notes

- **The round-1 corrections were applied at the right depth.** All three were stale-fact defects in the carry-forward section, and rather than patching the three sentences the revision added a governing preamble ("re-grep each claim before acting on it, and treat 'already closed' as the expected outcome, not a surprise. An entry that resolves to nothing is the system working, not a defect in the entry"). That converts a recurring failure mode into a standing instruction — the same generalize-don't-patch move Assumption 1 made for the `\s+` lesson.
- **The retained-but-closed entry is the right disposal.** Round 1 offered "delete the entry, or rewrite it as a closed observation"; the plan took the second option and says why — "this entry has now been dropped once and restored once across revisions; keeping it visible-but-closed is what stops that cycle — a deferred observation is disposed of by being answered, not by being omitted." That is correct discipline and it prevents a third round of the same oscillation.
- **Assumption 5's self-audit remains the strongest reasoning in the plan.** Catching that an earlier revision widened past the spec for `task spec` while deferring the identical class for `contract line`, and resolving it by doctrine rather than convenience, is what a conformance pass should look like. The boundary it draws — in-file yes, reaching into 17.3's `roadmap-prune` no — is principled and enforced by Task 6's file-scoped grep.
- **Task 6 reads the new value back, not just the old one's absence.** The positive assertions on `john.doe@example.com` / `john-doe` close the hole where an implementer deletes the example outright or writes a slug violating the derivation rule stated in the same sentence — the one edit whose correct value must be computed rather than substituted.
- **The residue guard is enumerated by class, not by number.** Targeting zero on `note` would be unclosable because `note` is a skill name that must survive; declaring the four legal classes and requiring every hit to fall in one, while explicitly warning that line numbers shift, is the correct shape for this check.
- **The behavior gate is honest about what it cannot do.** Naming why a headless `roadmap-decompose` render is impossible (`AskUserQuestion` at 164–182 / 196–206, stray writes into `.ai-factory/`) and substituting static byte-identity over the format block, tags, and path templates — with the scratch render demoted to "confirms, it does not gate" — beats a gate that would be silently skipped.
- **The 17.5 boundary is handled precisely.** That `oa:55`'s `spec-note path` is the *lagging* half of an already-half-executed pair rather than a frozen pair, that the synonym grep's `\s+` correctly does not match the hyphenated form, and that the tails stay per-side per 17.5's ruling — three distinct traps, all avoided.

## Deferred observations

- Affects: 17.3 / `.ai-factory/specs/72-cleanup-coupling-one-dictionary.md` — the plan's carry-forward asking that spec 72 be narrowed to `roadmap-prune` 231/276 with a carve-out for 155 is **now closed on disk**, and this is a confirming read rather than open work. Spec 72 line 9 already carries it verbatim: "**Carve-out: line 155 is not the concept** — … substituting 'contract lines' there would corrupt the drop-history description. Edit 231 and 276, leave 155 alone." Ground truth agrees the carve-out is correct: `roadmap-prune:155` reads "the commit before which the prune deleted roadmap lines; equivalently `<prune-commit>^`" — literal lines removed from the roadmap *file* at a git snapshot boundary, not the contract-line tier — while 231 ("touches no roadmap line") and 276 ("its roadmap line and its spec file") are the concept. This resolved-to-nothing outcome is exactly what the plan's own preamble predicts, and its guard sentence ("do not dismiss on the ground that spec 72 already names the substitution") still reads correctly, since the dismissal here rests on the carve-out itself being present, not on the substitution half. Nothing for 17.1 to do; 17.3 inherits a spec that is already right.

PLAN_REVIEW_PASS

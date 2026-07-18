# Plan review — 17.1 Engines: one dictionary in note, roadmap-engine, test-philosophy, orchestrator-artifacts

## Code Review Summary

**Files Reviewed:** plan + 4 target `SKILL.md` files (`note`, `roadmap-engine`, `test-philosophy`, `orchestrator-artifacts`), spec 62, `ROADMAP.md:27`, `docs/philosophy/multiuser-roadmaps.md`, `skills/CLAUDE.md`, `orchestrator/orchestrator/prompts/reviewer.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md:39` states the mechanism/policy contract (engine holds shared content, caller keeps control, load-once). This pass is naming-only with an explicit guard that `loads:` edges and both reverse-graph marker sentences stay byte-identical, so no boundary is touched.
- **Rules** — no `.ai-factory/RULES.md` in this repo. Not applicable (WARN-free; the binding rules are `docs/reserved-words.md` + `docs/using-the-language.md`, and the plan conforms to both — it retires synonyms for registry concepts while leaving protocol tokens byte-exact).
- **Roadmap** — PASS. `ROADMAP.md:27` carries the 17.1 contract line; its `Spec:` tag resolves to `.ai-factory/specs/62-engines-reserved-words-conformance.md`, which the plan's task bodies track faithfully. Governing spec named in spec 62 line 3 is `docs/reserved-words.md` — walked; the plan's substitutions match the registry entries for `task spec`, `contract line`, `task`, and `phase`.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent. No project overrides to apply.

### Verification performed against ground truth

Every line citation in Tasks 1–6 was re-grepped this session against the live files. All of them hold:

| Claim | Verified |
|---|---|
| `spec note` — 7 sites in `roadmap-engine` (5, 16–17, 28, 69, 103, 105, 209) | ✅ `rg -U -in 'spec\s+notes?'` returns exactly these; 16–17 wrap confirmed (`spec` ends 16, `note` opens 17) |
| Task 1's verbatim two-line target for 16–17 | ✅ byte-matches the live lines; length-preserving as claimed |
| Bare artifact-`note` — 8 sites (33, 36, 43, 47, 75, 212, 213, 214) | ✅ confirmed; 32–33 and 74–75 wraps confirmed, substitution falls on 33 and 75 respectively |
| `roadmap line` at `roadmap-engine:105`, `orchestrator-artifacts:31` | ✅ exactly two, both single-line (31 is *not* wrapped — the plan's correction of the earlier revision is right) |
| `milestone` — `oa:49`, `oa:73`, `re:104`; nothing at `oa:7`/`44` | ✅ Assumption 3 holds; 16.1 has landed |
| `oa:73–74` wrap, substitution wholly on 73 | ✅ |
| Legal `note` residue = 9 lines (5, 11, 36, 37, 39, 70, 73, 190, 210) | ✅ matches the four declared classes exactly |
| `grep -c '<note pending>'` → 2; `grep -c 'Spec: \`'` → 7; `grep -c '## Deferred observations'` → 2 | ✅ 2 / 7 / 2 |
| `Silent-Failure\|Loud-failure` → 3 at 14 (H1), 25 (H2), 41 (sentence-initial attributive) | ✅ all three exonerated; Assumption 4's no-edit expectation is correct |
| `note/SKILL.md` synonym-free | ✅ zero hits for `spec note`, `milestone`, `roadmap line`, casing tokens |
| Line-width claims (43: 85→90, 213: 84→89, `oa` 68: 81→86 under 67's 89) | ✅ measured 85, 84, 81, 89 — the no-reflow band argument is sound |
| Emitter half already landed (`reviewer.md:108` reads `task-spec path`) | ✅ re-read this session; `orchestrator-artifacts:55` is the lagging half, correctly left to 17.5 |

This is unusually well-grounded planning. The wrap taxonomy in Assumption 1 (phrase-wraps vs. substitution-wraps, and naming which line each edit falls on) is the right abstraction, and the guard design in Task 6 — enumerating the legal residue by class rather than targeting zero on a word that must survive — is correct where a naive zero-grep would be unclosable.

### Critical Issues

None. Tasks 1–6 are executable as written; no missing step, no wrong file path, no incorrect API usage, no behavior risk.

### Issues

**1. Deferred observation #4 is factually false — `skills/CLAUDE.md` is already conformant.**

The entry claims that file "carries `spec note` at 108 and 166 and 'strategic milestones' at 164", and on that basis raises a scoping question proposing "a 17.6, or an amendment to 17.4's audit sweep". Ground truth (`rg -U -in 'spec note|milestone' CLAUDE.md`) returns **zero hits** across all 197 lines. The cited regions read the conformant words already:

- ~108 — "…in **task specs** are contract text…"
- ~164 — "`/roadmap-outline` (strategic **phases**)"
- ~166 — "New **task specs** land in `.ai-factory/specs/`…"

The file was conformed in an earlier commit (it has no working-tree diff). As written, this entry is addressed to the direction and would seed a phantom task for work that does not exist. **Delete the entry, or rewrite it as a closed observation** ("`skills/CLAUDE.md` was checked and is already conformant; the scope gap between § 'What conforms' and Phase 17's skill-body scope is real in principle but has no live surface"). The contrast note in its second half — that the `milestone` occurrences in `docs/reserved-words.md:5`, `docs/using-the-language.md:23`, `docs/skill-description-field.md:25` are legitimate mentions and stay — is correct and worth keeping under either rewrite.

**2. Deferred observation #1's uncommitted-file caveat is stale.**

The entry states `docs/philosophy/multiuser-roadmaps.md`'s fix "currently sits **uncommitted** in the working tree (3 insertions / 3 deletions)" and instructs the implementer to "confirm the file is committed rather than treating it as settled". `git diff --name-only` shows the working tree carries only five `.ai-factory/` files; that doc is **committed and clean** (verified: `john.doe@example.com` at 15 and 24, `plans/john-doe/…` at 47, no `kg-` anywhere). The premise is false, so the instruction resolves trivially — harmless but misleading to a later reader reconstructing state. Drop the caveat; the entry's main claim (17.1 closes the last two live surfaces) is correct and confirmed by a repo-wide `--hidden` grep: `kg.wmservice`/`kg-wmservice` survive only in `roadmap-engine:57–58` and `orchestrator-artifacts:28–29` outside archival artifacts.

**3. Deferred observation #1 cites stale line numbers for spec 62's archival occurrences.**

It names spec 62 lines `:12`, `:22`, `:47` as the surviving inventory mentions of the old address; the amended spec carries them at **14, 25, 52**. The plan's own § "Assumptions" header notes spec 62 was amended on disk, which is what shifted them — the citation was simply not re-swept. Cosmetic, but it sits in the current artifact and is fixable in-boundary.

### Positive Notes

- **Assumption 5's self-audit is the strongest part of the plan.** Catching that an earlier revision widened past the spec for `task spec` (Assumption 2) while deferring the identical class for `contract line` — and resolving the inconsistency by the doctrine rather than by convenience — is exactly the reasoning a spec-conformance pass should show. The boundary it draws (in-file yes, reaching into 17.3's `roadmap-prune` no) is principled and correctly enforced by Task 6's file-scoped grep.
- **Task 6 reads the new value back, not just the old one's absence.** The positive assertions on `john.doe@example.com` / `john-doe` close the hole where an implementer deletes the example or writes a slug that violates the derivation rule stated in the same sentence — the one edit here whose correct value must be computed rather than substituted.
- **The `\s+`-not-literal-space lesson is generalized rather than patched.** Assumption 1 promotes a single caught defect into a rule applied to every check *and* every citation in the plan, then reports the sweep's results in both directions (including the two the earlier revision got wrong in opposite directions). That is the correct response to a near-miss.
- **The behavior gate is honest about what it cannot do.** Naming why a headless `roadmap-decompose` render is impossible (`AskUserQuestion` at 164–182 / 196–206, stray writes into `.ai-factory/`) and substituting a static byte-identity gate over the format block, tags, and path templates — with the scratch render explicitly demoted to "confirms, does not gate" — is a better outcome than a gate that would be silently skipped.
- **The 17.5 boundary is handled precisely.** Recognizing that `orchestrator-artifacts:55`'s `spec-note path` is the *lagging* half of an already-half-executed pair (not a frozen pair), that the synonym grep's `\s+` correctly does not match the hyphenated form, and that the tails must stay per-side per 17.5's ruling — three distinct traps, all avoided.

## Deferred observations

- Affects: 17.3 / `.ai-factory/specs/72-cleanup-coupling-one-dictionary.md` — the plan's carry-forward about spec 72 over-including `roadmap-prune:155` is correct and should be acted on before 17.3 runs. Line 155 describes lines removed from the roadmap *file* during a prune ("the commit before which the prune deleted roadmap lines; equivalently `<prune-commit>^`") — a git snapshot boundary, not the contract-line tier — so substituting "contract lines" there would make the sentence assert something it does not mean. 17.3 must edit 231 and 276 and leave 155 alone. Recorded here so the carve-out survives this plan, which is transient while the spec persists.
- Affects: `.ai-factory/specs/62-engines-reserved-words-conformance.md` — spec 62's § Guards (line 38) and § Verification item 3 (line 53) have been amended and now correctly expect zero `milestone` in `orchestrator-artifacts`, so the plan's carry-forward about a "stale Phase-16 carve-out" outliving this plan appears already closed on disk. Worth one confirming read at implementation time before treating that carry-forward as live work — if it is indeed closed, the entry can be dropped rather than propagated.

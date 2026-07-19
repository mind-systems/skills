# Plan Review 3 — 19.1 aif family: stop generating retired artifacts, align to the canonical harness contract

## Code Review Summary

**Files Reviewed:** plan + spec `78-aif-generates-to-norm.md` + contract lines 19.1/19.2 + 3 skill bodies (`aif`, `aif-architecture`, `aif-docs`) + 3 surviving `references/` files
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" governs when a capability is factored into its own skill. This task adds and removes no skill and no `loads:` edge; it retires three `references/` files private to `aif` and edits instruction text in place. No boundary moves.
- **Rules** — WARN (non-blocking). No `.ai-factory/RULES.md` exists in this repo, so there are no project rules to check against. Noted only because this task is *about* that artifact's canonical path in generated projects — the absence here is unrelated and not a defect.
- **Roadmap** — PASS. Contract line 19.1 is present at `.ai-factory/roadmaps/trickster77777.md:15`, names `Spec: .ai-factory/specs/trickster77777/78-aif-generates-to-norm.md`, and its guard clause ("fixed-English invariant restated per-generator … config-residue sweep grep-defined, verified by content") is what the plan implements. The deferred `Bash(ln *)` grant has its own line at :16 (19.2) with the matching mutual-preservation guard on both sides. Linkage complete.

### Round 2's critical issue: resolved

Round 2 raised exactly one blocker — Task 6's language split overrode the spec's "`aif-docs` goes **fully ambient**" ruling with no spec amendment recorded, leaving the governing spec asserting behavior the shipped code would not have. **Verified fixed at the source, not merely claimed.**

Spec L18 now rules the split in its own words: `aif-architecture` fixed-English for `ARCHITECTURE.md` with ambient prompts, `aif-docs` **splits** — docs content ambient, the `## Documentation` index sections written into `CLAUDE.md`/`AGENTS.md` staying fixed English — with the two-skills-disagreeing-about-the-same-bytes argument carried into the spec itself. Spec Verification L42 no longer says a blanket "language ambient"; it now says "language per the per-generator rule above, not a blanket ambient" and names the three concrete runtime outcomes. `git status` confirms the spec file is modified in the working tree.

The plan's Task 6 additionally handles the trap this amendment creates: the amended bullet still contains the words "fully ambient" inside the sentence explaining why a blanket ruling was *rejected*, so a bare grep for that phrase reads as though nothing changed. Task 6 says so explicitly and directs confirmation by content. That is the right call and it is correct — I hit exactly that string while verifying.

### Verification performed against ground truth

Every line-number claim in the plan was checked against the actual files, not taken on the plan's word:

- **`aif/SKILL.md` deletion range L43–65 is exact.** L43 *is* the `## Language Resolution` heading, L65 *is* the `config-persistence.md` pointer, L67 *is* the surviving `rules-generation.md` pointer, and L41/L69 are the two `---` rules. Task 3's core worry — that L67 would float headingless between them — is real, and `## Rules Generation` is the correct fix.
- **The English-invariant sweep enumerations are complete, not samples.** `grep -n 'language\.ui\|language\.artifacts\|Localized'` returns, for `aif/SKILL.md`: L45/47/49/51/53 (inside the deleted range) plus L93, L138, L171, L232, L235–240, L245 — Task 4's list, exactly. For `aif-architecture`: L19/L21 (Step 0), L146, L149–159 (Step 4's L146–159 range) — Tasks 5's two bullets, exactly. For `aif-docs`: **only** L34 and L260, both ordered by Task 6. I specifically looked for an unordered `[Localized …]` sweep in `aif-docs` that Task 6 lacks a bullet for — there is none to order. No gap.
- **`grep -n 'resolved architecture'` in `aif-architecture` returns L73, 124, 126, 134, 136, 146, 152, 164, 165** — the plan's list verbatim, with L73 correctly identified as the `$ARGUMENTS` pattern sense (`Use the resolved architecture directly, skip the recommendation step`), the one byte-identical survivor.
- **`paths.docs` in `aif-docs` → L19, L22, L33, L41, L260.** Five, as Task 6 claims; all five ordered.
- **`.ai-factory/rules/` directory residue at `aif/SKILL.md` L116** confirmed live ("Ensure `.ai-factory/rules/` directory exists") — the case that `rules/base\.md` does not match, justifying the fourth grep term.
- **Task 8 strands nothing.** `grep -rn 'config-persistence\|config-template\|update-config'` across `src/`, `docs/`, `active/` and the sibling `orchestrator/` repo returns only `aif/SKILL.md` L5, 65, 85, 113, 134, 177 plus the three files themselves. All six lines sit inside ranges Tasks 1/3/4 edit (L85/L134/L177 are the three modes' Persist-config.yaml steps).
- **Task 9's zero-hit grep is achievable.** Against the three surviving `references/` files the pattern currently hits only `rules-generation.md` L3, L7, L17 — precisely the three renames Task 7 orders — plus L5's "After language resolution and config write", also ordered. `mcp-configuration.md` and `stack-analysis.md` are clean of every term in the pattern; `mcp-configuration.md`'s 4 bare-`config` hits are MCP-configuration prose, correctly pre-cleared as legitimate survivors of the wider net.
- **Task 4a's self-contradiction is live.** L218 primary ownership omits `RULES.md`; L220 declares it read-only. Once Task 4 makes Step 7 write it, the body contradicts itself. Correctly scoped in as introduced-by-this-change.
- **Step-number cross-references** — the renumber instruction has four real targets I could find: L110 "(generated in Step 3)" → Step 2; L130 "once Step 4's dialog answers land" → Step 2; L173 "the Step 2 description" → Step 1 and "once Step 5's dialog answers land" → Step 3. Task 4's blanket "every cross-reference to a step number still resolves" plus Task 9's end-to-end mode read covers all four. This is exactly the class of detail a deletion-and-renumber plan usually drops.

### Critical Issues

None.

### Positive Notes

- **The spec amendment was made at the source and confirmed by content.** Round 2 offered two acceptable fixes and named the weaker one; the plan took the stronger one — amending spec L18 and L42 rather than annotating a live contradiction — and then documented the grep trap the amendment leaves behind. Reconciling a governing spec with the code it governs, rather than shrugging at the drift, is the behavior the repo's own grounding discipline asks for.
- **The inverse-trap analysis remains the plan's best work, and it survived three rounds intact.** "No zero-hits check can notice an invariant that vanished, because its absence *is* the clean state every other check is looking for" is the correct diagnosis of a deletion-shaped task, and it is answered in four places rather than merely observed: Task 3 folds the invariant into `## CLAUDE.md Generation`, Task 5 restates it in `aif-architecture` (verified: L25 really is that file's only `english` hit), Task 9 asserts it as a deliberately non-zero grep, Task 10 exercises it live.
- **Task 9's asymmetric English checks are reasoned per-file, not assumed uniform.** The bare grep is trusted on `aif-architecture` (sole hit, so any survivor must be the restatement) and explicitly refused on `aif/SKILL.md`, where L37 and L117 survive independently and would read green over a forgotten fold. The `AGENTS.md` co-occurrence discriminator is sound — I confirmed neither L37 nor L117 names `AGENTS.md`.
- **The four false-green axes are exhaustive.** `config`-without-`.yaml`, `paths.*`, "resolved architecture path", and `.ai-factory/rules/` — each with a live case, each wired into Task 9, and the grep declared authority over the line lists rather than the reverse. Re-verified hit-by-hit this round; nothing is reachable only by an unlisted pattern.
- **The `<resolved docs dir>` ruling is the right restraint.** Refusing to sweep ~20 phrasings to a literal `docs/`, on the ground that resolution still has a live referent (`docs/` by default *or* the project's existing docs directory) and only one *source* of it was removed, avoids both an overreach of the register guard and an assertion less true than the current text. Making Step 0 the definition site instead is the minimal correct move.
- **Task 4's scope widening is justified and then actually paid for.** Modes 2 and 3 never wrote the rules artifact; a scratch project routes to Mode 3; the spec's first verification check would be unsatisfiable without closing that pre-existing gap. Having leaned on that check to widen scope, Task 10 commits to running it — the plan notices it owes that debt and settles it.
- **Task 10 refuses to hedge the non-English session.** "Not 'if practical'… If a non-English session genuinely cannot be arranged, say so explicitly rather than reporting Task 10 as passed" is the correct posture: an English-ambient run produces English artifacts whether the invariant survived or not and can distinguish nothing. Reporting reduced coverage honestly beats a green box.
- **Scope discipline held at three boundaries, each with a named home** — `Bash(ln *)` to 19.2 (with the same-line mutual guard recorded on both the plan and the contract line), the rotted `rules-generation.md` L11 spec citation left byte-identical, and the `orchestrator/docs/configuration.md` residue routed to the sibling repo rather than reached into.

## Deferred observations

- Affects: unknown (pre-existing, `src/skills/aif/references/rules-generation.md` L11) — the file cites `.ai-factory/specs/41-aif-rules-counter-default-filter.md` as the home of its composition-model reasoning; no such file exists under `.ai-factory/specs/` or `.ai-factory/notes/`. Task 7 correctly orders everything outside its four named edits byte-identical, and the edge rotted independently of this task, so it is out of scope here. It wants its own contract line — either repoint it at the surviving artifact or drop the parenthetical.
- Affects: `orchestrator/.ai-factory/` — `orchestrator/docs/configuration.md:87` disambiguates the orchestrator's own overlay against `.ai-factory/config.yaml`; once this task retires that artifact the sentence disambiguates against nothing. Correctly excluded by the spec's scope guard, which confines this task to the aif-family skill sources; noted so the sibling-repo follow-up is not lost.

PLAN_REVIEW_PASS

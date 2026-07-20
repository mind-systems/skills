# Plan Review: 19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract (round 2)

## Code Review Summary

**Files Reviewed:** plan (round 2) + spec `78-aif-generates-to-norm.md` + roadmap contract lines 19.1/19.2 + 4 target skill bodies (`aif/SKILL.md`, `aif/references/rules-generation.md`, `aif-architecture/SKILL.md`, `aif-docs/SKILL.md`) + the 3 deletion targets + the 3 surviving reference files
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`) — **PASS**. In-place edits to skill bodies; no engine extracted, no engine content inlined into a lens. `rules-generation.md` stays a reference of `aif`, its only caller.
- **Rules** (`.ai-factory/RULES.md`) — **WARN**, file absent in this repo. No rule surface to check against; carried from round 1, unchanged and still out of scope.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md` L15) — **PASS**. Linkage explicit; the 19.2 co-ordination guard on `aif/SKILL.md` L5 is honored in both directions (Task 1 drops only the `update-config.mjs` grant, leaves the rest for 19.2 to extend).
- **Governing spec** (`docs/sakshi-harness/sakshi-harness.md` via the spec's Phase 19 header) — **PASS**. Retiring `config.yaml` and moving the rules artifact to `.ai-factory/RULES.md` moves the generators toward the wiring contract.

### Round-1 issues: all three resolved

1. **`aif-docs` fully-ambient collision** — resolved, and resolved better than the round-1 fix suggested. Task 6's second bullet now splits the ruling into a named ambient half and a named fixed-English half, argues each on its own evidence, and propagates the split into Task 9's content assertion and Task 10 Run 2's fourth bullet. The `aif`-vs-`aif-docs` contradiction over the same `## Documentation` bytes is closed.
2. **L51 in Task 4's sweep list** — dropped. The list now reads L93, L138, L171, L232, L235–240, L245; all six survive Task 3's L43–65 deletion. Verified.
3. **`references/mcp-configuration.md` missing from Task 9's expected survivors** — added, with its hit count (4) named inline.

### Verification of the plan's factual claims

Re-checked independently against the files, not carried from round 1. **Every claim holds exactly.**

- `grep -n 'resolved architecture' src/skills/aif-architecture/SKILL.md` → L73, 124, 126, 134, 136, 146, 152, 164, 165 — the plan's list precisely, and L73 is indeed the `$ARGUMENTS` pattern sense.
- `grep -in 'english' src/skills/aif-architecture/SKILL.md` → **only L25**. The plan's central worry — that Task 5's deletion strips the file's sole English statement — is real.
- `grep -in 'english' src/skills/aif/SKILL.md` → L37, L47, L51, L59, L117. L47/L51/L59 fall inside L43–65; L37 and L117 survive, exactly the two false-green survivors Task 9 predicts, and neither names `AGENTS.md` — so the co-occurrence proxy is a sound discriminator.
- `paths.docs` in `aif-docs` → L19, L22, L33, L41, L260. Five, as claimed.
- **Task 9's wider `config` net is now exhaustive** — checked hit-by-hit. `aif-architecture`: L17/21/23 (Step 0, Task 5), L134, L165 — all ordered edited, no unlisted survivor. `aif-docs`: L3, L32, L36, L43, L241, L260, L267, L271 — every one either ordered edited or named as a legitimate survivor. `references/`: `mcp-configuration.md` 4 hits (named), `stack-analysis.md` **0** hits, `rules-generation.md` 1 hit at L5 which Task 7 explicitly edits away. The enumeration leaves nothing unaccounted for.
- **Anchor safety** — `[Language Resolution](#language-resolution)` occurs at L79, L128, L158 only, all three inside "Resolve Language Settings" steps Task 4 deletes. No dangling anchor survives. The `#claudemd-generation` anchors at L81/L130/L173 keep a live target.
- **Deletion safety** — `grep -rn 'config-persistence\|config-template\|update-config\.mjs'` across `src/`, `docs/`, `active/`, and the sibling `orchestrator/` repo returns only `aif/SKILL.md` (L5, 65, 85, 113, 134, 177) and the three files themselves. Every one of those six lines is inside a range Task 1/3/4 edits. Task 8 strands nothing.
- Mode 1 Step 7 sub-item 2 (`mkdir -p .ai-factory`, L111) does cover the `RULES.md` write's directory need, as Task 4 claims.
- `aif-docs` Step 5's symlink branch (L252) exists, which is what makes Task 10's "if it is a regular file rather than a symlink" qualifier correct rather than hedging.

## Critical Issues

**1. Task 6's split overrides the spec's explicit "fully ambient" ruling, and the plan records no spec amendment — leaving the task spec asserting behavior the shipped code will not have.**
*Plan Task 6, second bullet; spec `78-aif-generates-to-norm.md` Change L18 and Verification L42.*

Spec L18 does not merely omit the fixed-English half for `aif-docs` — it rules against it in so many words: "`aif-docs` goes **fully ambient**". Task 6 correctly overrides that (round 1's issue 1 is a genuine defect and the split is the right resolution), but the plan presents the override as a *derivation from* the spec rather than a departure from it. Task 6 argues "Docs are **absent** from the spec's fixed-English artifact list (Change L17…)", which is true of L17 and reads as conformance — while L18, one line down in the same section, says the opposite and goes unquoted.

The consequence is concrete. After this task lands: `aif-docs/SKILL.md` Step 0 says the `## Documentation` sections written into `CLAUDE.md`/`AGENTS.md` stay English; spec L18 says `aif-docs` is fully ambient; spec Verification L42 says `/aif-architecture` and `/aif-docs` both run "language ambient", which is *also* wrong for `aif-architecture` under Task 5. A task spec is a governing statement of intended behavior — when it and the code it governs disagree, that is a defect to reconcile, not a stale doc to shrug at. And this one is introduced by this change: today L39's `en` is what pins those writes, so no disagreement exists yet.

This is squarely inside the task's boundary — it is the task's *own* spec, and the plan is otherwise scrupulous about recording what it defers (three items in "Carried forward", each with a home). This one has no home.

Fix — either is acceptable, but one of them must happen:
- Amend spec L18 to state the split as Task 6 implements it, and correct L42's blanket "language ambient" to name the per-generator rule the spec itself establishes at L17–18; **or**
- If amending the spec is out of scope for this run, add a `DEVIATION:` annotation on Task 6 naming L18 verbatim as the overridden text and the evidence for overriding it, and add a fourth "Carried forward" entry so the spec reconciliation is not lost.

The second option is weaker — it leaves the contradiction live — but it at least makes it visible. Silently shipping a split against a spec that says "fully ambient" is the one outcome to avoid, and it is the current one.

## Positive Notes

- **The round-1 fix on `aif-docs` overshot the review in the right direction.** Round 1 asked for the two halves to be split; Task 6 additionally records *why* deleting L39 is a real behavior change rather than the no-op that "defaults become the only path" implies, identifies L39-vs-item-4 as a pre-existing contradiction inside the file, and states which way this task resolves it and why. That reasoning is what makes the edit auditable later.
- **Task 9's `aif-docs` check was flipped, not patched.** The round-1 plan exempted `aif-docs` from the English assertion outright ("the deliberate exception … needs no such hit"); round 2 replaces the exemption with a two-halves content check and marks the change explicitly ("**not** exempt (it was, before Task 6's split ruling)"). Amending a verification check in lockstep with the ruling it verifies, and flagging that it moved, is the discipline that keeps a checklist from drifting into decoration.
- **The false-green analysis remains the strongest part of the plan** — four axes (`config`-without-`.yaml`, `paths.*`, "resolved architecture path", `.ai-factory/rules/`), each with a live case, each wired into Task 9. Verified exhaustive above; it genuinely leaves no residue reachable only by an unlisted pattern.
- **The inverse trap and its four-place follow-through.** "No zero-hits check can notice an invariant that vanished, because its absence *is* the clean state every other check is looking for" is exactly right, and Tasks 3, 5, 9, and 10 each carry a piece of the answer rather than the plan merely observing the risk.
- **Task 9's asymmetric English checks** — bare grep trusted on `aif-architecture` (sole hit at L25, so any survivor is the restatement), refused on `aif` (two independent survivors), with the `AGENTS.md` co-occurrence as a mechanical discriminator. Reasoned per-file, not assumed uniform; both halves verified correct here.
- **Task 10's refusal to hedge the non-English session**, and its instruction to report Task 10 as *not passed* rather than downgrade silently if one cannot be arranged. The added fourth bullet — the `## Documentation` table staying English while doc pages come out ambient, observed in one run — is the only runtime check that can catch the two skills disagreeing about the same bytes.
- **Task 4a** catches a self-contradiction (`RULES.md` declared read-only while Step 7 writes it) that this diff introduces and the spec's `## Change` list does not name. Verified live at L218/L220.
- **Scope discipline held three times** — `Bash(ln *)` deferred to 19.2 with a matching contract line already drafted and the mutual-preservation guard noted on both sides; the `rules-generation.md` L11 rotted spec citation recorded but not repointed; the `orchestrator/docs/configuration.md` residue routed to the sibling repo. Each with a named home.

## Deferred observations

- Affects: unknown (pre-existing, `src/skills/aif/references/rules-generation.md` L11) — the file cites `.ai-factory/specs/41-aif-rules-counter-default-filter.md` as the home of its composition-model reasoning; no such file exists under `.ai-factory/specs/` or `.ai-factory/notes/`. Task 7 correctly orders everything outside its four named edits byte-identical, so it is out of scope here, and the edge rotted independently of this task. It wants its own contract line — either repoint it at the surviving artifact or drop the parenthetical. [fixed]
- Affects: `orchestrator/.ai-factory/` — `orchestrator/docs/configuration.md:87` disambiguates the orchestrator's own overlay against `.ai-factory/config.yaml`; once this task retires that artifact the sentence disambiguates against nothing. Correctly excluded by the spec's scope guard; noted so the sibling-repo follow-up is not lost. [fixed]

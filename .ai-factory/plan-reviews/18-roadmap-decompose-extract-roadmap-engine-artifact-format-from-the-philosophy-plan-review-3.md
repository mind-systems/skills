# Plan Review (round 3): roadmap-decompose — extract `roadmap-engine` (artifact format)

**Plan:** `18-roadmap-decompose-extract-roadmap-engine-artifact-format-from-the-philosophy.md`
**Files reviewed:** `roadmap-engine/SKILL.md`, `roadmap-decompose/SKILL.md`, `aif-roadmap/SKILL.md` (frontmatter), full `src/skills` reference-graph, round-2 review
**Risk Level:** 🟢 Low

## Verdict

The single Medium blocker from round 2 — the dangling `Two-Tier Output` reference at decompose **line 198**, inside the Step 2.4.1 Atomicity Gate block — is now fully resolved. The plan adds line 198 to the repoint list (Task 3, plan line 43) and adds an explicit carve-out (plan line 47) that repoints its trailing pointer while keeping the gate's decision logic verbatim, and states this "resolves the byte-identical-vs-repoint contradiction." No new gaps introduced. The plan is internally consistent, factually accurate against the current file state, and ready to implement.

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy"): the plan's engine-vs-philosophy split (engine = artifact-format mechanism; decompose = decomposition policy) aligns with the mechanism/policy model. `WARN` only on the single-caller tension (see below) — the plan handles it transparently.
- **Rules** (`.ai-factory/RULES.md`): not present as a discrete file; the composition rule in `CLAUDE.md` is addressed under the WARN below.
- **Roadmap**: this plan corresponds to a roadmap milestone in the roadmap family (16 = engine creation, 17 = test-engine, 18 = this split). Linkage is present. No missing linkage.

## Round-2 blocker — resolved

- **Residual dangling reference at line 198 (was Medium):** Fixed. Plan line 43 now enumerates the five references as **136 / 187 / 198 / 208 / 210** and explicitly annotates 198 as "(Mode 2.4.1 Atomicity Gate, closing '→ proceed with the Two-Tier Output procedure')." Plan line 47 adds the carve-out: line 198 lives inside the 2.4.1 gate, its decision logic stays verbatim, but the trailing `Two-Tier Output procedure` reference is repointed like the others "so no pointer to the deleted section survives," with an example rewrite. It also correctly notes Step 1.3.1's gate needs no such edit (it closes by pointing at "Step 1.4", which stays). ✔

## Fact & line-number re-verification (current file state)

Verified directly against the files:

- decompose "Roadmap File Format" heading **302**, block **304–314**, contract-line rules **316–323** ✔
- decompose "Two-Tier Output (per task)" procedure **284–298**; Atomicity Gate embedded as its step 2 at **289** ✔
- Exactly five `Two-Tier Output` references in the body: lines **136, 187, 198, 208, 210** (grep-confirmed) — matches the plan's repoint list exactly, with none omitted and none invented ✔
- decompose intro **line 16**, Critical Rule 6 **line 332** ✔
- engine sections to remove — "Input Contract" (**23**), "Per-Task Render Procedure" (**42**), "What This Engine Does NOT Own" (**94**) ✔
- **Caller reality confirmed:** `roadmap-decompose-skeleton` directory does **not** exist; `aif-roadmap` `allowed-tools` = `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions` (**no `Skill`**, cannot invoke the engine); `roadmap-engine` is referenced by **no external skill** (only itself). The plan's "Caller reality" section (plan lines 6–12) is accurate. ✔

## Consistency checks (new this round)

- **aif-note load-once knowledge survives the split.** Task 1 explicitly carries into the engine "the note is written following aif-note's note format, with aif-note loaded once per chat; `<NN>` is scanned against `.ai-factory/notes/`." So when decompose's repointed references say "load `roadmap-engine` once for the artifact format, then produce the two-tier artifacts per that format," the aif-note-loaded-once and NN-collision guidance is preserved in the engine — no knowledge is dropped in the move. ✔
- **Atomicity Gate stays in decompose only.** Task 1 forbids carrying the gate into the engine; decompose keeps its standalone 1.3.1 / 2.4.1 gate blocks. The gate is philosophy (policy), correctly retained on the philosophy side. ✔
- **Guards are content-preserving, not rewrites.** Task 1's guard ("same content, reflowed from numbered steps into prose") and Task 3's guard ("no longer restate the format or the numbered procedure … philosophy wording otherwise unchanged") are mutually consistent with Task 4's verification checklist. ✔

## Accepted WARN (carried, not a blocker) — single real caller

Post-plan the engine has exactly one caller (`roadmap-decompose`), which is in tension with the `CLAUDE.md` composition rule ("factor into its own skill only when it carries shared content used by ≥2 callers"). The plan handles this honestly and transparently: it declares the engine forward-looking shared-format infra, forbids Task 2 from asserting three callers, and states (plan line 12) it "does not fix [the pre-existing condition] beyond making the wording honest." This is a legitimate scoping decision, not a defect this plan introduces. Recommendation only: keep the later `aif-roadmap` / `roadmap-decompose-skeleton` wiring on the roadmap so the engine does not stay a single-caller loader indefinitely.

## Minor observation (non-blocking, no action required)

The generic repoint text ("load `roadmap-engine` once for the artifact format, then produce the two-tier artifacts per that format") is applied to all five sites, but decompose **line 136** (Mode 1 Step 1.4) currently also carries mode-specific placeholder-replacement flow ("replace the `` Spec: `<note pending>`. `` placeholder with the real `Spec:` tag"). The plan's Task 3 bullet already covers this by saying the agent "renders per each mode using the engine's format — create writes the file, add appends, decompose-existing edits the named note in place," so the mode-specific behavior is preserved at the instruction level. The implementer should retain the `<note pending>` → real-tag mechanic at line 136 when repointing; the plan does not contradict this, so it is a note, not a gap.

## Positive Notes

- The round-3 carve-out is precise: it names line 198, quotes its current wording, provides an example rewrite, and explicitly distinguishes gate *decision logic* (verbatim) from the *pointer* (repointed) — dissolving the exact contradiction round 2 flagged.
- The "Caller reality" section remains the model response to the aspirational 3-caller framing — it corrects the premise with cited evidence and scopes wiring out explicitly.
- Every line number in the plan matches the current file state; the five-reference enumeration is exhaustive and correct with no phantom sites.
- Clean separation of concerns: format/mechanism → engine, decomposition/policy (modes, gate, exploration, AskUserQuestion) → decompose, with Task 4 providing a concrete, testable verification checklist.

## Recommendation

All round-1 and round-2 findings are resolved and re-verified against the current files. No blocking issues remain.

PLAN_REVIEW_PASS

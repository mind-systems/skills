# Plan Review: 19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract

## Code Review Summary

**Files Reviewed:** plan + spec `78-aif-generates-to-norm.md` + roadmap contract line 19.1/19.2 + 4 target skill bodies (`aif/SKILL.md`, `aif/references/rules-generation.md`, `aif-architecture/SKILL.md`, `aif-docs/SKILL.md`) + the 3 deletion targets
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`) — **PASS**. The task edits skill bodies in place; it neither extracts a new engine nor inlines an engine's content into a lens, so "Composition: mechanism vs policy" is untouched. `rules-generation.md` stays a reference of `aif`, its only caller.
- **Rules** (`.ai-factory/RULES.md`) — **WARN**, file absent in this repo. No rule surface to check against; noted only so the gap is visible. (Mildly ironic given the task's subject, but out of scope.)
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md` L15) — **PASS**. Task linkage is explicit and the plan honors 19.2's co-ordination guard: 19.2 warns that 19.1 Task 1 edits the same `allowed-tools` line, and the plan's "Carried forward" section correctly refuses to add `Bash(ln *)` here, leaving it to 19.2. Correct split.
- **Governing spec** (`docs/sakshi-harness/sakshi-harness.md` via spec Phase 19 header) — **PASS**. Retiring `config.yaml` and moving the rules artifact to `.ai-factory/RULES.md` moves the generators toward the wiring contract, not away from it.

### Verification of the plan's factual claims

Every line number and grep prediction in the plan was checked against the files. **All of them hold exactly** — this is unusually well-grounded reconnaissance:

- `aif/SKILL.md`: L3, L5, L12, L33, L37, L39, L43 (`## Language Resolution` heading), L47, L65, L67, L69, mode ranges L71–120 / L124–150 / L154–189, Step-7 sub-items 3–5 at L112–114 and item 6 at L115–117, L116, L120, L81/L130/L173, L216–220, L232/L234–241/L245 — all verified.
- `aif-architecture/SKILL.md`: `grep -n 'resolved architecture'` returns **exactly** L73, 124, 126, 134, 136, 146, 152, 164, 165 — the plan's list, no more, no less. `grep -in 'english'` returns **only L25**, confirming the plan's central worry that deleting L15–25 without replacement strips the file's sole English statement.
- `aif/SKILL.md` `grep -in 'english'` returns L37, L47, L51, L59, L117. L47/L51/L59 sit inside the L43–65 deletion; L37 and L117 survive — exactly the two false-green survivors Task 9 predicts. The content-based assertion (a hit that *also* names `AGENTS.md`) is a sound discriminator: neither L37 nor L117 names it.
- `aif-docs/SKILL.md`: `paths.docs` occurs at L19, L22, L33, L41, L260 — five, as claimed. The `<resolved docs dir>` survivor list (L49, 81, 100, 121, 143, 145, 154, 156, 162, 170, 238–241, 245, 259, 271) is accurate.
- **Deletion safety confirmed independently:** `grep -rln 'config-template\.yaml\|config-persistence\.md\|update-config\.mjs'` across `src/`, `active/`, and the sibling `orchestrator/` repo returns only `aif/SKILL.md` and the three files themselves. Task 8 strands nothing.
- **Residue containment confirmed:** `grep -rn 'rules/base\.md\|\.ai-factory/rules\|config\.yaml' src/ docs/` returns hits **only** inside the four target files and the three deletion targets. Nothing outside the aif family needs a follow-up edit in this repo, so the spec's scope guard is genuinely sufficient.

The plan's structural analysis is also correct on the two points it flags as its own risk surface: the fixed-English invariant is a survival requirement inside deletion ranges (Task 3 / Task 5 restatements, Task 9's deliberately non-zero grep, Task 10's non-English run) and the `RULES.md` read-only/primary-ownership contradiction Task 4 would introduce is real and correctly caught by Task 4a. Both are the kind of defect that normally ships silently.

### Critical Issues

**1. `aif-docs` "fully ambient" ruling collides with the fixed-English invariant on `CLAUDE.md` and `AGENTS.md` — the two skills would prescribe opposite languages for the same section of the same file.**
*Plan Task 6, second bullet; `aif-docs/SKILL.md` L130–146, L227–251, L259.*

Task 6 rules `aif-docs` **fully ambient** and deletes L39 (`- Language: `en` (English)`), justified as: "Generated docs are **absent** from the spec's fixed-English artifact list (Change L17 names CLAUDE.md/RULES.md/AGENTS.md/ARCHITECTURE.md — not docs)."

That reasoning is sound for the docs directory, but `aif-docs` does not only write docs. Its own `## Artifact Ownership` (L259) claims primary ownership of **"the Documentation section in `AGENTS.md`, and the `## Documentation` section in `CLAUDE.md`"**, and it actively writes both:
- L130–146 — "Update the CLAUDE.md Documentation Index": creates/updates `## Documentation` in the project's `CLAUDE.md`, including the `| Doc | What it covers |` header row and per-row descriptions. L146 even authorizes *creating CLAUDE.md* if absent.
- L227–251 — Step 5 writes the `| Document | Path | Description |` table into `AGENTS.md`.

Both files are on the spec's fixed-English list, and `aif`'s own `## CLAUDE.md Generation` L37 explicitly names `## Documentation` (with that exact table header) as a **fixed English heading**. So after this task: `aif` says the CLAUDE.md `## Documentation` table is fixed English; `aif-docs` — invoked standalone against a Russian-README project — says write it ambient. Two skill bodies, executable code, giving contradictory instructions for the same bytes. This is the same class of self-contradiction Task 4a exists to prevent, one file over.

It is introduced by this change: today L39's `en` default is what (inconsistently, but in the right direction) pins those writes to English.

Fix: scope the ambient ruling the way Task 5 scopes its English one — **split the two halves explicitly**. Step 0's replacement text should say that generated documentation content follows the ambient/project language per `## Important Rules` item 4, **while the `## Documentation` index sections `aif-docs` writes into `CLAUDE.md` and `AGENTS.md` keep fixed English headings and table text**, matching `aif`. Note this is precisely the shape Task 5 already uses for `aif-architecture` ("Do not write 'language ambient' as a blanket statement for this file") — the same care is owed here, and Task 6's current text does the opposite by making "fully ambient" a blanket. Task 9 should then assert `aif-docs` carries this statement rather than treating the file as needing no English hit at all (currently: "`aif-docs` is the deliberate exception … and needs no such hit"), and Task 10 Run 2's ambient-docs assertion should add: the `## Documentation` table written into `CLAUDE.md` stayed English in the non-English session.

### Minor Issues

**2. Task 4's sweep list cites L51, which Task 3 has already deleted.**
*Plan Task 4, final paragraph.*

The sweep enumerates "L51, L93, L138, L171, L232, L235–240, L245". L51 (`Ask them in resolved `language.ui`, never hard-code English…`) sits inside the L43–65 range Task 3 deletes in full, and Task 4 depends on Task 3. Harmless in effect — sweeping a deleted line is a no-op — but in a plan whose reconnaissance is otherwise line-exact, an implementer hunting a line that no longer exists will burn time deciding whether they mis-applied Task 3. Drop L51 from the list.

**3. Task 9's wider-net grep omits `references/mcp-configuration.md` from its expected-survivor enumeration.**
*Plan Task 9, fourth bullet.*

The check greps `src/skills/aif/references/` and instructs the implementer to "confirm each [hit] is one of them", listing MCP configuration in `aif/SKILL.md`, `aif/SKILL.md` L73, and `aif-docs` L241/L267. But `references/mcp-configuration.md` is inside the grepped path and carries 4 `config` hits of its own (verified). They are obviously legitimate, but an enumeration presented as exhaustive should name the file, or the implementer reasonably reads unlisted hits as misses to fix. Add it to the expected-survivor list.

### Positive Notes

- **The false-green analysis is the strongest part of this plan.** Identifying that Findings 4–6 say "config" not "config.yaml", then generalizing to three further axes (`paths.*`, "resolved architecture path", `.ai-factory/rules/`) that contain no "config" string at all, and widening Task 9 to cover each — that is the reconnaissance that keeps a grep-defined sweep honest. The `.ai-factory/rules/` axis in particular catches a live residue (L116) that `rules/base\.md` genuinely misses.
- **The inverse trap is rarer still, and correctly named.** "No zero-hits check can notice an invariant that vanished, because its absence *is* the clean state every other check is looking for" is exactly right, and the plan follows through on it in four places (Tasks 3, 5, 9, 10) rather than just observing it.
- **Task 9 asserting the `aif` English survivor by content rather than hit count**, having first proven the bare grep is a false green on that file but sound on `aif-architecture` — the asymmetry is reasoned, not assumed, and the `AGENTS.md` co-occurrence proxy is a genuinely mechanical discriminator.
- **Task 10's insistence on a non-English session, and its refusal to hedge it as "if practical"**, is the correct call: an English-ambient run cannot distinguish a live invariant from a deleted one. The explicit instruction to report Task 10 as *not passed* rather than silently downgrading is good discipline.
- **The `<resolved docs dir>` ruling** correctly distinguishes removing one *source* of a resolution from removing the resolution itself, and declines to overreach into twenty lines. The contrast with `aif-architecture` — where the path genuinely has no surviving resolution source and so does settle on the literal — is drawn accurately for both files.
- **Task 4a and the Modes 2/3 scope widening** are both defects the spec's `## Change` list does not name, correctly pulled in on principled grounds (self-contradiction introduced by this diff; the spec's own verification otherwise unsatisfiable, since a scratch project routes to Mode 3).
- **Scope discipline held twice** — the `Bash(ln *)` gap deferred to 19.2 with a matching contract line already drafted, and the `orchestrator/docs/configuration.md` residue recorded for the sibling repo without acting on it.

## Deferred observations

- Affects: unknown (pre-existing, `src/skills/aif/references/rules-generation.md` L11) — the file cites `.ai-factory/specs/41-aif-rules-counter-default-filter.md` as the home of its composition-model reasoning, but no such file exists under `.ai-factory/specs/` or `.ai-factory/notes/` (verified by `find`). Task 7 correctly orders everything outside its four named edits byte-identical, so this is out of scope here, and the citation is a doc-tree edge that has already rotted independently of this task. It wants its own contract line — either repoint it at the surviving artifact or drop the parenthetical.
- Affects: `orchestrator/.ai-factory/` — as the plan itself records at its close, `orchestrator/docs/configuration.md:87` disambiguates the orchestrator's own overlay against `.ai-factory/config.yaml`; once this task retires that artifact the sentence disambiguates against nothing. Correctly excluded from this task by the spec's scope guard; noted so the sibling-repo follow-up is not lost.

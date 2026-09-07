## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/23-29-1-command-pin-gaps-join-the-task-to-the-code-it-lands-in.md`
**Task spec:** `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`
**Files targeted:** 1 (`src/commands/command-pin-gaps.md`)
**Risk Level:** 🟢 Low — the one finding of plan-review-2 is closed at the exact line and with the exact quotes it asked for; every anchor in the plan re-verifies fresh against the files, and all eighteen of the spec's § Verification checks plus all nine of its § Guards reach a step.

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`) — PASS. `:22` places slash commands under `src/commands/` as a category parallel to `src/skills/`, so an in-place rewrite of a command is structurally correct and needs no move. § "Composition: mechanism vs policy" (`:30-39`) is untouched: nothing is extracted, no engine appears, and `loads:` keeps its single existing `roadmap-engine` edge — right under the ≥2-callers extraction rule, since naming an owner is a finding, not a delegation, and the plan states that reasoning itself ("naming an owner needs no load").
- **Rules** — WARN (unchanged from reviews 1 and 2, non-blocking). `.ai-factory/RULES.md` and `.ai-factory/skill-context/` are both absent, so there are no project `aif-review` overrides to apply. The binding discipline is the root and global CLAUDE.md: protocol tokens held byte-exact (the plan pins `Repair:`, `owner: <skill>`, `## Blocking decisions`, `N closed from source · M blocking · K owned elsewhere`, `value|meaning →`, `Governing spec:`, `Phase note:` as literals), the direction docs → roadmap → code carried as required body content, and the reserved-words contract — `src/commands/` is product we author, so it binds, and the plan's vocabulary (task, task spec, contract line, leaf, walk, phase, governing spec, owner) conforms.
- **Roadmap** — PASS. `.ai-factory/roadmaps/trickster77777.md:134` carries 29.1 under Phase 29's header at `:130`, tagged `Spec: .ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`; it is the first `[ ]` line and sits directly above `---STOP---`. Every clause of the contract line has a step behind it: the walk to the leaf, the two-sided orchestrator emulation, the finding definition, the implementability question, blast-radius as third class, resolve-in-place vs. explicit blocker, the four owners wielded by none, the phase-header-pointer exclusion, `allowed-tools`/`loads` unchanged, no path outside this repo. `git status --porcelain` shows only untracked `.ai-factory/` artifacts and `git diff HEAD -- src/ active/ docs/ CLAUDE.md` is empty, so the plan's negative diff check is satisfiable exactly as written.
- **Governing spec** — PASS. Phase 29's header names no `Governing spec:` and no `Phase note:`; the governing surface is `docs/sakshi-harness/skill-cycle.md` § "Пины — `command-pin-gaps`" (header `:37`, body `:39` and `:41`), which `CLAUDE.md:33` names the authoritative home of the cycle's order. Read fresh, every clause of `:39`/`:41` has a step behind it, and the plan treats the file as read-never-edited, as the spec requires.

### The plan-review-2 finding is closed, verified at the leaf

The Grounding step no longer attributes anything to § "Grounding claims" that does not live there. It now reads: "Do **not** carry into the file either of two rules that live elsewhere in that same always-loaded file: § 'Documentation style' `:27` … and § 'Project CLAUDE.md authoring' `:31` … Neither sits in § 'Grounding claims' — verify each at the line named before relying on it."

Both anchors and both quotes re-verify byte-for-byte against `src/global/CLAUDE.md` read fresh:
- `:27` — "**Docs form a walkable tree.** … A fact's second home is always a link to its first, never a copy." The plan quotes the sentence with "to its first" restored, which review-2 asked for.
- `:31` — "**One home per fact.** Anything stated in two places will drift." Under § "Project CLAUDE.md authoring" (`:29`), exactly as the fix directed.
- § "Grounding claims" spans `:3-17` and contains neither rule, so the plan's "Neither sits in § 'Grounding claims'" is true as stated, and the added "verify each at the line named before relying on it" makes the exclusion self-checking rather than trusted.

The step still scopes what *does* carry — "those two facts, and only those two" (docs → roadmap → code at `:7`; the walk to the leaf at `:11`/`:13`) — and both are genuinely resident in every session, so the produced command performs no fetch. The counter-default exception these exclusions protect is mandated positively in the "State the two ends" step and fenced by a matched pair of checks (rule present ≥ 1, inverse rule absent 0).

### Anchors re-verified fresh

`src/commands/command-pin-gaps.md` is 26 lines: `:1-12` frontmatter (`description: >-` at `:2`, folded text `:3-8`, `argument-hint: "[path | scan]"` at `:9`, `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill` at `:10`, `loads: roadmap-engine` at `:11`), `:14-15` the engine load, `:17` target resolution, `:19` the premise, `:21` value holes, `:23` meaning holes, `:25` scan mode carrying `value|meaning →`, `:26` the default report `N closed from source · M blocking`. The file is tracked and clean at `HEAD` (`5348761`), and `git show HEAD:src/commands/command-pin-gaps.md` returns `:10`/`:11` identical to the working tree, so the byte-exact capture the plan orders resolves. `CLAUDE.md:33` is the Skill-cycle row; `CLAUDE.md:115` is the `≤ 1024 chars` comment on `description:`. `skill-cycle.md:37/39/41` are the Пины header and its two paragraphs. `active/commands/command-pin-gaps.md` is an existing symlink into `src/commands/`, so an in-place rewrite leaves the active set intact and adds no symlink — the scope check's assumption holds.

The tool-grant reasoning stays grounded in the actual grant: `:10` gives the `Grep` tool and `Bash(rg *)` and no bare `grep`, so "the repair verb is `Grep` or `rg`, never bare `grep`" is fixed by the file, not by taste; `Read`, `Glob`, `Bash(git *)` cover the walk, `Edit` covers the in-place close, and nothing the plan asks for needs `Write`, `Agent` or `AskUserQuestion`.

The reconnaissance holds: `grep -rn command-pin-gaps docs/ CLAUDE.md src/ README.md` returns `docs/skill-description-field.md:13`, `docs/sakshi-harness/skill-graph.md:49`, `CLAUDE.md:33` and the governing `docs/sakshi-harness/skill-cycle.md:37,39,74`. None quotes the command's `description:`, and no file under `src/` invokes it, so the one-file diff boundary is real.

### Coverage

All eighteen § Verification checks of the spec appear in the plan's Verification step, including the ones easiest to lose — `Repair:` exactly 3, `value|meaning →` at 0, `Governing spec:`/`Phase note:` each 0, `orchestrator/` at 0, the `wc -m` measurement of the `description:` block, both halves of the emulation plus "no plan and no verdict", the oversized-sweep finding owned by `roadmap-decompose`, and the normalized-read method itself with "No count is evidence until taken this way". Two checks beyond the spec's list guard the counter-default exception on both sides. All nine § Guards reach a step: the identity guard and the no-verdict rule (Body step 1), no new authority and the four owners (owner step), no path outside the repo (Verification), no frontmatter growth (Frontmatter step), the repeated-paragraph exception (two-ends step), the comparative calibration (owner step), `Grep`/`rg` over bare `grep` and the single register with the third paragraph in `:21`/`:23`'s shape (class step), Phase 28 / 28.1 / spec 102 untouched (Verification).

### Critical Issues

None.

### Issues

None.

### Positive Notes

- **The exclusion is now falsifiable.** "Verify each at the line named before relying on it" converts a claim about a file into an instruction to check it — the only shape that survives the global CLAUDE.md being edited again before this task runs, and the one the plan's own grounding discipline demands of a reference it names.
- **The counter-default exception is fenced on both sides.** Requiring the "a repeated paragraph is not a finding" rule present *and* any collapse-or-route rule absent is what makes it survive a full-body rewrite whose surrounding reasoning ("follow named references to the leaf") pushes the other way; a presence-only check would pass a file that states the exception once and contradicts it in the meaning-hole paragraph.
- **The frontmatter is pinned negatively as well as positively** — the byte-exact capture ordered up front with `git show HEAD:…`, "whatever line numbers they end up on". That is precisely the failure a full-body rewrite invites, since every line number the plan is written against shifts under it.
- **The emulation is fenced three ways** — "it produces no plan and no verdict", "carry no orchestrator prompt into the file and name none", and separately that no pass/fail verdict displaces the finding list. Three distinct routes by which an orchestrator emulation could metastasize into an orchestrator, each closed, each with a check behind it.
- **The walk has a unit and a stopping rule** — one behavior the task claims, each ending at a `file:line` landing or becoming a finding, descending into referenced code "only as far as that behavior's landing requires, never past the question". Bounding by the question rather than by depth is the only bound that holds on a file whose references fan out.
- **Blast-radius is specified against its own degenerate output.** "A `Grep`/`rg` sweep whose **enumeration** goes into the task spec — never a sentence saying something may need updating" names the failure mode directly, and the oversized-sweep escape routes to `roadmap-decompose` with an explicit ban on filing it under `## Blocking decisions`, keeping that heading reserved for genuine product decisions as `skill-cycle.md:41` requires.
- **Authority is denied verb by verb** — "does not decompose, does not write documentation, does not author tests, and loads none of the four" — one verb per named owner, so no owner reads as an invitation to act.
- **Verification names the wrong instrument and refuses it.** "Never a line-oriented `grep`", `**` normalized out of both sides before any quoted span is compared, and "No count is evidence until taken this way" — correct for a file whose required spans (`N closed from source · M blocking · K owned elsewhere`, the bolded class names) straddle bold markers and line breaks once a rewrite reflows them.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` / a later task in Phase 29 — the command's default target, kept unchanged at `:17` by both the spec (its container is explicitly out of the cut) and the plan, is *all* open `- [ ]` tasks of the roadmap in play above `---STOP---`. Before this task each of those got a text-only interrogation; after it, each gets a walk into the code to the leaf plus a two-sided orchestrator emulation. Neither the spec nor `skill-cycle.md:39` says what the command does when that default fires over a dozen open tasks — walk all of them, walk the first, or ask. The plan cannot address it without contradicting "the container does not change", so it belongs upstream: either the container gains a scale rule, or the doc states that the whole-roadmap default is a scan-mode-only shape.
- Affects: `docs/skill-description-field.md` and `docs/sakshi-harness/skill-cycle.md:74` (both outside this task's one-file diff boundary, the latter additionally read-never-edited by this task) — `skill-description-field.md:13` paraphrases the command's zone as "close the places an implementer would guess at", and the cycle diagram at `skill-cycle.md:74` labels it `закрыть места угадывания`. After 29.1 the command also routes what it may not close to a named owner and raises fundamental conflicts as blockers, so "close" narrows the described zone in both places. Neither passage is a specification of the command's behavior — one illustrates action-without-invocation, the other is a one-line position label in the cycle diagram whose own prose at `:39`/`:41` already carries the full behavior — so nothing breaks; whoever next touches either doc may want the zone stated as close-or-route.

PLAN_REVIEW_PASS

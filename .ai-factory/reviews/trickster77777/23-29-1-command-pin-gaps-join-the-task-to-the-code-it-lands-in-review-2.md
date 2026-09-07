# Re-review: 29.1 — command-pin-gaps: join the task to the code it lands in

**Previous review:** `.ai-factory/reviews/trickster77777/23-29-1-command-pin-gaps-join-the-task-to-the-code-it-lands-in-review-1.md`
**Plan:** `.ai-factory/plans/trickster77777/23-29-1-command-pin-gaps-join-the-task-to-the-code-it-lands-in.md`
**Task spec:** `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`
**Diff:** still 1 file, +29 / −10 — `src/commands/command-pin-gaps.md`. Everything else in `git status` is this run's own `.ai-factory/` artifacts.
**Risk:** 🟢 Low — the single finding is closed; the fix touched only the frontmatter block it was about.

## Verdicts on review-1 findings

### 1. The `description:` narrowed the advertised target to a task alone — **Fixed**

Re-read fresh. Current `src/commands/command-pin-gaps.md:3-6`:

```
  Scan a plan, task, phase, or task spec for where the implementing agent
  would have to guess: read the task, its task spec, and the code it lands
  in, walking the task's transformation into the code along named
  references to the leaf, then reason the way the orchestrator would plan
```

The advertised target now covers every kind `:20` actually accepts. `:20` is unchanged and reads "the file(s) in `$ARGUMENTS`, if given — else the scope under discussion in chat (a named task, phase, or task spec) — else all open `- [ ]` tasks of the roadmap in play" — so frontmatter and body agree: **plan** and **phase** are back, and **task spec** covers both `.ai-factory/specs/` and the older `.ai-factory/notes/` location the contract line's `Spec:` tag resolves. The word **guess** is restored too, matching `docs/skill-description-field.md:13`'s phrasing of this command's zone ("close the places an implementer would guess at") and the likeliest word in a user's own request — the second half of the finding.

Nothing was lost buying that back. The mandated content is intact in the same block: the walk phrase "walking the task's transformation into the code" (`:5`), all three class names — value holes `:7`, meaning holes `:8`, blast-radius holes `:9` — the routed-to-its-owner clause `:8-9`, "Closes what it can in place" and the `scan` mode sentence `:10-11`. The block folds to **622 characters** (was 593), inside the 1024 cap at `CLAUDE.md:115`, measured with a real YAML parse rather than by eye. The former "to find where holding this task alone would force invention" is gone, but its content is carried by the new opening clause and, unchanged, by `:26` in the body.

**The fix is surgical.** Diffed against the exact blob reviewed last pass (`3d19644`): the only difference is lines 3–11, the description block. The body was not re-touched, so nothing verified in review-1 could have regressed silently — and it was all re-verified below regardless.

## Full re-verification — all spec checks hold

Counts taken against a whitespace-normalized read with `**` stripped from both sides, per the spec's § Verification; no line-oriented `grep` was used for any quoted span.

- `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill` (`:13`) and `loads: roadmap-engine` (`:14`) — **byte-identical** to `git show HEAD:src/commands/command-pin-gaps.md`. `Write` / `AskUserQuestion` / `Agent` in the grant → 0 each. `argument-hint: "[path | scan]"` keeps its required quoting; the frontmatter parses as valid YAML.
- `orchestrator/` → 0; `Governing spec:` → 0; `Phase note:` → 0. `:28` states the pointer exclusion positively and names the owning tier.
- `Repair:` → exactly 3 (`:36`, `:38`, `:40`), each paragraph in `:21`/`:23`'s original shape — bold name, definition, `Repair:`. No second register: the file is prose end to end.
- `value|meaning →` → 0; `value|meaning|blast-radius →` → 1 (`:44`); `owner: <skill>` → 2 (`:32`, `:44`); `N closed from source · M blocking · K owned elsewhere` → 1 (`:45`); `owned elsewhere` → 1.
- `docs → roadmap → code` → 1 (`:28`); both halves of the emulation plus "no plan and no verdict" → present (`:24`); both ends of the hole → present (`:30`); all three end→class mappings in one sentence shape → present (`:32`).
- The counter-default guard survives at `:34` ("A task spec that repeats a paragraph from a document instead of linking to it is not a finding"), and its inverse is absent — `:38`'s routing clause is scoped to "behavior no document states", a different object.
- Owners named, wielded by none: `roadmap-decompose` ×4, `roadmap-decompose-skeleton` ×1, `aif-docs` ×2, `test-philosophy` ×1; the only invocation instruction in the file is `:17`'s pre-existing `roadmap-engine` load; `loads:` gained nothing.
- Scope: file still at `src/commands/command-pin-gaps.md`; `active/commands/command-pin-gaps.md` remains a symlink into it; `git status --porcelain -- src/skills active/` is empty; `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly the one file; Phase 28, task 28.1, spec 102 and the roadmap are untouched.

## New issues

None.

## Deferred observations

Carried forward from review-1 and plan-review-3, all still open and all outside this task's one-file cut.

- Affects: `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` / a later task in Phase 29 — a blast-radius blocker has no stated destination. `:40` says a fundamental conflict, or code that does not come apart, "is raised as an explicit blocker", and bars `## Blocking decisions` only for the oversized sweep; `:38` pins that heading as the home of a genuine product decision, which the spec reserves it for. So the one blocker kind this task introduces has no named place to land, and the membership of `M blocking` in `:45`'s report is left to the reader. The file is faithful to the spec — the spec states both halves and never joins them — so the repair belongs upstream: either the heading widens to hold both blocker kinds, or the blast-radius blocker gets its own home.
- Affects: `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` / a later task in Phase 29 — the default target at `:20`, deliberately out of this cut, is *all* open `- [ ]` tasks above `---STOP---`. Each now gets a walk into the code to the leaf plus a two-sided orchestrator emulation instead of a text-only interrogation, and nothing says what happens when that default fires over a dozen open tasks: walk all, walk the first, or ask. Either the container gains a scale rule, or the doc states that the whole-roadmap default is a scan-mode-only shape.
- Affects: `docs/skill-description-field.md:13` and `docs/sakshi-harness/skill-cycle.md:74` (the latter read-never-edited by this task's spec) — both paraphrase the command's zone as closing the places an implementer would guess at (`закрыть места угадывания`). After this change the command also routes what it may not close to a named owner and raises conflicts as blockers, so "close" under-describes it. Neither passage specifies behavior, so nothing breaks; whoever next edits either doc may want the zone stated as close-or-route.

REVIEW_PASS

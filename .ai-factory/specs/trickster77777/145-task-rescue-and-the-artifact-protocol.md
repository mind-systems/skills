# Phase 51 — task-rescue and the artifact protocol close their own gaps

What still diverges, all of it in `src/skills/task-rescue/SKILL.md` and `src/skills/orchestrator-artifacts/SKILL.md`:

- **The sidecar path.** `task-rescue` locates the sidecar "per `orchestrator-artifacts` § 1" where it reads it, in Step 1, and at the two write sites of Step 5 ("Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`") it uses the flat path. That is wrong for any named roadmap, whose sidecar sits under a subdirectory named by the roadmap's stem, so one file holds two answers to where the sidecar is and the rollback write can land where nothing reads it. Both write sites want the locator the read site uses.
- **The body's size.** The body of `task-rescue` is far over the line bound in this repository's CLAUDE.md, § "Key constraints" and `.ai-factory/ARCHITECTURE.md`, § "Skill anatomy". The remedy is structural, moving the depth procedures or the `## What NOT to do` inventory into `references/`, and a widening edit cannot carry it.
- **The marker grammar.** `orchestrator-artifacts` § "6. Status-marker grammar" attributes the markers to "the resolution session" alone, while `task-rescue` § "Step 5.6 — Pin disposed observations" writes `[routed → <spec path>]` and `[dismissed]` too. That step has no branch for `[fixed]`, which § 6 defines, for the case where rescue's own repair closes a deferred observation directly.
- **The path shorthand.** `task-rescue`'s closed-set table cites its mirror source as `orchestrator/resume.py`, while the family-root path is `orchestrator/orchestrator/resume.py`; `orchestrator-artifacts` § "7. Mirrors-the-orchestrator invariant" lists `resume.py` in the same short form.
- **Hand-composing.** `task-rescue` § "Step 5.7 — Write the durable report" delegates to `note` without the explicit ban that `command-handoff`, Step 2, carries for the same delegation ("do not mine, number, slug, `mkdir`, or `Write` yourself"). The step is unambiguous as written; this is a hardening note for when the two callers are next touched together.

Nothing it had named has been settled.

Nothing under `docs/` is written by this phase's own note.

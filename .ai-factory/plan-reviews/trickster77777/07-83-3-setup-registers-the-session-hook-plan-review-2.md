## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/07-83-3-setup-registers-the-session-hook.md`
**Task:** 83.3 — setup registers the session hook (named roadmap `.ai-factory/roadmaps/trickster77777.md`, Phase 83)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The plan heading matches the open line 83.3. It sits right at the seam, directly after 83.1 and 83.2, which are both `[x]` and committed (`ac5c862`, `c2438d6`). The contract line, the task spec `.ai-factory/specs/trickster77777/0235-setup-registers-the-session-hook.md` and the plan agree on scope: one paragraph plus one JSON entry in `README.md` § "Setup — activating the package (one-time, per machine)".
- **Governing spec — OK.** Phase 83 names `docs/sakshi-harness/sakshi-harness.md`. That doc already says the slug line is printed by `roadmap-engine`'s `user-slug.sh` and registered by a `SessionStart` hook, and it points to README § Setup. This task supplies that pointer's target, so the governing spec needs no edit.
- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` says nothing about setup or hooks, so there is no boundary conflict.
- **Rules — WARN (non-blocking).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.

### Ground truth re-checked for this pass

- **Verbatim text.** I extracted the plan's paragraph and the spec's quoted paragraph and diffed them: they are identical. That includes the trailing space in `` `The user's slug: ` `` and the straight apostrophes. I also extracted the plan's JSON block and the spec's JSON block: they are identical byte for byte, and the result parses with `python3 -I -m json.tool`.
- **README target.** `README.md` § Setup is as the spec's "What is true now" describes it: a four-row table, then the "For each surface, detect its current state" list ending with the `skills/` `commands/` `agents/` merge bullet, then "The whole flow is idempotent…", then the `active/` paragraph. The plan's insertion point exists as described. A column-0 paragraph after a blank line closes the nested list cleanly.
- **The hook command.** I decoded the `command` value and ran it with `sh -c`. In this repo it prints `The user's slug: trickster77777` and exits 0. I then used a temporary `HOME` holding `.claude/skills/roadmap-engine` → `src/skills/roadmap-engine`, with `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1`, from a directory outside any repo. There the script on its own exits `2`, and the hook command prints nothing and exits 0. This is exactly the negative path the plan's verification now prescribes.
- **Working tree.** Only the plan, its sidecar and the earlier plan-review are untracked. `README.md` is unmodified, so the plan starts from the state it describes.

### Resolution of review 1

1. **The negative check now tests the "no slug" path.** The verification task uses the symlinked temporary `HOME` with git config isolated. It first confirms that the script exits `2`, so the case is "no slug derivable" and not "script missing". The empty-`HOME` run is kept only as an optional extra and is explicitly not a substitute. Resolved.
2. **The `CLAUDE.md` rationale is corrected.** The Context section now credits `sakshi-harness.md` with describing the hook. It says `CLAUDE.md` does not mention the hook, must not gain it, and stays unedited because its description of the four `~/.claude` links remains true, as the spec says. I confirmed that `CLAUDE.md` has no `hook`/`settings.json` mention. Resolved.

### Critical Issues

None.

### Issues

None.

### Positive Notes

- The plan states its placement assumption openly and gives reasons that fit the section's structure: the closing idempotence/reversibility sentence still closes the whole flow.
- The copy discipline is at byte level: trailing space, apostrophes, JSON escapes, two-space indentation and a ` ```json ` fence. That is right for text the spec pins verbatim.
- The scope boundary is explicit and matches the spec's "What breaks on contact". The sakshi root `README.md` is left to its own repository, `CLAUDE.md` and the governing spec stay unedited, and the real `~/.claude` is never touched.
- The verification covers each silent-failure surface of a text-only change: the JSON parses, the command behaves correctly in both slug states, the paragraph diffs against the spec, the spec's sweep runs, and `git diff --stat` confirms the scope.

PLAN_REVIEW_PASS

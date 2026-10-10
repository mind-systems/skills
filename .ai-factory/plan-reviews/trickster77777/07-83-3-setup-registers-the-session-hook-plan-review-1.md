## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/07-83-3-setup-registers-the-session-hook.md`
**Task:** 83.3 — setup registers the session hook (named roadmap `.ai-factory/roadmaps/trickster77777.md`, Phase 83)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The plan heading matches the open line 83.3 in `.ai-factory/roadmaps/trickster77777.md`, which sits right at the seam after 83.1 and 83.2 (both `[x]`). The contract line, the task spec `.ai-factory/specs/trickster77777/0235-setup-registers-the-session-hook.md` and the plan all agree on scope: one paragraph plus one JSON entry in `README.md` § "Setup — activating the package (one-time, per machine)".
- **Governing spec — OK.** Phase 83 names `docs/sakshi-harness/sakshi-harness.md`. That doc already says the slug line comes from `user-slug.sh` and that a `SessionStart` hook registers it at activation, with a link to README § Setup. This task supplies the target of that link. No edit to the governing spec is needed.
- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` says nothing about setup or hooks, so there is no boundary conflict.
- **Rules — WARN (non-blocking).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.
- **Dependency ground truth — OK.** `src/skills/roadmap-engine/scripts/user-slug.sh` exists and is executable. It prints the bare slug and exits `2` when there is none, as the spec says. `~/.claude/skills/roadmap-engine` resolves to `src/skills/roadmap-engine` on this machine.

### What was verified

- **Placement.** The plan puts the new text after the last per-surface bullet (README line 27, the `skills/` `commands/` `agents/` merge bullet) and before "The whole flow is idempotent…". The spec does not pin a position, and the plan says so and gives its reasons. This placement is sound: a column-0 paragraph after a blank line ends the nested list, and the idempotence/reversibility sentence still closes the whole flow.
- **Verbatim text.** The plan copies the spec's paragraph and JSON block character for character. That includes the trailing space in `` `The user's slug: ` `` and the JSON escapes `\"` and `\\n`.
- **The hook command.** I decoded the `command` string and ran it with `sh -c`:
  - In this repo it prints `The user's slug: trickster77777` and exits 0.
  - With a temporary `HOME` that holds a `.claude/skills/roadmap-engine` symlink, plus `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1`, outside any repo: the script on its own exits `2` with its stderr notice, and the hook command prints nothing and exits 0.
  
  So the pinned entry does what the spec says.
- **Scope.** Only `README.md` changes. The sakshi root `README.md` is correctly left to its own repository, as the spec's "What breaks on contact" says. The spec's sweep is carried into the verification task.

### Critical Issues

None.

### Issues

1. **The "no slug" check exercises the wrong path** (task "Verify the inserted text and run the spec's sweep", first bullet).
   The plan's negative case runs the command with `HOME` pointed at an *empty* directory. In that setup `~/.claude/skills/roadmap-engine/scripts/user-slug.sh` does not exist. The `$(…)` fails because the command is not found (status 127), not because the script exits `2`. The output is still empty with exit 0, so the check passes, but it never tests the spec's actual claim: "prints nothing, exiting zero, when the script yields no slug".
   The plan offers the symlinked temporary `HOME` only for the positive case. Use it for the negative case too: a temporary `HOME` holding `.claude/skills/roadmap-engine` → `<repo>/src/skills/roadmap-engine`, with `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1`, run from a working directory outside any repo. Then confirm two things: the script on its own exits `2`, and the hook command prints nothing and exits `0`. You can keep the empty-`HOME` run as an extra case (script missing), but it must not be the only negative check.

2. **The Context section gets `CLAUDE.md` wrong.**
   The plan says "`CLAUDE.md` and `docs/sakshi-harness/sakshi-harness.md` already describe the hook and its README pointer, so they stay unedited." `CLAUDE.md` does not mention the hook, `SessionStart`, `settings.json` or the slug line at all. Its only slug mention is `.ai-factory/architects/<user-slug>/`. Only `sakshi-harness.md` describes the hook and links to README § Setup.
   The conclusion is still right: `CLAUDE.md` stays unedited. The reason is the one the spec gives: it "describes the `~/.claude` links of the four surfaces and stays true". The wrong reason matters because an implementer who checks it will find no hook in `CLAUDE.md` and may decide to add one, which is outside this task's scope.
   Fix: change the sentence so `sakshi-harness.md` is credited with the hook description, and `CLAUDE.md` stays unedited because its description of the four `~/.claude` links remains true.

### Positive Notes

- The plan states its placement assumption openly instead of guessing silently, and the reasoning matches the section's structure.
- The plan has a byte-level copy discipline: trailing space, straight apostrophes, JSON escapes, two-space indentation, and a ` ```json ` fence. That is right for a pinned-verbatim spec.
- "Do not modify the real `~/.claude`" is stated explicitly, and the plan keeps documenting the walkthrough separate from performing it.
- The verification parses the JSON block (`python3 -I -m json.tool`) and diffs the paragraph against the spec. Both are good checks for a change made entirely of pinned text.

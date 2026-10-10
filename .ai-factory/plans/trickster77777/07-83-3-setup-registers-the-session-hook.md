# Plan: 83.3 — setup registers the session hook

## Context
`README.md`, § "Setup — activating the package (one-time, per machine)", walks the agent through four `~/.claude` surfaces. All of them are symlinks into `active/`, so no session starts holding the user's slug. This task adds the paragraph and the `SessionStart` hook entry pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0235-setup-registers-the-session-hook.md`, § "What must be true after". Together they describe a further surface that is not a symlink: a hook in `~/.claude/settings.json`. It runs `~/.claude/skills/roadmap-engine/scripts/user-slug.sh` (added in 83.1), prints `The user's slug: <slug>`, and prints nothing while exiting zero when the script yields no slug.

Scope boundary: only `README.md` in this repository changes. Per the spec, "The rest of the section stands": the table, the per-surface state bullets, the idempotence/reversibility sentence and the `active/` paragraph stay word for word. The sakshi root `README.md` ("to activate the ~/.claude symlinks", "(the `~/.claude` symlinks)") is in a separate repository and is changed there, as the spec says; it is not part of this task. `docs/sakshi-harness/sakshi-harness.md`, the phase's governing spec, already describes the hook and links to README § Setup, so it stays unedited; this task supplies that link's target. `CLAUDE.md` does not mention the hook and must not gain it: it stays unedited because its description of the four `~/.claude` links remains true, as the spec says. The task writes nothing to the real `~/.claude/settings.json`. It documents the walkthrough and does not perform it.

Placement assumption: the spec pins the text but not where it goes inside the section. The paragraph goes immediately after the per-surface bullet list (which ends with the `skills/` `commands/` `agents/` merge bullet) and before "The whole flow is idempotent (a second run is all-skips) and reversible …". That way the closing sentence still closes the whole flow, the hook surface included. The hook is idempotent too, because the paragraph says to skip it when an entry already runs the script.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The setup section

- [x] **Insert the hook paragraph and its JSON entry into § Setup**
  Files: `README.md`
  In § "Setup — activating the package (one-time, per machine)", insert a new paragraph after the last bullet of the "For each surface, detect its current state" list and before the paragraph that starts `The whole flow is idempotent`. Keep one blank line on each side, as the section's other blocks have. The paragraph is the spec's text, verbatim and on one line, because the section's existing paragraphs are not hard-wrapped:

  ```
  A further surface is not a symlink: a `SessionStart` hook in `~/.claude/settings.json` whose command prints `The user's slug: ` followed by the output of `~/.claude/skills/roadmap-engine/scripts/user-slug.sh`, so that each session starts holding the user's slug, and prints nothing, exiting zero, when the script yields no slug. Walk the user through it like the others. Read their `settings.json` first. If a `SessionStart` entry already runs that script, skip it. If the file is absent, or holds other settings, show the entry below merged into what they keep, preserving every existing key and any other `SessionStart` entries, and write it only on their word. If they decline, skip the surface.
  ```

  Keep the trailing space inside the backtick span `` `The user's slug: ` ``, and use straight apostrophes as in the spec.

  Directly after it, separated by one blank line, add the fenced block exactly as the spec pins it, with a ` ```json ` opening fence and a ` ``` ` closing fence:

  ```json
  {
    "hooks": {
      "SessionStart": [
        {
          "hooks": [
            {
              "type": "command",
              "command": "s=$(~/.claude/skills/roadmap-engine/scripts/user-slug.sh 2>/dev/null) && printf \"The user's slug: %s\\n\" \"$s\" || true"
            }
          ]
        }
      ]
    }
  }
  ```

  Copy the `command` string byte for byte: the JSON escapes `\"` and `\\n` stay as written, and so do `2>/dev/null`, `&&` and `|| true`. Use two-space indentation, as in the spec. Do not touch any other line in the section. "Four surfaces under `~/.claude`" stays as it is, because the new paragraph names itself "A further surface".

### Contact check

- [x] **Verify the inserted text and run the spec's sweep** (depends on Insert the hook paragraph)
  Files: none (read-only)
  - Extract the JSON block from `README.md` and confirm it parses, for example by piping the fenced lines to `python3 -I -m json.tool`. Take the parsed `command` value and run it through `sh -c` in each case below. Do not modify the real `~/.claude`.
    - **Positive case:** run in this repo. It prints `The user's slug: <slug>` and exits 0. If `~/.claude/skills/roadmap-engine` does not resolve on the machine, use the temporary `HOME` from the negative case, run from this repo.
    - **Negative case (the script yields no slug):** create a temporary `HOME` that holds a `.claude/skills/roadmap-engine` symlink to `<repo>/src/skills/roadmap-engine`. Set `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1`, and use a working directory outside any git repository. First confirm the script on its own, `$HOME/.claude/skills/roadmap-engine/scripts/user-slug.sh`, exits `2`; this proves the path under test is "no slug derivable" and not "script missing". Then confirm the hook command prints nothing on stdout and exits `0`.
    - **Optional extra (script missing):** with `HOME` pointed at an empty directory, the hook command also prints nothing and exits `0`. This is supplementary only and never stands in for the negative case.
  - Diff the paragraph against the spec's quoted text and confirm the words match exactly.
  - Run the spec's sweep, `grep -n "symlink" README.md`. It should return only the section's own symlink flow, which the new paragraph extends, and the lines on `active/` and on adding a skill. None of these needs an edit.
  - `git diff --stat` shows only `README.md` changed.

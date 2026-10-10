# 83.3 — setup registers the session hook

## What is true now

`README.md`, § "Setup — activating the package (one-time, per machine)", is addressed to the agent on a fresh checkout, says "do not run this silently — walk them through it one surface at a time and let them choose per surface", and lists "Four surfaces under `~/.claude`, each with a target in `active/`": `CLAUDE.md`, `skills/`, `commands/`, `agents/`, all symlinks. Each is detected (`readlink`/`test`) and is absent, already ours, or the user's own, which they replace, keep or merge. The section closes the flow with "The whole flow is idempotent (a second run is all-skips) and reversible".

`~/.claude/settings.json` is a regular file the user keeps, not a link into this repository, and no repository of the family holds it. `~/.claude/skills/roadmap-engine` resolves to `src/skills/roadmap-engine` through the `skills/` surface. As 83.1 leaves it, `scripts/user-slug.sh` sits in that directory, prints the bare slug as one line, and exits with status `2` when no slug is derivable; a `SessionStart` hook that exits `2` shows its standard error to the user as a hook error notice in every session.

## What must be true after

In `README.md`, § "Setup — activating the package", a paragraph on the hook reads:

"A further surface is not a symlink: a `SessionStart` hook in `~/.claude/settings.json` whose command prints `The user's slug: ` followed by the output of `~/.claude/skills/roadmap-engine/scripts/user-slug.sh`, so that each session starts holding the user's slug, and prints nothing, exiting zero, when the script yields no slug. Walk the user through it like the others. Read their `settings.json` first. If a `SessionStart` entry already runs that script, skip it. If the file is absent, or holds other settings, show the entry below merged into what they keep, preserving every existing key and any other `SessionStart` entries, and write it only on their word. If they decline, skip the surface."

followed directly by the entry:

````
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
````

The rest of the section stands.

## What breaks on contact

The hook's path resolves through the `skills/` surface, or through `roadmap-engine` linked into a merged `skills/` directory; a user who keeps their own `skills/` and links none of ours has no such file at that path.

**Rule:** a text breaks on this change if it describes setup as only the `~/.claude` symlinks.

**Sweep:**
```
grep -n "symlink" README.md
grep -n "symlink" ../README.md
```

**Finding.** In `README.md` the search returns the section's own symlink flow, which this paragraph extends, and the lines on `active/` and on adding a skill, which stay true. In the sakshi root `README.md` it returns the Setup prompt's "to activate the ~/.claude symlinks" and the closing sentence's "(the `~/.claude` symlinks)", which are in a separate repository and are changed there. `CLAUDE.md` describes the `~/.claude` links of the four surfaces and stays true.

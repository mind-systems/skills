# Plan: 83.4 — the slug script's header names no caller

## Context
The header comment of `src/skills/roadmap-engine/scripts/user-slug.sh` describes the derivation as "the way the pipeline does". The orchestrator now runs this script and derives nothing itself, so that phrase points back at the script. This task replaces the two header lines that carry the phrase with the after-text pinned in the task spec `.ai-factory/specs/trickster77777/0245-the-slug-scripts-header-names-no-caller.md`, § "What must be true after".

Scope boundary: only the two header comment lines change. The shebang, the `# user-slug.sh — …` line, the `# Exit 0 = …` line and the whole script body stay byte-identical. The spec's sweep (§ "What breaks on contact") was re-run: `pipeline does` and `hyphen-collapsed` match only this header. The `local-part` mentions in `docs/reserved-words.md` and `docs/philosophy/multiuser-roadmaps.md` name no caller, so they stay as they are. The orchestrator's caller (`orchestrator/orchestrator/main.py`) lives in a separate repository and is not touched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The script header

- [x] **Replace the caller phrase in the header comment**
  Files: `src/skills/roadmap-engine/scripts/user-slug.sh`
  Replace these two consecutive header lines, which currently follow the `# user-slug.sh — print the current user's slug, bare, on one line.` line:

  ```
  # Derives the slug the way the pipeline does: the lowercased, hyphen-collapsed
  # local-part of git user.email, falling back to git user.name.
  ```

  with exactly these two lines, as the spec pins them (same `# ` prefix and wrap):

  ```
  # Derives the slug: the lowercased, hyphen-collapsed local-part of git
  # user.email, falling back to git user.name.
  ```

  Leave every other line of the file unchanged, and keep the file's executable bit. To check: `git diff` shows exactly two removed and two added comment lines. `bash -n src/skills/roadmap-engine/scripts/user-slug.sh` passes. Running the script in this repo prints the same slug as before. `grep -rn "pipeline does" src docs CLAUDE.md` returns nothing.

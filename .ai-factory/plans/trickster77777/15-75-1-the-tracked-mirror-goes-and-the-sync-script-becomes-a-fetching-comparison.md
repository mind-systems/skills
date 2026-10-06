# Plan: 75.1 — the tracked mirror goes and the sync script becomes a fetching comparison

## Context
Remove the tracked mirror `upstream/ai-factory/` and the `aif-skill-generator` symlink into it, git-ignore the local clones of the sources we follow, and replace `scripts/sync-upstream.sh` with `scripts/compare-sources.sh` — a script that reads each `upstream/*.md`, clones or fetches the source beside its file, prints what moved since the newest `Last seen:` commit, diffs our counterparts, and writes nothing tracked. The spec (`.ai-factory/specs/trickster77777/0212-upstream-is-a-list-of-sources-and-the-mirror-and-the-generator-go.md`) is the authority: its § "What must be true after" fixes the order and pins the `.gitignore` lines and the full script text verbatim.

Ground truth checked at planning time: `upstream/ai-factory/` has 174 files, all tracked, nothing untracked or ignored inside it; `active/skills/aif-skill-generator` is a tracked symlink to `../../upstream/ai-factory/aif-skill-generator`; `scripts/sync-upstream.sh` is mode 755; `CLAUDE.md` (repository tree and § "Sources We Follow"), `README.md` and `.ai-factory/ARCHITECTURE.md` already describe the end state and need no edit. The three tracked files `upstream/ai-factory.md`, `upstream/spec-kit.md`, `upstream/paperclip.md` stay untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Remove the mirror and the generator

- [x] **Delete the tracked mirror and the generator symlink**
  Files: `upstream/ai-factory/` (whole directory), `active/skills/aif-skill-generator`
  Run `git rm -r upstream/ai-factory` and `git rm active/skills/aif-skill-generator`. Afterwards `upstream/ai-factory/` must not exist on disk, and `upstream/ai-factory.md`, `upstream/spec-kit.md`, `upstream/paperclip.md` must still be present and unchanged (`git ls-files upstream` lists exactly those three). This step comes first because the clone of `lee-to/ai-factory` lands at the same path, `upstream/ai-factory/`. `~/.claude/skills/aif-skill-generator` dangling afterwards is intended — do not touch anything under `~/.claude`.

### Ignore the clones

- [x] **Add the clone pattern to `.gitignore`** (depends on Delete the tracked mirror and the generator symlink)
  Files: `.gitignore`
  Append after the last entry (`**/.trash/`), separated by one blank line as the existing entries are, exactly these two lines from the spec:
  ```
  # Local clones of the sources we follow — fetched, never committed
  upstream/*/
  ```
  The em dash is a literal `—`. Change nothing else in the file. Verify `git check-ignore upstream/ai-factory/x` matches and `git check-ignore upstream/ai-factory.md` does not.

### Replace the sync script

- [x] **Rename and rewrite the script as `scripts/compare-sources.sh`** (depends on Add the clone pattern to `.gitignore`)
  Files: `scripts/sync-upstream.sh` → `scripts/compare-sources.sh`
  Rename with `git mv scripts/sync-upstream.sh scripts/compare-sources.sh` so the executable mode (755) is kept, then replace the file's entire content with the script text pinned verbatim in the spec's § "What must be true after", step 3 (from `#!/usr/bin/env bash` through the final `done`). Copy it byte for byte from the spec — no added comments, no reformatting, no extra checks, trailing newline at end. Confirm `ls -l scripts/compare-sources.sh` still shows `x` bits and `bash -n scripts/compare-sources.sh` parses. Do not run the script as part of the implementation: it clones three remote repositories into `upstream/`; the spec records that the text was already exercised.

### Blast-radius check

- [x] **Run the spec's sweep and confirm the expected reach** (depends on Rename and rewrite the script as `scripts/compare-sources.sh`)
  Files: none changed (read-only check)
  From the repository root run the two searches from the spec's § "What breaks on contact":
  `grep -rnE "sync-upstream|aif-skill-generator|security-scan|rsync|source-checks" . ../orchestrator --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=.ai-factory --exclude-dir=upstream` must return nothing.
  `grep -rnE "upstream/" . ../orchestrator --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=upstream` must reach outside `.ai-factory/` only `CLAUDE.md` (tree and § "Sources We Follow"), `.gitignore` and `scripts/compare-sources.sh`, plus `.ai-factory/ARCHITECTURE.md`'s zones paragraph. Hits in `.ai-factory/` history (handoffs, closed specs, plans, reviews, rescue reports) are a record of their time and are not edited. If any other live text names the mirror, the sync script or the generator, stop and report it rather than editing outside this task's file boundary.

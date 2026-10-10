# Plan: 83.1 — the user's slug is derived by a script

## Context
The user's slug is derived only in prose today, in `roadmap-engine`'s **Slug derivation** paragraph, and every agent carries it out for itself. The orchestrator derives it in code, `_derive_identity_slug` + `_git_config_value` in `orchestrator/orchestrator/main.py`. This task adds `src/skills/roadmap-engine/scripts/user-slug.sh`, which derives the slug exactly as that code does and prints it bare on one line. The contract is the task spec `.ai-factory/specs/trickster77777/0233-the-users-slug-is-derived-by-a-script.md`, § "What must be true after".

Scope boundary: the engine's **Slug derivation** paragraph is NOT edited here. Task 83.2 rewrites it, and the spec defers to it ("the engine's paragraph being as 83.2 leaves it"). The `SessionStart` hook belongs to 83.3. Wiring the orchestrator to the script belongs to the orchestrator's liaison. This task delivers the script plus a read-only contact sweep.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The script

- [x] **Create `user-slug.sh`, mirroring the orchestrator's derivation**
  Files: `src/skills/roadmap-engine/scripts/user-slug.sh` (new; the `scripts/` directory is new too)
  Follow the shape of `src/skills/observe-logs/scripts/query-loki.sh`: `#!/usr/bin/env bash` shebang, a short header comment saying what it prints, `set -euo pipefail`, executable bit set (`chmod +x`, mode like `-rwxr-xr-x`). It must stay compatible with bash 3.2 (macOS), so no `${var,,}` and no associative arrays. Behaviour, matched step for step to `orchestrator/orchestrator/main.py`:
  - **Reading identity.** Run `git config user.email` and `git config user.name` in the current working directory, with no `--global`, so a repository-local identity wins as git resolves it. As in `_git_config_value`, a non-zero exit from `git config` (key unset, or any other git failure) or an empty value counts as "unset". Capture the value so that the non-zero exit does not trip `set -e` (e.g. `email="$(git config user.email 2>/dev/null)" || email=""`).
  - **Slugify** (one function, used for both values, the equivalent of `_slugify`): lowercase, replace every run of characters outside `a-z0-9` with a single `-`, then strip leading and trailing `-`. Do the collapse with `tr -cs`, not `sed`. `sed` works line by line, so an embedded newline would survive the collapse, and git does return multi-line values. `tr` treats newline as an ordinary byte. Run every stage under `LC_ALL=C` so the result does not depend on the locale:
    `printf '%s' "$1" | LC_ALL=C tr 'A-Z' 'a-z' | LC_ALL=C tr -cs 'a-z0-9' '-' | LC_ALL=C sed -E 's/^-+//; s/-+$//'`
    The trailing `sed` only trims the edges; after the `tr` stages its input contains no newline. Each byte of a multibyte character falls outside `a-z0-9`, so a non-ASCII run collapses to one hyphen, which matches Python for practically every identity. The exceptions are a few code points that Python's Unicode `.lower()` maps into ASCII, such as KELVIN SIGN U+212A → `k`. A byte-wise `tr` cannot reproduce these. They do not occur in real git identities, and no handling is required.
  - **Order.** If the email is set, slugify the text before the first `@` (`${email%%@*}`). If that gives a non-empty slug, use it. Otherwise, if the name is set, slugify the whole name and use it if non-empty. Otherwise there is no slug.
  - **Success:** print exactly the bare slug plus one newline to stdout (`printf '%s\n' "$slug"`), print nothing else to stdout or stderr, and exit `0`. Example: `john.doe@example.com` → `john-doe`.
  - **No slug:** print nothing to stdout, print one line to stderr saying why (neither `user.email` nor `user.name` yields a slug in this repository; set one of them), and exit `2`.
  - **Exit `2` is reserved** for "no slug derivable". Any other failure must exit with a different code. In particular, check `command -v git` up front, and if git is missing, print a stderr message and exit `1`. Under `set -e`, unexpected failures exit with their own status, which is never `2` in practice for `tr`/`sed`. Do not add other code paths that use `2`.
  - **Comments** describe behaviour only. Do not mention the orchestrator's file, the roadmap, a phase/task number, or any `.ai-factory/` path (global rule: comments never cite the plan layer). One line may say that the script derives the slug the way the pipeline does, without a path.

### Contact check

- [x] **Run the script against fixture identities, then run the spec sweep** (depends on Create `user-slug.sh`)
  Files: none (read-only checks; temporary repos go under a `mktemp -d` directory and are deleted afterwards. No test file is added to the repo.)
  - In a throwaway `git init` repo, run the script with `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null` (or `GIT_CONFIG_NOSYSTEM=1` and `HOME` pointed at the temp directory) so the developer's global identity does not leak in. Set the local identity with `git config user.email/user.name` and confirm:
    - `john.doe@example.com` → `john-doe`, exit 0, exactly one line.
    - `--John..Doe--@x` → `john-doe` (collapse and trim).
    - email `...@x` with name `Jane Q. Public` → `jane-q-public` (the email's slug is empty, so the name is used).
    - no email, name `Ann` → `ann`.
    - no email, name `$'Ann\nLee'` (embedded newline, set with `git config user.name "$(printf 'Ann\nLee')"`) → `ann-lee`, exactly one line on stdout (`| wc -l` gives `1`).
    - neither set → empty stdout, a non-empty stderr line, exit `2`.
    - a local identity that overrides a global one (set `GIT_CONFIG_GLOBAL` to a temp file holding a different email) → the local one wins.
  - Confirm `ls -l src/skills/roadmap-engine/scripts/user-slug.sh` shows the executable bit, and that `bash -n` on the script passes.
  - Run the spec's sweep from the repo root: `grep -rn "local-part" src docs CLAUDE.md`, `grep -rn "slugified" src docs CLAUDE.md`, `grep -n "scripts/" CLAUDE.md`. Expected per the spec's § "What breaks on contact": the only hits stating the derivation as an agent rule are in `src/skills/roadmap-engine/SKILL.md` § "Named roadmaps" (the **Slug derivation** paragraph), which 83.2 rewrites and which is left untouched here. The `docs/reserved-words.md` slug entry, the `docs/philosophy/multiuser-roadmaps.md` lines, and the `CLAUDE.md` `scripts/` mentions stay true and are not edited. If any other hit states the derivation as a rule for an agent, stop and report it instead of editing outside this task's boundary.

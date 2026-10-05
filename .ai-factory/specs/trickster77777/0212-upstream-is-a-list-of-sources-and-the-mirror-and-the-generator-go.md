# 75.1 — upstream holds one file per source, and the tracked mirror and the generator go

## What is true now

`upstream/ai-factory/` is tracked in this repository: a mirror of `lee-to/ai-factory`'s `skills/` that `scripts/sync-upstream.sh` overwrites with `rsync -a --delete`, so every refresh is a diff of other people's files in this repository's tree, and the orchestrator's task commit takes the whole tree. It is not a git repository, so nothing in it can be fetched. `active/skills/aif-skill-generator` is a symlink into the mirror, the one upstream skill in the working set; the user writes his own skills and has no use for it. The script's comments name "aif-docs, aif-plan, and roadmap-outline (vs upstream aif-roadmap)" as the skills to diff by hand. Nothing records when a source was last compared or what was seen.

Beside the mirror, `upstream/` already holds one tracked file per source we follow, `ai-factory.md`, `spec-kit.md` and `paperclip.md`. Each opens with its `URL:` line and a `Counterparts:` line (the skills of ours that share an origin with it, or `none`), says why we follow it, and keeps that source's dated check entries, newest last, each with a `Last seen:` line naming the commit seen. `.gitignore` has no entry for the clones; its entries run as a comment line naming the reason, then the pattern, for example "# Trash left behind by tooling, anywhere in the tree" above `**/.trash/`.

`CLAUDE.md`, `README.md` and `.ai-factory/ARCHITECTURE.md` already describe the end state: two zones, `src/` and `active/`; the sources we follow recorded in `upstream/`, one file each, with git-ignored clones beside them as `upstream/<repo-name>/`; and `scripts/compare-sources.sh` as the comparison, which reads those files and writes nothing tracked. No other live text under `src/` or `docs/` names the mirror, the sync script or the generator.

## What must be true after

The task makes its changes in this order, which matters because the clone of `lee-to/ai-factory` lands at the path the old mirror occupies, `upstream/ai-factory/`:

1. The tracked mirror is removed from the index and the tree: `git rm -r upstream/ai-factory`. The tracked `upstream/*.md` files stay. `active/skills/aif-skill-generator` is deleted with the mirror.
2. `.gitignore` gains, after its last entry and in its own style, two lines:

~~~~
# Local clones of the sources we follow — fetched, never committed
upstream/*/
~~~~

3. `scripts/sync-upstream.sh` is renamed to `scripts/compare-sources.sh`, because it no longer syncs anything, and keeps its executable mode. Its whole text is:

~~~~
#!/usr/bin/env bash
# Compare our skills with the sources we follow. Each source is one file in upstream/,
# read here: a `URL:` line, a `Counterparts:` line (the skills of ours that share an
# origin with it, or none) and dated entries, newest last, each with a `Last seen:` line
# naming the commit we saw. The file is written by hand by whoever reads a check, never
# by this script. Its clone sits beside it as upstream/<repo-name>/, which git ignores:
# cloned on first use, fetched after, so only new history comes down. For each source
# the head and its commit subjects since the last seen commit are printed, and our
# counterparts are diffed against theirs. Nothing tracked is written. Our copy is
# authoritative; changes worth taking are ported by hand.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLONES="$REPO_ROOT/upstream"

for file in "$CLONES"/*.md; do
  [ -e "$file" ] || continue
  url="$(sed -n 's/^URL: *//p' "$file" | head -1)"
  counterparts="$(sed -n 's/^Counterparts: *//p' "$file" | head -1)"
  seen="$(sed -n 's/^Last seen: *`\([^`]*\)`.*/\1/p' "$file" | tail -1)"
  if [ -z "$url" ]; then
    echo "$file has no URL: line" >&2
    continue
  fi
  clone="$CLONES/$(basename "$url")"

  if [ -d "$clone/.git" ]; then
    git -C "$clone" fetch --quiet origin
    git -C "$clone" checkout --quiet --force --detach origin/HEAD
  elif [ -e "$clone" ]; then
    echo "$clone exists and is not a git clone; remove it and run again" >&2
    exit 1
  else
    # Full history without file contents: the baseline stays reachable, and only the
    # files checked out are fetched.
    git clone --quiet --filter=blob:none "$url" "$clone"
  fi
  echo "== $url ($(git -C "$clone" log -1 --format='%h %ad' --date=short))"

  if [ -z "$seen" ]; then
    echo "no baseline recorded for this source"
  elif git -C "$clone" cat-file -e "$seen^{commit}" 2>/dev/null; then
    echo "commits since $seen:"
    git -C "$clone" log --format='%h %ad %s' --date=short "$seen..HEAD"
  else
    echo "baseline $seen is not in this source's history"
  fi

  for skill in ${counterparts//,/ }; do
    if [ "$skill" != none ]; then
      echo "-- $skill"
      diff -rq "$REPO_ROOT/src/skills/$skill" "$clone/skills/$skill" || true
    fi
  done
done
~~~~

The script holds no list of sources: a source is a file in `upstream/`. A file with no `URL:` line is reported on stderr and skipped; `Counterparts: none` runs no diff. If an old non-git `upstream/ai-factory/` is still present on a first run, the script stops before touching it: it prints "<path> exists and is not a git clone; remove it and run again" on stderr and exits 1. Step 1 removes the directory, so this guard is for a machine that has the old mirror untracked on disk.

The files are written by hand by whoever reads a check, never by the script. The form the script reads is stated once, in its header: a `URL:` line, a `Counterparts:` line, and a `Last seen:` line, the newest read last in the file.

## What breaks on contact

**Rule:** a text breaks on this change if it names the tracked mirror, the sync script, `rsync`, the generator or a list of sources kept outside `upstream/`, or tells a reader to take a skill from `upstream/` as if it were ours.

**Sweep:**
```
grep -rnE "sync-upstream|aif-skill-generator|security-scan|rsync|source-checks" . ../orchestrator --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=.ai-factory --exclude-dir=upstream
grep -rnE "upstream/" . ../orchestrator --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=upstream
```
run from this repository's root.

**Finding.** Once the steps land, the first search reaches nothing: the old script is the only file it reaches today, and it is renamed and rewritten. The second reaches the sources directory where it is meant: `CLAUDE.md` in its repository tree and in § "Sources We Follow", `.ai-factory/ARCHITECTURE.md` in its zones paragraph, `.gitignore` and the new script. The `.ai-factory/` history of both repositories, handoffs, closed specs, plans, reviews and rescue reports, names the mirror, the generator and the earlier diary as a record of its time and is not edited. On this machine `~/.claude/skills/aif-skill-generator` resolves through `active/skills/`, so it dangles after the deletion and the skill leaves the loaded set, which is intended.

The script keeps no baseline of its own: it reads the newest `Last seen:` line of each source's file. A first run clones each source with `--filter=blob:none`, full history without file contents, and a later run only fetches and moves the clone to `origin/HEAD`, so only new history comes down. It writes nothing tracked: its writes are the ignored clones. Three states print a line and stop nothing: a file with no `Last seen:` line, a recorded commit missing from the source's history (a rewritten history, say), and no files in `upstream/` at all. The script text was run under macOS bash 3.2 from a throwaway copy with scratch source files against the three live sources: a first run cloned all three, a second run only fetched, a clone stepped back five commits was moved to the fetched head, an older recorded baseline listed the commits since it, a file with no `URL:` line was skipped with a message, and a non-git directory at a clone path stopped the run with the message above. An entry written in another form than the header states reads as no baseline, silently.

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

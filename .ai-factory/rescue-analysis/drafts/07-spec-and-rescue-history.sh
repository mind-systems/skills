#!/bin/bash
# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: for one task in a project repository, when its spec was created and changed (author
# date beside commit date), which commit carried its plan, plan-reviews and reviews, and which
# spec path its contract line named. Used to answer "was the spec rewritten by a rescue, and
# when was it written relative to the run".
#
# Usage: 07-spec-and-rescue-history.sh <repo> spec <spec-path>
#        07-spec-and-rescue-history.sh <repo> artifacts <task-key>      (key like 52-1)
#        07-spec-and-rescue-history.sh <repo> line <N.M>                 (roadmap path ROADMAP)
#
# Known defects and traps:
#  - Author date and commit date differ for amended "Roadmap update" commits. Print both; use
#    the transcript for when something was authored and the commit date for when it landed.
#  - Plan, plan-review and review files of a failed run are deleted by the rescue; the
#    artifacts search shows only what survived in a commit.
#  - A task key in a file name has dots turned into hyphens (52.1 -> 52-1).
#  - The contract line's Spec tag is read from the first commit that introduced the line; a
#    reworded line can name a different spec later.
set -u
REPO=$1; MODE=$2; ARG=${3:-}
ROADMAP=${ROADMAP:-.ai-factory/ROADMAP.md}
cd "$REPO" || exit 1
case "$MODE" in
  spec)
    git log --all --format='%h author=%ad commit=%cd %s' --date=format:'%m-%d %H:%M' --follow -- "$ARG" ;;
  artifacts)
    k=$ARG
    git log --all --format='%h %cd %s' --date=format:'%m-%d %H:%M' --name-only \
      -- ".ai-factory/plans/*/*$k-*" ".ai-factory/plans/*$k-*" ".ai-factory/plan-reviews/*/*$k-*" \
         ".ai-factory/plan-reviews/*$k-*" ".ai-factory/reviews/*/*$k-*" ".ai-factory/reviews/*$k-*" ;;
  line)
    git log --all --format='%h %ad %s' --date=format:'%m-%d %H:%M' -S"**$ARG —" -- "$ROADMAP"
    c=$(git log --all --format=%h -S"**$ARG —" -- "$ROADMAP" | tail -1)
    git show "$c:$ROADMAP" | grep -F "**$ARG —" | grep -o 'Spec: `[^`]*`' ;;
  *) echo "usage: $0 <repo> spec|artifacts|line <arg>"; exit 2 ;;
esac

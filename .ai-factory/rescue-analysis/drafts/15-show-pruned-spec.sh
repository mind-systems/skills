#!/bin/bash
# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: nothing; prints the first lines of a task spec that has since been pruned from the
# working tree, by finding the commit that added it and reading it there.
#
# Usage: 15-show-pruned-spec.sh <spec-number> [lines]    (run in the skills repository)
#
# Known defects and traps:
#  - The folder is fixed to .ai-factory/specs/trickster77777/; change it for another roadmap.
#  - The spec is shown as it was when ADDED, not as it stood at the landing commit; a rescue
#    may have rewritten it since. Use 07-spec-and-rescue-history.sh to see the later versions.
#  - The number is matched as a prefix of the file name ("-" after it), so 110 does not match 1100.
cd /Users/max/projects/sakshi/skills || exit 1
n=$1; lines=${2:-14}
f=$(git log --all --format= --name-only --diff-filter=A -- ".ai-factory/specs/trickster77777/*" | grep -E "specs/trickster77777/${n}-" | sort -u | head -1)
c=$(git log --all --format=%h --diff-filter=A -- "$f" | tail -1)
echo "######## $f (added $c $(git log -1 --format=%ad --date=format:%m-%d $c))"
git show "$c:$f" | head -$lines | cut -c1-1500

#!/bin/bash
# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: the history of one skill file -- every commit that touched it, what each diff
# changed, what else moved in the same commit, the neighbouring tasks of the same days,
# and what became of a phase. Meant to be read by a person; it prints, it decides nothing.
#
# Inputs: the skills repository (default below), the file under study, a task number N.M,
# a commit <c>, a phase number.
#
# Known defects and traps:
#  - `git log -S"**N.M --"` finds the first and last appearance of a contract line only,
#    and misses a line that was reworded in between.
#  - The roadmap file of a named roadmap is .ai-factory/roadmaps/<slug>.md; the default
#    roadmap is .ai-factory/ROADMAP.md. Use the one the history lived in.
#  - Dates print in the commit's own +06 zone. "Roadmap update" commits are amended, so the
#    author date (%ad) can be days older than the commit date (%cd).
#  - A subject like "N.M -- title" is the orchestrator's task commit; any other subject
#    (for instance "Roadmap update") may hold a task's change swept in with other work.
set -u
REPO=${REPO:-/Users/max/projects/sakshi/skills}
FILE=${FILE:-src/commands/command-pin-gaps.md}
ROADMAP=${ROADMAP:-.ai-factory/roadmaps/trickster77777.md}
cd "$REPO" || exit 1

history_list() {            # every commit of the file, newest first, following renames
  git log --follow --format='%h %ad %s' --date=format:'%Y-%m-%d %H:%M' -- "$FILE"
  git log --follow --name-status --format='%h' -- "$FILE" | grep -E "^[RAD]"
}
diff_of() {                 # $1 = commit: the changed lines of the file only
  git show "$1" -- "$FILE" | grep "^[+-]" | grep -v "^+++\|^---"
}
moved_with() {              # $1 = commit: other files in the same commit, minus orchestrator artifacts
  git show "$1" --name-only --format= | grep -vE "^\.ai-factory/(plans|plan-reviews|reviews|rescue)" | grep -v "^$"
}
contract_line() {           # $1 = N.M: the first version of a (possibly pruned) contract line
  git log --all --format='%h %ad %s' --date=format:'%m-%d %H:%M' -S"**$1 —" -- "$ROADMAP"
  c=$(git log --all --format=%h -S"**$1 —" -- "$ROADMAP" | tail -1)
  git show "$c:$ROADMAP" | grep -F "**$1 —"
}
neighbours() {              # $1 = since, $2 = until: what else was landing in the window
  git log --format='%h %ad %s' --date=format:'%m-%d %H:%M' --since="$1" --until="$2"
}
phase_fate() {              # $1 = phase number: when its header appeared and disappeared
  git log --all --format='%h %ad' --date=format:'%m-%d %H:%M' -S"### Phase $1 —" -- "$ROADMAP"
}

case "${1:-}" in
  list) history_list ;;
  diff) diff_of "$2" ;;
  moved) moved_with "$2" ;;
  line) contract_line "$2" ;;
  neighbours) neighbours "$2" "$3" ;;
  phase) phase_fate "$2" ;;
  *) echo "usage: $0 list | diff <c> | moved <c> | line <N.M> | neighbours <since> <until> | phase <N>"; exit 2 ;;
esac

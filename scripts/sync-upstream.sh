#!/usr/bin/env bash
# Refresh upstream/ai-factory/ — a pristine mirror of lee-to/ai-factory's skills/.
#
# The mirror is never hand-edited: every skill we modified lives in src/skills/,
# so this is an unconditional overwrite with no merge and no conflicts.
#
# After a refresh, reconcile our reworked skills by hand (opt-in): each skill that
# shares an origin with an upstream one (aif-docs, aif-plan, and roadmap-outline vs
# upstream aif-roadmap) can be diffed to spot upstream changes worth porting into
# our src/ copy. Our src/ copy is authoritative and is never auto-overwritten.
set -euo pipefail

UPSTREAM_URL="https://github.com/lee-to/ai-factory"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "Cloning $UPSTREAM_URL ..."
git clone --depth 1 "$UPSTREAM_URL" "$TMP_DIR/upstream" >/dev/null 2>&1

echo "Mirroring skills/ → upstream/ai-factory/ ..."
mkdir -p "$REPO_ROOT/upstream/ai-factory"
rsync -a --delete "$TMP_DIR/upstream/skills/" "$REPO_ROOT/upstream/ai-factory/"

echo "Done. $(find "$REPO_ROOT/upstream/ai-factory" -maxdepth 1 -type d | tail -n +2 | wc -l | tr -d ' ') skills mirrored."
echo "Reworked skills to diff if desired: aif-docs, aif-plan, roadmap-outline (vs upstream aif-roadmap)."

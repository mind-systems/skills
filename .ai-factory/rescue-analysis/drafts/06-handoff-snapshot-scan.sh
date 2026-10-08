#!/bin/bash
# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: which handoffs and architect snapshots mention a gap pass or a given task, and the
# date each file first landed in git. Before the architect folders existed, snapshots were
# handoffs, so both paths are scanned. Answers "what did the architect say about the pass when
# the task was written".
#
# Inputs: a repository (first argument, default tradeoxy_core), the paths below. For the broker
# repository add .ai-factory/notes to PATHS. Second argument: comma-separated task ids to look for.
#
# Known defects and traps:
#  - The date is the commit date at which the file was added, not when it was written; an amend
#    chain can move it by days. Read the file's own text for the writing date when it matters.
#  - A file added in a rename is missed by --diff-filter=A (only additions are listed).
#  - Patterns are English and Russian spellings of the command; a different phrasing is missed.
#  - Buffers are skipped on purpose (buffer.md, address.md); this scan must never read a buffer.
set -u
REPO=${1:-/Users/max/projects/tradeoxy/tradeoxy_core}
TASKS=${2:-52.1,53.1,55.8,63.1,64.3}
PATHS=${PATHS:-".ai-factory/handoffs .ai-factory/architects"}
cd "$REPO" || exit 1
OUT=${OUT:-/tmp/snaps.tsv}
git log --all --format='%H %cd' --date=format:'%m-%d %H:%M' --name-status --diff-filter=A -- $PATHS \
 | awk 'NF>=3 && length($1)==40 {c=$1; d=$2" "$3; next} $1=="A" && NF==2 {print c"\t"d"\t"$2}' > "$OUT"
TASKS="$TASKS" OUT="$OUT" python3 - <<'EOF_PY'
import subprocess, re, os
pat = re.compile(r'pin-gaps|pingaps|gap-clos|gap pass|gap-pass|gap scan|пингапс|пин-гапс', re.I)
tids = os.environ['TASKS'].split(',')
for line in open(os.environ['OUT']):
    c, d, p = line.rstrip('\n').split('\t')
    if 'buffer.md' in p or p.endswith('address.md') or 'architect-buffer' in p:
        continue
    t = subprocess.run(['git', 'show', f'{c}:{p}'], capture_output=True, text=True).stdout
    g = len(pat.findall(t))
    hits = [x for x in tids if x in t]
    if g or hits:
        print(d, p.split('/')[-1][:70], 'gapmentions=', g, 'tasks=', hits)
        for m in pat.finditer(t):
            s = max(0, m.start() - 220)
            e = min(len(t), m.end() + 260)
            print('   ...', t[s:e].replace('\n', ' '))
            break
EOF_PY

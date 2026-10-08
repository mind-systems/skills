# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since. The original was
# several separate snippets typed at a shell; this file joins them and is the least faithful of
# the set.
#
# Measures: per time window, the share of tasks whose plan review and code review passed in the
# first round, mean rounds, median files outside .ai-factory, tasks touching many files, how many
# had pinned after-text, and which were rescued; then the same split by pinned vs not, by files
# changed, by presence of a Verification/Guards section, and by whether the task touched the
# paired-loop files.
#
# Usage: python3 13-window-stats-skills.py <rows2.json>   (rows from 08, 09, 11 and 12 combined)
#
# Known defects and traps:
#  - RESCUE SET IS HAND-TYPED from rescue-report file names: 29.1, 30.1, 31.1, 32.1, 36.1, 58.2.
#    It is not read from the reports; check it against .ai-factory/rescue-reports/skills/.
#  - Rounds are those of the landed run only (see 08).
#  - Windows are hard-coded date cuts; the cuts fall in gaps where no task landed.
#  - "pinned" is pinned_chars >= 300, a judgment; "many files" is three or more.
#  - The paired-loop file list is a fixed set of paths of that period.
import json, statistics as st
from collections import defaultdict
import sys

rows = [x for x in json.load(open(sys.argv[1])) if x['pr'] > 0]
RESC = {'29.1', '30.1', '31.1', '32.1', '36.1', '58.2'}      # HAND-TYPED
PAIR = {'src/skills/agent-architect/SKILL.md', 'src/skills/agent-architect/templates/buffer-seed.md',
        'src/skills/architect-editor-engine/SKILL.md', 'src/agents/editor.md', 'src/skills/architect-pairing-engine/SKILL.md'}


def win(x):
    t = x['d']
    if t < '2026-09-05':
        return 'W0'
    if t < '2026-09-12':
        return 'W1'
    if t < '2026-09-25':
        return 'Wm'
    return 'W2'


g = defaultdict(list)
for x in rows:
    g[win(x)].append(x)


def line(lab, xs):
    if not xs:
        print(lab, 'none')
        return
    print(lab, 'n', len(xs), 'plan1st', sum(1 for x in xs if x['pr'] == 1), 'code1st', sum(1 for x in xs if x['rv'] == 1),
          'meanP %.2f meanC %.2f' % (st.mean(x['pr'] for x in xs), st.mean(x['rv'] for x in xs)),
          'files<=1', sum(1 for x in xs if len(x['out']) <= 1), 'files>=3', sum(1 for x in xs if len(x['out']) >= 3),
          'pinned', sum(1 for x in xs if x.get('pinned_chars', 0) >= 300),
          'rescued', [x['t'] for x in xs if x['t'] in RESC])


for k in sorted(g):
    line(k, g[k])
    line('  pinned', [x for x in g[k] if x.get('pinned_chars', 0) >= 300])
    line('  not pinned', [x for x in g[k] if x.get('pinned_chars', 0) < 300])
    line('  files<=1', [x for x in g[k] if len(x['out']) <= 1])
    line('  files>=2', [x for x in g[k] if len(x['out']) >= 2])
    line('  check section', [x for x in g[k] if x.get('check')])
    line('  no check section', [x for x in g[k] if not x.get('check')])
    line('  paired-loop files', [x for x in g[k] if any(f in PAIR for f in x['out'])])
    line('  other files', [x for x in g[k] if not any(f in PAIR for f in x['out'])])

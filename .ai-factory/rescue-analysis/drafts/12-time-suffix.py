# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: the run duration the orchestrator writes at the end of a done roadmap line
# ("[5m 33s]"), per task, read from the roadmap diff of the task's landing commit. Gives the
# run-time comparison between windows.
#
# Usage: python3 12-time-suffix.py <repo> <rows.json> <out.json>
# Inputs: rows from 08-task-rounds.py; the roadmap at .ai-factory/ROADMAP.md or
# .ai-factory/roadmaps/*.md.
#
# Known defects and traps:
#  - The suffix is a duration, not a clock time. It covers the run that landed, not a failed run.
#  - Present in the skills roadmap on every landed task; not looked for in core's, so no core
#    run-time comparison exists.
#  - A line whose suffix was pruned or never written gives None; the median is over the rest.
#  - Window labels in the original were hard-coded date cuts: before 09-05, before 09-12,
#    before 09-25, after. Change them to fit the question.
import json, subprocess, re, sys, statistics as st

repo, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
rows = [x for x in json.load(open(src)) if x['pr'] > 0]


def git(*a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True).stdout


def secs(s):
    m = re.search(r'\[(?:(\d+)h )?(?:(\d+)m )?(\d+)s\]', s)
    if not m:
        return None
    return int(m.group(1) or 0) * 3600 + int(m.group(2) or 0) * 60 + int(m.group(3))


for x in rows:
    d = git('show', '--format=', '-U0', x['h'], '--', '.ai-factory/ROADMAP.md', '.ai-factory/roadmaps')
    x['secs'] = None
    for l in d.split('\n'):
        if l.startswith('+') and '**' + x['t'] + ' ' in l:
            x['secs'] = secs(l)


def win(x):
    t = x['d']
    if t < '2026-09-05':
        return 'W0'
    if t < '2026-09-12':
        return 'W1'
    if t < '2026-09-25':
        return 'Wm'
    return 'W2'


from collections import defaultdict
g = defaultdict(list)
for x in rows:
    g[win(x)].append(x)
for k in sorted(g):
    v = [x['secs'] for x in g[k] if x['secs']]
    print(k, 'with suffix', len(v), 'of', len(g[k]), 'median %.0fs' % st.median(v) if v else '', 'max', max(v) if v else '')
json.dump(rows, open(dst, 'w'))

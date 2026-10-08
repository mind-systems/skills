# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: for the core repository, rounds, files outside .ai-factory and rescues grouped by
# stretch of the project (protocol build, alerts and replay, review-debt fixes, failure doors,
# hygiene, refactors, shared pool, dependency fixes, backtest engine), then by files changed
# (two or fewer, three to seven, eight or more).
#
# Usage: python3 14-window-stats-core.py <core-rows.json>
#
# Known defects and traps:
#  - RESCUE SET IS HAND-TYPED from rescue-report file names and is INCOMPLETE: it omits core
#    77.1 (report 0024). Core has no 77.x row in the data, so the tables are unaffected, but
#    the list is not a count of rescues. Rebuild it from .ai-factory/rescue-reports/tradeoxy_core.
#  - Rounds count the landed run only; a task rescued four times shows the rounds of the last.
#  - "files outside" includes tests and docs, so a retyping task shows a very large number.
#  - Stretch boundaries are my judgment of what the phases were; phase 39's early tasks are in
#    the 34-40 group by date, so a date-cut and a phase-cut overlap for 39.x.
#  - Rescue reports in the skills repo's folder start 2026-09-08; earlier core rescues have no report.
import json, statistics as st, sys

r = [x for x in json.load(open(sys.argv[1])) if x['pr'] > 0]
RESC = {'52.1', '53.1', '55.6', '55.7', '55.8', '55.9', '56.1', '61.2', '61.4', '59.6', '63.1', '64.3', '64.5',
        '67.4', '79.2', '79.3.2', '79.4', '39.6.2.2.1.1'}      # HAND-TYPED, incomplete (no 77.1)


def ph(x):
    return int(x['t'].split('.')[0])


groups = {
    'phases 1-10 (protocol and engine build)': lambda x: x['d'] < '2026-07-12',
    'phases 34-40 (alerts, replay, order axis; includes 39.x)': lambda x: '2026-07-12' < x['d'] < '2026-09-08',
    'phases 49-51 (review-debt fixes)': lambda x: ph(x) in (49, 50, 51) and x['d'] < '2026-09-17',
    'phases 52-53 (failure doors)': lambda x: ph(x) in (52, 53) and '2026-09-17' < x['d'] < '2026-09-20',
    'phases 54-55 (deferred-observation fixes, hygiene)': lambda x: ph(x) in (54, 55),
    'phases 56-60 (refactor, slots)': lambda x: ph(x) in (56, 57, 58, 59, 60) and x['d'] > '2026-09-24',
    'phases 61-62 (shared pool)': lambda x: ph(x) in (61, 62),
    'tail of 39.x and phases 63-76': lambda x: (x['t'].startswith('39.') and x['d'] > '2026-09-28') or ph(x) in (63, 64, 65, 67, 70, 72, 73, 74, 75, 76),
    'phase 79 (backtest engine)': lambda x: ph(x) == 79,
}
for k, f in groups.items():
    xs = [x for x in r if f(x)]
    if not xs:
        continue
    print(k, '\n   n', len(xs), 'plan1st', sum(1 for x in xs if x['pr'] == 1), 'code1st', sum(1 for x in xs if x['rv'] == 1),
          'meanP %.2f meanC %.2f' % (st.mean(x['pr'] for x in xs), st.mean(x['rv'] for x in xs)),
          'median files', st.median(len(x['out']) for x in xs), 'files>=8', sum(1 for x in xs if len(x['out']) >= 8),
          'pinned>=300', sum(1 for x in xs if x.get('pinned_chars', 0) >= 300),
          'rescued', [x['t'] for x in xs if x['t'] in RESC])
for lab, f in [('out<=2', lambda x: len(x['out']) <= 2), ('out 3-7', lambda x: 3 <= len(x['out']) <= 7), ('out>=8', lambda x: len(x['out']) >= 8)]:
    xs = [x for x in r if f(x)]
    print(lab, len(xs), 'plan1st', sum(1 for x in xs if x['pr'] == 1), 'meanP %.2f meanC %.2f' % (st.mean(x['pr'] for x in xs), st.mean(x['rv'] for x in xs)))
for lab, pre in [('39.x', '39.'), ('79.x', '79.')]:
    xs = [x for x in r if x['t'].startswith(pre)]
    print(lab, 'n', len(xs), 'plan1st', sum(1 for x in xs if x['pr'] == 1), 'code1st', sum(1 for x in xs if x['rv'] == 1))

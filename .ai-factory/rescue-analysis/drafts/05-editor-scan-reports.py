# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: which tasks an architect's editor reported a gap pass on, and when, by reading the
# task-notification user turns that carry the editor's report ("... `command-pin-gaps` scan,
# task `N.M` alone (spec `NNN`)"). The result is a list of (time, task, spec) lines.
#
# Usage: python3 05-editor-scan-reports.py <session.jsonl> <lo-iso> <hi-iso> [task ...]
# With task ids it prints only those tasks; without, every report in the window.
#
# Known defects and traps:
#  - Matches only reports phrased "command-pin-gaps` scan, task `N.M`" or "pass -- task `N.M`".
#    An editor that phrased its report differently is missed, and so is a pass whose report
#    never reached the transcript.
#  - The same notification is often present several times; the script dedupes on (time, text).
#  - Timestamps are UTC.
import json, sys, re

f, lo, hi = sys.argv[1:4]
targets = set(sys.argv[4:])
seen = set()
for line in open(f):
    try:
        o = json.loads(line)
    except Exception:
        continue
    ts = o.get('timestamp', '')
    if not (lo <= ts <= hi) or 'message' not in o or o.get('type') != 'user':
        continue
    c = o['message']['content']
    t = c if isinstance(c, str) else ''.join(b.get('text', '') for b in (c or []) if isinstance(b, dict))
    m = re.search(r'command-pin-gaps` scan, task `(\d+\.\d+)`[^\n]*', t) or re.search(r'pass — task `(\d+\.\d+)`[^\n]*', t)
    if m and (not targets or m.group(1) in targets):
        k = (ts, m.group(0)[:60])
        if k not in seen:
            seen.add(k)
            print(ts, m.group(0)[:130])

# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: the same spec lookup and shape fields as 08 and 09, for a rows file whose first
# run was cut short (core's, because the full run exceeded the shell time limit). It also sets
# "check": whether the spec has a heading matching Verification, Guards or Acceptance.
#
# Usage: python3 10-spec-only.py <repo> <rows.json>      (rewrites the JSON in place)
#
# Known defects and traps:
#  - It SKIPS any row that already has a "spec" key, so a row filled by an earlier partial run
#    never gets "check" from here; run 11-check-only.py afterwards. This is exactly what went
#    wrong in the session: the first listing showed no check sections until 11 was run.
#  - Roadmap path is fixed to .ai-factory/ROADMAP.md (core and broker use the default roadmap).
#  - Same threshold and template caveats as 09.
import json, subprocess, re, sys

repo, src = sys.argv[1], sys.argv[2]
rows = json.load(open(src))


def git(*a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True).stdout


for r in rows:
    if 'spec' in r:
        continue
    h = r['h']
    d = git('show', '--format=', '-U0', h, '--', '.ai-factory/ROADMAP.md')
    path = None
    for l in d.split('\n'):
        if l.startswith('+') and ('**' + r['t'] + ' ' in l):
            m = re.search(r'Spec: `([^`]+)`', l)
            if m:
                path = m.group(1)
    if not path:
        for l in d.split('\n'):
            if l.startswith('-') and '**' + r['t'] + ' ' in l:
                m = re.search(r'Spec: `([^`]+)`', l)
                if m:
                    path = m.group(1)
    r['spec'] = path
    if not path:
        continue
    t = git('show', f'{h}^:{path}') or git('show', f'{h}:{path}')
    r['speclen'] = len(t)
    m = re.search(r'^## (What must be true after|The change)\s*$(.*?)(?=^## |\Z)', t, re.M | re.S)
    sec = m.group(2) if m else ''
    r['sec'] = m.group(1) if m else None
    r['seclen'] = len(sec)
    r['pinned_chars'] = sum(len(x) for x in re.findall(r'"([^"\n]{60,})"', sec)) + sum(len(l) for l in sec.split('\n') if l.startswith('>'))
    hs = re.findall(r'^#{2,3} (.*)', t, re.M)
    r['check'] = any(re.search(r'Verification|Guards|Acceptance', x) for x in hs)
    r['heads'] = hs[:8]
    r['srcfiles'] = len(set(re.findall(r'`((?:src|docs|Sources|Tests|proto)/[A-Za-z0-9_./\-]+)`', t)))
json.dump(rows, open(src, 'w'))
print('done')

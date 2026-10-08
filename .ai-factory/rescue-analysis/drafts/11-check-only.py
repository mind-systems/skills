# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
# Smoke test: ran without error on a small recent window on 2026-10-09; the original measurements were not reproduced.
#
# Measures: whether each task's spec carries a checking apparatus, by heading: any heading
# matching Verification, Guards or Acceptance. Writes "check" and the first headings into the
# rows file. Used to compare rounds with and without such sections.
#
# Usage: python3 11-check-only.py <repo> <rows.json>      (rewrites the JSON in place)
#
# Known defects and traps:
#  - Heading names only. A spec that holds its checks under a different heading, or inside a
#    "Blast radius" or "What breaks on contact" section, is counted as having none.
#  - In core the sections stay present in most specs until the end of September, so the flag
#    does not separate its rounds; in the skills repo it is absent after 2026-09-24.
#  - Reads the spec at <commit>^ with fallback to <commit>.
import json, subprocess, re, sys

repo, src = sys.argv[1], sys.argv[2]
rows = json.load(open(src))


def git(*a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True).stdout


for r in rows:
    if not r.get('spec'):
        continue
    h = r['h']
    t = git('show', f'{h}^:{r["spec"]}') or git('show', f'{h}:{r["spec"]}')
    hs = re.findall(r'^#{2,3} (.*)', t, re.M)
    r['check'] = any(re.search(r'Verification|Guards|Acceptance', x) for x in hs)
    r['heads'] = hs[:8]
json.dump(rows, open(src, 'w'))

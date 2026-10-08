# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since. Written, run once,
# and not used in any result; kept because it was part of the record.
#
# Measures: how many times a spec says "verbatim", "word for word", "byte-exact", "reads in full",
# "reads:", "reads exactly" or "pinned"; and the first headings of the spec. An attempt to find
# specs that pin their after-text, superseded by the pinned_chars measure in 09-spec-shape.py.
#
# Usage: python3 18-verbatim-count.py <repo> <rows.json>      (rewrites the JSON in place)
#
# Known defects and traps:
#  - Counts a word anywhere in the spec, including in the prose about the task's own method, so
#    it over-reports. That is why the measure was replaced.
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
    r['verb'] = len(re.findall(r'verbatim|word for word|byte-exact|reads in full|reads:|reads exactly|pinned', t, re.I))
    r['heads'] = re.findall(r'^#{1,3} .*', t, re.M)[:8]
json.dump(rows, open(src, 'w'))

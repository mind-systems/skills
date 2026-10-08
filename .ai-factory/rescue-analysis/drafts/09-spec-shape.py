# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
# Smoke test: ran without error on a small recent window on 2026-10-09; the original measurements were not reproduced.
#
# Measures: for each row of 08-task-rounds.py's JSON, the shape of the spec the task landed
# from: which template it used (old: "The change"; new: "What must be true after"), the length
# of that section, and how much of it is pinned text (quoted passages of 60+ characters,
# blockquote lines, fenced blocks). "pinned_chars" is the number the analysis called pinned
# when it passed 300.
#
# Usage: python3 09-spec-shape.py <repo> <rows.json>      (rewrites the JSON in place)
#
# Known defects and traps:
#  - The 300-character threshold is a judgment, not a rule. An early version counted quotes of
#    the CURRENT text found in a "what is true now" section; this one looks only at the section
#    that says what must be true after. Sample specs by hand before trusting totals.
#  - A section that quotes the target text over a code fence counts the fence once (pinned_q) and
#    its characters not at all; fences are not added to pinned_chars.
#  - Specs without either heading get templ='old' and a zero-length section.
#  - Reads the spec at <commit>^ with fallback to <commit>, like 08.
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
    m = re.search(r'^## (What must be true after|The change)\s*$(.*?)(?=^## |\Z)', t, re.M | re.S)
    sec = m.group(2) if m else ''
    r['sec'] = m.group(1) if m else None
    r['seclen'] = len(sec)
    r['pinned_q'] = len(re.findall(r'"[^"\n]{60,}"', sec)) + len(re.findall(r'^>', sec, re.M)) + len(re.findall(r'^```', sec, re.M)) // 2
    r['pinned_chars'] = sum(len(x) for x in re.findall(r'"([^"\n]{60,})"', sec)) + sum(len(l) for l in sec.split('\n') if l.startswith('>'))
    r['templ'] = 'old' if (r['sec'] == 'The change' or not r['sec']) else 'new'
json.dump(rows, open(src, 'w'))

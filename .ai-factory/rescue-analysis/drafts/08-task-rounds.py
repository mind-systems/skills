# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since. The original was
# edited three times in place (tab escape in the format string, a bad --until argument removed,
# the spec-enrichment block appended); this file is the final form assembled from those edits.
# Smoke test: ran without error on a small recent window on 2026-10-09; the original measurements were not reproduced.
#
# Measures: for every task commit ("N.M — title") since a date: plan-review rounds, code-review
# rounds, files changed outside .ai-factory, and the spec's size and quoting. The orchestrator
# commits the whole tree, so a task's commit carries its plan, plan-reviews and reviews.
#
# Usage: python3 08-task-rounds.py <repo> <since-date> x <out.json>
# (the third argument is a placeholder that is no longer used.)
# Inputs: a git repository with .ai-factory/{plans,plan-reviews,reviews}; for the spec lookup,
# .ai-factory/ROADMAP.md or .ai-factory/roadmaps/<slug>.md.
#
# Known defects and traps:
#  - THE PASS FLAGS ARE UNPROVEN: ppass/rpass test only that the token PLAN_REVIEW_PASS or
#    REVIEW_PASS occurs somewhere in the last review file. They came out true for every task,
#    which suggests the token also occurs in text that is not a pass. Do not read them as outcomes.
#  - Rounds count only the run that landed. A rescue deletes the failed run's plan, reviews and
#    sidecar; the rescue report is the only account of that run.
#  - Only commits whose subject matches "N.M — title" are tasks. Subjects before the orchestrator
#    numbered them (skills repo: before 2026-09-03) are not found. Tasks done in chat have no
#    artifacts and show zero rounds.
#  - "out" counts every changed path outside .ai-factory, including tests and docs; a rename
#    reports its last path only. A mirror deletion or a purge shows as a very large number.
#  - The spec is found from a "**N.M " line in the landing commit's roadmap diff; a task whose
#    line was not touched in its landing commit has no spec (reported as None).
#  - The spec is read at <commit>^ (before the landing commit). If a rescue rewrote it earlier,
#    that is the version read; if the landing commit rewrote it, the old text is read.
#  - The slow part is the git calls per task; a long run exceeds a two-minute shell limit.
import subprocess, re, sys, json

repo = sys.argv[1]
since = sys.argv[2]
outfile = sys.argv[4] if len(sys.argv) > 4 else '/tmp/rows.json'


def git(*a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True).stdout


log = git('log', '--all', '--no-merges', '--format=%H%x09%cd%x09%s', '--date=format:%Y-%m-%d %H:%M', f'--since={since}')
rows = []
for l in log.strip().split('\n'):
    if not l:
        continue
    h, d, s = l.split('\t', 2)
    m = re.match(r'^(\d+(?:\.\d+)+)\s+—\s+(.*)', s)
    if not m:
        continue
    files = git('show', '--name-status', '--format=', '-M', h).strip().split('\n')
    pr = rv = pl = 0
    out = []
    pr_files = []
    rv_files = []
    for f in files:
        if not f:
            continue
        parts = f.split('\t')
        st = parts[0]
        p = parts[-1]
        if '.ai-factory/plan-reviews/' in p and st.startswith('A'):
            pr += 1
            pr_files.append(p)
        elif '.ai-factory/reviews/' in p and st.startswith('A'):
            rv += 1
            rv_files.append(p)
        elif '.ai-factory/plans/' in p and p.endswith('.md') and st.startswith('A'):
            pl += 1
        elif '.ai-factory/' in p:
            pass
        else:
            out.append(p)

    def final_pass(fs, tok):
        if not fs:
            return None
        fs = sorted(fs, key=lambda p: int(re.search(r'-(\d+)\.md$', p).group(1)) if re.search(r'-(\d+)\.md$', p) else 0)
        t = git('show', f'{h}:{fs[-1]}')
        return tok in t

    rows.append(dict(h=h[:7], d=d, t=m.group(1), title=m.group(2)[:60], pr=pr, rv=rv, plans=pl,
                     ppass=final_pass(pr_files, 'PLAN_REVIEW_PASS'), rpass=final_pass(rv_files, 'REVIEW_PASS'), out=out))
rows.sort(key=lambda r: r['d'])
json.dump(rows, open(outfile, 'w'))
print(len(rows))


# ---- spec enrichment (originally appended to the same script)
def spec_info(r):
    h = r['h']
    d = git('show', '--format=', '-U0', h, '--', '.ai-factory/ROADMAP.md', '.ai-factory/roadmaps')
    path = None
    for l in d.split('\n'):
        if l.startswith('+') and ('**' + r['t'] + ' ' in l or '**' + r['t'] + ' —' in l):
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
        return
    t = git('show', f'{h}^:{path}')
    if not t:
        t = git('show', f'{h}:{path}')
    r['speclen'] = len(t)
    r['bq'] = len(re.findall(r'^>', t, re.M))
    r['fence'] = len(re.findall(r'^```', t, re.M)) // 2
    r['srcfiles'] = len(set(re.findall(r'`((?:src|docs|Sources|Tests)/[A-Za-z0-9_./\-]+)`', t)))
    r['quotes'] = len(re.findall(r'"[^"\n]{100,}"', t)) + len(re.findall(r'“[^”\n]{100,}”', t))


for r in rows:
    spec_info(r)
json.dump(rows, open(outfile, 'w'))

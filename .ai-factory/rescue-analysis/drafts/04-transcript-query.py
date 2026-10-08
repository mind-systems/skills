# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: where a string (a task id, a spec number) occurs in the visible text of one session
# transcript between two timestamps, with 160 characters before and 240 after. Used to find
# what the architect and the editor said about a task on a given day.
#
# Usage: python3 04-transcript-query.py <session.jsonl> <needle> <lo-iso> <hi-iso> [max-hits]
# Inputs: a ~/.claude/projects/<folder>/<session-id>.jsonl file; lo/hi compare as strings, so
# give ISO prefixes in UTC (for example 2026-09-16T05:00).
#
# Known defects and traps:
#  - Only text blocks are read; tool results and thinking are not searched.
#  - One hit per text block (the first occurrence). The same message can be present several
#    times, so identical hits repeat; dedupe by eye or with `awk '!seen[substr($0,1,70)]++'`.
#  - Lines without a "message" key (queue operations, attachments) are skipped.
import json, sys, re

f, tid, lo, hi = sys.argv[1:5]
maxn = int(sys.argv[5]) if len(sys.argv) > 5 else 12
n = 0
for line in open(f):
    try:
        o = json.loads(line)
    except Exception:
        continue
    ts = o.get('timestamp', '')
    if not (lo <= ts <= hi):
        continue
    m = o.get('message', {})
    c = m.get('content')
    texts = []
    if isinstance(c, str):
        texts = [c]
    elif isinstance(c, list):
        for b in c:
            if b.get('type') == 'text':
                texts.append(b['text'])
    for t in texts:
        for mm in re.finditer(re.escape(tid), t):
            s = max(0, mm.start() - 160)
            e = min(len(t), mm.end() + 240)
            print(ts, o.get('type'), '|', t[s:e].replace('\n', ' '))
            n += 1
            break
        if n >= maxn:
            sys.exit()

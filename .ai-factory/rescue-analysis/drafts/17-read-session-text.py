# DRAFT. Written for this folder from the coordinator's description; NOT run by the hand that
# wrote it.
# Smoke test: ran without error on a small recent window on 2026-10-09; the original measurements were not reproduced.
#
# Measures: nothing. Prints the visible text blocks of the latest turns of a session transcript,
# so that an answer cut off by a classifier mid-sentence can be read back, and so that the end of
# an interviewed session can be checked.
#
# Usage: python3 17-read-session-text.py <session.jsonl> [N-latest-turns] [--roles assistant,user]
# Inputs: ~/.claude/projects/<folder>/<session-id>.jsonl
#
# Known defects and traps:
#  - Prints text blocks only: no thinking, no tool calls, no tool results. A tool-heavy turn may
#    print nothing.
#  - A turn is one JSON line with a "message"; consecutive lines of one assistant turn are shown
#    separately.
#  - Times are UTC.
import json, sys

f = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 6
roles = {'assistant', 'user'}
if '--roles' in sys.argv:
    roles = set(sys.argv[sys.argv.index('--roles') + 1].split(','))
turns = []
for line in open(f):
    try:
        o = json.loads(line)
    except Exception:
        continue
    if 'message' not in o or o.get('type') not in roles:
        continue
    c = o['message'].get('content')
    texts = [c] if isinstance(c, str) else [b.get('text', '') for b in (c or []) if isinstance(b, dict) and b.get('type') == 'text']
    t = '\n'.join(x for x in texts if x.strip())
    if t.strip():
        turns.append((o.get('timestamp', ''), o['type'], t))
for ts, role, t in turns[-n:]:
    print('-----', ts, role)
    print(t)

# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
#
# Measures: for every project folder under ~/.claude/projects, when a slash command was last
# used and how often, plus the invocations since a given date. Used to test the premise that
# a command "stopped being called" after a date. With --args it also prints each invocation's
# arguments (up to 420 characters), which is how the user's own words were collected.
#
# Inputs: ~/.claude/projects/*/*.jsonl. Arguments: --command <name> (default command-pin-gaps),
# --since <ISO date> (default 2026-09-29), --args.
#
# Known defects and traps:
#  - A line is counted only if it contains the literal "type":"user"; a transcript whose JSON is
#    spaced differently would be missed. The earlier per-folder scan (02) has no such filter.
#  - A session that only asks "which skills did I call" can contain the marker without a use;
#    one such core session on 2026-10-06 matched the first scan and was not a use.
#  - Timestamps are UTC, cut to the minute.
#  - Files under 500 bytes are skipped.
import json, glob, os, re, sys, collections

os.chdir(os.path.expanduser('~/.claude/projects'))
cmd = 'command-pin-gaps'
since = '2026-09-29'
if '--command' in sys.argv:
    cmd = sys.argv[sys.argv.index('--command') + 1]
if '--since' in sys.argv:
    since = sys.argv[sys.argv.index('--since') + 1]
show_args = '--args' in sys.argv
marker = '<command-name>/' + cmd
rows = []
for f in glob.glob('*/*.jsonl'):
    if os.path.getsize(f) < 500:
        continue
    if marker not in open(f, errors='ignore').read():
        continue
    for line in open(f, errors='ignore'):
        if marker in line and '"type":"user"' in line:
            try:
                o = json.loads(line)
            except Exception:
                continue
            c = o.get('message', {}).get('content')
            t = c if isinstance(c, str) else ''.join(b.get('text', '') for b in (c or []) if isinstance(b, dict))
            if marker in t:
                m = re.search(r'<command-args>(.*?)</command-args>', t, re.S)
                a = (m.group(1)[:420] if m else '(no args)').replace('\n', ' ')
                rows.append((o.get('timestamp', '')[:16], f.split('/')[0].replace('-Users-max-projects-', ''), a))
rows = sorted(set(rows))
by = collections.defaultdict(list)
for ts, p, a in rows:
    by[p].append(ts)
for p, l in by.items():
    print(p, len(l), 'first', l[0], 'last', l[-1])
print([r[:2] for r in rows if r[0] >= since])
if show_args:
    for ts, p, a in rows:
        print(p[:22], ts, a)

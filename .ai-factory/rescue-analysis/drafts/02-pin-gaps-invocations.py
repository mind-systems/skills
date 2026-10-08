# DRAFT. Reconstructed from a session record (2026-10-07), not re-run since.
# Smoke test: ran without error on a small recent window on 2026-10-09; the original measurements were not reproduced.
#
# Measures: when a user invoked a slash command, per session transcript, and with which
# arguments. First scan of the analysis; it was run for the core and broker folders.
#
# Inputs: folders under ~/.claude/projects (one per working directory, every non-alphanumeric
# character of the path turned into a hyphen). Pass the folder names as arguments, or the two
# defaults below. Optionally pass --command to look for another command name.
#
# Known defects and traps:
#  - Timestamps are UTC ("Z"); commit times elsewhere are +06.
#  - The same message appears several times in a session file; the script dedupes by (time, args).
#  - The marker also appears in a user line that merely talks about the command (the
#    command's own text is expanded into the user turn). Read the arguments, not the count.
#  - Only the architect's own session files are scanned; an editor sub-agent's transcript is a
#    different file and is not read.
#  - The arguments are cut at 200 characters here; a longer instruction needs a second look.
import json, glob, os, re, sys

os.chdir(os.path.expanduser('~/.claude/projects'))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
cmd = 'command-pin-gaps'
if '--command' in sys.argv:
    cmd = sys.argv[sys.argv.index('--command') + 1]
    args = [a for a in args if a != cmd]
dirs = args or ['-Users-max-projects-tradeoxy-tradeoxy-core', '-Users-max-projects-tradeoxy-tradeoxy-broker']
for d in dirs:
    print('==', d)
    for f in sorted(glob.glob(d + '/*.jsonl')):
        first = last = None
        hits = []
        with open(f) as fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                ts = o.get('timestamp')
                if ts:
                    first = first or ts
                    last = ts
                if '<command-name>/' + cmd in line:
                    m = re.search(r'<command-args>(.*?)</command-args>', line)
                    hits.append((ts, (m.group(1)[:200] if m else '')))
        if hits:
            print(os.path.basename(f), first, last)
            seen = set()
            for h in hits:
                if h not in seen:
                    print('   ', h)
                    seen.add(h)

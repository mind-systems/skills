#!/bin/bash
# DRAFT. Written for this folder from the coordinator's description of the 2026-10-08
# interview; NOT run by the hand that wrote it, and not re-run since by anyone recorded here.
#
# Measures: nothing. Asks a surviving planner session about what its own conversation SHOWS,
# read-only, with the planner's own model and effort.
#
# Usage: 16-interview.sh <session-id> <prompt-file> [project-dir]
# Inputs: a session id found in a rescue report's rewritten sidecar (planner session); the
# transcript is ~/.claude/projects/<folder>/<id>.jsonl; the prompt goes in on stdin.
#
# Known defects and traps:
#  - The prompt is read from stdin on purpose: a variadic flag such as --disallowedTools
#    swallows a trailing prompt argument.
#  - Tools are limited to read-only ones: Read, Grep, Glob. No edits, no shell.
#  - Ask about the record, never about inner reasoning. "Does this conversation show X; quote the
#    places" passes. "What you made of ...", "how you treated what you remembered", "go through
#    the findings and judge" are stopped by a safety classifier as reasoning extraction, sometimes
#    in the middle of an answer. A stopped answer is not lost: read it back with
#    17-read-session-text.py from the session's own .jsonl.
#  - Resuming appends to the same session file (unverified here): the interview's turns may sit at
#    the end of the transcript that is being studied. Do not count them as part of the run.
#  - --model and --effort are the planner's own; confirm them from the sidecar or the run's config.
#  - The working directory should be the project the session ran in; that is where the session is
#    looked up (unverified).
set -eu
ID=$1; PROMPT=$2; DIR=${3:-/Users/max/projects/tradeoxy/tradeoxy_core}
cd "$DIR"
claude -p --resume "$ID" --model opus --effort high --tools "Read,Grep,Glob" < "$PROMPT"

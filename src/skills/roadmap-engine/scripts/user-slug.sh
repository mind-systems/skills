#!/usr/bin/env bash
# user-slug.sh — print the current user's slug, bare, on one line.
# Derives the slug the way the pipeline does: the lowercased, hyphen-collapsed
# local-part of git user.email, falling back to git user.name.
# Exit 0 = slug printed; exit 2 = no slug derivable; any other code = failure.
set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "user-slug.sh: git is not installed" >&2
  exit 1
fi

slugify() {
  printf '%s' "$1" \
    | LC_ALL=C tr 'A-Z' 'a-z' \
    | LC_ALL=C tr -cs 'a-z0-9' '-' \
    | LC_ALL=C sed -E 's/^-+//; s/-+$//'
}

email="$(git config user.email 2>/dev/null)" || email=""
name="$(git config user.name 2>/dev/null)" || name=""

slug=""
if [ -n "$email" ]; then
  slug="$(slugify "${email%%@*}")"
fi
if [ -z "$slug" ] && [ -n "$name" ]; then
  slug="$(slugify "$name")"
fi

if [ -z "$slug" ]; then
  echo "user-slug.sh: neither user.email nor user.name yields a slug in this repository; set one of them" >&2
  exit 2
fi

printf '%s\n' "$slug"

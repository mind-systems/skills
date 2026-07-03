#!/usr/bin/env bash
# query-loki.sh — read-only Loki log slice tool
# Usage: query-loki.sh <subcommand> [args...]
# Subcommands: since-restart | trace | window
set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LOKI_URL="${OBS_LOKI_URL:-http://localhost:3100}"
LOKI_AUTH="${OBS_LOKI_AUTH:-}"
DEFAULT_LIMIT=200
PAGE_SIZE=5000        # Loki's default max_entries_limit_per_query; used by query_range_all
DEFAULT_WINDOW="1h"

# Auth args for curl, built once. Empty when OBS_LOKI_AUTH is unset — byte-identical
# behavior to no-auth. Never expand unguarded (bash 3.2 aborts on unbound-array
# expansion under `set -u`); use ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} at call-sites.
AUTH_ARGS=()
[[ -n "$LOKI_AUTH" ]] && AUTH_ARGS=(-H "Authorization: ${LOKI_AUTH}")

# ---------------------------------------------------------------------------
# Backend-down guard
# ---------------------------------------------------------------------------
check_backend() {
  local http_code
  http_code=$(curl -s -o /dev/null -w "%{http_code}" \
    --max-time 3 --connect-timeout 2 \
    ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} \
    "${LOKI_URL}/ready" 2>/dev/null || true)

  if [[ "$http_code" != "2"* ]]; then
    echo "ERROR: Loki backend unreachable at ${LOKI_URL} (HTTP ${http_code})" >&2
    echo "       To start it: make backend-up  (in the observability repo)" >&2
    exit 1
  fi
}

# ---------------------------------------------------------------------------
# Compact output formatter
# ---------------------------------------------------------------------------
# Prints log lines as: [timestamp] [level] [project/service] message
format_response() {
  local raw="$1"

  if command -v jq &>/dev/null; then
    local count
    count=$(echo "$raw" | jq -r '[.data.result[].values[]] | length' 2>/dev/null || echo "0")
    if [[ "$count" == "0" ]]; then
      echo "No log lines matched."
      return
    fi
    # Flatten all streams into one globally time-ordered feed.
    # gmtime before strftime for jq 1.6 compat (1.7+ also accepts it).
    # Single-stream input is unchanged in ordering (sort over one ordered stream is a no-op).
    echo "$raw" | jq -r '
      [
        .data.result[] |
        . as $stream |
        ($stream.stream | {
          project: (.project      // "-"),
          service: (.service_name // "-"),
          level:   (.level        // "-")
        }) as $labels |
        $stream.values[] |
        {
          ns:      .[0],
          msg:     .[1],
          level:   $labels.level,
          project: $labels.project,
          service: $labels.service
        }
      ] |
      sort_by(.ns) |
      .[] |
      "[\(.ns | tonumber / 1e9 | gmtime | strftime("%Y-%m-%dT%H:%M:%SZ"))] [\(.level)] [\(.project)/\(.service)] \(.msg)"
    ' 2>/dev/null || echo "$raw"
  else
    # Minimal fallback: strip outer JSON wrappers, print raw value pairs.
    # Avoids strftime (GNU awk only — not available on macOS BSD awk).
    local lines
    lines=$(echo "$raw" | grep -oE '"[0-9]{19}","[^"]*"' | \
      sed 's/"//g' | \
      awk -F',' '{
        ns=$1; msg=$2;
        sec=int(ns/1000000000);
        printf "[%d] %s\n", sec, msg
      }' 2>/dev/null)
    if [[ -z "$lines" ]]; then
      echo "$raw"
    else
      echo "$lines"
    fi
  fi
}

# ---------------------------------------------------------------------------
# Core read-only query helper
# Params: query, start (ns), end (ns), limit, direction
# ---------------------------------------------------------------------------
query_range() {
  local logql="$1"
  local start_ns="$2"
  local end_ns="$3"
  local limit="${4:-$DEFAULT_LIMIT}"
  local direction="${5:-forward}"

  local url="${LOKI_URL}/loki/api/v1/query_range"
  local response

  response=$(curl -s --max-time 30 \
    --get \
    ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} \
    --data-urlencode "query=${logql}" \
    --data-urlencode "start=${start_ns}" \
    --data-urlencode "end=${end_ns}" \
    --data-urlencode "limit=${limit}" \
    --data-urlencode "direction=${direction}" \
    "${url}" 2>/dev/null)

  local status
  if command -v jq &>/dev/null; then
    status=$(echo "$response" | jq -r '.status // "unknown"' 2>/dev/null || echo "unknown")
  else
    status=$(echo "$response" | grep -o '"status":"[^"]*"' | head -1 | cut -d'"' -f4 || echo "unknown")
  fi

  if [[ "$status" != "success" ]]; then
    echo "ERROR: Loki query failed (status=${status})" >&2
    if command -v jq &>/dev/null; then
      echo "$response" | jq -r '.error // .message // empty' 2>/dev/null >&2 \
        || echo "$response" | head -5 >&2
    else
      echo "$response" | head -5 >&2
    fi
    exit 1
  fi

  echo "$response"
}

# ---------------------------------------------------------------------------
# Paginated fetch — returns ALL matching entries across Loki pages.
# Params: logql, start_ns, end_ns
# Returns a single Loki-shaped JSON payload with all pages' .data.result merged.
# Requires jq for multi-page accumulation; falls back to a single query_range
# call at PAGE_SIZE when jq is absent (best-effort, no cross-page merge).
# Termination: stops on empty page, short page, or stalled cursor.
# ---------------------------------------------------------------------------
query_range_all() {
  local logql="$1"
  local start_ns="$2"
  local end_ns="$3"

  if ! command -v jq &>/dev/null; then
    # Best-effort fallback: single call at PAGE_SIZE — no JSON merge without jq.
    query_range "$logql" "$start_ns" "$end_ns" "$PAGE_SIZE" "forward"
    return
  fi

  local cursor="$start_ns"
  local accumulated='{"status":"success","data":{"result":[]}}'

  while true; do
    local page
    page=$(query_range "$logql" "$cursor" "$end_ns" "$PAGE_SIZE" "forward")

    # Count total entries in this page across all streams
    local page_count
    page_count=$(echo "$page" | jq -r '[.data.result[].values[]] | length' 2>/dev/null || echo "0")

    # Empty page → done
    if [[ "$page_count" == "0" ]]; then
      break
    fi

    # Merge this page's .data.result into the accumulator
    accumulated=$(printf '%s\n%s' "$accumulated" "$page" | jq -s '
      {"status":"success","data":{"result": (.[0].data.result + .[1].data.result)}}
    ' 2>/dev/null || echo "$accumulated")

    # Short page → last page; accumulate then stop
    if [[ "$page_count" -lt "$PAGE_SIZE" ]]; then
      break
    fi

    # Find the maximum ns timestamp across all streams in this page.
    # Strings — lexicographic max over equal-length 19-digit strings equals numeric
    # max, without the IEEE-754 precision loss of tonumber on jq < 1.7.
    local last_ns
    last_ns=$(echo "$page" | jq -r '
      [.data.result[].values[][0]] | max // empty
    ' 2>/dev/null || true)

    if [[ -z "$last_ns" || "$last_ns" == "null" ]]; then
      break
    fi

    # Advance cursor; stalled-cursor guard — never spin
    local next_cursor=$((last_ns + 1))
    if [[ "$next_cursor" -le "$cursor" ]]; then
      break
    fi
    cursor="$next_cursor"
  done

  echo "$accumulated"
}

# ---------------------------------------------------------------------------
# Time helpers
# ---------------------------------------------------------------------------

# Current time in nanoseconds
now_ns() {
  # Use Python for portable sub-second precision; fall back to date
  if command -v python3 &>/dev/null; then
    python3 -c 'import time; print(int(time.time() * 1e9))'
  else
    echo "$(date +%s)000000000"
  fi
}

# Parse a duration string (e.g. 15m, 2h, 1d) into nanoseconds offset
duration_to_ns() {
  local dur="$1"
  local value unit seconds

  if [[ "$dur" =~ ^([0-9]+)([smhd])$ ]]; then
    value="${BASH_REMATCH[1]}"
    unit="${BASH_REMATCH[2]}"
    case "$unit" in
      s) seconds=$value ;;
      m) seconds=$((value * 60)) ;;
      h) seconds=$((value * 3600)) ;;
      d) seconds=$((value * 86400)) ;;
    esac
    echo "${seconds}000000000"
  else
    echo "ERROR: Invalid duration '${dur}'. Use e.g. 15m, 2h, 1d" >&2
    exit 1
  fi
}

# ---------------------------------------------------------------------------
# Subcommand: since-restart <service> [--project P]
# Two-step: find latest service.start event, then fetch logs after it
# ---------------------------------------------------------------------------
cmd_since_restart() {
  local service=""
  local project=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --project)
        [[ $# -ge 2 ]] || { echo "ERROR: --project requires a value" >&2; exit 1; }
        shift; project="$1" ;;
      -*) echo "ERROR: Unknown flag '$1'" >&2; exit 1 ;;
      *) service="$1" ;;
    esac
    shift
  done

  if [[ -z "$service" ]]; then
    echo "Usage: query-loki.sh since-restart <service> [--project P]" >&2
    exit 1
  fi

  # Build label selector for the start-marker query
  local selector="{service_name=\"${service}\""
  if [[ -n "$project" ]]; then
    selector="${selector},project=\"${project}\""
  fi
  selector="${selector}}"

  local end_ns; end_ns=$(now_ns)
  # Search back 7 days for a restart marker
  local lookback_ns=$((7 * 86400 * 1000000000))
  local start_ns=$((end_ns - lookback_ns))

  echo "Searching for latest service.start marker for '${service}'..." >&2

  # Step 1: find the latest service.start event
  # event.name is a structured-metadata key → filter with | event_name="service.start"
  local marker_query="${selector} | event_name=\"service.start\""
  local marker_response
  marker_response=$(query_range "$marker_query" "$start_ns" "$end_ns" 1 "backward")

  local restart_ts_ns
  if command -v jq &>/dev/null; then
    restart_ts_ns=$(echo "$marker_response" | jq -r '
      .data.result[0].values[0][0] // empty
    ' 2>/dev/null || true)
  else
    restart_ts_ns=$(echo "$marker_response" | grep -oE '"[0-9]{19}"' | head -1 | tr -d '"' || true)
  fi

  if [[ -z "$restart_ts_ns" ]]; then
    echo "ERROR: No service.start marker found for '${service}' in the last 7 days." >&2
    echo "       The service may not emit this event, or it hasn't restarted recently." >&2
    exit 1
  fi

  local restart_readable
  restart_readable=$(python3 -c "
import datetime, sys
ns = int('${restart_ts_ns}')
dt = datetime.datetime.utcfromtimestamp(ns / 1e9)
print(dt.strftime('%Y-%m-%dT%H:%M:%SZ'))
" 2>/dev/null || echo "${restart_ts_ns}ns")

  echo "Found restart at: ${restart_readable}" >&2
  echo "Fetching logs since restart..." >&2

  # Step 2: fetch ALL logs since that timestamp (paginated — no line cap)
  local log_query="${selector}"
  local response
  response=$(query_range_all "$log_query" "$restart_ts_ns" "$end_ns")

  format_response "$response"
}

# ---------------------------------------------------------------------------
# Subcommand: trace <trace_id>
# trace_id is structured metadata — filter with | trace_id="..."
# ---------------------------------------------------------------------------
cmd_trace() {
  local trace_id=""
  local limit="$DEFAULT_LIMIT"

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --limit)
        [[ $# -ge 2 ]] || { echo "ERROR: --limit requires a value" >&2; exit 1; }
        shift; limit="$1"
        [[ "$limit" =~ ^[1-9][0-9]*$ ]] || { echo "ERROR: --limit must be a positive integer, got '${limit}'" >&2; exit 1; } ;;
      -*) echo "ERROR: Unknown flag '$1'" >&2; exit 1 ;;
      *) trace_id="$1" ;;
    esac
    shift
  done

  if [[ -z "$trace_id" ]]; then
    echo "Usage: query-loki.sh trace <trace_id> [--limit N]" >&2
    exit 1
  fi

  local end_ns; end_ns=$(now_ns)
  # Default: search back 24 hours for the trace
  local window_ns=$((24 * 3600 * 1000000000))
  local start_ns=$((end_ns - window_ns))

  # trace_id is structured metadata, not a label → pipeline filter | trace_id="..."
  # Loki requires at least one non-empty label matcher; service_name=~".+" spans all services.
  local logql="{service_name=~\".+\"} | trace_id=\"${trace_id}\""

  echo "Fetching logs for trace ${trace_id} (last 24h, limit=${limit})..." >&2

  local response
  response=$(query_range "$logql" "$start_ns" "$end_ns" "$limit" "forward")

  format_response "$response"
}

# ---------------------------------------------------------------------------
# Subcommand: window <range> [--level L] [--project P] [--service S]
# ---------------------------------------------------------------------------
cmd_window() {
  local range=""
  local level=""
  local project=""
  local service=""
  local limit="$DEFAULT_LIMIT"

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --level)
        [[ $# -ge 2 ]] || { echo "ERROR: --level requires a value" >&2; exit 1; }
        shift; level="$1" ;;
      --project)
        [[ $# -ge 2 ]] || { echo "ERROR: --project requires a value" >&2; exit 1; }
        shift; project="$1" ;;
      --service)
        [[ $# -ge 2 ]] || { echo "ERROR: --service requires a value" >&2; exit 1; }
        shift; service="$1" ;;
      --limit)
        [[ $# -ge 2 ]] || { echo "ERROR: --limit requires a value" >&2; exit 1; }
        shift; limit="$1"
        [[ "$limit" =~ ^[1-9][0-9]*$ ]] || { echo "ERROR: --limit must be a positive integer, got '${limit}'" >&2; exit 1; } ;;
      -*) echo "ERROR: Unknown flag '$1'" >&2; exit 1 ;;
      *)  range="$1" ;;
    esac
    shift
  done

  if [[ -z "$range" ]]; then
    echo "Usage: query-loki.sh window <range> [--level L] [--project P] [--service S] [--limit N]" >&2
    echo "       range examples: 15m, 2h, 1d" >&2
    exit 1
  fi

  local end_ns; end_ns=$(now_ns)
  local duration_ns; duration_ns=$(duration_to_ns "$range")
  local start_ns=$((end_ns - duration_ns))

  # Build label selector from optional filters
  local parts=()
  [[ -n "$project" ]]  && parts+=("project=\"${project}\"")
  [[ -n "$service" ]]  && parts+=("service_name=\"${service}\"")
  [[ -n "$level" ]]    && parts+=("level=\"${level}\"")

  local selector
  if [[ ${#parts[@]} -gt 0 ]]; then
    local IFS=","
    selector="{${parts[*]}}"
  else
    # Loki requires at least one non-empty matcher; this spans all services.
    selector='{service_name=~".+"}'
  fi

  echo "Fetching logs for window ${range} (selector: ${selector}, limit=${limit})..." >&2

  local response
  response=$(query_range "$selector" "$start_ns" "$end_ns" "$limit" "forward")

  format_response "$response"
}

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
  cat >&2 <<'EOF'
query-loki.sh — read-only Loki log slice tool

Usage:
  query-loki.sh since-restart <service> [--project P]
      Fetch logs since the service's last restart (requires event.name="service.start" marker).

  query-loki.sh trace <trace_id> [--limit N]
      Fetch all log lines for a trace ID (searched in structured metadata, last 24h).

  query-loki.sh window <range> [--level L] [--project P] [--service S] [--limit N]
      Fetch logs in a time window. Range: 15m, 2h, 1d, etc.

Environment:
  OBS_LOKI_URL   Loki base URL (default: http://localhost:3100)
  OBS_LOKI_AUTH  Full Authorization header value (default: unset — no auth)

Notes:
  - Index labels: project, service_name, level
  - service.name maps to service_name (the label key in Loki)
  - trace_id and other high-cardinality fields are structured metadata, not labels
  - All requests are read-only (GET only)
EOF
  exit 1
}

# ---------------------------------------------------------------------------
# Main dispatch
# ---------------------------------------------------------------------------
check_backend

case "${1:-}" in
  since-restart) shift; cmd_since_restart "$@" ;;
  trace)         shift; cmd_trace "$@" ;;
  window)        shift; cmd_window "$@" ;;
  *)             usage ;;
esac

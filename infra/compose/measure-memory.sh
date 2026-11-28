#!/usr/bin/env bash
# Measure the memory at rest of the laptop profile, with the AI off (D408, REQ-T09-03, "Memory at rest").
#
# It starts the laptop profile without the `ai` profile, so without Milvus, waits REST_S seconds, reads the memory
# of every container with `docker stats`, prints one line per container in MiB and the total, then stops the stack.
# Usage: measure-memory.sh [--rest-s N]
# Exit 0: measured. Exit 64: bad argument. Any other code: the one of `docker compose up` when the stack did not start.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=laptop-profile.env
source "${HERE}/laptop-profile.env"

usage() {
  echo "Usage: measure-memory.sh [--rest-s N]" >&2
}

rest_s="${REST_S}"
while (($# > 0)); do
  case "$1" in
    --rest-s)
      if (($# < 2)) || [[ ! "$2" =~ ^[0-9]+$ ]]; then
        usage
        exit 64
      fi
      rest_s="$2"
      shift 2
      ;;
    *)
      usage
      exit 64
      ;;
  esac
done

compose_files=(-f "${HERE}/${BASE_COMPOSE_FILE}" -f "${HERE}/${LAPTOP_COMPOSE_FILE}")

stop_stack() {
  docker compose "${compose_files[@]}" down >/dev/null 2>&1 || true
}
trap stop_stack EXIT

up_code=0
docker compose "${compose_files[@]}" up --detach --wait >&2 || up_code=$?
if ((up_code != 0)); then
  echo "The laptop profile did not start." >&2
  exit "${up_code}"
fi

sleep "${rest_s}"

mapfile -t ids < <(docker compose "${compose_files[@]}" ps --quiet)
usage_lines="$(docker stats --no-stream --format '{{.Name}}\t{{.MemUsage}}' "${ids[@]}")"

echo "Memory at rest of the laptop profile on $(date -u +%F), ${rest_s} s after start, AI off:"
awk -F '\t' '
  function to_mib(text,   value, unit) {
    sub(/ \/ .*/, "", text)
    match(text, /^[0-9.]+/)
    value = substr(text, 1, RLENGTH) + 0
    unit = substr(text, RLENGTH + 1)
    if (unit == "B") return value / 1048576
    if (unit == "KiB") return value / 1024
    if (unit == "MiB") return value
    if (unit == "GiB") return value * 1024
    return value
  }
  NF >= 2 { value = to_mib($2); total += value; printf "%s: %.1f MiB\n", $1, value }
  END { printf "Total: %.1f MiB\n", total }
' < <(LC_ALL=C sort -t $'\t' -k1,1 <<<"${usage_lines}")

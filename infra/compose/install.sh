#!/usr/bin/env bash
# Install the laptop profile, after checking that the machine fits it (REQ-T09-03, D408).
#
# Usage: install.sh [--ai on|off]
# With the AI off (the default) the profile `ai` is not passed to Compose, so Milvus is not installed (REQ-T08-01, D22).
# Exit 0: installed. Exit 64: bad usage, before any docker call. Otherwise: the code of check-machine.sh when the
# machine does not fit, or the code of `docker compose` when the profile did not start.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

usage() {
  echo "Usage: install.sh [--ai on|off]" >&2
}

ai="off"
if (($# == 0)); then
  :
elif (($# == 2)) && [[ "$1" == "--ai" ]] && [[ "$2" == "on" || "$2" == "off" ]]; then
  ai="$2"
else
  usage
  exit 64
fi

check_code=0
"${HERE}/check-machine.sh" || check_code=$?
if ((check_code != 0)); then
  exit "${check_code}"
fi

# shellcheck source=laptop-profile.env
source "${HERE}/laptop-profile.env"

compose=(docker compose -f "${HERE}/${BASE_COMPOSE_FILE}" -f "${HERE}/${LAPTOP_COMPOSE_FILE}")
if [[ "${ai}" == "on" ]]; then
  compose+=(--profile ai)
fi

up_code=0
"${compose[@]}" up --detach --wait || up_code=$?
if ((up_code != 0)); then
  echo "The laptop profile did not start." >&2
  exit "${up_code}"
fi

echo "Installed the laptop profile with the AI ${ai}."

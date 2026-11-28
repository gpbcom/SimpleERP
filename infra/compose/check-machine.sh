#!/usr/bin/env bash
# Check that this machine fits the laptop profile before installing it.
#
# It reads the memory, the cores and the Docker data folder from `docker info`, and the free disk from `df`,
# then compares them with the minimums of laptop-profile.env (D408, REQ-T09-03). It takes no argument.
# Exit 0: the machine fits. Exit 1: it is too small, one line per shortfall on stderr.
# Exit 2: Docker is missing or not running, so the machine cannot be checked.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=laptop-profile.env
source "${HERE}/laptop-profile.env"

if ! info="$(docker info --format '{{.MemTotal}} {{.NCPU}} {{.DockerRootDir}}' 2>/dev/null)"; then
  echo "Cannot check the machine: Docker is not installed or not running." >&2
  exit 2
fi

read -r memory_bytes cpus docker_root <<<"${info}"
if [[ ! -d "${docker_root}" ]]; then
  docker_root="${HERE}"
fi
free_kib="$(df -Pk "${docker_root}" | awk 'NR==2 {print $4}')"

memory_mib=$((memory_bytes / 1048576))
free_gib=$((free_kib / 1048576))

short=0
if ((memory_mib < MEMORY_MIN_MIB)); then
  echo "Not enough memory: ${memory_mib} MiB. The laptop profile needs at least ${MEMORY_MIN_MIB} MiB." >&2
  short=1
fi
if ((cpus < CPUS_MIN)); then
  echo "Not enough cores: ${cpus}. The laptop profile needs at least ${CPUS_MIN}." >&2
  short=1
fi
if ((free_gib < DISK_FREE_MIN_GIB)); then
  echo "Not enough free disk: ${free_gib} GiB. The laptop profile needs at least ${DISK_FREE_MIN_GIB} GiB." >&2
  short=1
fi
if ((short == 1)); then
  echo "This machine is too small for the laptop profile." >&2
  exit 1
fi

echo "The machine fits the laptop profile: ${memory_mib} MiB of memory, ${cpus} cores, ${free_gib} GiB of free disk."

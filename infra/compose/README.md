# infra/compose

The Docker Compose profiles of SimpleERP (D408, D421), for one server and for a laptop. Both run the same images as
the Helm charts of [`infra/helm/`](../helm/README.md) and as [`compose.e2e.yaml`](../../compose.e2e.yaml), the stack the
end-to-end tests run. The requirement is [REQ-T09-02](../../docs/specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md),
and the layout is [D438](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the
[repository layout design page](../../docs/technical/architecture/repository-layout.md).

## Files

| File | Holds |
| --- | --- |
| [`compose.yaml`](compose.yaml) | The one-server profile: PostgreSQL 18, the `platform` service and the `backoffice` front end |
| [`compose.laptop.yaml`](compose.laptop.yaml) | The laptop profile: an overlay that binds the published ports to the loopback address only |
| [`.gitignore`](.gitignore) | Ignores the `secrets/` folder, so that the password never reaches git |

## One server

The one-server profile runs PostgreSQL, the platform service and the back office. Its one install command is:

```bash
ERP_IMAGE_TAG=<commit sha> docker compose -f infra/compose/compose.yaml up -d --wait
```

- `ERP_IMAGE_TAG` is required. Set it to the commit SHA the images were published under. Compose refuses to start
  without it.
- `ERP_IMAGE_PREFIX` is optional. It defaults to `ghcr.io/gpbcom/simpleerp`, and each image is `<prefix>/<name>:<tag>`.
- `ERP_PLATFORM_PORT` is optional and defaults to `8000`, the port the platform service publishes.
- `ERP_BACKOFFICE_PORT` is optional and defaults to `8080`, the port the back office publishes.

**Before the first start**, the operator creates the PostgreSQL password file. Git ignores it, through the `.gitignore`
of this folder:

```bash
mkdir -p infra/compose/secrets && openssl rand -base64 24 > infra/compose/secrets/postgres_password
```

PostgreSQL reads the password from that file, as a Docker secret, and its data lives in the `postgres-data` volume.
The platform service starts once PostgreSQL is healthy, and the back office once the platform service is healthy.

## Laptop

The laptop profile adds `compose.laptop.yaml` to the one-server profile, on the same images:

```bash
ERP_IMAGE_TAG=<commit sha> docker compose -f infra/compose/compose.yaml -f infra/compose/compose.laptop.yaml up -d --wait
```

It only binds the published ports of the platform service and the back office to `127.0.0.1`, so that the laptop serves
its own user alone. It sets no image, no build and no memory or CPU limit. The memory budget of D408 is measured later,
by ticket T0.25.

## Same images everywhere

Both profiles pull the images that CI publishes, the same ones as `compose.e2e.yaml` and the Helm charts. Nothing is
built from these files.

## Installing the laptop profile

The installer checks the machine, then starts the laptop profile:

```bash
infra/compose/install.sh [--ai on|off]
```

- The AI is off by default. `--ai on` passes the Compose profile `ai` to `docker compose`, which is how Milvus is meant
  to start, as [REQ-T08-01](../../docs/specs/03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md)
  and [D22](../../docs/specs/06-decisions/foundations/d22-no-graphics-card-needed.md) require the AI to be optional. For
  now no service of `compose.yaml` or `compose.laptop.yaml` carries the `ai` profile, so `--ai on` starts the same stack
  as `--ai off` until the Milvus service is added.
- Before it starts anything, `install.sh` runs `infra/compose/check-machine.sh`. You can run that check on its own, with
  no argument, to see whether the machine fits without installing.
- The check reads the memory, the cores and the Docker data folder from `docker info`, and the free disk from `df`,
  then compares them with the minimums of [`laptop-profile.env`](laptop-profile.env):
  - **8192 MiB of memory**: the 8 GB budget of the laptop profile in
    [D408](../../docs/specs/06-decisions/technical/d408-performance-and-profiles.md).
  - **4 cores**: the normal load of the
    [performance and capacity page](../../docs/technical/infrastructure/performance-and-capacity.md).
  - **20 GiB of free disk**: an assumption of T0.25, because the specifications give no disk size.

Exit codes of `install.sh`:

| Code | Meaning |
| --- | --- |
| 0 | The machine fits and the profile is installed |
| 1 | The machine is too small (`check-machine.sh`, one line per shortfall on stderr), or the profile did not start |
| 2 | Docker is not installed or not running, so the machine cannot be checked |
| 64 | Bad argument, reported before any Docker call |

`check-machine.sh` exits 0 when the machine fits, 1 when it is too small and 2 when Docker is not running.
An exit code other than these comes from `docker compose`, when the profile does not start.

## Measuring the memory at rest

```bash
infra/compose/measure-memory.sh [--rest-s N]
```

The script starts the laptop profile with the AI off, so without Milvus, waits `N` seconds (60 by default, set by
`REST_S` in [`laptop-profile.env`](laptop-profile.env)), then reads the memory of every container with `docker stats`.
It prints a dated header, one line per container in MiB, the total in MiB, and then stops the stack. Exit codes: 0
when measured, 64 for a bad argument, and the code of `docker compose up` when the stack did not start.

The 8 GB promise of D408 is not proved by this script alone: it waits for the whole stack, which is only complete in
phase P2.

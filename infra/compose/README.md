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

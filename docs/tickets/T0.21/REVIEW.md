# T0.21: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `compose.e2e.yaml` at the repository root starts PostgreSQL 18 (pinned by digest, port not published, trust auth inside the throwaway stack), `platform` and `backoffice` from `${ERP_IMAGE_PREFIX}-<name>:${ERP_IMAGE_TAG}`. Each one waits for the health of the service before it. A `build:` fallback lets `stage.yml` build when the pull fails.
- The one-server profile `infra/compose/compose.yaml` runs the same three services with `restart: unless-stopped` and a named data volume. The PostgreSQL password is read as a Docker secret from `infra/compose/secrets/`, which git ignores. `ERP_IMAGE_TAG` is required, and the prefix defaults to `ghcr.io/gpbcom/simpleerp`.
- The laptop profile is an overlay that only binds the published ports to `127.0.0.1` (`!override`). It sets no image and no limit, because the D408 memory budget is measured in T0.25.
- `tests/infra/compose/` checks each file statically and through `docker compose config`. It also checks that the e2e stack, the one-server profile and the laptop profile resolve to the same images.
- Decision (K03): images are named `<prefix>-<name>`, as `images.yml` publishes them and Helm uses them, and the prefix test pins that whole form. This is sound.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. `docker compose -f compose.e2e.yaml up --wait` in CI's images job and `stage.yml` starts platform, backoffice and PostgreSQL, healthy | `tests-evidences/pytest.txt`: `test_compose_e2e.py` (health checks, `service_healthy` chain, only the two workflow variables, `test_docker_compose_resolves_the_file_with_only_those_two_variables`). The workflows already call this file. A real `up --wait` is only shown by CI | ✅ Pass (static and `config`; live start shown in CI) |
| 2. On one server, one command starts the one-server profile from the same images | `test_one_server_profile.py::test_one_command_with_only_the_image_tag_is_enough`, `test_same_images.py` | ✅ Pass, with a caveat: the password file must be created before the first start (follow-up) |
| 3. The laptop profile uses the same images as the one-server profile | `test_laptop_profile.py::test_the_laptop_profile_runs_the_same_images_as_the_one_server_profile`, `test_the_override_sets_no_image_and_no_build`, `test_same_images.py` | ✅ Pass |

## Look at first

- **Secrets:** no password appears in any file. The one-server profile reads `POSTGRES_PASSWORD_FILE` from `secrets/postgres_password`, which `.gitignore` excludes. The e2e stack uses `POSTGRES_HOST_AUTH_METHOD: trust`, which is acceptable only because the stack is throwaway and PostgreSQL publishes no port: `compose.e2e.yaml`, `infra/compose/compose.yaml`, `infra/compose/.gitignore`.
- **Same images:** the dash naming must match `images.yml` lines 74 and 166 and `infra/helm/values.yaml`. The `infra/compose/README.md` still shows the slash form (follow-up).
- **Health checks** repeat each Dockerfile's HEALTHCHECK (port 8000 `/v1/health`, port 8080 `/`): `backend/services/platform/Dockerfile`, `frontend/backoffice/Dockerfile`.
- **Exposure:** on one server, the platform and back-office ports are published on every interface, and on the laptop on the loopback address only.
- Company data isolation, identity and permissions: this ticket does not touch them (one company per Compose install, D18).

## Assumptions accepted

- Image naming `<prefix>-<name>` (K03, K11): accepted, it matches `images.yml`, `compose.e2e.yaml` and Helm.
- Resolver test case changed to the dash form (K03): accepted, it only tests substitution.
- K11 changed only compose.yaml lines 27 and 42, and left the K03 test to its owner: accepted, the tests pass.
- PostgreSQL 18, pinned by digest in every file (K10, approved by the person): accepted, no specification fixes the version.
- The TICKET anchors `#s04` and `#epics`, criterion 3 derived from the roadmap, and "healthy" meaning `up --wait`: accepted.

## Follow-ups

- `infra/compose/README.md`: the image form reads `<prefix>/<name>:<tag>` and should read `<prefix>-<name>:<tag>`.
- One command for the first install: the password file is a prerequisite step that the test sandbox creates for itself. Generate it when it is missing, or record the gap for T0.25 and T9.
- `ComposeLoader` and `construct_tagged` are written twice, in two `helpers.py` files. Move them into one file of their own.
- `test_one_server_profile.py`: `environment_of` returns a bare `dict`, which should be a `typing.Dict`. The image test also accepts the slash form and should assert only `-{name}:`.
- Evidence: add the CI log of a real `up --wait` and `ps` to `tests-evidences/`, and name the 3 skipped tests.

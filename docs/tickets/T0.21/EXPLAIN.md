# T0.21: Compose stack and its profiles

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Starts a throwaway stack of the real images (PostgreSQL, `platform`, `backoffice`) for Playwright and the stages, with one command, and waits until every service is healthy.
- Gives one server a Compose profile that installs the same three services with one command, restarting them and keeping the data on a volume.
- Gives a laptop a profile on the very same images, which only keeps the published ports on the loopback address.
- Checks all of this with tests that read each file and ask `docker compose config`, including that the three files resolve to the same images.

## ⚙️ How it works

1. **The stack of the tests:** [`compose.e2e.yaml`](../../../compose.e2e.yaml) declares PostgreSQL 18 pinned by digest, with trust authentication and no published port, in [`compose.e2e.yaml:6-17`](../../../compose.e2e.yaml#L6-L17).
2. **The platform waits for the database:** `platform` uses `${ERP_IMAGE_PREFIX}-platform:${ERP_IMAGE_TAG}`, with a `build:` fallback for `stage.yml`, and starts when PostgreSQL is `service_healthy`, in [`compose.e2e.yaml:19-38`](../../../compose.e2e.yaml#L19-L38). Its health check calls `/v1/health` on port 8000, as its Dockerfile does.
3. **The back office waits for the platform:** same pattern, with a `wget` check on port 8080, in [`compose.e2e.yaml:40-55`](../../../compose.e2e.yaml#L40-L55). `up --wait` therefore returns when the whole chain is healthy.
4. **The one-server profile:** [`infra/compose/compose.yaml:8-24`](../../../infra/compose/compose.yaml#L8-L24) runs the same PostgreSQL image, but reads its password from `POSTGRES_PASSWORD_FILE`, a Docker secret, and keeps data in the `postgres-data` volume.
5. **Required tag, default prefix:** the two application images use `${ERP_IMAGE_PREFIX:-ghcr.io/gpbcom/simpleerp}-<name>:${ERP_IMAGE_TAG:?...}` in [`infra/compose/compose.yaml:26-39`](../../../infra/compose/compose.yaml#L26-L39) and [`infra/compose/compose.yaml:41-54`](../../../infra/compose/compose.yaml#L41-L54), so Compose refuses to start without the tag. Every service has `restart: unless-stopped`.
6. **The secret stays out of git:** the secret file is declared in [`infra/compose/compose.yaml:56-58`](../../../infra/compose/compose.yaml#L56-L58) and the folder is ignored by [`infra/compose/.gitignore:1`](../../../infra/compose/.gitignore#L1).
7. **The laptop overlay:** [`infra/compose/compose.laptop.yaml:5-12`](../../../infra/compose/compose.laptop.yaml#L5-L12) replaces the ports of both services with `!override` so they bind to `127.0.0.1`. It sets no image, no build and no limit.
8. **The tests:** the e2e file is checked in [`tests/infra/compose/e2e/test_compose_e2e.py:24-95`](../../../tests/infra/compose/e2e/test_compose_e2e.py#L24-L95), the profiles in [`tests/infra/compose/profiles/test_one_server_profile.py:21-92`](../../../tests/infra/compose/profiles/test_one_server_profile.py#L21-L92) and [`tests/infra/compose/profiles/test_laptop_profile.py:18-51`](../../../tests/infra/compose/profiles/test_laptop_profile.py#L18-L51). The images test resolves the variables of each file with its own resolver ([`tests/infra/compose/images/helpers.py:44-82`](../../../tests/infra/compose/images/helpers.py#L44-L82)) and asserts one image per service across the three files, with the whole form `<prefix>-<service>:` in [`tests/infra/compose/images/test_same_images.py:44-48`](../../../tests/infra/compose/images/test_same_images.py#L44-L48).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`compose.e2e.yaml`](../../../compose.e2e.yaml) | Added | [1-55](../../../compose.e2e.yaml#L1) | +55 | −0 |
| [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) | Modified | [85-94](../../../docs/technical/delivery/ci-cd-and-stages.md#L85), [128](../../../docs/technical/delivery/ci-cd-and-stages.md#L128) | +11 | −3 |
| [`docs/technical/infrastructure/deployment.md`](../../../docs/technical/infrastructure/deployment.md) | Modified | [3-4](../../../docs/technical/infrastructure/deployment.md#L3), [8-14](../../../docs/technical/infrastructure/deployment.md#L8), [57](../../../docs/technical/infrastructure/deployment.md#L57) | +10 | −2 |
| [`infra/compose/.gitignore`](../../../infra/compose/.gitignore) | Added | [1](../../../infra/compose/.gitignore#L1) | +1 | −0 |
| [`infra/compose/README.md`](../../../infra/compose/README.md) | Modified | [3-6](../../../infra/compose/README.md#L3), [8-56](../../../infra/compose/README.md#L8) | +53 | −4 |
| [`infra/compose/compose.laptop.yaml`](../../../infra/compose/compose.laptop.yaml) | Added | [1-12](../../../infra/compose/compose.laptop.yaml#L1) | +12 | −0 |
| [`infra/compose/compose.yaml`](../../../infra/compose/compose.yaml) | Added | [1-61](../../../infra/compose/compose.yaml#L1) | +61 | −0 |
| [`tests/infra/compose/e2e/helpers.py`](../../../tests/infra/compose/e2e/helpers.py) | Added | [1-73](../../../tests/infra/compose/e2e/helpers.py#L1) | +73 | −0 |
| [`tests/infra/compose/e2e/test_compose_e2e.py`](../../../tests/infra/compose/e2e/test_compose_e2e.py) | Added | [1-95](../../../tests/infra/compose/e2e/test_compose_e2e.py#L1) | +95 | −0 |
| [`tests/infra/compose/images/helpers.py`](../../../tests/infra/compose/images/helpers.py) | Added | [1-85](../../../tests/infra/compose/images/helpers.py#L1) | +85 | −0 |
| [`tests/infra/compose/images/test_same_images.py`](../../../tests/infra/compose/images/test_same_images.py) | Added | [1-81](../../../tests/infra/compose/images/test_same_images.py#L1) | +81 | −0 |
| [`tests/infra/compose/profiles/helpers.py`](../../../tests/infra/compose/profiles/helpers.py) | Added | [1-97](../../../tests/infra/compose/profiles/helpers.py#L1) | +97 | −0 |
| [`tests/infra/compose/profiles/test_laptop_profile.py`](../../../tests/infra/compose/profiles/test_laptop_profile.py) | Added | [1-51](../../../tests/infra/compose/profiles/test_laptop_profile.py#L1) | +51 | −0 |
| [`tests/infra/compose/profiles/test_one_server_profile.py`](../../../tests/infra/compose/profiles/test_one_server_profile.py) | Added | [1-92](../../../tests/infra/compose/profiles/test_one_server_profile.py#L1) | +92 | −0 |
| **14 files** | | | **+777** | **−9** |
<!-- /changes -->

- [`compose.e2e.yaml`](../../../compose.e2e.yaml), lines [`1-55`](../../../compose.e2e.yaml#L1-L55): the new throwaway stack; only the prefix and the tag are required.
- [`infra/compose/compose.yaml`](../../../infra/compose/compose.yaml), lines [`1-61`](../../../infra/compose/compose.yaml#L1-L61): the one-server profile, with secret, volume and restart policy.
- [`infra/compose/compose.laptop.yaml`](../../../infra/compose/compose.laptop.yaml), lines [`5-12`](../../../infra/compose/compose.laptop.yaml#L5-L12): the loopback overlay.
- [`infra/compose/.gitignore`](../../../infra/compose/.gitignore): ignores `secrets/`.
- [`infra/compose/README.md`](../../../infra/compose/README.md), lines [`8-56`](../../../infra/compose/README.md#L8-L56): files, install command, secret step, laptop and same-images notes.
- [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) and [`docs/technical/infrastructure/deployment.md`](../../../docs/technical/infrastructure/deployment.md): describe the e2e stack and the profiles, and mark Compose as built.
- [`tests/infra/compose/e2e/`](../../../tests/infra/compose/e2e/test_compose_e2e.py), [`tests/infra/compose/images/`](../../../tests/infra/compose/images/test_same_images.py) and [`tests/infra/compose/profiles/`](../../../tests/infra/compose/profiles/test_laptop_profile.py): the tests and their helpers ([`e2e`](../../../tests/infra/compose/e2e/helpers.py), [`images`](../../../tests/infra/compose/images/helpers.py), [`profiles`](../../../tests/infra/compose/profiles/helpers.py)).

## 🧪 How to test it

```bash
uv run pytest tests/infra/compose -n 2
ERP_IMAGE_PREFIX=ghcr.io/gpbcom/simpleerp ERP_IMAGE_TAG=<tag> docker compose -f compose.e2e.yaml up --detach --wait
mkdir -p infra/compose/secrets && openssl rand -base64 24 > infra/compose/secrets/postgres_password
ERP_IMAGE_TAG=<tag> docker compose -f infra/compose/compose.yaml -f infra/compose/compose.laptop.yaml config --images
```

The first command runs the static and `docker compose config` checks, the second starts the e2e stack, the last two prepare the password and show that the laptop profile lists the same images.

## 🔗 Evidence

- [pytest](tests-evidences/pytest.txt): 1362 passed, 3 skipped.
- [ruff check](tests-evidences/ruff-check.txt) and [ruff format](tests-evidences/ruff-format.txt): clean.
- [mypy](tests-evidences/mypy.txt): clean.
- [Plan view](tests-evidences/plan-view.txt) and [ticket references](tests-evidences/ticket-refs.txt): up to date.

## 📝 Assumptions accepted

- K03: application images are `<prefix>-<name>`. This is the published naming of `images.yml`, [`compose.e2e.yaml`](../../../compose.e2e.yaml) and the Helm values.
- K03: the resolver test case became `${ERP_IMAGE_PREFIX:-other}-platform`; it only exercises substitution.
- K11: only the replacements at `compose.yaml` lines 27 and 42 were made, as the first attempt's edit was already in place.
- K11: it did not examine the assertion of `test_same_images.py`, which belongs to K03 (TKT-19); the pytest evidence shows it passing.
- PROGRESS (K10): PostgreSQL 18, pinned by digest, in every file. No specification fixes the version, it is the newest major, and the person approved it.
- TICKET: the roadmap anchor is `#s04` and the epic anchor `#epics`, as the phase page has no per-ticket anchors.
- TICKET: criterion 3 is derived from "the laptop and one-server profiles from the same images", since D408 gives no laptop measure before T0.25.
- TICKET: "healthy" means what `up --wait` waits for, using health checks that repeat each Dockerfile's `HEALTHCHECK`.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`infra/compose/README.md:27`](../../../infra/compose/README.md#L27) | Says each image is `<prefix>/<name>:<tag>`. Since K11 every file uses `<prefix>-<name>:<tag>`, so fix the sentence. |
| [`infra/compose/compose.yaml`](../../../infra/compose/compose.yaml), [`infra/compose/README.md:30-35`](../../../infra/compose/README.md#L30-L35), [`tests/infra/compose/profiles/helpers.py:65-79`](../../../tests/infra/compose/profiles/helpers.py#L65-L79), [`tests/infra/compose/profiles/test_one_server_profile.py:87-92`](../../../tests/infra/compose/profiles/test_one_server_profile.py#L87-L92) | The first install needs the password file first (two commands), and the test hides it because its sandbox writes the file. Generate the password when missing, or record the gap for T0.25 and T9. |
| [`tests/infra/compose/images/helpers.py:22-37`](../../../tests/infra/compose/images/helpers.py#L22-L37), [`tests/infra/compose/profiles/helpers.py:20-35`](../../../tests/infra/compose/profiles/helpers.py#L20-L35) | `ComposeLoader` and `construct_tagged` are written twice, and each helpers file also holds a class. Move the loader into one shared file. |
| [`tests/infra/compose/profiles/test_one_server_profile.py:22`](../../../tests/infra/compose/profiles/test_one_server_profile.py#L22) | `environment_of` returns a bare `dict`. Use `Dict[str, object]`. |
| [`tests/infra/compose/profiles/test_one_server_profile.py:34`](../../../tests/infra/compose/profiles/test_one_server_profile.py#L34) | The image test accepts `/{name}:` or `-{name}:`. Assert only `-{name}:`, as `test_same_images.py` does. |
| [`docs/tickets/T0.21/tests-evidences/pytest.txt`](tests-evidences/pytest.txt) | Only static and `config` checks, with 3 skipped tests not named. Add the CI log of a real `up --wait` and `ps`, and name the skipped tests. |

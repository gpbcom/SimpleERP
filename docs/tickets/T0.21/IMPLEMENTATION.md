# T0.21: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- `up --wait` on [`compose.e2e.yaml`](../../../compose.e2e.yaml) must start `platform`, `backoffice` and PostgreSQL healthy, with only the prefix and the tag set (acceptance criterion 1 of [TICKET.md](TICKET.md)).
- One command installs the one-server profile, and the laptop profile uses the same images (criteria 2 and 3, REQ-T09-02, D408, D421).
- No secret in a file or in git (AGENT.md, "Data and enums": secrets live in a secret store).
- The image names must match the ones `images.yml` publishes and Helm uses.
- The memory budget of the laptop is measured by T0.25, not here ([TICKET.md](TICKET.md), out of scope).
- Test files follow AGENT.md: one class per file, five files per folder at most.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Image naming | `<prefix>-<name>:<tag>` | `<prefix>/<name>:<tag>` | One stricter assertion, and a README sentence to fix |
| [D2](#d2) | Laptop profile | An overlay on the one-server file | A separate full file | The laptop cannot differ in images, by design |
| [D3](#d3) | PostgreSQL password | A Docker secret file, ignored by git | A literal or an environment variable | A manual step before the first start |
| [D4](#d4) | PostgreSQL version | 18, pinned by digest | A moving tag | A digest to update by hand |
| [D5](#d5) | The e2e stack | Trust authentication, no published database port | A password in the stack | Acceptable only because the stack is throwaway |
| [D6](#d6) | How the files are tested | Static reading plus `docker compose config` | Only a live `up --wait` | No live start proved locally |

## <a id="d1"></a>D1: Image naming

**Chosen:** `${ERP_IMAGE_PREFIX}-<name>:${ERP_IMAGE_TAG}` · **Where:** [`compose.e2e.yaml:20`](../../../compose.e2e.yaml#L20) and [`infra/compose/compose.yaml:27`](../../../infra/compose/compose.yaml#L27) · **Source:** K03, K11 and the reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ `<prefix>-<name>` | It is the form `images.yml` publishes and Helm uses (accepted assumption); the test pins the whole form in [`tests/infra/compose/images/test_same_images.py:44-48`](../../../tests/infra/compose/images/test_same_images.py#L44-L48) | Stricter than a prefix check alone |
| `startswith(PREFIX)` plus a check of the name part (K03's alternative) | Looser, two assertions | Does not pin the published form |
| `<prefix>/<name>` | Was the first wording of the README | Differs from the published images; K11 removed it |

**Trade-off:** the test fails if the naming ever changes, which is the point. [`infra/compose/README.md:27`](../../../infra/compose/README.md#L27) still shows the slash form (follow-up).

**Revisit when:** the registry layout of `images.yml` changes.

## <a id="d2"></a>D2: The laptop profile is an overlay

**Chosen:** [`infra/compose/compose.laptop.yaml:5-12`](../../../infra/compose/compose.laptop.yaml#L5-L12) with `!override` on the ports · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Overlay | It cannot name another image, so criterion 3 holds by construction; a test checks it sets no image or build | Needs `-f` twice |
| A second full file | Self-contained | Could drift from the one-server images; no reason for it is given in the specifications |

**Trade-off:** no limit is set, since D408's budget is measured in T0.25.

**Revisit when:** T0.25 gives a laptop memory figure.

## <a id="d3"></a>D3: The PostgreSQL password

**Chosen:** `POSTGRES_PASSWORD_FILE` from a `secrets/` file ignored by git · **Where:** [`infra/compose/compose.yaml:14-16`](../../../infra/compose/compose.yaml#L14-L16), [`infra/compose/.gitignore:1`](../../../infra/compose/.gitignore#L1) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Secret file | No password in any file; tests refuse a literal value | The operator creates the file first, so install is two commands |
| A password in an environment variable | One command | Secrets must not appear in configuration |

**Trade-off:** criterion 2 holds with a caveat, listed as a follow-up in [EXPLAIN.md](EXPLAIN.md).

**Revisit when:** T0.25 or T9 build the installer.

## <a id="d4"></a>D4: PostgreSQL 18 pinned by digest

**Chosen:** [`compose.e2e.yaml:7`](../../../compose.e2e.yaml#L7), the same digest in [`infra/compose/compose.yaml:9`](../../../infra/compose/compose.yaml#L9) · **Source:** K10, approved by the person

| Option | For | Against |
| --- | --- | --- |
| ✅ 18 by digest | Same image in every file; a test checks it | No specification fixes the version; the digest is updated by hand |
| A moving tag | Gets patches | Files could run different images |

**Revisit when:** a specification fixes the PostgreSQL version.

## <a id="d5"></a>D5: Trust authentication in the e2e stack

**Chosen:** `POSTGRES_HOST_AUTH_METHOD: trust` in [`compose.e2e.yaml:9`](../../../compose.e2e.yaml#L9), no published port ([`tests/infra/compose/e2e/test_compose_e2e.py:67-68`](../../../tests/infra/compose/e2e/test_compose_e2e.py#L67-L68)) · **Source:** reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ Trust, private network | The workflows set only two variables, and no secret exists | Insecure for anything not throwaway |
| A password | Safer | Would need a third variable or a literal |

**Revisit when:** a stage keeps the stack running for people.

## <a id="d6"></a>D6: How the files are tested

**Chosen:** static reading plus `docker compose config`, skipped without Docker · **Where:** [`tests/infra/compose/e2e/test_compose_e2e.py:79-95`](../../../tests/infra/compose/e2e/test_compose_e2e.py#L79-L95) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Static and `config` | Fast, runs in the unit suite, no registry | A real start is shown only by CI |
| A live `up --wait` | Proves health | Needs published images; open point whether the unit suite could pull them |

**Trade-off:** the evidence has no live start (follow-up).

**Revisit when:** the images job logs are kept as evidence.

## 📝 Assumptions behind the choices

- Images are `<prefix>-<name>`: supports [D1](#d1).
- PostgreSQL 18, pinned by digest, approved by the person: supports [D4](#d4).
- "Healthy" means what `up --wait` waits for, the Dockerfile health checks repeated: supports [D6](#d6).
- Criterion 3 is derived from the roadmap, with no laptop measure before T0.25: supports [D2](#d2).

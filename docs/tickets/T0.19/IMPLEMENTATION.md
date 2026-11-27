# T0.19: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

The workers reported no decision, so every choice below is recorded in [PLAN.md](PLAN.md), or read from the diff, and the reasons that nobody gave are written as open points.

## 🎯 Constraints

- One chart per image (`platform`, `backoffice`), from the same images as Compose, under `infra/helm` ([TICKET.md](TICKET.md), criterion 3; [D438](../../specs/06-decisions/technical/d438-repository-layout.md); [REQ-T09-02](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md)).
- Every default written out, the tag from the commit and no secret in values ([TICKET.md](TICKET.md), criterion 4; [D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md)).
- `helm lint` and `helm template` pass in CI and the manifests validate against the Kubernetes schemas ([TICKET.md](TICKET.md), criteria 1 and 2).
- CI runs jobs only for what changed, and a release runs every suite and keeps its test reports ([`AGENT.md`](../../../AGENT.md), "CI/CD"; TKT-26 in [`.claude/rules/tickets.md`](../../../.claude/rules/tickets.md)).
- No Python module-level constants or shell logic hidden in workflows: CI steps are scripts of `.github/scripts/` ([`AGENT.md`](../../../AGENT.md), "Layout").

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Chart structure | Umbrella with no template, one unpacked chart per image | One chart holding every template | Two charts that drifted apart |
| [D2](#d2) | Image tag | `global.image.tag`, set from the commit, fallback `appVersion` | A tag required by the chart | A plain install pulls a tag nobody publishes |
| [D3](#d3) | Schema validation | `kubeconform -strict`, pinned by version and checksum | `helm lint` alone, or `kubectl --dry-run` | Schema proof only in CI |
| [D4](#d4) | CI wiring | Own reusable `helm.yml`, selected by a `helm` output | Fold into `terraform.yml` or run always | `images` does not wait for it |
| [D5](#d5) | Secrets and exposure | No Secret, no Ingress, `ClusterIP` | An Ingress or a Secret template | The install needs more work later |

## <a id="d1"></a>D1: Chart structure

**Chosen:** an umbrella `simpleerp` that only depends on `platform` and `backoffice`, each switched by `<chart>.enabled` · **Where:** [`infra/helm/Chart.yaml:7-13`](../../../infra/helm/Chart.yaml#L7-L13) · **Source:** [PLAN.md](PLAN.md) and the layout page

| Option | For | Against |
| --- | --- | --- |
| ✅ Umbrella plus one chart per image | The [repository layout](../../technical/architecture/repository-layout.md) says `helm/` holds "an umbrella chart and a chart per service"; later phases add a chart per service; each chart renders alone ([`tests/infra/helm/test_rendering.py:78`](../../../tests/infra/helm/test_rendering.py#L78)) | The two templates were written separately and differ without reason (follow-up) |
| A single chart with every template | Less duplication today | Does not follow the layout page; a service added later would grow one chart |

**Trade-off:** duplication between two charts for the shape the specification names.

**Revisit when:** a third service chart is added: share the helpers in a library chart.

## <a id="d2"></a>D2: Image tag

**Chosen:** `global.image.tag`, empty by default and falling back to `appVersion`; CI passes `github.sha` · **Where:** [`infra/helm/charts/platform/templates/_helpers.tpl:20-23`](../../../infra/helm/charts/platform/templates/_helpers.tpl#L20-L23), [`.github/workflows/helm.yml:40`](../../../.github/workflows/helm.yml#L40) · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Empty tag with fallback | Criterion 4 (tag from the commit) is met; the chart renders with no flag, so `helm lint` runs plain | An install with no tag points at `0.1.0`, which no image carries |
| `required` on the tag | A missing tag fails at once, not as ImagePullBackOff | `helm lint` and `helm template` then need a tag everywhere; the reviewer left it as a follow-up |

**Trade-off:** a silent bad default for a simple render.

**Revisit when:** images are published under release versions, or the first real install is documented.

## <a id="d3"></a>D3: Schema validation

**Chosen:** `kubeconform -strict` on the rendered release, Kubernetes 1.33.0, pinned by version and SHA-256 · **Where:** [`.github/scripts/check_helm.sh:43-50`](../../../.github/scripts/check_helm.sh#L43-L50), [`.github/workflows/helm.yml:14-16`](../../../.github/workflows/helm.yml#L14-L16) · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ kubeconform | Criterion 2 asks for validation against the Kubernetes schemas, offline, with a JUnit report for TKT-26 | One more downloaded tool; the checksum could not be checked offline |
| `helm lint` only | Already required | It does not validate the rendered manifests |

The alternatives other than these two, and why 1.33.0, are an open point: no worker gave a reason for the version.

**Trade-off:** the proof of criterion 2 is in CI only; locally three tests are skipped.

**Revisit when:** a Kubernetes version is chosen by the Installation page, or the first CI run rejects the pin.

## <a id="d4"></a>D4: CI wiring

**Chosen:** a reusable [`.github/workflows/helm.yml`](../../../.github/workflows/helm.yml) called by `ci.yml` and `release.yml`, selected by a `helm` output of `detect_changes.py` only once [`infra/helm/Chart.yaml`](../../../infra/helm/Chart.yaml) exists · **Where:** [`.github/scripts/detect_changes.py:174-219`](../../../.github/scripts/detect_changes.py#L174-L219), [`.github/workflows/ci.yml:92-96`](../../../.github/workflows/ci.yml#L92-L96) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Own workflow and output | Same shape as `terraform.yml`; jobs run only for what changed (AGENT.md CI step 1); the release runs it with everything selected | `images` does not wait for it (follow-up) |
| Run on every change | Simpler | Breaks "run jobs only for those that changed" |

**Trade-off:** a failing Helm check does not stop images from being built, while `result` still gates the merge.

**Revisit when:** images are published from `develop` and a bad chart must block them.

## <a id="d5"></a>D5: Secrets and exposure

**Chosen:** no Secret template, no Ingress, Services of type `ClusterIP`, env as plain values · **Where:** [`infra/helm/charts/platform/values.yaml:24-26`](../../../infra/helm/charts/platform/values.yaml#L24-L26) · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Nothing exposed, no secret | Criterion 4 and D421 (private services); checked by [`tests/infra/helm/test_values.py:146`](../../../tests/infra/helm/test_values.py#L146) and [`tests/infra/helm/test_rendering.py:61`](../../../tests/infra/helm/test_rendering.py#L61) | A real install needs a gateway and a secret store later |
| An Ingress and a Secret | Closer to a usable install | Out of scope for a skeleton; the specification gives nothing to fill them |

**Trade-off:** a skeleton that is not yet reachable from outside.

**Revisit when:** the gateway and the secret store tickets land.

## 📝 Assumptions behind the choices

- Only the platform and backoffice charts are built: supports [D1](#d1).
- REQ-T09-02, D421 and D438 are the specification the ticket builds on: supports [D1](#d1) and [D5](#d5).
- No budget is taken from the Installation page: supports [D3](#d3).

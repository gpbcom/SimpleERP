# Deployment

Targets OVHcloud, Scaleway and self-hosted; Terraform by default; Compose and Helm (D18). Compose and Helm are built;
Terraform and the cloud targets are not yet.

## Today

**Compose.** The Compose profiles are in [`infra/compose/`](../../../infra/compose/README.md): the one-server profile
[`compose.yaml`](../../../infra/compose/compose.yaml) (PostgreSQL, the platform service and the back office) and the
laptop overlay [`compose.laptop.yaml`](../../../infra/compose/compose.laptop.yaml), which binds the ports to the loopback
address. Both run the images tagged with a commit SHA, and the end-to-end stack of
[`compose.e2e.yaml`](../../../compose.e2e.yaml) runs the same images for the tests. The password of PostgreSQL is read
from a file the operator creates, which git ignores.

The Helm deployment of T0.19 is in `infra/helm/` ([README](../../../infra/helm/README.md)). It is the first step of the
[Helm delivery](../../specs/03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md)
(REQ-T09-02), and it installs the images that Compose runs ([D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md)).

| Part | Where | What it does |
| --- | --- | --- |
| Umbrella chart `simpleerp` | [`Chart.yaml`](../../../infra/helm/Chart.yaml), [`values.yaml`](../../../infra/helm/values.yaml) | Depends on the two charts below, each enabled by a condition. It has no template of its own |
| Chart `platform` | [`charts/platform/values.yaml`](../../../infra/helm/charts/platform/values.yaml) | Installs the platform service, on port 8000 with the probe `/v1/health` |
| Chart `backoffice` | [`charts/backoffice/values.yaml`](../../../infra/helm/charts/backoffice/values.yaml) | Installs the back-office front end, on port 8080 with the probe `/` |

There is one chart per image. The images are `ghcr.io/gpbcom/simpleerp-<name>`, the same images as Compose, built by
[`images.yml`](../../../.github/workflows/images.yml) under the prefix `global.image.prefix`. `global.image.tag` is set
to the commit SHA the images were published under. An empty tag falls back to the chart's `appVersion`.

**Values.** Every default is written out in the values files, and none of them is a secret. The services are private:
their Services are `ClusterIP`, and no chart renders an ingress yet, so nothing is exposed outside the cluster. The
`env` maps are empty by default, and the resources, the security contexts, the scheduling and the replica count are
set in the values, ready to be overridden.

**Install.** The command of [`infra/helm/README.md`](../../../infra/helm/README.md) is:

```bash
helm install simpleerp infra/helm --namespace simpleerp --create-namespace --set global.image.tag=<commit SHA>
```

**Check.** The CI job [`helm.yml`](../../../.github/workflows/helm.yml) runs when `infra/helm/` changes. It calls
[`check_helm.sh`](../../../.github/scripts/check_helm.sh), which runs `helm lint --strict` on the umbrella chart and on
each chart, then `helm template` of the whole release, then `kubeconform` in strict mode against the Kubernetes 1.33.0
schemas. The JUnit report is `helm.xml`, kept as the `test-report-helm` artifact, failed runs included, for the release
test report ([D438](../../specs/06-decisions/technical/d438-repository-layout.md) for the layout of `infra/`, and the
[repository layout](../architecture/repository-layout.md)).

## Target design (specified in GH-2, not built yet)

**Targets (D419, D421).** SimpleERP is fully CNCF compatible: it runs on a self-managed Kubernetes and on the managed
Kubernetes of European clouds (for example Scaleway and OVHcloud, D375), with only portable components. Docker Compose
and Helm are both supported everywhere: Compose for one server and the laptop profile, Helm for every Kubernetes, with
the same images. Terraform describes the infrastructure; the details are in
[Infrastructure deployment](infrastructure.md).

Decided in [D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md).

Last reviewed: 2026-11-28 (T0.21)

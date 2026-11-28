# infra/helm

The Helm deployment of SimpleERP: the umbrella chart `simpleerp` (`Chart.yaml`, `values.yaml`) and, under `charts/`,
one chart per image (`platform`, `backoffice`). The umbrella chart has no template of its own. Its dependencies sit
unpacked in `charts/`, so `helm lint` and `helm template` work without `helm dependency build`.

## Install

```bash
helm install simpleerp infra/helm --namespace simpleerp --create-namespace --set global.image.tag=<commit SHA>
```

## Images

The images are the ones Compose runs, built and published by `.github/workflows/images.yml` under
`global.image.prefix` (`ghcr.io/gpbcom/simpleerp`), tagged with the commit SHA. Set `global.image.tag` to that SHA.
An empty tag falls back to the chart's `appVersion`. The values hold no secret.

## Platform address

The back-office image proxies `/v1/` to `ERP_PLATFORM_URL`. Its chart sets it to the platform Service of the same
release, `http://<release>-platform.<namespace>.svc.<clusterDomain>:<platformPort>`, fully qualified because nginx
resolves it without the pod's search domains. Set `backoffice.platformUrl` to point it elsewhere.

## Check

```bash
bash .github/scripts/check_helm.sh infra/helm <tag> reports
```

See [D438, the repository layout](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the
[repository layout design page](../../docs/technical/architecture/repository-layout.md).

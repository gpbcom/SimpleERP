# T0.19: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `infra/helm` now holds an umbrella chart `simpleerp` with no templates of its own. It depends on one unpacked chart per image, `platform` (port 8000, probe `/v1/health`) and `backoffice` (port 8080, probe `/`), and each can be switched off with `<chart>.enabled`.
- Images are `<global.image.prefix>-<name>:<global.image.tag>`. The prefix defaults to `ghcr.io/gpbcom/simpleerp`, the same names `images.yml` publishes. CI sets the tag to `github.sha`, and an empty tag falls back to `appVersion`.
- Every default is written out in the values files. Services are `ClusterIP`, and no Ingress and no Secret are rendered. Tests check that every `.Values.x` a template reads exists in the values, and that no key names a secret.
- A new reusable CI workflow `helm.yml` runs `check_helm.sh`: `helm lint --strict` on the umbrella and on each chart, `helm template`, then a strict `kubeconform` check against the Kubernetes 1.33.0 schemas. kubeconform is pinned by version and SHA-256. The JUnit report is kept as `test-report-helm`, which feeds the release report (TKT-26).
- `detect_changes.py` gains a `helm` output, true when `infra/helm/` changes (it also selects the repository tests) or when everything is selected, and only once `infra/helm/Chart.yaml` exists. `ci.yml` and `release.yml` call the new workflow.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. `helm lint` passes in CI | `tests-evidences/helm-lint-infra-helm.txt`, `helm-lint-infra-helm-charts-platform.txt`, `helm-lint-infra-helm-charts-backoffice.txt`; `TestHelmWorkflow::test_the_check_script_runs_on_the_charts_with_the_commit_as_image_tag`; `TestCiWorkflow::test_each_language_job_calls_its_workflow_under_its_condition[helm]` | ✅ Pass |
| 2. `helm template` renders and the manifests validate against the Kubernetes schemas | `TestRendering` (all cases, `tests-evidences/pytest.txt`); `TestCheckHelm::test_the_real_chart_passes_and_writes_a_junit_report` and `test_an_unknown_field_in_the_deployment_spec_fails_the_strict_schema_check` (skipped locally, since kubeconform is absent, and run by `helm.yml` in CI) | ✅ Pass (schema validation proven in CI only) |
| 3. One chart per image, `platform` and `backoffice`, same images as Compose | `TestCharts::test_a_chart_matches_an_image_with_a_dockerfile`, `test_every_chart_folder_matches_an_image`; `TestRendering::test_every_image_carries_the_commit_tag` | ✅ Pass |
| 4. Every default written out, tag from the commit, no secret | `TestValues::test_a_chart_writes_out_its_defaults`, `test_every_value_a_template_reads_is_written_out_in_the_chart_values`, `test_no_key_names_a_secret`, `test_no_template_declares_a_secret`; `TestRendering::test_no_ingress_and_no_secret_is_rendered[Secret]`; `helm.yml` sets `IMAGE_TAG: ${{ github.sha }}` | ✅ Pass |

## Look at first

- **The kubeconform pin** (`KUBECONFORM_VERSION` v0.8.0 and its SHA-256), in `.github/workflows/helm.yml`. I could not check the checksum offline. The first CI run proves it, and a wrong pin fails the job loudly.
- **The tag fallback**, in `infra/helm/charts/*/templates/_helpers.tpl` and `infra/helm/values.yaml`. With no `--set global.image.tag`, the pods point at `:0.1.0`, a tag nobody publishes (see the follow-up).
- **What triggers the check**, in `.github/scripts/detect_changes.py`. `helm` is selected only once the umbrella `Chart.yaml` exists, and a shared path (`.github/scripts/`, `helm.yml`) selects it.
- **Images are not gated on Helm**, in `.github/workflows/ci.yml`. The `images` job does not wait for `helm`, unlike `terraform`. The merge is still gated by `result`.
- **Isolation and secrets:** no identity, permission or company data is touched. The values hold no secret, and Services stay inside the cluster (`ClusterIP`, no Ingress).

## Assumptions accepted

- Roadmap links point to the sprint and epic sections: accepted. It changes no behaviour.
- No budget is taken from the Installation page: accepted. Its measures are still to be specified.
- Only the `platform` and `backoffice` charts: accepted. These are the only images today, and the roadmap row names just these two.
- REQ-T09-02, D421 and D438 are the specification the ticket builds on: accepted. They settle Helm, the same images as Compose, and the `infra/helm` layout.
- The agents reported no other assumption and no implementation decision.

## Follow-ups

- Make `images` in `ci.yml` wait for `helm`, as it does for `terraform`, and add `helm` to `CHECK_JOBS` in `test_ci_workflow.py`.
- Make `global.image.tag` required, or say plainly that the `appVersion` fallback has no published image.
- Align the platform and backoffice templates and helpers (`if` against `with`, the `helm.sh/chart` label), or move them into a library chart.
- Move the module-level constants of `test_check_helm.py` and `test_charts.py` into ClassVars.
- Re-wrap the long header comment line of `release.yml`.
- Add a local `check_helm.sh` report (`helm.xml`) to `tests-evidences/`, as evidence of the schema validation.

#!/usr/bin/env bash
# Check the Helm charts: helm lint --strict on the umbrella chart and on every sub-chart, helm template of the whole
# release, then kubeconform (strict) on the rendered manifests with a JUnit report in <reports dir>/helm.xml.
#
# Usage: .github/scripts/check_helm.sh <helm root> <image tag> <reports dir>
set -euo pipefail

# The Kubernetes version the manifests are validated against, written out as X.Y.Z.
KUBERNETES_VERSION="1.33.0"

if [ "$#" -ne 3 ]; then
  echo "usage: check_helm.sh <helm root> <image tag> <reports dir>" >&2
  exit 2
fi

root="$1"
tag="$2"
reports="$3"

for tool in helm kubeconform; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "check_helm.sh: $tool is not installed." >&2
    exit 1
  fi
done

echo "::group::helm lint $root"
helm lint --strict --set "global.image.tag=$tag" "$root"
for chart in "$root"/charts/*/; do
  if [ -f "${chart}Chart.yaml" ]; then
    helm lint --strict --set "global.image.tag=$tag" "$chart"
  fi
done
echo "::endgroup::"

rendered="$(mktemp)"
trap 'rm -f "$rendered"' EXIT

echo "::group::helm template $root"
helm template simpleerp "$root" --set "global.image.tag=$tag" >"$rendered"
echo "::endgroup::"

echo "::group::kubeconform $KUBERNETES_VERSION"
mkdir -p "$reports"
status=0
kubeconform -strict -summary -kubernetes-version "$KUBERNETES_VERSION" -output junit "$rendered" \
  >"$reports/helm.xml" || status=$?
cat "$reports/helm.xml"
echo "::endgroup::"
exit "$status"

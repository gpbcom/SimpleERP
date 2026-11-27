# Deployment

Targets OVHcloud, Scaleway and self-hosted; Terraform by default; Compose and Helm (D18). Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Targets (D419, D421).** SimpleERP is fully CNCF compatible: it runs on a self-managed Kubernetes and on the managed
Kubernetes of European clouds (for example Scaleway and OVHcloud, D375), with only portable components. Docker Compose
and Helm are both supported everywhere: Compose for one server and the laptop profile, Helm for every Kubernetes, with
the same images. Terraform describes the infrastructure; the details are in
[Infrastructure deployment](infrastructure.md).

Decided in [D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md).

Last reviewed: 2026-11-12 (GH-2)

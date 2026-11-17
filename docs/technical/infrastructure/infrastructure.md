# Infrastructure deployment

The deployment targets, self-hosted and the fully managed hosted edition: clusters, regions, sizing, networks,
Terraform. Nothing of the target is built yet.

## Today

Nothing built yet; the targets of D18 are in [Deployment](deployment.md).

## Target design (specified in GH-2, not built yet)

**Principle (D421).** Fully CNCF compatible: only portable components and Kubernetes-native operators, so that nothing
requires a cloud's proprietary service. It works on a self-managed Kubernetes and on the managed Kubernetes of European
clouds (for example Scaleway and OVHcloud, D375).

**Data services.** Operators run them in the cluster by default: CloudNativePG for PostgreSQL, an S3-compatible server
(for example Garage or MinIO) for objects, OpenBao for secrets, Milvus for vectors, the event bus and the workflow
engine. On a European managed Kubernetes, the cloud's managed PostgreSQL, object storage and KMS may replace them by
configuration, never required.

**Packaging.** Docker Compose and Helm are both supported everywhere, from the same images: Compose for one server and
the laptop profile (an installer checks the machine and the 8 GB budget, D408), Helm charts for every Kubernetes (an IT
provider's platform, a large company, the hosted edition); air-gapped installs work from a mirrored registry. MCP
servers, A2A agents and the AI gateway are pods behind Kubernetes Services, autoscaled by KEDA (D411, D412, D417).

**Network.** One ingress or API gateway per cluster with TLS, rate limits and a web application firewall; every service
private behind it; network policies between namespaces; customers' sites (F18) behind a European CDN; outbound calls of
connectors and scrapers through controlled egress proxies.

**Hosted clusters.** One region per cluster, in France first, a second region for disaster recovery; up to 5 000
companies per cluster (D405); GPU node pools only where AI needs them; Terraform modules per cloud behind one interface.

**Overview.** One cluster, as specified (not built yet):

```mermaid
flowchart TB
    subgraph Cluster[Kubernetes, self-managed or a European managed offer]
        IN[Ingress or API gateway: TLS, rate limits, web application firewall] --> SV[Services, private]
        SV --> MCP[MCP servers, A2A agents, AI gateway: pods autoscaled by KEDA]
        SV --> DATA[Operators: CloudNativePG, S3-compatible objects, OpenBao, Milvus, event bus, workflow engine]
        SV --> EG[Egress proxies for connectors and scrapers]
    end
    CDN[European CDN for customers' sites] --> IN
    DATA -. may be replaced by configuration .-> MAN[The cloud's managed PostgreSQL, objects and KMS]
    TF[Terraform modules per cloud] --> Cluster
    PKG[Helm charts, or Docker Compose on one server] --> Cluster
```

Decided in [D421](../../specs/06-decisions/technical/d421-infrastructure-cncf.md).

Last reviewed: 2026-11-12 (GH-2)

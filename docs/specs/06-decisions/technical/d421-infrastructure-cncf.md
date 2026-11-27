🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D421 Infrastructure: fully CNCF compatible

# 📜 D421 Infrastructure: fully CNCF compatible

**Status:** ✅ decided

## Context

Step 19za of the technical interview (PLAN D35). The owner: "This project MUST BE FULLY CNCF compatible. It MUST WORK
for both self-managed and Managed Kubernetes on European Cloud."

## Options

- Managed Kubernetes on European clouds, or self-managed Kubernetes.
- Compose for one server and Helm for clusters, or Helm only.
- One gateway with private services, or services exposed directly.
- Operators by default with managed services optional, or always in the cluster.

## Choice

Confirmed by the owner on 2026-11-12: fully CNCF compatible, working on self-managed and on managed Kubernetes of
European clouds; Compose and Helm supported everywhere; one gateway with private services; operators by default, a
cloud's managed services optional by configuration, never required.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The infrastructure chapter's target design.

## Related

- [Infrastructure: fully CNCF compatible](../../../technical/infrastructure/infrastructure.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D420 DevOps practice](d420-devops-practice.md) · ⬆️ [Up](README.md) ·
➡️ [D422 Backups and recovery targets](d422-backups-and-recovery.md)

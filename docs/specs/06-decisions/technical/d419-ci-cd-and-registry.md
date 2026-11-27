🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D419 CI/CD and the image registry

# 📜 D419 CI/CD and the image registry

**Status:** ✅ decided

## Context

Step 19j of the technical interview; the pipeline order is fixed in AGENT.md.

## Options

- GitHub Actions with a European registry.
- A self-hosted CI.

## Choice

Confirmed by the owner on 2026-11-12: GitHub Actions; signed images in a European container registry, mirrored to
GitHub's registry for self-hosters; dev and QA stages ephemeral as today. The owner: "This project MUST BE FULLY CNCF
compatible. It MUST WORK for both self-managed and Managed Kubernetes on European Cloud." The owner: "Both Compose &
Helm supported everywhere."

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The CI/CD and deployment chapters' target design.

## Related

- [CI/CD and the image registry](../../../technical/delivery/ci-cd-and-stages.md)
- [CI/CD and the image registry](../../../technical/infrastructure/deployment.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D418 Open points of F17 to F21](../vision/d418-open-points-of-f17-to-f21.md) · ⬆️ [Up](README.md) ·
➡️ [D420 DevOps practice](d420-devops-practice.md)

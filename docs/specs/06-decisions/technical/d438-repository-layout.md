🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D438 Repository layout

# 📜 D438 Repository layout

**Status:** ✅ decided

## Context

Step 19zb of the technical interview (PLAN D39).

## Options

- backend/ and frontend/, or AGENT.md's services/, frontends/ and packages/.
- Shared models in one library, or every model shared.
- Plugins and the SDK together, or apart.
- Deployment files under deploy/ or infra/.

## Choice

Confirmed by the owner on 2026-11-12: "I want a mono-repo: with backend and frontend separated"; each back-end
micro-service layered (models, storage with the repositories, service with the business logic, api); shared components
as libraries under backend/shared/; the shared Pydantic models directly under backend/models/, used by the services,
plugins/ and sdk/; plugins/ and sdk/ separate; infra/ for Compose, Helm and Terraform.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The repository layout chapter; AGENT.md and the conventions tests follow in a harness ticket.

## Related

- [Repository layout](../../../technical/architecture/repository-layout.md)

---

⬅️ [D437 DevOps agents live in the CI](../f25-devops-agents/d437-devops-agents-in-the-ci.md) · ⬆️ [Up](README.md) ·
➡️ [D439 AI autonomy tiers per feature](../f03-assistant/d439-ai-autonomy-tiers.md)

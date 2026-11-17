🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) › 📜 D412 A2A agents

# 📜 D412 A2A agents

**Status:** ✅ decided

## Context

Step 19y of the technical interview (PLAN D35), from TC-07.

## Options

- Agent cards per domain, or one agent.
- Allow-listed outside agents, or open discovery.
- Signed cards and mutual TLS, or OAuth only.
- The same tools and rules for every agent, or the in-app assistant apart.

## Choice

Confirmed by the owner on 2026-11-12: agent cards per domain with skills from the use cases, "each A2A agent will be a
pod deployed with KEDA behind a k8s service"; allow-listed outside agents with rights passed down; signed cards and
mutual TLS for partners; the same tools and rules for every agent.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The A2A chapter's target design.

## Related

- [A2A agents](../../../technical/interfaces/a2a.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D411 MCP server and client](d411-mcp-server-and-client.md) · ⬆️ [Up](README.md) ·
➡️ [D413 Configuration layers](d413-configuration-layers.md)

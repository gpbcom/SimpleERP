🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D411 MCP server and client

# 📜 D411 MCP server and client

**Status:** ✅ decided

## Context

Step 19x of the technical interview (PLAN D35), from TC-07.

## Options

- One endpoint with tools from OpenAPI, or one endpoint per module.
- Writes confirmed, or trust the outside client.
- Remote and sandboxed local outside servers, or remote only.
- Tool search, or every tool at once.

## Choice

Confirmed by the owner on 2026-11-12: one endpoint, tools generated from OpenAPI, and "each MCP will be a pod deployed
with KEDA behind a k8s service"; writes confirmed, irreversible acts always; remote outside servers and sandboxed local
ones; tool search and groups.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The MCP chapter's target design.

## Related

- [MCP server and client](../../../technical/interfaces/mcp.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D410 API style and authentication](d410-api-style-and-auth.md) · ⬆️ [Up](README.md) ·
➡️ [D412 A2A agents](d412-a2a-agents.md)

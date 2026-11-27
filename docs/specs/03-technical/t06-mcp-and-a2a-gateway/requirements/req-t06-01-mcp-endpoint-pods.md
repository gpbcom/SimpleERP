🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T06-01 One MCP endpoint, pods per domain

# 📌 REQ-T06-01 One MCP endpoint, pods per domain

**Status:** ✅ specified

## Statement

One public MCP endpoint routes to MCP servers per business domain, each a pod behind a Kubernetes Service, autoscaled by
KEDA.

## Why

Confirmed by the owner on 2026-11-12; D411.

## Acceptance criteria

1. **Given** load rises, KEDA adds pods.
2. **Given** no load, pods scale down.

## Measure

Scale-up time.

## Priority

Must

## Capabilities served

F3

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T06-02 Tools from OpenAPI, tool search](req-t06-02-tools-from-openapi.md)

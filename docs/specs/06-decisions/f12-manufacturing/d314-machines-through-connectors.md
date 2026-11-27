🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: F12 Manufacturing (plugin)](README.md) ›
📜 D314 Machines through connectors

# 📜 D314 Machines through connectors

**Status:** ✅ decided

## Context

How machines, PLCs and sensors reach F12.

## Options

- Through T12 connectors.
- Manual entry only in v1.

## Choice

Machines, PLCs and sensors (OPC UA, MQTT, gateways), scales and label printers are T12 connectors: counts, times and
stops flow in; a new one needs no F12 change. Manual entry stays possible and is marked as such.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

UC-F12-13, UC-F12-14; BR-F12-08.

## Related

- [F12 Manufacturing](../../02-functional/f12-manufacturing/README.md)

---

⬅️ [D313 Manufacturing personas](d313-manufacturing-personas.md) · ⬆️ [Up](README.md) ·
➡️ [D315 F12 use cases](d315-f12-use-cases.md)

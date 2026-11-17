🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-02 Static workflow mode

# 📌 REQ-T12-02 Static workflow mode

**Status:** ✅ specified

## Statement

A workflow (F2) calls connector actions in fixed steps, with conditions and approvals; no model decides the
path.

## Why

Some processes must be fully predictable
([D238](../../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md)).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A refund workflow runs the same steps for the same inputs; every step is logged.

## Measure

Share of runs reproducible.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-01 Connector catalogue](req-t12-01-connector-catalogue.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-03 Agentic mode](req-t12-03-agentic-mode.md)

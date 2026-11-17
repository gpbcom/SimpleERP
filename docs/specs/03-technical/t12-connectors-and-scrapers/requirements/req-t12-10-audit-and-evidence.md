🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-10 Audit and evidence

# 📌 REQ-T12-10 Audit and evidence

**Status:** ✅ specified

## Statement

Every connector action logs who or which agent ran it, for which request, inputs with secrets redacted,
outputs, duration, cost, and for browser writes a screenshot; logs feed T3's audit trail and F16's monitoring.

## Why

Automatic actions on customers' accounts must be explainable.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

An automatic refund shows its procedure, reasoning, action and evidence.

## Measure

Actions with complete logs.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-09 Sandbox for connectors and generated code](req-t12-09-sandbox-isolation.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-11 Health and drift](req-t12-11-health-and-drift.md)

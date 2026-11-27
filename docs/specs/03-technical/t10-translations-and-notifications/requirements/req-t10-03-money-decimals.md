🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🌐 [T10 Translations and notifications](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T10-03 Money as exact decimals

# 📌 REQ-T10-03 Money as exact decimals

**Status:** ✅ specified

## Statement

Money is an exact decimal with its currency; rates and rounding follow the country pack.

## Why

Confirmed by the owner on 2026-11-12; D293.

## Acceptance criteria

1. **Given** a conversion, rounded as the pack says.
2. **Given** a sum of lines, no float error.

## Measure

Rounding tests.

## Priority

Must

## Capabilities served

F6 to F8, F13, F22

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T10-02 Legal documents exact](req-t10-02-legal-documents-exact.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T10-04 One notification service](req-t10-04-one-notification-service.md)

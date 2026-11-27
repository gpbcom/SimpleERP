🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🌐 [T10 Translations and notifications](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T10-06 Mail delivery records checked

# 📌 REQ-T10-06 Mail delivery records checked

**Status:** ✅ specified

## Statement

SPF, DKIM and DMARC are checked for sending domains.

## Why

Confirmed by the owner on 2026-11-12; D385.

## Acceptance criteria

1. **Given** a record missing, alert.
2. **Given** records valid, mail delivered.

## Measure

Delivery rate.

## Priority

Must

## Capabilities served

F18

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T10-05 From events, grouped](req-t10-05-events-to-digests.md) · ⬆️ [Up](README.md)

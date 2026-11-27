🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🌐 [T10 Translations and notifications](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T10-05 From events, grouped

# 📌 REQ-T10-05 From events, grouped

**Status:** ✅ specified

## Statement

Notifications come from events, deduplicated and grouped into digests.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** ten similar events, one message.
2. **Given** a digest chosen, sent daily.

## Measure

Messages per user.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T10-04 One notification service](req-t10-04-one-notification-service.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T10-06 Mail delivery records checked](req-t10-06-mail-records.md)

🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🌐 [T10 Translations and notifications](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T10-04 One notification service

# 📌 REQ-T10-04 One notification service

**Status:** ✅ specified

## Statement

One service sends in-app, email, chat (Matrix) and push messages, with each user's preferences.

## Why

Confirmed by the owner on 2026-11-12; D92.

## Acceptance criteria

1. **Given** a user prefers chat, sent there.
2. **Given** a channel down, fallback.

## Measure

Delivery rate.

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

⬅️ [REQ-T10-03 Money as exact decimals](req-t10-03-money-decimals.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T10-05 From events, grouped](req-t10-05-events-to-digests.md)

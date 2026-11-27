🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-18 Meeting capture

# 📌 REQ-T12-18 Meeting capture

**Status:** ✅ specified

## Statement

Meetings come from the platforms' own transcripts through the user's linked account (the official APIs of Meet, Teams
and Zoom) and from a self-hosted recorder bot that joins as a participant named "SimpleERP recorder" and posts a notice
in the chat; any participant can stop it; speakers are named from the platform's participant names, never from voice
prints; recordings stay in the company's storage.

## Why

Confirmed by the owner on 2026-11-12; D7, D23; TC-10; the review of 2026-11-12 (R14).

## Acceptance criteria

1. **Given** a Teams meeting with the bot invited, the notice is posted and the transcript lands on the meeting record.
2. **Given** a participant asks the bot to leave, it stops recording and leaves.

## Measure

Meetings captured per platform; stops honoured.

## Priority

Must

## Capabilities served

F4, F16

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T12-17 Connector contract tests daily](req-t12-17-contract-tests-daily.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-19 E-invoicing platform connectors](req-t12-19-e-invoicing-platforms.md)

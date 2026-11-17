🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-11 Health and drift

# 📌 REQ-T12-11 Health and drift

**Status:** ✅ specified

## Statement

Each connector has health checks; a scraper whose results drop below its usual completeness, or whose page
structure changes, is flagged and a regeneration is proposed through the factory; failing connectors pause the intents
that need them (back to human).

## Why

Outside systems change without notice.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A portal redesign pauses its intents and proposes a new connector.

## Measure

Time to detect drift.

## Priority

Should

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-10 Audit and evidence](req-t12-10-audit-and-evidence.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-12 Lawful collection](req-t12-12-lawful-collection.md)

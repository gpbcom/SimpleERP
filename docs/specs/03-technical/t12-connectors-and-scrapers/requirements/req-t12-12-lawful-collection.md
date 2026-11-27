🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-12 Lawful collection

# 📌 REQ-T12-12 Lawful collection

**Status:** ✅ specified

## Statement

Browser automation acts only on the company's own accounts with its consent; public scraping respects the
site's terms, robots rules, database rights and GDPR; personal data collected is minimised and kept as the data's
purpose requires.

Public scraping never uses stealth fetching or disguised browsers (REQ-T12-07).

## Why

Scraping can breach contracts or rights.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A public scraper on a site forbidding it is not activated.

## Measure

Activations with a legal check.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-11 Health and drift](req-t12-11-health-and-drift.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-13 Target discovery](req-t12-13-target-discovery.md)

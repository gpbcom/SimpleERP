🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-07 Fetch ladder

# 📌 REQ-T12-07 Fetch ladder

**Status:** ✅ specified

## Statement

Pages are fetched with the lightest rung that works: plain HTTP, then a headless browser, served by a
self-hosted fetch service (MCP); a stealth browser only for the company's own accounts on tools without an API
(REQ-T12-05), never for public scraping; per-site rate limits and concurrency; the site's terms and robots
rules checked before a public scraper is activated.

## Why

Sites differ; heavy rungs cost more.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A static site uses HTTP; a JavaScript app climbs to the browser.

## Measure

Share per rung.

## Priority

Should

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-06 Scraper and connector factory](req-t12-06-scraper-factory.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-08 Credentials stored safely](req-t12-08-credential-vault.md)

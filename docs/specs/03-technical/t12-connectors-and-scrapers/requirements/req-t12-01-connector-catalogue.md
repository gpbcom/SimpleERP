🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-01 Connector catalogue

# 📌 REQ-T12-01 Connector catalogue

**Status:** ✅ specified

## Statement

Connectors cover every outside system the agents and workflows need, by category: helpdesks (Zendesk,
Intercom, HubSpot, Freshdesk, Notion); channels (IMAP and SMTP, Gmail and Microsoft Graph mail, web forms, chat widget,
WhatsApp Business, SMS, voice over SIP); CRMs; payment providers (refunds, deposits, disputes); e-commerce platforms
(orders, returns); carriers (tracking, claims); banks through PSD2 aggregators; e-invoicing platforms (Q13);
e-signature; calendars and storage; and back-office tools with no API (insurance policy systems, order systems, legacy
portals) through browser automation.

## Why

Every resolution needs data and actions in the company's own tools.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

Each category has at least one connector, or the factory can generate one (REQ-T12-06).

## Measure

Connectors available per category.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T12-02 Static workflow mode](req-t12-02-static-workflow-mode.md)

🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 🔌 [Interfaces](README.md) › 🔌 I-T12-06 E-invoicing platform connector

# 🔌 I-T12-06 E-invoicing platform connector

**Status:** ✅ specified

## Contract

One contract every platform adapter implements: connect a company and its SIRETs, look up a buyer in the directory,
submit an invoice, receive invoices, receive and send lifecycle statuses (signed webhooks, polling as a fallback), send
the e-reporting data. Adapters: Super PDP, B2Brouter, AFNOR XP Z12-013 (generic), Chorus Pro. Field-level schemas are
generated from the code (D406).

## Used by

F8, F6, F7

## Rules

Rights (T2), audit (T3), problem+json errors (D410), secrets in the vault (REQ-T12-08).

## Open questions

None.

---

⬅️ [I-T12-05 Scraper factory runs](i-t12-05-scraper-factory-runs.md) · ⬆️ [Up](README.md)

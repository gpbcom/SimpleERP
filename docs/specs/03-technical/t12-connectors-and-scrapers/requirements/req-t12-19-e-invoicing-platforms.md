🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-19 E-invoicing platform connectors

# 📌 REQ-T12-19 E-invoicing platform connectors

**Status:** ✅ specified

## Statement

simple-ERP sends and receives e-invoices, their statuses and the e-reporting data through a Super PDP adapter, a
B2Brouter adapter, one generic AFNOR XP Z12-013 adapter and Chorus Pro for public buyers; more adapters are added on
demand. A company connects its platform in the fewest steps, may use one to issue and another to receive, and may change
at any time.

## Why

Confirmed by the owner on 2026-11-12 ([D454](../../../06-decisions/f08-accounting/d454-e-invoicing-platforms.md));
France's e-invoicing reform.

## Acceptance criteria

1. **Given** a validated invoice to a company **when** it is sent **then** its Factur-X, UBL or CII file reaches the
   company's platform and the platform's id is kept.
2. **Given** the platform rejects a file **then** its message shows on the invoice, which is not marked sent.
3. **Given** a supplier invoice on the platform **then** it becomes a draft purchase invoice.
4. **Given** a lifecycle status (200 to 213) **when** its webhook does not arrive **then** polling picks it up.
5. **Given** a public buyer **then** the invoice goes through Chorus Pro.
6. **Given** a platform offering AFNOR XP Z12-013 and no adapter of its own **when** its contract tests pass in its
   sandbox **then** it is connected through the generic adapter.
7. **Given** a company changes platform **then** new flows go to the new one and the history stays.

## Measure

Invoices accepted at the first submission; the delay between a status and its display.

## Priority

Must

## Capabilities served

F8, F6, F7, F24

## Tests

Contract tests daily against each platform's sandbox (REQ-T12-17); the pilot through B2Brouter's test staging connected
to the DGFiP's.

## Open questions

None. What is still to check is listed on the
[e-invoicing platforms](../../../05-non-functional/e-invoicing-platforms.md) page.

---

⬅️ [REQ-T12-18 Meeting capture](req-t12-18-meeting-capture.md) · ⬆️ [Up](README.md)

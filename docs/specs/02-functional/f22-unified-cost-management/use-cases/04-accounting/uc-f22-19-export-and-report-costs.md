🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-04 Accounting](README.md) › 📝 UC-F22-19 Export and report costs

# 📝 UC-F22-19 Export and report costs

**Status:** ✅ specified

## Summary

Accounting and the owner export and report costs, KPIs included.

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Reports.

## Trigger

Month.

## Frequency

Monthly.

## Preconditions

- Costs.

## Postconditions

- Success: exported.
- Failure: none.

## Main flow

1. Choose (S-F22-19).
2. Export.
3. Share.
4. KPIs (UC-F22-24).

## Alternative flows

- 2a. PDF.

## Error flows

- 2e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-02 Every paid call is metered](../../business-rules/br-f22-02-every-paid-call-metered.md)

## Entities

- [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md)
- [E-F22-11 Forecast](../../data/e-f22-11-forecast.md)

## Permissions

Accounting, owner.

## Notifications

- None.

## Audit events

Exports.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-19 Cost reports](../../screens/04-accounting/s-f22-19-cost-reports.md)

## Flowchart

See [FL-F22-04 Accounting](../../flows/fl-f22-04-accounting.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Accounting
  participant S as Reports
  A->>S: November CSV
```

## Acceptance criteria

1. **Given** November **when** exported **then** CSV.
2. **Given** PDF **when** exported **then** PDF.
3. **Given** KPIs **when** included **then** shown.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Billing and accounting rules of the France country pack:
[CR-FR-015 Mandatory invoice mentions](../../../../10-country-packs/france/invoicing/cr-fr-015-invoice-mandatory-mentions.md),
[CR-FR-016 Electronic invoicing](../../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md),
[CR-FR-100 VAT on services to clients abroad](../../../../10-country-packs/france/tax-and-vat/cr-fr-100-vat-on-services-abroad.md),
[CR-FR-002 Accounting records kept 10 years](../../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md),
[CR-FR-202 Price reductions on invoices](../../../../10-country-packs/france/invoicing/cr-fr-202-price-reductions-on-invoices.md),
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md).

## Related use cases

- [UC-F22-24 Read the cost KPIs](../06-savings-and-kpis/uc-f22-24-read-the-cost-kpis.md)

## Open questions

None.

---

⬅️ [UC-F22-18 Spot anomalies and runaway agents](../03-runs/uc-f22-18-spot-anomalies-and-runaway-agents.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F22-20 Ask the AI assistant about costs](../01-see-and-set-up/uc-f22-20-ask-the-assistant-about-costs.md)

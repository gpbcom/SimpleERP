🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-03 Runs](README.md) › 📝 UC-F22-11 Follow a run's cost live and stop it

# 📝 UC-F22-11 Follow a run's cost live and stop it

**Status:** ✅ specified

## Summary

The administrator follows a run's cost live and stops it.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Control.

## Trigger

Run.

## Frequency

Occasional.

## Preconditions

- Run.

## Postconditions

- Success: stopped or done.
- Failure: none.

## Main flow

1. Watch (S-F22-11).
2. Stop.
3. Kept done (BR-F22-07).
4. Resume later.

## Alternative flows

- 2a. Let it finish.

## Error flows

- 2e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-07 Runs stop cleanly](../../business-rules/br-f22-07-runs-stop-cleanly.md)
- [BR-F22-02 Every paid call is metered](../../business-rules/br-f22-02-every-paid-call-metered.md)

## Entities

- [E-F22-10 Run estimate](../../data/e-f22-10-run-estimate.md)
- [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md)

## Permissions

Administrator.

## Notifications

- None.

## Audit events

Runs.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-11 Live run](../../screens/03-runs/s-f22-11-live-run.md)

## Flowchart

See [FL-F22-03 Runs](../../flows/fl-f22-03-runs.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Live run
  A->>S: Stop at 12.40 EUR
```

## Acceptance criteria

1. **Given** 12.40 EUR **when** stopped **then** step finished.
2. **Given** resume **when** resumed **then** continues.
3. **Given** done **when** finished **then** cost final.

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

- [UC-F22-10 Estimate a run before it starts](uc-f22-10-estimate-a-run-before-it-starts.md)

## Open questions

None.

---

⬅️ [UC-F22-10 Estimate a run before it starts](uc-f22-10-estimate-a-run-before-it-starts.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F22-12 Forecast the month's costs](../04-accounting/uc-f22-12-forecast-the-month-s-costs.md)

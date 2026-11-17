🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-02 Budgets and stops](README.md) › 📝 UC-F22-07 Receive warnings at thresholds

# 📝 UC-F22-07 Receive warnings at thresholds

**Status:** ✅ specified

## Summary

The owner and administrator receive warnings at thresholds.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Act before the stop.

## Trigger

Threshold.

## Frequency

Occasional.

## Preconditions

- Budgets.

## Postconditions

- Success: warned.
- Failure: none.

## Main flow

1. Threshold reached.
2. Warning sent once (BR-F22-05).
3. Open details (S-F22-07).
4. Act.

## Alternative flows

- 4a. Raise (UC-F22-09).

## Error flows

- 2e. Sending fails: in-app.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-05 Warnings at thresholds](../../business-rules/br-f22-05-warn-at-thresholds.md)

## Entities

- [E-F22-06 Cost budget](../../data/e-f22-06-cost-budget.md)
- [E-F22-07 Cost alert](../../data/e-f22-07-cost-alert.md)

## Permissions

Owner, administrator.

## Notifications

- Warning.

## Audit events

Warnings.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-07 Budget warnings](../../screens/02-budgets-and-stops/s-f22-07-budget-warnings.md)

## Flowchart

See [FL-F22-02 Budgets and stops](../../flows/fl-f22-02-budgets-and-stops.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant B as Budgets
  actor O as Owner
  B-->>O: F17 at 82 percent
```

## Acceptance criteria

1. **Given** 82 % **when** reached **then** one warning.
2. **Given** 85 % **when** reached **then** none again.
3. **Given** failed email **when** sent **then** in-app.

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

- [UC-F22-09 Raise a budget or approve a run](uc-f22-09-raise-a-budget-or-approve-a-run.md)

## Open questions

None.

---

⬅️ [UC-F22-06 Set budgets at every level](uc-f22-06-set-budgets-at-every-level.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F22-08 Stop paid calls at 100 %, legal duties kept](uc-f22-08-stop-paid-calls-at-100-legal-duties-kept.md)

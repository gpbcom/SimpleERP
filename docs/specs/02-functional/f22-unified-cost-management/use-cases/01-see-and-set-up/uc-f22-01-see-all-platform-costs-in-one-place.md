🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-01 See and set up](README.md) › 📝 UC-F22-01 See all platform costs in one place

# 📝 UC-F22-01 See all platform costs in one place

**Status:** ✅ specified

## Summary

The owner and accounting see all platform costs in one place for a period, including self-hosted compute and
foreign-currency providers converted, and drill down.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Goal

One view of what the platform costs.

## Trigger

Any time.

## Frequency

Weekly.

## Preconditions

- Usage metered.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. Open the Costs overview (S-F22-01).
2. Choose the period.
3. Read the total and its parts (paid providers, local compute).
4. Drill down to a feature.

## Alternative flows

- 3a. Foreign amounts shown on demand.

## Error flows

- 1e. No usage: said.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-02 Every paid call is metered](../../business-rules/br-f22-02-every-paid-call-metered.md)
- [BR-F22-14 Foreign prices converted at the day's rate](../../business-rules/br-f22-14-foreign-prices-converted-at-the-days-rate.md)
- [BR-F22-15 Self-hosted compute has a cost](../../business-rules/br-f22-15-self-hosted-compute-has-a-cost.md)

## Entities

- [E-F22-01 Cost period](../../data/e-f22-01-cost-period.md)
- [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md)
- [E-F22-14 Exchange rate](../../data/e-f22-14-exchange-rate.md)
- [E-F22-15 Compute machine](../../data/e-f22-15-compute-machine.md)

## Permissions

Owner, accounting; managers their team.

## Notifications

- None.

## Audit events

None.

## AI involvement

Explains.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-01 Costs overview](../../screens/01-see-and-set-up/s-f22-01-costs-overview.md)

## Flowchart

See [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Costs overview
  O->>S: November
  S-->>O: 312.40 EUR, local 72.60
```

## Acceptance criteria

1. **Given** November **when** opened **then** 312.40 EUR with parts.
2. **Given** USD providers **when** shown **then** converted with USD on demand.
3. **Given** no usage **when** opened **then** said.

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

- [UC-F22-02 See costs per module, feature and provider](uc-f22-02-see-costs-per-module-feature-and-provider.md)
- [UC-F22-24 Read the cost KPIs](../06-savings-and-kpis/uc-f22-24-read-the-cost-kpis.md)

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [UC-F22-02 See costs per module, feature and provider](uc-f22-02-see-costs-per-module-feature-and-provider.md)

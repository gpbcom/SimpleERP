🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-01 See and set up](README.md) › 📝 UC-F22-04 Register a paid provider and its prices

# 📝 UC-F22-04 Register a paid provider and its prices

**Status:** ✅ specified

## Summary

The administrator registers a paid provider and its prices with dates, in its currency.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Costs computed right.

## Trigger

New provider.

## Frequency

Rare.

## Preconditions

- None.

## Postconditions

- Success: saved.
- Failure: refused.

## Main flow

1. Open (S-F22-04).
2. Add provider.
3. Enter prices, currency and dates (BR-F22-03).
4. Save.

## Alternative flows

- 3a. Foreign currency (UC-F22-21).

## Error flows

- 3e. Overlapping dates: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-03 Prices versioned per provider](../../business-rules/br-f22-03-prices-versioned-per-provider.md)
- [BR-F22-14 Foreign prices converted at the day's rate](../../business-rules/br-f22-14-foreign-prices-converted-at-the-days-rate.md)

## Entities

- [E-F22-03 Provider price list](../../data/e-f22-03-provider-price-list.md)
- [E-F22-04 Paid provider](../../data/e-f22-04-paid-provider.md)
- [E-F22-14 Exchange rate](../../data/e-f22-14-exchange-rate.md)

## Permissions

Administrator.

## Notifications

- None.

## Audit events

Changes.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-04 Providers](../../screens/01-see-and-set-up/s-f22-04-providers.md)

## Flowchart

See [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Providers
  A->>S: Provider A, 0.006 per 1 000 tokens from 2026-11-01
```

## Acceptance criteria

1. **Given** prices from 2026-11-01 **when** saved **then** used from then.
2. **Given** overlapping dates **when** saved **then** refused.
3. **Given** USD **when** saved **then** converted daily.

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

- [UC-F22-21 Record a provider's prices in a foreign currency](uc-f22-21-record-a-providers-prices-in-a-foreign-currency.md)

## Open questions

None.

---

⬅️ [UC-F22-03](../04-accounting/uc-f22-03-see-costs-per-department-project-and-client.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F22-05 Bring own keys or use the hosted quota](uc-f22-05-bring-own-keys-or-use-the-hosted-quota.md)

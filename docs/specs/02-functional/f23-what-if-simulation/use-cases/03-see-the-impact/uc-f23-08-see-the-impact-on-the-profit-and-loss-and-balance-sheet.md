🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F23-03 See the impact](README.md) ›
📝 UC-F23-08 See the impact on the profit and loss and balance sheet

# 📝 UC-F23-08 See the impact on the profit and loss and balance sheet

**Status:** ✅ specified

## Summary

Accounting sees the impact on the profit and loss and balance sheet.

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Goal

Statements foreseen.

## Trigger

Run.

## Frequency

Quarterly.

## Preconditions

- Run.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. Open (S-F23-08).
2. Compare (BR-F23-01).
3. Export.
4. Share with the accountant.

## Alternative flows

- 3a. PDF.

## Error flows

- 1e. Not run.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F23-01 Legal values from the country pack](../../business-rules/br-f23-01-legal-values-from-the-country-pack.md)
- [BR-F23-05 The impact across every area](../../business-rules/br-f23-05-impact-across-every-area.md)

## Entities

- [E-F23-05 Impact result](../../data/e-f23-05-impact-result.md)

## Permissions

Accounting.

## Notifications

- None.

## Audit events

Exports.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F23-08 Statements impact](../../screens/03-see-the-impact/s-f23-08-statements-impact.md)

## Flowchart

See [FL-F23-03 See the impact](../../flows/fl-f23-03-see-the-impact.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Accounting
  participant S as Statements
  A->>S: Open
  S-->>A: Profit -18 k
```

## Acceptance criteria

1. **Given** the scenario **when** read **then** profit -18 000.00 EUR.
2. **Given** export **when** done **then** file.
3. **Given** taxes **when** computed **then** from the pack.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Values of the France country pack read by scenarios:
[CR-FR-046 Headcount thresholds](../../../../10-country-packs/france/labour/cr-fr-046-headcount-thresholds.md),
[CR-FR-008 VAT rates](../../../../10-country-packs/france/tax-and-vat/cr-fr-008-vat-rates.md),
[CR-FR-185 Minimum wage (SMIC)](../../../../10-country-packs/france/payroll/cr-fr-185-minimum-wage.md),
[CR-FR-064 Accounting frameworks of the books](../../../../10-country-packs/france/accounting/cr-fr-064-accounting-frameworks.md),
[CR-FR-058 AI in recruitment and work is high-risk](../../../../10-country-packs/france/ai-and-recording/cr-fr-058-high-risk-ai-in-employment.md),
[CR-FR-057 A person confirms what the AI does](../../../../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md).

## Related use cases

- [UC-F23-29 Prepare a forecast pack for the bank](../06-goals-and-financing/uc-f23-29-prepare-a-forecast-pack-for-the-bank.md)

## Open questions

None.

---

⬅️ [UC-F23-07 See the impact on cash and treasury](uc-f23-07-see-the-impact-on-cash-and-treasury.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F23-09 See the impact on stock and purchases](uc-f23-09-see-the-impact-on-stock-and-purchases.md)

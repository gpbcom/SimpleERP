🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F23-03 See the impact](README.md) › 📝 UC-F23-10 See the impact on production and capacity

# 📝 UC-F23-10 See the impact on production and capacity

**Status:** ✅ specified

## Summary

The production planner sees the impact on production and capacity.

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Goal

No overload.

## Trigger

Run.

## Frequency

Monthly.

## Preconditions

- Run.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. Open (S-F23-10).
2. See overloads.
3. Options.
4. Simulate a shift (UC-F23-30).

## Alternative flows

- 2a. None.

## Error flows

- 1e. Not run.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F23-04 The same rules as the ERP](../../business-rules/br-f23-04-same-rules-as-the-erp.md)
- [BR-F23-05 The impact across every area](../../business-rules/br-f23-05-impact-across-every-area.md)

## Entities

- [E-F23-05 Impact result](../../data/e-f23-05-impact-result.md)

## Permissions

Production planner.

## Notifications

- None.

## Audit events

None.

## AI involvement

Explains.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F23-10 Capacity impact](../../screens/03-see-the-impact/s-f23-10-capacity-impact.md)

## Flowchart

See [FL-F23-03 See the impact](../../flows/fl-f23-03-see-the-impact.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor PL as Production planner
  participant S as Capacity impact
  PL->>S: Open
  S-->>PL: Line 2 at 118 percent in April
```

## Acceptance criteria

1. **Given** line 2 **when** read **then** 118 % in April.
2. **Given** options **when** shown **then** shift or subcontract.
3. **Given** none **when** read **then** said.

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

- [UC-F23-30 Simulate a new shift or machine](uc-f23-30-simulate-a-new-shift-or-machine.md)

## Open questions

None.

---

⬅️ [UC-F23-09 See the impact on stock and purchases](uc-f23-09-see-the-impact-on-stock-and-purchases.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F23-11](uc-f23-11-see-the-impact-on-staff-payroll-and-planning.md)

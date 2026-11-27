🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F23-01 Build a scenario](README.md) › 📝 UC-F23-04 Give uncertain inputs as ranges

# 📝 UC-F23-04 Give uncertain inputs as ranges

**Status:** ✅ specified

## Summary

Accounting and the treasurer give uncertain inputs as ranges.

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Goal

Realistic outcomes.

## Trigger

Uncertainty.

## Frequency

Monthly.

## Preconditions

- Changes.

## Postconditions

- Success: ranges saved.
- Failure: none.

## Main flow

1. Open Ranges (S-F23-04).
2. Set a range (BR-F23-07).
3. Choose the shape.
4. Save.

## Alternative flows

- 3a. Uniform.

## Error flows

- 2e. Min above max: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F23-07 Ranges for uncertain inputs](../../business-rules/br-f23-07-ranges-for-uncertain-inputs.md)

## Entities

- [E-F23-03 Scenario change](../../data/e-f23-03-scenario-change.md)

## Permissions

Accounting, treasurer.

## Notifications

- None.

## Audit events

Ranges.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F23-04 Ranges](../../screens/01-build-a-scenario/s-f23-04-ranges.md)

## Flowchart

See [FL-F23-01 Build a scenario](../../flows/fl-f23-01-build-a-scenario.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Accounting
  participant S as Ranges
  A->>S: 5 to 10 percent, likely 8
```

## Acceptance criteria

1. **Given** 5 to 10 % **when** saved **then** best and worst computed.
2. **Given** min above max **when** saved **then** refused.
3. **Given** a shape **when** chosen **then** used.

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

- [UC-F23-05 Run the scenario on a copy with the real rules](../02-run/uc-f23-05-run-the-scenario-on-a-copy-with-the-real-rules.md)

## Open questions

None.

---

⬅️ [UC-F23-03 Change one or several elements](uc-f23-03-change-one-or-several-elements.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F23-05](../02-run/uc-f23-05-run-the-scenario-on-a-copy-with-the-real-rules.md)

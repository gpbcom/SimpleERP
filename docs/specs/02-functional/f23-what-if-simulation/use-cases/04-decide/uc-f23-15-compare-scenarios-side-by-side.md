🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F23-04 Decide](README.md) › 📝 UC-F23-15 Compare scenarios side by side

# 📝 UC-F23-15 Compare scenarios side by side

**Status:** ✅ specified

## Summary

The owner compares scenarios side by side.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Choose.

## Trigger

Several scenarios.

## Frequency

Monthly.

## Preconditions

- Runs.

## Postconditions

- Success: chosen.
- Failure: none.

## Main flow

1. Pick (S-F23-15).
2. Compare.
3. Choose.
4. Share.

## Alternative flows

- 2a. With financing.

## Error flows

- 1e. Not run.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F23-05 The impact across every area](../../business-rules/br-f23-05-impact-across-every-area.md)

## Entities

- [E-F23-02 Scenario](../../data/e-f23-02-scenario.md)
- [E-F23-06 Sensitivity](../../data/e-f23-06-sensitivity.md)

## Permissions

Owner.

## Notifications

- None.

## Audit events

Choice.

## AI involvement

Explains.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F23-15 Comparison](../../screens/04-decide/s-f23-15-comparison.md)

## Flowchart

See [FL-F23-04 Decide](../../flows/fl-f23-04-decide.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Comparison
  O->>S: S-4 vs S-5
```

## Acceptance criteria

1. **Given** two **when** compared **then** side by side.
2. **Given** chosen **when** marked **then** saved.
3. **Given** not run **when** picked **then** said.

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

- [UC-F23-17 Turn a scenario into actions](../05-act-and-watch/uc-f23-17-turn-a-scenario-into-actions.md)

## Open questions

None.

---

⬅️ [UC-F23-14 See what matters most](uc-f23-14-see-what-matters-most.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F23-16 Get counter-measures proposed](uc-f23-16-get-counter-measures-proposed.md)

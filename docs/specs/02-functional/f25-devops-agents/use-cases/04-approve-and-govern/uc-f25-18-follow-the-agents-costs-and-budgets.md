🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-04 Approve and govern](README.md) › 📝 UC-F25-18 Follow the agents' costs and budgets

# 📝 UC-F25-18 Follow the agents' costs and budgets

**Status:** ✅ specified

## Summary

Agents' costs and budgets are followed.

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Control cost.

## Trigger

Monthly.

## Frequency

Monthly.

## Preconditions

- Runs.

## Postconditions

- Success: budgets set.
- Failure: none.

## Main flow

1. Open (S-F25-18).
2. Compare.
3. Set budgets (F22).
4. Save.

## Alternative flows

- 3a. Stop at budget.

## Error flows

- 2e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-11 Agents are metered and audited](../../business-rules/br-f25-11-agents-metered-and-audited.md)

## Entities

- [E-F25-10 Agent run](../../data/e-f25-10-agent-run.md)

## Permissions

Maintainer, hosting engineer.

## Notifications

- Budget warnings.

## Audit events

Budgets.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-18 Agent costs](../../screens/04-approve-and-govern/s-f25-18-agent-costs.md)

## Flowchart

See [FL-F25-04 Approve and govern](../../flows/fl-f25-04-approve-and-govern.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor H as Hosting engineer
  participant S as Agent costs
  H->>S: November 214 EUR
```

## Acceptance criteria

1. **Given** 214.00 EUR **when** read **then** per kind.
2. **Given** budget **when** set **then** warnings.
3. **Given** stop **when** reached **then** stops.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Rules of the France country pack the agents follow:
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md),
[CR-FR-199 Notifying a personal data breach](../../../../10-country-packs/france/data-protection/cr-fr-199-personal-data-breach-notification.md),
[CR-FR-056 People know they deal with an AI](../../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md),
[CR-FR-057 A person confirms what the AI does](../../../../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md),
[CR-FR-168 Cyber Resilience Act reporting](../../../../10-country-packs/france/digital/cr-fr-168-cyber-resilience-reporting.md),
[CR-FR-052 Personal data kept no longer than needed](../../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Related use cases

- [UC-F25-19 Measure the quality of the agents' work](uc-f25-19-measure-the-quality-of-the-agents-work.md)

## Open questions

None.

---

⬅️ [UC-F25-17 Control the agents' rights and audit](uc-f25-17-control-the-agents-rights-and-audit.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F25-19 Measure the quality of the agents' work](uc-f25-19-measure-the-quality-of-the-agents-work.md)

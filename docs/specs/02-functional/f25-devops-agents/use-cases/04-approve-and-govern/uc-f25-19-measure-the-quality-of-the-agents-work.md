🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-04 Approve and govern](README.md) › 📝 UC-F25-19 Measure the quality of the agents' work

# 📝 UC-F25-19 Measure the quality of the agents' work

**Status:** ✅ specified

## Summary

The maintainer measures the quality of the agents' work, spec checks included.

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Goal

Better agents.

## Trigger

Monthly.

## Frequency

Monthly.

## Preconditions

- Runs.

## Postconditions

- Success: improved.
- Failure: none.

## Main flow

1. Open (S-F25-19).
2. Read share approved first time and spec checks passed.
3. Find weak spots.
4. Improve prompts and tools.

## Alternative flows

- 2a. Per kind.

## Error flows

- 2e. Few runs.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-11 Agents are metered and audited](../../business-rules/br-f25-11-agents-metered-and-audited.md)
- [BR-F25-16 Agents' spec pull requests checked first](../../business-rules/br-f25-16-agents-spec-pull-requests-checked-first.md)

## Entities

- [E-F25-08 Approval](../../data/e-f25-08-approval.md)
- [E-F25-10 Agent run](../../data/e-f25-10-agent-run.md)
- [E-F25-13 Spec check report](../../data/e-f25-13-spec-check-report.md)

## Permissions

Maintainer.

## Notifications

- None.

## Audit events

None.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-19 Agent quality](../../screens/04-approve-and-govern/s-f25-19-agent-quality.md)

## Flowchart

See [FL-F25-04 Approve and govern](../../flows/fl-f25-04-approve-and-govern.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor M as Maintainer
  participant S as Agent quality
  M->>S: November
  S-->>M: 71 percent first time
```

## Acceptance criteria

1. **Given** 71 % **when** read **then** shown.
2. **Given** spec checks **when** counted **then** pass rate.
3. **Given** few runs **when** read **then** said.

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

- [UC-F25-23 Check an agent's spec pull request](../02-feature-requests/uc-f25-23-check-an-agents-spec-pull-request.md)

## Open questions

None.

---

⬅️ [UC-F25-18 Follow the agents' costs and budgets](uc-f25-18-follow-the-agents-costs-and-budgets.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F25-20](../05-tell-the-customer/uc-f25-20-ask-the-assistant-about-my-requests.md)

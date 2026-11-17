🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-01 First run](README.md) › 📝 UC-F21-12 Ask the AI assistant at any step

# 📝 UC-F21-12 Ask the AI assistant at any step

**Status:** ✅ specified

## Summary

The owner asks the AI assistant at any step.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Help when stuck.

## Trigger

Question.

## Frequency

Often.

## Preconditions

- None.

## Postconditions

- Success: answered.
- Failure: none.

## Main flow

1. Ask (S-F21-12).
2. Answer or fill (BR-F21-09).
3. Confirm.
4. Continue.

## Alternative flows

- 2a. From a document.

## Error flows

- 2e. Beyond rights: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-09 The AI assistant at every step](../../business-rules/br-f21-09-assistant-at-every-step.md)

## Entities

- [E-F21-01 Onboarding progress](../../data/e-f21-01-onboarding-progress.md)

## Permissions

Within rights.

## Notifications

- None.

## Audit events

Questions.

## AI involvement

Answers.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-12 Guide assistant](../../screens/01-first-run/s-f21-12-guide-assistant.md)

## Flowchart

See [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Guide assistant
  O->>S: What is a SIRET
  S-->>O: Answer
```

## Acceptance criteria

1. **Given** a question **when** asked **then** answer.
2. **Given** a document **when** given **then** filled.
3. **Given** beyond rights **when** asked **then** refused.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Set-up rules of the France country pack:
[CR-FR-001 Company identifiers](../../../../10-country-packs/france/company/cr-fr-001-company-identifiers.md),
[CR-FR-016 Electronic invoicing](../../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md),
[CR-FR-005 Accounting entries file (FEC)](../../../../10-country-packs/france/accounting/cr-fr-005-fec-export.md),
[CR-FR-038 Personnel register](../../../../10-country-packs/france/labour/cr-fr-038-personnel-register.md),
[CR-FR-048 Record of processing activities](../../../../10-country-packs/france/data-protection/cr-fr-048-record-of-processing.md),
[CR-FR-069 Website legal notices](../../../../10-country-packs/france/consumer/cr-fr-069-website-legal-notices.md).

## Related use cases

- [UC-F21-01 Start the first-run guide](uc-f21-01-start-the-first-run-guide.md)

## Open questions

None.

---

⬅️ [UC-F21-11 Follow a module's short guide](../02-modules/uc-f21-11-follow-a-module-s-short-guide.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F21-13](../04-learn-and-improve/uc-f21-13-try-with-demo-data-then-clear-it.md)

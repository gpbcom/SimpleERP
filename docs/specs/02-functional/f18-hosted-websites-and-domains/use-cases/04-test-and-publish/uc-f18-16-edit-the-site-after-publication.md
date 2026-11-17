🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-04 Test and publish](README.md) › 📝 UC-F18-16 Edit the site after publication

# 📝 UC-F18-16 Edit the site after publication

**Status:** ✅ specified

## Summary

Marketing edits the site after publication on the preview, with versions, then publishes.

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Goal

Changes safely.

## Trigger

A change.

## Frequency

Weekly.

## Preconditions

- Site live.

## Postconditions

- Success: published.
- Failure: draft kept.

## Main flow

1. Marketing opens Editor (S-F18-16).
2. They edit on the preview (BR-F18-03).
3. Checks run.
4. The owner publishes.

## Alternative flows

- 2a. ERP data changes update the preview.

## Error flows

- 3e. Failure: wait.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-03 Private preview first](../../business-rules/br-f18-03-preview-before-publication.md)
- [BR-F18-02 Built from the ERP's data](../../business-rules/br-f18-02-built-from-erp-data.md)

## Entities

- [E-F18-01 Hosted website](../../data/e-f18-01-hosted-website.md)
- [E-F18-02 Page](../../data/e-f18-02-page.md)

## Permissions

Marketing.

## Notifications

- The owner when ready.

## Audit events

Versions.

## AI involvement

The AI assistant writes texts.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-16 Editor](../../screens/04-test-and-publish/s-f18-16-editor.md)

## Flowchart

See [FL-F18-04 Test and publish](../../flows/fl-f18-04-test-and-publish.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor M as Marketing
  participant S as Editor
  M->>S: Edit
  S-->>M: Preview
```

## Acceptance criteria

1. **Given** an edit **when** saved **then** live unchanged.
2. **Given** checks pass **when** published **then** live.
3. **Given** ERP change **when** made **then** preview updates.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Website rules of the France country pack:
[CR-FR-069 Website legal notices](../../../../10-country-packs/france/consumer/cr-fr-069-website-legal-notices.md),
[CR-FR-070 Consent before cookies and trackers](../../../../10-country-packs/france/data-protection/cr-fr-070-cookie-consent.md),
[CR-FR-072 Accessible online shops](../../../../10-country-packs/france/consumer/cr-fr-072-web-accessibility-eaa.md),
[CR-FR-194 Rules for job offers](../../../../10-country-packs/france/labour/cr-fr-194-job-offer-rules.md),
[CR-FR-195 Candidates' personal data](../../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md),
[CR-FR-197 Who may hold a .fr domain](../../../../10-country-packs/france/digital/cr-fr-197-fr-domain-eligibility.md),
[CR-FR-058 AI in recruitment and work is high-risk](../../../../10-country-packs/france/ai-and-recording/cr-fr-058-high-risk-ai-in-employment.md),
[CR-FR-063 Consent for email and SMS marketing](../../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md).

## Related use cases

- [UC-F18-15 Approve, publish and roll back](uc-f18-15-approve-publish-and-roll-back.md)

## Open questions

None.

---

⬅️ [UC-F18-15 Approve, publish and roll back](uc-f18-15-approve-publish-and-roll-back.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-17](../01-build-the-site/uc-f18-17-offer-the-site-in-several-languages.md)

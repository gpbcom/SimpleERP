🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-04 Test and publish](README.md) › 📝 UC-F18-15 Approve, publish and roll back

# 📝 UC-F18-15 Approve, publish and roll back

**Status:** ✅ specified

## Summary

The owner approves and publishes after the checks, and can roll back to the previous version.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Controlled publication.

## Trigger

Checks passed.

## Frequency

Each publication.

## Preconditions

- Checks passed.

## Postconditions

- Success: live.
- Failure: refused.

## Main flow

1. The owner opens Publication (S-F18-15).
2. They approve (BR-F18-05).
3. The site is live.
4. They can roll back.

## Alternative flows

- 4a. Older versions from backups (UC-F18-27).

## Error flows

- 2e. Checks failed: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-05 The customer approves; rollback kept](../../business-rules/br-f18-05-customer-approves-rollback-kept.md)
- [BR-F18-04 Automatic checks gate publication](../../business-rules/br-f18-04-checks-gate-publication.md)

## Entities

- [E-F18-01 Hosted website](../../data/e-f18-01-hosted-website.md)
- [E-F18-10 Publication check report](../../data/e-f18-10-publication-check-report.md)

## Permissions

Owner; granted roles.

## Notifications

- Owner and marketing on publish.

## Audit events

Publications.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-15 Publication](../../screens/04-test-and-publish/s-f18-15-publication.md)

## Flowchart

See [FL-F18-04 Test and publish](../../flows/fl-f18-04-test-and-publish.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Publication
  O->>S: Publish v13
  S-->>O: Live
```

## Acceptance criteria

1. **Given** checks passed **when** published **then** live.
2. **Given** failed **when** published **then** refused.
3. **Given** a rollback **when** chosen **then** v12 is live.

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

- [UC-F18-27 Back up and restore the site](../05-run-the-site/uc-f18-27-back-up-and-restore-the-site.md)

## Open questions

None.

---

⬅️ [UC-F18-14 Run the automatic checks](uc-f18-14-run-the-automatic-checks.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-16 Edit the site after publication](uc-f18-16-edit-the-site-after-publication.md)

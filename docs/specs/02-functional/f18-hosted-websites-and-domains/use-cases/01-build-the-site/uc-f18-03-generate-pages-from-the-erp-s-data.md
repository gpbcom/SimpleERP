🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-01 Build the site](README.md) › 📝 UC-F18-03 Generate pages from the ERP's data

# 📝 UC-F18-03 Generate pages from the ERP's data

**Status:** ✅ specified

## Summary

Marketing generates pages from the ERP's data: products, services, about, sites and team, then edits their text.

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Goal

Pages that stay true to the ERP.

## Trigger

The builder.

## Frequency

Rare.

## Preconditions

- ERP data.

## Postconditions

- Success: pages on the preview.
- Failure: missing data listed.

## Main flow

1. Marketing opens Pages (S-F18-03).
2. They choose pages.
3. simple-ERP generates them (BR-F18-02).
4. They edit texts.

## Alternative flows

- 2a. Sector template pages (UC-F18-25).

## Error flows

- 3e. Data missing: listed.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-02 Built from the ERP's data](../../business-rules/br-f18-02-built-from-erp-data.md)

## Entities

- [E-F18-02 Page](../../data/e-f18-02-page.md)

## Permissions

Marketing.

## Notifications

- None.

## Audit events

Pages generated.

## AI involvement

The AI assistant writes texts.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-03 Pages](../../screens/01-build-the-site/s-f18-03-pages.md)

## Flowchart

See [FL-F18-01 Build the site](../../flows/fl-f18-01-build-the-site.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor M as Marketing
  participant S as Pages
  M->>S: Services, sites
  S-->>M: Generated
  M->>S: Edit
```

## Acceptance criteria

1. **Given** 6 services **when** generated **then** 6 appear.
2. **Given** a price change in the ERP **when** changed **then** the preview updates.
3. **Given** missing data **when** generated **then** it is listed.

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

- [UC-F18-25 Use a sector page template](../06-content-and-search/uc-f18-25-use-a-sector-page-template.md)

## Open questions

None.

---

⬅️ [UC-F18-02 Apply the visual identity](uc-f18-02-apply-the-visual-identity.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-04 Add a contact page that feeds leads](uc-f18-04-add-a-contact-page-that-feeds-leads.md)

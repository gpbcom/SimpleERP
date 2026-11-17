🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-02 Careers](README.md) › 📝 UC-F18-05 Publish a careers page from openings

# 📝 UC-F18-05 Publish a careers page from openings

**Status:** ✅ specified

## Summary

HR publishes a careers page from F9 openings, after checking each offer.

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Goal

Openings visible on the site.

## Trigger

An opening in F9.

## Frequency

Monthly.

## Preconditions

- Openings exist.

## Postconditions

- Success: careers page live.
- Failure: offers refused.

## Main flow

1. HR opens Careers page (S-F18-05).
2. They choose openings.
3. Each offer is checked (BR-F18-07).
4. The page is published with the site.

## Alternative flows

- 2a. Job postings in structured data (UC-F18-26).

## Error flows

- 3e. Discriminating wording: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-07 Job offers checked before posting](../../business-rules/br-f18-07-job-offers-checked.md)
- [BR-F18-09 Candidates informed, data limited](../../business-rules/br-f18-09-candidates-informed-and-data-limited.md)

## Entities

- [E-F18-05 Job posting](../../data/e-f18-05-job-posting.md)

## Permissions

HR.

## Notifications

- HR when published.

## Audit events

Offers published.

## AI involvement

The AI assistant checks wording.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-05 Careers page](../../screens/02-careers/s-f18-05-careers-page.md)

## Flowchart

See [FL-F18-02 Careers](../../flows/fl-f18-02-careers.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor H as HR
  participant S as Careers page
  H->>S: Carer opening
  S->>S: Check offer
  S-->>H: Ready
```

## Acceptance criteria

1. **Given** an offer **when** checked **then** it passes.
2. **Given** "young" in an offer **when** checked **then** it is refused.
3. **Given** published **when** live **then** the opening shows.

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

- [UC-F18-06 Post openings to LinkedIn and Indeed](uc-f18-06-post-openings-to-linkedin-and-indeed.md)

## Open questions

None.

---

⬅️ [UC-F18-04](../01-build-the-site/uc-f18-04-add-a-contact-page-that-feeds-leads.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-06 Post openings to LinkedIn and Indeed](uc-f18-06-post-openings-to-linkedin-and-indeed.md)

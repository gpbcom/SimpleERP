🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-03 Domain and DNS](README.md) › 📝 UC-F18-10 Connect an existing domain

# 📝 UC-F18-10 Connect an existing domain

**Status:** ✅ specified

## Summary

The administrator connects an existing domain by delegation or records, verifies it, and maps the old site's addresses
(UC-F18-22).

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

The site on the company's own domain.

## Trigger

An existing domain.

## Frequency

Rare.

## Preconditions

- Access to the domain.

## Postconditions

- Success: connected and verified.
- Failure: steps to fix.

## Main flow

1. The administrator opens Connect domain (S-F18-10).
2. They choose delegation or records.
3. They follow the steps.
4. SimpleERP verifies.
5. If an old site existed, marketing maps its addresses (UC-F18-22).

## Alternative flows

- 2a. Records only.

## Error flows

- 4e. Not verified: steps shown.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-10 Domains through registrar APIs](../../business-rules/br-f18-10-domains-through-registrar-apis.md)
- [BR-F18-11 DNS changes are planned and checked](../../business-rules/br-f18-11-dns-changes-are-planned.md)
- [BR-F18-16 Every old address redirects](../../business-rules/br-f18-16-every-old-address-redirects.md)

## Entities

- [E-F18-07 Domain](../../data/e-f18-07-domain.md)
- [E-F18-08 DNS record](../../data/e-f18-08-dns-record.md)
- [E-F18-14 Redirect](../../data/e-f18-14-redirect.md)

## Permissions

Administrator.

## Notifications

- The administrator when verified.

## Audit events

Connections.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-10 Connect domain](../../screens/03-domain-and-dns/s-f18-10-connect-domain.md)

## Flowchart

See [FL-F18-03 Domain and DNS](../../flows/fl-f18-03-domain-and-dns.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Connect domain
  A->>S: restaurant.example
  S-->>A: Records to add
  A->>S: Verify
  S-->>A: Verified
```

## Acceptance criteria

1. **Given** records added **when** verified **then** connected.
2. **Given** wrong records **when** verified **then** steps shown.
3. **Given** an old site **when** connected **then** redirects are asked.

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

- [UC-F18-22 Redirect the old site's addresses](uc-f18-22-redirect-the-old-sites-addresses.md)

## Open questions

None.

---

⬅️ [UC-F18-09 Buy or transfer a domain](uc-f18-09-buy-or-transfer-a-domain.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-11 Manage the DNS zone and certificates](uc-f18-11-manage-the-dns-zone-and-certificates.md)

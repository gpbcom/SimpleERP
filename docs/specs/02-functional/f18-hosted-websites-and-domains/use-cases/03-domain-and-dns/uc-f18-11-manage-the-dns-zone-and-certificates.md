🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F18-03 Domain and DNS](README.md) › 📝 UC-F18-11 Manage the DNS zone and certificates

# 📝 UC-F18-11 Manage the DNS zone and certificates

**Status:** ✅ specified

## Summary

The administrator manages the DNS zone and certificates through the provider's API, with each change shown as a plan and
verified.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

DNS and TLS right.

## Trigger

A change needed.

## Frequency

Rare.

## Preconditions

- Domain connected.

## Postconditions

- Success: applied and verified.
- Failure: refused.

## Main flow

1. The administrator opens DNS and certificates (S-F18-11).
2. They see the plan of records (BR-F18-11).
3. They apply.
4. SimpleERP verifies; certificates renew (BR-F18-13).

## Alternative flows

- 2a. The hosting engineer helps.

## Error flows

- 2e. Conflict with mail: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F18-11 DNS changes are planned and checked](../../business-rules/br-f18-11-dns-changes-are-planned.md)
- [BR-F18-13 Certificates renewed early](../../business-rules/br-f18-13-certificates-renewed-early.md)

## Entities

- [E-F18-08 DNS record](../../data/e-f18-08-dns-record.md)
- [E-F18-09 TLS certificate](../../data/e-f18-09-tls-certificate.md)

## Permissions

Administrator; hosting engineer supports.

## Notifications

- On certificate failures.

## Audit events

Changes.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F18-11 DNS and certificates](../../screens/03-domain-and-dns/s-f18-11-dns-and-certificates.md)

## Flowchart

See [FL-F18-03 Domain and DNS](../../flows/fl-f18-03-domain-and-dns.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as DNS
  A->>S: Add record
  S-->>A: Plan
  A->>S: Apply
```

## Acceptance criteria

1. **Given** a plan **when** applied **then** verified.
2. **Given** a conflict **when** planned **then** refused.
3. **Given** a certificate 30 days from expiry **when** checked **then** renewed.

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

- [UC-F18-12 Set mail records SPF, DKIM and DMARC](uc-f18-12-set-mail-records-spf-dkim-and-dmarc.md)

## Open questions

None.

---

⬅️ [UC-F18-10 Connect an existing domain](uc-f18-10-connect-an-existing-domain.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F18-12 Set mail records SPF, DKIM and DMARC](uc-f18-12-set-mail-records-spf-dkim-and-dmarc.md)

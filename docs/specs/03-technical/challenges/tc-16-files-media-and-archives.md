🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🗂️ TC-16 Files, media and archives

# 🗂️ TC-16 Files, media and archives

**Status:** ✅ listed for the technical interviews

## Challenge

Store documents, attachments, recordings, videos, product images, generated sites and the legal archive, with their
retention, rights and, for health practices, certified hosting.

## Raised by

- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md)
- [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [SC09 Health practices](../../08-sectors/sc09-health-practices/README.md)

## Why it is hard

- Media are large and grow quickly.
- Health data needs certified hosting (country pack).
- Retention differs per kind of file and per country.

## Already decided

- [D19](../../06-decisions/foundations/d19-one-database-per-company.md) One database per company
- [D241](../../06-decisions/security-and-compliance/d241-security-frameworks.md) Deployable under security frameworks

## Options to weigh

- Object storage per company with lifecycle rules.
- Encryption per company and per kind of data.
- A separate, certified profile for health data.

## Settled in

- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19f Security ([chapter](../../../technical/security/security.md))
- 19k Backups, recovery and upgrades ([chapter](../../../technical/operations/operations.md))
- Then the technical capabilities: [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md).

## Questions for the interview

- Is health data in the first version's hosted edition?
- What quota per company in the hosted edition?

---

⬅️ [TC-15 Large lists, reports and dashboards](tc-15-large-data-reports-and-lists.md) · ⬆️ [Up](README.md) ·
➡️ [TC-17 Security and compliance profiles](tc-17-security-and-compliance-profiles.md)

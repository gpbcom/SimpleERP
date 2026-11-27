🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🔒 Security

# 🔒 Security

**Status:** ✅ specified

## Requirement

- Remote access from anywhere over HTTPS, with two-factor authentication; an administrator can restrict some roles to
  the office network. See [D37](../06-decisions/security-and-compliance/d37-remote-access.md).
- **Deployable under security frameworks**
  ([D241](../06-decisions/security-and-compliance/d241-security-frameworks.md)), through compliance deployment profiles
  and the evidence each needs:
  - **SecNumCloud** (ANSSI): installable on a SecNumCloud-qualified hosting offer, with every component self-hosted, no
    call to services outside the EU or subject to non-EU laws, administration from the EU, the qualified provider's key
    management, and the logging and retention the qualification requires;
  - **SOC 2 Type II**: controls mapped to the Trust Services Criteria (security, availability, processing integrity,
    confidentiality, privacy), with evidence produced continuously;
  - **ISO/IEC 27001** with 27017 (cloud), 27018 (personal data in the cloud) and 27701 (privacy);
  - **HDS** (French health data hosting) for health practices (SC09);
  - **NIS2** and **DORA** obligations of customers that are essential or financial entities;
  - **GDPR**, the **Cyber Resilience Act** (SimpleERP as a product with digital elements) and the **EU AI Act** (D234);
  - national schemes such as **C5** (Germany) and **ENS** (Spain), and **EUCS** once adopted;
  - **PCI DSS** scope kept minimal: card numbers never stored, only payment providers' tokens.
- **Customers' credentials** in a dedicated vault
  ([D240](../06-decisions/security-and-compliance/d240-credential-vault.md),
  [REQ-T12-08](../03-technical/t12-connectors-and-scrapers/requirements/req-t12-08-credential-vault.md)).

- **Two factors for every user** ([D450](../06-decisions/security-and-compliance/d450-two-factors-for-every-user.md)):
  passkeys preferred, a second factor otherwise; signing in again is required before a link opens a payslip or other
  personal data, a leaver's payslip link included.
- **Vulnerabilities in SimpleERP itself** (the Cyber Resilience Act's duties of the publisher, review R20): a published
  security policy (SECURITY.md) with a private reporting path through GitHub's private vulnerability reporting and
  security advisories; a report that may be a vulnerability never becomes a public USER issue (BR-F25-12); fixes
  released with an advisory and a CVE; actively exploited vulnerabilities and severe incidents reported to the
  authorities as the Cyber Resilience Act requires, its dates to read at build; an acknowledgement within 3
  working days.
- **Health data and the hosted agents** (review R27): namespaces holding health data (SC09) are excluded from the
  support assistant's and the DevOps agents' model access unless the hosting and the whole model path are HDS-certified
  (BR-F20-13, BR-F25-13).

## Measures

- A control matrix per framework, kept in the repository, each control linked to its evidence (configuration,
  test, log, report).
- Software bill of materials, vulnerability management, penetration tests before each major release,
  hardening guides per profile.
- The technical design of these profiles is interviewed at step 19f (Security).

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-055 Health data hosting](../10-country-packs/france/data-protection/cr-fr-055-health-data-hosting.md)

## Open questions

⬜ To be specified.

---

⬅️ [Data isolation](data-isolation.md) · ⬆️ [Up](README.md) · ➡️ [Privacy and GDPR](privacy-gdpr.md)

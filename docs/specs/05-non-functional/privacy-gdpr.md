🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🛂 Privacy and GDPR

# 🛂 Privacy and GDPR

**Status:** ✅ specified

## Requirement

Specified on 2026-11-12 ([D446](../06-decisions/security-and-compliance/d446-privacy-specified.md)).

**Roles (GDPR articles 4, 24, 26 and 28).**

- The company using simple-ERP is the controller of its data, whoever runs it.
- Self-hosted: the company alone; the simple-ERP project and its publisher receive none of its data and are not its
  processors.
- An IT provider hosting client companies (D1) is their processor, under a data processing agreement (GDPR article 28).
- The hosted edition: the publisher is the processor of every hosted company, under its data processing agreement; its
  subprocessors are listed below.
- The publisher is the controller only of its own customer accounts, billing and support contacts.

**The hosted edition's subprocessors**, (Proposed) until they are named at launch
([D440](../06-decisions/vision/d440-local-by-default-outside-by-choice.md)):

| Service | Provider | Region | Data |
|---|---|---|---|
| Hosting, storage, backups | A European cloud, for example Scaleway or OVHcloud (D375) | France, a second EU region for recovery | Everything |
| AI models, when the publisher hosts no model for a feature | Providers of D440's list, per feature | EU processing where offered | Prompts, masked (D417) |
| Email delivery | A European email provider | EU | Addresses and messages |
| Payment of the hosted subscription | A payment provider | EU | Billing contacts |
| Code hosting | GitHub (United States) | - | No customer data: sanitised USER tickets only (D433, D440) |

**Transfers (GDPR chapter V,
[CR-FR-049](../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md)).** None outside the EU in
the hosted edition, except to a provider an administrator chooses for a feature (D82, D440), shown with its country and
its transfer basis (an adequacy decision or standard contractual clauses) before it is switched on.

**Impact assessments (GDPR article 35).** Done by the publisher before launch for the hosted edition, and shipped as
templates for companies to complete before they switch on: meetings and call recording (F4, D449), call scoring and any
evaluation of workers (UC-F4-12), candidate scoring and matching (D234), health data (SC09,
[CR-FR-055](../10-country-packs/france/data-protection/cr-fr-055-health-data-hosting.md)), and the location of field
staff ([CR-FR-054](../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md)).

**Rights ([CR-FR-051](../10-country-packs/france/data-protection/cr-fr-051-access-and-erasure.md)).** Access,
rectification, erasure and portability are handled by the company's administrators: a person's data is found across the
company's stores, exported or erased; erasure reaches the analytics store (REQ-T01-08) and backups as they expire; the
audit trail keeps its entries without the personal data (REQ-T03-03).

**Records and breaches.** A record of processing activities per company, generated from the modules switched on
([CR-FR-048](../10-country-packs/france/data-protection/cr-fr-048-record-of-processing.md)); a breach is notified as
[CR-FR-199](../10-country-packs/france/data-protection/cr-fr-199-personal-data-breach-notification.md) says, and the
hosted edition tells the company without undue delay (GDPR article 33(2)).

**By design ([CR-FR-050](../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md)).** Local AI by
default (D440), personal data masked before any outside model (D417), retention per kind of entity
([Data retention](data-retention.md)), legitimate interest documented
([CR-FR-196](../10-country-packs/france/data-protection/cr-fr-196-legitimate-interest-balancing.md)), candidates' data
([CR-FR-195](../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md)).

## Measures

- (Proposed) A data processing agreement template for IT providers and for the hosted edition, reviewed by a lawyer
  before launch.
- (Proposed) The subprocessor list published on the hosted edition's site, a change announced 30 days before it applies.
- Impact-assessment templates shipped with the features listed above.
- The record of processing and the log of rights requests kept per company (F1).

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-207 Call recording at work kept proportionate](../10-country-packs/france/data-protection/cr-fr-207-call-recording-proportionate.md)

## Open questions

- (Proposed) Whether the publisher appoints a data protection officer (GDPR article 37), decided before the hosted
  edition opens.

---

⬅️ [Security](security.md) · ⬆️ [Up](README.md) · ➡️ [Data retention](data-retention.md)

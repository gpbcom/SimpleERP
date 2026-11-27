🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💼 [SC03 Services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC03-18 Certificates lapse without their surveillance audit

# 📏 BR-SC03-18 Certificates lapse without their surveillance audit

**Status:** 🔄 waiting for the owner

## Statement

A certificate stays valid only while its surveillance audits are done by their due dates; on the day after a due date
without an audit, the certificate becomes Lapsed and the client is told. A lapsed certificate returns to Issued only
after a catch-up audit passes.

## Why

A certificate that is not watched loses its meaning for those who rely on it, and the body loses its accreditation if it
lets it continue. The owner asked for certification bodies
([D547](../../../06-decisions/sectors/d547-benchmark-gaps-sc03-services.md)).

## Examples

| Case | Result |
|---|---|
| Issued 2026-02-01, surveillance due 2027-01-31, audit done 2027-01-20 | stays Issued |
| Audit not done on 2027-02-01 | Lapsed |
| Catch-up audit passed 2027-03-10 | Issued again |
| Three years pass | Expired, recertification needed |

## Applies to

- [UC-SC03-18](../use-cases/06-staffing-agencies-and-certification/uc-sc03-18-run-certification-audits.md)
- [E-SC03-19 Certificate](../data/e-sc03-19-certificate.md)
- [E-SC03-11 Skill](../data/e-sc03-11-skill.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-255 Certification body accreditation](../../../10-country-packs/france/professional-firms/cr-fr-255-certification-accreditation.md)

## Exceptions

None.

## Configurable

The reminder before a due date (60 days by default), by the engagement manager.

## Open questions

None.

---

⬅️ [BR-SC03-17](br-sc03-17-media-are-rebilled-at-cost-plus-the-agreed-fee.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC03-19 Library answers carry their review date](br-sc03-19-library-answers-carry-their-review-date.md)

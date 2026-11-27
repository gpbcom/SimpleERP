🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-03 Certificates are given to the customer

# 📏 BR-SC19-03 Certificates are given to the customer

**Status:** 🔄 waiting for the owner

## Statement

Every legal check-up gives the customer a certificate, whatever its result, signed by a qualified technician and sent
within the delay of the pack. A check-up with a missing reading is not closed.

## Why

The certificate is the customer's proof that the check-up was done, and the company's proof of its service
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Compliant result | certificate sent |
| Not compliant result | certificate sent with the defects, the dispatcher is told |
| Reading missing | not closed |
| Customer absent | sent without signature, absence noted |
| Technician without the qualification | refused |

## Applies to

- [UC-SC19-03](../use-cases/01-maintenance-contracts/uc-sc19-03-record-legal-check-ups.md)
- [E-SC19-03 Check-up certificate](../data/e-sc19-03-check-up-certificate.md)
- [E-SC19-02 Planned visit](../data/e-sc19-02-planned-visit.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

The delay to send the certificate and the check-up forms, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-02](br-sc19-02-visits-are-planned-before-the-legal-due-date.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-04](br-sc19-04-renewals-follow-the-notice-and-index-clauses.md)

🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-12 The advance needs the customer's consent

# 📏 BR-SC19-12 The advance needs the customer's consent

**Status:** ✅ specified

## Statement

A claim for the immediate advance is sent only for a household that consented and is enrolled, and the consent is kept
with its date and can be withdrawn. A disputed claim leaves the household with an invoice for the full amount; a claim
the household does not answer within 48 hours is validated automatically.

## Why

Without the consent the claim is unfounded and the household may be charged twice
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rule is
[CR-FR-104 Immediate advance of the tax credit](../../../10-country-packs/france/tax-and-vat/cr-fr-104-immediate-advance-of-tax-credit.md):
the household activates its account, has 48 hours to check each request, then it is validated automatically; URSSAF pays
the whole service to the company and debits the household for its remainder.

## Examples

| Case | Result |
|---|---|
| Consent and enrolment | the claim is sent |
| No consent | refused, invoice in full |
| Household disputes | claim withdrawn, invoice in full |
| No answer within 48 hours | validated automatically |
| Rejected for a wrong amount | corrected and sent again |
| Consent withdrawn | later claims are not sent |

## Applies to

- [UC-SC19-12](../use-cases/03-home-services-tax-credit/uc-sc19-12-use-the-immediate-advance.md)
- [E-SC04-13](../../sc04-home-care/data/e-sc04-13-immediate-advance-claim.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)

## Exceptions

None.

## Configurable

No: the 48 hours to check and the automatic validation come from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-11 Certificates list paid amounts only](br-sc19-11-certificates-list-paid-amounts-only.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-13 Works start after the grant file is filed](br-sc19-13-works-start-after-the-grant-file-is-filed.md)

🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-08 Payments meet the legal payment term

# 📏 BR-SC20-08 Payments meet the legal payment term

**Status:** ✅ specified

## Statement

Each invoice of a public contract is paid within the legal payment term counted from its receipt, and the deadline is
shown from the receipt. A payment after the term shows the late-payment interest and the fixed indemnity due.

## Why

Late payment of suppliers by a public body is penalised automatically
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The France-pack rule is
[CR-FR-091 Public contracts: payment period and Chorus Pro](../../../10-country-packs/france/invoicing/cr-fr-091-public-contracts-payment-and-chorus-pro.md):
30 days for the State, public bodies and local authorities (50 days for health establishments), with late-payment
interest at the ECB rate plus 8 points and a 40 EUR recovery indemnity.

## Examples

| Case | Result |
|---|---|
| Invoice received 1 March | deadline 30 days later |
| Paid on day 36 | interest and indemnity shown |
| Invoice rejected as incorrect | supplier told, clock restarts with the right invoice |
| Amendment within the limit | recorded with its approval |
| Amendment above the limit | needs the council's approval |

## Applies to

- [UC-SC20-08](../use-cases/02-public-procurement/uc-sc20-08-follow-the-public-contract.md)
- [E-SC20-07 Public contract](../data/e-sc20-07-public-contract.md)
- [E-SC20-07 Public contract](../data/e-sc20-07-public-contract.md)
- [E-SC20-03 Payment order](../data/e-sc20-03-payment-order.md)

## Exceptions

None.

## Configurable

The term and the rates, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC20-07 Award follows the published criteria](br-sc20-07-award-follows-the-published-criteria.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC20-09 Requests are acknowledged with a deadline](br-sc20-09-requests-are-acknowledged-with-a-deadline.md)

🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-09 Requests are acknowledged with a deadline

# 📏 BR-SC20-09 Requests are acknowledged with a deadline

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

Every request is acknowledged with its date of receipt and its deadline as soon as it arrives. An incomplete request is
returned with what is missing and a delay to complete it, and is not answered as if complete. A request near its
deadline is flagged.

## Why

A request without acknowledgement leaves the citizen without a deadline and may make silence mean refusal
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). (⚖️ lawyer review before launch, D574) The
France-pack rule is still to write: to read the acknowledgement, the incomplete request and the effect of silence (Code
des relations entre le public et l'administration L112-3, L114-5, L231-1 and following).

## Examples

| Case | Result |
|---|---|
| Complete request | acknowledged at once with the deadline |
| Missing document | Incomplete, item and delay named |
| Request for another authority | passed on, citizen told |
| Deadline in two days | flagged |
| Citizen with no way to be answered | cannot be sent |

## Applies to

- [UC-SC20-09](../use-cases/03-citizen-services/uc-sc20-09-receive-a-citizens-request.md)
- [E-SC20-08 Citizen request](../data/e-sc20-08-citizen-request.md)
- [E-SC20-08 Citizen request](../data/e-sc20-08-citizen-request.md)

## Exceptions

None.

## Configurable

The request types, their documents and their deadlines, set by the body.

## Open questions

None.

---

⬅️ [BR-SC20-08 Payments meet the legal payment term](br-sc20-08-payments-meet-the-legal-payment-term.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC20-10 Bookings follow the council's rates](br-sc20-10-bookings-follow-the-councils-rates.md)

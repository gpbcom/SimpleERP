🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-11 Payments go to the public treasury's channel

# 📏 BR-SC20-11 Payments go to the public treasury's channel

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

An online payment of a public bill is taken only through the public treasury's channel, never on the body's own account,
and is matched to its title. A failed payment leaves the title open.

## Why

Public money is collected by the public accountant and a payment elsewhere is irregular
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). (⚖️ lawyer review before launch, D574) The
France-pack rule is still to write: to read the public accountant's sole competence to collect public money (décret n°
2012-1246, GBCP) and the DGFiP's online payment service (PayFiP).

## Examples

| Case | Result |
|---|---|
| Card payment through the channel | title settled |
| Failed payment | title stays open |
| Payment for an unknown title | kept in a list to match |
| Counter payment | recorded and confirmed by the treasury |
| Second payment of the same bill | refused |

## Applies to

- [UC-SC20-11](../use-cases/03-citizen-services/uc-sc20-11-take-online-payments.md)
- [E-SC20-03 Payment order](../data/e-sc20-03-payment-order.md)

## Exceptions

None.

## Configurable

The payment methods offered, set by the finance officer.

## Open questions

None.

---

⬅️ [BR-SC20-10 Bookings follow the council's rates](br-sc20-10-bookings-follow-the-councils-rates.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC20-12](br-sc20-12-decisions-are-published-to-become-enforceable.md)

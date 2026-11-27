🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC16-16 Unused balances are refundable after the event

# 📏 BR-SC16-16 Unused balances are refundable after the event

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

The unused balance of a cashless account is refundable to the visitor after the event, in full and once, until the
deadline set for the event. Money is never debited from an account that is Closed, Refunded or Expired.

## Why

Money held for visitors belongs to them until they spend it, and keeping it without a way to get it back is a breach of
trust and of the rules on prepaid instruments. The owner asked for cashless payments
([D560](../../../06-decisions/sectors/d560-benchmark-gaps-sc16-events-and-culture.md)). (⚖️ lawyer review before launch, D574) The France-pack
rule is still to write: to read the Code monétaire et financier on electronic money and the limited-network exemption
(L525-1 to L525-6) and any limit on refund fees.

## Examples

| Case | Result |
|---|---|
| Loaded 20.00 EUR and spent 12.50 EUR | 7.50 EUR refundable |
| Refund requested before the deadline | paid once |
| Refund requested twice | second refused |
| Purchase on a Closed account | refused |
| No refund request by the deadline | the account becomes Expired under the pack's rule |

## Applies to

- [UC-SC16-21](../use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-21-run-cashless-payments-at-a-festival.md)
- [E-SC16-19 Cashless account](../data/e-sc16-19-cashless-account.md)
- [E-SC16-13 Event till](../data/e-sc16-13-event-till.md)

## Exceptions

None.

## Configurable

The maximum balance, the refund deadline and any refund fee within the limit of the country pack, by the event producer.

## Open questions

None.

---

⬅️ [BR-SC16-15 Attendees contacted with consent](br-sc16-15-attendees-contacted-with-consent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC16-17 Box-office figures are reported to the CNC](br-sc16-17-box-office-figures-are-reported-to-the-cnc.md)

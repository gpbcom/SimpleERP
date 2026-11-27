🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
💳 [Payments](README.md) › ⚖️ CR-FR-289 Closed-loop payment wristbands

# ⚖️ CR-FR-289 Closed-loop payment wristbands

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

Only electronic-money institutions and credit institutions issue electronic money as a business
([Code monétaire et financier, art. L525-1 and
L525-3](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000027006283), read 2026-11-27);
by exception, a business may issue and manage it to buy goods or services only in its own premises, or under a
commercial agreement in a limited network of acceptors or for a limited range of goods or services, on condition that
the loading capacity of the medium does not exceed an amount set by decree; it is then outside the rules on
electronic-money issuers but stays under the Banque de France's oversight (L525-5); once the electronic money in
circulation exceeds 1 million EUR, it declares itself to the ACPR and updates the declaration each year (L525-6)
([Code monétaire et financier, art. L525-5 and
L525-6](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000027006283), read 2026-11-27).
Cash loaded follows [CR-FR-022](cr-fr-022-cash-payment-limit.md); the VAT of money loaded and spent follows the voucher
rule of [CR-FR-013](../tax-and-vat/cr-fr-013-vouchers-vat.md).

## Values

- A wristband spent only at the stands of the event, or of the organiser's network under its agreement: the
  limited-network exception of L525-5, within the decree's loading cap.
- Above 1 million EUR in circulation: declaration to the ACPR, which may answer that the conditions are not met; silence
  means approval; yearly update; three months to comply or ask for an approval (L525-6).
- Spendable at merchants outside that network: electronic money, issued only by an approved institution (L525-1, L525-3).
- (⚖️ lawyer review before launch, D574) The decree's maximum loading capacity, and the refund of an unused balance and
  its fee for a wristband under the exception, are not in the articles read.
- SimpleERP enforces: an event wallet is limited to the event's network and to the loading cap, and money in
  circulation is totalled against the 1 million EUR threshold.

## Legal references

- [Code monétaire et financier, art. L525-1 to L525-7](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000027006283),
  read 2026-11-27.

## Effective dates

L525-1, L525-3, L525-5 and L525-6 in their version since 2024-10-18 (ordonnance n° 2024-936) (texts above, read
2026-11-27).

## Enforced by

- [UC-SC16-21 Run cashless payments at a festival](../../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-21-run-cashless-payments-at-a-festival.md)

## When the law changes

Watched in the law corpus: Code monétaire et financier L525-1 to L525-7 and the decree on the loading cap. A change flags
this rule and warns the administrators; the corrected rule ships in a pack update (D294).

## Penalty

None stated in the articles read; issuing electronic money outside the exception without approval is forbidden
(L525-3).

## Exceptions

Special dematerialised payment titles listed by order (meal vouchers and similar) are not electronic money (L525-4).

## Open questions

None: the law was read on 2026-11-27; the loading cap and the refund are a lawyer item above.

---

⬅️ [CR-FR-288 Furnished tourist rentals](../real-estate/cr-fr-288-furnished-tourist-rentals.md) · ⬆️ [Up](README.md) · ➡️ [CR-FR-290 Cosmetic products used and sold](../products/cr-fr-290-cosmetic-products.md)

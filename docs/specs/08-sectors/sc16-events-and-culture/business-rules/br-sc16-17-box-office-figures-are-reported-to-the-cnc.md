🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC16-17 Box-office figures are reported to the CNC

# 📏 BR-SC16-17 Box-office figures are reported to the CNC

**Status:** ✅ specified

## Statement

Every screening that has been shown has its admissions and receipts closed and reported to the national film centre
each week through Cinedi, within 5 days after the end of the cinema week (Wednesday to Tuesday), one slip per film,
version and screen for all its screenings of the week; the tax is declared monthly. A report is not sent while a shown
screening has no figures. Admissions are recorded in a computerised ticketing system approved by the national film
centre, whose delivery and installation are declared to it: the cinema sells no ticket until the company has recorded
the CNC approval number of its ticketing system and the date it declared the delivery and installation to the centre
(Code du cinéma et de l'image animée L212-32, [CR-FR-248](../../../10-country-packs/france/events/cr-fr-248-cinema-box-office.md); the owner's choice, [D575](../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md), point 13). The tax is due at each collection of an admission price,
and a part whose total stays under its small-amount threshold is not paid.

## Why

A late or incomplete report brings penalties and the support the cinema receives depends on it. The owner asked for
cinemas ([D560](../../../06-decisions/sectors/d560-benchmark-gaps-sc16-events-and-culture.md)). The
France-pack rule is [CR-FR-248 Cinema box-office reporting and tax](../../../10-country-packs/france/events/cr-fr-248-cinema-box-office.md):
- the weekly declaration of the receipts of each programme is sent electronically to the national film centre and to
  the distributors, and a computerised ticketing system must be approved by the centre, its delivery and installation
  declared to it (Code du cinéma et de l'image animée L212-32 3°, 5° and 6°);
- the cinema operator owes a tax on the price paid for each admission, 10.72 % of the base plus 0.232 % of the base less
  that first part (5 % instead of 10.72 % in overseas collectivities, CIBS L452-5 and L452-8), due at each collection
  of an admission price (L452-9);
- the first part is not paid when its total over the period the decree sets (3 to 6 weeks) is 80 EUR or less, or when
  the operator holds a single screening in a week; the second part is not paid when its yearly total is 30 EUR or less
  (L452-11).

## Examples

| Case | Result |
|---|---|
| Screening shown with 96 admissions | reported with its receipts |
| Shown screening without figures | the report is held |
| Cancelled screening | no admissions reported, tickets refunded |
| Private session | reported in its own category |
| Week of Wednesday 11 to Tuesday 17 November | one slip per film, version and screen, sent by 22 November |
| Report after the date | flagged late |
| No CNC approval number recorded for the cinema | no ticket is sold, at the box office or online |
| Approval number recorded, delivery and installation not declared | no ticket is sold |
| Both recorded | tickets are sold |
| Ticket of 8.00 EUR collected on 14 November | the tax is due for 14 November |
| First part of the tax totals 72.00 EUR over the decree's period | not paid |
| Second part of the tax totals 24.00 EUR for the year | not paid |

## Applies to

- [UC-SC16-22](../use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md)
- [E-SC16-20 Screening](../data/e-sc16-20-screening.md)
- [E-SC16-07 Ticket order](../data/e-sc16-07-ticket-order.md)
- France-pack rule:
  [CR-FR-248 Cinema box-office reporting and tax](../../../10-country-packs/france/events/cr-fr-248-cinema-box-office.md)

## Exceptions

None.

## Configurable

The reporting period and the distributors' shares by film, by the owner within the pack's limits; the CNC approval
number and the declaration date of the delivery and installation, by the company on its cinema
([E-SC16-03 Venue room](../data/e-sc16-03-venue-room.md)), never skipped; the tax rates, the
small-amount thresholds and the decree's period, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC16-16](br-sc16-16-unused-balances-are-refundable-after-the-event.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC16-18 Each show is settled per its contract](br-sc16-18-each-show-is-settled-per-its-contract.md)

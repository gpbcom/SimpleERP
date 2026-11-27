🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎭 [SC16 Events and culture](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC16-18 Each show is settled per its contract

# 📏 BR-SC16-18 Each show is settled per its contract

**Status:** ✅ specified

## Statement

A date is settled on its contract terms: the venue pays the higher of the guarantee and the share of the net receipts
after the costs the contract allows, unless the contract says the share is added to the guarantee. A date is not settled
while a figure is missing or a performer is not declared.

## Why

A settlement that does not follow the contract starts a dispute with the venue, and an undeclared performer is a legal
risk. The owner asked for touring productions
([D560](../../../06-decisions/sectors/d560-benchmark-gaps-sc16-events-and-culture.md)). No France-pack rule sets the
settlement, which follows the contract; the performers are declared before the show
([CR-FR-037](../../../10-country-packs/france/labour/cr-fr-037-dpae-before-the-first-day.md), or
[CR-FR-178](../../../10-country-packs/france/events/cr-fr-178-occasional-organiser-guso.md) for an occasional organiser).

## Examples

| Case | Result |
|---|---|
| Guarantee 6,000, 70 percent over 2,000 of costs, net 8,000 | share 4,200, the guarantee 6,000 applies |
| Same terms, net 12,000 | share 7,000, which is paid |
| Guarantee plus share | both are added |
| Receipts missing | the date stays Played |
| Performer not declared | no settlement |

## Applies to

- [UC-SC16-23](../use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-23-run-a-tour.md)
- [E-SC16-21 Tour date](../data/e-sc16-21-tour-date.md)
- [E-SC16-04 Artist contract](../data/e-sc16-04-artist-contract.md)

## Exceptions

A date cancelled under the contract's cancellation clause is settled on the clause.

## Configurable

The form of the terms (higher of, or added) per contract, by the event producer.

## Open questions

None.

---

⬅️ [BR-SC16-17 Box-office figures are reported to the CNC](br-sc16-17-box-office-figures-are-reported-to-the-cnc.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC16-19](br-sc16-19-images-are-sold-only-with-the-models-release.md)

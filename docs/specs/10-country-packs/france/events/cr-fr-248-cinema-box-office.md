🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) › 🎭 [Events](README.md) ›
⚖️ CR-FR-248 Cinema box-office reporting and tax

# ⚖️ CR-FR-248 Cinema box-office reporting and tax

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) A cinema reports its admissions and receipts per screening to the national film centre by the transmission of
its ticketing data, and a special additional tax is added to the ticket price, declared by the cinema and used to
support film production. This tax is not the show ticket tax of live performances
([CR-FR-177](cr-fr-177-show-ticket-tax.md)).

## Values

- (Proposed) Report per screening, frequency to read.
- (Proposed) Rate of the tax kept as data.
- (Proposed) Distributor's share of the net receipts under the rental terms.
- (Proposed) SimpleERP enforces: box-office figures are reported to the CNC.
- Read in the
  [CNC page on the TSA](https://www.cnc.fr/cinema/etudes-et-rapports/la-taxe-sur-les-entrees-en-salles-de-spectacles-cinematographiques-tsa_211700)
  (publication dated 5 March 2007); the declaration frequency and procedure are not on the page, and the rate may have
  changed since 2007:
- Read: single rate of 10.72 % of the ticket price, declared per establishment and not per screen.
- Read: since 1 January 2007 the CNC collects the tax and receives, registers and checks the declarations (before: the
  tax administration); article 104 of law 2006-1771 of 30 December 2006.

## Legal references

- Law to read: cinema box-office reporting and the additional tax (not read yet).

## Effective dates

(Proposed) To read.

## Enforced by

- [BR-SC16-17 Box-office figures are reported to the CNC](../../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md)
- [UC-SC16-22 Run a cinema](../../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md)

## When the law changes

Watched in the law corpus: Cinema reporting and tax. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None stated.

## Open questions

The law on cinema box-office reporting and the additional tax is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-247 Medical device UDI traceability](../products/cr-fr-247-medical-device-udi.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-249 Harvest and stock declarations](../agriculture/cr-fr-249-vineyard-declarations.md)

🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) › 🎭 [Events](README.md) ›
⚖️ CR-FR-248 Cinema box-office reporting and tax

# ⚖️ CR-FR-248 Cinema box-office reporting and tax

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A cinema gives each spectator an admission ticket, or records the admission in a computerised system, before entry;
keeps the receipts of each programme; and sends the national film centre (CNC), at the end of each cinema week and
electronically, a declaration of the receipts of each programme, also sent to the distributors
([Code du cinéma et de l'image animée, art. L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240), read 2026-11-27). Through Cinedi the declaration is due within
5 days after the end of the cinema week (Wednesday to Tuesday), one slip per film, version and screen, and the tax is
declared monthly ([CNC, Cinedi](https://www.cnc.fr/professionnels/demarche/cinedi--transmission-des-declarations-de-recettes-des-exploitants-au-cnc-et-aux-distributeurs_2612893), read 2026-11-27). A tax on cinema screenings is due by the cinema operator on the
price paid for each admission ([Code des impositions sur les biens et services, art. L452-6 and L452-10](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048625998/), read
2026-11-27). This tax is not the show ticket tax of live performances ([CR-FR-177](cr-fr-177-show-ticket-tax.md)).

## Values

- Weekly receipts declaration per programme, sent electronically to the CNC and to the distributors (L212-32 3°)
  ([Code du cinéma et de l'image animée, art. L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240), read 2026-11-27); through Cinedi, per film, version and
  screen, within 5 days; tax declaration monthly ([CNC, Cinedi](https://www.cnc.fr/professionnels/demarche/cinedi--transmission-des-declarations-de-recettes-des-exploitants-au-cnc-et-aux-distributeurs_2612893), read 2026-11-27).
- A computerised ticketing system must be approved (homologated) by the CNC against its specifications, and its
  delivery and installation are declared to the CNC (L212-32 5° and 6°)
  ([Code du cinéma et de l'image animée, art. L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240), read 2026-11-27).
- Receipt records kept as tax documents, under Livre des procédures fiscales L102 B I (L212-32 2°)
  ([Code du cinéma et de l'image animée, art. L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240), read 2026-11-27).
- Tax: 10.72 % of the admission price plus VAT, plus 0.232 % of the admission price less that first part (L452-5); the
  first rate is 5 % in the overseas collectivities (L452-8); due at each collection of an admission price (L452-9)
  ([CIBS, art. L452-5, L452-8 and L452-9](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048625998/), read 2026-11-27).
- Not paid: the first part when its total over a period of 3 to 6 weeks set by decree is 80 EUR or less, or when the
  operator holds a single screening in a week; the second part when its yearly total is 30 EUR or less (L452-11)
  ([CIBS, art. L452-11](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048625998/), read 2026-11-27).
- (⚖️ lawyer review before launch, D574) Distributor's share of the net receipts under the rental terms: set by the
  contracts and texts not read.
- SimpleERP enforces: box-office figures are reported to the CNC.

## Legal references

- [Code du cinéma et de l'image animée, art. L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240) (in force since 2016-12-24), read 2026-11-27.
- [Code des impositions sur les biens et services, art. L452-1 to L452-13](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048625998/), read 2026-11-27.
- [CNC, Cinedi](https://www.cnc.fr/professionnels/demarche/cinedi--transmission-des-declarations-de-recettes-des-exploitants-au-cnc-et-aux-distributeurs_2612893), read 2026-11-27.

## Effective dates

Code du cinéma L212-32 in its current version since 2016-12-24 ([Code du cinéma et de l'image animée, art.
L212-32](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688240), read 2026-11-27); CIBS L452-1 in force since 2024-01-01; the rate article L452-5 in its current version
since 2025-02-16 (loi n° 2025-127, applied from 2025-01-01); L452-2, L452-9-1 and L452-11 since 2025-03-01
([CIBS, art. L452-1 to L452-13](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048625998/), read 2026-11-27).

## Enforced by

- [BR-SC16-17 Box-office figures are reported to the CNC](../../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md)
- [UC-SC16-22 Run a cinema](../../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md)

## When the law changes

Watched in the law corpus: Cinema reporting and tax. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

(⚖️ lawyer review before launch, D574) Not read: CIBS L452-1 to L452-13 and Code du cinéma L212-32 state none; the
sanctions of the Code du cinéma for a missing or wrong declaration are not read.

## Exceptions

None stated.

## Open questions

None: the Code du cinéma and the CIBS were read on 2026-11-27; the distributor's share and the penalty are lawyer items.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-247 Medical device UDI traceability](../products/cr-fr-247-medical-device-udi.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-249 Harvest and stock declarations](../agriculture/cr-fr-249-vineyard-declarations.md)

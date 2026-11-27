🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🩺 [Health practice](README.md) › ⚖️ CR-FR-279 Veterinary medicines dispensing register

# ⚖️ CR-FR-279 Veterinary medicines dispensing register

**Status:** ✅ specified

## Statement

A vet or a pharmacist who dispenses prescribed veterinary medicines records each delivery at once, in a register or a
system that allows no change once a record is validated, kept 10 years and printable on demand for the inspectors, and
compares at least once a year the medicines in and out with the stock
([Code de la santé publique, art. R5141-112](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365266), read
2026-11-27); the prescription itself follows R5141-111
([art. R5141-111](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032256759), read 2026-11-27). EU law asks
every retailer of prescription veterinary medicines for detailed records of each transaction and a yearly stock audit,
available 5 years ([Regulation (EU) 2019/6, art.
103](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019R0006), read 2026-11-27).

## Values

- Register line (R5141-112 I, kept as data): 1° a sequential number; 2° the name and address of the animals' keeper,
  or "usage professionnel"; 3° the name or formula of the medicine; 4° the quantity dispensed; 5° the prescriber; 6°
  the date of delivery; 7° the manufacturing batch number; 8° "médicaments remis par..." with the intermediary, when one
  hands them over ([Code de la santé publique, art.
  R5141-112](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365266), read 2026-11-27).
- Records: no change after validation; duplicated on two separate media; printable, sorted by keeper, by medicine and by
  date; kept 10 years; the delivery date, number and quantity also written on the prescription given to the keeper
  (R5141-112 I).
- The vet is exempt from the register when its prescriptions are numbered and their duplicates kept the same way, with
  the delivery date, quantity and batch written on the duplicate (R5141-112 I).
- Yearly comparison of medicines in and out with the stock, any difference written in a report (R5141-112 I); EU: yearly
  audit, records and audit available 5 years (Regulation (EU) 2019/6, art. 103(3) and (5)).
- EU record of each prescription-medicine transaction (art. 103(3)): date; product with form and strength; batch;
  quantity received or supplied; supplier or recipient; prescribing vet and, where appropriate, a copy of the
  prescription; marketing authorisation number
  ([Regulation (EU) 2019/6, art. 103](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019R0006), read
  2026-11-27).
- Prescription valid at most 1 year, 1 month for critically important antibiotics; no repeat dispensing for those
  (R5141-111 II and III) ([art. R5141-111](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032256759),
  read 2026-11-27).
- SimpleERP enforces: dispensed medicines enter the register with the animal, the medicine, the batch, the quantity,
  the date and the vet; the register is kept 10 years.

## Legal references

- [Code de la santé publique, art. R5141-111](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032256759) and
  [R5141-112](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365266), read 2026-11-27.
- [Regulation (EU) 2019/6 on veterinary medicinal products, art. 103 and
  160](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019R0006), read 2026-11-27.

## Effective dates

R5141-112 in its version since 2021-11-26 (décret n° 2021-1519); R5141-111 since 2016-04-01; Regulation (EU) 2019/6
applies since 2022-01-28 (texts above, read 2026-11-27).

## Enforced by

- [BR-SC09-18 Dispensed medicines enter the register](../../../08-sectors/sc09-health-practices/business-rules/br-sc09-18-dispensed-medicines-enter-the-register.md)
- [UC-SC09-23 Run a veterinary practice](../../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-23-run-a-veterinary-practice.md)

## When the law changes

Watched in the law corpus: Code de la santé publique R5141-111, R5141-112; Regulation (EU) 2019/6, art. 103. A change
flags this rule and warns the administrators; the corrected rule ships in a pack update (D294).

## Penalty

None stated in the articles read.

## Exceptions

Numbered prescriptions with kept duplicates replace the register for the vet (R5141-112 I).

## Open questions

None: the texts were read on 2026-11-27.

---

⬅️ [CR-FR-278 Refurbished products](../products/cr-fr-278-refurbished-products.md) · ⬆️ [Up](README.md) · ➡️ [CR-FR-280 Personal data shared inside a group](../data-protection/cr-fr-280-personal-data-shared-inside-a-group.md)

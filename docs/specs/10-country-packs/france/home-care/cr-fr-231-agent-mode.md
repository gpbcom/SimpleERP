🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏠 [Home care](README.md) › ⚖️ CR-FR-231 Agent mode for family employers

# ⚖️ CR-FR-231 Agent mode for family employers

**Status:** ✅ specified

## Statement

In agent mode the family stays the legal employer: the contract, the payslip and the declarations name the
family, and the provider acts under a written mandate and invoices only its fee. The provider's personal-services
declaration or approval is needed ([servicesalapersonne.gouv.fr: using personal services](https://www.servicesalapersonne.gouv.fr/je-suis-un-particulier/particuliers-comment-recourir-aux-services-la-personne), updated 2026-04-10,
read 2026-11-27; arrêté du 24 novembre 2023, annex).

## Values

- Written mandate: every mandate service gives rise to a written mandate contract with the individual employer, which
  states the cost of the mandate and the VAT rate ([arrêté du 24 novembre 2023, annex, point 48](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776), in force since 2024-01-01, read 2026-11-27).
- The family named as employer on every document: the client is the employer, signs the contract and pays the
  salary; the provider draws up the payslips and the social declarations on the client's behalf ([servicesalapersonne.gouv.fr](https://www.servicesalapersonne.gouv.fr/je-suis-un-particulier/particuliers-comment-recourir-aux-services-la-personne),
  read 2026-11-27). Read: the first page of the mandate contract states that
  the consumer is the employer of the person who works at home, ending the mandate does not end the employment
  contract, and the provider holds a model employment contract between the worker and the employer ([arrêté du 24 novembre 2023, annex, point 48](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776), points 46,
  48 and 67, read 2026-11-27); payslips and declarations are not named there.
- The provider invoices its fee only: the client pays the salary, and the provider works for a fee under the mandate
  ([servicesalapersonne.gouv.fr](https://www.servicesalapersonne.gouv.fr/je-suis-un-particulier/particuliers-comment-recourir-aux-services-la-personne), read 2026-11-27). Read: the welcome booklet lists the price of mandate services, the
  contract states the cost of the mandate, and the invoice model follows Code du travail D7233-1 ([arrêté du 24 novembre 2023, annex, point 48](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776), points 46, 48
  and 67, read 2026-11-27); that the invoice holds the fee only is not stated.
- SimpleERP enforces: in agent mode the family is the employer.
- Read on Legifrance,
  [Code du travail L7232-6](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000006189974/)
  and [L7232-1 to L7232-1-2](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000006189973/)
  (read 15 November 2026); the words "agent mode" and "mandate" are not in these articles, so the written mandate, the
  family staying the legal employer and the provider invoicing only its fee are not read:
- Read: L7232-6, a personal-services provider may place workers with individual employers and, on their behalf, do the
  administrative formalities and the social and tax declarations linked to the employment; recruit workers to make them
  available, for a fee, to individuals (an association's activity is then deemed non-profit under L8231-1 and L8241-1);
  and supply services to individuals.
- Read: L7232-1, an approval from the competent authority, on quality criteria, is needed for child care under an age
  limit set by order and for the activities of 2 of L7231-1 (except those listed by decree that do not endanger people).
- Read: L7232-1-1, to benefit from the advantages of L7233-2 (1 and 2) and L7233-3, a provider that works exclusively in
  personal services declares its activity to the competent authority.
- Read: L7232-1-2, exceptions to the exclusive-activity condition (for example associations intermediaires, communes,
  micro-entrepreneurs and firms under 11 staff whose side activities stay within a share set by decree, at most 30 %).
- Read: L7232-1 and L7232-6 in force since 25 July 2010 (law 2010-853); L7232-1-1 and L7232-1-2 since 1 January 2025
  (law 2023-1322 of 29 December 2023); no penalty is on the page.

## Legal references

- Code du travail L7232-1 to L7232-1-2, L7232-6; arrêté du 24 novembre 2023 (approval specifications), annex.

## Effective dates

L7232-1 and L7232-6 since 2010-07-25, L7232-1-1 and L7232-1-2 since 2025-01-01 ([Code du travail](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000006189973/));
the approval specifications with the written mandate since 2024-01-01 ([arrêté du 24 novembre 2023, annex, point 48](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776), art. 5, read 2026-11-27).

## Enforced by

- [BR-SC04-18 In agent mode the family is the employer](../../../08-sectors/sc04-home-care/business-rules/br-sc04-18-in-agent-mode-the-family-is-the-employer.md)
- [UC-SC04-18 Run the agent mode for family employers](../../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-18-run-the-agent-mode-for-family-employers.md)

## When the law changes

Watched in the law corpus: Agent mode. A change flags this rule and warns the administrators; the corrected rule ships
in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None stated.

## Open questions

None, read on 2026-11-27.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-230 CESU vouchers](cr-fr-230-cesu-vouchers.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-232 Childcare at home and the PAJE aid](cr-fr-232-childcare-paje.md)
